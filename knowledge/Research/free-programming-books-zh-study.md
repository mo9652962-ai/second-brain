---
tags: [research, github, books, programming, article-study]
created: 2026-07-31
status: absorbed
source: https://github.com/justjavac/free-programming-books-zh_CN
license: GPL-3.0
---

# 《学编程买书？免费的 400 本中文编程书》— 研究笔记

> 来源：小黑盒文章（前沿情报站 07-18）· 2026-07-31 验证 + 评估

## 项目验证

- **justjavac/free-programming-books-zh_CN** — GitHub 实测 **116,970★**（文章说 117,376，基本吻合）
- 2013-11 创建（快 13 年），120+ contributors，GPL-3.0
- 818 行 README 索引，400+ 本免费中文编程书
- 2024-07 最后更新（社区持续维护，失效链接标 😟）

## 文章推荐书单抽查（链接验证）

| 书 | 链接状态 | 验证 |
|----|---------|------|
| 廖雪峰 Python 3 教程 | 301→https | ✅ 有效 |
| labuladong 算法小抄 (fucking-algorithm) | 200 | ✅ 有效 |
| Redis 设计与实现 (redisbook.com) | 301→https | ✅ 有效 |
| Docker 从入门到实践 (yeasy/docker_practice) | 200 (26k★) | ✅ 有效 |
| Docker 中文指南 / Cheat Sheet | 200 | ✅ 有效 |

## 落地决策

| 选项 | 决策 | 理由 |
|------|:---:|------|
| 全量下载 400 本当知识库 | ❌ 不采用 | 存储/维护成本高；链接大量失效；我们的知识吸收是实时 learn→research→apply 路径，非离线书库 |
| 索引存档（书单路由表） | ✅ 采用 | 818 行 README 是免费书单的最佳索引，接单遇到技术栈时按需查书 |
| 精选下载 | ⏳ 暂缓 | Redis 书/Docker 书都有价值但非当前刚需；需要时单本拉取 |

## 评论区关键信号

> "通通下载下来当 agent 的知识库，需要用的时候读取相关内容"

**评估**：这个思路对"离线知识库型" agent 有价值，但：
- 我们已有 codebase-memory-mcp（代码库知识图谱）+ llm-wiki（Karpathy KB）+ graphify（任意输入→知识图谱）
- 全量 400 本 ≈ 数十 GB，索引成本高
- 我们的实际需求是"按技术栈实时查"，不是"全量离线"——遇到具体任务时 web_search + 定向拉单本更高效

## 落地行动

1. 📄 本笔记存档（含书单索引路径 + 链接验证结果）
2. 🟡 待需要时：接 Python/JS/Go/Redis/Docker 等技术栈订单时，从索引按需查书拉取
3. 💡 对博主身份：这篇"免费书单"文章本身是长青选题，可做《免费中文编程书索引》内容

## 结论

- 项目真实（117K★，13 年维护），链接基本有效
- **对我们是"书单路由表"而非"书库"**——按需查用，不全量下载
- 我们体系已有更高效的实时知识获取路径（web_search + 定向拉取）
