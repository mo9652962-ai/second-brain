---
aliases:
  - arXiv Weekly Roundup 2026-08-02
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - computer-use-agent
  - multi-agent
  - ai4ai
  - paper-review
created: 2026-08-02
updated: 2026-08-02
status: reading
source: https://arxiv.org/
domain: research
---

# arXiv Weekly Roundup — AI Agent & LLM Papers

**Date:** 2026-08-02 | **Week 32**
**Papers:** 26 relevant (15 精选完整摘要 + 11 简评),收集范围 07-19 ~ 07-30

---

## 📄 Paper Highlights

### 1. [2607.28609v1] OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

- **Authors:** Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang et al. (OS-Copilot)
- **Published:** 2026-07-30
- **Categories:** cs.AI, cs.CL, cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.28609v1) | [PDF](https://arxiv.org/pdf/2607.28609v1) | [Project](https://os-copilot.github.io/OSReward-Home/)

**Abstract:**
Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier.

---

### 2. [2607.28568v1] Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering

- **Authors:** Junlin Yang, Che Jiang, Yu Fu et al. (Horizon Research, Frontis.AI + 清华大学)
- **Published:** 2026-07-30
- **Categories:** cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.28568v1) | [PDF](https://arxiv.org/pdf/2607.28568v1) | [Project/Code](https://frontisai.github.io/OpenRSI)

**Abstract:**
Recursive self-improvement (RSI) requires AI systems that improve the process of building AI (i.e., AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed for studying this capability. We introduce OpenMLE, an open full-stack system for RSI research in MLE, spanning verifiable task environments with execution feedback (OpenMLE-Gym), operator learning (OpenMLE-RL), and long-horizon search (OpenMLE-Evo). On this stack we post-train Frontis-MA1 (35B) as a meta-evolution agent for MLE, aligning post-training and inference around four atomic program-evolution operators (Draft, Improve, Debug, Crossover): the same operators are trained via execution-grounded SFT and RL on data deduplicated against all evaluation benchmarks, then composed into long-horizon search, coupling learning and evolution in a single loop. On MLE-Bench Lite under a 12-hour per-task budget on one RTX 4090 capped at 12 GB VRAM, Frontis-MA1 (35B) improves Medal Average from 39.39% to 60.61% over its base model with OpenMLE-Evo, and reaches 71.21% with OpenMLE-Evo-Max (benchmark-independent experience priors and asynchronous search), exceeding GPT-5.5 + Codex and approaching GPT-5.6 Sol and the 2.8T Kimi K3. On held-out NatureBench Lite, both components transfer: with the framework fixed, swapping in the trained model raises Match-SOTA from 50% to 70%; with the model fixed, swapping in OpenMLE-Evo raises it from 20% to 50%. We release the model weights and the full OpenMLE stack.

---

### 3. [2607.28430v1] AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration

- **Authors:** Xinxing Ren, Qianbo Zang, Ziyan Wang et al. (Coral Protocol)
- **Published:** 2026-07-30
- **Categories:** cs.MA
- **Links:** [Abstract](https://arxiv.org/abs/2607.28430v1) | [PDF](https://arxiv.org/pdf/2607.28430v1) | [Code](https://github.com/Coral-Protocol/AgentRadio)

**Abstract:**
Understanding large codebases is a long-horizon task for Large Language Model (LLM) agents: answering a single question can require building and running the software, tracing execution across files, and synthesizing evidence over tens of minutes. On SWE-Atlas QnA, a benchmark of long-horizon questions over production repositories, a single Claude Code agent (Opus 4.6) resolves only 32.3% of tasks. Dividing the work among agents with clean contexts mitigates this limitation. However, the subtasks of code comprehension are interdependent. One agent's findings can rewrite another's task, so agents must coordinate during execution, not only at phase boundaries. Existing multi-agent systems support such exchange only between phases, through staged handoffs or synchronized rounds. Communication and work remain mutually exclusive. A discovery made mid-execution cannot be shared until the next boundary. We present AgentRadio, an asynchronous message-passing layer that equips coding-agent harnesses with three primitives: threads, messages, and waiting for mentions. The last runs as a background task, surfacing teammates' messages without interrupting foreground work, so each agent remains passively aware of its peers and folds new findings into its ongoing task. Under a five-phase protocol of division of labor and negotiation, four agents organized by AgentRadio resolve 62.1% of tasks, 29.8 points above a single agent and above Claude Code with the newer Opus 4.8 (57.2%). Rubric-level analysis shows the gain growing with task difficulty, consistent with mid-course correction as the underlying mechanism.

---

### 4. [2607.28074v1] Echoverse: Deep, Evolving Environments for Training Computer-Use Agents at Scale

- **Authors:** Yash Pandya, Sahil Gupta, Sarthak Harne et al. (Microsoft Research)
- **Published:** 2026-07-30
- **Categories:** cs.AI, cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28074v1) | [PDF](https://arxiv.org/pdf/2607.28074v1) | [Code](https://github.com/microsoft/Echoverse) | [MSR Blog](https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents)

**Abstract:**
Computer-use agents learn from what their actions change, so training one needs applications it can act on, break and reset. The applications that matter most are login-gated and stateful, so synthetic environments stand in for them. Recent pipelines generate such environments in bulk, which moves the bottleneck from how many exist to what is inside each one. The returns, we find, come from three properties: how much behavioural depth an environment carries, whether it targets the interaction an agent actually fails, and whether it improves alongside the model. We present Echoverse, which compiles specifications into stateful applications whose tasks are graded against the application's own database, and a co-evolution loop that reads every graded rollout twice: as repairs to the environment, its tasks and its verifier, and as training signal for the model. Trained on twelve such environments, a 9B model improves from 36.5% to 67.1% across fourteen evaluation splits, within fourteen points of the much larger frontier model that taught it. On the same domains, shallow environments push live-site accuracy below the base model (80.0 → 75.0) while deep ones raise it (80.0 → 85.0 and 48.0 → 65.0); drilling one interface control across many renderings transfers to held-out widget families and to the open web; and repairing a single environment lifts the model trained on it from 16.2% to 38.5%. The same worlds serve as reinforcement-learning environments, where a reward combining the grounded verifier with a dense per-step judge raises held-out score from 58.8% to 68.0%. We release four environments as a benchmark, with their applications, seed data and grounded graders.

---

### 5. [2607.21557v2] OpenForgeRL: Train Harness-native Agents in Any Environment

- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu et al. (MSR / Columbia)
- **Published:** 2026-07-23 (v2 07-30)
- **Categories:** cs.AI, cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.21557v2) | [PDF](https://arxiv.org/pdf/2607.21557v2) | [HF Papers](https://huggingface.co/papers/2607.21557)

**Abstract:**
Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. OpenForgeRL achieves this with a lightweight proxy that serves the harness's model calls while recording them as training data for a standard RL codebase (e.g., veRL), and a Kubernetes orchestrator that runs each rollout in its own remote container, together enabling training on any harness in any environment at scale. By decoupling training and inference, OpenForgeRL allows researchers to easily train, study, and improve agents directly in the real harnesses and environments they are deployed with. Using only hundreds to a few thousand tasks, OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval and 33.7 on QwenClawBench. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. Both outperform open baselines of similar size on nearly all benchmarks, and in the GUI setting match or surpass models several times larger. Beyond benchmarks, we analyze how harness choice (e.g., ZeroClaw, OpenClaw, Codex) and RL shape agent behavior: some harnesses are substantially harder to learn than others, and RL improves agentic reliability (self-verification, tool coverage, multi-step plans), though critical abilities such as error recovery remain weak.

---

### 6. [2607.22798v1] StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

- **Authors:** Yan Yang, Xiangru Jian, Ziyang Luo et al. (Salesforce / Salesforce AI Research)
- **Published:** 2026-07-24
- **Categories:** cs.SE, cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.22798v1) | [PDF](https://arxiv.org/pdf/2607.22798v1) | [HF Papers](https://huggingface.co/papers/2607.22798)

**Abstract:**
Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click. Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. Different states can produce the same pixels, while code can inspect and modify that state directly. StateAct is a code-first, multi-agent harness built around this distinction. Its main agent works directly with program state by using code, while a dedicated GUI subagent handles screenshot-and-click interaction on the few subgoals that need it, just 28 of 108 tasks and 1.1% of main-agent steps. The same direct access to program state also supports verification: an independent finish gate double-checks the saved result for structural failures, e.g., output that is missing, unsaved, or written to the wrong path. To stay on track over hundreds of steps, the main agent hands subgoals to fresh subagents, keeping its own context focused. On OSWorld 2.0, StateAct lifts Claude Opus 4.8 from 20.6% to 26.9% on binary success, and from 54.8% to 61.6% on partial success, at ~9x lower cost per task than the same model driven by screenshots alone; a code-only variant with no GUI subagent reaches only 45.9% partial, below that screenshot-based baseline's 54.8%. Grounding action, verification, and memory in state (state-grounding) shifts the main bottleneck from perception toward reasoning.

---

### 7. [2607.28147v1] Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems

- **Authors:** Yu Cui, Wuli Yang, Yirui Shi et al.
- **Published:** 2026-07-30
- **Categories:** cs.CR
- **Links:** [Abstract](https://arxiv.org/abs/2607.28147v1) | [PDF](https://arxiv.org/pdf/2607.28147v1)

**Abstract:**
Autonomous multi-agent systems (AMAS) built on large language models (LLMs), such as Hermes, increasingly rely on inference-time harnesses to coordinate reasoning and action. Constructing these harnesses requires substantial engineering effort and computational resources, as they are iteratively optimized over a combinatorial search space while co-evolving with the underlying LLM. Inference-time harnesses therefore constitute valuable intellectual property (IP). Although prior work has investigated IP leakage in static multi-agent systems with pre-configured architectures, it remains unclear whether similar risks arise in AMAS, where harness behavior emerges dynamically during inference. To address this gap, we introduce Agent Harness Distillation (AHD), a framework for studying the security risks arising from inference-time harness extraction in AMAS. We formalize harness extraction as a new security problem and develop an evaluation framework for quantifying such risks. AHD extracts inference-time harness capabilities from a target agent through black-box interactions and consists of two stages. In the pre-distillation stage, AHD infers inference-time harness behaviors from the responses of the target agent and constructs an initial harness. In the post-distillation stage, AHD iteratively refines the initial harness to align with the behavioral patterns of the target agent. Experiments on real-world AMAS across multiple backbone LLMs demonstrate the effectiveness of AHD and reveal substantial IP leakage risks. We further propose a deception-based defense that reduces harness extraction effectiveness while preserving the utility of the protected agent.

---

### 8. [2607.27958v1] Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems

- **Authors:** Peilin Feng, Suorong Yang, Soujanya Poria (SUTD)
- **Published:** 2026-07-30
- **Categories:** cs.MA, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.27958v1) | [PDF](https://arxiv.org/pdf/2607.27958v1)

**Abstract:**
Memory is central to long-horizon LLM agents, yet existing memory systems primarily preserve interaction content rather than modeling which agents can be trusted and under what conditions. This limitation is particularly important in multi-agent systems, where a central model may be unable to directly verify plausible or correlated peer responses. We introduce Σ-Mem, an online reliability memory that records historical competence evidence for individual peers and peer relationship evidence across the peer set. Both forms of evidence are maintained as real symmetric states and updated from post-decision correctness feedback. By Weyl's inequality, the spectral change caused by each event-level update is bounded, enabling stable online adaptation without retraining the underlying models. Σ-Mem provides a general write-and-read interface: the same memory can be used for residual steering of a central model, response-free peer routing, or reliability-weighted voting. Across five Qwen-family models, Σ-Mem adapts to counterfactual reliability shifts and generalizes to unseen peers and task domains. Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set. Moreover, performance improves consistently as more correctness feedback becomes available, indicating that Σ-Mem progressively accumulates actionable reliability information.

---

### 9. [2607.28591v1] Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments

- **Authors:** Haomin Qi, Xingliang Wang, Xuanqi Gao et al. (MSRA)
- **Published:** 2026-07-30
- **Categories:** cs.SE, cs.CL, cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28591v1) | [PDF](https://arxiv.org/pdf/2607.28591v1)

**Abstract:**
Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. To expand this supply, we present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository. It aligns historical evidence with evolved code, reconstructs task states through Patch Reversal, Code Mapping, or Agent Reconstruction, and validates the lifecycle from a healthy base to a task state and a restored state. By deriving multiple tasks grounded in developer evidence from maintained environments, Change2Task provides executable data for coding agent training and evaluation while reducing repeated environment setup, storage, and task construction effort. Evaluated on five common coding agent task families (Bug Fix, Feature Addition, Test Generation, API Migration, Security Repair), starting from 1,130 source changes, Change2Task achieves 79.6% verified task construction success. On a matched candidate set, it recovers 29.2% more verified tasks than a PR-based construction baseline. Historical and reconstructed cases achieve up to 98.0% matched outcome agreement under agent evaluation, while reuse of modern bases reduces measured expenditure across the complete pipeline by 10.8%.

---

### 10. [2607.28527v1] MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

- **Authors:** Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28527v1) | [PDF](https://arxiv.org/pdf/2607.28527v1)

**Abstract:**
Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. MANTA is evaluated against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning, achieving the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

---

### 11. [2607.28545v1] ORCA-bench: How Ready Are Language Model Agents for Oncall?

- **Authors:** Albert Gong, Kyuseong Choi, Abhineet Agarwal et al. (Harvard / MIT)
- **Published:** 2026-07-30
- **Categories:** cs.CL, cs.AI, cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2607.28545v1) | [PDF](https://arxiv.org/pdf/2607.28545v1)

**Abstract:**
Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system — exposing six days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, OpenSearch via Grafana) and full source-code access — with 1,079 RCA tasks that systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's κ_w=0.90). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard — a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access degrades every metric. Since real production systems are order of magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability.

---

### 12. [2607.28573v1] Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs

- **Authors:** Woongkyu Lee, Jungwook Choi (Hanyang University)
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28573v1) | [PDF](https://arxiv.org/pdf/2607.28573v1)

**Abstract:**
Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging. While recent studies show that inference-time scaling can improve frontier computer-use agents through additional computation during execution, its effectiveness for resource-constrained local models remains poorly understood. We present a systematic empirical study of inference-time scaling in local CUAs across contextual, temporal, structural, and parallel dimensions, evaluating Qwen3-VL-8B/30B-A3B, UI-TARS-1.5-7B, and OpenCUA-7B on OSWorld. Results show that additional computation often yields diminishing returns while changing failure modes. Contextual scaling provides historical grounding that improves trajectory stability and task accuracy, but its gains saturate as token cost increases and failures shift from repetitive or stalled trajectories toward premature false successes. Temporal scaling similarly reduces max-step stalls, yet does not substantially improve task success, indicating that longer horizons often extend erroneous trajectories rather than correct them. Structural decomposition can introduce planning and formatting overhead in local two-stage agents, while parallel scaling partially mitigates these failures at substantial computational cost. Overall, efficient local CUAs require selective compute allocation, failure-aware control mechanisms, and agentic frameworks designed around the capabilities and limitations of local models.

---

### 13. [2607.28399v1] Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees

- **Authors:** Zihan Dong, Rui Qian, Qishi Zhan et al.
- **Published:** 2026-07-30
- **Categories:** cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28399v1) | [PDF](https://arxiv.org/pdf/2607.28399v1)

**Abstract:**
Computer-use agents often fail on transient GUI events because they produce the correct action only after the relevant window has already closed. We identify the main cause as expensive autoregressive decoding on the decision-time critical path. We propose Adaptive Anticipatory Policy Trees (AAPT), which eliminates this delay without modifying the underlying model. During idle screen periods, the same frozen multimodal model constructs a bounded conditional policy tree with observable guards, pre-authorized actions, and branch-specific deadlines. The tree is sized to cover the model's own decoding latency. When an event occurs, a lightweight observer matches change-gated frames to a prepared branch and immediately executes the corresponding action without generating new text. In paired trials with pre-registered endpoints and exact McNemar tests, AAPT improves the success rate from 0.50 to 0.79 within a contested decision window (p=1.8×10⁻³), while producing no incorrect actions. Both open-loop and predict-and-replan baselines achieve zero success because they still decode during execution. A pre-registered oracle probe rejects our initial hypothesis and instead points to branch routing as the causal bottleneck. On an external benchmark, AAPT matches the overall performance of a reactive baseline, with complementary strengths: AAPT performs best when candidate actions can be enumerated in advance, whereas reactive execution remains stronger when they cannot.

---

### 14. [2607.28367v1] How Benchmarks Mis-Score Computer-Use Agents

- **Authors:** Zihan Dong, Zhiyuan Ma, Zekun Wang et al.
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28367v1) | [PDF](https://arxiv.org/pdf/2607.28367v1)

**Abstract:**
Computer-use agents (CUA) are being deployed to browse the web and operate desktop software, yet their benchmark scores are still commonly produced by brittle scripted oracles. A score is the output of a pipeline in which tasks can be stale, trajectories can omit decisive visual evidence, evaluators can reject valid alternatives, and aggregate reports can hide the cause of failure. We organize these problems into a reliability framework spanning task construction, trajectory observation, scoring, and reporting. We then audit 150 public failure-scored trajectories from five web, enterprise-workflow, and desktop-control benchmarks, find that 15.3% of FAIL verdicts are wrong: 10.7% are evaluator false negatives and 4.7% are broken tasks. For genuine failures, a three-tier diagnostic taxonomy shows that verification/feedback and planning failures dominate execution/grounding errors, while a single scalar success rate cannot explain. We connect these findings to newer long-horizon CUA benchmarks and derive stage-specific design rules for CUA evaluation.

---

### 15. [2607.28595v1] Beacon: Knowing When and How to Perform Agentic Visual Reasoning

- **Authors:** Qixun Wang, Yang Shi, Letian Cheng et al. (ByteDance)
- **Published:** 2026-07-30
- **Categories:** cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.28595v1) | [PDF](https://arxiv.org/pdf/2607.28595v1)

**Abstract:**
The fundamental goal of agentic visual reasoning is to improve the success rate of multimodal large language models (MLLMs) on complex tasks, rather than merely equipping them with a sophisticated yet inefficient reasoning paradigm. In this work, we rethink agentic visual reasoning through two key dimensions of tool use: Mode Adaptiveness (MA) and Tool Effect (TE). Mode Adaptiveness characterizes whether an MLLM can recognize when tools are truly necessary and invoke them accordingly, thereby avoiding unnecessary computational overhead while improving performance on challenging problems that require tool assistance. Tool Effect characterizes the actual impact of tool use: tools should extend the model's capabilities on problems unsolvable through text-only reasoning, while avoiding additional errors on problems that the model can already solve without tools. We conduct a comprehensive analysis to quantify these two properties and empirically reveal that existing agentic visual reasoning models exhibit limited Mode Adaptiveness, while the gains produced by tool use on hard examples are largely offset by the harm introduced on easy examples that the models can already solve. Motivated by these observations, we propose Beacon, a novel agentic visual reasoning model that achieves stronger overall performance, improved Mode Adaptiveness, and genuine tool-induced performance gains. At the core of Beacon are the Necessity-Aware Adaptive Reward and the Hint-Guided Capability Expansion mechanism in the reinforcement learning stage, which respectively encourage adaptive tool invocation based on task necessity and strengthen the model's tool-use capability on the most challenging problems.

---

## 📋 更多值得关注(简评)

| # | Paper | 一句话 |
|---|-------|--------|
| 1 | [SeekJudge 2607.23263v1](https://arxiv.org/abs/2607.23263v1) | 四角色专用 Agent 的 CUA 奖励模型,首个在在线 RL 中匹配/超越规则基监督的模型奖励 |
| 2 | [AskChem 2607.28618v1](https://arxiv.org/abs/2607.28618v1) | 化学文献 claim 级检索基建(2.4M claims),提供 REST/SDK/MCP 供 AI agent 调用 |
| 3 | [PAIChecker 2607.28587v1](https://arxiv.org/abs/2607.28587v1) | 多智能体检查 SWE-bench 类基准 PR-Issue 错配,发现 13.6% 实例存在错配 |
| 4 | [FaithEyes 2607.28225v1](https://arxiv.org/abs/2607.28225v1) | 多智能体自审判框架,验证工具调用过程图是否真的帮助回答问题,抑制 reward hacking |
| 5 | [SKIMIX 2607.27994v1](https://arxiv.org/abs/2607.27994v1) | 技能混合多智能体:开放数学推理增益大,选择题增益有限,agent 数量 scaling 非单调 |
| 6 | [AISPA 2607.28617v1](https://arxiv.org/abs/2607.28617v1) | 审计 88 个商业 AI 产品的 3,249 条系统提示词:40% 产品含损害用户利益的指令 |
| 7 | [CARP/SPARC 2607.28330v1](https://arxiv.org/abs/2607.28330v1) | LLM 市场 agent 信誉惩罚机制,无地面真值即可抑制低信誉卖家销量 |
| 8 | [Sidekick 2607.17527v1](https://arxiv.org/abs/2607.17527v1) | CUA 多任务场景的多模态沟通设计,30 人实验显著提升并行多任务表现 |
| 9 | [Teach it to stop 2607.17136v1](https://arxiv.org/abs/2607.17136v1) | 35B CUA 策略修复:单次运行的 RL 结果有约 30% 概率是失败模式,呼吁 k-seed 报告 |
| 10 | [RT-SHCUA 2607.17951v1](https://arxiv.org/abs/2607.17951v1) | 实时自托管 CUA 无人机控制:合同约束技能调用 + 板载安全执行 |
| 11 | [Desktop-Delta Bench v2 2607.26041v2](https://arxiv.org/abs/2607.26041v2) | 上周 v1 已收录;v2 更新(1,550 before-after 对,8 模型族评估) |

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| Total Relevant Papers | 26 (15 精选 + 11 简评) |
| cs.AI | 17 |
| cs.CL | 7 |
| cs.CV | 5 |
| cs.SE | 5 |
| cs.LG | 5 |
| cs.MA | 2 |
| cs.CR | 2 |
| cs.HC | 3 |

## 🎯 Key Themes

This week's papers focus on:
1. **CUA 评估与奖励模型爆发** — OSReward(标准化的 VLM judge 评估)、Mis-Score(基准误评分审计)、SeekJudge、AAPT(延迟)、Teach it to stop(单次运行统计陷阱):CUA 从"能做"进入"怎么可靠度量"阶段
2. **CUA 训练范式转向** — Echoverse(深度环境替代批量浅环境)、StateAct(程序状态优先于像素)、Change2Task(仓库历史→可执行编码任务)
3. **多智能体协调与记忆** — AgentRadio(异步被动感知)、MANTA(拓扑自演化)、Σ-Mem(可靠性记忆而非内容记忆)
4. **AI4AI 与递归自改进开源化** — Frontis-MA1/OpenMLE(全开源 RSI 栈)、OpenForgeRL(harness-native 训练,直接支持 OpenClaw/Codex/Claude Code)
5. **Agent 安全与可信** — Agent Harness Distillation(推理时 harness IP 蒸馏攻击)、AISPA(系统提示词审计)、CARP(市场信誉机制)

---

## ✅ 论文验证状态(搜索引擎交叉验证)

| 论文 | 验证状态 | 备注 |
|-----|---------|------|
| **OSReward** | ✅ 已验证 | os-copilot.github.io 项目页 + arXiv HTML + AIGC 报道;1,019 条人标轨迹,27 个 judge 排行 |
| **Frontis-MA1** | ✅ 已验证 | frontisai.github.io/OpenRSI 官方页(Horizon Research + 清华),开源权重,HF 热议 07-30 |
| **AgentRadio** | ✅ 已验证 | GitHub Coral-Protocol/AgentRadio 开源;SWE-Atlas(Scale AI)基准背景确认 |
| **Echoverse** | ✅ 已验证 | microsoft/Echoverse GitHub(MIT) + MSR Blog 07-30,作者含 Awadallah/Kamar |
| **OpenForgeRL** | ✅ 已验证 | arXiv HTML + HF papers 页;veRL 后端 + Azure K8s 细节确认,直接点名 OpenClaw |
| **StateAct** | ✅ 已验证 | HF papers + arXiv HTML;OSWorld 2.0 数据确认(Opus 4.8: 20.6→26.9, 9x 成本下降) |
| **Σ-Mem** | 🔍 方向验证 | 与上周 UniMem/MemLens 同属 agent 记忆前沿,可靠性维度是新切入 |
| **Agent Harness Distillation** | 🔍 方向验证 | AMAS IP 泄漏新威胁面,论文太新无独立页面;点名 Hermes 具身 |
| **Change2Task** | 🔄 待深读 | MSRA 团队,编码 agent 数据供给方向真实,数字需全文核对 |
| **MANTA** | 🔄 待深读 | 拓扑自演化多智能体,与 AgentRadio 互补,待深读 |

---

## 🎯 阅读优先级(基于验证 + Second Brain 相关性)

**立即行动**(本周内):
1. **Frontis-MA1 / OpenMLE** — AI4AI 递归自改进,与 Second Brain 七大自举系统直接同构,开源可复现
2. **OpenForgeRL** — 我们的运行环境就是 OpenClaw/Hermes harness;harness-native 训练思路可直接借鉴

**中期跟踪**(1-2 周):
3. **OSReward** — VLM judge 评估方法论 + leniency bias 认知,可用于自我输出质量评估
4. **Σ-Mem** — 可靠性记忆:给多技能/多子代理场景引入 peer 可靠性评分
5. **StateAct** — 状态优先范式:验证、记忆、行动全部 grounding 在程序状态而非像素

**长期研究**(1 个月+):
6. **Echoverse / AgentRadio / MANTA / Agent Harness Distillation**

---

## ✅ 可落地行动项(更新)

### 🔴 高优先级(本周内)

#### 1. **AI4AI 递归自改进实践基线**(参考 Frontis-MA1 / OpenMLE)
**实现目标**:
- 借鉴 OpenMLE 四原子算子(Draft/Improve/Debug/Crossover)框架,映射到 Second Brain 自举系统
- **短期(1 周)**:盘点七大自举模块中哪些可以"执行可验证"化(如脚本输出→自动校验)
- **中期(2 周)**:对每周 arXiv digest / 知识吸收流程引入 execution-grounded 反馈(摘要是否被实际应用)

**当前 Progress**:
- ✅ Frontis-MA1 架构已分析(OpenMLE-Gym/RL/Evo 三件套)
- ✅ 确认单卡 12GB VRAM 即可跑通 MLE-Bench Lite(本机 4060 8GB 可评估更小模型)
- 🔄 待落地:可验证任务环境的第一个试点

---

#### 2. **Harness-native 训练认知**(参考 OpenForgeRL)
**实现目标**:
- 理解"harness 本身是训练对象"——OpenClaw/Codex/Claude Code 的 harness 差异会显著影响 RL 收益
- **短期(1 周)**:记录 Hermes 各工具链使用中的 harness 特性(工具调用格式、上下文管理),沉淀为 skill
- **中期**:跟踪 OpenForgeRL 开源进展,评估是否有可以在本地复用的 rollout 流程

**预期收益**:
- 不换模型也能通过 harness 优化获得 agentic 可靠性提升(self-verification、tool coverage)

---

### 🟡 中优先级(2-3 周)

#### 3. **可靠性记忆**(参考 Σ-Mem)
**实现目标**:
- 在记忆体系中增加"可信度"维度:哪些信息来源(web/工具/用户)历史上准确率高
- 对多来源结论冲突时,按可靠性加权而不是平均

---

#### 4. **异步被动感知协作**(参考 AgentRadio)
**实现目标**:
- 借鉴 wait-for-mention 模式:后台任务不打断前台工作,但新发现能及时汇入
- 应用场景:长任务中的子代理/后台 cron 结果被动感知,避免阶段边界才同步

---

### 🟢 长期跟踪(1 个月+)

#### 5. **CUA 评估审计方法论**(OSReward + Mis-Score)
#### 6. **深度训练环境**(Echoverse)
#### 7. **多智能体拓扑自演化**(MANTA)
...

---

*生成时间:2026-08-02 | 数据源:arXiv API (export.arxiv.org) | 验证:搜索引擎交叉验证 | 状态:reading → processed*

*Generated automatically via arXiv API cron job (arxiv-weekly-digest skill). Last updated: 2026-08-02*

---

**已处理：** 核心贡献精选 3 篇（Frontis-MA1 / AgentRadio / Σ-Mem）→ 📄 `knowledge/arXiv/arxiv-2026-08-02-core-contributions.md`（2026-08-02 arxiv-summarize）

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
