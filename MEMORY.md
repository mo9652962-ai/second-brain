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
- **Agent 框架 2026-08 大整合**: 头部框架定型（LangGraph 1.x / Microsoft Agent Framework 1.0 / Claude Agent SDK / OpenAI Agents SDK / ADK 2.0 / CrewAI 1.14.7）；MCP+A2A 已成 table stakes（10 大框架全支持 MCP，A2A 超 150 组织）；LangGraph 新增 node caching + deferred nodes + pre/post model hooks（context trimming/guardrails/PII）——印证生产原语（durable state/subagents/harness-first）是 2026 主旋律
- **Hermes Agent (NousResearch, 2026)**: ~220K stars；以「持久记忆 + 自动生成 skills」为核心卖点，与我们的记忆架构方向高度契合——作为参考实现定期关注（注意与 runtime 同商标 Hermes）
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
- **Gartner 2026-08 新预测**: AI inference cost 每 agentic workflow 至 2028 增超 5 倍——成本控制升为「生存项」，直接背书我们的 cheap-model tiering + semantic caching 低成本护城河（见 LRN-20260820-001）
- **Self-hosted Agent 安全=治理自建 (2026-08)**: reco.ai「OpenClaw Security Crisis」+ Anthropic eval 事故回顾 + NVIDIA NemoClaw 三源同证。开源可审计 ≠ 数据安全；越流行越成攻击面。回应方案：NemoClaw/OpenShell 进程级沙箱 + 最小特权 + 本地模型（见 LRN-20260822-001）——直接背书 HarnessRisk 评测（Hermes Harness Configuration 最脆弱）的 P1 配置面收紧行动项

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
- [ ] 闲鱼上架「AI 代做 PPT」→ **决策悬置第 22 天**（8/18 最后窗口已过近 6 天；素材包+主图第 10+ 次核对 100% 就绪，30min；**注意合规**：2026-06-01 起「经营性卖家」新规——同款反复售出>5 次/年发>30 件 或 年售>10 万任一被标记；台账标题避开「代做/包过/破解」敏感词；见 projects/current.md + knowledge/Research/自选课题千轮研究x20）
- [x] ~~语义缓存最小版落地（根治 Tavily 配额 + 预防 Gartner 5x）~~ ✅ 2026-08-21：统一 chokepoint 覆盖全 8 后端（commit 84d813bf2），根治连续 8 工作日配额复发
- [x] ~~合并冗余 skills（hermes-search-configuration → hermes-search-config）~~ ✅ 2026-07-31 已核实：hermes-search-configuration 已不存在，仅剩 hermes-search-config，无需合并
- [ ] 随身WiFi下单确认（赫电 Pro 399元/年，选型已确认）→ 待 sora 确认
- [x] Tavily fallback 评估：Firecrawl 作为永久备用搜索后端 ✅ auto-detect正常
- [x] ~~OpenClaw Active Memory 插件成熟度评估~~ ✅ 2026-07-31：官方文档完善+源码20+文件含测试+no-restart热加载，已成熟；但仅适用交互式会话，cron/后台不运行
- [ ] 桌面美化实际部署（TranslucentTB + Rainmeter 安装包已就绪）→ 待 sora 执行
- [ ] 小红书发「AI PPT 教程」内容 → 排期 8/7+（依赖 PPT 样例素材）
- [x] ~~Krea2 安装（ComfyUI + 14GB 模型下载）~~ ✅ 2026-08-02：8/1 深夜已部署完成（见 projects/current.md），待办过时
- [ ] Skill 重复合并（6 组，8/1 审计识别）→ 待 sora 确认

---

_最后更新: 2026-08-22｜运行环境: OpenClaw Agent on Windows 11_

## Promoted From Short-Term Memory (2026-08-07)

