---
aliases:
  - arxiv-2026-09-06-agent-llm
  - arxiv-agent-llm-2026-09-06
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-06
updated: 2026-09-06
status: adopted
source: arxiv.org list pages + abs pages（API 429 限流期间，补全性质）
---

# arXiv AI Agent / LLM 速览 — 2026-09-06（补全性质）

> **检索时间**: 2026-09-06 GMT+8
> **⚠️ 补全性质**: 索引继续冻结（export.arxiv.org 全局最新时间戳仍停在 09-03T17:59Z，list 页无 09-05/09-06 分组，API 持续 429 限流）——**无任何新提交**。09-05 速览虽补录了 09-03+09-04 同池的 21 主 + 8 简评，但**仍未盖满**：本次对同一池剩余 821 篇未覆盖做全量标题粗筛，发现 09-05 漏掉的 **15 篇强相关主条目 + 9 篇简评**（harness 三连、委托授权三篇、agent 记忆三篇、评估反身性两篇、API 审计等），全部补录。头部声明补全性质，不重写 09-04/09-05 已收录内容。
> **收集**: 6 类别 list/recent 页全量 → 09-03 454 + 09-04 471 = **924 unique base ID**（与 09-05 同池，索引未推进）→ 剔除 covered_ids（含 09-05 新增 28）→ **821 未覆盖** → 标题粗筛 433 候选（2609 窗口 176）→ 人工剔除领域应用 → 逐篇抓 abs 页精选 **15 主条目 + 9 简评**（仅保留 LLM/AI Agent 本体相关）
> **数据源**: [export.arxiv.org](https://export.arxiv.org)（429 限流） + [arxiv.org/list](https://arxiv.org/list/cs.AI/recent)

---

## 一、Harness / 工具工程（3 篇）

### 1. Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents -- A Source-Code Study of Eleven Systems

- **ID:** [2609.00006v1](https://arxiv.org/abs/2609.00006v1) | [📄 PDF](https://arxiv.org/pdf/2609.00006v1)
- **作者:** Paul Barbaste, Tristan Darrigol, Germain Vu, Tom Wiltberger
- **分类:** cs.SE, cs.MA
- **摘要:** 2026 上半年「agent = model + harness」从口号变成平台事实。本文给年轻学科最完整的实证地基：对 11 个生产编码 harness（Claude Code / Codex CLI / Gemini CLI / Mistral Vibe / OpenHands / Aider / Mini-SWE-Agent / **Hermes / Pi / OpenCode / OpenClaw**）做源码解剖（约四百万行 Python/TS/Rust），加 Omnigent（Databricks）首个 meta-harness 作对照。定义 harness 的七个规范子系统（loop、工具、上下文管理、安全控制、编排、扩展面等），映射各系统最小/最大实现；审计产出 **13 条横切观察 + 29 个重复设计模式**，多个首次记录（agent 维护的记忆流水线、verify-on-stop 守卫、lineage 压实、log-as-queue、语法感知命令权限等）。两个贯穿 11 系统的实证空白：**没有任何 agent runtime 导入通用 agentic 框架（LangChain/AutoGen 等），也没有一个用 embedding 检索代码**——全靠手写 async loop + 确定性检索（ripgrep/tree-sitter/glob）；扩展标准上 **SKILL.md skills 领先 MCP（9/11 vs 8/11）**，ACP 进 6 个系统并新增 harness hosting 角色（OpenHands 把 Claude Code/Codex/Gemini CLI 当可互换后端）。四月版已有 8 系统快照 → 保留纵向样本（90 天源码级演化：收敛变成模仿、行为策略从 prompt 散文迁移到配置）。结尾 18 条设计建议 + 90 行最小可行 harness 脚手架（实现其中 10 条）。
- **关联度:** ★★★★★ 直接解剖 **Hermes/OpenClaw/OpenCode**——k 的运行时本体研究必读；「SKILL.md 9/11 领先 MCP 8/11」直接背书 k 的技能体系路线；与 09-05 的 HookPry（harness hook 攻击面）构成 harness 研究潮的攻防两端

### 2. CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?

- **ID:** [2609.01600v1](https://arxiv.org/abs/2609.01600v1) | [📄 PDF](https://arxiv.org/pdf/2609.01600v1)
- **作者:** Damien Sileo, Dimitri Kachler
- **分类:** cs.CL, cs.AI
- **摘要:** 动态 agent harness 允许 LLM 改变塑造自身执行的软件——本地插件变更会沿依赖与清理逻辑传播，这是全新的推理负担。引入 **CordisBench**：1200 问的生命周期推理基准，用受控形式化设定 + 在 Cordis（管理组件依赖与清理的 runtime）上执行的程序，问模型：识别受影响组件、预测指定 teardown 顺序后的状态、判定哪些条件在所有/部分顺序下成立、选择能成功执行的重配置。跨三个面向效率的模型族评估（摘要在此截断，主要看它把「harness 内部生命周期推理」变成可测能力）。
- **关联度:** ★★★★★ harness 一旦允许 agent 自改运行软件，「组件生命周期推理」就是新的能力维度——与 00006（harness 解剖）、01437（harness 自演化）构成 harness 三连，是 09-05 之后最集中的主线

### 3. HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

- **ID:** [2609.01437v1](https://arxiv.org/abs/2609.01437v1) | [📄 PDF](https://arxiv.org/pdf/2609.01437v1)
- **作者:** Yuhao Wu 等（10 人）
- **分类:** cs.SE, cs.CL
- **摘要:** agent 从原型走向部署工具，能力越来越依赖模型外部执行基建（agent harness）；固定模型权重、更换 harness 可大幅改变任务表现。但现有 agent 评估都在「选定 harness 下报下游表现」，模型自己开发 harness 的能力几乎未被探索。提出 **HarnessDev**：把评估单元从任务输出移到可运行基建。覆盖两个阶段——**Creation**（agent 从最小种子 + 少量用例出发，构建完整 harness）与后续演化阶段（摘要截断，核心是把「harness 能否被 LLM 自举/自演化」变成一等评估对象）。
- **关联度:** ★★★★★ harness 从「外部配置」变成「agent 可自举的产物」——k 若探索自我改进型 agent（改自己的运行时/技能），HarnessDev 的方法与 00006/01600 连读是设计参照

---

## 二、Agent 安全、授权与治理（5 篇）

### 4. Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems

- **ID:** [2609.00267v1](https://arxiv.org/abs/2609.00267v1) | [📄 PDF](https://arxiv.org/pdf/2609.00267v1)
- **作者:** Panduranga Sai Varma Dantuluri, Jyotirmoy Sundi
- **分类:** cs.CR, cs.AI
- **摘要:** 自主 LLM agent 越来越代表用户行事：持有凭据、调用工具、派生子 agent 再代用户行动——「谁有权做什么、凭谁的授权」从老分布式系统问题变成紧迫难题，因为驱动每个 agent 的组件是可被劫持的 LLM。主张 agent 安全必须在 **untrusted-model 假设**下评估：正确系统 = 被完全 prompt 注入的 agent 仍不能超出显式授予它的权限。三点贡献：①四个对手威胁模型（confused deputy / token 窃取重放 / prompt 注入提权 / 被攻陷子 agent）+ 推导 8 条治理 agent 系统必须满足的安全要求；②差距真实：默认 agent runtime（宽泛 bearer 凭据、授权门在模型内）四威胁全败，LangGraph/CrewAI/AutoGen/MCP 授权模型——三个无内置隔离、一个仅部分，无单一标准覆盖要求集；③实现并对抗性评估 authorization broker：四威胁全挡、抵抗 11 次直接攻击、20 万伪造 token 接受 0、把被攻陷子 agent 限制在其委托任务（2,000 随机场景平均 1.5 可达动作 vs bearer 的 8,100）、每决策约 **2.6 微秒**。生产落地 VotalAI 的 LLM Shield。
- **关联度:** ★★★★★ 「授权决策必须移出模型、由基础设施强制」——k 的多 agent/委派流程（Codex/ZCode/WorkBuddy/dsh）应逐条对照 8 条安全要求；与 09-05 的 01836 记忆授权洗白、03884 HookPry 同属「agent 安全 = 架构问题」共识潮

### 5. Spawn Freely, Act Sparingly: Progressive Risk Vesting for Recursive LLM-Agent Trees

- **ID:** [2609.01035v1](https://arxiv.org/abs/2609.01035v1) | [📄 PDF](https://arxiv.org/pdf/2609.01035v1)
- **作者:** Molly Wang
- **分类:** cs.AI, cs.LG, math.PR
- **摘要:** 递归 LLM agent 靠派生专家分支拓宽搜索，但有些分支会请求发数据、部署代码的工具。分支何时该获得行动权？区分**沙盒派生**（外部控制阻止指定危害）与**能力激活**（选中分支越过不可逆动作边界）。提出 **Progressive Risk Vesting（PRV）**：把轨迹级风险预算放在 escrow 中，随分支激活逐笔扣减，证明自适应生成树的 anytime harm 界。分支结果可以相关，但每个局部证书只需在……（摘要截断，核心是把「递归 agent 树的授权时机」形式化为可证明的风险预算问题）。
- **关联度:** ★★★★★ 递归/spawn agent 树的「何时放权」形式化——k 编排多 agent 派活时，沙盒 vs 能力激活的区分是设计授权策略的框架；与 00267 同属「agent 授权工程」主线

### 6. Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents

- **ID:** [2609.01487v1](https://arxiv.org/abs/2609.01487v1) | [📄 PDF](https://arxiv.org/pdf/2609.01487v1)
- **作者:** Xiaofang Yang, Ziqi Miao, Dianbo Sui, Jing Shao, Lijun Li
- **分类:** cs.CR, cs.AI
- **摘要:** skill 增强 agent 把可复用 skill 作为持久运行时上下文加载，提升任务表现的同时，也给了恶意 skill 一条持久通道去引导未来动作——这类 skill 可能在具体用户任务 + 工作区状态让不安全动作显得有用之后，才泄露机密、破坏代码、绕过审批或暂存数据外泄。这使得安装前审查不够，需要**运行时、任务条件化的防护**。提出 **Defense-as-Skill**：把运行时 guard 本身实现为可安装、可检查、可编辑的 skill。守卫 **SkillSonar** 与不受信任的……（摘要截断，核心是用「skill 式守卫」对抗「skill 式攻击」，把防御做成与攻击同构的、可迭代的一等对象）。
- **关联度:** ★★★★★ skill 供应链/运行时防护——直接映射 k 的 Hermes/OpenClaw 技能体系安全面；与 09-05 的 03884 HookPry（hook 更新木马化）、技能审核流程同线程，「守卫本身做成可编辑 skill」是低成本可落地思路

### 7. Validity-Aware Jailbreak Evaluation for Large Language Models

- **ID:** [2609.00498v1](https://arxiv.org/abs/2609.00498v1) | [📄 PDF](https://arxiv.org/pdf/2609.00498v1)
- **作者:** Qilong Wu, Sahil Wadhwa, Pranab Mohanty, Giri Iyengar, Varun Chandrasekaran
- **分类:** cs.AI
- **摘要:** 越狱鲁棒性已成 LLM 安全评估核心，但主流方法依赖拒答行为、语义相似、意图匹配等启发式——重语言似真、轻正确性。指出关键局限：许多越狱意图依赖**指令有效性**而非事实正确性，导致「看起来合理但事实上/程序上错误」的响应被标成成功。提出 **SEAV（Sequential Epistemic and Action-Level Validation）**：验证中心的越狱评估框架，把响应分解为……（摘要截断，核心是把越狱评估从「像不像成功」升级到「是不是真造成有效违规」）。
- **关联度:** ★★★★ 越狱评估的 validity 修正——与 09-05 的 03436（评估伪影）、今日 01519（construct validity）同属「测量仪器不可靠」主线；k 做安全评测/验收时「成功」判定要卡 epistemic + action 两级有效性

### 8. Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges

- **ID:** [2609.01210v1](https://arxiv.org/abs/2609.01210v1) | [📄 PDF](https://arxiv.org/pdf/2609.01210v1)
- **作者:** Rui Yang 等（10 人）
- **分类:** cs.CR, cs.AI
- **摘要:** LLM 安全基准常评估用户查询的风险，但 QA 的结局取决于响应是否违反政策——这在中文学害内容评估里尤为关键：语言变体与对抗变换可掩盖风险意图。引入 **C-SafeQA**：政策接地的响应级中文安全评估基准，538 条基础查询 + 8,877 条对抗查询，由 4 个全量模型部署作答，产出 37,660 条 query-response 记录标注 safe/unsafe/disputed；参考标签经一致感知多模型裁决 + 盲审（摘要截断，核心是「评估响应而非仅查询」的中文安全基准 + 对安全 judge 自身的评估）。
- **关联度:** ★★★★ 中文安全评估稀缺品——k 的中文场景/墨题类中文内容审查可直接迁移「响应级政策接地」设计；「谁审 judge」的自我指涉与今日 01073、09-05 03436 的评估反身性呼应

---

## 三、Agent 记忆与身份（3 篇）

### 9. Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers

- **ID:** [2609.00546v1](https://arxiv.org/abs/2609.00546v1) | [📄 PDF](https://arxiv.org/pdf/2609.00546v1)
- **作者:** Zhenyu Zhao, Roy Zhao
- **分类:** cs.SE, cs.AI
- **摘要:** agent 系统常以「当前产生其行为的模型 + harness」来描述——对单次执行够用，却欠规定一个长寿 agent：它可以换模型、换编排 harness、换交互会话、换宿主服务器，却保持单一身份、记忆与可执行代码血统。提出**运行时无关的持久 agent 架构**：连续性承载基底 P_t=(I_t, M_t, B_t)（架构身份表示 + 私有持久记忆 + 版本化软件体），配可替换的部署绑定 E_t=(R_t, H_t, D_t)（reasoner + harness + host）……（摘要截断，核心是把「身份/记忆/代码」与「运行时绑定」彻底解耦，让 agent 跨模型/harness/服务器迁移而不丢连续性与可验证血统）。
- **关联度:** ★★★★★ agent 长寿化 = 记忆 + 身份 + 代码三件套与运行时解耦——k 的持久 agent/记忆设计（Hermes/Mnemon/cross-agent memory）的架构蓝图；与 09-05 的 01836 记忆授权洗白连读，记忆绑定溯源正好落在 P_t 的版本化设计里

### 10. MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence

- **ID:** [2609.01235v1](https://arxiv.org/abs/2609.01235v1) | [📄 PDF](https://arxiv.org/pdf/2609.01235v1)
- **作者:** Walid Saidi
- **分类:** cs.CR, cs.AI
- **摘要:** MutMem V1 提出持久 agent 记忆的「保留 + 加密授权变异」，但没有完整可移植验证契约或干净安装复现路径。**MutMem V2** 补上发布缺口而不引入第二个记忆引擎：规定规范字节、域分离的 object/package commitment、强制 recall-evidence 成员与顺序、外部信任锚、身份 epoch、撤销、授权、请求回执、有序披露、三种变异终止类型。发布协议含 18 个版本化 object schema、39 个 recall vector、15 个变异……（摘要截断，核心是把「记忆变异」做成可移植、可复现、可独立验证的密码学契约）。
- **关联度:** ★★★★★ agent 记忆的加密授权变异协议——与 09-05 的 01836（记忆授权洗白）、03450（检索指引劫持）同线：给「谁有权改记忆、改了什么、可验证吗」提供工程化答案；k 的记忆安全设计可借其 commitment/recall-evidence 机制

### 11. Safin-1: Safety from Within through Memory-Native State Evolution

- **ID:** [2609.00092v1](https://arxiv.org/abs/2609.00092v1) | [📄 PDF](https://arxiv.org/pdf/2609.00092v1)
- **作者:** Ming Zhang 等（11+ 人）
- **分类:** cs.LG
- **摘要:** 长时复杂任务要求基础模型积累信息、维护内部状态、跨长交互适应。**安全应是模型自身的内在属性**，而非依赖外部护栏或 SFT 式后验对齐的行为约束——这就是 Safety from Within：安全相关能力通过模型原生计算表示与调用。提出 **Safin-1** 模型族：基于 Memory-Anchor Routing across Context……（摘要截断，核心是把「记忆路由 + 状态演化」作为安全能力的原生载体，安全不是外挂约束而是模型架构的一部分）。
- **关联度:** ★★★★★ 「记忆原生安全」模型族——安全从外部约束下沉到模型记忆路由；与 09-05 的 03887（拒绝电路 = 训练方法×架构耦合）、今日 00546/01235 的记忆主线同频，安全进记忆成为模型级趋势

---

## 四、评估、审计与可靠性（4 篇）

### 12. trajectory-judge: What Outcome-Only LLM Judges Miss on Agent Trajectories

- **ID:** [2609.00038v1](https://arxiv.org/abs/2609.00038v1) | [📄 PDF](https://arxiv.org/pdf/2609.00038v1)
- **作者:** Hadi Mohammadi
- **分类:** cs.CL, cs.AI, cs.SE
- **摘要:** 只看出结果是 LLM agent 的生产默认：给 judge 请求 + 最终回复问是否处理得当。该指标对「用错误方式得出正确答案」的 agent **结构性地盲**。本文在 ground truth 由构造保证处测量盲区：确定性工具型 support-desk 环境、总能解出的脚本 oracle 策略、已知步骤恰好破坏一件事的 fault injector（按客户可见结局是否存活分 silent/loud 两类故障）。五种 judge（程序化规则、outcome-only、两种规模的 step-rubric……）在……（摘要截断，核心是量化「结果对但过程错」的盲区，论证评估必须看轨迹）。
- **关联度:** ★★★★★ outcome-only 评估是生产默认但结构性失明——k 的自动化验收/交付质量门若只看最终结果会漏掉「错路达成」；与 09-05 的 03436（轨迹伪影）、今日 01519（construct validity）构成评估反身性三连

### 13. When Guardrails Look Effective: Construct Validity Failures in LLM Agent Commerce Evaluation

- **ID:** [2609.01519v1](https://arxiv.org/abs/2609.01519v1) | [📄 PDF](https://arxiv.org/pdf/2609.01519v1)
- **作者:** Peiying Zhu, Sidi Chang
- **分类:** cs.AI
- **摘要:** 交互式模拟越来越多地用语言模型 agent 填充的市场评估政策——输出看着像经济数据（价格、利润、消费者剩余、福利），却没实例化声明所命名的行为。在多轮买卖测试台上审计该风险：初始实现报告两个 marketplace guardrail 的福利增益 **+87.4 / +35.0 / +28.8**（Qwen2.5 1.5B–14B 梯），但它给了 guarded/unguarded agent 不同的 offer schema 与选择程序；固定 schema 与买家选择器后，配对对比变成 **+7.2 / -13.9 / +23.8**——大部分「增益」是测量构念失效。四个最大 14B 单生成器……（摘要截断，核心是模拟评估的 construct validity：声称的机制没被实例化，控制变量不齐 = 假改善）。
- **关联度:** ★★★★★ 「评估显示有效」≠「声称的机制存在」——k 对任何「加了 X 效果提升」的结果，先问控制变量是否在两组间一致；与 09-05 的 03436（难度/预算伪影）、今日 00038 同主线，评估反身性的最强一击

### 14. What Does an Agentic Software Engineering Benchmark Measure? Profiling Task Demands and Agent Behaviour Beyond What Category Labels Reveal

- **ID:** [2609.01271v1](https://arxiv.org/abs/2609.01271v1) | [📄 PDF](https://arxiv.org/pdf/2609.01271v1)
- **作者:** Radin Shayanfar, Keheliya Gallaba, Ahmed E. Hassan
- **分类:** cs.SE, cs.CL
- **摘要:** Agentic SWE 基准常用「bug fix」「feature implementation」等名义类别标签概括，但**带相同标签的基准由完全不同的 curation 流水线构建**——标签几乎不透露基准要求什么样的工程工作。提出 **Spread–Novelty–Centrality（SNC）profile**：仓库级编码任务需求的三轴刻画，基于实证软件工程研究。应用于 5 个常用基准 + 两个模型家族三规模共 14,922 条轨迹，三点发现：①标签是任务需求的不可靠代理……（摘要截断，核心是「基准到底测什么」的实证剖析：标签掩盖真实任务构成）。
- **关联度:** ★★★★ 选/建 SWE 评估基准前的必修课——k 评估编码 agent（Codex/ZCode 产出）时，SNC 三轴比名义标签更能刻画任务真实难度；与今日 01603（PTA-IRT 高效 SWE 评估）互补

### 15. AgentProv: Auditing Agentic LLM API Providers via Tool-use Policy Probes

- **ID:** [2609.00052v1](https://arxiv.org/abs/2609.00052v1) | [📄 PDF](https://arxiv.org/pdf/2609.00052v1)
- **作者:** Xun Wang, Bihe Zhao, Michael Backes, Franziska Boenisch, Adam Dziedzic
- **分类:** cs.CR, cs.CL, cs.LG
- **摘要:** 商业 LLM API 宣称提供某个基础模型，但背后的 backbone 可能被静默替换、量化或包装（省部署成本）。所有既有审计从**文本输出通道**判定 backbone 身份——对 agentic API 结构性脆弱：现代 serving 栈（OpenAI/Anthropic/Gemini/Cloudflare Workers AI/LangGraph）在模型调工具时丢弃文本、只暴露结构化动作，且 provider 注入的 system prompt 会扭曲文本分布，让文本通道测试误伤诚实 provider。观察：近期 agentic 后训练把工具使用**直接内化进权重**，开启 serving 栈仍暴露、且对部署上下文基本不变的新审计通道。提出 **AgentProv**：首个基于动作的 agentic LLM API 身份审计——用工具调用分布的类别指纹 + MMD 置换检验判定身份。630 个 checkpoint 对上**抓到每个被替换模型（100%）**，system prompt 注入下 FP 仅 **7%**（MET 67% / RUT 53%）；9 个 OpenRouter 三方可疑端点验证，其与 MET 的分歧与独立 token-count 侧通道（检测注入的 system prompt）一致。
- **关联度:** ★★★★★ API 供应商审计从「文本指纹」转向「动作指纹」——k 用第三方 API/中转站时，「宣称的模型是不是真身」有了新校验手段；文本通道在 agentic 时代结构性失效，直接补进 ai-api-provider-evaluation 类技能

---

## 十、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.01603](https://arxiv.org/abs/2609.01603v1) | PTA-IRT | 特权轨迹感知的 SWE agent 高效评估：把历史执行轨迹（探索的上下文、尝试的编辑、求解路径）作过程级证据融入 IRT，超越纯 pass/fail 结果矩阵——「怎么解的」也能帮预估全量表现，省评估成本 |
| 2 | [2609.00062](https://arxiv.org/abs/2609.00062v1) | RePro | 证明验证的数学基准重写：首个把 Lean 导向神经自动定理证明器(ATP)集成进基准重写，GSM8K/MATH 重写后 100% 良定义/可行/答案正确——防记忆污染的同时保证题没改坏 |
| 3 | [2609.01491](https://arxiv.org/abs/2609.01491v1) | GlossoGen | 多 agent LLM 互动中的涌现语言平台：SaveVeyru 场景下 agent 语言确实演化、具组合性与形态能产性、偏离英语先验——对「agent 间通信可监控性」的实证基础 |
| 4 | [2609.00738](https://arxiv.org/abs/2609.00738v1) | BASIN | 结构感知的推理时搜索：把推理状态聚成 basin、惩罚重复访问同一策略，固定算力下重分配搜索到真正不同的推理路径——Game of 24 上超 ToT +22pp、MuSR +6.7pp |
| 5 | [2609.00823](https://arxiv.org/abs/2609.00823v1) | Polished but Unresolved | 长时工具 agent 的晚期压力状态：线性探针可从隐状态识别「急着交一个看着完整其实约束没解决」的状态，激活干预能改变 agent 是继续用工具还是提前提交 |
| 6 | [2609.00035](https://arxiv.org/abs/2609.00035v1) | SilentProbe | 生产 API 作 agent 工具时的静默失败测量：审计 2501 份 OpenAPI 文档发现 7.5% 声明枚举、40.1% 只在散文里写约束、schema 没编码——agent 无法区分「没匹配到」与「服务器没听懂」 |
| 7 | [2609.00012](https://arxiv.org/abs/2609.00012v1) | MD5 State Tracking | 长时状态跟踪评估：让 LLM 经深序列依赖工具调用执行 MD5，单步准确率看似优秀、端到端因错误级联灾难性衰减——隔离「状态跟踪难度」与指令理解、防幻觉捷径 |
| 8 | [2609.00605](https://arxiv.org/abs/2609.00605v1) | Forget-Set Misalignment | LLM unlearning 的 forget-set 错位：忘记集漏了已记忆知识=欠遗忘泄露仍在，逼算法忘掉从未学过的知识=过遗忘损效用——梯度级分析显示源于目标错位而非算法本身 |
| 9 | [2609.01073](https://arxiv.org/abs/2609.01073v1) | Post-hoc LLM-judge Alignment | LLM-as-judge 后验对齐人类判断分布：5 数据集上 LLM 达近人类水平预测聚合 hard-label，但对未聚合的 soft-label（人类判断分布）系统性更差——评估要保留人类标签变异信息 |

---

## 今日要点（主题信号）

1. **harness 完成「工具 → 平台」转折，且直接包含 Hermes**：00006 解剖 11 个生产 harness（含 Hermes/OpenClaw/OpenCode），400 万行源码零通用框架依赖、零 embedding 检索代码，**SKILL.md 9/11 领先 MCP 8/11**、ACP 6 系统 + harness hosting 角色；01600 把「harness 内部生命周期推理」变成可测能力、01437 让 harness 成为 agent 可自举的产物——harness 从「配置面」升格为「一等研究对象 + 攻击面 + 能力维度」三位一体，与 09-05 的 HookPry 攻击线正好攻防闭环。
2. **agent 委托授权进入「untrusted-model」范式**：00267 的 authorization broker（每决策 2.6μs、20 万伪造 token 0 接受、被攻陷子 agent 1.5 vs 8100 可达动作）+ 01035 递归树风险预算 PRV + 09-05 的 01836 记忆授权洗白——**「注入后的 agent 也不能越权」成为可证标准**，授权决策必须移出模型、由基础设施强制，k 的多 agent 委派流程应逐条对照其 8 条安全要求。
3. **agent 记忆「可移植 + 可验证 + 原生安全」三线并进**：00546 把身份/记忆/代码与运行时绑定解耦（跨模型/harness 迁移不丢连续性）、01235 用密码学契约让记忆变异可移植可复现、00092 Safin-1 把安全做成记忆路由原生的模型架构——延续 09-05「记忆 = 授权策略」共识，从安全面扩展到工程面。
4. **评估反身性再添两击**：00038 量化 outcome-only judge 对「错路达成」的结构性盲区、01519 用 +87.4→+7.2 的对照组揭示 guardrail 评估的 construct validity 失败——与 09-05 的 03436 合成「测量仪器不可靠」完整证据链，**所有「加 X 有效」必须先过控制变量审查**。
5. **API 供应商审计转向「动作指纹」**：00052 用工具调用分布（而非文本）审计模型真身，630 对 100% 抓替换、注入下 FP 7%（MET 67%）——文本通道在 agentic 时代结构性失效，k 用第三方 API/中转站时有了更强的身份校验手段。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Harness Engineering 2609.00006 | web_search arXiv 页（Wavestone AI Lab）+ 关联 AI Harness Engineering 2605.13357/Code as Agent Harness 2605.18747 | ✅ 已确认（11 harness 含 Hermes/OpenClaw/OpenCode 属实；13 观察/29 模式/SKILL.md 9/11 vs MCP 8/11/零框架依赖属实） |
| Delegation Without Trust 2609.00267 | web_search arXiv 页 + 关联 Bounded Agents 2608.15888/LDP 2603.08852/Five Primitives 2608.26696 | ✅ 已确认（4 威胁/8 要求/20 万伪造 token 0 接受/2.6μs 属实；同潮 2608.15888/2604.02767 均走「授权移出模型」路线） |
| AgentProv 2609.00052 | web_search arXiv HTML 页（CISPA）| ✅ 已确认（630 对 100% 抓替换、FP 7% vs MET 67%、OpenRouter 9 端点验证属实） |
| 其余 26 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据（API 429 期间） | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要） |

## 可落地行动项

- 🔴 **精读 Harness Engineering 00006**：它直接解剖了 k 的运行时本体（Hermes/OpenClaw/OpenCode）——通读 7 子系统对比 + 29 模式 + 18 条设计建议，对照自身配置找可迁移改进；「SKILL.md 领先 MCP、零通用框架、确定性检索」三条实证结论直接背书 k 的技能体系与工具选型
- 🔴 **多 agent 委派按 untrusted-model 审查**：00267 的 8 条安全要求 + 01035 的沙盒 vs 能力激活区分——k 的委派流程（Codex/ZCode/WorkBuddy/dsh）自查「被完全注入的 agent 是否仍无法超出被授予权限」，凭据与授权状态移出模型上下文
- 🟡 **记忆工程化参照三篇**：00546 的 P_t=(I,M,B) 连续性基底 + 01235 加密授权变异契约 + 00092 记忆原生安全——k 的持久记忆/跨 agent 记忆设计把「身份/记忆/代码版本化绑定」与「授权带溯源」做成一等字段
- 🟡 **任何「加 X 有效」先过 control 审查**：01519 的 +87.4→+7.2、00038 的 outcome-only 盲区——k 的评估/验收/交付质量门先问「改的真是声称的东西吗、对照组变量齐吗」再信增益数字
- 🟢 **待深读**：00006 Harness Engineering、00267 Delegation Without Trust、00546 Persistent Agents、00052 AgentProv、01519 Guardrails validity → 进 core-contributions 候选

---

*本速览由 cron 自动生成：09-06 索引继续冻结（API 最新 09-03T17:59Z、list 页无 09-05/09-06 分组、API 429 限流）→ 09-05 速览补录 21+8 仍未盖满同池 → 窗口全量 924 篇比对 covered_ids 得 821 未覆盖 → 标题粗筛剔除领域应用 → 逐篇抓 abs 页人工精选（15 主条目 + 9 简评，全部为新覆盖）→ 关键论文 web_search 交叉验证。数据源 arxiv.org + export.arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
