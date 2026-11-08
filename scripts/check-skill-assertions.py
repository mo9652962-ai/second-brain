# -*- coding: utf-8 -*-
"""check-skill-assertions.py — 周期校验「高风险技能的核心功能断言」还在不在

判据（scripts/skill-core-assertions.json）：
    每个高风险技能声明 1 条独占断言 + must_contain 字符串；
    该字符串必须仍出现在技能 SKILL.md 中，否则报红（exit 1）。

为什么：技能会在多轮 patch/合并中被改写，最容易丢的正是「一句狠话」——
比如「移出 ≠ 安全」「严禁在 Public 仓库裸奔」。丢了不会报错，只会静默降级。

用法:
    python scripts/check-skill-assertions.py [--root <skills 根>] [--quiet]
"""
import json
import os
import sys

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(WS, "scripts", "skill-core-assertions.json")
DEFAULT_ROOTS = [
    os.path.expanduser("~/AppData/Local/hermes/skills"),
    os.path.expanduser("~/.openclaw/workspace/skills"),
]


def find_skill_dir(name, roots):
    """在 skills 根下递归找同名目录（技能可能分层放在 security/ productivity/ 下）。"""
    for root in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, _ in os.walk(root):
            for d in dirnames:
                if d == name and os.path.isfile(os.path.join(dirpath, d, "SKILL.md")):
                    return os.path.join(dirpath, d)
            # 只下钻两层（root/<cat>/<skill>）
            if dirpath.count(os.sep) - root.count(os.sep) >= 2:
                dirnames[:] = []
    return None


def main():
    quiet = "--quiet" in sys.argv
    roots = DEFAULT_ROOTS
    if "--root" in sys.argv:
        roots = [sys.argv[sys.argv.index("--root") + 1]]

    with open(REGISTRY, encoding="utf-8") as f:
        reg = json.load(f)
    entries = reg.get("assertions", [])
    fails = []
    for e in entries:
        name = e["skill"]
        d = find_skill_dir(name, roots)
        if not d:
            fails.append(f"❌ {name}: 找不到技能目录")
            continue
        try:
            text = open(os.path.join(d, "SKILL.md"), encoding="utf-8", errors="ignore").read()
        except Exception as ex:
            fails.append(f"❌ {name}: 读取失败 {ex}")
            continue
        if e["must_contain"] not in text:
            fails.append(f"❌ {name}: 核心断言丢失 —— 找不到 {e['must_contain']!r}（{e['assertion']}）")
        elif not quiet:
            print(f"✅ {name}: {e['assertion']}")

    if fails:
        print(f"\n⚠️ 技能核心断言校验：{len(fails)}/{len(entries)} 项失败")
        for x in fails:
            print("  " + x)
        return 1
    if not quiet:
        print(f"\n✅ {len(entries)}/{len(entries)} 条核心断言在位")
    return 0


if __name__ == "__main__":
    sys.exit(main())
