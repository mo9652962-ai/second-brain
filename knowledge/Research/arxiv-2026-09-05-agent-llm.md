---
aliases:
  - arxiv-2026-09-05-agent-llm
  - arxiv-agent-llm-2026-09-05
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-05
updated: 2026-09-05
status: adopted
source: arxiv.org list pages + abs pages（API 429 限流期间）
---

# arXiv AI Agent / LLM 速览 — 2026-09-05（补全性质）

> **检索时间**: 2026-09-05 GMT+8
> **⚠️ 补全性质**: 09-04 速览已收录 09-03+09-04 双日窗口全部 925 篇的唯一索引；本次**索引冻结无新提交**（export.arxiv.org 全局最新时间戳停在 09-03T17:59Z，list 页无 09-05 分组，API 持续 429 限流）。但 09-04 速览只是「精选 24 主条目 + 12 简评」、**未盖满同一提交池**——本速览**补录同池漏网强相关论文**，头部声明补全性质，不重写已收录内容。
> **收集**: 6 类别 list/recent 页全量 → 09-03 454 + 09-04 471 = **924 唯一 base ID**（与 09-04 速览同池，索引未推进）→ 剔除 covered_ids 已覆盖 75 → **849 未覆盖** → 标题粗筛 106 → 逐篇抓 abs 页精选出 **21 主条目 + 8 简评**（仅保留 LLM/AI Agent 本体相关）
> **数据源**: [export.arxiv.org](https://export.arxiv.org)（429 限流） + [arxiv.org/list](https://arxiv.org/list/cs.AI/recent)

---

## 一、Agent 安全与对齐（3 篇）

### 1. Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness

- **ID:** [2609.03887v1](https://arxiv.org/abs/2609.03887v1) | [📄 PDF](https://arxiv.org/pdf/2609.03887v1)
- **作者:** Hoang Cuong Nguyen, Mark Dras, Usman Naseem
- **分类:** cs.CL
- **摘要:** 训练 LLM「拒绝有害请求」的方法如何决定拒绝在模型内部的实际计算方式？对比三种后训练方法——监督微调 SFT、推理增强微调（用证明安全决策的推理链训练）、偏好优化 ORPO——跨三个架构不同的模型（Llama-3.1-8B / Gemma-2-9B / Qwen3-8B）。发现**训练方法（不只是数据）重塑拒绝的计算内部结构**：推理增强训练在三模型上都产生一种独特的拒绝计算形态；架构则独立塑造内部结构与拒绝可被可靠定向编辑的程度。最关键的是：**没有任何方法同时具备安全对齐想要的三性质**——拒绝不集中在少数脆弱组件、安全增益不牺牲通用能力、安全行为可通过小而定向的编辑修正。作者警告不要把当前后训练方法当作已解决、可靠的防御，尤其对安全关键用途。
- **关联度:** ★★★★ 对齐从「数据问题」翻转为「方法×架构耦合问题」——k 选模型/做对齐评估时，不能只看拒答率，要看拒绝电路的形态与可修复性；与 09-04 的 Representational alignment（对齐下沉到表示层）互为补充

### 2. Context Inference Attacks Without Jailbreaks

- **ID:** [2609.01663v1](https://arxiv.org/abs/2609.01663v1) | [📄 PDF](https://arxiv.org/pdf/2609.01663v1)
- **作者:** Prince Jha, Samuele Poppi, Nils Lukas
- **分类:** cs.CR, cs.LG
- **摘要:** Agentic AI 越来越多在推理时处理敏感数据——医疗记录、财务文档被组装进隐藏 context 再作答。已有隐私研究主要通过**越狱**让模型直接泄露内容，忽略了「context 由 agent 自己的工具调用组装」的 agentic 场景。作者证明：尽管施加了「不得披露 context」指令、logit 抑制、context 稀释等控制，被评估 agent 仍对隐藏 context 泄露脆弱——例如一个回答良性用户查询的网页浏览 agent，仍携带可被利用的「记录被静默载入其 context」的信号。形式化 **context-inference 攻击**为安全博弈，评估三种攻击者知识递减+投递越来越间接的场景（已知 context / 未知 context / agent 自己检索的 context），区分灰盒（用目标模型打分）与黑盒（用可控替代模型打分）。单个攻击无需修改贯穿三场景：小候选集 100% ASR、1024 候选时 63%；未知模板+记录时 AUROC 78.9；14B 替代模型给 32B 目标打分 AUROC 92.5；记录经 agent 检索返回时 AUROC 81.8（随机基线 1/|Z| 与 50）。
- **关联度:** ★★★★★ 不越狱也能侧信道窃取 context——k 做敏感数据处理 agent / 隐私评估时，「不披露指令」类防护全部无效，需按「工具调用组装 context」的攻击面重新设计；直接补进安全面清单

### 3. Door-in-the-Face Requests and Refusal Behaviour in Large Language Models

- **ID:** [2609.02707v1](https://arxiv.org/abs/2609.02707v1) | [📄 PDF](https://arxiv.org/pdf/2609.02707v1)
- **作者:** Til Jordan
- **分类:** cs.AI, cs.CL
- **摘要:** 人类心理学里的「先拒后从」（door-in-the-face）技巧——先被拒的大请求会让随后的较小请求更可能被答应——对 LLM 是否成立？对三家供应商九款生产模型实测：每个模型先拒绝一个大请求，再收到同一请求的较小版本，对比直接问的合规率。**答案因模型而异**：Anthropic 前沿模型上技巧成立（Opus 5 先拒后答 65.8% vs 直接问 29.3%）；OpenAI / Google 前沿模型和 Haiku 4.5 上**适得其反**（合规率降 15.5-23.0 分）。对照定位了效应：无关主题的被拒大请求比相关主题的效应弱（九模型一致），说明「让步本身」处处有效，而对「刚拒绝过」的反应因模型家族而异。该技巧不能迁移到公开基准的拒答上。决定「退一步能否得手」的是请求内容本身：把 265 条被拒请求从「可用指令」改写成「同一主题的解释请求」，263 条不再被拒。人类影响技巧按模型家族逐一迁移到语言模型。
- **关联度:** ★★★★ 社会工程式请求的模型差异实证——k 的越狱/安全测试与 09-04 的 ASCII Attack 互补（一个改呈现形式、一个用心理脚本）；「改写为解释请求」= 现有拒答训练的大盲区

---

## 二、多智能体编排与协作（3 篇）

### 4. The Illusion of Independent Quorums: Epistemic Fault Domains and Correlated Cognitive Failures in Agentic Quorums

- **ID:** [2609.02925v1](https://arxiv.org/abs/2609.02925v1) | [📄 PDF](https://arxiv.org/pdf/2609.02925v1)
- **作者:** Jun He, Deying Yu
- **分类:** cs.DC, cs.MA, cs.SE
- **摘要:** 多智能体 quorum（法定人数投票）广泛用于授权高风险基建与策略变更，但不同评审者常共享上游遥测、文档或工具后端。**上游输入一挂，多个投票坍缩到同一个被污染原因上：复制 ≠ 认识冗余**。引入 Epistemic Fault Domains（EFD）与 Structural Epistemic Cut κ_E——量化「暴露一个授权联盟所需的最少建模根故障数」。在封闭因果核算、保守暴露、授权对齐假设下，κ_E 是语义妥协所需根数 κ_S 的下界。证明：任意大的 quorum 可保持 κ_E=1；识别共享血统从不增加可信冗余；固定阈值下加投票者不增 cut。给出 Dependency-Aware Quorum Controller（DAQC）在运行时准入强制结构 cut，附冻结的 120 任务外部基准套件。
- **关联度:** ★★★★ 多 agent「独立评审」是幻觉——k 的多 agent 编排/安全评审流程应检查评审者间共享依赖（同一模型/同一工具后端/同一文档源），否则冗余投票给虚假安全感；可落地为「评审去相关」检查清单

### 5. Beyond Outcome Gaps: Process-Aware Fairness Diagnosis for LLM-based Multi-Agent Decision Systems

- **ID:** [2609.02092v1](https://arxiv.org/abs/2609.02092v1) | [📄 PDF](https://arxiv.org/pdf/2609.02092v1)
- **作者:** Yiran Zhao, Lu Zhou, Liming Fang, Yufei Chen, Jiafei Wu, Zhe Liu, Xiaogang Xu
- **分类:** cs.AI
- **摘要:** LLM 多智能体系统（MAS）越来越多用于高风险决策，但**基于结果的公平审计会漏掉风险出现在决策轨迹内的位置**。提出 SCOPED-Hiring：面向 LLM 招聘 MAS 的过程感知公平诊断流水线——构造受控简历变体、运行基于角色的招聘委员会、记录 311K+ 条结构化决策轨迹，把轨迹字段转成六个诊断透镜的量化公平信号：最终结果 / 反事实 / 过程 / 路径 / 动态 / 设计效应。揭示**均衡的最终录用率可掩盖隐藏的轨迹不公平**：职业空窗触发怀疑、代理线索塑造资质判断、身份线索导致不均衡调查。由诊断引导的定向修复把总分层负担降 72.3%、录用率只偏移 1.86 个百分点——过程诊断能指导有效修复。
- **关联度:** ★★★★ 「结果公平」是错觉、过程审计才见风险——k 做自动化评审/验收/多 agent 决策时，公平性检查要下沉到决策轨迹（谁被多查、谁被少查），与 09-04 的 Counterfactual Fairness Audits（每动作不稳定地板）同主线

### 6. The Civilization Framework: Sovereign-Anchored Communication Between Personal Multi-Agent Systems

- **ID:** [2609.03425v1](https://arxiv.org/abs/2609.03425v1) | [📄 PDF](https://arxiv.org/pdf/2609.03425v1)
- **作者:** Guangjun Liu
- **分类:** cs.MA, cs.AI
- **摘要:** 人类是 AI 系统之间的传输层，每一跳都丢上下文。提出 Civilization Framework：可寻址的当事方是**文明**而非 agent（一个人类主权者 + 一个持久账本 + 可互换的 agent），配 Embassy Protocol（载体无关的覆盖层）：消息异步到达常驻账本端点、接收方任一在线 agent 处理、两账本上的承诺状态（而非投递）是 ground truth。**权威源于记忆**：agent 为其文明行事的权力上限 = 它能访问的记忆，经签名凭据外化，与文明级声誉分离。识别 AI 间通信的**时间权重效应**（先到的信息获得不当权威）：预注册 1908 试次实验中，移除验证时错误的上游声明先到捕获 54.2% 的答案（完整验证下 4.2%）；接收方已密封自己答案后到达则只捕获 31.6%。因工具调用检查未达调用预算，注册判定本轮 inconclusive、结果全按探索性报告，复制计划中。
- **关联度:** ★★★★ 个人多 agent 系统间通信的「主权账本」设计 + 时间权重效应——k 若搭多 agent 协作/知识交换，「先到即有权」是必须防的偏差（与 01836 记忆授权洗白同构）；探索性结果需谨慎引用

---

## 三、Agent 记忆（2 篇）

### 7. Agent Memory Is a Surface for Endogenous Authorization Laundering

- **ID:** [2609.01836v1](https://arxiv.org/abs/2609.01836v1) | [📄 PDF](https://arxiv.org/pdf/2609.01836v1)
- **作者:** Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol
- **分类:** cs.CR, cs.AI
- **摘要:** 长期运行 LLM agent 依赖持久记忆跨交互携带状态——包括权限、限制、撤销。当记忆错误表述不断演化的授权状态，**agent 自己的记录就能授予底层历史从未允许的权限**，无需任何外部攻击（内生授权洗白：写进记忆的虚假权限因溯源被洗掉而通向未授权动作）。提出 EAL-Bench 测两点：记忆写入器是否保真保存演化中的授权状态、错误是否传导到下游未授权动作。5 个 LLM 当写入器 + 2 个当执行者（采购/网安/金融）：增量记忆更新下写入器为最高 **50.2%** 的未授权请求制造虚假权限；虚假权限一旦存在，执行者在 **98.6%** 试次照单执行。两个防护——存储权限须有有效源事件背书、用有界事件溯源追踪权限变更——显著降低洗白但误拒更多合法动作，暴露安全-效用权衡。**持久记忆不只是性能组件，而是 agent 有效授权策略的一部分**。
- **关联度:** ★★★★★ 记忆即授权策略——k 给任何 agent/Hermes/Mnemon 加持久记忆时，权限/限制/撤销必须绑定源事件 + 有界溯源，防「记忆洗白权限」；同线程 2607.29167 Memory Provenance Laundering、2608.01679 Authority Collapse 可连读成「agent 记忆安全」小专题

### 8. Plan Pointers and Record-Directive Form in Budgeted Verification of Inherited Agent Memory

- **ID:** [2609.03450v1](https://arxiv.org/abs/2609.03450v1) | [📄 PDF](https://arxiv.org/pdf/2609.03450v1)
- **作者:** Kazuki Nakayashiki
- **分类:** cs.IR, cs.AI, cs.CL
- **摘要:** 继承六行记忆的 agent 行动前最多拉取 1 条归档源记录；写进存储的**指令形态**（指向记录的指针、识别它的 criteria、或两者）能操纵这个选择。12 个注册研究、同一工具谱系、14,760 次尝试：长度匹配的 criteria 比裸 id 高 +35.0 分（Study D）；对九个模型的 OpenRouter 面板上该优势未过注册显著性（Study E）；在三个 Claude 模型上追加 id 会**抵消** criteria 效果（Opus 5：40/40 → 0/40）；单字符 plan pointer +78.0 分（预注册复跑 +81.7）。全为精确编辑的 descriptive 效应、注册区间、无机制声明——「记录指引表单」能系统性操纵 agent 的检索方向。
- **关联度:** ★★★★ 记忆提示注入的另一面：不污染内容、用「指引文字」劫持检索路径——与 01836 授权洗白是同一威胁面（谁控制 agent 读哪条记忆）的互补入口；k 的 Agent 记忆安全检查应覆盖「检索指引指令」这类隐形控制

---

## 四、Harness / 工具工程（2 篇）

### 9. A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors

- **ID:** [2609.03884v1](https://arxiv.org/abs/2609.03884v1) | [📄 PDF](https://arxiv.org/pdf/2609.03884v1)
- **作者:** Pengxun Li, Litian Zhang, Jianwei Hou, Shujiang Wu, Song Li, Zifeng Kang, Xi Zhang
- **分类:** cs.CR, cs.AI
- **摘要:** 现代 AI agent harness 暴露**生命周期 hook**，把 shell 命令绑定到会话启动、工具调用、文件编辑等运行时事件。这些命令以宿主权限运行、却作为 hook 配置随插件分发、可能在 LLM 从不观察的时机触发。识别出 harness 盲信的 **lifecycle-hook 更新路径**为新攻击面：供应链威胁模型下攻击者只控制插件元数据与 hook 配置，一个良性版本化插件可被「静默把攻击者选定的命令绑到良性事件」的更新木马化，产生提权等恶意宿主行为。提出开源全自动攻击框架 **HookPry**，实现十个攻击目标；25 种 harness×后端组合、1000 次端到端运行中**七个被测 harness 全部沦陷**，单 harness 成功率最高 92.5%。现有防御不足：Microsoft Defender 召回 0%，三个静态防御的并集仍漏 47.5% 恶意工件。
- **关联度:** ★★★★★ 插件/hook 供应链攻击直达 k 的 Hermes/Codex/Claude Code 配置面——「hook 命令 = 可执行代码」应成为安装插件/技能时的第一原则；与 HarnessSafe/HarnessRisk（直接评测 Hermes/OpenClaw）同一研究潮，harness 配置面是当前最薄弱防御点

### 10. Architecting Conversational Data Systems for Stateless LLM APIs: The Hydration Proxy Pattern

- **ID:** [2609.01834v1](https://arxiv.org/abs/2609.01834v1) | [📄 PDF](https://arxiv.org/pdf/2609.01834v1)
- **作者:** Joseph Axisa
- **分类:** cs.AI, cs.SE
- **摘要:** 企业平台转向会话式推理界面时，LLM API 的无状态性制造架构缺口：无状态让 AI 供应商横向可扩展，却把会话状态与语义记忆的负担全压给客户端。识别 **Hydration Proxy Pattern**：把会话持久化与推理引擎解耦的架构，保证平台对会话数据的**主权**、同时支持安全的多阶段语义接地。提出 Context Stabilization Mandate 解决「主权状态管理 vs KV 缓存」的取舍。
- **关联度:** ★★★ 会话状态与推理解耦的参考架构——k 的墨题/刷题机若接 LLM 对话接口，「谁持有会话状态、如何语义接地」可借鉴此模式（数据主权 + 缓存权衡）

---

## 五、评估与可靠性（3 篇）

### 11. It's the Problem, Not the Path: Budget and Difficulty Confounds in LLM Reasoning Trajectories

- **ID:** [2609.03436v1](https://arxiv.org/abs/2609.03436v1) | [📄 PDF](https://arxiv.org/pdf/2609.03436v1)
- **作者:** Yigit Utku Bulut
- **分类:** cs.LG, cs.AI, cs.CL
- **摘要:** 推理轨迹被广泛解读为包含「突破时刻」与「早期注定」——两种解读都缺在声明层面的反事实对照，本文补齐两个对照。其一，**重启受控的截断探针**：在匹配的总 token 预算下对比「续接锚点前缀」与「从头重启」的解题率，分离「解适应续接预算」与「前缀携带新鲜计算买不到的价值」。178 个 problem-model 单元（89 MATH × 两个小开源模型）中**恰好 1 个**以「前缀受限」存活；重启剂量-反应可区分「算力饥饿的模型」与「能力受限的模型」；匹配预算落在重启网格内时，续接自己的前缀胜过重启（9/9）——主要是计算压缩而非扩展可达性。其二，预注册难度受控测试在早期窗口内部信号里**找不到超出题目难度基线的可检测结果信息**。还证明为什么需要这个对照：trace-blind 难度代理在 192K 条 DeepSeek-R1 生成上达 AUROC 0.873（落在已发表探针区间内）；最接近的已发表「早期窗口正结果」复现出可比聚合值（0.849），但问题内十个锚点全部与随机无显著差异（t=4 时 0.496）。**高聚合探针 AUROC 本身不能确立单次尝试内有信息，必须补 question-only 基线或问题内评估**。
- **关联度:** ★★★★★ 把「早期信号能预判成败」的研究判定为测量伪影——k 用推理轨迹做验收/预测时，先补「重启对照 + 难度基线」，否则把预算/难度伪影读成能力信号；与 09-04 的 LLM judge 仪器化主线完全同频

### 12. The Dice Roll Method: A Standardized Protocol for Repeated-Query Auditing of LLM Brand Recommendations

- **ID:** [2609.04047v1](https://arxiv.org/abs/2609.04047v1) | [📄 PDF](https://arxiv.org/pdf/2609.04047v1)
- **作者:** Dmitrij Żatuchin
- **分类:** cs.IR, cs.CL
- **摘要:** 研究者越来越多用重复相同提示审计 LLM 品牌推荐的随机变异，但缺少设定迭代次数、选稳定性指标、定可靠性阈值的标准协议。把 **Dice Roll Method** 形式化为可复用协议，基于温度缩放 nucleus 采样的生成模型；把总响应方差分解为采样/提示措辞/运行间/模型版本四部分。方法栈：负二项混合模型（迭代为重复测量）+ Cliff's delta（无分布效应量）+ 保持依赖的 bootstrap + 基于模拟的功效 + 概化理论分解 + 固定快照漂移诊断。重分析 5 个品牌推荐审计研究（约 19 万观测、270+ 品牌、6 语言、迭代数 5-40），得出**三档迭代指引：探索 n=5（G=0.58）/ 确证 n=10（G=0.74）/ 严格 n=15（G=0.81）**，绑定效应量与概化目标。三个独立语料的外部验证 39 格中 37 格复现可靠性预测，但固定档位不可迁移——支持「先试点再定档」的读法。
- **关联度:** ★★★★ 重复查询审计从「凭感觉定 n」升级为统计原则——k 用 LLM 反复查询/抽样做稳定性判断时按 探索5/确证10/严格15 分层定迭代数，方差按四来源分解

### 13. GPS-Bench: A Governance Policy Benchmark for Automating Policy Analysis

- **ID:** [2609.03553v1](https://arxiv.org/abs/2609.03553v1) | [📄 PDF](https://arxiv.org/pdf/2609.03553v1)
- **作者:** Linh Le, Melanie Bui, My Chiffon Nguyen, Zachary Schlosser, David Williams-King
- **分类:** cs.AI, cs.CY
- **摘要:** 政策分析不止预测提案能否通过，还要识别谁受影响、行为体如何反应、后续是什么。LLM 政策仿真规模化建模这些过程，但「貌似合理的仿真从未与观测结果对照」时有效性难立。提出 **GPS-Bench**：证据接地的治理政策仿真基准，用立法记录、游说披露、监管文件、公司备案、经济数据等公共证据把政策链接到相关行为体、行为与下游影响。行为体从带日期的记录重建而非提示成原型——persona 是带溯源证据对象；人工标注池构成 Gold 评估集，另一 LLM 从检索证据标注的案例只作 Silver 监督、永不作测试标签。所有推理模式读同一接地状态、输出同一 schema，把「多 agent 仿真有没有用」变成受控对比（联合推理/独立与通信行为体 agent/图方法/权重级微调）。结果：对接地记录微调给出最强的行为体级影响预测，分解不赢它——**分解带来的是机制**。
- **关联度:** ★★★ 治理/政策多 agent 仿真的证据接地基准——k 若做政策/制度类仿真，「persona 必须是从记录重建的带溯源证据对象 + Silver 永不作测试标签」是可借鉴的严谨性红线

---

## 六、RL 后训练（3 篇）

### 14. Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR

- **ID:** [2609.04108v1](https://arxiv.org/abs/2609.04108v1) | [📄 PDF](https://arxiv.org/pdf/2609.04108v1)
- **作者:** Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye
- **分类:** cs.CL, cs.AI, cs.LG
- **摘要:** RLVR（可验证奖励强化学习）与 OPD（on-policy 蒸馏）是后训练推理 LLM 的两大主流。已有工作用 OPD 的稠密 token 级监督补 RL 的稀疏奖励，在单步内融合两信号——加权相加或教师调制重标 RL advantage。本文证明**简单的两阶段方案 OPD-then-RL 一致胜过纯 OPD、纯 RLVR 与所有单步联合基线**（逻辑与数学推理基准）。机制解释：pass@k 行为、学习动力学与参数更新一致表明——**OPD 扩大学生对教师支持解集的覆盖，RL 在该支持集内锐化**；而单步联合优化让两信号互相干扰。实用配方：**OPD 验证分是切换到 RL 的关键信号**，且 OPD 比 SFT 更适合做 RL 的冷启动。
- **关联度:** ★★★★★ 后训练范式收敛为「先蒸馏扩覆盖、验证分触顶再切 RL 锐化」——k 做模型微调/蒸馏任务按两阶段编排，避免单步联合的互相干扰；与 OPDVR/CoPD/Demystifying OPD 同研究潮（2608.24696/2604.27083/2607.13399）

### 15. FlowBalance: Verifier-Grounded Self-Improvement from On-Policy Reasoning Experience

- **ID:** [2609.03241v1](https://arxiv.org/abs/2609.03241v1) | [📄 PDF](https://arxiv.org/pdf/2609.03241v1)
- **作者:** Zixun Huang, Kishan Panaganti, Haitao Mi, Leowei Liang
- **分类:** cs.LG, cs.AI
- **摘要:** 推理模型能从自身 on-policy 经验改进，但这个内环脆弱：终局验证器可靠却稀疏，稠密的同模型引导会强化虚假信心或过度集中于狭窄解法模式。提出 **FlowBalance**：验证器接地的自我改进方法，学习完整响应的归一化分布。每条 on-policy 轨迹用冻结的训练时策略视图（特权上下文）产生 token 级对数概率增益，聚合成轨迹级自引导分；用验证器派生的组 advantage 校准：正 advantage 轨迹保留引导、负 advantage 轨迹反转、无结果偏好组禁用。能量法指数重加权参考策略，profile 轨迹平衡每 roll-out 组一个 log-分区估计拟合并归一化目标。分析给出组内对比保持、最小变更 reverse-KL 表征、验证器对目标奖励的单调控制、对被拒响应上假阳性自引导的精确修正。数学推理上比 FlowRL 在 Qwen3-4B/8B 均更优，同时训练更快更稳，避免 OPSD 的响应长度坍缩，AIME24 受控诊断中正确策略多样性更高。
- **关联度:** ★★★★ 「验证器校准自我引导」解决自训练内环的虚假信心——k 做 self-improve/自蒸馏类流水线时，「稠密自引导必须被外部验证器校准」是防塌缩的关键；与 04108 同属 RL 后训练收敛主线

### 16. On-Policy Distillation Meets Off-Policy GRPO: Training Compact Instruction-Following Rerankers

- **ID:** [2609.01947v1](https://arxiv.org/abs/2609.01947v1) | [📄 PDF](https://arxiv.org/pdf/2609.01947v1)
- **作者:** Vignesh Prabhakar, Jialing Pan, Anil Babu Ankisettipalli
- **分类:** cs.LG, cs.AI
- **摘要:** 紧凑指令跟随 reranker 部署友好，但传统蒸馏用离线模仿教师输出、监督被锁死在教师观察到的排序空间。用强化学习视角重做 reranker 蒸馏：两阶段框架——阶段 1 用离策略 GRPO + LLM-judge 反馈在 88K 指令跟随样本上强化 4B 教师 reranker；阶段 2 让 1B 紧凑学生**从自身策略采样排序**、接收软教师派生奖励，耦合学生探索与知识迁移。最大增益出现在分布偏移下：MAIR-11 上学生达 0.7670 nDCG@6，超离线 listwise KD +4.6 分；受控对比证明改离线目标或 on-policy 教师分布匹配都复现不了「基于奖励的 on-policy 蒸馏（学生采样排序）」的成绩。MAIR-Full 全部 126 任务/9,356 查询上取最高 task-macro 点估计（0.6808 nDCG@6、0.7865 MRR@6），还超两个已发布 7B RL 训练的 reranker；同一阶段 2 流程一致改进三种架构不同的替代学生骨干。
- **关联度:** ★★★★ 学生采样自身排序 + 奖励驱动蒸馏（而非离线模仿）——k 做检索/排序类蒸馏任务时，「学生探索与知识迁移耦合」比固定集模仿抗分布偏移；GRPO 进蒸馏与 09-04 的 RL 主线呼应

---

## 七、推理与长上下文（3 篇）

### 17. Trace as State: Reasoning Traces as Conditional States for Long-Context Transformers

- **ID:** [2609.02702v1](https://arxiv.org/abs/2609.02702v1) | [📄 PDF](https://arxiv.org/pdf/2609.02702v1)
- **作者:** Xu Zou, Jie Tang
- **分类:** cs.CL
- **摘要:** Transformer 因果处理信息，但长上下文推理可能依赖只有后面才发现的**任务状态**。把这种错配形式化为条件状态更新任务：对因果状态更新处理器，最坏情况下「条件先给」比「条件后给」可指数级省内存。据此提出 **Trace as State**：用收集到的推理轨迹作为任务状态的文本代理，放在长上下文块之前的新一趟阅读，让先前派生的信息引导重读。对照 Trace Append（同一状态代理放 context 之后）。三模型三长上下文数据集上，27 个 模型×任务×指标 组合里 Trace as State 胜 26 个。GraphWalks Parents 精确匹配把 DeepSeek V4 Pro Preview 从首趟 29.2%（Append 43.0%）拉到 81.8%，GLM-5.2 从 66.4%/83.2% 到 100.0%。保留因果结构前提下「轨迹前置」即可显著提升长上下文推理。
- **关联度:** ★★★★ 不用改架构、纯输入排布就能大幅提长上下文推理——k 的 RAG/长文档 agent 可低成本试「先给推理轨迹再给正文」的 prompt 排布；与 09-04 记忆/长上下文主线互补

### 18. A Survey on Self-Improving Test-Time Intelligence: Feedback-Driven Adapting, Learning, and Scaling at Inference

- **ID:** [2609.01679v1](https://arxiv.org/abs/2609.01679v1) | [📄 PDF](https://arxiv.org/pdf/2609.01679v1)
- **作者:** Shuaicheng Niu 等（17 人）
- **分类:** cs.LG
- **摘要:** AI 系统在部署期间改进自身行为的能力日益重要。推理已超出「固定训练模型的静态执行」，大量工作研究模型如何利用测试时信息与额外计算实时精炼行为。发展沿两个方向：用测试时信号**修改模型状态**的方法，与用额外推理时资源（更多采样、工具使用）**改进预测**的方法——但常被不同社区、不同术语割裂研究。本综述以**反馈驱动的测试时智能（TTI）**作为统一视角，用这一视图关联测试时适应（test-time adaptation）、测试时学习（test-time learning）与测试时扩展（test-time scaling），凸显区分与混合系统中的重叠；覆盖视觉、语言、多模态、生成模型、机器人、医疗等主要范式、代表应用与开放挑战，给出自改进 AI 系统的概念基础与研究路线图。
- **关联度:** ★★★★ 把碎片化的测试时研究方向统一成一张地图——k 做「部署期自改进」类设计（agent 在跑的过程中变强）时，这是绝佳的总入口/索引，避免只见树木

### 19. RecurTrace: Adaptive Latent Reasoning with Loop-Time Memory

- **ID:** [2609.03379v1](https://arxiv.org/abs/2609.03379v1) | [📄 PDF](https://arxiv.org/pdf/2609.03379v1)
- **作者:** Yuxiang Wang, Kunyu Feng, Yingda Shen, Haoning Xu, Junyu Wang, Zhizheng Wu
- **分类:** cs.LG
- **摘要:** 重复小块中间层可无参数、无额外 token 地增加模型有效推理深度，最近工作证明这种**隐式循环**（latent recurrence）提升推理。两个设计选择限制增益：每次迭代只见上次输出、无法直接访问更早计算；固定循环数在简单输入上浪费深度、在困难输入上又不够算。提出 **RecurTrace** 用循环自身轨迹解决两者：Loop Memory Attention 让每个循环层沿循环时间轴关注自身历次迭代状态（可回看早期计算而非只靠最新状态）；halting head 读循环状态预测是否继续，用「额外深度是否仍降 loss」的 oracle 监督。受控 MathQA 对比：56.9% 精度、平均 2.0 循环，超最佳固定深度 2.2 分（匹配算力下）；ACT/PonderNet 坍缩到 1 循环，CALM 5.6 循环才 54.1%。0.6B-8B 上生成精度一致超同预算微调基线，增益随规模从 0.6 涨到 3.4 分。
- **关联度:** ★★★ 隐式循环 + 循环记忆 + 自适应停止——推理深度分配的工程路线，与固定算力提升推理的诉求匹配；k 的模型选型/推理优化可关注这类「无参加深」趋势

---

## 八、代码 Agent（1 篇）

### 20. TIPCODER: Reinforcement Learning Boosted Test-time Instruction Proposer for Code Generation

- **ID:** [2609.03309v1](https://arxiv.org/abs/2609.03309v1) | [📄 PDF](https://arxiv.org/pdf/2609.03309v1)
- **作者:** Minyu Chen, Sihao Wu, Ling-I Wu, Song Qin, Jingyang Li, Lei Ning, Jianxin Xue, Guoqiang Li
- **分类:** cs.SE
- **摘要:** 代码生成的测试时扩展通常从固定指令采样多个程序探索解空间；本文研究互补方向：**实例级指令空间探索**。观察：很多编码失败源于原提示缺失约束、漏边界情况、或误导性推理路径。提出 **TipCoder**：在代码合成前生成问题专属辅助 tips 的测试时指令提议器——把多轮调试轨迹蒸馏成主动引导，再用**边际效用奖励**的强化学习优化提议器。推理时同时生成基础解与 tip 引导解，用奖励模型事后选择。这个「探索-选择」设计让 tips 暴露额外候选潜力、同时减少不必要引导带来的回归。在评估的代码生成基准与目标 Code LLM 上提供一致的指令级测试时扩展策略，在共享奖励模型选择协议下优于随机采样与通用提示优化基线。
- **关联度:** ★★★★ 代码 agent 的失败常是「提示没问对」——k 的代码生成/接单质量门可借鉴「先生成辅助 tips 再合成」的指令级扩展，而不是无脑多采样；边际效用奖励防过度引导

---

## 九、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.04024](https://arxiv.org/abs/2609.04024v1) | Instruction Duplication | 把过程性指令复制一份的黑盒推理时控制：All-8 诊断 90.22%→93.17%、消除单副本后 30.2% 残余失败；下游系统消费暴露轨迹时价值放大（Answer Engineering 84.2%→97.1%）——低成本、位置敏感、无重训 |
| 2 | [2609.04066](https://arxiv.org/abs/2609.04066v1) | PreferenceEKF | 把主动偏好奖励学习当顺序贝叶斯滤波：扩展卡尔曼滤波在低维参数子空间追踪奖励模型不确定性——D4RL/V-D4RL 上样本效率/运行时/标定优于其他贝叶斯方法，RLHF 主动学习的可扩展不确定性量化 |
| 3 | [2609.02685](https://arxiv.org/abs/2609.02685v1) | DKL | 解耦知识学习：在基座 LLM 上做扩展预训练注入新知识、再与 Instruct LLM 合并权重——避免 RAG 检索失败幻觉与昂贵 IFT，RAG 检索失败场景准确率 54.17→79.26，数据需求远低于 RAFT/PA-RAG |
| 4 | [2609.03920](https://arxiv.org/abs/2609.03920v1) | Value-Preserving Architectures | 多智能体系统的价值保持架构模式：联邦拓扑保隐私、分布式保多元、guard-agent 检测并缓解不公平——架构决策是价值观的载体，可信 MAS 设计从「功能正确」扩展到「价值对齐」 |
| 5 | [2609.03416](https://arxiv.org/abs/2609.03416v1) | Dude | 首个双检测多 agent 论文-代码一致性检测系统：语言/代码粒度不对称导致过度解读与过度上报，粒度对齐协商 + 两阶段显著性过滤——recall/precision 最高 +22.8%、F1 最高 +18.7% |
| 6 | [2609.02177](https://arxiv.org/abs/2609.02177v1) | WeaveMark | 编码负载扩展的多比特 LLM 水印：多比特每 token 扩展 + 软判决纠错码 + 无偏多层重加权——200 token 下 32 比特消息匹配率 89.8%（BiMark 20.8%）、10% 替换攻击下 86.0% vs 30.7%，保文本质量 |
| 7 | [2609.02526](https://arxiv.org/abs/2609.02526v1) | Persona Attributes & Alignment | 人格提示是否改善群体对齐取决于属性选择方法：人类问卷响应变异是混合表现的解释变量——4 项一般社会调查×2 国×6 LLM×20 预测任务，给出何时该用 persona 提示的判断 |
| 8 | [2609.03148](https://arxiv.org/abs/2609.03148v1) | ContextConflict | 六类上下文内知识冲突（事实/推理/时间/粒度/视角/歧义）数据集 5,781 样本：九 LLM 解决不足、机制分析揭示对早期证据的一致性位置偏好——无训练无标签的激活引导法一致提升推理任务准确率与摘要质量 |

---

## 今日要点（主题信号）

1. **「agent 记忆 = 授权策略」成为安全共识**：01836 内生授权洗白（写入器最高 50.2% 虚假权限、执行者 98.6% 照单执行）+ 03450 记录指引操纵检索 + 2607.29167 Memory Provenance Laundering + 2608.01679 Authority Collapse——四条独立证据指向同一结论：**持久记忆的「何时信任、如何验证权限」已是 agent 安全第一性问题**，与 09-04 的 Memory Trust Gap / PlanFence 完全同频，记忆不再只是性能组件。
2. **harness 供应链面被系统化武器化**：03884 HookPry 通过生命周期 hook 更新静默木马化良性插件，7 harness 全沦陷、单 harness 92.5% 成功率、Defender 0% 召回；与 HarnessSafe / HarnessRisk（2608.06984/2608.17597，直接评测 Hermes/OpenClaw）同一研究潮——**harness 自身的 hook/配置更新路径是当前最薄弱防御点**，插件的更新即代码执行。
3. **对齐方法决定「拒绝电路」的形态**：03887 证明训练方法（SFT/推理增强/ORPO）重塑拒绝计算内部结构，且无方法同时满足「不脆弱 + 不损能力 + 可定向编辑」三性质；01663 证明不越狱也能侧信道窃取 agent context——**「直白防护」全线失守，安全评估必须按方法-架构-攻击面三维做**。
4. **RL 后训练收敛为「先拓宽再锐化」两阶段**：04108 证明 OPD-then-RL 一致胜过纯 OPD/纯 RLVR/单步联合（OPD 扩覆盖、RL 在支持集内锐化、验证分是切换信号）；01947 把 GRPO + 学生自采样引入 reranker 蒸馏；03241 FlowBalance 用验证器校准自引导——**「蒸馏打底、验证器校准、RL 锐化」成为可操作配方**。
5. **评估「反身性」进一步发酵**：03436 用重启受控探针把「突破时刻/早期注定」判定为测量伪影（178 单元仅 1 个存活，trace-blind 难度代理 AUROC 0.873 就够）；04047 把重复查询审计协议化为 探索5/确证10/严格15 三档——延续 09-04「测量仪器本身不可靠」主线，**所有基于轨迹/采样的结论都要先过反事实与预算控制**。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Agent Memory Laundering 2609.01836 | web_search arXiv 页 + HuggingFace papers + 社区解读（EleutherAI 系） | ✅ 已确认（50.2%/98.6% 数字属实；同线程 2607.29167/2608.01679 属实） |
| Blind Trust, Bloody Thrust 2609.03884 | web_search arXiv 页 + 关联 HarnessSafe/HarnessRisk 潮 | ✅ 已确认（HookPry 7 harness 全沦陷、92.5% 成功率、Defender 0% 召回；同潮 2609.01222/2608.06984/2608.17597 均评测 Hermes/OpenClaw） |
| Sequential Beats Joint 2609.04108 | web_search arXiv 页 + 关联 OPDVR/CoPD/Demystifying OPD | ✅ 已确认（OPD-then-RL 两阶段；2608.24696/2604.27083/2607.13399 同研究潮属实） |
| 其余 26 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据（API 429 期间） | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要） |

## 可落地行动项

- 🔴 **agent 记忆权限必须带溯源**：01836 的 50.2%/98.6% —— k 给 Hermes/Mnemon 或任何 agent 加持久记忆时，权限/限制/撤销状态绑定源事件 + 有界事件溯源追踪变更，防「记忆洗白假权限」；与 09-04 的 PlanFence/RuleMem 记忆机制合读，把「授权状态」当成记忆的一等字段
- 🔴 **harness 生命周期 hook 当可执行代码审**：03884 证明 hook 配置更新可被静默木马化（Defender 0% 召回）——k 的 Hermes/Codex/Claude Code 插件/技能/钩子检查「谁控制更新路径」，hook 命令一律按可执行代码对待，装插件先看元数据与 hook 绑定
- 🟡 **LLM 判断加反身性检查**：03436 证明「早期信号/突破时刻」多为预算与难度伪影——k 用推理轨迹、采样结果做验收/预测时，先补「重启对照 + 难度基线」再下结论；重复查询审计按 04047 的 探索5/确证10/严格15 分层定迭代数
- 🟡 **后训练默认 OPD-then-RL**：04108 的切换信号 = OPD 验证分——k 做微调/蒸馏/自蒸馏流水线按「先 OPD 扩覆盖 → 验证分触顶切 RLVR 锐化」编排，别单步联合；自引导必须被外部验证器校准（03241）
- 🟢 **待深读**：01836 授权洗白、03887 拒绝电路、04108 OPD-then-RL、02702 Trace as State、01679 TTI survey → 进 core-contributions 候选

---

*本速览由 cron 自动生成：09-05 索引冻结（API 最新 09-03T17:59Z、list 页无 09-05 分组、API 429 限流）→ 09-04 速览只精选 24+12 未盖满同池 → 窗口全量 924 篇比对 covered_ids 得 849 未覆盖 → 标题粗筛 106 → 逐篇抓 abs 页人工精选（21 主条目 + 8 简评，仅保留 LLM/AI Agent 本体相关）→ 关键论文 web_search 交叉验证。数据源 arxiv.org + export.arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
