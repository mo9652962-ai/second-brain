#!/bin/bash
# gh-fast.sh — GitHub 大文件高速下载（aria2 16线程 + 本地代理）
# 用法: gh-fast.sh <GitHub Release URL> [输出文件名]
# 示例: gh-fast.sh https://github.com/microsoft/PowerToys/releases/download/v0.100.2/PowerToysUserSetup-0.100.2-x64.exe
#
# 效果: 3.2 MiB/s（实测 271MB 约 90 秒），对比 curl 直连 30 分钟反复断线
# 依赖: aria2c（winget install aria2.aria2）

set -euo pipefail

URL="${1:?用法: gh-fast.sh <URL> [文件名]}"
OUT="${2:-}"
PROXY="${GH_FAST_PROXY:-http://127.0.0.1:7890}"   # FlClash 默认端口，可覆盖
THREADS="${GH_FAST_THREADS:-16}"

# aria2c 在 WinGet Links 目录（PATH 可能未刷新）
if ! command -v aria2c >/dev/null 2>&1; then
    export PATH="$PATH:$LOCALAPPDATA/Microsoft/WinGet/Links"
fi

ARGS=(-x "$THREADS" -s "$THREADS" --all-proxy="$PROXY" --timeout=30 --max-tries=3 --continue=true)
if [ -n "$OUT" ]; then
    ARGS+=(-o "$OUT")
fi

echo "📥 下载: $URL"
echo "   ⚡ 线程: $THREADS | 代理: $PROXY"
aria2c "${ARGS[@]}" "$URL"

echo ""
echo "✅ 下载完成（aria2 自动断点续传，中断重跑即可续传）"
