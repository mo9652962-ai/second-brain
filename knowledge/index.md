---
title: 知识库索引
type: 索引
created: 2026-09-05
updated: 2026-09-05
tags: [meta, 知识库治理]
---

# 📇 知识库索引 — Knowledge Index

> 内容导向目录（Karpathy LLM-Wiki 规范）：每个知识域一行摘要。
> 用途：**回答前先读这里定位页面，再深入**——这是 AI 翻库的第一入口。
> 最后更新: 2026-09-05 | 页面总数: 522 | 由 knowledge-lint 维护

## 🧭 MOC 入口（主导航）

| 域 | 入口 | 规模 | 摘要 |
|:---|:---|:---|:---|
| 总地图 | [[knowledge-map]] | 522 | 全知识领域索引，W36 起新增 MOC 必须挂载 |
| Research | [[MOC-Research]] | 167 | 研究域：千轮研究、多Agent、GitHub 调研、AI 论文 |
| GitHub | [[MOC-GitHub]] | 42 | GitHub 项目实证研究（clone→测→评→可PR） |
| Security | [[MOC-Security]] | 50 | 网络安全：SRC/逆向/防御/合规 |
| Dev | [[MOC-Dev]] | 101+23 | 开发域：软件工程/前端/后端/系统 |
| Hardware | [[MOC-Hardware]] | 21 | 硬件：PCB/KiCad/FreeCAD/单片机 |
| Productivity | [[MOC-Productivity]] | 41 | 生产力：写作/PPT/文档/效率 |
| Finance | [[MOC-Finance]] | 7 | 金融：A股/量化/自选股分析 |
| Inbox | [[MOC-Inbox]] | 53 | 待接入笔记（未挂载的入口） |
| Duplicate-Review | [[MOC-Duplicate-Review]] | 0 组 | 重复审阅（当前无逐字重复） |

## 🗂 主要知识域（AI 可检索子目录）

| 目录 | 数量 | 典型内容 |
|:---|:---|:---|
| AI/ | ~15 | Agent 评估、墨题 AI 研究、知识库方法论 |
| Content/ | ~8 | 抖音 AI 博主、内容生产 |
| Daily/ | ~40 | hackernews 日报、每日回顾 |
| Development/ | ~30 | 墨题开发、部署方案、项目落地 |
| Education/ | ~5 | 考研考证规划、家教 |
| Hardware/ | ~20 | PCB/KiCad/嵌入式 |
| META/ | ~5 | 知识库治理、MOC 体系 |
| Projects/ | ~15 | 墨题、数模、闲鱼项目 |
| Research/ | ~80 | 千轮研究、Agent 评测、论文深研 |
| Security/ | ~30 | 安全策略、SRC 方法论 |
| SOP/ | ~10 | 操作流程、质量门禁 |
| cards/ | ~15 | 知识卡片（每日精选） |

## 🛠 知识库治理（META）

| 资产 | 位置 | 用途 |
|:---|:---|:---|
| 查询依据规则 | [[META/KNOWLEDGE-QUERY-RULES]] | 回答必须标来源页面（query 纪律） |
| 体检脚本 | `META/scripts/knowledge-lint.py` | 只读扫描断链/孤立/缺 frontmatter/重复 |
| 知识库方法论 | [[AI/知识库-AI不翻知识库根因-2026-09-04]] |
| 工具精度方法论 | [[AI/工具精度方法论-假阳性税与知识库Lint-2026-09-05]] | 「差的不是资料是最上面那层规则」+ AGENTS.md 实践 |
| 操作时间线 | [[log]] | 所有 ingest/lint/query 的 append-only 记录 |

## 📐 使用规则（AI 必读）

1. **回答前先读本索引**定位相关页面，再 read_file 深入；不要凭记忆作答
2. **回答必须标注依据**：说明结论来自哪些具体页面（例如「基于 知识库-AI不翻知识库根因 和 index 中的规则」），不写泛泛的「根据知识库」
3. **新页面必须挂载**：创建后 24h 内加入对应 MOC 或本索引，否则会成为孤岛
4. **有价值的回答写回**：实质性的综合分析存回 knowledge/，不收藏即止
5. **维护动作进 log**：每次 ingest/lint/query 归档追加到 log.md

---
*本文件由 k 于 2026-09-05 创建（Karpathy LLM-Wiki 规范落地）*
