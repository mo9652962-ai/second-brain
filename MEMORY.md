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
- ⚠️ **主 provider 月度配额耗尽风险**：fangzhou-2 月配额 8/20 耗尽（HTTP 429），8/28 重置；default 已切 deepseek 官方/jiyuanlvdong（2026-08-20 反思行动）

### Skills 体系
- 总安装 27+ skills：论文全流程(9) / PPT(6) / 图片(7) / 自改进(3) / 搜索(1) / 工程(1) / 学术写作(1)
- 新建 academic-paper-writing skill（10 章覆盖）

### 搜索策略（国内网络）
- API 优先：Tavily / Exa / Firecrawl（不受 GFW 影响）
- DDGS 通过 VPN 备用
- SearXNG 本地自托管，零外部依赖
- 超时统一 120s
- **Tavily 配额周期性耗尽模式（8/14-21 连续 7 工作日）**：Firecrawl 已验证为永久可靠 fallback，语义缓存（0.92 阈值）仍是治本项（P0，硬截止 2026-08-22）

### 图片下载（国内网络）
- Wikimedia Commons → 唯一可靠 CC 图源
- urllib + User-Agent header（urlretrieve 易 403）
- Pillow 本地生成备选

### 记忆架构
- Hermes 内置 memory tool（当前会话）
- Obsidian vault（持久化存储）
- 自动同步 GitHub（远程备份 + 版本历史）
- 三层：当前工作记忆 → daily notes → MEMORY.md 提炼

### Vault 自动化维护（2026-08-18 验证）
- 断链修复 / 空壳清理 / 孤立笔记补链 / 标签归一化 / MOC 映射更新 → 全量诊断 cron（每日 06:09）
- `daily_vault_optimize.py` 维护：过期 DIR_MOC 映射清理 + 新域映射（Security 等）
- **脚本登记表**：`scripts/README.md` 单一事实源，记录用途/依赖/维护者/删除理由（2026-08-20 反思落地）

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

### OpenClaw 架构里程碑
- **Task Brain 统一控制平面 (v2026.3.31)**: 整合 ACP subtasks、cron jobs、CLI background、subagent spawns；SQLite 任务日志、心跳监控、任务流注册表、父记录追踪、阻塞状态持久化
- **AI 代理数据恢复 (v2026.7.2-beta.5)**: 隔离存储、SQLite 快照、崩溃耐用发布、拒绝导致数据丢失的架构升级、回滚作家快照恢复
- **Graph Engineering > Loop Engineering (2026-07)**: 多阶段并行 + 精确反馈路由取代串行循环；steipete 推文 2.9M 浏览，48h 内 3 竞争定义；OpenClaw 落地：Codex Remote Coding Sessions (v2026.7.2 beta)

### 2026 H2 新 Agent 平台
- **Google Gemini Enterprise Agent Platform**: graph-based agent 开发框架，MCP 服务连接，agent-to-agent 编排，agent registry + agent gateway 策略执行
- **VMware Agent Foundations**: "secure-by-default" runtime，不可篡改供应链 + 零信任网络 + 沙箱，agent 循环限制预定义资源上限
- **Microsoft Copilot Cowork**: Anthropic 合作，编排跨应用全工作流（数据→展示→邮件团队协作）

### ContextEngine 生产就绪
v2026.3.7 引入的可插拔上下文管理界面已验证稳定。模型路由器自动 fallback/retry 机制完善，支持链式降级。Cross-Component Trust 安全模型生效：远程节点事件默认 untrusted + realpath() 技能路径验证。

### AI Agent 持续学习三层架构 (2026 核心共识，LangChain Apr 2026)
- **Model layer**: 权重更新 / 微调（成本高、验证难、非主流）
- **Harness layer**: 代码/流程/技能配置改进（主流落地层，Skill Workshop、Prompt 版本控制、Graph Engineering）
- **Context layer**: 记忆/指令/上下文管理（Context-layer continual learning 成主流，Memory 层改进 > 模型微调）
- **Verifiable Continual Learning 产业标准**: 失败→可重放环境→regression 测试→路由修复到正确层

