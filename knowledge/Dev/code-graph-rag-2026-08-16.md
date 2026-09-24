---
tags: [code-RAG, knowledge-graph, monorepo, mcp, tree-sitter, W34]
aliases: [code-graph-rag, cgr]
date: 2026-08-16
source: https://github.com/vitali87/code-graph-rag
status: watch
---

# code-graph-rag — monorepo 知识图谱 RAG

> **简介**：vitali87 出品，「the ultimate RAG for your monorepo」——多语言代码库的查询/理解/编辑，知识图谱驱动。本周 4,381⭐ **+1,756/周**（Python，MIT，**4,993 commits** 极度活跃，版本号已到 0.0.657 高频迭代）。

## 核心思路

1. **AST 精度优先于 embedding**：用 tree-sitter 解析多语言（Python/JS/TS/C# 等）→ 构建符号级知识图谱（Folder/File/Function/Class 节点 + 调用边），而非向量嵌入——对 monorepo 精确检索。
2. **Memgraph 图数据库**：知识图谱存 Memgraph（图数据库），支持复杂图查询（跨文件调用链、依赖影响面）。
3. **动态调用追踪**：最近 commit 加了 Python runtime call tracing——静态 AST 之外补**动态 CALLS 边**（真实运行时调用），静态+动态结合。
4. **MCP server + CLI 双入口**：`cgr` CLI + MCP server 供 Claude Code 等 agent 消费——查询、理解、编辑代码库。
5. **OpenCore 商业化**：开源核心 + 商业版（Cloud-Hosted / On-Premise Air-Gapped + 定制开发 + 咨询），企业数据主权场景收费。

## 精妙细节

- **benchmarks/ + evals/ 目录**：自带基准和评测——不只是工具，是可验证的 RAG 系统。
- **source-map 解析报告**：JS/TS source-map 解析率上报 + 失败分类——可观测性做到位。
- **blake3/orjson 可选加速**：依赖可选，轻量部署。
- **protobuf 覆盖导出**：codec 层做 protobuf round-trip，数据结构严谨。

## 💎 可借鉴点（对 sora 最值）

1. **与已装 code-review-graph MCP 同赛道对比**：sora 已装 tirth8205/code-review-graph（local-first code intelligence graph，本周也 30.3k⭐ 连榜）。对比：code-review-graph 本地优先 SQLite、code-graph-rag 用 Memgraph + 动态调用追踪。**动态 CALLS edge（运行时 tracing 补静态 AST）是独特思路**——sora 的代码理解工具可关注这个「静态+动态」混合信号。
2. **「AST 图而非 embedding」的取舍**：对 monorepo 精确检索，符号图 + 调用链远好于向量相似度——sora 的代码库检索（墨题项目、PCB 脚本库）如果遇到 embedding 召回不准，可考虑轻量 AST 图方案（tree-sitter 已有 Python 绑定）。
3. **OpenCore 分层变现**：开源核心打口碑 + 企业版（on-prem/air-gapped + 定制）收费——sora 的 AI 服务（闲鱼接单升级）或未来产品可参考这个分层。
4. **自带 evals 门禁**：每个 RAG/工具项目都应带 benchmarks——sora 的评估工程方法论（PawBench）与此同频。

## 综合评估

| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★☆（AST+图数据库+动态追踪，工程量大、迭代猛）|
| 与 sora 工作流关联 | ★★★☆☆（已有 code-review-graph MCP 覆盖同类需求，不重复装；方法论值得吸收）|
| 值得安装 | 🔵 不装——与 code-review-graph 功能重叠，但关注动态调用追踪进展 |
| 趋势判断 | 代码图谱 RAG 赛道拥挤（codebase-memory-mcp / code-review-graph / code-graph-rag），「动态+静态混合」是差异化方向 |

> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]] · 平行参考：[[codebase-memory-mcp]]（已入库）· `code-review-graph`（sora 已装 MCP）· [[semantica-graph-native-2026-08-14]]（图原生 AI 基础设施）
