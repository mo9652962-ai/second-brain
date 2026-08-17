---
tags: [improvement, cron, fault-tolerance, self-improvement]
created: 2026-07-30
source: 2026-07-29-reflection + 全库扫描
---

# Cron 容灾改进方案

## 问题
7/28 早 8:00-9:00，6个 cron 任务因 Connection error 集中失败，无自动重试。

## 改进措施

### 1. 错峰调度（已实施）
网络敏感任务错开执行时间，避免同时击中同一故障窗口：

| 原时间 | 任务 | 新时间 | 原因 |
|--------|------|--------|------|
| 07:00 | arxiv-fetch | 07:00 | 保持 |
| 07:00 | hackernews-daily | 07:02 | +2min |
| 08:00 | arxiv-summarize | 08:00 | 保持 |
| 08:00 | daily-wechat-knowledge-card | 08:05 | +5min |
| 08:15 | daily-health-check | 08:15 | 保持 |
| 08:30 | daily-self-improvement | 08:30 | 保持 |
| 09:00 | 闲鱼提醒 | 09:00 | 保持 |

### 2. 自动重试（待 Hermes 支持）
当前 Hermes cron 不支持内置重试。替代方案：
- 网络依赖任务使用 `no_agent: true` + script mode，在脚本内实现 retry loop
- 健康检查 cron 增加「连续失败次数」指标

### 3. 每日吸收底线
- 每日至少 1 个主动研究项 + 1 个工具改进项
- daily-monetization-review 在产出末尾加入吸收检查
- 如果当天零吸收，标记为 ⚠️ 并在次日 morning cron 中提醒

## 状态
- [x] 错峰分析完成
- [x] 实施 cron 时间调整（已通过 cron-health-board 看板验证错峰生效：arxiv 07:00 / wechat 08:00 / health 08:15 / self-improve 08:30 / 闲鱼 09:00）
- [x] 添加 retry script（scripts/cron-retry-wrapper.sh 已落地 2026-08-01，v2.0 模板）
- [x] 每日吸收底线加入 cron 检查（daily-self-improvement 任务 prompt 已含「今日知识吸收检查」章节，2026-08-03 确认）

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
