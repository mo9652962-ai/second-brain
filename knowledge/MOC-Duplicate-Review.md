---
title: 重复笔记审阅与合并边界
aliases: [Duplicate Review, 重复笔记清单]
type: moc
domain: META
status: active
created: 2026-08-31
updated: 2026-08-31
tags:
  - meta/moc
  - knowledge/governance
  - knowledge/deduplication
source: scripts/vault-orphan-duplicate-scan.py
---

# 🔁 重复笔记审阅与合并边界

> 本页记录“标题相似”与“内容重复”的区别。当前批次保留所有原始笔记；只有逐字重复或明确的转录副本才允许合并。

## 扫描结论（2026-08-31）

- 知识库内逐字内容重复：**0 组**（按 SHA-256 校验）。
- 标题归一化后相似组：主要是日报、周报、arXiv 连续期、研究稿/知识卡片，不能仅凭标题合并。
- 当前采取：补充主笔记/卡片关系、统一入口、保留时间序列；不删除原始内容。

## 已确认的关系

| 关系 | 主笔记 | 补充/派生笔记 | 处理 |
|---|---|---|---|
| 原则 + 吸收记录 | [[knowledge/Dev/ponytail]] | [[knowledge/Dev/ponytail-absorbed]] | 保留两篇，补充反向说明 |
| 深研稿 + 知识卡片 | [[knowledge/Dev/prime-agent-rlm-2026-08-14]] | [[knowledge/cards/2026-08-14-prime-agent-rlm]] | 保留两篇，卡片作为复习入口 |
| 方法论 + 知识卡片 | [[knowledge/Productivity/github-monetization-2026-08-20]] | [[knowledge/cards/2026-08-21-github-monetization]] | 保留两篇，卡片作为行动摘要 |
| 主笔记 + 文章来源研究 | [[knowledge/Dev/system-design-primer]] | [[knowledge/Research/system-design-primer-study]] | 保留两篇，研究页标注主笔记 |

## 按时间序列保留

- `hackernews-*`：不同日期的日报，内容来源和当天榜单不同。
- `GitHub-Weekly-*`、`github-trending-w*`：不同周次/口径的周报，不能合并成一篇而丢失时间线。
- `arxiv-*`、`skill-audit-*`、`token-usage-report-*`、`墨题每日巡检-*`、`每日股票分析-*`：每期都有独立数据或结论，保留原始记录。

## 后续合并门槛

1. 两个文件正文逐字相同，或一个文件明确写明“副本/转录”，才考虑合并。
2. 合并前先在保留文件中记录来源路径，并保留可恢复副本。
3. 研究稿与知识卡片不合并：一个承载证据，一个承载复习与行动。

---

[[knowledge-map|🗺️ 返回知识地图]] · [[MOC-Inbox|🧭 待接入入口]] · [[HOME|🏠 返回首页]]
