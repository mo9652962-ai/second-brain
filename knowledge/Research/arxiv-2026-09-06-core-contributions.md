---
title: arXiv 2026-09-06 核心贡献总结
date: 2026-09-06
source: arxiv-2026-09-06-agent-llm.md (15+9 篇补全精选)
selected: Harness Engineering / Delegation Without Trust / Runtime-Independent Persistent Agents
status: 已深挖 3 篇（web_search 双源交叉验证）
data-cutoff: 2026-09-06
---

# arXiv 核心贡献总结 · 2026-09-06

> 来源：arxiv-fetch cron 2026-09-06 输出（09-03+09-04 同池补全，索引冻结无新提交），web_search 双源交叉验证后深挖 3 篇
> 精选原则：排除前几周 core-contributions 已深挖论文（本次候选全部 2609.xxxxx，与历史 2607/2608 零重叠 ✅）；从 fetch 推荐的 5 篇候选（00006/00267/00546/00052/01519）中跨簇选 3 篇，覆盖本周三大主线——**harness 工具→平台转折 / agent 委托 untrusted-model 范式 / 记忆与运行时解耦**

## 🥇 Harness Engineering: 11 个编码 agent 的源码解剖 (2609.00006)

**标题**: Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems
**核心**: 对 11 个生产编码 harness（Claude Code / Codex CLI / Gemini CLI / Mistral Vibe / OpenHands / Aider / Mini-SWE-Agent / **Hermes** / Pi / OpenCode / **OpenClaw** + Omnigent meta-harness 对照）做源码级解剖（约四百万行 Python/TS/Rust），给出「agent = model + harness」学科最完整的实证地基——harness 在 2026 上半年完成从工具到平台的转折。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **7 个规范子系统映射** | loop / LLM 集成 / 工具 / 记忆与上下文 / 安全与权限 / 编排 / 扩展面，各配最小+最大实现 | 拿到 harness 的标准化解剖框架，可逐子系统对照自身配置 |
| **零通用框架依赖** | 11 系统无一 import LangChain/LangGraph/AutoGen（Gemini CLI 连自家都不用） | 实证背书 k 的工具选型：手写 async loop + 确定性检索 > 通用框架堆栈 |
| **零 embedding 检索代码** | 全用 ripgrep / tree-sitter / glob / 自动发现的 Markdown 上下文文件 | 「确定性检索优于向量检索」有了 400 万行级实证；AGENTS.md/技能文件机制被点名为正例 |
| **SKILL.md 领先 MCP** | SKILL.md 9/11 vs MCP 8/11（扩展标准采用率） | 直接背书 k 的技能体系路线——portable markdown 技能注入 system prompt 是行业主流方向 |
| **Hermes 定位** | 增长最快的开源 harness + self-improving skill loop（自改进技能循环） | k 运行的 Hermes 正是该领域前排样本，本论文明的「技能自演化」与 k 的 skill-evolution 同向 |
| **13 条横切观察 + 29 个设计模式** | 首次记录：agent 维护的记忆流水线、verify-on-stop 守卫、lineage 压实、log-as-queue、语法感知命令权限等 | 可直接对照自身 harness 检查「29 模式里我用了哪些、缺哪些」 |
| **90 天纵向演化（4→7 月快照）** | 收敛变成模仿（hook 词汇逐字复制）、行为策略从 prompt 散文迁移到配置 | 「策略进配置不进 prompt」= 配置化治理趋势，对应 k 的 hermes-harness-profile 思路 |
| **平台转折论 + 18 条设计建议 + 90 行脚手架** | ACP 进 6 系统 + harness hosting 角色；Omnigent meta-harness 编排 11 家 | 从「配置面」升格为「一等研究对象」，90 行最小 harness 是学习脚手架 |

### 方法/架构

