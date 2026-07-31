"""
Hermes 轨迹导出器 — OpenForgeRL 数据管线 P0
从 state.db 导出 agent 使用轨迹为 JSONL 训练数据

用法:
  uv run python scripts/export_traces.py --days 7 --out traces/
  uv run python scripts/export_traces.py --model deepseek-v4-flash --days 30
"""
import sqlite3, json, argparse, sys
from pathlib import Path
from datetime import datetime, timedelta

DB = Path.home() / "AppData/Local/hermes/state.db"


def get_sessions(days: int, model: str | None) -> list[dict]:
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

    # Get messages for those sessions
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
        by_session: dict[str, list[dict]] = {}
        for m in msgs:
            by_session.setdefault(m["session_id"], []).append(dict(m))

        for s in usage:
            traces.append({
                "session_id": s["session_id"],
                "model": s["model"],
                "api_call_count": s["api_call_count"],
                "tokens": {
                    "input": s["input_tokens"],
                    "output": s["output_tokens"],
                    "cache_read": s["cache_read_tokens"],
                    "reasoning": s["reasoning_tokens"],
                },
                "first_seen": s["first_seen"],
                "last_seen": s["last_seen"],
                "messages": by_session.get(s["session_id"], []),
            })
    conn.close()
    return traces


def to_rl_format(traces: list[dict]) -> list[dict]:
    """转换为 veRL/OpenForgeRL 风格: 每条轨迹 = prompt + 完成消息序列"""
    rl = []
    for t in traces:
        msgs = []
        for m in t["messages"]:
            role = m["role"]
            content = m["content"] or ""
            if role == "tool":
                msgs.append({"role": "tool", "content": content[:2000], "tool": m["tool_name"]})
            elif role == "assistant" and m.get("tool_calls"):
                try:
                    tc = json.loads(m["tool_calls"]) if isinstance(m["tool_calls"], str) else m["tool_calls"]
                    msgs.append({"role": "assistant", "content": content, "tool_calls": tc})
                except Exception:
                    msgs.append({"role": "assistant", "content": content})
            else:
                msgs.append({"role": role, "content": content[:4000]})
        if not msgs:
            continue
        rl.append({
            "session_id": t["session_id"],
            "model": t["model"],
            "conversation": msgs,
            "token_count": sum(m.get("token_count", 0) for m in t["messages"]),
        })
    return rl


def main():
    ap = argparse.ArgumentParser(description="Hermes 轨迹导出器")
    ap.add_argument("--days", type=int, default=7, help="导出最近 N 天")
    ap.add_argument("--model", type=str, default=None, help="按模型过滤")
    ap.add_argument("--out", type=str, default="traces", help="输出目录")
    args = ap.parse_args()

    if not DB.exists():
        print(f"❌ 未找到 state.db: {DB}")
        sys.exit(1)

    print(f"📡 读取 {DB.name} ({(DB.stat().st_size/1e6):.0f} MB)")
    traces = get_sessions(args.days, args.model)
    print(f"✅ 找到 {len(traces)} 条会话轨迹 (最近 {args.days} 天{'，模型: ' + args.model if args.model else ''})")

    rl = to_rl_format(traces)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # 统计
    total_in = sum(t["tokens"]["input"] for t in traces)
    total_out = sum(t["tokens"]["output"] for t in traces)
    total_msg = sum(len(t["messages"]) for t in traces)

    ts = datetime.now().strftime("%Y%m%d_%H%M")
    path = out_dir / f"hermes_traces_{ts}.jsonl"
    with open(path, "w", encoding="utf-8") as f:
        for item in rl:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"\n📊 导出统计:")
    print(f"   • 轨迹数: {len(rl)}")
    print(f"   • 消息数: {total_msg}")
    print(f"   • 输入 tokens: {total_in:,}")
    print(f"   • 输出 tokens: {total_out:,}")
    print(f"   • 文件: {path} ({path.stat().st_size/1024:.0f} KB)")

    # OpenForgeRL 可行性提示
    print(f"\n🎯 OpenForgeRL 可行性:")
    print(f"   • 论文门槛: 几百到几千任务可训练")
    print(f"   • 当前轨迹: {len(traces)} 会话 (7 天)")
    print(f"   • 达标进度: {min(100, len(traces)//10)}%")


if __name__ == "__main__":
    main()
