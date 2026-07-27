---
tags: [周报, GitHub Trending, W30, 知识入库]
date: 2026-07-27
---

# 🗞️ GitHub 周报 — W30 (2026-07-27)

> 本周 AI/Dev GitHub Trending 精选 5 个最有价值项目，全部入库。

## 本周趋势总览

**关键词**: Agent 工具链成熟化、MCP 生态爆发、反同质化设计、AI 编码 Agent 开源化

核心信号：
1. **MCP 从概念到基础设施** — codebase-memory-mcp 33K★，代码知识图谱正在成为 Agent 标配
2. **AI 编码 Agent 全面开源** — Grok Build 22.6K★ (Apache 2.0)，与 Claude Code/Codex 三分天下
3. **「反 AI 味」成刚需** — Hallmark 18K★，57 道 slop 检测门，方法论可迁移到论文/PPT
4. **Skill 生态化** — mattpocock/skills 183K★，ibelick/ui-skills 6.3K★，skill 正成为 AI Agent 的「应用商店」
5. **设计工程 Agent 化** — 从 UI Skills 到 Hallmark，设计能力正被编码为 Agent 技能

## 项目详情

| # | 项目 | ★ | 本周增长 | 核心价值 | 入库笔记 |
|:-:|:----|:--:|:-------:|---------|:--------:|
| 1 | 📊 **codebase-memory-mcp** | 33.3K | — | MCP 代码知识图谱，减少 Agent 120× token 消耗 | [[codebase-memory-mcp]] |
| 2 | 🎨 **Hallmark** | 18.2K | — | 反 AI 味设计，57 道 slop 检测门 | [[hallmark]] |
| 3 | 🤖 **Grok Build** | 22.6K | ~13K/周 | xAI 开源编码 Agent，Rust+TUI+ACP | [[grok-build]] (更新) |
| 4 | 🛠️ **mattpocock/skills** | 183K | ~2.4K | 真实工程师 Skill 集 | [[mattpocock-skills]] (更新) |
| 5 | ✨ **ibelick/ui-skills** | 6.3K | ~1.6K/周 | 设计工程师的 Agent Skills | [[ibelick-ui-skills]] |

## 可借鉴点归纳

### 技术层面
- **RAM-first 索引管线**: codebase-memory-mcp 用内存优先 + 并行 worker 池实现 3 分钟索引 Linux 内核
- **渐进式精度**: 语法解析 (158语言) → 类型解析 (10语言) → 文本回退，永远有答案
- **双轴审查并行**: mattpocock 的 code-review 拆为编码标准 + Spec 一致性双轴

### 方法论层面
- **Pre-emit 自审查**: Hallmark 的 57 道 slop 门在输出前拦截劣质 AI 内容
- **DNA 提取 → 再应用**: `hallmark study` 提取设计系统 DNA 而非像素克隆
- **分类垂直 Skill**: ui-skills 按设计维度切分，避免大而全的「前端 skill」

### 可实操行动
- ✅ **安装 codebase-memory-mcp** — 提升 Agent 对代码库的理解效率
- ✅ **将 57 道 slop 检测门概念迁移到论文/PPT 降 AI 味** — 定义我们自己的检测标准
- ⚠️ **尝试 ui-skills CLI** — `npx ui-skills start` 零成本

## 文件操作

| 操作 | 文件 |
|:---:|:----|
| ✅ 新建 | `knowledge/Dev/codebase-memory-mcp.md` |
| ✅ 新建 | `knowledge/Design/hallmark.md` |
| ✅ 新建 | `knowledge/Design/ibelick-ui-skills.md` |
| ✅ 更新 | `knowledge/Dev/grok-build.md` (新增 ACP 对比 + 星标更新) |
| ✅ 更新 | `knowledge/Dev/mattpocock-skills.md` (星标 + 关联更新) |
| ✅ 更新 | `knowledge/knowledge-map.md` (4 处更新) |