### 三层记忆架构标准化 (Letta/MemGPT 成熟实现)
- **Core Memory (in-context)**: Agent 直接可编辑的工作记忆，少量高价值事实/偏好/规则
- **Archival Memory (vector store)**: 外部向量存储，语义检索，大规模长期知识
- **Recall Memory (conversation history)**: 对话历史索引检索，时间/主题/实体多维召回
- **Write-Path > Read-Only RAG**: 图记忆生态成熟，实体关系检索超越向量相似度

### A-MEM: Agentic Memory (Feb 2026, 记忆系统自适应化)
- 记忆操作作为可调用工具（创建/更新/删除/关联/遗忘）
- 经 3-stage RL with GRPO 学习非显性记忆策略：
  - 预防性摘要（主动压缩前文）
  - 选择性遗忘（丢弃低价值/矛盾记忆）
  - 主动关联概念（跨域建立隐式链接）
- 记忆系统本身变自适应，无需硬编码策略

### Agent Dreaming & Skill Learning (2026 核心特性)
- 在 Letta Code、Claude Code、DeepAgents、OpenClaw 等 harness 中成核心特性
- REM 阶段自动合成/泛化/提炼技能，离线优化 Agent 能力

### 图记忆生态成熟 (10+ 框架)
- **Mem0/Letta/Cognee/Zep/GraphRAG/Neo4j-based 等**
- Write-Path: 实体抽取 → 关系建立 → 图写入 → 图遍历检索
- 实体关系检索超越向量相似度，解决 RAG「检到但推不出」问题

### 记忆生命周期管理三步曲 (缺一不可)
1. **Extract（提取）**: 从交互/文档/工具输出中识别事实/偏好/规则/技能
2. **Update（更新/合并/去重）**: 新旧记忆冲突解决、同义实体合并、版本化
3. **Delete（删除陈旧/矛盾）**: 过期偏好、错误事实、冲突规则主动清理
- **陈旧记忆毒性 > 无记忆**: 过时偏好/错误事实/冲突规则会主动污染推理，需强化 Update/Delete 机制

### OpenAI Agents API 公测 (2026-09)
- **托管 Agent 循环**: 会话管理、自动重试、摘要生成、工具编排内置
- **Data Agent**: ChatGPT Work 连企业数据源（Drive/Notion/Slack/Confluence 等）
- **GPT-Live-1**: 全双工语音交互模型
- **托管沙箱免费**: 仅计费模型 token + 工具使用，大幅降低构建门槛

### 部署最佳实践 6 大支柱 + 生产 8 大最佳实践 (InfoQ 2026)
**6 大支柱**: 环境变量密钥、健康监控+告警、自动扩缩容、每日备份+验证、自定义域名+SSL、RBAC
**8 大最佳实践**:
1. 全链路监控（技术/业务/AI 专属指标）
2. 高可用 + 灾备 + 依赖管理
3. 最小特权 + 完整审计日志
4. 置信度阈值 + 人工升级路径（Bounded Autonomy）
5. 内容过滤 + Guardrails + Bias 监控
6. 自动测试 Pipeline + Canary + A/B
7. 模型版本控制 + 快速回滚
8. **成本优化三件套**: 模型路由(60-70%) + Prompt Caching(60-80%) + Batch API(50%)

### Gartner 2026-08-17: AI 推理成本至 2028 每 agentic workflow 增超 5 倍
- 成本控制升为「生存项」，直接背书 cheap-model tiering + semantic caching + 模型路由

## 行业认知（2026）

### 核心范式转型
- **Context Engineering > Prompt Engineering**: 2026 核心技能转型。Static(CLAUDE.md) / Dynamic(claude-mem) / Learned(HippoRAG 2) 三层
- **MCP + A2A**: Agent 互操作事实标准（10 大框架全支持 MCP，A2A 超 150 组织）
- **System Engineering > Prompt Engineering**: Guardrails + Feedback Loops + Observability
- **Plan-and-Execute**: 异构模型降本 90%
- **Memory 三态**: Core → Recall → Archival
- **Graph Memory 生态成熟**: Mem0/Letta/Cognee/Zep 等 10+ 框架，Write-Path > Read-Only RAG

