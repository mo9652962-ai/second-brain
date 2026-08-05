"""
Hermes 轨迹标注器 + 清洗器 — OpenForgeRL 数据管线 P1/P2

参考 OpenForgeRL (2607.21557): 轨迹需标注成功/失败才能作为 RL 训练数据
参考 OSReward (2607.22471): 评估器可靠性——标注规则要防宽松偏见

用法:
  uv run python scripts/label_traces.py --days 7
  uv run python scripts/label_traces.py --days 30 --out traces/labeled.jsonl
  uv run python scripts/label_traces.py --days 7 --verbose   # 打印抽样标注

输出:
  traces/labeled_YYYYMMDD.jsonl  — 标注+清洗后的轨迹
  traces/label_stats.md          — 统计报告
"""
import sqlite3
import json
import argparse
import re
from pathlib import Path
from datetime import datetime, timedelta

DB = Path.home() / "AppData/Local/hermes/state.db"

# ============ 清洗阈值 ============
MAX_TOKENS = 200_000      # 超长轨迹（上下文爆炸；200k 内可训练）
MAX_MESSAGES = 2000       # 消息过多（长期桌面会话 13100 消息该丢，500-2000 可训练）
MIN_MESSAGES = 3          # 过短（无训练价值）
ERR_KEYWORDS = [
    "traceback", "keyerror", "nameerror", "assertionerror", "valueerror",
    "exit_code", "❌", "error:", "failed", "exception", "winerror",
    "timeout", "connectionerror", "refused", "not found",
]


def get_sessions(days: int, model: str | None) -> list[dict]:
    """从 state.db 读取会话（与 export_traces.py 一致）"""
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    since = (datetime.now() - timedelta(days=days)).timestamp()
    params = [since]
    q = """
        SELECT session_id, model, api_call_count,
               input_tokens, output_tokens, cache_read_tokens,
               reasoning_tokens, first_seen, last_seen
        FROM session_model_usage
        WHERE last_seen >= ?
    """
    if model:
        q += " AND model = ?"
        params.append(model)
    usage = [dict(r) for r in cur.execute(q, params).fetchall()]

    session_ids = list({u["session_id"] for u in usage})
    traces = []
    if session_ids:
        placeholders = ",".join("?" * len(session_ids))
        mq = f"""
            SELECT session_id, role, content, tool_name, tool_calls,
                   reasoning_content, timestamp
            FROM messages
            WHERE session_id IN ({placeholders})
            ORDER BY timestamp ASC
        """
        msgs = cur.execute(mq, session_ids).fetchall()
        by_session = {}
        for m in msgs:
            by_session.setdefault(m["session_id"], []).append(dict(m))
        for s in usage:
            traces.append({
                "session_id": s["session_id"],
                "model": s["model"],
                "api_call_count": s["api_call_count"],
                "tokens": {
                    "input": s["input_tokens"], "output": s["output_tokens"],
                    "cache_read": s["cache_read_tokens"], "reasoning": s["reasoning_tokens"],
                },
                "first_seen": s["first_seen"], "last_seen": s["last_seen"],
                "messages": by_session.get(s["session_id"], []),
            })
    conn.close()
    return traces


# ============ 标注 ============
def label_trace(t) -> tuple[str, list[str]]:
    """给单条轨迹标 success / fail / uncertain"""
    msgs = t["messages"]
    reasons = []
    if not msgs:
        return "fail", ["空会话"]

    tool_msgs = [m for m in msgs if m["role"] == "tool"]
    n_tools = len(tool_msgs)
    err_tools = []
    for m in tool_msgs:
        content = (m.get("content") or "")
        # 结构化判断优先：JSON 里 success=false / error 字段非空 = 真失败
        try:
            obj = json.loads(content)
            if isinstance(obj, dict):
                if obj.get("success") is False:
                    err_tools.append(m)
                    continue
                if obj.get("error"):
                    err_tools.append(m)
                    continue
                # 无失败标志 → 成功，跳过关键词
                continue
        except Exception:
            pass
        # 非 JSON 文本才用关键词（避免 web_search 摘要里的 "Error" 字样误判）
        low = content.lower()
        if any(k in low for k in ERR_KEYWORDS) and len(content) < 500:
            err_tools.append(m)

    # 最终回复：最后一个非 tool 的 assistant 消息，且有实质内容
    final_reply = None
    for m in reversed(msgs):
        if m["role"] == "assistant":
            final_reply = m
            break
    has_final = bool(final_reply and (final_reply.get("content") or "").strip())

    # 用户确认信号（最后几条 user 消息里有没有"谢谢/可以/好/ok"）
    user_msgs = [m for m in msgs if m["role"] == "user"]
    ack_pattern = re.compile(r"(谢谢|感谢|可以了|好的|搞定|ok|✅|完成了|不错|正确|就是这样|对|yes|great|works)")
    last_user = user_msgs[-1].get("content", "")[:500] if user_msgs else ""
    user_ack = bool(ack_pattern.search(last_user.lower()))

    # 判定
    if n_tools == 0 and has_final:
        return "success", ["纯对话无工具调用"]
    if n_tools > 0 and not err_tools and has_final:
        return "success", ["工具全成功且有最终回复"]
    if n_tools > 0 and len(err_tools) > n_tools * 0.5:
        return "fail", [f"工具失败率 {len(err_tools)}/{n_tools}"]
    if not has_final:
        return "fail", ["无最终回复（截断/中断/agent 循环）"]
    if n_tools > 0 and err_tools and has_final:
        # 有错误但最终有回复——看用户是否确认
        if user_ack:
            return "success", [f"部分工具错误({len(err_tools)}/{n_tools})但用户确认完成"]
        return "uncertain", [f"部分工具错误({len(err_tools)}/{n_tools})无用户确认"]
    return "uncertain", ["混合信号无法判定"]


