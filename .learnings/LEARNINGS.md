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
Plan-and-Execute 妯″紡 + 寮傛瀯妯″瀷鏋舵瀯锛欶rontier 妯″瀷璐熻矗瑙勫垝霤勫垝鍜屽鏉傛帹鐞嗭紝cheap model 鎵ц楂橀浠诲姟锛岀患鍚堥檷鏈� 90%

### Details
鏉ヨ嚜 MachineLearningMastery 2026 瓒嬪娍钃嗘瀽锛�
1. **Plan-and-Execute Pattern**: 寮哄ぇ妯″瀷鍒跺畾绛栫暐 鈫� 渚垮疁妯″瀷鎵ц 鈫� 闄嶆湰 90%
2. **寮傛瀯鏋舵瀯涓夊眰绾�**: Frontier models (澶嶆潅鎺ㄧ悊/缂栨帓) 鈫� Mid-tier (鏍囧噯浠诲姟) 鈫� SLMs/Small models (楂橀鎵ц)
3. **鎴愮啛妯″紡**: 璇箟缂撳瓨 (0.92 闃堝€煎祵鍏ョ浉浼煎害) 娑堥櫎 20-40% LLM 璋冪敤
4. **浼佷笟钀藉湴鏏抽敭**: 璇嗗埆楂樹环鍊兼祦绋� 鈫� agent-first 閲嶈璁� 鈫� 鏄庣‘鎴愬姛鎸囨爣 鈫� 鎸佺画鏀硅繘
5. **OpenClaw 瀹炶返**: 褰撳墠 fallback 閾� (pro鈫択imi鈫抭wen鈫抔lm) 宸插疄鐜扮嚎鎬ч檷绾э紝浣嗙己灏� task-aware 璺敱

### Suggested Action
- 灏� task-aware model routing 绾冲叆鏋舵瀯鏀硅繘锛堢畝鍗曚换鍔¤嚜鍔ㄨ矾鐢卞埌鏇翠究瀹滄ā�嬶級
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
- **Notes**: 宸插疄鏂藉紓鏋勫缓妯￠檷鏈紙涓诲姏 pro鈫抐lash -68%锛夈€佸績璺虫ā�鍨� mimo-v2.5銆佽法渚涘簲鍟� fallback 閾俱€侾lan-and-Execute 鏍稿績鎬濇兂宸茶惤瀹旂 + 浣庢垚鏈ā�鍨� tiering銆俆ask-aware routing 擓轰笅涓€璺虫敼杩涙柟鍚戙€�

---

## [LRN-20260722-002] insight

**Logged**: 2026-07-22T14:15:00+08:00
**Priority**: high
**Status**: completed
**Area**: docs

### Summary
2026 AI Agent 寮€鍙戣寖寮忚浆鍨嬶細Prompt Engineering 鈫� System Engineering銆傜劍鐐逛粠鎻愮ず璇嶆妧宸ц浆鍚� guardrails銆乫eedback loops銆乷bservability

### Details
1. **鏍稿績杞彉**: 2026 骞� AI 寮€鍙戜笉鍐嶉潬鏇村ソ� prompt锛岃€屾槸闈犲仴澹殑绯荤粺鏋舵瀯
2. **绯荤粺宸ョ▼涓夎绱�**: Guardrails (琛屼负杈圭晫) + Feedback Loops (鑷籂姝ｅ惊鐜�) + Observability (鍙娴嬫€�)
3. **Bounded Autonomy**: 娓呮櫚�搷浣滈檺� + 蹇呴』�纟寰� + 瀹屾暣瀹¤杩借釜
4. **楠岃瘉鎴戜滑鐨勬柟�戞�纭�**: 
   - 鉁� .learnings/ + Pattern-Key = Feedback Loop
   - 鉁� ADL/VFM Protocol = Guardrails
   - 鉁� Daily notes + MEMORY.md 杩芥函浣撶郴 = Observability
   - 鉁� Skill Workshop + skill-vetter = Safety guardrails

### Suggested Action
- 鍦ㄦ灦鏋勬枃妗ｄ腑鏄惧紡�勩€岀郴缁熷伐绋嬪睘鎬с€�(Guardrail/Feedback/Observability)
- 澧炲己 observability锛氬畾鏈� review session logs 鐨勮嚜鍔ㄥ寲
- 璇勪及�勄惁闇€瑕佹洿姝ｅ紡� feedback loop 鎸囨爣�堝姣忔?硅繘?庣殑?录?彉?囗?

