#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""projects/state.yaml 与 current.md「第 N 天」一致性断言门禁（2026-09-10 反思建）。
只读检查：state.yaml 权威值 vs current.md 文本中「第 N 天」分布，输出 PASS/FAIL。
用法: python scripts/assert_state_consistency.py
登记: vault scripts/README.md（见 vault 脚本登记表）
"""
import re, sys, pathlib
from collections import Counter

VAULT = pathlib.Path(__file__).resolve().parent.parent
STATE = VAULT / "projects" / "state.yaml"
CURRENT = VAULT / "projects" / "current.md"
MEMORY = VAULT / "MEMORY.md"


def parse_state(p):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    day = re.search(r"xianyu_decision_day:\s*(\d+)", txt)
    status = re.search(r"xianyu_decision_status:\s*(\w+)", txt)
    upd = re.search(r"updated_at:\s*(\d{4}-\d{2}-\d{2})", txt)
    return (int(day.group(1)) if day else None,
            status.group(1) if status else None,
            upd.group(1) if upd else None)


def main():
    results = []

    def check(name, ok, detail=""):
        results.append((name, ok))
        print(("PASS " if ok else "FAIL ") + name + (" | " + detail if detail else ""))

    if not STATE.exists():
        check("state.yaml 存在", False, f"缺失: {STATE}")
        print("\nRESULT: FAIL")
        return 1
    if not CURRENT.exists():
        check("current.md 存在", False, f"缺失: {CURRENT}")
        print("\nRESULT: FAIL")
        return 1

    day, status, updated = parse_state(STATE)
    check("state.yaml 解析", day is not None, f"day={day}, status={status}, updated={updated}")

    txt = CURRENT.read_text(encoding="utf-8", errors="ignore")
    days = [int(m) for m in re.findall(r"第\s*(\d+)\s*天", txt)]
    dist = Counter(days)
    top_n, top_c = dist.most_common(1)[0] if dist else (None, 0)

    if day is None:
        check("state.yaml 权威值", False)
    else:
        check("current.md 主导值=state.yaml", top_n == day,
              f"current.md 主导 第{top_n}天 x{top_c} / 全分布 {dict(sorted(dist.items()))}")
        divergent = {k: v for k, v in dist.items() if k != day}
        check("无残留漂移值", len(divergent) == 0,
              f"漂移残留 {divergent}" if divergent else "current.md 天数全一致")

    # MEMORY.md 兜底盲区修复（2026-09-15 反思实测：assert PASS 与 MEMORY.md 漂移并存）
    if day is not None and MEMORY.exists():
        m = MEMORY.read_text(encoding="utf-8", errors="ignore")
        m_line = re.search(r"闲鱼[^\n]*决策悬置第\s*(\d+)\s*天", m)
        check("MEMORY.md 闲鱼决策天数=state.yaml",
              m_line is not None and int(m_line.group(1)) == day,
              f"MEMORY.md 决策 第{m_line.group(1)}天" if m_line else "MEMORY.md 无闲鱼决策天数行")

    # reflection/daily-review 盲区扫描（2026-09-20 反思扩展：第 3 次漂移根治面）。
    # 只扫文件名日期 >= state.yaml updated_at 的反思/日报；早于权威更新的历史文件
    # 当时的计数合法，不判（防假阳性）。
    # 匹配范围收紧为「表格行动项行 + 闲鱼上下文」（行首 | + 行内含 闲鱼 + 第N天）：
    #   叙述性提及（漂移历史 43->42 复盘）、机制引用（「第 8 天起每周复盘」）不算漂移。
    if day is not None and updated is not None:
        memdir = VAULT / "memory"
        stale = []
        if memdir.exists():
            for p in sorted(memdir.rglob("*.md")):
                if "reflection" not in p.name and "daily-review" not in p.name:
                    continue
                m_date = re.search(r"(\d{4}-\d{2}-\d{2})", p.name)
                if not m_date or m_date.group(1) < updated:
                    continue
                t = p.read_text(encoding="utf-8", errors="ignore")
                for line in t.splitlines():
                    if not line.lstrip().startswith("|") or "闲鱼" not in line:
                        continue
                    for v in re.findall(r"第\s*(\d+)\s*天", line):
                        if int(v) != day:
                            stale.append(f"{p.name}:{line.strip()[:60]}")
        check("reflection/daily-review 表格行动项无天数漂移", len(stale) == 0,
              f"漂移残留 {stale}" if stale else f">= updated({updated}) 文件行动项天数全一致(权威第{day}天)")

    ok = all(o for _, o in results)
    print(f"\nRESULT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
