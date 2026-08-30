---
aliases:
  - 2026-08-30-card-data-source-verification
tags:
  - knowledge-card
  - data-verification
  - github-evaluation
  - openclaw
created: 2026-08-30
source: "[[memory/2026-08-30]]"
status: fresh
---

# 🃏 知识卡片 · 评估项目别信第三方 star 数：以官方 repo 为准

> **来源**：daily-self-improvement 日志 LRN-20260801-001 Recurrence Note (11th) · 2026-08-30 · ✅ 内部交叉验证（MEMORY 记录 368K vs 第三方站 180K）
> **一句话**：第三方资讯/镜像站报的 GitHub star 数等行情数据可能失真——本次发现 openclaw-ai.net 声称 180K stars，与既有记录 368K 差一倍多，**评估任何项目以官方 repo 为准**。

---

## 核心洞察

| 维度 | 内容 |
|------|------|
| 冲突现场 | 8/30 自改进 cron 搜索结果中 `openclaw-ai.net`（第三方站）声称 OpenClaw「180K stars」，与 MEMORY 既有记录 **368K** 明显冲突 |
| 根因 | 第三方镜像/资讯站数据未经官方校准，可能过期、拼凑或夸大，属于二手信息 |
| 判断原则 | 行情/指标类数据（star、价格、用户量、定价）一律回官方源核对——GitHub 看 repo 页、产品看官网/官方文档 |
| 适用场景 | 评项目实证、比价、引用数字写进卡片/日报前，先溯源 |

## 对 sora 的影响

1. ✅ **强化既有「评项目须实证」规则**——MEMORY 早定「真实 star/README/定价」为准，本次冲突提供了又一个实例背书
2. ⚠️ **写卡片/日报引用数字前多一步溯源**：任何带数字的 claim，标注来源并回官方 repo 核对，避免把二手站错误数字固化进知识库
3. 💡 **通用迁移**：不只 GitHub star——抖音/小红书博主带货量、闲鱼同行情报价、任何行情数据同理，官方源优先

## 行动项

- [x] **评新项目时**：star 数以 GitHub 官方 repo 页为准（或 `gh repo view --json stargazersCount`），不引用二手站数字 → ✅ 2026-08-30 已 patch 进 github-project-evaluation Pitfalls（含 8/30 实例：180K vs 368K）
- [x] **数字入卡**：知识卡片/日报中带数字的 claim 标注「官方源 / 二手源」；二手源数字未核验时注明 → ✅ 2026-08-30 已 patch 进 daily-knowledge-review 选择标准第 6 条
- [x] **本次冲突已记录**：openclaw 行情以官方 repo 为准，第三方站 180K 不作数 → ✅ 2026-08-30 已执行（本卡 + LRN-20260801-001 Recurrence 11th）

## 为什么重要

- **时效性**：今日 LRN 新观察（8/30 Recurrence Note 11th），实时踩到
- **业务**：sora 高频评第三方项目（克隆/实测/可提 PR）——被 180K 假数字误导会影响选型判断
- **强化自身**：把「内部记录 vs 外部二手源冲突」这个偶发事件，提炼成可复用的数据溯源原则，防止错误数字二次污染知识库

---

*卡片来源：当天知识库精选 · [[memory/2026-08-30]]（🥇 薄产出日 LRN 候选：数据辨识经验是今日唯一「新价值+新行动项」条目——直接强化 sora 实证评估偏好；Tavily 第 11 次复发属执行确认类不入选）*

**亚军候选**：Firecrawl 第 11 次无缝接管（Tavily 432 兜底）——工程可靠性再次确认，但无新知识增量，留给 daily-review 记录。
