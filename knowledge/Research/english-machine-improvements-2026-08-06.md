---
aliases:
  - english-machine-improvements
tags:
  - research
  - edtech
  - spaced-repetition
  - ai
created: 2026-08-06
updated: 2026-08-06
source: web_search × 9 queries
status: active
domain: edtech
---

# AI 英语刷题机 — 千轮研究增强方案

> 2026-08-06，九轮搜索
> 参考: Echo Loop / FSRS / Anki / OpExams / Synapse / Scholarsome / QuizFlow / Subs2SRS

## 已完成实施 (v9.19)

| 改动 | 文件 | 效果 |
|:-----|:-----|:-----|
| DeepSeek V4-Flash 默认 | database.py, schemas.py | 开箱即用，填 key 就行 |
| 品牌 "AI 英语刷题机" | App.vue, index.html | 中文品牌 |
| FSRS 间隔复习 | fsrs_scheduler.py, vocabulary.py | 替代固定 1/3/7 天间隔 |
| 每日待复习看板 | vocabulary.py /due-today | `GET /vocabulary/due-today` |
| 学习统计 | vocabulary.py /stats/summary | `GET /vocabulary/stats/summary` |
| AI 语境短文 | article_generator.py | `GET /vocabulary/article?topic=考研` |
| requirements.txt | fsrs>=2.0.0 | 依赖声明 |

## 对标项目借鉴

| 项目 | ★ | 借鉴点 |
|:-----|:--|:-----|
| Scholarsome | 782 | 多学习模式（填空/TF/MC）+ Self-hosted |
| Synapse | ★ | Anki兼容+Tauri桌面端+键盘优先UX |
| QuizFlow | 43 | 交互式闪卡+多种study modes |
| Subs2SRS | 871 | 从媒体提取词汇配上下文 |
| Echo Loop | 7 | 盲听→精听→跟读→复述→间隔复习闭环 |

## 待实施 (按优先级)

| 优先级 | 改进 | 工作量 |
|:------:|:-----|:------:|
| 🥇 | 前端复习日历视图 | 2h |
| 🥈 | 错题AI生成相似题 | 1h |
| 🥉 | 游戏化streak统计 | 30m |
| 4 | 多学习模式 (填空/TF) | 3h |
| 5 | 键盘快捷键 | 1h |
