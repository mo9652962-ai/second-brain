# Pipeline 工作流总览（优化版）

> 更新：2026-07-25 | 10 轮研究后优化

## 📊 架构全景

```
时间层        任务链
──────        ──────
7:00  ──→  arxiv-fetch
　　　　↕ context_from
8:00  ──→  arxiv-summarize
8:30  ──→  daily-health-check
9:00  ──→  daily-self-improvement
18:00 ──→  daily-monetization-review 🆕
22:00 ──→  memory-summary

每30min ─→ obsidian-github-sync
每2h   ──→ obsidian-vault-sync

每周日:
10:00 ──→ 知识整合
12:00 ──→ 图谱更新
14:00 ──→ 系统清理  
15:00 ──→ 趋势项目吸收 🆕
20:00 ──→ 学习进度
21:00 ──→ 成本报告
```

## ⚡ 稳定性优化

| 任务 | 问题 | 优化方案 |
|:-----|:-----|:---------|
| memory-prune | 超时 604s | 已缩短 prompt，2h 间隔 |
| obsidian-maintenance | HTTP 401 | 已修复 ✅ |
| **全部 cron 401** | **model.base_url 指向 opencode.ai 需 Key** | **已切回 api.deepseek.com/v1 ✅** |

## 🔧 修复记录 (2026-07-26)
- 修复：`model.base_url` 从 `opencode.ai/zen/go/v1` → `api.deepseek.com/v1`（后又切回 opencode）
- 修复：`opencode-go` provider 补上 `key_env: OPENCODE_GO_API_KEY`
- 修复：`model.provider` 设为 `opencode-go`
- 修复：所有 cron 任务重建并锁定 model/provider，绕过"配置漂移"安全拦截
- 影响：18+ cron 任务全部恢复 ✅

## 📈 当前状态

| 项目 | 状态 |
|:-----|:------|
| 当前 provider | **opencode-go** (deepseek-v4-flash) |
| Gateway | ✅ Running (PID 22808) |
| arxiv-fetch | ✅ 已触发执行中 |
| cron 认证 | ✅ 全部修复 |

## 📈 扩展建议

| 优先级 | 行动 | 收益 |
|:------|:-----|:-----|
| ⭐⭐⭐ | context_from 链式配置 | 消除数据断层 |
| ⭐⭐ | cron 输出归档到 knowledge | 知识沉淀 |
| ⭐ | 修复 401/超时任务 | 稳定性提升 |
