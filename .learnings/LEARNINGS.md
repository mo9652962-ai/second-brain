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

## [LRN-20260925-001] correction

**Logged**: 2026-09-26T12:20:00+08:00
**Priority**: high
**Status**: resolved
**Area**: infra

### Summary
检测器读错字段名会把「全部异常」报成「全部正常/空」——比误报更危险，因为它不会引来任何人排查

### Details
1. `scripts/cron_health.py:115` 写 `last = j.get("last_run") or {}`，但 `cron/jobs.json` 的 schema 是**扁平字段** `last_status` / `last_run_at` / `last_error`，**没有 `last_run` 键**（实测 `sum(1 for j in jobs if 'last_run' in j) == 0`）。
2. 于是 `last` 恒为空 dict → 47 个任务全部落进 `else: icon = "⚪"; never_count += 1`，看板输出 `✅ 0 正常 ❌ 0 错误 ⚪ 47 从未执行`；而真实状态是 `Counter({'ok': 37, 'error': 7, 'delivery_failed': 3})` —— **7 个真实 error 被完全掩盖**。
3. 更隐蔽的一层：当日日报（`memory/2026-09-25.md:69`）看到了这个荒谬输出，却给它**编了一个合理解释**（「所有 cron 任务目前显示为『从未执行』，因为今日尚未到达调度时间」），而不是怀疑检测器。
4. 同类复发链：9/5「假阳性税」、9/7「verify 基线对照」、8/8「health 全绿掩盖静默失败」——本次形态不同：前几次检测器**误报异常**（有人会去查），本次是检测器**把异常报成空**（无人会去查）= 静默失败。

### Suggested Action
- 修复：改读扁平字段 `last_status` / `last_run_at` / `last_error`，并给 `delivery_failed` 独立图标（📭）
- **加自检护栏**：`if never_count == len(jobs) and len(jobs) > 0` → 输出显式告警「全部任务被判从未执行，极可能是 schema 变更后字段名失配」
- 通用规则：**「物理上不可能的全体值」（100% 全绿 / 100% 全空）必须让检测器自己喊出来**，不要依赖人去发现
- 检测器读外部文件时，先 `print(sorted(j.keys()))` 核对真实 schema，不凭记忆写字段名

### Metadata
- Source: local debugging
- Tags: cron, health-check, detector-bug, silent-failure, schema-mismatch, false-negative
- Pattern-Key: infra.detector-schema-mismatch-masks-all-errors
- Recurrence-Count: 4
- First-Seen: 2026-08-08
- Last-Seen: 2026-09-26

### Resolution
- **Resolved**: 2026-09-26T12:15:00+08:00
- **Notes**: 已 patch `AppData/Local/hermes/scripts/cron_health.py`（3 处：字段读取 / delivery_failed 分支 / 自检护栏），实测看板恢复真实值 37/7/3/0

## [LRN-20260925-002] best_practice

**Logged**: 2026-09-26T12:20:00+08:00
**Priority**: high
**Status**: adopted
**Area**: research

### Summary
web_extract 报 `Blocked: private or internal network address` 时重试永远无效——本机 FlClash fake-ip 与工具侧「内网地址」策略不兼容，直接切 curl

### Details
1. 症状：`web_extract` 对**任何**公网 URL 都返回 `Blocked: URL targets a private or internal network address`。
2. 根因（实测坐实）：本机 DNS 走 FlClash **fake-ip 段** —— `nslookup arxiv.org` → `198.18.0.102`；工具侧把 198.18.0.0/15 判定为内网地址而拦截。**不是代理坏了**：`curl https://arxiv.org/abs/2609.30266` → HTTP 200 / 0.46s。
3. 时间线：2026-09-25 首次记录（当日 4 次 web_extract 全部 Blocked），**2026-09-26 复核仍复现** → 非偶发，是稳定不兼容。
4. 当日研究全部改走 curl 直连兜底并成功：arxiv.org abs 页逐篇 / f-droid.org 35,993B / launchvideo.io 26,378B / keepandroidopen.org 367,806B，四站全 200。