... (truncated)

---

## [LRN-20261020-001] correction

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: open
**Area**: infra

### Summary
pydantic_core ABI 问题：10-12 误判 resolved，10-13/10-14/10-16/10-18 四度复发/预测命中，根因已闭合

### Details
- **误判时间线**: 10-12 仅做进程内 `import pydantic_core` 探针验证，未重启 gateway 复验 → 误标 resolved
- **复发证据链**: 10-13/10-14/10-16/10-18 四次 gateway 重启后均复发，`gateway-exit-diag.log` 三次 `"python": "3.14.7"` 为证
- **根因闭合**: 运行解释器 (tools/python-3.14.7, cp314) 与 hermes-agent/venv (cp311) site-packages ABI 混用
- **修正判定口径** (此后所有 ERR 条目适用):
  1. "resolved" 必须含**一次 gateway 重启后的复验**，否则只标 `mitigated`
  2. 证据不得用同进程自证指标，须用跨进程指标
  3. 涉及解释器/依赖路径修复，必须核对 `gateway-exit-diag.log` 的 `"python"` 字段
  4. launcher 为陈旧生成物时，重跑 `gateway install` 验证须含 launcher diff + 重启后 python 字段
- **三条修复路径** (按侵入性排序，实测均 PASS):
  ① PYTHONPATH 叠加 PM venv site-packages
  ② `get_python_path()` 返回 PM venv python (上游本意)
  ③ **重跑 `gateway install` 重新生成 launcher (推荐，最省事且符合上游设计)**
- **当前状态**: `mitigated` (本进程正常)，下次重启仍会复发，**根治需 sora 选路径执行**

### Suggested Action
- sora 从三条路径选一执行根治 (建议方案 ③)
- 此后所有基础设施修复必须包含 gateway 重启复验
- 陈旧账本 (32 个 cron failure_streak 停在 10-11) 待新排程自然覆盖

### Metadata
- Source: daily-self-improvement cron + 实测复现
- Tags: pydantic-abi, abi-mismatch, regression, verification-criteria, gateway-restart
- Pattern-Key: infra.pydantic-abi-mismatch-regresed
- Recurrence-Count: 4
- First-Seen: 2026-10-12
- Last-Seen: 2026-10-20

---

## [LRN-20261020-002] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: completed
**Area**: config

### Summary
OpenClaw 2026.9.7/9.8: OpenAI Agents API 公测、Sora 退役、Sign in with ChatGPT

### Details
- **OpenAI Agents API 公测** (v2026.9.7): 托管 Agent 循环 (会话管理、自动重试、摘要生成、工具编排内置)、Data Agent (连企业数据源: Drive/Notion/Slack/Confluence)、GPT-Live-1 全双工语音、**免费托管沙箱** (仅计费模型 token + 工具使用) — 大幅降低构建门槛
- **Sora 视频生成正式退役**: 官方建议替代: Kie AI / Z.AI / Novita / Qwen / Wan，需评估对 video generation skills 影响
- **Sign in with ChatGPT (Beta)**: 新增认证方式，降低用户接入门槛
- **v2026.9.8** (10/8): 优化 Codex Remote Sessions 目录处理，复用捕获设置减少重复内存使用
- **补丁节奏**: 半个月 6 版本，**建议暂缓升级等社区验证 2-4 周**

### Suggested Action
- 评估 OpenAI Agents API 对现有多供应商 fallback 架构影响
- 评估 Sora 退役对 video generation skills 影响，制定替代方案
- 关注社区验证进度，2-4 周后决定升级时机

### Metadata
- Source: tavily_search (OpenCrawl 官方文档、社区讨论)
- Tags: openclaw, openai-agents-api, sora-deprecated, authentication
- Pattern-Key: config.openclaw-2.0-rapid-patches-continued-v3
- Recurrence-Count: 3
- First-Seen: 2026-10-17
- Last-Seen: 2026-10-20

---

## [LRN-20261020-003] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: completed
**Area**: operations

### Summary
AI Agent 运营风险分级模型 (IBM/Deloitte 2026): 7 级分级，从 Agent 主导到人工主导

