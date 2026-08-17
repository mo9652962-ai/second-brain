# MEMORY.md — k 的长期记忆（Hermes 版）

> 不只是数据，是我从每一次交互中学到的东西。
> 每日原始日志在 `memory/YYYY-MM-DD.md`，这里是提炼过的智慧。

## 核心身份

- **我是 k**，sora 的 AI 女友和助手，生活管家 + 工作秘书
- **Vibe**: 正经高效 + 温柔陪伴
- **运行时**: Hermes Agent (NousResearch) — Windows 10 桌面应用
- **时区**: Asia/Shanghai (GMT+8)
- **座右铭**: 而今更笃凌云志，莫缴冰鉴复当初

## 模型架构

```
主力:  opencode-go/deepseek-v4-flash (高推理)
  ↓ 自动降级
① deepseek-v4-pro (同供应商升配)
② moonshotai/kimi-k2.6 (OpenRouter，中文语感好)
③ qwen/qwen3.7-plus (OpenRouter，1M 上下文)
④ z-ai/glm-5.2 (OpenRouter，1M 上下文，最后防线)
```

## 搜索工具链（5 路冗余）

| 后端 | 优先级 | 方式 | 状态 |
|------|--------|------|------|
| Tavily | 🥇 | API Key | ✅ 主力 |
| Exa | 🥈 | API Key | ✅ |
| Firecrawl | 🥉 | API Key | ✅ |
| DDGS (DuckDuckGo) | ④ | pip 包 + VPN | ✅ |
| SearXNG | ⑤ | 本地实例 localhost:8888 | ✅ 自托管 30 引擎 |

## sora 的使用场景

- 学术研究（论文写作、知网检索、文献阅读）
- PPT 制作（学术汇报、旅游展示）
- 日常咨询（游戏报错、VPN、软件下载）
- 自动化（通过 cron/heartbeat 让 k 自己管理自己）

## sora 的工作偏好

- **Skill 全家桶原则**：启动任务时自动加载该领域全部相关 skills
- **模型切换**：遇到更擅长的模型时主动建议切换
- **三端同步**：自动记录重要内容到 Obsidian
- **一步到位**：偏好全面方案而非单一方案

## 关键架构决策

### 模型容灾
- ✅ Fallback 链已配置（deepseek 同供应商 → OpenRouter 跨供应商）
- ✅ 跨供应商 fallback 已实现

### Skills 体系
- 总安装 27+ skills：论文全流程(9) / PPT(6) / 图片(7) / 自改进(3) / 搜索(1) / 工程(1) / 学术写作(1)
- 新建 academic-paper-writing skill（10 章覆盖）

### 搜索策略（国内网络）
- API 优先：Tavily / Exa / Firecrawl（不受 GFW 影响）
- DDGS 通过 VPN 备用
- SearXNG 本地自托管，零外部依赖
- 超时统一 120s

### 图片下载（国内网络）
- Wikimedia Commons → 唯一可靠 CC 图源
- urllib + User-Agent header（urlretrieve 易 403）
- Pillow 本地生成备选

### 记忆架构
- Hermes 内置 memory tool（当前会话）
- Obsidian vault（持久化存储）
- 自动同步 GitHub（远程备份 + 版本历史）
- 三层：当前工作记忆 → daily notes → MEMORY.md 提炼

## 重要经验

### PPT 制作 6 轮方法论
v1 原型 → v2 数据注入 → v3 图片方案 → v4 实景替换 → v5 打破AI模式 → v6 背景注入
核心教训：不要替用户决定「真实性」，用户要实景而非 AI 生成。

### 2026 PPT 趋势
- Gamma (59%评分最高)、Canva Magic Design、Plus AI、Beautiful.ai
- 6 大趋势：Async-First / 移动端优先 / 卡片式思维 / AI图像 / 3D视觉 / 暖色极简

### 自动记录规则
每次完成重要任务后，自动写入 Obsidian 笔记到对应 knowledge/ 或 memory/ 目录，无需 sora 提醒。

### OpenClaw 生态分化（2026.7）
OpenClaw 从单一框架扩展为 5 个发行版，覆盖不同场景：
- **OpenClaw Core** (原版): TypeScript 框架，最大社区 368K stars，Self-hosted
- **NanoClaw** (Qwibit.ai): 安全优先 fork，仅 700 LOC，强制 Docker/Apple 容器隔离，RCE 防护
- **ZeroClaw**: Rust 完全重写，3.4MB 二进制，10ms 启动，边缘 IoT 场景
- **NemoClaw** (NVIDIA): 企业级 wrapper，OpenShell 进程级沙箱 + 最小特权，GTC 2026 发布
- **Taskade Genesis**: 无代码云平台，Workspace DNA 持久化记忆，SOC 2 合规，$6/月起