### Suggested Action
- 遇到 `Blocked: private or internal network address` → **不要重试 web_extract**，直接 `curl -s -m 30 "<URL>" -o out.html` + Python regex 清洗
- 验证手段可降级，**验证标准不降级**（与 9/7 curl 兜底核对 arXiv 官方源同一原则）
- 已固化进 `link-content-fetch` 决策树 `⓪` 号分支（本次 patch）

### Metadata
- Source: local debugging
- Tags: web-extract, curl-fallback, flclash, fake-ip, proxy, channel-failure
- Pattern-Key: research.web-extract-fakeip-block-curl-fallback
- Recurrence-Count: 2
- First-Seen: 2026-09-25
- Last-Seen: 2026-09-26

### Resolution
- **Resolved**: 2026-09-26T12:18:00+08:00
- **Notes**: patch `research/link-content-fetch/SKILL.md` 决策树插入 `⓪` 分支（故障识别 → 正确动作压进第一格，无需回忆）

## [LRN-20260925-003] knowledge_gap

**Logged**: 2026-09-26T12:20:00+08:00
**Priority**: medium
**Status**: resolved
**Area**: infra

### Summary
产出型 cron 失败后无缺口感知：反思 cron 连断 4 天（9/21~9/24），产物缺失只入哈希账本、从不告警

### Details
1. `cron/executions.db` 实测：daily-self-improvement 9/22-9/24 连续 3 天 `failed`（HTTP 429 火山 ARK 配额），9/25 `unknown`（12:48 机器重启）→ 应产出的 `2026-09-2[1-4]-reflection.md` **四份全部不存在**。
2. 连带损失：反思的「🔄 上次反思行动项核查」闭环**断 4 天**——09-20 反思的 8 个行动项期间无人追踪。
3. `status=unknown` 的隐蔽性：jobs.json 的 `last_status` 仍显示旧值 error，**只有 executions.db 的批次 + 开机时长能还原真相**。
4. 告警缺口：`deterministic-verify` 的 5 项异常**不含 reflection**；`cron_product_hash.py` 虽把 reflection 记成 `MISSING`（账本 9/25 实测有该行），但 **MISSING 只入账本、不告警**。

### Suggested Action
- `cron_product_hash.py --verify` 的 MISSING 加**告警**输出（现只入账本）
- `deterministic-verify` 哨兵清单纳入 `*-reflection.md`
- 反思跨缺口补位时，「上次反思行动项核查」**不因中间空档而跳过**，直接对最后一份有效反思做核查（本次已执行）

### Metadata
- Source: local debugging
- Tags: cron, reflection, silent-failure, missing-artifact, alerting, quota-429
- Pattern-Key: infra.producer-cron-missing-artifact-no-alert
- Recurrence-Count: 3
- First-Seen: 2026-08-08
- Last-Seen: 2026-09-25

### Resolution
- **Resolved**: 2026-09-26T12:25:00+08:00
- **Notes**: 本次反思已跨缺口核查 09-20 行动项 8 项；告警改进登记为行动项交 daily-todo-executor

---

## [LRN-20261002-001] insight

**Logged**: 2026-10-02T12:31:00+08:00
**Priority**: high
**Status**: completed
**Area**: config

### Summary
OpenClaw 2026.9.7 发布：负载响应更快、长对话更流畅、更新回滚保护增强、新增 OpenAI Agents API + Sign in with ChatGPT (Beta)、移除已退役的 Sora 视频生成。2,818 PR、344 贡献者，半个月内 6 版本极速补丁节奏延续。

### Details
1. **关键变更**:
   - 更好的更新备份和回滚保护，修复从 2026.9.5 升级问题
   - OpenAI Agents API 公测集成：托管 Agent 循环、Data Agent、GPT-Live-1 全双工语音、免费托管沙箱
   - Sign in with ChatGPT (Beta) 降低准入门槛
   - Sora 退役：需替换 `openai/sora-2` / `openai/sora-2-pro` 为 Kie AI、Z.AI、Novita、Qwen、Alibaba Wan 等
   - Mac/iPhone/iPad 聊天体验改进，重启后工作恢复更好

2. **架构信号**: 持续的「每日补丁」模式印证 LRN-20260914-001 —— 大版本后进入激进修复期，建议继续暂缓升级等社区验证

### Suggested Action
- 监控社区反馈 2-4 周后再评估升级
- 关注 OpenAI Agents API 集成对我们多供应商 fallback 架构的影响
- 确认 Sora 替代方案在 video generation skills 中的可用性