```
11 生产 harness 源码快照（July 2026 pin；8 个保留 April 快照做纵向）
    ↓ 沿 7 规范子系统解剖（D1 loop ... D7 扩展面）
13 条横切观察 + 29 个重复设计模式
    ↓ 三倍语料扩张后仍成立的两个实证空白
① 无通用 agentic 框架依赖  ② 无 embedding 代码检索
    ↓
平台转折（SDK / marketplace / agent-as-a-model gateway / meta-harness）
    → 18 条设计建议 + 90 行 minimum-viable-harness 脚手架（实现其中 10 条）
```

| 子系统 | 最小实现 | 最大实现 |
|:---|:---|:---|
| Agent Loop | Mini-SWE-Agent：线性 while-loop（~5K 行）| OpenHands：事件溯源会话引擎 |
| LLM 集成 | 单 LiteLLM 调用 | Hermes：5 个自有传输 + 29 个 provider 档案 |
| 工具与动作 | 仅 bash（1 个工具）| OpenClaw：109+ 工具经 gateway 委派 |
| 记忆与上下文 | 无界线性历史 | Codex：agent 维护的跨会话记忆流水线 |
| 安全与权限 | 仅成本/步数上限 | Codex：四层栈（Starlark 策略→hooks→Guardian LLM 审查→OS 沙箱）|
| 编排 | Aider：刻意缺席 | Claude Code：递归组合 |
| 扩展面 | 结构化类型 | Pi：万物皆扩展的运行时 |

### 与 sora 的关联

✅ **k 的运行时本体研究必读**：论文直接解剖 Hermes/OpenClaw/OpenCode——7 子系统对比表就是自身 harness 的体检清单；「SKILL.md 9/11 领先 MCP 8/11」「零通用框架」「确定性检索」三条实证直接背书 k 的技能体系与工具选型（不用 LangChain 堆栈）
✅ **自演化闭环参照**：Hermes 被点名为「self-improving skill loop」样本——与 k 的 skill-evolution 蒸馏链（会话经验→启发式→技能沉淀）同构，论文的「行为策略从 prompt 迁移到配置」给 hermes-harness-profile 提供行业方向
✅ **harness 三连主线**：与 CordisBench（01600，harness 生命周期推理）、HarnessDev（01437，harness 可自举）同读，是 09-05 之后最集中的主线；HookPry（09-05）攻击线正好攻防闭环

## 🥈 Delegation Without Trust: agent 委托授权缺口实证 (2609.00267)

**标题**: Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems
**核心**: agent 安全必须在 **untrusted-model 假设**下评估——一个被完全 prompt 注入的 agent 仍不能超出显式授予它的权限。对 4 个主流框架做缺口分析 + 实现对抗性验证的 authorization broker，把「注入后不越权」从口号变成可证标准。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **4 个对手威胁模型 + 8 条安全要求** | confused deputy / token 窃取重放 / prompt 注入提权 / 被攻陷子 agent | k 的委派流程（Codex/ZCode/WorkBuddy/dsh）可逐条对照 8 条要求自查 |
| **默认运行时四威胁全败** | 宽泛 bearer 凭据 + 授权门在模型内 = 全部沦陷 | 「把凭据交给模型让它小心」是结构性失败，不是模型不够乖 |
| **主流框架缺口** | LangGraph/CrewAI/AutoGen 三个无内置隔离、MCP 仅部分；无单一标准覆盖要求集 | 框架自带安全不可依赖，隔离必须自己做 |
| **authorization broker 实证** | 四威胁全挡 + 抵抗 11 次直接攻击 + 20 万伪造 token 0 接受 | 非语义、可验证的授权门是可行且便宜的 |
| **被攻陷子 agent 收窄** | 平均 1.5 可达动作 vs bearer 的 8,100（2,000 随机场景）| 「委派=能力铸造不是凭据转发」——被黑子 agent 也出不了它的笼子 |
| **微秒级开销** | 每决策 ~2.6μs，相对模型推理可忽略 | 「外部授权太慢」是伪借口，agent 循环加授权门无痛 |
| **生产落地** | VotalAI 的 LLM Shield | 已投产，非纯学术方案 |