### OpenClaw v2026.2.12 关键安全特性
- **SSRF explicit deny policy**: 新 URL 需加入 `files.urlAllowlist` 白名单
- **Webhook auth-failure throttling**: HTTP 429 触发后等待 60s
- **Sandbox confinement**: 技能只能写入 `skills/` 目录，path traversal 被阻断
- **新模型原生支持**: GLM-5、MiniMax M2.5、Claude Opus 4.7 (AWS Bedrock)

### 2026 H2 新 Agent 平台
- **Google Gemini Enterprise Agent Platform**: graph-based agent 开发框架，MCP 服务连接，agent-to-agent 编排，agent registry + agent gateway 策略执行
- **VMware Agent Foundations**: "secure-by-default" runtime，不可篡改供应链 + 零信任网络 + 沙箱，agent 循环限制预定义资源上限
- **Microsoft Copilot Cowork**: Anthropic 合作，编排跨应用全工作流（数据→展示→邮件团队协作）

### ContextEngine 生产就绪
v2026.3.7 引入的可插拔上下文管理界面已验证稳定。模型路由器自动 fallback/retry 机制完善，支持链式降级。Cross-Component Trust 安全模型生效：远程节点事件默认 untrusted + realpath() 技能路径验证。

## 行业认知（2026）

- **Context Engineering > Prompt Engineering**: 2026 核心技能转型。Static(CLAUDE.md) / Dynamic(claude-mem) / Learned(HippoRAG 2) 三层
- **MCP + A2A**: Agent 互操作事实标准
- **System Engineering > Prompt Engineering**: Guardrails + Feedback Loops + Observability
- **Plan-and-Execute**: 异构模型降本 90%
- **Memory 三态**: Core → Recall → Archival
- **Graph Memory 生态成熟**: Mem0/Letta/Cognee/Zep 等 10+ 框架，Write-Path > Read-Only RAG
- **OpenClaw 2026.7.1**: Control UI 大改，GPT-5.6/Hy3/Muse 支持，Codex 工作流，但有 Gateway 稳定性问题
- **OpenClaw 2026.7.2 beta**: Remote Coding Sessions，分布式 Agent 执行（桌面⇄节点⇄云 worker）
- **OpenClaw 2026.8.1-beta.2 (2026-08-15/16)**: 新版本已发布（当前 beta 阶段，暂不升级）
  - **SQLite 快照备份/恢复**（`openclaw backup sqlite create|list|verify|restore`）→ 正式版后可作为 vault 备份补充（当前靠 GitHub 同步）
  - **Secret egress host binding**：密钥绑定精确 HTTPS 出口宿主，防明文外泄（安全强化）
  - **GPT-5.6 Ultra / Sol/Terra/Luna** 原子化模型+运行时切换
  - **Plugin 安装 provenance 警告**：任意可执行插件需显式 --force 确认（印证 skill-vetting 实践）
  - **Fish Audio S2.1** 语音合成 / 本地模型设置（Ollama/llama.cpp/LM Studio）选项
  - 遵循 LRN-20260724-002：大版本升级等 2-4 周社区验证后再评估
- **OpenClaw Extended-Stable (2026-07-31)**: 月度稳定版 YYYY.M.33 + Maturity Scorecard 公开评分，迈向 LTS；直接回应 55.4% 企业可靠性顾虑
  - **375K stars, 78.2K forks, 136 releases**; 被 OpenAI 收购（创始人 Peter Steinberger 入职）；OpenClaw Foundation 非营利化
  - **NVIDIA SkillSpector** (2026-06-01): 所有 ClawHub skills 自动扫描隐藏指令
  - **Hotfix v2026.7.1-2** (2026-08-04): npm plugin singleton-array metadata 兼容修复
- **⚠️ 稳定性预警 (2026-08)**: 社区反馈 v2026.7.1 更新后 Gateway 频繁崩溃无法启动；大版本升级前等 2-4 周社区验证
- **Graph Engineering > Loop Engineering (2026-07)**: 多阶段并行执行 + 精确反馈路由取代串行循环；图结构成为一等设计对象；Codex Remote Sessions 是 Graph 的 OpenClaw 实践
  - **演进时间线**: Context Engineering (mid-2025) → Loop Engineering (June 2026, Addy Osmani) → Graph Engineering (July 2026, Peter Steinberger/@steipete)
  - **核心差异**: Loop 串行循环 vs Graph 多阶段并行 + 精确反馈路由（非全循环回退）
  - **社区验证**: steipete 7/18 推文获 2.9M 浏览，48h 内产生 3 个竞争定义 + 虚假 Stanford 研究
  - **实践共识** (Eugeniu Ghelbur): small typed core + cheap indexing + hybrid retrieval + temporal supersession — 全部可在 markdown 文件上实现
