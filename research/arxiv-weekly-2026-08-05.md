---
aliases:
  - arXiv Weekly Roundup 2026-08-05
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - paper-review
  - agent-security
  - agent-memory
created: 2026-08-05
updated: 2026-08-05
status: processed
source: https://arxiv.org/
domain: research
---

# arXiv Weekly Roundup — AI Agent & LLM Papers

**Date:** 2026-08-05 | **Week 32**  
**Papers:** 27 new relevant papers (cs.AI/cs.SE/cs.CR/cs.CL/cs.LG 等)

---

## 📄 Paper Highlights

### [2608.02499v1] SWE-Touch: Benchmarking Coding Agents When Users Touch the Code

- **Authors:** Yuqiao Tan, Jinxiang Meng, Fangyu Lei, Minzheng Wang, Shizhu He, Jun Zhao, Kang Liu
- **Published:** 2026-08-03
- **Categories:** cs.SE, cs.AI, cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2608.02499v1) | [PDF](https://arxiv.org/pdf/2608.02499v1)
- **💡 短评:** 编码 agent 共享工作区评测——真实开发中用户会边看边改代码,SWE-chat 数据 59% 会话含用户改动;Counter-Edit 让 9 模型在 SWE-bench Verified 平均掉 7.7 分,直击 agent 状态感知短板

**Abstract:**  
Real-world software development requires coding agents to operate in shared workspaces where users may inspect and modify code during an ongoing task, yet existing repository-level benchmarks typically evaluate agents working alone or restrict user participation to messages. This leads us to ask: how do coding agents understand and respond to code changes in a shared workspace? We introduce SWE-Touch, a framework that stress-tests this setting through validated Counter-Edits: plausible edits to task-relevant code that conflict with task completion. SWE-Touch mines task-critical regions from multiple repair trajectories, uses a separate User Patch Generator to construct the edits, and injects them with contextual user messages when agents reach the relevant code. We evaluate nine coding models on SWE-bench Verified, with additional experiments on longer-horizon tasks from SWE-Bench Pro and DeepSWE. Counter-Edit lowers average resolve rate by 7.7 percentage points on SWE-bench Verified, with degradation also persisting on both longer-horizon benchmarks. Trajectory analysis links these failures to limited awareness of the evolving workspace: agents may retain conflicting code or replace it without sufficiently re-inspecting the repository and validating the revised code with targeted tests. These findings show that strong autonomous performance does not yet ensure the state awareness and adaptive behavior needed for shared-workspace collaboration, and point to detecting workspace changes, reconciling conflicting edits with the task, and verifying the affected behavior as key capabilities for future optimization.

---

### [2608.02464v1] Real-Time Detection and Repair of LLM Agent Failures

- **Authors:** Sunny Dubey
- **Published:** 2026-08-03
- **Categories:** cs.AI, cs.LG, cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2608.02464v1) | [PDF](https://arxiv.org/pdf/2608.02464v1)
- **💡 短评:** agent 失败实时检测+自动修复:不靠第二 LLM 裁判,纯步级遥测+单类 ESN 检测器(~200μs/步),回滚重跑恢复 45% 失败、任务成功率 52%→73%——Hermes 可靠性体系可直接借鉴(对应 cron 心跳/静默失败检测)

**Abstract:**  
LLM agents fail mid-episode -- they loop, cascade tool errors, drift off goal, fabricate results, or silently absorb corrupted content -- and the standard remedy, judging every step with a second LLM, costs more than the agent itself. We ask how much detection is achievable from observable step telemetry alone, using monitors costing microseconds per step and trained only on healthy runs. On 2,823 committed agent episodes across three frameworks, three local models (qwen2.5 7b/3b, llama3.1 8b) and a commercial API (gemini-2.5-flash), a one-class echo-state-network ensemble with CUSUM alarms detects 0.71 of failures at a 5% false-alarm budget (AUROC 0.872). Its advantage over a memoryless baseline is a monotone function of post-onset horizon (+0.09 at <=3 steps, +0.40 at >=9), predicting its own failure region out of sample on AFTraj-2K. Ranking transfers with no retraining to two corpora from other groups (AFTraj-2K 0.745, ATBench 0.779). Monitors carry two burdens: a per-deployment healthy null (they do not transfer -- AUROC 0.527 cold against 0.885 recalibrated) and a residual false-alarm rate. We add a layer carrying neither: deterministic verification, which recomputes a run's stated total from the tool results it actually received and confirms every required call was made. Head-to-head it catches 60% of failures (96% with the coverage check) at 0 of 63 false positives against the monitor's 54% at 17%, transfers unchanged to llama3.1:8b (110 of 110 at 0 of 10), and trips on 0 of 1825 healthy episodes. Detection is then closed into repair: each flagged run is rolled back and re-run live, recovering 45% of failures against a 16% resampling control (p=0.0005) and lifting task success from 52% to 73% for about one extra model call per run. The system runs at ~200 microseconds per step, three orders of magnitude below a judge call. Code, traces and results are released.

---

### [2608.02508v1] RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States

- **Authors:** Yi Yang, Zhennan Chen, Yihong Zhuang, Tiehan Fan, Yinan Chen, Jian Li, Jian Yang, Ying Tai
- **Published:** 2026-08-03
- **Categories:** cs.LG, cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2608.02508v1) | [PDF](https://arxiv.org/pdf/2608.02508v1) | [Code](https://github.com/YOUNG-fnxm/RoMeRL)
- **💡 短评:** 自进化 agent 记忆的降阶效用状态,破解记忆-奖励陷阱(无关记忆被共同检索误得高效用):Cold-Q 降 80%、反馈密度约 6 倍、记忆体积减 84%、LLM 调用省 21%——第二大脑记忆体系的核心算法候选

**Abstract:**  
Learning-based memory systems for self-evolving LLM agents face two tightly coupled challenges. First, trajectory-indexed utilities grow with the interaction history, thereby dispersing limited feedback over an ever-expanding state space. Second, because trajectory-level rewards are jointly assigned to co-retrieved memories, irrelevant experiences may receive misleading utility updates and consequently enter the memory-reward trap. To address these challenges, we introduce Reduced-Order Memory Reinforcement Learning (RoMeRL), which represents the growing trajectory-indexed utility space using a fixed-dimensional per-task memory state factorized by outcome polarity and memory dynamics. RoMeRL incorporates new experiences through a fixed set of semantic coordinates whose contents are updated or replaced over time, thereby concentrating feedback over a bounded utility support. Theoretically, we show that this reduced-order parameterization increases the average feedback received by each utility coordinate and characterize the steady-state occupancy of erroneous coordinates under a generic coordinate-transition model. Empirically, across ALFWorld and LifelongAgentBench, RoMeRL improves task performance, reduces the Cold-Q ratio by 80.0%, increases feedback density by approximately 6.0 times, reduces the maintained memory size by 84.4%, and cuts LLM calls by 21.1%. These results show that reduced-order utility states support efficient self-evolving agent memory while limiting persistent reward contamination. Code is available at: https://github.com/YOUNG-fnxm/RoMeRL

---

### [2608.02515v1] LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference

- **Authors:** Zhichen Liu, Ruihan Sun, Hengjie Yang, Zipeng Wu, Zhaohan Chen, Xiaofan Zhang, Yang Xu
- **Published:** 2026-08-03
- **Categories:** cs.CL, cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2608.02515v1) | [PDF](https://arxiv.org/pdf/2608.02515v1)
- **💡 短评:** 内禀记忆状态延续性:固定容量记忆态生命周期独立于活动上下文,支持证据移出窗口仍能作答(LongMemEval 验证)——长运行 agent 的"状态连续性"抽象,比 RAG/摘要更进一步

**Abstract:**  
Long-running assistants and agents consume interaction streams that eventually outgrow the context. Existing context retention, summarization, and retrieval preserve access to selected history, but do not provide a persistent state over the full lifecycle when working context changes. We formulate this missing inference capability as *state continuity under context turnover*: carrying computation forward through a fixed-capacity memory state whose lifetime is independent of the active context. We introduce an intrinsic memory method, **LiveMem**, which augments a pretrained full-attention LLM with a memory state that preserves the historical information over the whole lifecycle while the main attention path retains a bounded KV window. Context turnover and memory state maintaining, memory-oriented post-training, and state-aware serving jointly make this memory state load bearing after its originating tokens are released. Our experiments show that LiveMem achieves leading overall performance among evaluated systems and other intrinsic memory methods. Experiments on LongMemEval show that LiveMem is able to answer the question based on the memory state, even when the supporting evidence has been removed from the current context, and evidence-distance analysis shows that useful information persists beyond the active window. LiveMem thus establishes state continuity as a distinct and complementary abstraction for continual LLM inference.

---

### [2608.02518v1] Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation

- **Authors:** Natalie Isak, Matthew Dressman
- **Published:** 2026-08-03
- **Categories:** cs.AI, cs.CY
- **Links:** [Abstract](https://arxiv.org/abs/2608.02518v1) | [PDF](https://arxiv.org/pdf/2608.02518v1)
- **💡 短评:** 跨会话能力累积检测:攻击者把有害目标拆成无害子任务跨会话执行(agent 无状态但攻击者有状态),按用户维度聚合"能力位向量"而非逐会话检查——agent 安全新威胁模型,承接 Cross-Session Threats(2604.21131)

**Abstract:**  
The most capable AI deployments are not single models but ensembles of specialized agents that delegate and act in coordination. This architecture unlocks powerful new capabilities, and it also introduces risks that existing frameworks for monitoring, detection, and mitigation were not designed to address. Most state-of-the-art AI abuse detection literature focuses on single-turn or multi-turn (single-session) threat models. This leaves a critical gap: an attacker can decompose a harmful goal into innocuous-looking units and execute each in isolated agentic sessions. The agent is stateless between conversations, but the attacker is not. This asymmetry allows for cross-session trajectories that are effective at evading detection. Our contributions are twofold. First, we demonstrate cross-session goal decomposition as an evasion technique, showing it may elicit more harmful capability than equivalent single-session or multi-turn attacks. By capability we mean an artifact produced at one step of an objective, evidenced by what an interaction produced (model responses and tool-call results), and composable with capabilities accrued elsewhere into a harmful whole. Second, we propose Magnet: an efficient and robust detection approach that models relevant capabilities accrued over time and across agentic conversations, aggregated at a higher-level correlator (in this case, a user ID) rather than per-conversation state. The main challenge is assembling the evidence bundle Magnet reasons over. The incriminating artifacts may be needles scattered through a haystack of benign sessions that are individually harmless, dangerous only once collected. Rather than searching the haystack straw-by-straw (i.e. per-session inspection), Magnet does what its name implies: it attracts the relevant needles out of the hay, across sessions and across time, into a compact evidence bundle a detector can act on.

---

### [2608.02582v1] ACEM: A Cost Estimation Model for Agentic Software Engineering

- **Authors:** Mohammad El-Ramly
- **Published:** 2026-08-03
- **Categories:** cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2608.02582v1) | [PDF](https://arxiv.org/pdf/2608.02582v1)
- **💡 短评:** agentic 软件工程成本模型:LLM token + HITL 监督 + 基建三维成本;Revision Factor(拒绝重试开销)/Context Factor(上下文累积)/HITL Intensity Score 四级监督分级——闲鱼 AI 接单定价的量化工具雏形

**Abstract:**  
Traditional software cost estimation models, such as COCOMO II, Function Points, and Story Points, assume that development effort is primarily driven by human labor in design, coding, and testing. Agentic software engineering, where autonomous AI agents perform substantial implementation work and humans focus on planning, specification, and validation, challenges this assumption. New cost dimensions arise: large language model (LLM) token consumption across agent actions, Human-in-the-Loop (HITL) oversight effort, and infrastructure costs for agent orchestration and tooling. These costs are nondeterministic: identical tasks may consume different tokens, follow divergent reasoning paths, and require varying human correction, phenomena absent in traditional development. A new framework is needed to bridge standard sizing metrics with this cost structure. This paper proposes ACEM (Agentic Cost Estimation Model), which decomposes total agentic development cost into three additive dimensions: LLM, HITL, and infrastructure cost. ACEM introduces three constructs for agentic dynamics: the Revision Factor (RF), modeling token overhead from output rejection and retries; the Context Factor (CF), capturing rising token consumption as context accumulates; and the HITL Intensity Score (HIS), a four-level oversight classification scheme. It further maps Use Case Points, Story Points, and Function Points to estimated token consumption, enabling organizations to reuse existing project-scoping data for agentic cost forecasting. ACEM is presented as a fully specified model structure and calibration methodology, with constants left symbolic pending empirical grounding. As an early-stage proposal, it invites the research community to calibrate, test, and extend the model through real project data.

---

### [2608.02407v1] Antares: Foundation Models for Agentic Vulnerability Localization

- **Authors:** Supriti Vijay, Aman Priyanshu, Didier Chapoteau, Arthur Goldblatt, Jianliang He, Kimia Majd, Fraser Burch, Baturay Saglam, Takahiro Matsumoto, Zhuoran (et al.)
- **Published:** 2026-08-03
- **Categories:** cs.CR, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.02407v1) | [PDF](https://arxiv.org/pdf/2608.02407v1) | [Technical Report](https://cisco-foundation-ai.github.io/antares/technical-report.pdf)
- **💡 短评:** Cisco 出品:350M-3B 紧凑模型做 agentic 漏洞定位,基于 IBM Granite,SFT+可验证奖励 RL,3B 接近 GPT-5.5 且优于 200 倍大的开源模型;单 H100 500 任务 15 分钟(<$0.002/任务)——低成本安全 agent 范例

**Abstract:**  
Vulnerability localization is a fundamental step in software security, requiring models to reason over large codebases and iteratively identify vulnerable implementations. We present Antares, a family of compact language models (350M, 1B, and 3B parameters) for agentic vulnerability localization. Based on IBM Granite base models, Antares is trained through a two-stage pipeline that combines supervised fine-tuning on cybersecurity reasoning and repository exploration data with reinforcement learning from verifiable rewards over vulnerable repositories. Across extensive evaluations, Antares-3B approaches GPT-5.5 while outperforming open-weight models over 200x larger in size. The Antares family further enables fast, low-cost local inference, completing a full 500-task evaluation sweep in approximately 15 minutes on a single H100 GPU, corresponding to an amortized evaluation time of under 2 seconds and less than $0.002 per task.

---

### [2608.02569v1] AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies

- **Authors:** Qiushi Lin, Chaojie Zhang, Íñigo Goiri, Aditya Akella, Ricardo Bianchini, Jovan Stojkovic
- **Published:** 2026-08-03
- **Categories:** cs.AI, cs.DC, cs.OS
- **Links:** [Abstract](https://arxiv.org/abs/2608.02569v1) | [PDF](https://arxiv.org/pdf/2608.02569v1)
- **💡 短评:** 数据中心控制策略的 agentic 生成框架:任务编译器把自然语言目标编译成可机器检查的规格,进化搜索+扩散模型+代理模型扩展 LLM 视野——"agentic 系统工程化(formal/transferable/systematic)"范式

**Abstract:**  
The efficiency of a datacenter rests on its control plane policies. Designing these policies is increasingly hard: the hardware-software stack grows fast, the design space is vast and interdependent, and prototyping a single policy takes months. Agentic AI promises to automate this search. Off the shelf, however, it falls short on three fronts. It is not formal: with no structured, searchable statement of the problem, the search has little structure to exploit and hard constraints are not guaranteed. It is not transferable: each task is solved from scratch, so nothing learned on one task carries to the next. Finally, it is not systematic: relying on the LLM as the sole source of candidates, it explores a narrow slice of the design space and settles into local optima. We introduce AtumAI, a framework that generates datacenter control-plane policies with agentic AI, making the process formal, transferable, and systematic. From a goal stated in plain language, AtumAI autonomously proposes, tests, and refines candidate policies until one satisfies the request. It does so through two components. The Datacenter Task Compiler automates problem formulation: it compiles the request into a formal, machine-checkable, and searchable specification of the task's objectives, constraints, decision variables, and evaluation methodology. The Evolutionary Design Discovery Loop then searches this specification, expanding the search beyond the LLM itself via a diffusion model, an evolutionary algorithm, and a surrogate model. Together, they reduce onboarding a new task from months of engineering to writing its description. We evaluate AtumAI on three control-plane tasks with distinct problem scopes, design spaces, and trade-offs: workload placement, resource scaling, and power management. Across all tasks, the policies generated by AtumAI consistently outperform expert-engineered baselines.

---

### [2608.02291v1] TreeCredit: Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning

- **Authors:** Yiqing Liu, Zihao Wang, Hantao Yao, Wu Liu, Yongdong Zhang
- **Published:** 2026-08-03
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.02291v1) | [PDF](https://arxiv.org/pdf/2608.02291v1)
- **💡 短评:** 共享前缀信用分配:用状态匹配的后缀信用替代轨迹级归因,训练轻量成对状态路由器——多智能体推理在精度小幅提升下大幅降本(六个推理基准更好的 accuracy-cost 权衡)

**Abstract:**  
Multi-agent reasoning (MAR) improves reasoning reliability through iterative solution exchange and refinement. Existing adaptive MAR methods typically learn routing decisions from query-level labels or trajectory-level returns, but such coarse supervision cannot accurately estimate the state-conditioned utility of individual operators in multi-step collaboration. We propose TreeCredit, a shared-prefix credit assignment framework for efficient adaptive MAR. Its core insight is to estimate operator utility through state-matched downstream comparisons, rather than directly attributing trajectory-level outcomes to preceding decisions. TreeCredit constructs shared-prefix collaboration trees by expanding candidate operators from the same intermediate state and assigns each state--operator pair a correctness-prioritized suffix credit based on the terminal correctness and cumulative additional cost of its complete continuation. These structured credits are converted into state-local operator preferences to train a lightweight pairwise state router, which dynamically selects the next admissible operator during inference. Experiments on six reasoning benchmarks show that TreeCredit modestly improves accuracy while substantially reducing inference cost, achieving a better accuracy--cost trade-off than representative MAR methods.

---

### [2608.01805v1] CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for Embodied Multi-Agent Cockpits

- **Authors:** Wei Wang, Shuanghe Liu, Zhu Zhuo, Jiaqi Zhong, Xiaozhao Zhao, Xiaojie Zuo, Jie Su
- **Published:** 2026-08-03
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.01805v1) | [PDF](https://arxiv.org/pdf/2608.01805v1)
- **💡 短评:** 依赖图分层归因:交互 DAG 依赖距离替代位置窗口+多通道证据+安全加权共识,诊断"正确性坍塌"(任务级准确掩盖过程级失败)——安全关键多智能体故障归因新范式,附 CockpitBench(ISO 26262 ASIL 标注)

**Abstract:**  
LLM multi-agent systems suffer from Correctness Collapse, where high task-level accuracy conceals severe process-level failures. This is especially hazardous in safety-critical embodied settings such as automotive cockpits, where lexically correct utterances may trigger dangerous physical operations. Existing attribution methods rely on text traces alone, missing dependency structure, multi-channel evidence, and safety-aware evaluation. We introduce CockpitHAT, a hierarchical attribution framework that replaces positional windows with dependency-distance thresholds from interaction DAGs, integrates multi-channel evidence via an embodied adapter, and applies a safety-uplift to high-risk failures during confidence-weighted analyst consensus. We further release CockpitBench, a benchmark of 212 annotated failure traces spanning dialogue, vehicle-state, environmental, and memory channels, each labeled with ISO 26262 ASIL severity via three-expert consensus. On the public Who&When benchmark, CockpitHAT achieves agent-level / step-exact accuracies of 77.9% / 37.8% on the Hand-Crafted split and 86.5% / 46.0% on the Algorithm-Generated split, surpassing the text-only SOTA ECHO by up to 17.6 / 16.7 points. On CockpitBench, it attains 78.3% agent-level and 38.2% step-exact accuracy. These results establish dependency-aware, multi-channel, risk-calibrated attribution as an effective paradigm for reliable failure diagnosis in real-world embodied LLM multi-agent systems.

---

### [2608.01719v1] MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication

- **Authors:** Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, Hankai Liu
- **Published:** 2026-08-03
- **Categories:** cs.CR, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.01719v1) | [PDF](https://arxiv.org/pdf/2608.01719v1)
- **💡 短评:** 最小必要通信协议:类型化语义去分类,披露绑定接收方/用途/转发/生命周期/日志/记忆作用域,参考监视器执行——多智能体隐私通信的实用边界(两骨干 MAGPIE 实测)

**Abstract:**  
Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs appear innocuous. Existing privacy prompts, redaction methods, and source-level access controls restrict surface content or data access, but do not specify what a legitimately informed agent should disclose or how that disclosure may be reused downstream. We introduce Minimum-Necessary Communication (MNC), a typed semantic-declassification protocol that selects a task-sufficient disclosure from an application-authored candidate family and binds it to explicit recipient, purpose, forwarding, lifetime, logging, and memory scopes. A reference monitor enforces these scopes across subsequent operations, while a history-aware extension accounts for inference risk accumulated over repeated disclosures. Controlled semantic-join, memory, probing, and longitudinal experiments show that conventional defenses can preserve protocol-level utility while exposing substantial additional inference signal. Under identical receipt text, MNC preserves authorized delivery while blocking unauthorized forwarding, logging, durable storage, and retrieval after expiration that a text-only semantic declassifier permits. Two-backbone MAGPIE executions further show that mediated disclosures propagate through subsequent planning, tool use, coordination, and memory retrieval. These results support scope-bound semantic declassification as a practical communication boundary for private LLM-agent systems.

---

### [2608.01791v1] PICopilot: An LLM-based Agentic Framework for Assisting Photonic Integrated Circuit Design via Script Generation

- **Authors:** Xiaohan Jiang, Zeyu Li, Wei Zhang, Jiang Xu
- **Published:** 2026-08-03
- **Categories:** cs.ET, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.01791v1) | [PDF](https://arxiv.org/pdf/2608.01791v1)
- **💡 短评:** 光子 IC 设计 agent:自然语言→设计脚本,多智能体+反馈机制+定制 RAG,48 任务全完成、比 GPT-5 通用 RAG 多解 21 题——硬件设计自动化,与 sora 的 PCB/工程自动化方向直接呼应(JLC MCP 可叠加同类编排)

**Abstract:**  
The rapid development of photonic integrated circuits (PICs) is shifting the design flow from traditional graphical user interface (GUI)-based methods to script-based methods for higher flexibility, portability, and maintainability. However, script-based design introduces new challenges, requiring designers to possess additional proficiency in tool application programming interfaces (APIs) and programming. It also demands greater effort and time because it is inherently less intuitive and more complex than GUI-based methods. As PICs grow in scale and complexity, the productivity gap between design needs and manual scripting capabilities continues to widen. To address this gap, we introduce PICopilot, the first large language model (LLM)-based agentic framework that assists in PIC design via automated design script generation from natural language instructions. PICopilot leverages a multi-agent architecture with a feedback mechanism and a specifically designed retrieval-augmented generation (RAG) pipeline, achieving a high success rate and reliability. Experimental results on a benchmark of diverse PIC scripting tasks demonstrate that PICopilot successfully completes all 48 tasks and outperforms other LLM-based approaches without incurring substantial extra latency or cost, even solving 21 more tasks than the advanced GPT-5 model with a general RAG pipeline.

---

### [2608.02553v1] A Taxonomy of Cognitive Capability Gaps in Generative and Agentic AI

- **Authors:** Taye Akinrele, Sindhuja Penchala, Noorbakhsh Amiri Golilarz, Sudip Mittal, Shahram Rahimi
- **Published:** 2026-08-03
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.02553v1) | [PDF](https://arxiv.org/pdf/2608.02553v1)
- **💡 短评:** 认知能力差距分类综述:五维(持久状态建模/目标自主/自我监控/环境交互/学习适应)+ACIA 架构草图+认知评测方向——评估认知 AI 进展的统一框架,可对照第二大脑系统查缺

**Abstract:**  
Cognitive AI seeks to move beyond language generation and autonomous task execution toward systems capable of sustained reasoning, adaptive behavior, persistent memory, and self-regulation. While generative and agentic AI have demonstrated impressive capabilities across a wide range of tasks, many fundamental cognitive functions remain fragmented or weakly developed, limiting reliable operation over extended time horizons. This paper presents a taxonomy-driven survey of the major cognitive capability gaps that continue to constrain the development of Cognitive AI. The literature is organized around five dimensions: persistent state modeling, goal-directed autonomy, self-monitoring and control, environment interaction, and learning and adaptation. For each dimension, we review recent advances, identify recurring limitations, and discuss open research challenges. Building on these insights, we outline a conceptual Adaptive Cognitive Intelligence Architecture (ACIA) and examine emerging directions in cognition-centric evaluation. The proposed taxonomy provides a unified framework for organizing existing research, identifying unresolved challenges, and guiding the design of future cognitively capable systems. Together, the taxonomy, architectural perspective, and evaluation framework offer a roadmap for advancing AI systems that exhibit more reliable long-term reasoning, adaptive decision-making, and continual learning. The survey highlights key research opportunities toward more adaptive, reliable, and cognitively capable AI systems, providing a foundation for future progress toward Cognitive AI and, ultimately, Artificial General Intelligence (AGI).

---

### [2608.02441v1] Agentic Commerce World: An Auditable and Verifiable Environment for Vibe Commerce

- **Authors:** Shicheng Fan, Mingdai Yang, Duohao Wang, Canyu Chen, Yongfeng Zhang, Hua Wei, Manling Li, Julian McAuley, Kun Zhang, Philip S. Yu, Kejing Yu, Zhiwei L (et al.)
- **Published:** 2026-08-03
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.02441v1) | [PDF](https://arxiv.org/pdf/2608.02441v1)
- **💡 短评:** vibe commerce 评测环境:买方/卖方 agent 在共享市场独立博弈,VCP 协议校验动作+记录交互(可审计),200+60 任务、785K 商品目录——电商 agent 审计基准,过程级证据优于终态

**Abstract:**  
In vibe coding, people describe software in natural language and delegate implementation to AI agents. By analogy, vibe commerce allows people to express buying or selling goals in natural language and delegate the corresponding tasks to agents. Commerce, however, requires independently controlled Buyer and Merchant agents to interact in a shared market while preserving their private objectives and distinct authority. We introduce Agentic Commerce World (ACWorld), an environment for evaluating such agents across ongoing transactions. Through its Vibe Commerce Protocol (VCP), ACWorld validates agent actions before updating shared transaction state and records the resulting interactions, making agent behavior auditable and evaluation reproducible. The ACWorld Benchmark contains a 200-task capability-coverage track and a 60-task large-catalog track that searches 785,022 transactable listings. Across ten models, mean scores range from 65.9% to 85.6% and from 56.1% to 91.4%, respectively. Our analysis shows that process-level evidence is necessary: final state alone can miss evaluated errors, incomplete trajectories still retain useful process signals, and large-catalog tasks expose bottlenecks across stages.

---

### [2608.02444v1] ParEvalLayer: When Partial LLM-Agent Evaluations Support a Decision

- **Authors:** Wei-Jung Huang, Bonan Shen
- **Published:** 2026-08-03
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2608.02444v1) | [PDF](https://arxiv.org/pdf/2608.02444v1)
- **💡 短评:** 部分评估决策层:读配对结果+预选比较策略,输出"更好/不足/需更多证据/弃权";公开基准仅 15-25% 任务即达与完整评估相同结论——agent 评测性价比方法论,回应"跑一半就想下结论"的常见误用

**Abstract:**  
LLM-agent evaluations often produce task outcomes long before the full benchmark run is complete. A partial score is tempting to report, but it does not show whether the observed tasks support the same conclusion as the completed evaluation. Early tasks can omit important parts of a benchmark, running cheaper tasks first can distort the observed sample, and a rule that decides only easy pairs can appear accurate while leaving many comparisons unresolved. We introduce ParEvalLayer, a decision layer that reads paired outcomes for two agent systems and a comparison policy chosen in advance. For each partial run, it records whether the tested agent system is better by the required amount, is not better by that amount, needs more evidence, or should abstain. We evaluate ParEvalLayer by replaying completed public benchmark data as if each evaluation had stopped earlier. At each point, ParEvalLayer applies the policy using only the outcomes observed so far; if it reaches one of the two comparison judgments, we check whether that judgment matches the completed data for the same system pair. With the main comparison rule, three of the public benchmarks reach the same decision as the completed evaluation after observing only 15% to 25% of task outcomes. Other benchmarks require more task outcomes. This variation shows why a partial score alone is not enough: reports should also state the decision rule and how many comparisons remain without a decision.

---

## 📋 更多值得关注（简评）

| # | Paper | 一句话 |
|---|-------|--------|
| 1 | [2608.02583v1] UEmbed: Unified Sparse and Dense Multimodal Embeddings | decoder-only 单前向同时产出稀疏+密集表示(2B/4B/9B 开源),MMEB-v2 领先,agentic 检索基建 |
| 2 | [2608.02602v1] AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling | 连续潜空间扩散语言模型:保留高容量可解码文本潜表示而非压缩,OpenWebText/XSum 领先(华为 Ascend NPU 训练) |
| 3 | [2608.02560v1] PRECOG: Structured Memory for Edge Language Models | 边缘 LLM 的 O(1) SSM 状态注入:RAG prefill 27s→6ms(~4500×),SSM 特有机制,Transformer 无法做到 |
| 4 | [2608.02218v1] PosterMELD: Multi-Agent Paper-to-Poster Generation | 模板条件化多智能体论文→海报,81.3% PRR、$0.38/请求(3.5% of Codex+Skill),输出可编辑 PPTX/PNG——PPT 自动化接单相关 |
| 5 | [2608.02005v1] OASE: Evolving in the Agent Jungle via History-Informed Opponent Awareness | 对手快照锚定成对比较,只采纳有收益证据的技能修订——多智能体动态环境中的稳定进化 |
| 6 | [2608.02178v1] Microscopic dynamics of consensus formation in multi-agent LLM Naming Games | 统计物理视角:解码温度成为 LLM 群体共识的架构相关控制参数(三种监听者状态) |
| 7 | [2608.01938v1] D-MUTRA: DLT-based MUTual Remote Attestation for Multi-Agent Systems | 区块链化多智能体互证:软件级连续运行时完整性测量,Hyperledger Besu PoC+ROS 蜂群验证 |
| 8 | [2608.01861v1] FedJigsaw: Multi-Agent Collaborative Model Reassembly | 联邦学习模型重组:模块化交换+注意力稳定训练,相对精度 +13.8%,降内存/延迟 |
| 9 | [2608.02422v1] Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning | 数字孪生+战术/操作双层规划的安全应急响应:恢复时间 -15.1%、恢复率 +33.6% |
| 10 | [2608.02470v1] Grounding Agentic VLMs ... Fine-Grained Vehicle Damage Assessment | 专用分割模型接地 VLM 推理(7 节点 LangGraph),报告幻觉率 92%→31%;focal loss 会致小目标塌缩,对比损失更好 |
| 11 | [2608.02505v1] Abduction Without a Body? Representational Grounding and the Abduction Loop | 科学假设生成的溯因循环架构(表征接地而非具身),含 DAB-30 评测程序——哲学味浓 |
| 12 | [2608.02446v1] Advancing Relevance Measurement with VLMs for Web-Scale Search | Pinterest 生产环境 VLM 相关性评估,在线 A/B 验证,显著降低 MDE |

> 注：另 2 篇离题理论文 [2608.02588v1] Condition-Number Barrier / [2608.02564v1] Dithering 值得留意——两篇都由 Google 内部**全自动 Gemini agentic 系统首次证明**再由作者人工验证，"AI 自动证明"信号本身值得跟踪。

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| Total Papers | 27 |
| cs.AI | 11 |
| cs.CR | 4 |
| cs.SE | 2 |
| cs.CL | 2 |
| cs.LG | 2 |
| cs.CV | 2 |
| cs.ET | 1 |
| cs.DC | 1 |
| cs.IR | 1 |
| physics.soc-ph | 1 |

## 🎯 Key Themes

本周论文按主题分组:

### 🛡️ Agent 安全与治理（本周最强信号）
- [2608.02518v1] Magnet: Detecting Cross-Session AI Misuse Through Capability Accumulation
- [2608.01719v1] MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication
- [2608.02407v1] Antares: Foundation Models for Agentic Vulnerability Localization
- [2608.01938v1] D-MUTRA: DLT-based Mutual Remote Attestation for Multi-Agent Systems
- [2608.02422v1] Agentic Incident Response through Digital Twin-Enhanced Multiscale Planning

### 🧠 Agent 记忆与状态连续性
- [2608.02515v1] LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference
- [2608.02508v1] RoMeRL: ... Self-Evolving Agent Memory via Reduced-Order Utility States
- [2608.02560v1] PRECOG: Structured Memory for Edge Language Models

### 🛠️ 编码 Agent 与软件工程
- [2608.02499v1] SWE-Touch: Benchmarking Coding Agents When Users Touch the Code
- [2608.02464v1] Real-Time Detection and Repair of LLM Agent Failures
- [2608.02582v1] ACEM: A Cost Estimation Model for Agentic Software Engineering

### 🤖 多智能体协作与推理
- [2608.02291v1] TreeCredit: Shared Prefixes, Better Credit: Adaptive Routing for Multi-Agent Reasoning
- [2608.01805v1] CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution
- [2608.02218v1] PosterMELD: Multi-Agent Paper-to-Poster Generation
- [2608.02005v1] OASE: Evolving in the Agent Jungle
- [2608.02178v1] Multi-Agent LLM Naming Games
- [2608.01861v1] FedJigsaw: Multi-Agent Collaborative Model Reassembly

### ⚙️ Agentic 行业自动化
- [2608.02569v1] AtumAI: Agentic Generation of Datacenter Control-Plane Policies
- [2608.01791v1] PICopilot: LLM-based Agentic Framework for Photonic IC Design
- [2608.02441v1] Agentic Commerce World
- [2608.02470v1] TinyDamage: Grounding Agentic VLMs for Vehicle Damage Assessment

### 🧪 Agent 评测方法论
- [2608.02444v1] ParEvalLayer: When Partial LLM-Agent Evaluations Support a Decision
- [2608.02441v1] Agentic Commerce World（协议校验+可审计）
- [2608.02553v1] A Taxonomy of Cognitive Capability Gaps

---

## ✅ 论文验证状态（搜索引擎交叉验证）

| 论文 | 验证状态 | 备注 |
|-----|---------|------|
| **SWE-Touch** | ✅ 已验证 | HF papers 页确认：59% 会话含用户代码改动，9 模型 SWE-bench Verified |
| **Real-Time Detection & Repair** | ✅ 已验证 | arXiv 页+chatpaper 确认，代码/数据已发布 |
| **RoMeRL** | ✅ 已验证 | arXiv 页确认 + GitHub 代码（YOUNG-fnxm/RoMeRL） |
| **LiveMem** | ✅ 已验证 | arXiv 页确认（cs.CL） |
| **Magnet** | ✅ 已验证 | arXiv 页+chatpaper；承接 Cross-Session Threats（2604.21131） |
| **Antares** | ✅ 已验证 | Cisco Foundation AI 官方 technical report 确认 |
| **ACEM** | ✅ 已验证 | arXiv 页确认（27 页，cs.SE）；agentic 成本话题行业热度高 |
| **TreeCredit** | 🔍 方向验证 | 论文太新无独立页面，多智能体路由方向真实 |
| **AtumAI** | 🔍 方向验证 | agentic control plane 为行业热点，论文本身太新 |
| **PICopilot** | 🔍 方向验证 | LLM 硬件设计 agent 方向真实（同域有 P2P 等），48/48 待深读 |
| **CockpitHAT** | 🔄 待深读 | 元数据可信（Who&When 基准 agent 级 77.9%） |
| **MNC** | 🔄 待深读 | 元数据可信 |
| **Taxonomy** | 🔄 待深读 | 综述型，框架价值待评估 |
| **ACWorld** | 🔄 待深读 | 元数据可信（200+60 任务，十模型 65.9%-91.4%） |
| **ParEvalLayer** | 🔄 待深读 | 元数据可信 |

---

## 🎯 阅读优先级（基于验证 + 第二 Brain 相关性）

**立即行动**（本周内）：
1. **Real-Time Detection and Repair**（agent 失败监控 → Hermes 可靠性体系）
2. **RoMeRL**（记忆-奖励陷阱 → 第二大脑记忆体系）

**中期跟踪**（1-2 周）：
3. **SWE-Touch**（共享工作区状态感知 → 桌面插件/agent 运行时）
4. **ACEM**（agentic 成本建模 → 闲鱼接单定价）

**长期研究**（1 个月+）：
5. **LiveMem / Magnet / PICopilot / AtumAI**

---

## ✅ 可落地行动项

### 🔴 高优先级（本周内）

#### 1. Agent 失败轻量监控层（参考 Real-Time Detection and Repair）
**实现目标**：
- 为 Hermes cron/agent 任务加"零成本哨兵"：**确定性验证优先于 LLM 裁判**——重算工具结果（校验总和/必需调用），0 误报代价下捕获 60% 失败
- 对高频 cron 任务记录步级遥测（工具错误数、循环检测、目标漂移），训练单类检测器成本太高时可先落地确定性验证层

**具体行动**：
- 在 `hermes-automation-patterns` 技能增加「确定性验证哨兵」模式：失败→回滚→重跑，恢复率参考 45%、任务成功率 52%→73%（约 +1 次模型调用/次）

#### 2. 记忆降阶 + 反奖励污染（参考 RoMeRL）
**实现目标**：
- memory 系统按**固定语义坐标**组织（outcome polarity × 记忆动态），替代无限增长的轨迹索引；剔除 co-retrieved 误得效用的条目

**具体行动**：
- 在 `daily-knowledge-absorption-gate` 增加记忆条目 outcome 标注（✅ 有效/❌ 误导），低价值条目降权而非删除；反馈密度目标 ×6

---

### 🟡 中优先级（2-3 周）

#### 3. 共享工作区状态感知（参考 SWE-Touch）
- Hermes 桌面插件/agent 运行时检测用户对文件/代码的**并发修改**；冲突编辑时重新检视仓库 + 跑目标测试后再提交（对应 Counter-Edit 暴露的三大能力缺口：变更检测、冲突调和、行为验证）

#### 4. Agentic 成本估算（参考 ACEM）
- 闲鱼 AI 接单报价引入 token 成本因子：**Revision Factor**（返工/重试开销）与 **Context Factor**（上下文累积膨胀）；按任务复杂度给 LLM / HITL / 基建三维预算，替代纯拍脑袋报价

---

### 🟢 长期跟踪（1 个月+）

#### 5. 硬件设计脚本 Agent（参考 PICopilot）
- 评估「自然语言 → PCB/EDA 脚本」服务化：JLC MCP 已有 38 工具，可叠加 PICopilot 式多智能体编排（反馈机制+定制 RAG）——与 PCB 接单业务直接相关

#### 6. 认知能力差距框架（参考 Taxonomy）
- 对照五维分类（持久状态建模/目标自主/自我监控/环境交互/学习适应）盘点 Second Brain 七大自举系统的认知缺口

---

*生成时间：2026-08-05 | 数据源：arXiv API (export.arxiv.org) | 验证：搜索引擎交叉验证 | 状态：reading*

*Generated automatically via arXiv API cron job (arxiv skill). Last updated: 2026-08-05*

---

## 已处理：核心贡献精选 3 篇 → 📄 knowledge/arXiv/arxiv-2026-08-05-core-contributions.md

- 🥇 Real-Time Detection and Repair of LLM Agent Failures（→ hermes-automation-patterns 确定性验证哨兵已落地）
- 🥈 RoMeRL（→ Second Brain 记忆体系语义坐标）
- 🥉 SWE-Touch（→ 桌面插件共享工作区感知）

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