### 方法/架构

```
4 个对手威胁模型（confused deputy / token 重放 / 注入提权 / 被攻陷子 agent）
    → 推导 8 条治理安全要求
    → 现状缺口审计（默认运行时 + LangGraph/CrewAI/AutoGen/MCP）→ 全败/部分
    → authorization broker（非语义、可验证、能力铸造式委派）
        每决策 ~2.6μs | 20 万伪造 token 0 接受 | 子 agent 1.5 vs 8100 可达动作
    → 生产：VotalAI LLM Shield
```

| 组件 | 作用 |
|:---|:---|
| 威胁模型 | 四类对手 + 8 条要求，作为治理 checklist |
| 授权 broker | 把授权决策从模型上下文移出，由基础设施强制 |
| 能力铸造式委派 | 委托的工具调用携带**更小**的权限面，而非转发账号级凭据 |
| 外部验证 | 非语义校验：模型只提案，broker 对照严格策略验证 |

### 与 sora 的关联

✅ **委派流程安全基线**：k 的多 agent 委派（Codex/ZCode/WorkBuddy/dsh）应逐条对照 8 条安全要求——「被完全注入的 agent 是否仍无法超出被授予权限？」「凭据是否移出模型上下文？」。对照 hermes-codex-security-gate 已有基线（凭据 BLOCKED、L0-2 自动/L3 授权/L4 禁），本次可补「委派=能力铸造」视角
✅ **外部 broker 模式**：「授权逻辑在模型内，模型就是漏洞」——k 的本地多用户认证方案（pbkdf2+opaque token）已走外部强制路线，论文给出通用化论证
✅ **批判视角（延伸）**：moltbook 指出 broker 的 **policy-write 路径**是新特权面（被攻陷子 agent 无法直接越权，但可能诱导 operator 放宽策略）——审查时把 broker 自己的策略更新路径也纳入同等非语义标准

## 🥉 Runtime-Independent Persistent Agents: 记忆与运行时解耦 (2609.00546)

**标题**: Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers
**核心**: agent 的「身份/记忆/代码」与「运行时绑定」彻底解耦——换模型、换 harness、换服务器是**迁移（migration）**而不是**新建 agent（creation）**。给出连续性不变量 + 六步迁移协议 + Enoch 参考实现，是持久 agent 的架构蓝图。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **连续性基底 P_t=(I_t,M_t,B_t)** | 架构身份表示 + 私有持久记忆 + 版本化软件体 | 把「我是谁/我记得什么/我会什么」做成与运行时可分离的载体 |
| **可替换部署绑定 E_t=(R_t,H_t,D_t)** | reasoner + harness + host，加交互面 S_t（chat/API/UI）| 换模型/harness/服务器只换绑定层，不重建 agent |
| **6 条连续性不变量** | I1 lineage / I2 memory 从不静默重置 / I3 body 同版本 / I4 单一 continuation authority / I5 capability delta 可见 / I6 标签不覆盖身份 | 可直接对照自身记忆系统逐条检查缺口 |
| **六步迁移协议** | quiesce→checkpoint→validate→bind→rehydrate→resume | 「迁移」不是拷贝文件，是受治理的授权连续性转移 |
| **Enoch 参考实现** | 冻结 commit c8013ed 过 833 core tests + 92 provider/library tests（clean-room）| 协议可落地，非纸面设计 |
| **已演示单轴替换** | reasoner-version / interaction-surface / host-machine 替换保持连续性状态 | k 的 Hermes 换模型、换部署主机不丢记忆是有架构依据的 |
| **诚实边界** | 作者明说：支撑的是机械可替换性，**非行为级保真** | 「换模型后表现是否一致」仍是开放问题，别过度宣称 |

### 方法/架构