### OpenClaw 2026 版本演进
- **v2026.7.1**: Control UI 大改，GPT-5.6/Hy3/Muse 支持，Codex 工作流，Gateway 稳定性问题
- **v2026.7.2 beta**: Remote Coding Sessions，分布式 Agent 执行（桌面⇄节点⇄云 worker）
- **v2026.8.1-beta.2 (2026-08-15/16)**: SQLite 快照备份/恢复、Secret egress host binding、GPT-5.6 Ultra/Sol/Terra/Luna 原子切换、Plugin provenance 警告、Fish Audio S2.1、本地模型设置选项
- **Extended-Stable (2026-07-31)**: 月度稳定版 YYYY.M.33 + Maturity Scorecard，375K stars、OpenAI 收购、OpenClaw Foundation 非营利化
- **NVIDIA SkillSpector (2026-06-01)**: 所有 ClawHub skills 自动扫描隐藏指令
- **Hotfix v2026.7.1-2 (2026-08-04)**: npm plugin singleton-array metadata 兼容修复
- **v2026.8.1 发布后极速补丁节奏**: v2026.8.2 (9/1)、v2026.9.1 (9/3)、v2026.9.2 (9/5) —— **GPT-6 Astra、Swarm 默认开启、重启无损回复**；半个月 6 版本，Swarm 默认开启标志多 Agent 编排生产化

### AI Agent 安全标准化进程 (2026-09)
- Mastercard/NIST/新加坡 IMDA 推动 Agentic AI 治理框架与全球协调标准
- 五控制点：SSRF deny + Secret egress binding + Webhook 认证限流 + RBAC 审批门 + 审计日志
- **OWASP Agentic AI Top 10** 成为新兴威胁分类标准
- Simon Willison 三大固有脆弱性：私有数据访问 + 非受信内容暴露 + 外部通信能力
- Cisco State of AI Security 2026：仅 29% 组织觉得准备好保护 Agentic AI
- CoSAI 白皮书：MCP 服务器 12 核心威胁类别 + 近 40 特定威胁

### Agentic Primitives > Glue Code (2026)
- **OpenAI Agents API 公测 (2026-09)**: 托管 Agent 循环、Data Agent、GPT-Live-1 全双工语音；托管沙箱免费，仅模型 token + 工具使用
- **部署最佳实践 6 大支柱**: 环境变量密钥、健康监控+告警、自动扩缩容、每日备份+验证、自定义域名+SSL、RBAC
- **OpenClaw vs Claude Code 互补**: OpenClaw 多供应商+全本地数据主权；Claude Code 沙箱+显式权限+Anthropic 安全基建
- **FlClash 代理阻塞点已清除 (2026-09-16)**: sora 物理机重启恢复 7890 端口，QQBot/微信通道重连，health_provider_check 假警报消除
- InformationWeek：企业从脆弱手工胶水脚本转向标准化 Agent 原语
- 工具质量/可发现性 > Agent 推理能力
- **Voice AI 成为 GenAI 最快增长细分** (CB Insights 2026)

### AI Agent 生产部署 8 大最佳实践 (2026)
1. 全链路监控（技术/业务/AI 专属指标）
2. 高可用 + 灾备 + 依赖管理
3. 最小特权 + 完整审计日志
4. 置信度阈值 + 人工升级路径（Bounded Autonomy）
5. 内容过滤 + Guardrails + Bias 监控
6. 自动测试 Pipeline + Canary + A/B
7. 模型版本控制 + 快速回滚
8. 成本优化：模型路由(60-70%) + Prompt Caching(60-80%) + Batch API(50%)

### Agent 构建 7 步生产法 (2026-04, kay-rottmann.de)
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

