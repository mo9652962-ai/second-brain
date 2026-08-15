---
tags: [agentscope, 架构参考, PawBench, harness, 千轮研究, AI测评]
type: research
date: 2026-08-15
status: adopted
---

# 小君AI测评架构参考 + PawBench 深度分析

> 2026-08-15 · 基于 Joho6666/xiaojunceping 代码实证 + agentscope-ai/PawBench 官方数据

## 一、小君「本地知识库 + 来源核验 + 规则引擎」架构拆解

### 数据层（knowledgeBaseService.ts）

- better-sqlite3 本地库（`.agentscope/knowledge.sqlite`，WAL 模式）
- 种子 103 条（官方数据 + 扩展数据 + 精确模型目录），每条带：
  - `sourceType`: official / github / registry / provider-discovered（**来源分级**）
  - `sourceUpdatedAt` + `verifiedAt`（**时间戳核验**）
  - `confidence`: 高/中/低（**可信度分级**）
  - `lifecycle`: stable / preview / deprecated（**生命周期**，旧 ID 自动标 stale 提示迁移）
- 动态同步：连上 Provider 调 `/models` API → 真实模型 ID 入库标 `provider-discovered`（"Provider 已发现，需官方模型卡继续核验"）

### 检索层（knowledgeRetrievalService.ts）

- **词袋匹配**（无向量依赖）：profile 的 tags/capabilities/stack/domain 分词 → 与条目 name/summary/tags 双向子串匹配
- **评分**：35 基础分 + 8/命中词 + confidence 权重（高15/中8/低2），封顶 99，Top 30

### 规则层（knowledgeRuleEngine.ts）

- 失效条目过滤（status/publication）
- 高敏感数据不推仅云端方案
- 平台匹配（Self-host 需求 → 必须有本地平台）
- verifiedAt 加分（+5）

### 核验层（knowledgeSyncService + githubService）

- 同步时从 GitHub Search API 拉真实仓库（star/license/主题），upsert 进知识库
- 报告只出「已发布 + status 有效 + source_url 是 http」的条目（listKnowledgeItems 的防御性过滤）

### 关键设计亮点

1. **「报告不包含未经核验的模型输出」**——无 Provider 时明确失败，不回退假报告（README 承诺 + 代码实践一致）
2. **精确模型 ID 与展示名分离**——名称只是展示，`modelId` 才是调用 ID（DeepSeek v4-flash/pro、Gemini 3.5 Flash 等都有精确 ID + 价格）
3. **旧 ID 迁移提示**——`deepseek-chat` deprecated → 提示用 v4-flash/pro（与社区 2026-07-24 废弃一致）

## 二、PawBench：工具/框架选对了比模型选对了更值钱

### 基准设置（agentscope-ai/PawBench v1.0, 2026-05-29）

- **150 任务 × 9 模型 × 3 Harness = 4050 单元**（Docker 沙箱，保留 traces/grader artifacts）
- 3 个 Harness：**Hermes** v2026.4.23 / **OpenClaw** v2026.4.24 / **QwenPaw** v1.1.3
- Judge: claude-opus-4.6

### 完整评分矩阵（Hermes 被完整评测了！）

| Model | Hermes | OpenClaw | QwenPaw | Δ |
|:---|:---|:---|:---|:---|
| claude-opus-4.6 | **78.4** 🥇全场第一 | 76.1 | 78.3 | 2.3 |
| deepseek-v4-pro | 72.1 | 75.4 | 75.6 | 3.6 |
| qwen3.7-max | 72.3 | 72.5 | 77.6 | 5.4 |
| qwen3.6-max-preview | 68.1 | 75.1 | 78.3 | 10.3 |
| qwen3.6-plus | 70.4 | 73.6 | 75.0 | 4.6 |
| qwen3.6-27b | 68.2 | 72.9 | 72.7 | 4.7 |
| glm-5.1 | 63.2 | 68.5 | 71.1 | 7.9 |
| kimi-k2.6 | 66.4 | 66.6 | 66.6 | 0.2 |
| qwen3.6-35b-a3b | 56.7 | 67.8 | 68.3 | **11.5** |
| **平均** | **68.4** | 72.1 | 73.7 | |

### 三大发现

**Finding 1：小模型更需要 Harness 稳定执行**
- claude-opus-4.6 跨 harness 仅 2.3 分差（大模型能补上下文：推断路径/过滤工具表/检查产物）
- qwen3.6-35b-a3b 差 **11.5 分**（小模型易忘 cwd、误判文件写入、工具表太大选错第一个工具）
- **工具表大小：Hermes ~65 / OpenClaw ~30 / QwenPaw ~15——工具太多对小模型是决策负担**

**Finding 2：Skill 使用 = 发现 + 模型跟进**
- Skill 任务三 harness 都难（Hermes 44.6 / OpenClaw 52.5 / QwenPaw 44.5）
- Hermes 扫 `~/.hermes/skills/` 但**容易漏 workspace 内 Skill**；OpenClaw 扫 workspace 渲染进 available_skills（最好）
- 模型侧：harness 指了路，模型还得跟进（复杂推理/精确计算仍会失败）

**Finding 3：Web 搜索取决于默认可用性**
- Hermes 的 web_search/web_extract 需外部 API key——**默认体验差**（评分环境只有 LLM key 时不可用）
- OpenClaw web_search 用 DuckDuckGo 免 key 开箱即用
- QwenPaw 无专用搜索，browser_use 兜底

### 核心结论（sora 说的「工具选对 > 模型选对」实证）

1. **同模型跨 harness 分差（最高 11.5）≈ 模型升级差距**——qwen3.6-plus+QwenPaw(76.5) > qwen3.6-max-preview+Hermes(70.2)
2. **强模型 + Hermes = 最强组合**（claude-opus-4.6+Hermes 78.4 全场第一）——Hermes 的丰富工具面在强模型手里是优势
3. **弱模型在 Hermes 上最吃亏**（35b-a3b 只有 56.7）——65 工具表 + 需要 key 的 web 搜索

### 对咱们联合工作的启示

| 现状 | 启示 |
|:---|:---|
| sora 用 deepseek-v4-flash（弱快模型）+ Hermes 做日常 | 按 PawBench 弱模型在 Hermes 吃亏 → 但咱们重任务走云端强模型，日常简单任务影响小 |
| dsh（DeepSeek Harness）纯文本任务最稳 | 印证「精简 harness + 中等模型」组合（类似 QwenPaw 路线）|
| Hermes 默认工具多 | 可针对性精简 enabled_toolsets（cron 已这么做）|
| Hermes web 搜索要 key | 搜索兜底链已配（exa/Firecrawl/DDG/Bing/CDP）——比默认体验强 |

## 三、可借鉴到 Hermes 体系的 3 个动作

1. **知识库核验意识**：评价模型/工具时标注来源分级（official/github/实测）+ 时间戳——日常评估已按此实践（实证评估原则）
2. **模型目录快照**：把常用模型 ID + 价格 + lifecycle 做成一个 notes 条目（小君 modelKnowledgeCatalog 思路）——防旧 ID 踩坑
3. **Skill 发现改进**：PawBench 指出 Hermes 漏 workspace Skill——咱们的技能放在 `~/AppData/Local/hermes/skills/`（Hermes 主目录），不放在项目 workspace——方向正确，但项目级 skill 可以考虑放 workspace 供 OpenClaw 式发现

---
*数据源：PawBench v1.0 leaderboard (2026-05-29) · agentscope-ai/PawBench GitHub · tongyilab.substack.com/p/the-harness-gap*
