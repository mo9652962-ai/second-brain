---
aliases:
  - arxiv-2026-08-19-agent-llm
  - arxiv-agent-llm-2026-08-19
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-19
updated: 2026-08-19
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-19 ⚠️ 补全性质（08-17 提交池）

> **检索时间**: 2026-08-19 GMT+8
> **⚠️ 补全性质声明**: arXiv 索引仍停在 08-17 提交池（最新 2608.16889, 08-17T17:59Z），与 08-18 速览同池。08-18 速览从 51 篇关键词命中里精选 17 篇，未盖满同池。本次用 6 类别×08-17 时间窗全量收集（358 篇唯一）交叉比对，补录 08-18 未覆盖的强相关漏网论文。
> **数据源**: [export.arxiv.org](https://export.arxiv.org)
> **统计**: 全量窗口 358 篇 → 已覆盖 98 → 补录 14 篇强相关（Agent/安全 9 + LLM/RL 5）

---

## 一、Agent 执行与安全（补录）

### 1. Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence
- **ID:** [2608.16590v1](https://arxiv.org/abs/2608.16590v1) | [📄 PDF](https://arxiv.org/pdf/2608.16590v1)
- **作者:** Xin Ding, Liang Mi, ... Yunxin Liu, Ting Cao（清华 AIR + 域变换 Z-Trans）| [项目页](https://AIR-embodied-brain.github.io/zetta/)
- **分类:** cs.RO
- **摘要:** 物理智能体的 agentic 路径至今没实现 closed-loop 学习——现有 harness 大多是开环：rollout 时跟固定技能、episode 结束后才反思。Zetta 提出**三个时间尺度分离的闭环**：①Critic-Governed Action Loop 动作频率级治理（frozen VLA 之上的高频运行时 critic，异常即触发 recovery）；②Rollout-Batch Candidate Optimization Loop 聚类+因果诊断失败、用 SGD 式代码空间优化产出候选 critic/recovery；③Validation-Gated Skill Update Loop 只放行提升成功率且能泛化的更新。配套 Z-Infra 首个面向自进化物理智能体的 rollout 基建（agent 逻辑与异构硬件解耦）。LIBERO-Pro 成功率 34.5%→90.8%、RoboCasa 73.6%→93.6%，推理加速 11.1×，涌现机器人「Aha Moment」。
- **关联度:** ★★★★★ 与 ClawGym II 同轴——「harness 从编排工具升级为训练/进化对象」在物理世界落地；三环自进化 + 验证门控与 Hermes 的 skill 沉淀理念同构

### 2. Bounded Agents: Delegation Security for Multi-Agent AI Systems
- **ID:** [2608.15888v1](https://arxiv.org/abs/2608.15888v1) | [📄 PDF](https://arxiv.org/pdf/2608.15888v1)
- **作者:** Xabier Muruaga
- **分类:** cs.AI, cs.CR
- **摘要:** 核心论点：**prompt 注入的安全后果是授权架构问题，不只是模型抗性问题**——agent 无权做的事再怎么注入也做不了。提出 Agentic Principal Chain (APC)：会话级授权状态，沿委派链（principal→sub-agent）追踪并**只收窄、不放宽**权威（signed authorization envelope + delegation budget），用 six authorization checks + **composition closure**（跨会话历史约束非法动作组合）在模型外强制执行。证明 Blast Radius Monotonicity + Composition Soundness。实测 3,154 实例：AgentDojo 四域泄密 75-100%→0%、阻断 544 个 InjecAgent 盗数案例、intent binding 破坏 38.6%→4.0%、操纵 90.5%→12.1%；授权延迟 P99 0.24ms。代码与数据开源。
- **关联度:** ★★★★★ MCP/A2A 时代的委派安全基座；与 sora 的 MCP 工具链 + Hermes 外部动作谨慎审批原则直接相关

### 3. Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation
- **ID:** [2608.16843v1](https://arxiv.org/abs/2608.16843v1) | [📄 PDF](https://arxiv.org/pdf/2608.16843v1)
- **作者:** Jiawei Liu, ... Bowen Xiao
- **分类:** cs.RO
- **摘要:** 具身 agent 越来越多用 foundation model 做感知/推理/规划/动作，安全风险从数字输入传播到物理行为。现有 survey 按 jailbreak/prompt 注入/后门/投毒/对抗样本分类，但没定位**对手最早从哪里进入具身控制环**。本文提出 trust-boundary-centric（首个失守信任边界原则）survey，按输入端→控制闭环→物理执行重新组织攻击面、攻击、防御与评测。
- **关联度:** ★★★★ 把 8-18 速览「安全从 prompt 扩到状态」的信号在具身领域系统化；sora 硬件/机器人兴趣相关

### 4. A Policy Algebra for Trust-Preserving Agentic AI Execution
- **ID:** [2608.16402v1](https://arxiv.org/abs/2608.16402v1) | [📄 PDF](https://arxiv.org/pdf/2608.16402v1)
- **作者:** Bhaskar Tripathi, Anurag Kumar, ...（企业）
- **分类:** cs.AI
- **摘要:** LLM agentic 框架主要优化「能力」（能否推理/检索/调工具/委派/达成目标），但企业执行要求更强性质：**成功结果不可靠，如果它是通过未授权数据访问、扩大委派权限、未经批准的副作用、不可恢复的预算消耗或不完整证据产生的**。把「可靠能力」定义为路径性质——agent 只在能通过一个在理想策略下可准入的动作事件序列完成任务时才算可靠。给出策略代数框架约束 agentic 执行。
- **关联度:** ★★★★ 与 Bounded Agents 同主题（委派安全/策略约束）；补全企业级 agent 执行可靠性视角

### 5. When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable Capability Retrieval
- **ID:** [2608.16502v1](https://arxiv.org/abs/2608.16502v1) | [📄 PDF](https://arxiv.org/pdf/2608.16502v1)
- **作者:** Yiqi Liu, Joseph James, ... Chenghua Lin
- **分类:** cs.LG
- **摘要:** 大规模 agent 越来越依赖检索获取外部能力。在结构化工具/API（tool-backed 可执行技能，agent 必须先检索到才能规划/整合/行动）这个检索门上，**检索层会静默失败**：在 ToolRet 上，一个在某个 source 切片微调的 retriever 会在同 benchmark 的另一 source 切片上崩溃（source-style collapse）。即使能力语料固定，检索层仍可能在跨来源时失效。
- **关联度:** ★★★★ 直指 agent 检索基建的泛化隐患；sora 的工具/技能检索相关（skill 库随来源切片变化可能失效）

### 6. HarnessEval-W: Agentifying the Evaluation of Visual Worlds
- **ID:** [2608.16859v1](https://arxiv.org/abs/2608.16859v1) | [📄 PDF](https://arxiv.org/pdf/2608.16859v1) | [GitHub](https://github.com/mirros-lab/harnesseval-w) | [主页](https://mirros-lab.github.io/HarnessEval-W/)
- **作者:** Weiliang Chen, ... Fangfu Liu（MirroS/MirroS lab）
- **分类:** cs.CV
- **摘要:** 评测不应只给标量分数，还要给**支撑分数的推理链**——对世界模型尤其关键（判断 rollout 的物理/因果/世界状态是否演化正确）。现有 benchmark 全靠暴力算指标，没有可检查的 reasoning chain。HarnessEval-W 把 LLM 生态的 harness 范式搬到世界模型评测：分层 agent 工作流——顶层解释用例上下文→路由到技能→分解成可测子问题→spawn 带诊断工具的子 agent→父 agent 验证证据→汇总裁决，产出透明的 evidence tree。18 个世界模型 330 用例，判断与人类偏好高度一致（Intentional ρ=0.93/Physical ρ=0.87），把 WBench 的 draw rate 从 >50% 压到 <2%，全流程开源为 live benchmark。
- **关联度:** ★★★★★ 评测即推理/证据树 vs 标量分——与 sora「实体验证再下结论」的实证主义一致；也呼应 harness 作为 agent 基建的主线

---

## 二、LLM / RL 补录

### 7. Le Critique: Privileged Value Functions for LLM Reinforcement Learning
- **ID:** [2608.16739v1](https://arxiv.org/abs/2608.16739v1) | [📄 PDF](https://arxiv.org/pdf/2608.16739v1)
- **作者:** Siddarth Venkatraman, Matthieu Dinot, Laurence Aitchison
- **分类:** cs.LG
- **摘要:** LLM 的 RL 算法主要靠方差削减策略区分。GRPO 等分组相对方法靠每 prompt 采样多条 rollout 降梯度方差，但只给 sequence-level credit，且被 straggler rollout 拖慢、增加 off-policyness。学到的 value function 理论上两样都解决（token-level advantage、无需大分组），但工程成本高、critic-less 方法又成功。本文研究 privileged value function 路径，给 LLM RL 提供中间地带。
- **关联度:** ★★★★ RL 后训练前沿——与 8-18 的 ClawGym II（harness 上 RL）互补，覆盖 token-level credit 与吞吐痛点

### 8. Policy Iteration with Human Feedback: Bringing Post-Training RL to In-context Learning
- **ID:** [2608.16831v1](https://arxiv.org/abs/2608.16831v1) | [📄 PDF](https://arxiv.org/pdf/2608.16831v1)
- **作者:** Minh-Ha Nguyen, Cathy Shyr
- **分类:** cs.AI, cs.CL
- **摘要:** 生成式预训练建立了可复用任务表征；in-context learning 让固定模型从指令/示范自适应。PIHF 在此基础上用广义策略迭代的 evaluate-and-improve 循环：以预训练 LM 为执行基底，把持久化修订移到 versioned 自然语言策略+工具集，LM critic 与临床专家审完整面板推理。把后训练 RL 的机制带进 in-context 设定，无需权重更新。
- **关联度:** ★★★★ 记忆/策略外置而非改权重——与 Hermes 的版本化 skill 演进理念一致

### 9. STAGE: Controlled Objective Admission for Multi-Preference LLM Alignment
- **ID:** [2608.16553v1](https://arxiv.org/abs/2608.16553v1) | [📄 PDF](https://arxiv.org/pdf/2608.16553v1)
- **作者:** Yongqi Tong, ... Jianshe Li
- **分类:** cs.CL
- **摘要:** 多偏好对齐常被当成标量化（组合 reward 维度再优化），但漏了时序决策：**每个偏好维度何时进入策略优化**？STAGE 是 stability-guided active-set controller（受控目标准入）：从小的 active set 起步、保留已准入目标、当 reward-deviation 门限表示低偏差或 patience budget 耗尽时扩展；probing 阶段估难→易顺序，自适应加权强调表现不足的 active 目标。
- **关联度:** ★★★★ 对齐/奖励工程的可控时序准入——比一次性 scalarize 更稳

### 10. PCA-guided Activation Scaling for Monotonic Bidirectional Control over LLM Sycophancy
- **ID:** [2608.16650v1](https://arxiv.org/abs/2608.16650v1) | [📄 PDF](https://arxiv.org/pdf/2608.16650v1)
- **作者:** Zheng Chen, ... Emmanuele Chersoni, Bo Li
- **分类:** cs.CL
- **摘要:** LLM 有 sycophancy（迎合用户信念不管事实）。但全消除会矫枉过正。有效控制要既能降也能升 sycophancy、且效果可预测渐进。现有方法无法保证跨模型/数据集的单调双向关系。PAS 用激活转向：PCA 分解 residual stream，按主成分缩放，实现 sycophancy 的单调双向控制。
- **关联度:** ★★★ 激活转向的精细控制——sora 关注因果/可解释性的备选工具

### 11. Proteus: Incremental Memory Activation for Long-Context Sequence Modeling
- **ID:** [2608.16844v1](https://arxiv.org/abs/2608.16844v1) | [📄 PDF](https://arxiv.org/pdf/2608.16844v1)
- **作者:** Reza Bayat, Ali Behrouz, Vahab Mirrokni, Aaron Courville
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** 长上下文记忆模型大多整条序列暴露静态 memory——早期 token 没压缩压力，占用过多自由度「污染」记忆态，留给后续上下文容量不足、存储与新来内容干扰。Proteus 提出**增量记忆激活**范式：有效容量随序列渐进启用，缓解早期 token 的 memory 占用与干扰。
- **关联度:** ★★★★ 长上下文记忆体系节流——与 8-18 的 QUMem/FTA-Mem 记忆精细化同向，但聚焦 memory 激活时机

### 12. When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented Generation
- **ID:** [2608.16515v1](https://arxiv.org/abs/2608.16515v1) | [📄 PDF](https://arxiv.org/pdf/2608.16515v1)
- **作者:** Haolin Jin, Pengyue Yang, Huaming Chen
- **分类:** cs.AI, cs.CL
- **摘要:** RAG 靠外部证据 grounded 生成，但引入信任问题：检索到的上下文可能有用、无关甚至误导。现有系统对检索证据用固定信任策略——over-trust 错误上下文或 underuse 用户要跟的上下文。IGD 是在解码期按用户意图仲裁「检索上下文 vs 参数记忆」的框架。
- **关联度:** ★★★★ RAG 信任/意图仲裁——sora 知识吸收/检索管道可借鉴的意图感知路由

### 13. DSPrompt: Dynamic Soft Prompt Defense Against M-RAG Corruption
- **ID:** [2608.16536v1](https://arxiv.org/abs/2608.16536v1) | [📄 PDF](https://arxiv.org/pdf/2608.16536v1)
- **作者:** Chang Liu, ... Kai Zhou, Bin Xiao
- **分类:** cs.CL
- **摘要:** 多模态 RAG 易受对抗攻击：恶意数据被构造出与良性条目向量对齐的 embedding，骗过检索产出有害输出。现有防御多在 query 时做、推理开销大、泛化差、假设特定攻击分布。DSPrompt 用动态 soft prompt 防御 M-RAG 污染。
- **关联度:** ★★★★ M-RAG 安全与 12 的「检索可信」互补；sora 检索增强系统的鲁棒性参考

### 14. Don't Drop the BATON: Long-Horizon Robot Manipulation via Agentic Subtask Exploration and Transition-aware Memory
- **ID:** [2608.16889v1](https://arxiv.org/abs/2608.16889v1) | [📄 PDF](https://arxiv.org/pdf/2608.16889v1)
- **作者:** Bingxin Xu, Yuzhang Shang, Emilio Ferrara
- **分类:** cs.AI, cs.RO, cs.CV
- **摘要:** 长时程机器人操纵把多个接触丰富技能串成多阶段任务。VLA 模型单个技能越来越强，但串联仍失败：错误超出策略校正能力复合、一个子任务静默约束下一个。一个有效配方是 frozen VLA + LLM agent 负责：语言规划、用解析原语在自由空间移动、只在接触丰富段调 VLA、把适应写进语言记忆。对长时程会断：能力来自整体/局部与记忆过渡的权衡。
- **关联度:** ★★★★ 与 1（Zetta）、8-18 的 ClawGym II 同属「VLA+LLM agent harness」主线；sora 机器人兴趣相关

---

## 本周值得关注的主题信号（补全视角）

1. **harness 成为「进化对象」闭合成环**：Zetta（物理三环自进化）、ClawGym II（数字 harness 上 RL）、SHAPER（skill+harness 共同进化）——harness 从编排工具升级为可训练/可进化的主体，这是 08-17 池补录后更强的信号。
2. **agent 安全=授权架构而不是模型防御**：Bounded Agents（APC 组合闭包）、Policy Algebra（可靠能力=路径性质）、Embodied 安全（trust-boundary）——三条独立佐证「防注入靠最小授权 + 模型外强制」，与 8-18 的 State-Semantic Injection 呼应。
3. **评测从标量分走向证据树/推理链**：HarnessEval-W 把评测当 agentic reasoning 任务，产出透明 evidence tree——「评测可信靠可检查的推理而非分数」成新范式。
4. **RL 后训练分化出 critic/value 与 in-context 两路**：Le Critique（privileged value function vs GRPO 序列级）、PIHF（把后训练 RL 带入 in-context）——token-level credit 与无需权重更新的对齐是两条互补路径。
5. **检索可信成为 RAG/能力检索的根问题**：When Context Misleads（意图仲裁）、DSPrompt（防 M-RAG 污染）、Tool-Backed Skill Retrieval 崩坍（source-style collapse）——检索层从「能召回」到「可信召回」的可靠性补课。

---

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