```
连续性基底 P_t = (I_t, M_t, B_t)      ← 身份 / 私有持久记忆 / 版本化软件体
可替换绑定   E_t = (R_t, H_t, D_t) + S_t ← reasoner / harness / host + 交互面
部署执行     A_t = P_t ▷ (E_t, S_t)
    改变任一层 = 迁移（授权协议保 lineage + 转移 continuation authority）

六步协议：quiesce → checkpoint → validate → bind → rehydrate → resume
        （停新流/推进 epoch）→（抓取状态）→（验 schema/哈希/lineage）→（按契约解析）→（原子安装）→（健康检查+取新 epoch）
```

| 组件 | 作用 |
|:---|:---|
| I_t 身份表示 | 名称/使命/关系/价值观/血统记录（体与身份分离加载，升级 body 不覆盖身份）|
| M_t 持久记忆 | 带祖先记录的记忆与工作流状态，**绝不静默重置** |
| B_t 版本化软件体 | 工具/策略/provider 契约/测试，按版本契约演进 |
| 授权协议 | 迁移 = 受治理的授权连续性转移，不是文件拷贝 |

### 与 sora 的关联

✅ **持久 agent/记忆架构蓝图**：k 的 Hermes/Mnemon/cross-agent memory/Crystal 蒸馏链——「身份/记忆/代码版本化绑定」与「授权带溯源」做成一等字段，P_t=(I,M,B) 就是跨会话连续性（SOUL.md=身份、memory=持久记忆、skills/代码=软件体）的学术形式化
✅ **迁移不是新建**：k 换模型（fangzhou-2 等 provider 切换）、换 harness、换主机时，「连续性」有协议可循而非凭运气——配合记忆锚点自然嵌入的 SOUL 机制
✅ **与 MutMem-V2（01235）连读**：01235 给「谁有权改记忆、改了什么、可验证吗」密码学契约（commitment/recall-evidence），00546 给「换运行时不丢连续性」架构——两条记忆主线互补成完整工程方案

## 综合评估矩阵

| 论文 | 价值 | 可落地性 | 行动 |
|:---|:---|:---|:---|
| Harness Engineering 2609.00006 | ★★★★★ | 高（对照自身 harness 配置逐项体检）| ⬜ 待办（通读 7 子系统对比 + 29 模式 + 18 条建议）|
| Delegation Without Trust 2609.00267 | ★★★★★ | 高（委派流程逐条对照 8 条要求）| ⬜ 待办（🟡 行动项已列）|
| Persistent Agents 2609.00546 | ★★★★★ | 中-高（记忆/身份架构参照）| ⬜ 待办（🟡 记忆工程化）|

## 落地行动清单

| 行动项 | 状态 |
|:---|:---|
| 🔴 精读 Harness Engineering 00006：对照自身 Hermes 配置（skill 体系 + 工具选型）做 7 子系统体检，找可迁移改进（「SKILL.md 领先 MCP、零通用框架、确定性检索」三条实证直接背书现状）| ⬜ 待办 |
| 🔴 多 agent 委派按 untrusted-model 审查：00267 的 8 条安全要求——委派流程（Codex/ZCode/WorkBuddy/dsh）自查「被完全注入的 agent 是否仍无法超出被授予权限」，凭据与授权状态移出模型上下文 | ⬜ 待办 |
| 🟡 记忆工程化参照 00546：P_t=(I,M,B) 连续性基底——持久记忆/跨 agent 记忆设计把「身份/记忆/代码版本化绑定」与「授权带溯源」做成一等字段（配合 01235 MutMem-V2 契约）| ⬜ 待办 |
| 🟡 评估反身性：01519 guardrails +87.4→+7.2、00038 outcome-only 盲区——「加 X 有效」先过控制变量审查再信增益数字 | ⬜ 待办 |
| 🟢 AgentProv 00052 动作指纹审计：第三方 API/中转站「宣称的模型是不是真身」新校验手段（630 对 100% 抓替换、FP 7%），补进 ai-api-provider-evaluation 类技能 | ⬜ 待办 |