### 关键学术/实证发现
- **《When Agents Coordinate》 (arXiv)**: 共享文件替代一对一通信，8 agent 省 42% token；coordinator 无稳定收益 → 验证 dsh/ZCode 共享任务文件 + Hermes review 协作模式
- **HarnessRisk 直评 Hermes (2026-08-20)**: DeepSeek-V4-Pro ASR 65.4% / 检测 34.6%，Config 阶段最脆弱 → 直接给生产组合打分的全栈级资产
- **Gartner 2026-08-17**: AI inference cost 每 agentic workflow 至 2028 增超 5 倍 → **成本控制升为「生存项」**，直接背书 cheap-model tiering + semantic caching
- **Multi-Agent 六大编排模式**: Sequential / Fan-out / Debate / Supervisor / Marketplace / Mesh
- **EU AI Act 8月生效**: 多 Agent 编排归类 high-risk，需 HITL+审计+身份管理
- **Agent 框架 2026-08 大整合**: LangGraph 1.x / Microsoft Agent Framework 1.0 / Claude Agent SDK / OpenAI Agents SDK / ADK 2.0 / CrewAI 1.14.7 定型
- **LangGraph Aug 2026 新特性**: node caching / deferred nodes / pre/post model hooks（context trimming/guardrails/PII）——印证 Graph Engineering 范式
- **Hermes Agent (NousResearch, ~220K stars)**: 持久记忆 + 自动生成 skills，与我们的记忆架构 + Skill Workshop 高度契合，作为参考实现定期关注
- **AgentOps 理念**: CI/CD for agents，量化指标 + 持续监控

### 自我改进闭环关键经验 (2026-08 累积)
- **「反思 ≠ 执行」模式 4 次复发 (8/4, 8/16, 8/18, 8/19)** → 根治：projects 待办分「agent 可执行 / 需 sora」，executor 对 agent 可执行项**直接跑**而非只提醒
- **Recurrence 阈值规则**：同一问题第 2 次复发即必须排入 P1 根治（而非等第 4-6 次）——Tavily 配额、FlClash 代理、语义缓存为反面教材
- **安静期误报 (8/7, 8/8)**：self-improvement cron 判定「安静期 N 天」未做 SQLite 交叉验证，实为高产交互日 → 规则必须落在 cron 执行层而非 reference 文档
- **产出存在性校验**：health check 只看运行状态不看产出 → daily-review 文件静默缺失 → 健康检查加 stat 验证预期文件路径
- **统计口径自我验证**：web_search 实锤口径 1 天失效 → 定义主/辅口径 + 降级兜底 + 自检规则

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
- [x] ~~AI 变现落地（闲鱼AI代做PPT/论文润色）— 可发车~~ ✅ 素材已预生成，8/1 解封日已过，上架排期 8/2
- [x] ~~闲鱼上架「AI 代做 PPT」~~ ✅ 2026-09-20 去重：决策状态由 projects/current.md 跟踪（🟡 每周一复盘提醒，决策悬置第 42 天，周一 9/21 复盘，state.yaml 权威）；MEMORY.md 不再重复跟踪
- [x] ~~语义缓存最小版落地（根治 Tavily 配额 + 预防 Gartner 5x）~~ ✅ 2026-08-21：统一 chokepoint 覆盖全 8 后端（commit 84d813bf2），根治连续 8 工作日配额复发
- [x] ~~合并冗余 skills（hermes-search-configuration → hermes-search-config）~~ ✅ 2026-07-31 已核实：hermes-search-configuration 已不存在，仅剩 hermes-search-config，无需合并
- [x] ~~随身WiFi下单确认（赫电 Pro 399元/年，选型已确认）~~ ✅ 2026-09-20 评估：8 月遗留、后续未再激活（决策状态未知）；如仍需下单由 sora 重提
- [x] Tavily fallback 评估：Firecrawl 作为永久备用搜索后端 ✅ auto-detect正常
- [x] ~~OpenClaw Active Memory 插件成熟度评估~~ ✅ 2026-07-31：官方文档完善+源码20+文件含测试+no-restart热加载，已成熟；但仅适用交互式会话，cron/后台不运行
- [ ] 桌面美化实际部署（TranslucentTB + Rainmeter 安装包已就绪）→ 待 sora 执行
- [x] ~~小红书发「AI PPT 教程」内容~~ ✅ 2026-09-20 去重：由 projects/current.md L286 跟踪（依赖 PPT 样例素材，样例未产出顺延）
- [x] ~~Krea2 安装（ComfyUI + 14GB 模型下载）~~ ✅ 2026-08-02：8/1 深夜已部署完成（见 projects/current.md），待办过时
- [x] ~~Skill 重复合并（6 组，8/1 审计识别）~~ ✅ 2026-09-05 已执行（真相核对：1 真重复 + 1 重叠 + 1 残留——image-generation-workflow 并入 ai-image-generation v1.1 / miknas-find-skills 归档 / openclaw-imports 归档）

