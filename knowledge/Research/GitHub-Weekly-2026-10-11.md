---
tags: [github, github-trending, weekly, 周报, W41]
title: GitHub 宝藏挖掘 - 2026-10-11
type: report
domain: Research
created: 2026-10-11
updated: 2026-10-11
status: active
source: scripts/github_treasure_hunt.py
---

# GitHub 宝藏挖掘 - 2026-10-11（W41）

> 采集口径：topic 搜索 Top20 + 关注列表 7 项，共 25 个项目进入评分。
> 距上一期 [[GitHub-Weekly-2026-09-20|W39]] 相隔 3 周（W40 缺档）。

## Top 5

### 1. DeusData/codebase-memory-mcp (46,325⭐) [🔴]
- Score: 88/100 | Lang: C | License: MIT | 创建 2026-02-24 | 最后推送 2026-10-10
- High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 158 languages, sub-ms queries, 99% fewer tokens. Single static binary
- URL: https://github.com/DeusData/codebase-memory-mcp
- 增长：43,848（09-20）→ 46,325（10-11），21 天 **+2,477⭐**（周均 ~825，仍在加速）
- README 实证：162 语言 tree-sitter AST + Hybrid LSP（10 语言语义类型解析）；Linux 内核 28M LOC / 75K 文件全量索引 3 分钟；17 个 MCP 工具；8050 测试通过；arXiv 2603.27277；SLSA 3 + VirusTotal 每版扫描

### 2. HKUDS/nanobot (48,941⭐) [🔴]
- Score: 81/100 | Lang: Python | License: MIT | 创建 2026-02-01 | 最后推送 2026-10-11
- Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps
- URL: https://github.com/HKUDS/nanobot
- 增长：48,375 → 48,941，21 天 +566⭐（增长趋缓，进入平台期）
- README 实证：PyPI `nanobot-ai`（Python ≥3.11）；WebUI/终端/聊天应用三入口；内置 Dream 长期记忆、模型路由与 fallback、cron 定时自动化、OpenAI 兼容 API、Python SDK；渠道覆盖 Telegram/Discord/Slack/WeChat/Email/Mattermost/Linear；11 语言文档

### 3. tirth8205/code-review-graph (32,029⭐) [🔴]
- Score: 74/100 | Lang: Python | License: MIT | 创建 2026-02-26 | 最后推送 2026-10-06
- Local-first code intelligence graph for MCP and CLI. Builds a persistent map of your codebase so AI coding tools read only what matters, with benchmarked context reductions on reviews and large-repo w
- URL: https://github.com/tirth8205/code-review-graph
- 增长：31,623 → 32,029，21 天 +406⭐
- README 实证：flask 全量语料 143,594 tokens → 图谱答案 2,196 tokens（**65x 压缩**）；一条命令 `install` 自动探测并配置 16 个平台（含 **Hermes Agent**、Codex、Claude Code、Cursor、Antigravity、CodeBuddy）；`uninstall` 原子回滚，不动其他 MCP/hook

### 4. ChromeDevTools/chrome-devtools-mcp (53,255⭐) [🟡]
- Score: 69/100 | Lang: TypeScript | License: Apache-2.0 | 最后推送 2026-10-11
- Chrome DevTools for coding agents
- URL: https://github.com/ChromeDevTools/chrome-devtools-mcp
- 增长：52,339 → 53,255，21 天 +916⭐

### 5. sansan0/TrendRadar (62,790⭐) [🟡]
- Score: 63/100 | Lang: Python | License: GPL-3.0 | 最后推送 2026-10-10
- ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts. 聚合多平台热点 + RSS 订阅 + 关键词精准筛选 + AI 筛选/翻译/分析简报直推手机，支持 MCP
- URL: https://github.com/sansan0/TrendRadar

## MCP 生态发现

- **DeusData/codebase-memory-mcp** (88/100): 代码库→持久知识图谱，162 语言，亚毫秒结构查询，17 个 MCP 工具，单静态二进制零运行时依赖
- **HKUDS/nanobot** (81/100): 自托管 Agent 运行时，MCP + 长期记忆 + 多 Agent 委派 + cron 自动化，OpenAI 兼容 API
- **tirth8205/code-review-graph** (74/100): 本地代码知识图谱，MCP 服务 review 场景上下文，65x token 压缩，已原生支持 Hermes Agent

## 洞察

1. **「代码知识图谱」三连榜**：codebase-memory-mcp / code-review-graph 均已连续 9 期上榜，MCP 已成 Agent 上下文压缩的默认接口——三者共性是把「读文件」换成「查图」。
2. **本地优先 + 自托管是主流**：Top5 全部可离线自托管（nanobot 甚至主打「小而可读的内核」），与本机无虚拟化、无 Docker 的部署约束天然契合。
3. **记忆/上下文仍是核心突破点**：本期 3 个 🔴 全部指向同一问题——如何让 Agent 在有限上下文里拿到精准信息（图谱索引、记忆持久化、token 压缩）。
4. **Hermes 生态开始被第三方主动适配**：code-review-graph 的 `install` 已内置 hermes 平台配置，说明 Hermes 在 Agent 工具链中已具备被兼容的地位。

---
*自动生成 2026-10-11 13:45 · 增强整理 2026-10-11*

---
> 🗺️ 属于 [[MOC-GitHub]] · [[MOC-Research]] · [[Home|🏠 Home]]