### Metadata
Source: tavily_search (docs.openclaw.ai/releases/2026.9.7) + self-improvement cron
Tags: openclaw-2.0, rapid-patches, openai-agents-api, sora-retirement
Pattern-Key: config.openclaw-2.0-rapid-patches-continued
Recurrence-Count: 1
First-Seen: 2026-10-02
Last-Seen: 2026-10-02

---

## [LRN-20261002-002] best_practice

**Logged**: 2026-10-02T12:31:00+08:00
**Priority**: high
**Status**: adopted
**Area**: security

### Summary
OpenClaw 官方最佳实践指南 2026 核心四原则：Gateway 私有化部署、扩展代码即运行代码、最小权限凭证轮换、刻意修改默认值并记录原因。

### Details
1. **Gateway 私有化部署** (最高优先级):
   - 绑定 `127.0.0.1` + SSH 隧道/VPN 访问
   - 强制 TLS 1.2+，要求认证，限制源地址
   - 验证 WebSocket origin validation (同网络浏览器也是攻击路径)
   - `openclaw gateway status` 定期检查而非假设

2. **扩展代码即运行代码**:
   - 审查 declared capabilities、版本、来源再启用
   - Pin 版本：npm `--pin` / Git `--ref <40-char-SHA>`
   - Misbehave 时 disable 而非 delete (保留配置诊断)
   - 特别警惕 message-injection capability (Hermes 对应 `allow_gateway_injection`)

3. **最小权限凭证轮换**:
   - 每 Agent 独立模型 Key，可单独吊销
   - 定期轮换而非事后补救
   - 密钥存凭证存储，不烘焙进镜像/Shell profile

4. **刻意修改默认值并记录原因**:
   - 大多数故障源于为解决一事改默认值后遗忘
   - 配置入版本控制，每个非默认值写一句话备注
   - 排查前先读配置而非怪框架

### Suggested Action
- 将上述四原则纳入架构审查清单 (与 LRN-20260914-002 8 大最佳实践合并)
- 审计当前 openclaw.json 非默认值并补全备注
- 评估 Secret egress host binding 实施 (密钥出口域名白名单)
- 确保 cron/heartbeat/subagent 审计轨迹完整可追溯

### Metadata
Source: tavily_search (openclawlaunch.com/guides/openclaw-best-practices) + self-improvement cron
Tags: openclaw-best-practices, gateway-security, extension-security, credential-rotation, config-drift
Pattern-Key: security.openclaw-best-practices-2026
Recurrence-Count: 1
First-Seen: 2026-10-02
Last-Seen: 2026-10-02

---

## [LRN-20261002-003] insight

**Logged**: 2026-10-02T12:31:00+08:00
**Priority**: high
**Status**: completed
**Area**: architecture

### Summary
OpenClaw Skills Directory 爆发式增长至 5,798+ 社区技能，1,800+ AI Agent 专用技能，安装/发现已成核心工作流入口。

### Details
1. **规模跃升**: 从数百增长到 5,798+，覆盖 Automation/Communication/Creative/Crypto/Data/Development/DevOps 等 10+ 大类
2. **Top 10 技能分类**已成标准化发现入口
3. **Skill 生态成熟度**: `clawhub install @author/slug` 标准化流程 + skill-vetter 审计 + 版本管理
4. **对我们的启示**: 我们的 27+ skills 安装体系已具雏形，Skill Workshop 流程与官方「持久化技能」(v2026.9.3) 方向一致

### Suggested Action
- 继续维护 Skill Workshop 质量门控 (skill-vetter + 社区下载量对比)
- 关注官方持久化技能机制与我们的 Skill Workshop 对标
- 评估高频任务是否可封装为可复用 skill 贡献社区

### Metadata
Source: tavily_search (openclawai.io/skills) + self-improvement cron
Tags: openclaw-skills, skill-ecosystem, skill-workshop, clawhub
Pattern-Key: ecosystem.openclaw-skills-explosion
Recurrence-Count: 1
First-Seen: 2026-10-02
Last-Seen: 2026-10-02

---

## [LRN-20261002-004] insight

**Logged**: 2026-10-02T12:31:00+08:00
**Priority**: high
**Status**: completed
**Area**: operations

