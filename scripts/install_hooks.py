#!/usr/bin/env python3
"""安装 vault 的 git hooks（幂等，可重复运行）。

为什么需要这个脚本：
  .git/hooks/ 不被 git 跟踪 —— 换机器/重 clone 后 hook 全部丢失。
  把 hook 内容版本化在 scripts/ 里，用本脚本幂等安装。

当前安装的 hook：
  pre-commit → 删页/改名时复检 lint（scripts/post_change_lint.py）

用法: python scripts/install_hooks.py
"""
import pathlib
import stat
import sys

VAULT = pathlib.Path.home() / ".openclaw" / "workspace"
HOOKS = VAULT / ".git" / "hooks"

PRE_COMMIT = """#!/bin/sh
# Installed by code-review-graph. Remove this file to disable pre-commit graph checks.
if command -v code-review-graph >/dev/null 2>&1; then
    code-review-graph update || true
    code-review-graph detect-changes --brief || true
fi

# --- vault lint 复检（2026-09-20 加）：删页/改名时阻断未清理的引用 ---
# 背景：lint 是快照不是状态——同日删页会让先前的"清零"记录失效
# 只查 ERROR 类硬伤；无删页/改名时零开销直接跳过
if [ -f "scripts/post_change_lint.py" ]; then
    python scripts/post_change_lint.py || {
        echo ""
        echo "提交被阻断：删页/改名引入了断链。修好后重试，或 git commit --no-verify 绕过。"
        exit 1
    }
fi
"""

MARKER = "vault lint 复检"


def main():
    if not HOOKS.is_dir():
        print(f"[FATAL] hooks 目录不存在: {HOOKS}")
        return 1

    target = HOOKS / "pre-commit"
    if target.exists():
        cur = target.read_text(encoding="utf-8", errors="ignore")
        if MARKER in cur:
            print(f"[OK] 已安装（含 lint 复检）: {target}")
            return 0
        # 已有其他 hook（如 code-review-graph）→ 备份后追加
        bak = target.with_suffix(f".bak-{__import__('datetime').date.today()}")
        bak.write_text(cur, encoding="utf-8")
        print(f"[BAK] 已备份原 hook -> {bak.name}")

    target.write_text(PRE_COMMIT, encoding="utf-8")
    target.chmod(target.stat().st_mode | stat.S_IEXEC)
    print(f"[NEW] 已安装: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