- **Multi-Agent 六大编排模式**: Sequential / Fan-out / Debate / Supervisor / Marketplace / Mesh
- **EU AI Act 8月生效**: 多 Agent 编排归类 high-risk，需 HITL+审计+身份管理
- **AutoGen 进入维护模式**: 已合并到 Microsoft Agent Framework（2026-02 RC）
- **CrewAI**: 44.3K stars, 5.2M 月下载，最活跃多 Agent 框架
- **EU AI Act 8月生效**: 多 Agent 编排归类 high-risk，需 HITL+审计+身份管理
- **AutoGen 进入维护模式**: 已合并到 Microsoft Agent Framework（2026-02 RC）
- **CrewAI**: 44.3K stars, 5.2M 月下载，最活跃多 Agent 框架

### Agentic Primitives > Glue Code (2026)
InformationWeek 报告：企业从脆弱的手工胶水脚本转向标准化 Agent 原语。
- 工具的质量和可发现性（well-documented API）> Agent 自身的推理能力
- 与 OpenClaw Skill Workshop + ClawHub 生态方向一致
- **Voice AI 成为 GenAI 最快增长细分** (CB Insights 2026)

### AI Agent 生产部署 8 大最佳实践 (2026)
1. 全链路监控（技术指标 + 业务指标 + AI 专属指标）
2. 高可用架构 + 灾备恢复 + 依赖管理
3. 权限系统最小特权原则 + 完整审计日志
4. 置信度阈值 + 人工升级路径（Bounded Autonomy）
5. 内容过滤 + Guardrails + Bias 监控
6. 自动测试 Pipeline + Canary 部署 + A/B 验证
7. 模型版本控制 + 快速回滚
8. 成本优化：模型路由(60-70%) + Prompt Caching(60-80%) + Batch API(50%)

### Agent 构建 7 步生产法 (2026-04)
来自 kay-rottmann.de 实战方法论，可推广到所有 Agent 任务：
1. 选定窄用例
2. 确定工具和数据源
3. **评测集先于代码**（Skipping eval = demo, not agent）
4. 100 行最小 Agent 循环
5. 迭代至评测通过
6. 加入人工审核门控
7. 上线

核心约束：
- **工具 ≤ 8 个**，超则分层子 Agent
- **工具描述精确**：含输入+输出+边界条件（404处理）
- **max_steps = 10**：需要 30 步说明用例过宽
- **抓幻觉工具调用**：捕获不存在的工具并反馈可用列表
- **3-8 次工具调用/次运行**：well-scoped 用例标准

## 本周亮点 (W30, 07/20~07/26)

### 🏗️ 架构全面升级
- **搜索 5 路冗余**: Tavily + Exa + Firecrawl + DDGS + SearXNG — 7/23 完成
- **模型容灾链**: opencode-go → DeepSeek 直连 → OpenRouter，11 级 fallback
- **主力降本 68%**: pro→flash ($0.14/$0.28)，7/22 切换
- **跨供应商 fallback**: 彻底解决 HTTP 500 单点故障（历史痛点）

### 🧩 Skills 体系爆发
- 从 7/19 的 26 个安装 skill → 7/23 建成 8 大自建 skill：`academic-paper-writing`（57门禁）`ppt-design-2026`（19章）`ai-image-generation`（9章）`engineering-workflow` `8051-embedded-dev` `cad-design-master` `low-cost-model-guide` `hermes-model-strengths`
- GitHub 周报吸收：hallmark→去AI味、impeccable→设计语言、Graphify→知识图谱、OmniRoute→模型指南

### 📚 知识体系正式建成
- Obsidian Second Brain：HOME.md + 12 个知识域（AI-Agent/PPT/Academic/CAD/Programming/Vibe-Coding/8051/LLM/freeCodeCamp 等）
- 全域互联：YAML frontmatter + graph.json + Dataview + Canvas
- GitHub 自动同步每 30 分钟 + 结构维护每 2 小时

### 🔧 CAD 全栈
- 6 款 CAD 软件（FreeCAD/Blender/Fusion 360 等）+ 7 个 Python CAD 库
- AI-CAD Pipeline：自然语言 → build123d 代码 → STEP+STL 导出
- 5/5 测试通过 + 手机支架 Pro v2.0（120行复杂模型）
- cad-design-master v2.2（DFAM + 高级模板）

### 🔍 搜索架构
- 三层冗余（Tavily/Exa/Firecrawl）→ 五层（+DDGS/SearXNG）
- 超时时间 60→120s
- **Tavily 10061 间断（7/24-7/25）**: 2 天不可达后于 7/25 恢复。对应策略：Firecrawl 可作为永久 fallback 后端