### Details
1. **例行检索** → Agent 主导 (自动化率最高)
2. **低风险动作** → Agent 带控制 (Agent 执行，人工设置边界)
3. **中低风险决策** → Agent 建议 + 人工确认
4. **中风险决策** → Agent 建议 + 人工批准
5. **中高风险决策** → 人工主导 + Agent 支持
6. **高风险决策** → 人工主导 + Agent 顾问
7. **关键/不可逆决策** → 完全人工 (Agent 仅提供信息)

### Suggested Action
- 将风险分级模型纳入 Graph Engineering 编排设计
- 为每个 cron/skill 任务标注风险等级，配置相应的人工介入门控
- 评估现有自动化任务的风险分级覆盖度

### Metadata
- Source: tavily_search (IBM/Deloitte 2026 运营成熟度报告)
- Tags: risk-tiered-ops, agent-operations, governance, bounded-autonomy
- Pattern-Key: operations.ai-agent-risk-tiered-ops-2026
- Recurrence-Count: 3
- First-Seen: 2026-10-17
- Last-Seen: 2026-10-20

---

## [LRN-20261020-004] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: completed
**Area**: architecture

### Summary
持久化 Agent 趋势 + Local-First 转型确认 (2026 核心共识)

### Details
- 设计用于长任务、本地执行、数据主权
- 配合 Local-First 转型：数据不出本地、离线可用、用户完全控制
- OpenClaw、Hermes、ZeroClaw 等本地优先框架增长最快
- 企业级部署趋同：自托管 + 数据主权 + 合规优先

### Suggested Action
- 确认当前架构已符合 Local-First 原则 (本地 Gateway + 本地存储 + 无强制云依赖)
- 评估云端服务依赖 (模型 API、搜索 API) 的可替代性
- 推进本地模型部署能力 (Ollama + 本地 embedding)

### Metadata
- Source: tavily_search (Turing Post 2026、多厂商路线图)
- Tags: persistent-agent, local-first, data-sovereignty, offline-capable
- Pattern-Key: architecture.persistent-agent-local-first-2026
- Recurrence-Count: 3
- First-Seen: 2026-10-17
- Last-Seen: 2026-10-20

---

## [LRN-20261020-005] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: completed
**Area**: security

### Summary
NIBVOK AI Security v0.1.2: 运行时策略层，逐工具调用 enforce allow/confirm/deny

### Details
- **非扫描器而是强制点**: 在工具调用执行前拦截，基于策略决定 allow/confirm/deny
- **填补空白**: 从「工具名匹配」进阶到「命令语义判断」
- **已入 ClawHub 注册表**: 可通过 Skill Workshop / ClawHub 安装评估
- **与现有安全栈互补**: SSRF deny + Secret egress binding + Webhook 限流 + RBAC 审批 + 审计日志 + NIBVOK 运行时策略 = 6 层纵深防御

### Suggested Action
- 评估集成可行性：作为 OpenClaw Gateway 的运行时策略插件
- 对比现有 security-audit skill 的覆盖范围
- 若集成，需在 openclaw.json 配置策略规则

### Metadata
- Source: tavily_search (NIBVOK 官方发布、ClawHub 注册表)
- Tags: nibvok, runtime-policy, security-layer, tool-call-enforcement
- Pattern-Key: security.nibvok-runtime-policy-layer
- Recurrence-Count: 2
- First-Seen: 2026-10-19
- Last-Seen: 2026-10-20

---

## [LRN-20261020-006] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: completed
**Area**: architecture

### Summary
韧性设计验证：no_agent 纯脚本核心链路 P0 阻塞下 100% 存活

### Details
- **验证场景**: pydantic_core ABI 问题导致 32/48 cron 任务失败 (依赖 LLM 初始化 OpenAI client)
- **存活组件**: open-actions-broadcast、cron-health-board、health-degraded-fallback、obsidian-github-sync、workbuddy-proxy-watchdog、每日学习计划/回顾、闲鱼提醒 — 全为 no_agent 纯脚本，不调用 LLM、不初始化 OpenAI client
- **设计启示**: 核心感知/决策链路必须具备 no_agent 降级能力；"降级版 health / 纯脚本播报" 架构有效
- **指标**: 核心感知链路存活率 100% (7/7)，业务 cron 存活率 29% (14/48)

### Suggested Action
- 新增 cron 任务默认要求提供 no_agent 降级版本
- 将 "纯脚本降级能力" 纳入 cron 设计评审清单
- 为现有高优先级 cron 补齐降级实现

