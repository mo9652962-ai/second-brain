# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260722-001] best_practice

**Logged**: 2026-07-22T14:15:00+08:00
**Priority**: high
**Status**: resolved
**Area**: config

### Summary
Plan-and-Execute 妯″紡 + 寮傛瀯妯″瀷鏋舵瀯锛欶rontier 妯″瀷璐熻矗瑙勫垝鍜屽鏉傛帹鐞嗭紝cheap model 鎵ц楂橀浠诲姟锛岀患鍚堥檷鏈� 90%

### Details
鏉ヨ嚜 MachineLearningMastery 2026 瓒嬪娍鍒嗘瀽锛�
1. **Plan-and-Execute Pattern**: 寮哄ぇ妯″瀷鍒跺畾绛栫暐 鈫� 渚垮疁妯″瀷鎵ц 鈫� 闄嶆湰 90%
2. **寮傛瀯鏋舵瀯涓夊眰绾�**: Frontier models (澶嶆潅鎺ㄧ悊/缂栨帓) 鈫� Mid-tier (鏍囧噯浠诲姟) 鈫� SLMs/Small models (楂橀鎵ц)
3. **鎴愮啛妯″紡**: 璇箟缂撳瓨 (0.92 闃堝€煎祵鍏ョ浉浼煎害) 娑堥櫎 20-40% LLM 璋冪敤
4. **浼佷笟钀藉湴鏏抽敭**: 璇嗗埆楂樹环鍊兼祦绋� 鈫� agent-first 閲嶈璁� 鈫� 鏄庣‘鎴愬姛鎸囨爣 鈫� 鎸佺画鏀硅繘
5. **OpenClaw 瀹炶返**: 褰撳墠 fallback 閾� (pro鈫択imi鈫抭wen鈫抔lm) 宸插疄鐜扮嚎鎬ч檷绾э紝浣嗙己灏� task-aware 璺敱

### Suggested Action
- 灏� task-aware model routing 绾冲叆鏋舵瀯鏀硅繘锛堢畝鍗曚换鍔¤嚜鍔ㄨ矾鐢卞埌鏇翠究瀹滄ā鍨嬶級
- explore: cron/heartbeat 鐢� qwen3.7-plus 鎴� glm-5.2 鑰岄潪 deepseek-v4-pro
- 璇勪及 semantic caching 鍙鎬�

### Metadata
- Source: web_search
- Tags: cost-optimization, plan-and-execute, heterogeneous-architecture, model-routing
- Pattern-Key: config.plan-execute-pattern
- Recurrence-Count: 1
- First-Seen: 2026-07-22
- Last-Seen: 2026-07-22

### Resolution
- **Resolved**: 2026-07-25T11:32:00+08:00
- **Notes**: 宸插疄鏂藉紓鏋勫缓妯￠檷鏈紙涓诲姏 pro鈫抐lash -68%锛夈€佸績璺虫ā鍨� mimo-v2.5銆佽法渚涘簲鍟� fallback 閾俱€侾lan-and-Execute 鏍稿績鎬濇兂宸茶惤瀹炰负 cron/蹇冭烦闅旂 + 浣庢垚鏈ā鍨� tiering銆俆ask-aware routing 擓轰笅涓€璺虫敼杩涙柟鍚戙€�

---

## [LRN-20260722-002] insight

**Logged**: 2026-07-22T14:15:00+08:00
**Priority**: high
**Status**: completed
**Area**: docs

### Summary
2026 AI Agent 寮€鍙戣寖寮忚浆鍨嬶細Prompt Engineering 鈫� System Engineering銆傜劍鐐逛粠鎻愮ず璇嶆妧宸ц浆鍚� guardrails銆乫eedback loops銆乷bservability