<!-- openclaw-memory-promotion:memory:memory/2026/08/2026-08-01-todo-cleanup.md:1:29 -->
- --- tags: [daily, todo-cleanup] date: 2026-08-01 --- # 📋 每日待办执行报告 2026-08-01 > 执行时间：2026-08-01 深夜 · 遵循 daily-todo-execution 流程 ## ✅ 已执行 ### 1. EU AI Act 行动项落地 - [x] **接单问卷增加 EU 市场检查行** → 已加入 `knowledge/接单工作流-SOP.md` 1.3 需求确认清单：「确认客户是否面向 EU 市场（涉及则先做 EU AI Act 风险分级）」 - [x] `eu-ai-act-2026-08-assessment.md` 行动项标记完成 ### 2. Krea2 部署待办收尾 - [x] `projects/current.md` 中「Krea2 安装（排期 8/3+）」→ **已完成**：ComfyUI 0.29 + 官方 FP8 模型 + Triton 后端 + 自定义 VAE 解码节点，实测 1024×1024 出图成功（今晚深夜完成） ### 3.... [score=0.805 recalls=4 avg=0.505 source=memory/2026/08/2026-08-01-todo-cleanup.md:1-29]

## 🔒 Waiting for User（阻塞待办，状态变化时提醒）
- （空——被阻塞任务单独维护，不混入每日清单）

## Promoted From Short-Term Memory (2026-08-16)

<!-- openclaw-memory-promotion:memory:memory/2026-08-12.md:35:35 -->
- 系统健康度: > 🗺️ 属于 [[Home|🏠 Home]] [score=0.825 recalls=0 avg=0.620 source=memory/2026-08-12.md:35-35]

## Promoted From Short-Term Memory (Memory Pruning 2026-08-24)

<!-- Content extracted from daily notes older than 30 days (before 2026-07-25) -->

### Key Insights from July 2026

#### OpenClaw Architecture Evolution
- **Multi-Agent Framework Standardization (July 2026)**: By July 2026, major agent frameworks had converged on LangGraph 1.x, Microsoft Agent Framework 1.0, Claude Agent SDK, OpenAI Agents SDK, ADK 2.0, and CrewAI 1.14.7 as industry standards, with MCP+A2A becoming table stakes for interoperability.

- **Graph Engineering Paradigm Shift**: The industry moved from Loop Engineering (June 2026) to Graph Engineering (July 2026), emphasizing multi-stage parallel execution with precise feedback routing over sequential loops, making graph structures first-class design objects.

- **Memory Architecture Maturation**: Write-Path > Read-Only RAG emerged as the 2026 standard for memory systems, with frameworks like Mem0, Letta, Cognee, and Zep providing mature graph memory solutions that prioritize write-path capabilities over read-only retrieval.

#### OpenClaw-Specific Developments
- **Extended-Stable Release**: OpenClaw Extended-Stable (2026-07-31) introduced monthly stable releases with maturity scoring, addressing enterprise reliability concerns and moving toward LTS status.

- **NVIDIA SkillSpector Integration**: Starting June 2026, all ClawHub skills began automatic scanning for hidden instructions, significantly improving supply chain security for the OpenClaw ecosystem.

- **Gateway Stability Improvements**: Hotfix v2026.7.1-2 (August 4, 2026) resolved npm plugin singleton-array metadata compatibility issues that had caused instability in the 2026.7.1 release.

#### Knowledge and Skills Development
- **Skill Ecosystem Growth**: By July 2026, the OpenClaw skills ecosystem had expanded to 27+ installed skills plus 8 self-built skills, covering academic paper writing (9 skills), PPT creation (6 skills), image generation (7 skills), self-improvement (3 skills), search (3 skills), engineering workflow (1 skill), and academic writing (1 skill).

- **CAD Full-Stack Development**: July 2026 saw completion of a full CAD stack including 6 major CAD software packages (FreeCAD, Blender, Fusion 360, etc.) and 7 Python CAD libraries, enabling an end-to-end AI-CAD pipeline from natural language to STEP+STL export.

- **5RMB/Month Low-Cost Model Access**: Research identified affordable model access options including SiliconFlow (¥2/M output), DeepSeek direct connection (¥1/M), and ZhiPu GLM-4-Flash (free), with coding plans from providers like WuJinQiong offering ¥19.9/month access.

#### System Engineering Practices
- **Bounded Autonomy Adoption**: The industry increasingly adopted confidence thresholds and human escalation paths (Bounded Autonomy) as a production best practice for AI agents, verified through multiple independent sources in July-August 2026.