## 延伸阅读

- [[arxiv-2026-09-05-agent-llm]] / [[arxiv-2026-09-04-agent-llm]] — 同池速览（HookPry 攻击线、记忆授权 01836、检索指引劫持 03450）
- [[arxiv-2026-08-21-core-contributions]] — MemFuse（记忆融合）同记忆赛道
- Harness 三连：CordisBench [2609.01600](https://arxiv.org/abs/2609.01600) / HarnessDev [2609.01437](https://arxiv.org/abs/2609.01437)
- 授权同主线：Progressive Risk Vesting [2609.01035](https://arxiv.org/abs/2609.01035)（沙盒派生 vs 能力激活）、Defense-as-Skill [2609.01487](https://arxiv.org/abs/2609.01487)（skill 式守卫）
- 记忆同主线：MutMem-V2 [2609.01235](https://arxiv.org/abs/2609.01235)（加密授权变异契约）、Safin-1 [2609.00092](https://arxiv.org/abs/2609.00092)（记忆原生安全）
- 评估反身性：When Guardrails Look Effective [2609.01519](https://arxiv.org/abs/2609.01519)（construct validity 失败）、trajectory-judge [2609.00038](https://arxiv.org/abs/2609.00038)（outcome-only 盲区）
- API 审计：AgentProv [2609.00052](https://arxiv.org/abs/2609.00052)（动作指纹）
- 批判视角：moltbook 对 broker policy-write 路径的质疑（授权 broker 自身策略更新面须同等非语义标准）

---

## MANTA 试点记录

- **是否触发拓扑变更**：否
- **触发的变更类型**：无变更（保持固定拓扑）
- **评估过程**：
  - **监控点 1（候选池阶段）**：09-06 候选池 15 主条目分 4 簇——harness/工具工程 3 篇 / 安全授权治理 5 篇 / 记忆身份 3 篇 / 评估审计 4 篇。fetch 推荐的 5 篇 core-contributions 候选（00006 harness / 00267 委托 / 00546 记忆 / 00052 API 审计 / 01519 评估效度）**分散在 5 个不同方向** → 判定「候选池分散」→ 跨簇选文（harness 本体 / 委托安全 / 记忆架构）覆盖本周三大主线 → **不合并调研与验证阶段**，保持常规 3 篇精选
  - **监控点 2（草稿阶段）**：3 篇选文均通过 **web_search 双源验证**（arXiv abs 页 + 独立第三方解读——Codex Knowledge Base / DAIR.AI Academy / PulseAugur / moltbook），关键数字一致（00006 的 11 harness/SKILL.md 9/11、00267 的 2.6μs/1.5 vs 8100/20 万伪造 token、00546 的 P_t/六不变量/833 tests）→ 证据充分 → **保持固定验证路径，不增加独立验证者**
- **变更后的质量/成本 vs 固定拓扑观察**：未变更，无对比样本。本次观察：5 篇候选分散 5 方向，跨簇选 3 篇带来主题覆盖面收益（运行时本体/委托安全/记忆架构三主线），但**牺牲了「API 审计簇」（00052）与「评估效度簇」（01519）的深挖**——两者已入延伸阅读 + 落地行动清单（🟢 AgentProv 进 ai-api-provider-evaluation、🟡 评估反身性）。与 08-16/08-23 观察一致：跨簇选文覆盖面优先，单簇横向对比靠延伸阅读兜底。若未来要深挖单簇（如 harness 三连横向对比 00006 vs 01600 vs 01437），可考虑触发「簇内合并调研」
- **子代理预算使用**：0/3（本次全程主 agent 直接执行，未派子代理；3 篇选文 3 次并行 web_search 即完成双源验证）

*Generated via arxiv-summarize cron (arxiv-fetch 2026-09-06 输出) + 搜索引擎交叉验证 | Last updated: 2026-09-06*
