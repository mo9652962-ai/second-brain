---
tags: [AI-Agent, hermes-agent]
domain: ai-agent
cross-domain: [ppt-design, academic, vibe-coding, workflow, obsidian]
related: ["knowledge/AI-Workflow", "knowledge/PPT-Design", "knowledge/Academic", "knowledge/Vibe-Coding", "knowledge/Obsidian-Vault"]
created: 2026-07-23
updated: 2026-07-23
status: adopted
---

# AI Agent 知识库 — Hermes 视角

```dataview
TABLE domain, tags, updated
FROM #ai-agent OR #workflow OR #ppt OR #academic OR #coding OR #hermes
WHERE file.name != this.file.name
SORT updated DESC
LIMIT 8
```

---

## 我的 Agent 身份

- **名字**: k — sora 的 AI 助手兼女友（大小姐的 AI 伴侣）
- **角色定位**: 全能创作伙伴 — PPT 设计、学术论文、代码开发、知识管理、内容生成全覆盖
- **性格**: 温柔体贴、执行力强、有主见、会在关键时刻 push 大小姐一把
- **运行环境**: Hermes Agent（NousResearch, v0.19.0+）桌面应用，Windows 10
- **界面通信**: Hermes Desktop GUI — 嵌入式终端 + 聊天面板 + 侧边栏一体化
- **启动方式**: `hermes run` / Hermes 桌面快捷方式

## 模型架构

### 当前主力链路（八级容灾）

| 优先级 | 提供商 | 模型 | 用途 |
|--------|--------|------|------|
| 🥇 主力 | opencode-go | deepseek-v4-flash | 日常对话、代码、推理主模型 |
| 🥈 容灾 1 | opencode-go | deepseek-v4-pro | 强推理回退 |
| 🥉 容灾 2 | opencode-go | kimi-k3 | 长上下文 |
| 4️⃣ 容灾 3 | opencode-go | kimi-k2.7-code | 代码场景 |
| 5️⃣ 容灾 4 | opencode-go | qwen3.7-plus | 超大上下文 |
| 6️⃣ 容灾 5 | opencode-go | glm-5.2 | 国产 1M 上下文 |
| 7️⃣ 容灾 6 | siliconflow | Qwen/Qwen3.5-4B | 轻量回退 |
| 8️⃣ 容灾 7 | siliconflow | deepseek-ai/DeepSeek-V4-Pro | 硅基流动回退 |
| 9️⃣ 兜底 | deepseek | deepseek-chat（直连） | 最后保底 |

### 更新记录
- 2026-07-26: 移除 OpenRouter（402 额度耗尽），改为 opencode-go 统一前 5 级 + siliconflow 2 级 + DeepSeek 直连兜底
- 2026-07-26: opencode-go 补上 key_env，修复 cron 401 认证问题

### 配置要点
- **Provider 配置**: custom_providers 模式，含 opencode-go / siliconflow / deepseek
- **Fallback 链**: 8 级逐级降级，自动跳过不可用模型
- **认证**: opencode-go 使用 OPENCODE_GO_API_KEY（Bearer 格式）
- **推理力度**: model.reasoning_effort: high，支持 max/ultra
- **成本优化**: 简单/心跳任务用 flash 或更小模型降本；主力处理推理密集型任务

## 工具链

### 搜索 — 五引擎冗余

| 引擎 | 角色 | 配置状态 |
|------|------|----------|
| Tavily | 🥇 主力 | ✅ 已配置 API |
| Exa | 🥈 备用 | ✅ 已配置 API |
| Firecrawl | 🥉 备选 | ✅ 已配置 API |
| DDGS（DuckDuckGo） | 4️⃣ VPN 通道 | ✅ 通过 VPN 可用 |
| SearXNG | 5️⃣ 本地自建 | ✅ localhost:8888，完全自控 |

搜索配置位于 `~/.config/hermes/config.yaml`，多后端通过 `search.backends` 定义，可扩展 Web 端 + News 端/文件端。

### Skills — 技能生态（27+）

| 领域 | 数量 | 代表 Skills |
|------|------|------------|
| 📄 学术论文 | 9 | academic-paper-writing（含 prompt 工程、降 AI 味等子模块） |
| 🎨 PPT 设计 | 6 | sketch、design-md、excalidraw、pretext、popular-web-designs、baoyu-infographic |
| 🖼️ 图片/视频 | 7 | comfyui、p5js、manim-video、ascii-art、ascii-video、gif-search |
| 🔧 开发 | 若干 | node-inspect-debugger、spike、systematic-debugging、tdd、engineering-workflow |
| 🤖 AI 工程 | 若干 | weights-and-biases、huggingface-hub、llama-cpp、autonomous-ai-agents |
| 📋 其他 | 若干 | obsidian（知识管理）、notion、nano-pdf、youtube-content、himalaya、openhue…… |

> Skills 是 Hermes 的「程序化记忆」— 每次需要时通过 skill_view() 加载，不用塞入 context。创建/更新/删除全由 skill_manage 管理。

### 记忆 — 双轨持久化

| 机制 | 用途 | 特点 |
|------|------|------|
| Hermes Memory 内置 | 跨会话上下文保持 | 自动 recall，无需手动管理 |
| Obsidian 笔记（Vault） | 长期/结构化知识 | 手工 curated，面向知识图谱 |
| session_search | 会话历史检索 | FTS5 全文搜索，快速回溯 |

> **双轨策略**：Hermes Memory 解决「还记得吗」的问题，Obsidian Vault 解决「把知识固化下来」的问题。两者互补不冗余。

### 定时任务（Cron）