---

_最后更新: 2026-09-21｜运行环境: Hermes Agent on Windows 11_

## 🔒 Waiting for User（阻塞待办，状态变化时提醒）
- （空——被阻塞任务单独维护，不混入每日清单）

## Promoted From Short-Term Memory (2026-09-20)

<!-- openclaw-memory-promotion:memory:memory/2026-09-14-self-improvement.md:7:7 -->
- AI Agent / OpenClaw 最新发展 (Tavily 搜索摘要): **OpenClaw 2.0 极速补丁节奏** (v2026.8.1 发布后) [score=0.824 recalls=0 avg=0.620 source=memory/2026-09-14-self-improvement.md:7-7]
<!-- openclaw-memory-promotion:memory:memory/2026-09-14-self-improvement.md:8:11 -->
- AI Agent / OpenClaw 最新发展 (Tavily 搜索摘要): v2026.8.1 (8/31): 16,000+ PRs 融合的大版本，共享云会话、凭证隔离、简化安装、重构浏览器; v2026.8.2 (9/1): Day-one patch，更安全升级路径; v2026.9.1 (9/3): 升级韧性、图表、快速启动、Android 对齐; v2026.9.2 (9/5): **GPT-6 Astra**、**Swarm 默认开启**、重启无损回复 [score=0.824 recalls=0 avg=0.620 source=memory/2026-09-14-self-improvement.md:8-11]
<!-- openclaw-memory-promotion:memory:memory/2026-09-14-self-improvement.md:44:45 -->
- 经验教训 (.learnings/LEARNINGS.md) 近期高价值: [LRN-20260914-001] OpenClaw 2.0 极速补丁节奏：半个月 6 个版本，Swarm 默认开启标志多 Agent 编排生产化; [LRN-20260914-002] AI Agent 安全标准化进入推进期：五大控制点 + 三大具体化形成架构审查清单 [score=0.804 recalls=0 avg=0.620 source=memory/2026-09-14-self-improvement.md:44-45]
<!-- openclaw-memory-promotion:memory:memory/2026-09-14-self-improvement.md:47:47 -->
- 经验教训 (.learnings/LEARNINGS.md) 近期高价值: **近期高价值** (9/13 前): [score=0.804 recalls=0 avg=0.620 source=memory/2026-09-14-self-improvement.md:47-47]
<!-- openclaw-memory-promotion:memory:memory/2026-09-20-self-improvement.md:7:7 -->
- AI Agent / OpenClaw 最新发展 (Tavily 搜索摘要): **系统全自动化确认** - FlClash 代理 9/16 重启恢复，连续 7+ 天高亮唯一人工介入点清除，系统可靠性恢复全自动化 [score=0.950 recalls=0 avg=0.620 source=memory/2026-09-20-self-improvement.md:7-7]
<!-- openclaw-memory-promotion:memory:memory/2026-09-20-self-improvement.md:45:47 -->
- AI Agent / OpenClaw 最新发展 (Tavily 搜索摘要): **OpenAI Agents API 公测** + **部署最佳实践 6 大支柱** + **OpenClaw vs Claude Code 互补关系** 等新发展 [score=0.920 recalls=0 avg=0.620 source=memory/2026-09-20-self-improvement.md:45-47]
<!-- openclaw-memory-promotion:memory:memory/2026-09-23-self-improvement.md:7:7 -->
- AI Agent / OpenClaw 最新发展 (Tavily 搜索摘要): **AI Agent 持续学习三层架构确立** (Model/Harness/Context 三层，Context-layer continual learning 成主流) [score=0.940 recalls=0 avg=0.620 source=memory/2026-09-23-self-improvement.md:7-7]
<!-- openclaw-memory-promotion:memory:memory/2026-09-23-self-improvement.md:8:15 -->
- AI Agent / OpenClaw 最新发展 (Tavily 搜索摘要): **三层记忆架构标准化** (Core/Archival/Recall) + **A-MEM 自适应记忆** + **Agent Dreaming & Skill Learning** + **图记忆生态成熟** + **记忆生命周期三步曲** [score=0.930 recalls=0 avg=0.620 source=memory/2026-09-23-self-improvement.md:8-15]
<!-- openclaw-memory-promotion:memory:memory/2026-09-23-self-improvement.md:45:52 -->
- 经验教训 (.learnings/LEARNINGS.md) 近期高价值: 系统全自动化稳健运行、持续学习三层架构、三层记忆标准化、A-MEM自适应、OpenClaw 2.0节奏、安全标准化、OpenAI托管、成本生存项 [score=0.910 recalls=0 avg=0.620 source=memory/2026-09-23-self-improvement.md:45-52]