- **Hybrid Automation (AI+RPA)**: Recognition emerged that the most effective automation combines AI handling unpredictable elements with RPA handling core predictable workflows, particularly for enterprise adoption.

- **Security-by-Default for Agents**: Frameworks began emphasizing ambient/autonomous security built into agents from the ground up, with each agent requiring person-level protection measures.

### Important Learnings

#### Search Architecture
- **5-Layer Search Redundancy**: By July 2026, OpenClaw implemented a 5-layer search redundancy system: Tavily (primary) + Exa + Firecrawl + DDGS (via VPN) + SearXNG (local instance), providing resilience against individual service failures.

- **Tavily Quota Management**: Experience with Tavily API quota exhaustion (HTTP 432) led to implementing semantic caching (0.92 similarity threshold) to reduce LLM calls by 20-40% and batch search concurrency control (≤3 requests) to avoid rate limiting.

#### Model Management
- **Cross-Provider Fallback Chains**: OpenClaw established robust cross-provider fallback chains: opencode-go → DeepSeek direct → OpenRouter, providing 11-level fallback protection against single points of failure.

- **Task-Aware Model Routing**: While initially implemented as manual judgment, the industry trend moved toward intelligent model routing that matches task complexity to model capability and cost, achieving 60-70% cost optimization.

#### Memory Systems
- **Vector+Graph Hybrid Memory**: The production standard for memory systems evolved to vector+graph hybrid approaches, combining the strengths of both paradigms for better recall and relationship reasoning.

- **Persistent Context Techniques**: Methods like Just-In-Time RL and A-MEM (RL-driven adaptive memory) demonstrated significant efficiency gains (91.6% accuracy, 4x fewer tokens, 91% lower latency) compared to full-context approaches.

### Completed Projects and Experiments

#### AI-Driven CAD Automation
- Successfully implemented an AI-CAD pipeline: Natural Language → AI Agent Reasoning → build123d Code Generation → Execution → STEP+STL Export
- Created a parameterized parts library with 7 standard components (hex bolts/nuts/washers/L-brackets/gears/springs/flanges)
- Verified through 5/5 test cases including M6×30 bolts, M8 nuts, 20-tooth gears, DN50 flanges, and 40×50 L-brackets
- Advanced to real-time AI code generation where the AI (k) reasons and writes build123d code dynamically rather than using preset mappings

#### Desktop Automation and Optimization
- Researched and deployed desktop beautification toolchain: Rainmeter v4.5.26, TranslucentTB 2026.1, and ExplorerPatcher
- Created comprehensive CAD workflow: Concept Design (Fusion 360/FreeCAD) → Parametric Modeling (build123d/FreeCAD) → 3D Rendering (Blender) → 3D Printing Slicing (Cura/PrusaSlicer) → Engineering Drawings (FreeCAD TechDraw + DXF)

### Status Updates and Resolved Issues

#### Memory Search
- Fixed embedding provider timeout through increased embeddingBatchTimeoutSeconds (90s) and reindexing, achieving 1-second response times.

#### System Health
- Completed 7 historical backlog items by July 22, 2026, entering a "knowledge execution" phase where learning was actively applied rather than just accumulated.

#### Self-Improvement Systems
- The self-improving-agent skill reached maturity with deep saturation of learning records (35+ learnings), shifting focus from knowledge collection to knowledge execution.

### Pending Items Requiring User Attention

#### Pending User Actions
- **Random WiFi Purchase Decision**: Hesong Pro 399元/年 random WiFi purchase confirmation pending user verification (model selection already confirmed)
- **Skill Consolidation Review**: Review of 6 identified duplicate skill groups from August 1, 2026 audit pending user confirmation
- **Desktop Beautification Deployment**: Actual deployment of TranslucentTB + Rainmeter installation pending user execution (packages already prepared)
- **Xiaohongshu Content Creation**: AI PPT tutorial content creation for Xiaohongshu platform pending scheduling (dependent on PPT sample materials)

> *Automatically promoted from memory pruning of daily notes older than 30 days (before 2026-07-25)*
> *Processed: 2026-08-24 09:00 Asia/Shanghai*
