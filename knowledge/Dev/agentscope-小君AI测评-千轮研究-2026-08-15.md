---
tags: [agentscope, 小君AI测评, AI评估, 千轮研究, 项目评估]
type: research
date: 2026-08-15
status: adopted
---

# AgentScope（小君AI测评）千轮研究报告

> 2026-08-15 · clone 实证 + 搜索引擎多轮 + 测试验证
> 仓库: github.com/Joho6666/xiaojunceping

## 结论置顶

**方向有学术基础和市场需求，但项目是早期原型**：3 stars、11 commits、6188 行代码、7 个测试 4 过 3 挂（有真实 bug）。**「项目→全套 AI 方案推荐」是差异化，但「AgentScope」名字与阿里框架撞车是风险**。

## 实证数据

| 指标 | 值 |
|:---|:---|
| Stars / Forks | 3 / 0（很新，2026-08-13 创建）|
| Commits | 11（2 天开发）|
| 代码量 | 6188 行 TS/TSX（app+components+services+ai+scripts）|
| 技术栈 | Next.js 14.2.35 + React 18.3 + better-sqlite3 + Tailwind 3.4 |
| 依赖 | 极简（3 个运行时依赖，AI 调用全原生 fetch）|
| 测试 | 7 个脚本，**4 过 3 挂**（SQLITE_CONSTRAINT_PRIMARYKEY）|

## 功能全景（README + 代码实证）

1. **项目输入**：描述 + Quick/Expert 模式 + 模型选择（绑定项目不静默切换）
2. **Provider**：Codex/Claude/Gemini CLI 适配器 + DeepSeek + 自定义 OpenAI-compatible
3. **知识库**：本地 SQLite，种子 105 条（模型/Agent/Skill/MCP/Plugin/GitHub 项目），带 lifecycle/sourceType/来源核验
4. **研究链**：需求画像 → 知识库检索 → GitHub/官方源补充 → 规则过滤（knowledgeRuleEngine：失效/敏感/平台/评分）
5. **输出**：Agent 队列 + 模型角色路由 + 能力矩阵 + Workflow + Token/时间/成本估算 + 风险 + Prompt 生成（Codex/Claude Code/Cursor/OpenCode 模板 + AGENTS.md）
6. **安全**：API Key 只进服务端、CLI 不读 OAuth 文件、无 Provider 明确失败不伪造

**亮点**：精确模型目录（DeepSeek v4-flash/pro 价格、上下文 1M、旧 ID 迁移提示——与社区 2026-07-24 废弃一致）、来源核验（official/github/registry 分级）、evaluation-agent.md 工作流设计严谨（工具边界/不编造/无结果明确显示）。

## 竞品格局（搜索引擎实证）

| 类别 | 玩家 | 与小君差异 |
|:---|:---|:---|
| **同名框架** | 阿里 AgentScope（通义实验室，Apache 2.0，2.0 版本）| **撞名风险**；阿里是开发框架，小君是评估平台 |
| **Agent 推荐学术** | AgentSelect（arXiv 2603.03761：111K 查询×107K agents）| 学术证明「agent 推荐」方向成立 |
| **模型选型工具** | modelcompare.dev / BenchLM / Ofox / chooseaimodel.com（377 模型 51 provider）| 竞品只做「选模型」；小君做「全套方案」 |
| **评估框架** | OpenAI Evals / SWE-bench / OpenJudge（50+ graders）/ PawBench（Model×Harness，Hermes 是 3 个 Harness 之一）| 评估「已用方案」质量；小君推荐「该用什么」 |
| **真实任务基准** | SWE-Lancer（1400 Upwork 任务/$1M）| 与闲鱼接单场景直接相关 |

## 发现的真实 Bug（实证）

**seed 数据重复 id → 知识库初始化主键冲突**：
- `mcp-brave-search`、`plugin-github-copilot` 在两个 catalog 各出现一次
- `seedIfEmpty` 用裸 INSERT（无 ON CONFLICT）→ 首次初始化即崩
- 导致 test:knowledge / test:knowledge-coverage / test:discovery 3 个测试失败
- 修复：删 expansion 里的重复条目（或改 id）；seedIfEmpty 改 upsert 更稳

## 对 sora 的价值

1. **参考架构**：本地知识库 + 来源核验 + 规则引擎的「AI 选型」实现思路可借鉴（Hermes 已有 memory/skills，可做类似「项目→方案」工具）
2. **内容素材**：AI 博主方向——「AI 测评」主题的竞品分析/工具测评是好素材
3. **SWE-Lancer 关联**：AI 能力×真实任务经济价值，闲鱼接单场景的研究佐证
4. **PawBench 发现**：同一模型在不同 Harness 分数差 10+ 分——「工具/框架选择」比「模型选择」更影响结果（呼应 Hermes↔dsh 联合工作）

## 建议

- 若想用/改：可 PR 修复重复 id bug（2 分钟），项目可作为「AI 方案推荐」方向的参考实现
- 名字撞车警告：若要商业化/发布，改名避免与阿里 AgentScope 混淆
- 深度使用前：等它把测试修绿 + 补充多用户/部署方案（README 自述「正式多用户部署前需接数据库/账户隔离/CSRF」）

---
*数据截止 2026-08-15 · clone 自 github.com/Joho6666/xiaojunceping（commit 5d926a4）*

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