### Details
1. **鏍稿績杞彉**: 2026 骞� AI 寮€鍙戜笉鍐嶉潬鏇村ソ鐨� prompt锛岃€屾槸闈犲仴澹殑绯荤粺鏋舵瀯
2. **绯荤粺宸ョ▼涓夎绱�**: Guardrails (琛屼负杈圭晫) + Feedback Loops (鑷籂姝ｅ惊鐜�) + Observability (鍙娴嬫€�)
3. **Bounded Autonomy**: 娓呮櫚鐨勬搷浣滈檺鍒� + 蹇呴』鐨勪汉宸ュ崌绾ц矾寰� + 瀹屾暣瀹¤杩借釜
4. **楠岃瘉鎴戜滑鐨勬柟鍚戞纭�**: 
   - 鉁� .learnings/ + Pattern-Key = Feedback Loop
   - 鉁� ADL/VFM Protocol = Guardrails
   - 鉁� Daily notes + MEMORY.md 杩芥函浣撶郴 = Observability
   - 鉁� Skill Workshop + skill-vetter = Safety guardrails

### Suggested Action
- 鍦ㄦ灦鏋勬枃妗ｄ腑鏄惧紡鏍囨敞姣忎釜缁勪欢鐨勩€岀郴缁熷伐绋嬪睘鎬с€�(Guardrail/Feedback/Observability)
- 澧炲己 observability锛氬畾鏈� review session logs 鐨勮嚜鍔ㄥ寲
- 璇勪及鏄惁闇€瑕佹洿姝ｅ紡鐨� feedback loop 鎸囨爣锛堝姣忔鏀硅繘鍚庣殑鎴愬姛鐜囧彉鍖栵級...## [LRN-20260905-001] insight

**Logged**: 2026-09-05T12:14:00+08:00
**Priority**: high
**Status**: completed
**Area**: config
**Summary**: OpenClaw 2.0 发布 (v2026.8.1) 带来简化安装和协作 Agent 能力，Local-First 与 Model-Agnostic 趋势推动多供应商 fallback 和自托管架构，编码 Agent 采用领跑。
**Details**: 根据 Tavily 搜索和今日自改进研究，OpenClaw 2.0 简化了安装流程，增强了协作能力；用户推动数据本地化和框架独立性，OpenClaw 的跨供应商 fallback 链和自托管特性契合；编码 Agent 如 Claude Code、Devin、Cursor 成为开发者首选。
**Suggested Action**: 在技术任务中优先使用 coding agent skills；继续维护多供应商 fallback 链；考虑在 cron 任务中使用更便宜的模型。
**Metadata**: Source: tavily_search + self-improvement cron
Tags: openclaw-2.0, local-first, model-agnostic, coding-agent
Pattern-Key: config.openclaw-2.0-release
Recurrence-Count: 1
First-Seen: 2026-09-05
Last-Seen: 2026-09-05


## [LRN-20260907-001] insight

**Logged**: 2026-09-07T10:16:00+08:00
**Priority**: high
**Status**: completed
**Area**: config

### Summary
Persistent agents (always-on assistants) emerge as a 2026 trend, enabling longer workflows and local execution for data control.

### Details
Based on Tavily search and industry reports, persistent agents are designed to handle extended tasks, run locally, and maintain data privacy. They complement the shift toward local-first AI agents and reduce reliance on constant cloud invocation.

### Suggested Action
Consider designing agent workflows with persistent execution patterns for long-running tasks; evaluate local-first deployment options for sensitive workloads.

### Metadata
Source: tavily_search
Tags: persistent-agent, local-first, long-running
Pattern-Key: insight.persistent-agent-2026
Recurrence-Count: 1
First-Seen: 2026-09-07
Last-Seen: 2026-09-07

---

## [LRN-20260913-001] insight

**Logged**: 2026-09-13T08:00:00+08:00
**Priority**: high
**Status**: completed
**Area**: architecture

### Summary
Graph Engineering 确立为 2026 主流范式：多阶段并行执行 + 精确反馈路由取代串行循环，Codex Remote Sessions 为 OpenClaw 实践实证。

