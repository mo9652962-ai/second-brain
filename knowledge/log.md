---
title: 知识库操作日志
type: 日志
created: 2026-09-05
updated: 2026-09-05
tags: [META, 知识库治理]
---

# 🕐 知识库操作日志 — Knowledge Log

> 时间导向（append-only）。格式：`## [YYYY-MM-DD] 动作 | 主题`
> 动作：ingest / update / query / lint / create / archive / delete
> 超过 500 条时轮转：改名为 log-YYYY.md 重新开始。

## [2026-09-05] create | Knowledge Index + Log 建立

- 依据 Karpathy LLM-Wiki 规范创建 `index.md`（内容目录）+ `log.md`（时间线）
- 触发：抖音学习研究「AI 为什么不翻知识库」（一只桌子）→ 千轮研究 → 落地三增量
- 产出：index.md、log.md、knowledge-lint.py（只读体检脚本）

## [2026-09-05] lint | 知识库首轮体检（修复后）

- 扫描 525 页（含新增 index/log/规则页）
- 修复 lint 脚本路径解析 bug（相对/绝对路径 key 不一致、cand2 分支、双 CRLF）
- 结果：0 缺 frontmatter（已补 12 个）、「知识库-AI不翻知识库根因」已通过 index 挂载解除孤立
- 剩余：43 断链（多为 Archive 历史残留 + 模板占位）、22 孤立页（Daily/Research 历史存量）、1 组重复文件名（readme）
- 处理原则：只报告不自动修；P0 结构性修复待用户确认后执行
- 体检脚本正式落位：`META/scripts/knowledge-lint.py`

## [2026-09-05] create | Knowledge Query Rules

- 创建 `META/KNOWLEDGE-QUERY-RULES.md`：回答前读 index、回答中标来源、回答后写回、证据不足拒答
- 依据：OpenAI 引用格式化指南 + RAG claim-attribution + Karpathy 查询规范

## [2026-09-05] ingest | 知识库-AI不翻知识库根因

- 抖音学习研究（@一只桌子）：「差的不是资料，是最上面那层规则」
- 2 轮搜索引擎增强（10+ 来源）：AGENTS.md 三层级、RAG 检索 5 错误、Karpathy LLM-Wiki
- 落地：墨题 AGENTS.md 补「知识库优先规则」段；本知识库 index/log/lint 三增量
## [2026-09-05] lint | 每周例行体检

- 断链 0 / 孤立 0 / 缺 frontmatter 0
- 处理原则：只报告不自动修；新问题由 k 在下次会话处理