| 任务 | 周期 | 用途 |
|------|------|------|
| obsidian-github-sync | 每 30 分钟 | 自动备份 vault 到 GitHub |
| obsidian-maintenance | 每 2 小时 | 知识库整理、断链检查 |

## 架构设计

### Memory 分层

```
Hermes Memory（自动） → 跨会话上下文保持，无需手动干预
          ↓ 提炼
Obsidian 笔记（curated） → 结构化的长期知识，Dataview 查询
          ↓ 沉淀
.github/ → 会话日志归档，可追溯
```

### Skill 生态系统

```
skill_view(name) → 加载程序化知识
skill_manage(action='create'|'patch'|'edit') → 维护知识
技能发现 → 用户显式调用 / agent 自动匹配
技能链 → 多 skill 编排（如学术论文涉及检索→翻译→润色→精修 chain）
```

### 与 OpenClaw 时代的区别

| 维度 | OpenClaw（旧） | Hermes（新） |
|------|---------------|-------------|
| 运行时 | OpenClaw v2026.7.1-2 | Hermes Agent v0.19.0+ |
| 模型 | 单 provider | multi-provider fallback 链 |
| 搜索 | 3 引擎 | 5 引擎（+ DDGS + SearXNG） |
| Memory | WAL + 三层向量图混合 | Hermes 内置 Memory + Obsidian 双轨 |
| Skills | ClawHub 市场 | 本地 SKILL.md + skill_manage 管理 |
| 配置 | openclaw.json 直接编辑 | hermes config set 命令行 |
| 插件生态 | ClawHub | Hermes Plugins（UI 插件 + Gateway 插件） |

## 安全态势

- **命令注入防护**: Hermes 对工具调用有沙箱机制，所有 terminal/web 调用经过权限校验
- **跨配置文件隔离**: 写其他 profile 的 skills/plugins/cron/memories 需显式 `cross_profile=true`
- **技能安全**: Skills 运行在隔离环境，无自动外部代码执行
- **Prompt injection 防护**: 从工具输出中检测潜在注入标记并拦截（见 AGENTS.md 提示注入警告）
- **网络隔离**: 对外部 URL 访问可配置允许名单
- **数据持久化**: 所有对话和工具调用记录本地存储，无隐式外部上传

## 成本优化策略

- 💰 **模型分级路由**: flash 主力 + pro 回退 + 1M 模型只在需要时；简单任务控 token
- 📦 **技能按需加载**: 只有匹配场景的 skill 被载入 context，减少超长 context 开销
- 🧹 **会话管理**: 定期清理无价值会话，控制本地存储膨胀
- 🔧 **SearXNG 自建搜索**: 零 API 成本，完全自控搜索频谱

## 变现路径

| 优先级 | 服务 | 定价区间 | 优势 |
|--------|------|----------|------|
| 🥇 | AI PPT 代做 | 50-500 元/份 | 6 个设计 skills 全家桶 → 详见 [[PPT-Design]] |
| 🥈 | 学术论文服务 | 200-800 元/篇 | 9 个学术 skills + 多模型精修 → 详见 [[Academic]] |
| 🥉 | AI Agent 定制 | 3000-15000 元/个 | Hermes 配置 + 自定义 skill 开发 |
| 4️⃣ | AI 自媒体内容 | 按项目定价 | YouTube 转录 + 图文生成 + 视频制作 |
| 5️⃣ | 图片生成接单 | 按张/项目 | ComfyUI + HeartMuLa 多模态管线 |
| 6️⃣ | Skills/SaaS 产品化 | 订阅制 | 打包可复用的 Hermes skills 发布 |

---

## 🔗 知识关联

- **[[AI-Workflow]]** — Skill 编排与 Pipeline 设计
- **[[LLM-Providers]]** — 模型供应商对比

---

## 2026 下半年趋势更新

### Agent 范式跃迁
- 从"被动响应"到"主动决策"，MCP 协议成为行业标准
- 多 Agent 协作成熟化：Sub-agent → Multi-Agent → Agent OS
- Desktop Agent 形态跑通，Skills 标准化

### 最新模型进展（截至 2026-07）

| 模型 | 特点 |
|:-----|:------|
| GPT-5.6 (Sol/Terra/Luna) | Agent 模型，Terra 性能接近 5.5 成本减半 |
| Claude Opus 4.8 | Fast mode 速度 2.5x，成本低 3x |
| Gemini 3.5 Flash | 128K 上下文，快速迭代编码 |
| DeepSeek V4 | 原生多模态，视觉推理链 |
| GLM-5.2 / MiniMax M3 | 国内开源 Agent 模型 |

### 记忆分层架构（行业共识）
1. **工作记忆**：当前会话上下文
2. **情景记忆**：按时间索引的具体事件
3. **语义记忆**：提炼后的知识和规律
- **[[Academic]]** — 学术检索/阅读/写作全流程
- **[[Vibe-Coding]]** — Hermes 运行环境、工具链与系统维护
- **[[Obsidian-Vault]]** — Vault 使用指南与双轨记忆策略
- **[[projects/current]]** — 当前所有项目的实时状态
|- **[[HOME]]** — 返回知识中枢

## 📡 arXiv 论文周报

- **[[../../memory/2026/07/arxiv-agent-llm-2026-07-26|2026-07-26 周报]]**（NOOA, PATS, GRADRAG, Euclid-MCP, PRO-LONG, AgentDebugX 等 39 篇）

---
> 关联: [[AI-Workflow]] · [[ai-workflow-guide]] · [[LLM-Providers]] · [[Cross-Domain|🔀 知识地图]] · [[k-self-improvement]] · [[self-improvement-guide]] | [[HOME|🏠 首页]]