### Details
1. **演进时间线**: Context Engineering (mid-2025) → Loop Engineering (June 2026, Addy Osmani) → Graph Engineering (July 2026, Peter Steinberger/@steipete)
2. **核心差异**: Loop 串行循环 vs Graph 多阶段并行 + 精确反馈路由（非全循环回退）
3. **社区验证**: steipete 7/18 推文获 2.9M 浏览，48h 内产生 3 个竞争定义 + 虚假 Stanford 研究
4. **实践共识** (Eugeniu Ghelbur): small typed core + cheap indexing + hybrid retrieval + temporal supersession — 全部可在 markdown 文件上实现
5. **OpenClaw 实证**: Codex Remote Sessions (2026.7.2 beta) = 分布式 Agent 执行（桌面⇄节点⇄云 worker），即 Graph Engineering 的 OpenClaw 实践

### Suggested Action
- 设计多 Agent 工作流时优先采用图结构编排（Supervisor/Mesh/Marketplace 模式）
- 利用 OpenClaw subagent + sessions_spawn 实现并行阶段 + 精确反馈路由
- 关注 LangGraph node caching / deferred nodes / pre-post model hooks 生产原语

### Metadata
Source: tavily_search + self-improvement cron
Tags: graph-engineering, loop-engineering, multi-agent, codex-remote-sessions, openclaw
Pattern-Key: architecture.graph-engineering-2026
Recurrence-Count: 1
First-Seen: 2026-09-13
Last-Seen: 2026-09-13

---

## [LRN-20260913-002] insight

**Logged**: 2026-09-13T08:00:00+08:00
**Priority**: high
**Status**: completed
**Area**: memory

### Summary
记忆系统的「生命周期管理」（提取/更新/删除）比单纯存储更关键：陈旧记忆会主动降低智能体输出质量，向量检索 + 图遍历混合架构成标配。

### Details
1. **记忆四类型**: 短期(工作记忆/会话级) + 情景记忆(事件历史) + 语义记忆(事实/偏好/规则) + 程序记忆(技能/工作流)
2. **超越向量相似度**: 图记忆通过实体和关系检索事实，Mem0/Letta/Cognee/Zep 等 10+ 框架成熟
3. **新兴架构**: 分层系统、多智能体共享记忆、情感/上下文感知记忆
4. **生命周期三步曲**: Extract（提取）→ Update（更新/合并/去重）→ Delete（删除陈旧/矛盾），缺一不可
5. **陈旧记忆毒性**: 过时偏好、错误事实、冲突规则会主动污染推理，比无记忆更坏
6. **我们的架构对标**: Hermes 内置 memory tool + Obsidian vault + GitHub 同步 + 三层记忆（当前工作→daily notes→MEMORY.md），已具备雏形，需强化 Update/Delete 机制

### Suggested Action
- 在 cron/heartbeat 中引入定期「记忆清理」步骤：检测矛盾/过时条目并标记或归档
- 评估引入图记忆组件（Mem0/Letta/Cognee）作为 Hermes memory tool 补充
- 将「记忆生命周期管理」纳入 System Engineering Observability 支柱的监控指标

### Metadata
Source: tavily_search + self-improvement cron
Tags: memory-lifecycle, graph-memory, memory-architecture, agent-memory, mem0-letta
Pattern-Key: memory.lifecycle-management
Recurrence-Count: 1
First-Seen: 2026-09-13
Last-Seen: 2026-09-13

---

## [LRN-20260914-001] insight

**Logged**: 2026-09-14T10:15:00+08:00
**Priority**: high
**Status**: completed
**Area**: config

### Summary
OpenClaw 2.0 (v2026.8.1) 发布后进入极速补丁节奏：v2026.8.2(9/1)→v2026.9.1(9/3)→v2026.9.2(9/5 GPT-6 Astra+Swarm 默认开启)→v2026.9.3(9/8 Node 24.16+持久化技能)→v2026.9.4(9/11 回滚失败更新+统一插件工作区)，半个月内 6 个版本，体现大版本后的激进迭代策略。

### Details
1. **发布节奏变化**: 从「每两天一版」转为「七周大版本整合 → 每日补丁」模式，933 贡献者 16K+ PR 积压一次性合入后需快速修复回归
2. **关键特性时间线**:
   - v2026.8.1: 共享云会话、凭证隔离、简化安装、重构浏览器应用
   - v2026.8.2: Day-one patch，更安全的升级路径
   - v2026.9.1: 升级韧性、图表、快速启动、Android 对齐
   - v2026.9.2: **GPT-6 Astra**、**Swarm 默认开启**、重启无损回复
   - v2026.9.3: Node 24.16+ 强制、**持久化技能**、**可分享会话**
   - v2026.9.4: 失败更新回滚、统一 Plugins 工作区、预备云会话