# ============ 清洗 ============
def clean_trace(t) -> tuple[bool, list[str]]:
    """返回 (是否保留, 清洗原因)"""
    reasons = []
    tok = (t["tokens"]["input"] or 0) + (t["tokens"]["output"] or 0)
    n_msg = len(t["messages"])
    if tok > MAX_TOKENS:
        reasons.append(f"超长 {tok//1000}k tokens")
    if n_msg > MAX_MESSAGES:
        reasons.append(f"消息过多 {n_msg}")
    if n_msg < MIN_MESSAGES:
        reasons.append(f"过短 {n_msg} 消息")
    return (not reasons, reasons)


def main():
    ap = argparse.ArgumentParser(description="Hermes 轨迹标注器")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--model", type=str, default=None)
    ap.add_argument("--out", type=str, default="traces")
    ap.add_argument("--verbose", action="store_true", help="打印抽样标注")
    args = ap.parse_args()

    if not DB.exists():
        print(f"❌ 未找到 state.db: {DB}")
        return

    traces = get_sessions(args.days, args.model)
    print(f"📡 读取 {len(traces)} 条轨迹 (最近 {args.days} 天)")

    # 清洗
    kept, dropped = [], []
    for t in traces:
        ok, reasons = clean_trace(t)
        if ok:
            kept.append(t)
        else:
            dropped.append((t, reasons))

    # 标注
    labeled = []
    for t in kept:
        label, reasons = label_trace(t)
        labeled.append({
            "session_id": t["session_id"],
            "model": t["model"],
            "label": label,
            "reasons": reasons,
            "n_tools": sum(1 for m in t["messages"] if m["role"] == "tool"),
            "n_messages": len(t["messages"]),
            "tokens_total": (t["tokens"]["input"] or 0) + (t["tokens"]["output"] or 0),
        })

    # 统计
    from collections import Counter
    label_cnt = Counter(x["label"] for x in labeled)
    model_cnt = Counter(x["model"] for x in labeled)
    n_drop = len(dropped)
    drop_reasons = Counter(r for _, rs in dropped for r in rs)

    ts = datetime.now().strftime("%Y%m%d_%H%M")
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"labeled_{ts}.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for x in labeled:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")

    # 报告
    lines = [
        f"# 轨迹标注统计 — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"原始轨迹: {len(traces)}",
        f"清洗后: {len(kept)} (丢弃 {n_drop})",
        f"",
        f"## 标注分布",
        f"| label | 数量 | 占比 |",
        f"|:------|:----:|:----:|",
        f"| success | {label_cnt.get('success',0)} | {label_cnt.get('success',0)/max(1,len(labeled))*100:.0f}% |",
        f"| fail | {label_cnt.get('fail',0)} | {label_cnt.get('fail',0)/max(1,len(labeled))*100:.0f}% |",
        f"| uncertain | {label_cnt.get('uncertain',0)} | {label_cnt.get('uncertain',0)/max(1,len(labeled))*100:.0f}% |",
        f"",
        f"## 清洗原因",
        f"| 原因 | 数量 |",
        f"|:-----|:----:|",
    ]
    for r, c in drop_reasons.most_common():
        lines.append(f"| {r} | {c} |")
    lines.append("")
    lines.append("## 模型分布")
    for m, c in model_cnt.most_common():
        lines.append(f"- {m}: {c}")
    lines.append("")
    lines.append(f"输出: {out_path}")

    report = "\n".join(lines)
    print(report)
    (out_dir / "label_stats.md").write_text(report, encoding="utf-8")

    if args.verbose:
        print("\n=== 抽样标注（success 2 条 / fail 2 条 / uncertain 2 条）===")
        for label in ["success", "fail", "uncertain"]:
            samples = [x for x in labeled if x["label"] == label][:2]
            for s in samples:
                print(f"  [{label}] {s['session_id'][:30]} | tools={s['n_tools']} msgs={s['n_messages']} | {s['reasons']}")


if __name__ == "__main__":
    main()
