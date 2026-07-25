# Pipeline 工作流总览

> 更新：2026-07-25 | 所有 cron 任务状态

## 📊 每日 Pipeline

| 时间 | 任务 | 状态 | 说明 |
|:----|:-----|:----:|:------|
| **7:00** | arxiv-fetch | ✅ | 检索 arXiv 最新 AI 论文 |
| **8:00** | arxiv-summarize | ✅ | 总结论文到 Obsidian |
| **8:30** | daily-health-check | ✅ | 健康检查 |
| **9:00** | daily-self-improvement | ✅ | 技能学习（加载多个 skills） |
| **18:00** | daily-monetization-review | 🆕 | 每日闲鱼定价/成本复盘 |
| **22:00** | memory-prune-and-summary | ⚠️ 超时 | 记忆压缩（超时待修） |
| **每30min** | obsidian-github-sync | ✅ | Git 自动同步（no-agent） |
| **每2h** | obsidian-maintenance | ⚠️ 401 | Obsidian 维护（API key 待修） |

## 📅 每周 Pipeline

| 时间 | 任务 | 状态 | 说明 |
|:----|:-----|:----:|:------|
| 周六 18:00 | weekly-todo-cleanup | ✅ | TODO 清理 |
| 周日 10:00 | weekly-knowledge-consolidation | ✅ | 知识整合 |
| 周日 12:00 | weekly-graphify-update | ✅ | 知识图谱更新 |
| 周日 14:00 | weekly-system-cleanup | ✅ | 系统清理 |
| 周日 15:00 | weekly-trending-review | 🆕 | GitHub 趋势项目吸收 |
| 周日 20:00 | weekly-learning-progress | ✅ | 学习进度回顾 |
| 周日 21:00 | weekly-cost-report | ✅ | 成本报告 |

## 📆 双周/月 Pipeline

| 时间 | 任务 | 说明 |
|:----|:-----|:------|
| 1日/15日 10:00 | biweekly-skill-audit | Skill 使用审计 |
| 每月1日 10:00 | monthly-skill-usage | 月度 Skill 统计 |

## 📈 完整数据流

```
7:00  arXiv论文检索
  └─→ 8:00 论文摘要→Obsidian
       │
8:30  健康检查
9:00  每日技能学习
       │
18:00 变现复盘（定价/成本/行动项）
       │
22:00 记忆压缩（当日日志→长期记忆）
       │
每30min → GitHub 自动同步
```

## ⚠️ 待修复

| 任务 | 问题 | 修复方案 |
|:-----|:-----|:---------|
| memory-prune-and-summary | 超时 604s/600s | 下次手动触发测试 |
| obsidian-maintenance | HTTP 401 | 检查 API Key 配置 |
