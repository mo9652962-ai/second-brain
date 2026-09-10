#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""projects/state.yaml 与 current.md「第 N 天」一致性断言门禁（2026-09-10 反思建）。
只读检查：state.yaml 权威值 vs current.md 文本中「第 N 天」分布，输出 PASS/FAIL。
用法: python scripts/assert_state_consistency.py
登记: vault scripts/README.md（见 vault 脚本登记表）
"""
import re, sys, pathlib
from collections import Counter

VAULT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")
STATE = VAULT / "projects" / "state.yaml"
CURRENT = VAULT / "projects" / "current.md"


def parse_state(p):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    day = re.search(r"xianyu_decision_day:\s*(\d+)", txt)
    status = re.search(r"xianyu_decision_status:\s*(\w+)", txt)
    return (int(day.group(1)) if day else None,
            status.group(1) if status else None)


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

    day, status = parse_state(STATE)
    check("state.yaml 解析", day is not None, f"day={day}, status={status}")

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

    ok = all(o for _, o in results)
    print(f"\nRESULT: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