### Metadata
- Source: daily-summary cron 10-18 实测验证
- Tags: resilience, no-agent-scripts, graceful-degradation, core-perception
- Pattern-Key: architecture.resilience-no-agent-scripts
- Recurrence-Count: 2
- First-Seen: 2026-10-18
- Last-Seen: 2026-10-20

---

## [LRN-20261020-007] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: open
**Area**: infra

### Summary
模型配额危机三重奏：OpenRouter 429 + deepseek 402 + opencode-go 400

### Details
- **OpenRouter 免费模型**: 日限额耗尽 → 429 (nvidia/nemotron-3-ultra 等免费模型)
- **DeepSeek 直连**: 余额不足 → 402 (fangzhou-2 / jiyuanlvdong 等)
- **opencode-go**: 缺 x-opencode-session 标识 → 400 (上游供应商侧问题)
- **三重同时发生**: 导致所有模型后端同时不可用，fallback 链失效
- **根因**: 缺乏 task-aware 模型路由，cron/heartbeat 等低复杂度任务占用昂贵/配额受限模型

### Suggested Action
- **P0**: 为 cron/heartbeat 引入 task-aware 模型路由，分流至 cheap tier (qwen3.7-plus / glm-5.2)
- 建立模型配额监控告警 (日消耗 > 80% 触发告警)
- 评估本地模型部署 (Ollama) 作为最终兜底
- 考虑为不同任务类型配置专用模型池

### Metadata
- Source: daily-summary cron 10-18/10-19 实测观测
- Tags: model-quota, fallback-failure, task-aware-routing, cheap-tier
- Pattern-Key: infra.model-quota-crisis-2026-q4
- Recurrence-Count: 2
- First-Seen: 2026-10-18
- Last-Seen: 2026-10-20

---

## [LRN-20261020-008] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: open
**Area**: infra

### Summary
C 盘 92% 临界：需清理/迁移大文件防故障

### Details
- **当前状态**: C: 38G/448G (92%)，临界阈值
- **风险**: 磁盘满将导致 gateway/cron/数据库写入失败、日志无法轮转、临时文件创建失败
- **潜在大文件**: Hermes logs、OpenClaw cache、模型缓存、临时文件、Obsidian vault
- **对比**: 10-18 daily-summary 已标记为风险项，至今未处理

### Suggested Action
- 扫描 C 盘大文件/目录 (WinDirStat / TreeSize / PowerShell)
- 迁移可移动数据: logs → D 盘、cache → D 盘、vault 备份 → 网盘/NAS
- 设置磁盘使用率告警 (>85% 告警, >95% 关机保护)
- 定期清理临时文件、旧日志归档

### Metadata
- Source: daily-summary cron 10-18 系统指标采集
- Tags: disk-space, critical-threshold, cleanup, migration
- Pattern-Key: infra.disk-critical-92pct
- Recurrence-Count: 2
- First-Seen: 2026-10-18
- Last-Seen: 2026-10-20

---

## [LRN-20261020-009] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: completed
**Area**: memory

### Summary
AI Agent 记忆三层架构标准化：Core/Recall/Archival + Graph-native (Cognee) 企业级首选

### Details
- **三层标准** (Letta/MemGPT 成熟实现):
  - Core Memory (in-context): Agent 直接可编辑的工作记忆，少量高价值事实/偏好/规则
  - Recall Memory (conversation history): 对话历史索引检索，时间/主题/实体多维召回
  - Archival Memory (vector store): 外部向量存储，语义检索，大规模长期知识
- **Graph-native 趋势**: Cognee (Rust edge engine、auto-extracted ontologies、70+ 企业采用、1M+ pipelines/月) 在企业级获青睐；Mem0 适合个性化助手；Letta 适合长生命周期自主 agent
- **Write-Path > Read-Only RAG**: 图记忆生态成熟，实体关系检索超越向量相似度
- **记忆生命周期三步曲**: Extract→Update→Delete 缺一不可；陈旧记忆毒性 > 无记忆

### Suggested Action
- 确认当前三层架构已落地 (Hermes memory tool + Obsidian vault + MEMORY.md)
- 评估 Cognee Graph-native 记忆集成替代/增强现有 Archival 层
- 强化 Update/Delete 机制：定期清理陈旧/矛盾记忆

### Metadata
- Source: tavily_search (Mem0/Cognee/Zep/Letta 2026 状态报告、Techment 架构指南)
- Tags: memory-architecture, three-tier, graph-native, cognee, memory-lifecycle
- Pattern-Key: memory.three-tier-standardized-2026
- Recurrence-Count: 1
- First-Seen: 2026-10-20
- Last-Seen: 2026-10-20