3. **架构信号**: Swarm 默认开启 = 多 Agent 编排从实验性转为生产默认；持久化技能 = Skill 生命周期管理原生化

### Suggested Action
- **暂缓升级**: 遵循 LRN-20260724-002「大版本等 2-4 周社区验证」，当前 v2026.9.x 仍处于激进补丁期
- 关注 v2026.9.3 的「持久化技能」与我们的 Skill Workshop 流程对标
- 评估「可分享会话」对协作场景的实际价值
- Swarm 默认开启意味着多 Agent 编排已成生产基线，需在工作流设计中默认考虑

### Metadata
Source: tavily_search (cellcog.ai blog release timeline) + self-improvement cron
Tags: openclaw-2.0, rapid-patching, swarm-default, persistent-skills, shareable-sessions
Pattern-Key: config.openclaw-2.0-rapid-patches
Recurrence-Count: 1
First-Seen: 2026-09-14
Last-Seen: 2026-09-14

---

## [LRN-20260914-002] insight

**Logged**: 2026-09-14T10:15:00+08:00
**Priority**: high
**Status**: completed
**Area**: security

### Summary
AI Agent 安全标准化进入实质推进期：Mastercard 倡议全球协调标准、NIST 发布、新加坡 IMDA Model Governance Framework —— 安全从「事后加固」升为「准入门槛」。OpenClaw Security 2026 体系五大控制点（最小权限 Token、RBAC 审批门、沙箱运行时、提示注入防御、完整审计日志）+ 三大具体化（SSRF deny、Secret egress host binding、Webhook throttling）形成可落地清单。

### Details
1. **三大标准化推手**:
   - **Mastercard**: 「Agentic Commerce」安全规则，强调早期采纳最佳实践 + 持续监控 + 全球协调标准
   - **NIST**: AI RMF 1.0 扩展至 Agentic AI，提供可测量的风险管理框架
   - **IMDA 新加坡**: Model Governance Framework 2.0，涵盖 Agent 生命周期治理
2. **OpenClaw 五控制点 + 三具体化** (2026 版):
   - Least-privilege tokens (最小权限凭证)
   - RBAC approval gates (RBAC 审批门控)
   - Sandbox tool runtime (沙箱工具运行时)
   - Prompt injection defense (提示注入防御)
   - Complete audit logging (完整审计日志)
   - SSRF explicit deny (新 URL 需显式加入 urlAllowlist)
   - Secret egress host binding (密钥绑定精确 HTTPS 出口宿主)
   - Webhook auth throttling (HTTP 429 后等待 60s)
3. **EU AI Act 生效 (8月)**: 多 Agent 编排归类 high-risk，强制要求 HITL + 审计 + 身份管理
4. **生产部署 8 大最佳实践** (InfoQ 2026): 全链路监控、高可用灾备、最小权限+审计、置信度阈值+人工升级、内容过滤+Guardrails、自动测试+Cannary、模型版本控制+快速回滚、成本优化(模型路由 60-70% + Prompt Caching 60-80% + Batch API 50%)

### Suggested Action
- 将上述 8 点纳入我们的架构审查清单（尤其是成本优化三件套已在落地：模型路由 + 语义缓存 + cheap-model tiering）
- Secret egress host binding 机制评估：是否需在 openclaw.json 中显式配置密钥出口域名白名单
- 审计日志完整性：确保 cron/heartbeat/subagent 执行轨迹可追溯
- 关注 NIST/IMDA 正式标准发布后的合规对标

### Metadata
Source: tavily_search (Mastercard blog + InfoQ + self-improvement cron 9/13 回顾)
Tags: ai-agent-security, mastercard, nist, imda, eu-ai-act, security-standards
Pattern-Key: security.ai-agent-standardization-2026
Recurrence-Count: 1
First-Seen: 2026-09-14
Last-Seen: 2026-09-14