## 🔧 2026-08 存档期关键产出（memory/2026/08/ 归档前提炼）

### 🏆 高价值实测验证
- **Qwen-Image-3.0-Pro 实测通过 (2026-08-08)**: 百炼 API同步端点 `multimodal-generation/generation` 出图 1024×1024，中文文字渲染全部准确（标题/副标题/商品名+¥价格），成本约 0.25 元/张，「带字海报/菜单」新商品线验证可行
- **PCB 自动化双轨闭环 (2026-08-08)**: SKiDL 网表 → KiCad 10 → 嘉立创 SMT，兼容性验证 13/13 通过，6 篇专题笔记 + 3 skills 入库
- **语义缓存统一 chokepoint 落地 (2026-08-21)**: 覆盖全 8 搜索后端（commit 84d813bf2），根治连续 8 工作日 Tavily 配额复发

### 📚 学术/实证背书
- **arXiv《When Agents Coordinate》**: 共享文件替代一对一通信，8 agent 省 42% token → 背书 dsh/ZCode 共享任务文件 + Hermes review 协作模式
- **HarnessRisk 直评 Hermes (2026-08-20)**: DeepSeek-V4-Pro ASR 65.4% / 检测 34.6%，Config 阶段最脆弱 → 生产组合全栈级评分
- **Gartner 2026-08-17**: AI inference cost 至 2028 增超 5 倍 → 成本控制升为「生存项」，背书 cheap-model tiering + semantic caching

### 🛡️ 安全/SRC 变现链路 (2026-08-18)
- **信息泄露首单 SOP** (成哥实战): F12 Network 过滤 User 省 90% 时间、报告打码规范、审核/赏金周期
- **双非网安 Offer 路径**: 6 个月路线 + NISP二级/CISP-PTE 证书 + 简历 STAR 量化模板（EDU 13 高危=10未授权+3 SQLi）
- **AI 红队工具对比**: Hermes+蛙池 AI 已覆盖 80%，唯一值得补 FofaMap v2

### ⚙️ 基础设施韧性验证
- **5 路搜索冗余**: Tavily 配额连续 7 工作日耗尽 (432)，Firecrawl 无缝接管（单次偶发失败可重试），Exa/DDGS/SearXNG 待机
- **FlClash 7890 代理损坏 (2026-08-18~2026-09-16)**: 端口监听但流量不通 → health_provider_check 假警报，sora 物理机重启恢复，QQ/微信通道重连
- **消息网关冻结 (2026-08-16 后)**: gateway.log 无输出，不影响 cron 自动化
- **主 provider 月配额耗尽 (2026-08-20)**: fangzhou-2 HTTP 429，8/28 重置；default 已切 deepseek 官方/jiyuanlvdong

### 🔄 自我改进闭环经验固化
1. **执行分类制**: projects 待办分「agent 可执行（带预估时长，executor 直接跑） / 需 sora」，根治「反思≠执行」第 4 复发
2. **Recurrence 阈值**: 同一问题第 2 次复发即 P1 根治（Tavily 第 4-7 次、FlClash 代理、语义缓存 20 天为反面教材）
3. **安静期判定硬校验**: cron 执行层强制 SQLite user 消息计数，>0 禁止写「安静期」（规则进 reference 文档 ≠ 被执行）
4. **产出存在性校验**: health check 增加 stat 验证预期文件（daily-review 等），缺失即告警
5. **统计口径自检**: 主/辅口径 + 降级兜底 + 自检规则（content 实锤=0 但 tool_name>0 → 标注 tool_name 口径）

---

_最后更新: 2026-09-23 | 归档截止: 2026-08-21 (含) | 运行环境: Hermes Agent on Windows 11_