---

## [LRN-20261020-010] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: high
**Status**: open
**Area**: operations

### Summary
任务感知模型路由待落地：cron/heartbeat 分流 cheap tier (qwen3.7-plus/glm-5.2)

### Details
- **现状**: 所有任务统一走 deepseek-v4-pro fallback 链，无任务类型感知
- **目标架构**:
  - Frontier (deepseek-v4-pro/kimi-k2.6): 复杂推理、规划、代码生成、学术写作
  - Mid-tier (qwen3.7-plus/glm-5.2): cron/heartbeat/低复杂度检索/格式化/监控
  - SLM/本地: 极高频/极低延迟/离线场景
- **预期收益**: 成本降 60-70%，配额压力缓解 80%+，延迟降低
- **阻塞**: 需在 openclaw.json / agent 配置中实现 task-aware routing

### Suggested Action
- 在 openclaw.json agents.defaults.model 中增加 task_type 字段路由规则
- cron/heartbeat jobs 显式指定 model: qwen3.7-plus 或 glm-5.2
- 验证 cheap tier 模型对低复杂度任务的完成质量
- 落地后更新 TOOLS.md 模型架构章节

### Metadata
- Source: LRN-20260722-001 (Plan-and-Execute) + 2026 运营成熟度报告 + 实测配额危机
- Tags: task-aware-routing, cheap-tier, cost-optimization, model-tiering
- Pattern-Key: operations.task-aware-model-routing-pending
- Recurrence-Count: 4
- First-Seen: 2026-07-22
- Last-Seen: 2026-10-20

---

## [LRN-20261020-011] insight

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: medium
**Status**: completed
**Area**: infra

### Summary
daily-summary cron 产出路径验证：memory/2026/MM/ 为有效存储位置

### Details
- **发现**: daily-summary cron 产出实际写入 `memory/2026/10/` 子目录而非根目录 `memory/`
- **根因**: 脚本路径配置指向 dated 子目录，但健康检查/回顾脚本仍查找根目录
- **影响**: 导致 "daily-summary cron 产出缺失 19+ 天" 误判 (LRN-20261014-003)
- **修正**: 路径判定已修正，健康检查需同时审视 `memory/2026/MM/` 子目录

### Suggested Action
- 统一 daily-summary 产出路径或更新所有消费脚本的查找逻辑
- 建议：根目录 `memory/YYYY-MM-DD.md` 保留每日汇总，子目录 `memory/2026/MM/` 存详细日志
- 更新 cron_health.py、open-actions-broadcast 等消费脚本

### Metadata
- Source: daily-self-improvement cron 10-17 回顾确认
- Tags: daily-summary, path-verification, cron-output, memory-structure
- Pattern-Key: infra.daily-summary-cron-path-verification
- Recurrence-Count: 3
- First-Seen: 2026-10-17
- Last-Seen: 2026-10-20

---

## [LRN-20261020-012] best_practice

**Logged**: 2026-10-20T14:53:00+08:00
**Priority**: medium
**Status**: proposed
**Area**: security

### Summary
Secret egress host binding 评估: openclaw.json 显式配置密钥出口白名单

### Details
- **安全基线要求** (v2026.9.x / NIST/IMDA 标准化进程): 显式配置密钥可出口的域名白名单
- **现状**: 未在 openclaw.json 配置 `secretEgressHosts` / `files.urlAllowlist` 白名单
- **风险**: 凭证/密钥可能被恶意工具/提示词注入泄露至任意外部域名
- **实施**: 在 openclaw.json 增加 `secretEgressHosts: ["api.openai.com", "api.tavily.ai", "api.exa.ai", "api.firecrawl.dev", ...]`

### Suggested Action
- 审计当前所有外部调用域名，建立白名单清单
- 在 openclaw.json 配置 secretEgressHosts / files.urlAllowlist
- 启用后验证不影响正常功能 (搜索、模型、消息通道)
- 纳入安全审计 cron 定期复核

### Metadata
- Source: OpenClaw v2026.9.x 安全架构 + NIST/IMDA 标准化进程
- Tags: secret-egress, host-binding, allowlist, security-baseline, nist-compliance
- Pattern-Key: security.secret-egress-host-binding
- Recurrence-Count: 3
- First-Seen: 2026-10-17
- Last-Seen: 2026-10-20