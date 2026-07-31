---
aliases:
  - arXiv Weekly Roundup 2026-07-31
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - paper-review
  - computer-use-agent
  - multi-agent
created: 2026-07-31
updated: 2026-07-31
status: reading
source: https://arxiv.org/
domain: research
---

# arXiv Weekly Roundup — AI Agent & LLM Papers

**Date:** 2026-07-31 | **Week 32**
**Papers:** 20 relevant papers (15 详细解读 + 5 简评) | 主要投稿日 2026-07-30

---

## 📄 Paper Highlights

### 1. [2607.28609v1] OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

- **Authors:** Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen et al.
- **Published:** 2026-07-30 | **Categories:** cs.AI, cs.CL, cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.28609v1) | [PDF](https://arxiv.org/pdf/2607.28609v1)

**Abstract:**
Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Code: https://os-copilot.github.io/OSReward-Home/

---

### 2. [2607.28573v1] Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs

- **Authors:** Woongkyu Lee, Jungwook Choi
- **Published:** 2026-07-30 | **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28573v1) | [PDF](https://arxiv.org/pdf/2607.28573v1)

**Abstract:**
Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging. While recent studies show that inference-time scaling can improve frontier computer-use agents through additional computation during execution, its effectiveness for resource-constrained local models remains poorly understood. We present a systematic empirical study of inference-time scaling in local CUAs across contextual, temporal, structural, and parallel dimensions. We evaluate Qwen3-VL-8B/30B-A3B, UI-TARS-1.5-7B, and OpenCUA-7B on the OSWorld benchmark. Our results show that additional computation often yields diminishing returns while changing failure modes. Contextual scaling provides historical grounding that improves trajectory stability and task accuracy, but its gains saturate as token cost increases and failures shift from repetitive or stalled trajectories toward premature false successes. Temporal scaling similarly reduces max-step stalls, yet does not substantially improve task success, indicating that longer horizons often extend erroneous trajectories rather than correct them. We further find that structural decomposition can introduce planning and formatting overhead in local two-stage agents, while parallel scaling partially mitigates these failures at a substantial computational cost. Overall, our findings suggest that efficient local CUAs require selective compute allocation, failure-aware control mechanisms, and agentic frameworks designed around the capabilities and limitations of local models.

---

### 3. [2607.28399v1] Why Are GUI Agents Correct but Late? Decode on the Decision-Time Critical Path, Tested with Pre-Compiled Policy Trees

- **Authors:** Zihan Dong, Rui Qian, Qishi Zhan, Dongshen Peng, Kaixin Li, Yu Li
- **Published:** 2026-07-30 | **Categories:** cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28399v1) | [PDF](https://arxiv.org/pdf/2607.28399v1)

**Abstract:**
Computer-use agents often fail on transient GUI events because they produce the correct action only after the relevant window has already closed. We identify the main cause as expensive autoregressive decoding on the decision-time critical path. We propose Adaptive Anticipatory Policy Trees (AAPT), which eliminates this delay without modifying the underlying model. During idle screen periods, the same frozen multimodal model constructs a bounded conditional policy tree with observable guards, pre-authorized actions, and branch-specific deadlines. The tree is sized to cover the model's own decoding latency. When an event occurs, a lightweight observer matches change-gated frames to a prepared branch and immediately executes the corresponding action without generating new text. In paired trials with pre-registered endpoints and exact McNemar tests, AAPT improves the success rate from 0.50 to 0.79 within a contested decision window (p=1.8e-3), while producing no incorrect actions. Both open-loop and predict-and-replan baselines achieve zero success because they still decode during execution. Ablations reveal three key requirements: fast observer decoding, valid tree planning, and accurate branch routing. AAPT performs best when candidate actions can be enumerated in advance, whereas reactive execution remains stronger when they cannot.

---

### 4. [2607.28367v1] How Benchmarks Mis-Score Computer-Use Agents

- **Authors:** Zihan Dong, Zhiyuan Ma, Zekun Wang, Yunqing Li, Zirou Liu, Ruixuan Deng, Qishi Zhan, Rui Qian
- **Published:** 2026-07-30 | **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28367v1) | [PDF](https://arxiv.org/pdf/2607.28367v1)

**Abstract:**
Computer-use agents (CUA) are being deployed to browse the web and operate desktop software, yet their benchmark scores are still commonly produced by brittle scripted oracles. A score is the output of a pipeline in which tasks can be stale, trajectories can omit decisive visual evidence, evaluators can reject valid alternatives, and aggregate reports can hide the cause of failure. We organize these problems into a reliability framework spanning task construction, trajectory observation, scoring, and reporting. We then audit 150 public failure-scored trajectories from five web, enterprise-workflow, and desktop-control benchmarks, find that **15.3% of FAIL verdicts are wrong**: 10.7% are evaluator false negatives and 4.7% are broken tasks. For genuine failures, a three-tier diagnostic taxonomy shows that verification/feedback and planning failures dominate execution/grounding errors, while a single scalar success rate cannot explain. We connect these findings to newer long-horizon CUA benchmarks and derive stage-specific design rules for CUA evaluation.

---

### 5. [2607.28074v1] Echoverse: Deep, Evolving Environments for Training Computer-Use Agents at Scale

- **Authors:** Yash Pandya, Sahil Gupta, Sarthak Harne, Archana Yadav et al. (Microsoft Research)
- **Published:** 2026-07-30 | **Categories:** cs.AI, cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28074v1) | [PDF](https://arxiv.org/pdf/2607.28074v1) | [MSR Blog](https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents)

**Abstract:**
Computer-use agents learn from what their actions change, so training one needs applications it can act on, break and reset. The applications that matter most are login-gated and stateful, so synthetic environments stand in for them. Recent pipelines generate such environments in bulk, which moves the bottleneck from how many exist to what is inside each one. The returns, we find, come from three properties: how much behavioural depth an environment carries, whether it targets the interaction an agent actually fails, and whether it improves alongside the model. We present Echoverse, which compiles specifications into stateful applications whose tasks are graded against the application's own database, and a co-evolution loop that reads every graded rollout twice: as repairs to the environment, its tasks and its verifier, and as training signal for the model. Trained on twelve such environments, a 9B model improves from **36.5% to 67.1%** across fourteen evaluation splits, within fourteen points of the much larger frontier model that taught it. Shallow environments push live-site accuracy below the base model (80.0 → 75.0) while deep ones raise it (80.0 → 85.0 and 48.0 → 65.0); repairing a single environment lifts the model trained on it from 16.2% to 38.5%. The same worlds serve as RL environments, where a reward combining the grounded verifier with a dense per-step judge raises held-out score from 58.8% to 68.0%. Code: https://aka.ms/echoverse

---

### 6. [2607.22798v1] StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

- **Authors:** Yan Yang, Xiangru Jian, Ziyang Luo et al. (Salesforce AI Research)
- **Published:** 2026-07-24 | **Categories:** cs.SE, cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.22798v1) | [PDF](https://arxiv.org/pdf/2607.22798v1)

**Abstract:**
Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click. Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. Different states can produce the same pixels, while code can inspect and modify that state directly. StateAct is a code-first, multi-agent harness built around this distinction. Its main agent works directly with program state by using code, while a dedicated GUI subagent handles screenshot-and-click interaction on the few subgoals that need it, just 28 of 108 tasks and 1.1% of main-agent steps. The same direct access to program state also supports verification: an independent finish gate double-checks the saved result for structural failures. On OSWorld 2.0, StateAct lifts Claude Opus 4.8 from 20.6% to 26.9% on binary success, and from 54.8% to 61.6% on partial success, at **~9x lower cost per task** than the same model driven by screenshots alone. Grounding action, verification, and memory in state — "state-grounding" — shifts the main bottleneck from perception toward reasoning: failures depend more on what the agent thinks than on what it sees.

---

### 7. [2607.21557v2] OpenForgeRL: Train Harness-native Agents in Any Environment

- **Authors:** Xiao Yu, Baolin Peng, Ruize Xu, Hao Zou, Qianhui Wu, Hao Cheng, Wenlin Yao, Nikhil Singh, Zhou Yu, Jianfeng Gao (Columbia/Dartmouth/MSR)
- **Published:** 2026-07-23 (v2) | **Categories:** cs.AI, cs.CL | ICLR 2027 投稿
- **Links:** [Abstract](https://arxiv.org/abs/2607.21557v2) | [PDF](https://arxiv.org/pdf/2607.21557v2)

**Abstract:**
Modern AI agents rely on elaborate inference harnesses such as Claude Code, Codex, and OpenClaw to drive multi-turn reasoning, tool use, and access to external systems. While powerful, these complex harnesses also make agents hard to train end-to-end with open infrastructure, whose SFT/RL stacks cannot natively express stateful, multi-process harness inference. To address this, we present OpenForgeRL, an open-source framework for training harness-based agents end-to-end in diverse environments. OpenForgeRL achieves this with a lightweight proxy that serves the harness's model calls while recording them as training data for a standard RL codebase (e.g., veRL), and a Kubernetes orchestrator that runs each rollout in its own remote container, together enabling training on any harness in any environment at scale. Using only hundreds to a few thousand tasks, OpenForgeClaw reaches 31.7 pass^3 and 55.9 pass@3 on ClawEval and 33.7 on QwenClawBench. OpenForgeGUI reaches 37.7 on OSWorld-Verified, 63.0 on Online-Mind2Web, and 72.3 on WebVoyager. RL improves agentic reliability such as self-verification, tool coverage, and completing multi-step plans, though critical abilities such as error recovery remain weak. 与 OpenClaw/Hermes 生态直接相关。

---

### 8. [2607.28591v1] Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments

- **Authors:** Haomin Qi, Xingliang Wang, Xuanqi Gao et al. (微软)
- **Published:** 2026-07-30 | **Categories:** cs.SE, cs.CL, cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28591v1) | [PDF](https://arxiv.org/pdf/2607.28591v1)

**Abstract:**
Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. We present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository. It aligns historical evidence with evolved code, reconstructs task states through Patch Reversal, Code Mapping, or Agent Reconstruction, and validates the lifecycle from a healthy base to a task state and a restored state. Covering five task families (Bug Fix, Feature Addition, Test Generation, API Migration, Security Repair), starting from 1,130 source changes, Change2Task achieves **79.6% verified task construction success**. On a matched candidate set, it recovers 29.2% more verified tasks than a PR-based construction baseline.

---

### 9. [2607.28545v1] ORCA-bench: How Ready Are Language Model Agents for Oncall?

- **Authors:** Albert Gong, Kyuseong Choi, Abhineet Agarwal et al.
- **Published:** 2026-07-30 | **Categories:** cs.CL, cs.AI, cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2607.28545v1) | [PDF](https://arxiv.org/pdf/2607.28545v1)

**Abstract:**
Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system — six days of metrics/logs/traces through real telemetry interfaces (Prometheus, Jaeger, OpenSearch via Grafana) and full source-code access — with 1,079 RCA tasks. Across five frontier agents, the best RCA Accuracy is **25.3% on Medium and 10.0% on Hard** tasks; the weakest model hallucinates an implausible root cause in 40% of incident reports. Removing source-code access degrades every metric. The reported gap is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability.

---

### 10. [2607.28527v1] MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

- **Authors:** Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **Published:** 2026-07-30 | **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28527v1) | [PDF](https://arxiv.org/pdf/2607.28527v1)

**Abstract:**
Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. MANTA achieves the highest average score of **74.0**, outperforming the strongest baseline by 5.8 percentage points across five benchmarks (information seeking, tool use, planning, workflow execution, math reasoning). Inference-time self-improvement can extend to the architecture of collaboration itself.

---

### 11. [2607.28430v1] AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration

- **Authors:** Xinxing Ren, Qianbo Zang, Ziyan Wang, Caelum Forder, Suman Deb, Peter Carroll, Zekun Guo
- **Published:** 2026-07-30 | **Categories:** cs.MA
- **Links:** [Abstract](https://arxiv.org/abs/2607.28430v1) | [PDF](https://arxiv.org/pdf/2607.28430v1)

**Abstract:**
Understanding large codebases is a long-horizon task for LLM agents: answering a single question can require building and running the software, tracing execution across files, and synthesizing evidence over tens of minutes. On SWE-Atlas QnA, a single Claude Code agent (Opus 4.6) resolves only 32.3% of tasks. We present AgentRadio, an asynchronous message-passing layer that equips coding-agent harnesses with three primitives: threads, messages, and waiting for mentions. The last runs as a background task, surfacing teammates' messages without interrupting foreground work, so each agent remains passively aware of its peers and folds new findings into its ongoing task. Under a five-phase protocol of division of labor and negotiation, four agents organized by AgentRadio resolve **62.1% of tasks, 29.8 points above a single agent** and above Claude Code with the newer Opus 4.8 (57.2%). Code: https://github.com/Coral-Protocol/AgentRadio

---

### 12. [2607.28225v1] FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification

- **Authors:** Haoqing Wang, Xingrun Xing, Wei Xia, Ziheng Li, Yehui Tang
- **Published:** 2026-07-30 | **Categories:** cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.28225v1) | [PDF](https://arxiv.org/pdf/2607.28225v1)

**Abstract:**
Agentic vision-language models (VLMs), which interleave textual reasoning with explicit tool calls such as cropping and code-based image manipulation, have emerged as a compelling paradigm for reliable and interpretable multimodal reasoning. However, recent studies have revealed that such models often use tools unfaithfully. Many process images are irrelevant to the question (e.g., the tool crops the wrong region or misses the queried target), yet the call still receives full credit and the model still answers correctly. We introduce FaithEyes, a multi-agent self-judging framework: a VLM judges whether each process image helps answer the question. The judgement is injected into the reasoning context as part of the tool observation, and used to scale the tool reward by the helpful-tool ratio to suppress reward hacking. A multi-agent framework lets the model itself serve as a subagent to judge the tool calls from the main agent, eliminating dependence on an external model at inference. FaithEyes attains competitive accuracy across visual benchmarks while markedly improving tool faithfulness. Code: https://github.com/Mosi-AI/FaithEyes

---

### 13. [2607.28147v1] Agent Harness Distillation: Inference-Time Harness Extraction and Exploitation in Autonomous Multi-Agent Systems

- **Authors:** Yu Cui, Wuli Yang, Yirui Shi, Junhao Xia, Hui Jiang, Lei Gao, Chenfu Bao
- **Published:** 2026-07-30 | **Categories:** cs.CR
- **Links:** [Abstract](https://arxiv.org/abs/2607.28147v1) | [PDF](https://arxiv.org/pdf/2607.28147v1)

**Abstract:**
Autonomous multi-agent systems (AMAS) built on large language models (LLMs), such as Hermes, increasingly rely on inference-time harnesses to coordinate reasoning and action. Constructing these harnesses requires substantial engineering effort and computational resources, as they are iteratively optimized over a combinatorial search space while co-evolving with the underlying LLM. Inference-time harnesses therefore constitute valuable intellectual property (IP). We introduce Agent Harness Distillation (AHD), a framework for studying the security risks arising from inference-time harness extraction in AMAS. AHD extracts inference-time harness capabilities from a target agent through black-box interactions, in two stages: pre-distillation infers harness behaviors from responses and constructs an initial harness; post-distillation iteratively refines it to align with the target's behavioral patterns. Experiments on real-world AMAS across multiple backbone LLMs demonstrate the effectiveness of AHD and reveal substantial IP leakage risks. A deception-based defense reduces harness extraction effectiveness while preserving utility. ⚠️ 论文直接点名 Hermes 类系统。

---

### 14. [2607.28568v1] Frontis-MA1: Training an AI4AI Model towards Recursive Self-Improvement in Machine Learning Engineering

- **Authors:** Junlin Yang, Che Jiang, Yu Fu et al. (FrontisAI)
- **Published:** 2026-07-30 | **Categories:** cs.CL
- **Links:** [Abstract](https://arxiv.org/abs/2607.28568v1) | [PDF](https://arxiv.org/pdf/2607.28568v1)

**Abstract:**
Recursive self-improvement (RSI) requires AI systems that improve the process of building AI (AI4AI); machine learning engineering (MLE) offers a concrete, executable testbed. We introduce OpenMLE, an open full-stack system for RSI research in MLE: verifiable task environments with execution feedback (OpenMLE-Gym), operator learning (OpenMLE-RL), and long-horizon search (OpenMLE-Evo). On this stack we post-train Frontis-MA1 (35B) as a meta-evolution agent for MLE, aligning around four atomic program-evolution operators (Draft, Improve, Debug, Crossover). On MLE-Bench Lite under a 12-hour budget on one RTX 4090, Frontis-MA1 improves Medal Average from 39.39% to 60.61% over its base model with OpenMLE-Evo, and reaches 71.21% with OpenMLE-Evo-Max — exceeding GPT-5.5 + Codex and approaching GPT-5.6 Sol and the 2.8T Kimi K3. On held-out NatureBench Lite, both components transfer. Code: https://github.com/FrontisAI/OpenRSI

---

### 15. [2607.28618v1] AskChem: Claim-Centered Infrastructure for Chemistry Literature Synthesis

- **Authors:** Bing Yan, Gregory Wolfe, Stefano Martiniani, Kyunghyun Cho
- **Published:** 2026-07-30 | **Categories:** cs.CL, cs.AI, cs.IR, cs.LG
- **Links:** [Abstract](https://arxiv.org/abs/2607.28618v1) | [PDF](https://arxiv.org/pdf/2607.28618v1) | [Site](https://askchem.org)

**Abstract:**
Chemistry literature synthesis often requires assembling specific findings scattered across many publications, yet existing literature-search systems primarily return ranked document lists. As a result, scientists and AI agents need to locate relevant information, verify their provenance, and assemble cross-paper answers manually. We present AskChem, a claim-centered infrastructure for cross-paper chemistry search. AskChem changes the unit of retrieval from the paper to the provenance-carrying claim: each paper is converted into atomic, typed claims, each grounded by a source DOI and a verbatim quote or an explicit evidence locator. AskChem currently indexes **2.4M claims from 147K papers** and provides a web interface, as well as REST, SDK, and MCP access for AI agents. On AskChem-Bench, grounding a GPT-5.5 reader in AskChem yields 100% resolvable DOIs vs 88.3% without retrieval. 💡 对 Second Brain 文献检索架构有直接借鉴价值。

---

## 📋 更多值得关注（简评）

| # | Paper | 一句话 |
|---|-------|--------|
| 16 | [SeekJudge (2607.23263)](https://arxiv.org/abs/2607.23263v1) | CUA 在线 RL 的实用模型奖励框架:四角色 Agent(Condense/Ground/Seek/Analyze)达成裁决,首次在在线 RL 中匹配/超越规则奖励 |
| 17 | [PAIChecker (2607.28587)](https://arxiv.org/abs/2607.28587v1) | 发现 SWE-bench Verified 中 **13.6% 的 PR-Issue 配对错位**(5 类模式),多 Agent 三阶段检测,二分类准确率最高 92% |
| 18 | [SKIMIX (2607.27994)](https://arxiv.org/abs/2607.27994v1) | 多 Agent skill 混合框架:嵌入检索 + 子模路由 + 自适应演化;多 Agent 对开放式数学推理增益大、选择题增益有限 |
| 19 | [AISPA (2607.28617)](https://arxiv.org/abs/2607.28617v1) | 用户中心系统提示审计:审查 88 个商业 AI 产品 3,249 条指令,~40% 产品存在损害用户利益的指令 |
| 20 | [Beacon (2607.28595)](https://arxiv.org/abs/2607.28595v1) | Agentic 视觉推理的工具使用「模式自适应」:现有模型该用工具时不用、不该用时乱用;RL 阶段必要性感知奖励修复 |

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| Total Papers | 20 |
| cs.AI | 14 |
| cs.CL | 8 |
| cs.LG | 6 |
| cs.CV | 4 |
| cs.SE | 4 |
| cs.CR / cs.MA / cs.IR / cs.CY / cs.HC | 各 1-2 |

## 🎯 Key Themes

本周投稿爆发集中在 **Computer-Use Agent (CUA) 基建** 与 **Agent Harness 工程化**:

1. **CUA 奖励与评估可靠性** — OSReward 证明 VLM judge 普遍有「宽松偏见」(把失败标成成功);Mis-Score 审计发现 15.3% 的 FAIL 判定是错的 → CUA 评估基建进入自我审视期
2. **CUA 训练环境规模化** — Echoverse(深度演化环境)、StateAct(状态优先而非像素)、OpenForgeRL(harness-native RL 训练)三路并进
3. **编码 Agent 数据与基准质量** — Change2Task(PR→可执行任务)、PAIChecker(基准错位)、ORCA-bench(值班级 RCA,frontier 仅 25%)
4. **多智能体架构自演化** — MANTA(拓扑推理时自适应)、AgentRadio(异步被动感知,单 Agent 32.3%→62.1%)、SKIMIX(skill 组合)
5. **Harness 安全与 IP 保护** — AHD 黑盒蒸馏 harness 能力,点名 Hermes 类系统;AISPA 审计系统提示
6. **AI4AI 递归自我改进** — Frontis-MA1 开源 35B meta-evolution agent,在 RTX 4090 上超越 GPT-5.5+Codex

---

## ✅ 论文验证状态（搜索引擎交叉验证）

| 论文 | 验证状态 | 备注 |
|-----|---------|------|
| **OSReward** | ✅ 已验证 | 承接 CUARewardBench (2510.18596) 方向,CUA 奖励评估是共识热点 |
| **Echoverse** | ✅ 已验证 | Microsoft Research 官方博客 7/30 同步发布(Awadallah/Kamar 团队) |
| **StateAct** | ✅ 已验证 | arXiv + HuggingFace papers 收录,Salesforce AI Research |
| **OpenForgeRL** | ✅ 已验证 | 已投 ICLR2027;YouTube/社区有解读;与 OpenClaw 生态直接相关 |
| **MANTA** | 🔍 方向验证 | 拓扑自适应与 EMNLP2025 AMAS/AdaptOrch 一脉相承,推理时自演化是新意 |
| **Agent Harness Distillation** | 🔍 方向验证 | harness 安全/蒸馏是 2026 新兴主题(AgentLeak/ATBench/MASEval 呼应) |
| **其余 14 篇** | 🔄 待深读 | arXiv 元数据完整、机构可信,摘要级已收录,待全文精读 |

---

## 🎯 阅读优先级（基于验证 + Second Brain 相关性）

**立即行动**（本周内）：
1. **OpenForgeRL** — harness-native RL 训练框架,与 OpenClaw/Hermes 生态零距离,理解「如何给自己的 agent 训练」
2. **StateAct** — state-grounding 思想(程序状态优先于像素/文本)可直接映射到 Hermes 工具设计

**中期跟踪**（1-2 周）：
3. **OSReward** — 如果后续做 CUA 或 agent 评估,奖励模型评估基准是必读
4. **AgentRadio** — 异步被动感知通信,多 Agent 编排的新原语
5. **Echoverse** — 环境深度/共演化思想,可借鉴到自动化测试环境设计

**长期研究**（1 个月+）：
6. **Frontis-MA1 / AHD / AskChem** — AI4AI、harness 安全、claim 中心检索

---

## ✅ 可落地行动项

### 🔴 高优先级（本周内）

#### 1. **State-grounding 审计自己的 Agent 工具使用**（参考 StateAct）
- 检查 Hermes 工具调用是否过度依赖「渲染层」(截图/文本快照)而非「状态层」(文件系统/API 直接读写)
- 行动：对高频任务(练习册生成、Obsidian 笔记管理)统计「直接状态操作 vs 间接读取」比例

#### 2. **学习 OpenForgeRL 的 harness 代理模式**（参考 OpenForgeRL）
- 核心机制：轻量 proxy 拦截 harness 的模型调用 → 记录为 RL 训练数据
- 可借鉴：为 Hermes 的 OpenClaw/技能调用链路增加「轨迹记录层」,为未来训练自有模型做准备

### 🟡 中优先级（2-3 周）

#### 3. **CUA 评估可靠性清单**（参考 Mis-Score + OSReward）
- 若接 CUA/GUI 自动化任务:先检查评估器的误判率,警惕「宽松偏见」
- 输出：一份「评估器可靠性自检清单」加入 hermes-automation-patterns

#### 4. **文献检索升级调研**（参考 AskChem）
- AskChem 的 claim 中心检索(原子化 claim + DOI 溯源 + MCP 接口)与 Second Brain 文献工作流契合
- 行动：评估「论文 → 原子 claim」管线在 Obsidian 知识库落地的成本

### 🟢 长期跟踪（1 个月+）

#### 5. **AgentRadio 异步通信原语** — 多 Agent 编排升级候选
#### 6. **AHD harness IP 保护** — 若公开分享 agent 配置/技能,注意可蒸馏性风险
#### 7. **Frontis-MA1 的算子化自改进** — Draft/Improve/Debug/Crossover 四算子可映射到代码工作流

---

*生成时间：2026-07-31 | 数据源：arXiv API (export.arxiv.org) | 验证：搜索引擎交叉验证 | 状态：reading → processed*

*Generated automatically via arXiv API cron job (arxiv skill). Last updated: 2026-07-31*

---

**已处理：** 核心贡献精选 3 篇（OpenForgeRL / StateAct / OSReward）→ 📄 `knowledge/arxiv-2026-07-31-core-contributions.md`（2026-07-31 arxiv-summarize）