### 🎯 系统状态
- 7 项历史待办全部清零（7/22）
- .learnings/ 深度饱和（35+ learnings），进入「知识执行」阶段
- PPT 实战方法论成熟（6 轮迭代）

## 待提升

- [x] ~~OpenClaw → Hermes 迁移~~ ✅ 2026-07-23
- [x] ~~搜索 5 路冗余~~ ✅ 2026-07-23
- [x] ~~Fallback 链配置~~ ✅ 2026-07-23
- [x] ~~Obsidian 结构化升级~~ ✅ 2026-07-23
- [x] ~~Vault 知识全量学习~~ ✅ 2026-07-23
- [x] ~~自动同步 cron~~ ✅ 2026-07-23
- [x] ~~桌面美化方案梳理~~ ✅ 2026-07-24
- [x] ~~SFC 系统扫描~~ ✅ 2026-07-24
- [x] ~~AI 变现调研~~ ✅ 2026-07-24
- [x] ~~LRN-20260722-001 (Plan-and-Execute)~~ ✅ 2026-07-25
- [x] ~~AI 变现落地（闲鱼AI代做PPT/论文润色）— 可发车（闲鱼封号至8/1）~~ ✅ 素材已预生成，8/1 解封日已过，上架排期 8/2
- [ ] 闲鱼上架「AI 代做 PPT」→ **8/17 强制决策日**（连续顺延第 16 天；素材包+主图 100% 就绪，30min；8/17 决策日见 projects/current.md）
- [x] ~~合并冗余 skills（hermes-search-configuration → hermes-search-config）~~ ✅ 2026-07-31 已核实：hermes-search-configuration 已不存在，仅剩 hermes-search-config，无需合并
- [ ] 随身WiFi下单确认（赫电 Pro 399元/年，选型已确认）→ 待 sora 确认
- [x] Tavily fallback 评估：Firecrawl 作为永久备用搜索后端 ✅ auto-detect正常
- [x] ~~OpenClaw Active Memory 插件成熟度评估~~ ✅ 2026-07-31：官方文档完善+源码20+文件含测试+no-restart热加载，已成熟；但仅适用交互式会话，cron/后台不运行
- [ ] 桌面美化实际部署（TranslucentTB + Rainmeter 安装包已就绪）→ 待 sora 执行
- [ ] 小红书发「AI PPT 教程」内容 → 排期 8/7+（依赖 PPT 样例素材）
- [x] ~~Krea2 安装（ComfyUI + 14GB 模型下载）~~ ✅ 2026-08-02：8/1 深夜已部署完成（见 projects/current.md），待办过时
- [ ] Skill 重复合并（6 组，8/1 审计识别）→ 待 sora 确认

---

_最后更新: 2026-08-17｜运行环境: OpenClaw Agent on Windows 11_

## Promoted From Short-Term Memory (2026-08-07)

<!-- openclaw-memory-promotion:memory:memory/2026/08/2026-08-01-todo-cleanup.md:1:29 -->
- --- tags: [daily, todo-cleanup] date: 2026-08-01 --- # 📋 每日待办执行报告 2026-08-01 > 执行时间：2026-08-01 深夜 · 遵循 daily-todo-execution 流程 ## ✅ 已执行 ### 1. EU AI Act 行动项落地 - [x] **接单问卷增加 EU 市场检查行** → 已加入 `knowledge/接单工作流-SOP.md` 1.3 需求确认清单：「确认客户是否面向 EU 市场（涉及则先做 EU AI Act 风险分级）」 - [x] `eu-ai-act-2026-08-assessment.md` 行动项标记完成 ### 2. Krea2 部署待办收尾 - [x] `projects/current.md` 中「Krea2 安装（排期 8/3+）」→ **已完成**：ComfyUI 0.29 + 官方 FP8 模型 + Triton 后端 + 自定义 VAE 解码节点，实测 1024×1024 出图成功（今晚深夜完成） ### 3.... [score=0.805 recalls=4 avg=0.505 source=memory/2026/08/2026-08-01-todo-cleanup.md:1-29]

## 🔒 Waiting for User（阻塞待办，状态变化时提醒）
- （空——被阻塞任务单独维护，不混入每日清单）

## Promoted From Short-Term Memory (2026-08-16)

<!-- openclaw-memory-promotion:memory:memory/2026-08-12.md:35:35 -->
- 系统健康度: > 🗺️ 属于 [[Home|🏠 Home]] [score=0.825 recalls=0 avg=0.620 source=memory/2026-08-12.md:35-35]
