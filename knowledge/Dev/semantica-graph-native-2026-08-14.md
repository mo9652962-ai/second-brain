---
tags: [ai-Infra, knowledge-graph, Graph-RAG, Provenance, Governance, 决策智能]
aliases: [semantica, Context Graph, Graph-Native Infrastructure]
date: 2026-08-14
source: https://github.com/semantica-agi/semantica
status: watch
---

# Semantica — 图原生的上下文与可审计 AI 基础设施

> **简介**：「The Open Source Palantir for AI Agents」。Graph-Native Infrastructure for Context and Accountable AI Systems（本周围绕 7,260⭐ **+4,073/周**，Python，MIT，2322 commits，活跃）。核心理念：*"Most AI agents act without a trail. They store embeddings, not meaning: context that can't be explained, decisions that can't be audited."*

## 核心思想
- 所有 Agent 的知识/决策/推理构建成**结构化、可查询的 Context Graph**
- **决策是一等对象**：可追溯、按先例搜索、因果链接（决策智能）
- **确定性推理层**：Rete 网络、Datalog、SPARQL——不是黑盒，路径可解释
- **W3C PROV-O provenance** 落在每个事实上，审计轨迹可导出 JSON/CSV/RDF
- **AI 治理与本体**：SHACL 约束、冲突检测、OWL 生成、SKOS 词表管理
- 多源接入 → 实体感知 chunking → NER/关系/事件抽取 → 语义去重 + 保留 provenance 的合并

## 为什么是「确定性」基础设施
> 坐落在 LLM、向量库、agent framework 之下：**图构建、推理、provenance 都不需要 LLM**。向量库存嵌入（相似性），Semantica 存意义（可解释的图 + 因果 + 来源）。

## 存储：Polyglot 图存储
- **RDF**：Oxigraph(嵌入式)/Blazegraph/Apache Jena/RDF4J（via SPARQL）
- **Labeled Property Graph**：Neo4j/FalkorDB/Apache AGE/AWS Neptune（via Cypher）
- 全部可换后端，不加锁。集成：Agno / MCP server / CLI / REST API。

## 核心流程（文字架构）
```
多源数据(DB/文档/网页) → 实体感知抽取 → Context Graph + KG(W3C PROV-O)
        → 确定性推理(Datalog/Rete/SPARQL) → 决策对象(可追溯/先例/因果)
        → 治理(SHACL约束/冲突检测/OWL) → 审计导出(JSON/CSV/RDF)
```

## 💎 可借鉴点（对 Obsidian/vault 最值）
1. **「存意义而非只存嵌入」**：sora 的 Obsidian + graphify 专注 markdown 链接图；Semantica 提醒可给知识库加**来源/provenance 字段**（每条笔记来自哪、何时、置信度），让知识可审计——尤其对「降低 AI 痕迹」工作流，来源可追溯 = 交付可信度。
2. **来源优先**：与 grounded-citations 技能同源但更系统（PROV-O 标准）。落地：知识库笔记 frontmatter 加 `provenance` 字段，link 到原始来源。
3. **决策可审计**：sora 各项目的「决策记录」（ADR / AGENTS.md 交接文档）可借鉴「每个决策是带因果链的对象」——写清为什么、依据什么，不仅记结论。
4. **语义去重而非静默覆盖**：导入知识冲突时**标记冲突**而非悄悄覆盖——可直接用于 vault 去重/整理（当前是覆盖式）。

## 综合评估
| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★☆（确定性推理 + 图原生设计扎实）|
| 与 sora 工作流关联 | ★★★★（知识图谱/provenance 与 graphify/Obsidian 强相关）|
| 值得安装 | 🟡 观察——偏企业级/治理场景，sora 用不上全量；借鉴 provenance + 语义去重思路即可 |
| 趋势判断 | Context Engineering + Graph-RAG 持续升温；「可审计 AI」在受监管行业是刚需 |

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]] · 平行参考：[[codebase-memory-mcp]] · [[mattpocock-skills]]