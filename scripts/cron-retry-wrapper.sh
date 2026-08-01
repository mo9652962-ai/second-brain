#!/bin/bash
# Cron 自动重试包装器 v2.0 (落地 2026-08-01，来自 hermes-automation-patterns 技能模板)
# 用法：cron-retry-wrapper.sh "你的命令" [重试次数] [间隔秒数]
# 适用：幂等操作（网络调用、文件同步、API 上报）。不适用：LLM 任务/发通知/非幂等操作。

COMMAND="$1"
MAX_RETRIES="${2:-2}"       # 默认重试 2 次 = 总共跑 3 次
RETRY_INTERVAL="${3:-300}"   # 默认间隔 5 分钟

if [ -z "$COMMAND" ]; then
    echo "用法: $0 \"命令\" [重试次数=2] [间隔秒数=300]"
    exit 2
fi

for i in $(seq 0 $MAX_RETRIES); do
    echo "[$(date -Iseconds)] 尝试第 $((i+1)) 次: $COMMAND"

    if bash -c "$COMMAND"; then
        echo "[$(date -Iseconds)] ✅ 成功"
        exit 0
    fi

    if [ $i -lt $MAX_RETRIES ]; then
        echo "[$(date -Iseconds)] ❌ 失败，${RETRY_INTERVAL} 秒后重试..."
        sleep "$RETRY_INTERVAL"
    fi
done

echo "[$(date -Iseconds)] 💥 全部 $((MAX_RETRIES+1)) 次尝试都失败了"
exit 1