### Summary
AI Agent 运营实践成熟 (IBM/Deloitte 2026)：企业从「构建 Agent」转向「安全规模化运营」，确立风险分级运营模型。

### Details
1. **关键运营活动** (IBM 2026):
   - 监控执行 / 跟踪完成 / 审查失败 / 测量工具使用 / 延迟成本
   - 管理提示配置 / 更新知识源 / 审查权限 / 发布前测试
   - 审计高影响动作 / 管理人工升级 / 退役低价值 Agent

2. **风险分级运营模型** (Deloitte 2026):
   - 例行信息检索 → Agent 主导
   - 重复数据处理 → Agent 主导
   - 低风险工作流动作 → Agent 带控制
   - 中风险决策 → Agent 建议 + 人工批准
   - 高影响决策 → 人工主导 + Agent 支持
   - 异常和模糊情况 → 人工主导
   - 战略决策 → 人工主导 + AI 分析

3. **员工角色转变**: 从手工完成每步 → 定义目标、审查输出、处理异常、批准动作、改进工作流

### Suggested Action
- 将风险分级模型纳入我们的多 Agent 工作流设计 (Graph Engineering 编排)
- 为 cron/heartbeat/subagent 建立显式的风险等级标注
- 完善「退役低价值 Agent」的评估机制 (定期 ROI 复盘)
- 强化 Observability: 自动化 review session logs、工具使用统计、成本追踪

### Metadata
Source: tavily_search (xicom.biz AI Agent Trends 2026) + self-improvement cron
Tags: ai-agent-operations, risk-tiered-operations, ibm-deloitte-2026, bounded-autonomy
Pattern-Key: operations.ai-agent-operations-maturity-2026
Recurrence-Count: 1
First-Seen: 2026-10-02
Last-Seen: 2026-10-02

---

## [LRN-20261002-005] insight

**Logged**: 2026-10-02T12:31:00+08:00
**Priority**: medium
**Status**: completed
**Area**: config

### Summary
OpenClaw 生态分化加速：NanoClaw/PicoClaw/Nanobot/memU/OpenCode/Claude Code/ZeroClaw/Moltworker/NullClaw/Anything LLM/TrustClaw 等 12+ 替代方案涌现，但轻量级 fork (nanoclaw/zeroclaw/ironclaw/picoclaw) 缺乏生产验证，社区共识是碎片化而非打磨替代品。

### Details
1. **替代方案画像**:
   - NanoClaw: 容器隔离安全优先
   - PicoClaw: 极简极速部署
   - Nanobot: 轻量 Python + 持久化记忆
   - memU: 主动知识图谱助手
   - OpenCode: Go 多 LLM 编码
   - Claude Code: 沙箱 + 显式权限 + Anthropic 安全基建
   - ZeroClaw: 超极简无花哨
   - Moltworker: 嵌入式安全稳定执行
   - NullClaw: Zig 边缘 IoT
   - Anything LLM: 自定义 LLM 应用
   - TrustClaw: 企业级安全平台

2. **社区信号**:
   - Reddit r/LocalLLaMA: fork 处于实验期，缺乏生产验证
   - PaulGugAI (X, 2026-07): "OpenClaw update stability has regressed! 最后两个更新导致 gateway 无法启动"
   - 维护负担成切换主要理由

3. **我们的定位**: OpenClaw Core (TypeScript、368K stars、Self-hosted、多供应商 fallback、本地数据主权) 仍为主流选择，Claude Code 为互补 (编码专用)

### Suggested Action
- 维持 OpenClaw Core 主力 + Claude Code 编码互补策略
- 关注 NanoClaw 安全隔离模式在高敏感场景的适用性
- 暂不投入轻量 fork 生态 (生产验证缺失)
- 监控 OpenClaw 稳定性回归 (v2026.9.x 补丁期)

### Metadata
Source: tavily_search (larksuite.com + vellum.ai blog) + self-improvement cron
Tags: openclaw-alternatives, ecosystem-fragmentation, stability-regression, claude-code-complement
Pattern-Key: ecosystem.openclaw-alternatives-landscape-2026
Recurrence-Count: 1
First-Seen: 2026-10-02
Last-Seen: 2026-10-02
