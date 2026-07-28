---
name: hermes-automation-patterns
description: Cron 自动化模式与故障恢复机制：自动重试、错峰调度、健康检查
tags: [cron, automation, reliability, retry, devops]
category: Hermes
created: 2026-07-28
updated: 2026-07-29
version: 1.1.0
---

# Hermes 自动化与故障恢复模式

> 从真实故障中沉淀的 Cron 可靠性机制

---

## 📋 目录

1. [网络敏感任务错峰调度](#1-网络敏感任务错峰调度)
2. [自动重试脚本模式](#2-自动重试脚本模式)
3. [连续失败升级通知](#3-连续失败升级通知)
4. [改进记录](#4-改进记录)

---

## 1. 网络敏感任务错峰调度

### 故障背景 2026-07-28

> 7/28 早 8:00-9:00 期间，**6 个 cron 任务** 因网络波动集中失败
> 全部撞在同一个故障窗口 = 批量失败 = 需要人工重跑

### ✅ 已实施的错峰方案

```
原调度（全部撞 8:00-9:00）：
  08:00 arxiv-summarize     ← 网络依赖（API 调用）
  08:30 daily-health-check  ← 网络依赖（API 连通性）
  09:00 daily-self-improvement ← 轻度网络依赖
  09:00 闲鱼提醒           ← 网络依赖

新调度（错峰 15 分钟间隔，避免雪崩）：
  08:00 arxiv-summarize          (第一个，API 流量低峰)
  08:15 daily-health-check       +15min，错开 arxiv 的 API 调用窗口
  08:30 daily-self-improvement   +15min，不跟任何任务撞
  09:00 闲鱼提醒 (工作日)        保持，作为第二波起点
```

### 错峰原则

```
高网络依赖任务（调用外部 API）：
  ├── 间隔至少 15 分钟
  ├── 避免集中在整点
  └── 优先安排在网络低峰期（早 7-8 点）

纯本地任务（文件读写、Git 提交）：
  └── 可以更密集，网络故障不影响
```

---

## 2. 自动重试脚本模式

### 什么时候用

```
适合：
  ├── 纯脚本型 cron 任务（no-agent 模式）
  ├── 网络调用密集型任务
  ├── 幂等的操作（跑多次结果一样）
  └── 间歇性故障最有效（API 临时 5xx、DNS 波动、VPN 切换）

不适合：
  ├── Agent 驱动的 LLM 任务（重试成本高）
  ├── 非幂等操作（发邮件、发通知）
  └── 已确认的永久故障（API Key 过期、服务下线）
```

### 重试脚本模板 `cron-retry-wrapper.sh`

```bash
#!/bin/bash
# Cron 任务自动重试包装器
# 使用方式：./cron-retry-wrapper.sh "你的命令" [最大重试次数] [重试间隔秒]

COMMAND=${1:-"echo 'No command provided'"}
MAX_RETRIES=${2:-2}           # 默认最多重试 2 次 = 总共跑 3 次
RETRY_INTERVAL=${3:-300}      # 默认间隔 5 分钟

RETRY_COUNT=0

while [ $RETRY_COUNT -le $MAX_RETRIES ]; do
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 执行尝试 #$RETRY_COUNT: $COMMAND"
    
    # 执行命令
    if eval $COMMAND; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ✅ 执行成功"
        exit 0
    fi
    
    RETRY_COUNT=$((RETRY_COUNT + 1))
    
    if [ $RETRY_COUNT -le $MAX_RETRIES ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 失败，$RETRY_INTERVAL 秒后进行第 $RETRY_COUNT 次重试..."
        sleep $RETRY_INTERVAL
    fi
done

echo "[$(date '+%Y-%m-%d %H:%M:%S')] ❌ 全部 $MAX_RETRIES 次重试均失败，放弃"
exit 1
```

### Hermes Cron 配置方式

```yaml
# 使用 no-agent 脚本模式
name: "network-task-with-retry"
schedule: "0 8 * * *"
script: |
  #!/bin/bash
  # 你的任务命令
  python your_script.py
no_agent: true
```

---

## 3. 连续失败升级通知

### 健康检查增强项

```
在 daily-health-check 中增加：
1. 统计每个 cron 的连续失败次数
2. 如果连续失败 >= 2 次 → 高亮警告
3. 如果连续失败 >= 3 次 → 触发主动通知（需要用户干预）

健康报告输出模板：
  🔴 高危：xxx 任务已连续失败 3 次，建议人工检查
  🟡 注意：xxx 任务已连续失败 2 次，明日观察
  ✅ 正常：xxx 任务运行正常
```

---

## 4. 改进记录

| 版本 | 日期 | 变更内容 | 来源 |
|------|------|---------|------|
| 1.1.0 | 2026-07-29 | 增加「网络敏感任务错峰调度」+「自动重试脚本模式」 | 2026-07-29-reflection 改进 #2 |
| 1.0.0 | 2026-07-28 | 初始创建 | Cron 任务经验总结 |

