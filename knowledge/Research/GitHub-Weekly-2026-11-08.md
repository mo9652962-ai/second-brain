---
tags: [github, github-trending, weekly, 周报, W45]
title: GitHub 宝藏挖掘 - 2026-11-08
type: report
domain: Research
created: 2026-11-08
updated: 2026-11-08
status: active
source: scripts/github_treasure_hunt.py
---

# GitHub 宝藏挖掘 - 2026-11-08（W45）

> 采集口径：`scripts/github_treasure_hunt.py` 自动评分（topic 搜索 Top20 + 关注列表），Top5 按 Score 排序；**原始产出只有当次快照**，没有增长对比、没有真实性核验。
> 距上一期 [[GitHub-Weekly-2026-10-11|W41]] 相隔 **28 天 / 4 周**（W42~W44 缺档，期间无周报产出）。
> 本页在原始产出之上只补了两件事：① 按 W41 快照回算 28 天 star 变化；② 把「核验过 / 没核验」分开写清。原始条目文本保留不动。

## Top 5（含 28 天 star 变化）

| # | 项目 | 11-08 ★ | 10-11 ★ | 28 天变化 | Score |
|:--|:--|--:|--:|:--|--:|
| 1 | DeusData/codebase-memory-mcp | 48,311 | 46,325 | +1,986（+4.3%，日均 ~71） | 81 |
| 2 | tirth8205/code-review-graph | 32,638 | 32,029 | +609（+1.9%，日均 ~22） | 74 |
| 3 | ChromeDevTools/chrome-devtools-mcp | 54,942 | 53,255 | +1,687（+3.2%，日均 ~60） | 69 |
| 4 | sansan0/TrendRadar | 63,520 | 62,790 | +730（+1.2%，日均 ~26） | 63 |
| 5 | langgenius/dify | 160,643 | — | 首次进榜 | 62 |

### 1. DeusData/codebase-memory-mcp (48,311⭐) [🔴]
- Score: 81/100 | Lang: C | License: MIT
- Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent integrations and change-aware test selection.
- URL: https://github.com/DeusData/codebase-memory-mcp
- 增长：46,325（10-11）→ 48,311（11-08），28 天 **+1,986⭐（+4.3%）**，日均 ~71，仍在上行通道
- 本库旧笔记对照：[[knowledge/Dev/codebase-memory-mcp|Codebase Memory MCP 学习笔记]] 记于 07-27 的 38.2K★ → 现 48.3K★（104 天 +10,111⭐）

### 2. tirth8205/code-review-graph (32,638⭐) [🔴]
- Score: 74/100 | Lang: Python | License: MIT
- Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo w
- URL: https://github.com/tirth8205/code-review-graph
- 增长：32,029（10-11）→ 32,638（11-08），28 天 **+609⭐（+1.9%）**，增速回落到平台期
- 本机落地（观察）：工作区根 `.code-review-graph/graph.db` 现 **107MB**，今天 14:47 仍在写入 → 这套工具在本库是**在用状态**，不是收藏

### 3. ChromeDevTools/chrome-devtools-mcp (54,942⭐) [🟡]
- Score: 69/100 | Lang: TypeScript | License: Apache-2.0
- Chrome DevTools for coding agents
- URL: https://github.com/ChromeDevTools/chrome-devtools-mcp
- 增长：53,255（10-11）→ 54,942（11-08），28 天 **+1,687⭐（+3.2%）**，本期增速最快的一项

### 4. sansan0/TrendRadar (63,520⭐) [🟡]
- Score: 63/100 | Lang: Python | License: GPL-3.0
- ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，
- URL: https://github.com/sansan0/TrendRadar
- 增长：62,790（10-11）→ 63,520（11-08），28 天 **+730⭐（+1.2%）**

### 5. langgenius/dify (160,643⭐) [🟡]
- Score: 62/100 | Lang: Python | License: NOASSERTION
- Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from prototype to production without reb
- URL: https://github.com/langgenius/dify
- 本期新面孔：**160.6K★** 的 Agent 工作流平台首次进 Top5，榜单从「单点工具」往「平台」扩了一档
- ⚠️ License 字段是 `NOASSERTION`（GitHub 未能归类为 SPDX 标准许可），商用/二次分发前要自己读一遍条款

## MCP 生态发现

- **DeusData/codebase-memory-mcp** (81/100): Local code intelligence for developers and AI agents. Connect code, docs and infrastructure in a persistent graph, with CBM Lens, MCP tools, agent int
- **tirth8205/code-review-graph** (74/100): Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmar
- **ChromeDevTools/chrome-devtools-mcp** (69/100): Chrome DevTools for coding agents

## 洞察

1. **MCP 持续成为 Agent 标准接口** — 5 项里 3 项直接是 MCP 服务端（codebase-memory / code-review-graph / chrome-devtools-mcp），「代码知识图谱」类从 W31 起连续第 4 个月在榜。
2. **本地优先是主流趋势** — 前三项都能完全离线自托管（单静态二进制 / 本地图谱 / 本地 DevTools），与本机「无 Docker、无虚拟化」的约束天然契合；`.code-review-graph/graph.db` 107MB 是本机在用的硬证据。
3. **记忆系统是核心突破点** — 上榜项目争的还是同一件事：让 Agent 在有限上下文里拿到精准信息（图谱索引 / 上下文压缩 / 变更感知）。
4. **平台开始挤进工具榜** — dify 首次进榜说明「工作流平台」和「单点 MCP 工具」在同一个评分池里竞争；这对选型有影响：工具可以换，平台换了要迁移全部编排。
5. **nanobot 掉榜原因未知** — W41 时 48,941★（高于本期第 1 名），本期未进 Top5。脚本不输出各分项得分，**原因不明，不做推断**（可能是 Score 分项权重，也可能是本期 topic 抓取集合变化）。

## 真实性核验状态

| 项目 | 状态 | 依据 |
|:--|:--|:--|
| codebase-memory-mcp | ✅ W41 已核验 | commits 3,645 / 100+ contributors / v0.11.0（见 [[GitHub-Weekly-2026-10-11]]） |
| code-review-graph | ✅ W41 已核验 | commits 1,229 / 100+ contributors / v2.3.9 |
| chrome-devtools-mcp | ✅ W41 已核验 | 官方 ChromeDevTools 组织仓库 |
| TrendRadar | ✅ W41 已核验 | 持续在榜，GPL-3.0 |
| dify | ❓ **未核验** | 首次进榜；160.6K★ + NOASSERTION 许可，商用前需自查 |

> 口径提醒：本期**没有重跑** commits / contributors / releases，上表「已核验」指的是 W41 那次的结论，不是本期实测。

---
*自动生成 2026-11-08 14:45 · 整理 2026-11-08（补 frontmatter / 28 天 delta / 核验状态标注，原始条目文本未改）*

---
> 🗺️ 属于 [[knowledge/Research/MOC-GitHub|MOC-GitHub]] · [[knowledge/Research/MOC-Research|MOC-Research]] · [[Home|🏠 Home]]
