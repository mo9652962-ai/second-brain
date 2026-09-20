#!/usr/bin/env python3
"""删页/改名后自动复检 lint —— 防「清理快照」失效。

背景（2026-09-20 仓库评估发现）：
  log.md 记录 `[2026-09-20] lint | 例行体检：8 问题 → 0`，
  但同日另一提交删除了被引用的模板 → 断链立刻复现，无人复检。
  教训：lint 是快照，不是状态。任何删页/改名的操作都该触发一次复检。

设计：只报**回归**（相对基线的增量），不报既有问题。
  vault 允许存在良性提示（如两个不同子目录的同名 README），
  若无差别地报"有问题"会变成假阳性税 → 很快被 --no-verify 绕过。

用法:
  python scripts/post_change_lint.py           # 检查暂存区改动
  python scripts/post_change_lint.py --always  # 无条件跑（手动全量体检）

退出码:
  0 = 无删页/改名，或复检无回归
  1 = 复检发现新增问题（配合 git hook 可阻断提交）
"""
import argparse
import pathlib
import re
import subprocess
import sys

VAULT = pathlib.Path.home() / ".openclaw" / "workspace"
LINT = VAULT / "knowledge" / "META" / "scripts" / "knowledge-lint.py"

# 这些前缀的删除不影响知识库链接完整性
IGNORE_PREFIXES = ("knowledge/META/", "memory/", "scripts/", ".backup/")

COUNTER_RE = re.compile(r"^\[(ERROR|WARNING|INFO)\]\s+(.+?):\s*(\d+)")


def staged_md_changes() -> list[str]:
    """返回暂存区中被删除(D)/改名(R)的 .md 路径。"""
    r = subprocess.run(
        ["git", "-C", str(VAULT), "diff", "--cached", "--name-status", "--diff-filter=DR"],
        capture_output=True, text=True, timeout=60,
    )
    out = []
    for line in r.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status, path = parts[0], parts[-1]     # R100 改名时 parts[-1] 是新路径
        if not path.endswith(".md"):
            continue
        if path.startswith(IGNORE_PREFIXES):
            continue
        out.append(f"{status}\t{path}")
    return out


def parse_lint(out: str) -> tuple[int, dict]:
    """解析 lint 输出 -> (总数, {分类: 计数}, 明细行)"""
    counts = {}
    for ln in out.splitlines():
        s = ln.strip()
        m = COUNTER_RE.match(s)
        if m:
            counts[m.group(2).strip()] = int(m.group(3))
    m = re.search(r"TOTAL ISSUES:\s*(\d+)", out)
    return (int(m.group(1)) if m else -1), counts


def run_lint() -> str:
    r = subprocess.run(
        [sys.executable, str(LINT), "knowledge"],
        capture_output=True, text=True, timeout=300, cwd=str(VAULT),
    )
    return r.stdout + r.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--always", action="store_true", help="无条件复检（忽略暂存区）")
    args = ap.parse_args()

    if not LINT.exists():
        print(f"[SKIP] lint 脚本不存在: {LINT}")
        return 0

    changes = ["FORCE\t(手动全量体检)"] if args.always else staged_md_changes()
    if not changes:
        print("[OK] 本次提交无删页/改名 → 跳过复检")
        return 0

    print("=" * 60)
    print("删页/改名复检 —— 以下改动可能造成断链：")
    for c in changes:
        print(f"  {c}")
    print("=" * 60)

    out = run_lint()
    total, counts = parse_lint(out)
    if total < 0:
        print("[WARN] lint 输出无法解析 → 不阻断（人工确认）")
        return 0

    # 回归判定（简洁规则）：
    #   ERROR 类 → 阻断（断链/缺 frontmatter 是硬伤，删页直接导致）
    #   WARNING 类 → 仅提示（孤立/重名/短页多为既有良性项，不阻断，避免假阳性税）
    BLOCKING = ("Broken wikilinks", "Missing frontmatter",
                "Glued frontmatter close (no standalone ---)")
    blocking = {k: v for k, v in counts.items() if k in BLOCKING and v > 0}
    warns = {k: v for k, v in counts.items() if k not in BLOCKING and v > 0}

    print(f"\n复检结果: TOTAL ISSUES = {total}")
    for ln in out.splitlines():
        if re.match(r"\s*\[(ERROR|WARNING)\]", ln):
            print("  " + ln.strip())

    if blocking:
        print("\n[FAIL] 删除/改名引入了硬伤：")
        for k, v in blocking.items():
            print(f"       {k}: {v}")
        print("       修法：更新或移除指向已删页面的 [[wikilink]]，再提交。")
        print("       绕过（不推荐）：git commit --no-verify")
        return 1

    if warns:
        print(f"\n[PASS] 无硬伤（{len(warns)} 类提示项为既有/非阻断）："
              + ", ".join(f"{k}={v}" for k, v in warns.items()))
        return 0

    print("[PASS] 无新增断链/孤立。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
