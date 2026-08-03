---
aliases:
  - arXiv Weekly Roundup 2026-08-03
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - multi-agent
  - paper-review
created: 2026-08-03
updated: 2026-08-03
status: reading
source: https://arxiv.org/
domain: research
---

# arXiv Weekly Roundup — AI Agent & LLM Papers

**Date:** 2026-08-03 | **Week 31**  
**Papers:** 12 new relevant papers in cs.AI / cs.CL / cs.LG / cs.MA / cs.SE  
**检索方式:** arXiv API (`cat:cs.AI+all:agent` / `abs:multi-agent+abs:LLM` / `all:agentic+all:tool`), sortBy=submittedDate 倒序

---

## 📄 Paper Highlights

### 1. [2607.28609v1] OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models

- **Authors:** Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen
- **Published:** 2026-07-30
- **Categories:** cs.AI, cs.CL, cs.CV
- **Links:** [Abstract](https://arxiv.org/abs/2607.28609v1) | [PDF](https://arxiv.org/pdf/2607.28609v1)

**Abstract:**  
Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

---

### 2. [2607.28527v1] MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems

- **Authors:** Mao-xun Huang, Jerry Wang, Yi-Cheng Lai, Zhengxin Zhang, Claire Cardie, Hen-Hsen Huang
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28527v1) | [PDF](https://arxiv.org/pdf/2607.28527v1)

**Abstract:**  
Large language model-based multi-agent systems improve complex problem solving through task decomposition, agent specialization, information exchange, and intermediate validation. However, existing systems typically treat communication topology as a fixed design choice or an offline optimization target. We introduce MANTA, a framework for Multi-Agent Network Topology Adaptation that enables communication structures to self-evolve at inference time. Before execution, MANTA initializes a task-conditioned topology from prior structural experience. During deployment, it monitors collaboration traces and applies bounded structural updates when the current organization becomes insufficient. These updates can modify agent roles, communication links, execution order, information visibility, and validation pathways while preserving the task interface and agent budget. We evaluate MANTA against representative single-agent and multi-agent baselines on five benchmarks spanning information seeking, tool use, planning, workflow execution, and mathematical reasoning. MANTA achieves the highest average score of 74.0, outperforming the strongest baseline by 5.8 percentage points and obtaining the best result on PlanCraft. These results show that inference-time self-improvement can extend to the architecture of collaboration itself.

---

### 3. [2607.27958v1] Σ-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems

- **Authors:** Peilin Feng, Suorong Yang, Soujanya Poria
- **Published:** 2026-07-30
- **Categories:** cs.MA, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.27958v1) | [PDF](https://arxiv.org/pdf/2607.27958v1)

**Abstract:**  
Memory is central to long-horizon LLM agents, yet existing memory systems primarily preserve interaction content rather than modeling which agents can be trusted and under what conditions. This limitation is particularly important in multi-agent systems, where a central model may be unable to directly verify plausible or correlated peer responses. We introduce Σ-Mem, an online reliability memory that records historical competence evidence for individual peers and peer relationship evidence across the peer set. Both forms of evidence are maintained as real symmetric states and updated from post-decision correctness feedback. By Weyl's inequality, the spectral change caused by each event-level update is bounded, enabling stable online adaptation without retraining the underlying models. Σ-Mem provides a general write-and-read interface: the same memory can be used for residual steering of a central model, response-free peer routing, or reliability-weighted voting. Across five Qwen-family models, Σ-Mem adapts to counterfactual reliability shifts and generalizes to unseen peers and task domains. Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set. Moreover, performance improves consistently as more correctness feedback becomes available, indicating that Σ-Mem progressively accumulates actionable reliability information. These results establish reliability memory as a reusable foundation for adaptive coordination in LLM-based multi-agent systems.

---

### 4. [2607.28367v1] How Benchmarks Mis-Score Computer-Use Agents

- **Authors:** Zihan Dong, Zhiyuan Ma, Zekun Wang, Yunqing Li, Zirou Liu, Ruixuan Deng
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28367v1) | [PDF](https://arxiv.org/pdf/2607.28367v1)

**Abstract:**  
Computer-use agents (CUA) are being deployed to browse the web and operate desktop software, yet their benchmark scores are still commonly produced by brittle scripted oracles. A score is the output of a pipeline in which tasks can be stale, trajectories can omit decisive visual evidence, evaluators can reject valid alternatives, and aggregate reports can hide the cause of failure. We organize these problems into a reliability framework spanning task construction, trajectory observation, scoring, and reporting. We then audit 150 public failure-scored trajectories from five web, enterprise-workflow, and desktop-control benchmarks, find that 15.3% of FAIL verdicts are wrong: 10.7% are evaluator false negatives and 4.7% are broken tasks. For genuine failures, a three-tier diagnostic taxonomy shows that verification/feedback and planning failures dominate execution/grounding errors, while a single scalar success rate can not explain. We connect these findings to newer long-horizon CUA benchmarks and derive stage-specific design rules for CUA evaluation.

---

### 5. [2607.28545v1] ORCA-bench: How Ready Are Language Model Agents for Oncall?

- **Authors:** Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal
- **Published:** 2026-07-30
- **Categories:** cs.CL, cs.AI, cs.SE
- **Links:** [Abstract](https://arxiv.org/abs/2607.28545v1) | [PDF](https://arxiv.org/pdf/2607.28545v1)

**Abstract:**  
Large language models can write, patch, and search code, but oncall root cause analysis (RCA) demands something different: reasoning over noisy metrics, logs, traces, and source code, starting from ambiguous user-facing reports, often hours after the incident began. We introduce ORCA-bench, a benchmark that puts general-purpose coding agents in a production-fidelity oncall setting. ORCA-bench pairs a live OpenTelemetry-instrumented microservice system—exposing six days of metrics, logs, and traces through real telemetry interfaces (Prometheus, Jaeger, and OpenSearch via Grafana) and full source-code access—with 1,079 RCA tasks that systematically vary report specificity, time-to-detection, and co-occurring fault scenarios. Ground-truth symptoms are curated and signed off by expert SREs, and our LLM-as-judge is independently re-scored by humans (Cohen's κ_w=0.90). Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks (the realistic-input setting) and 10.0% on Hard—a gap that remains even with Claude Fable 5. The weakest model hallucinates an implausible root cause in 40% of incident reports, and removing source-code access degrades every metric. Crucially, these are performances on a curated 50 GB / six-day testbed with tasks investigated in isolation on a system whose code and instrumentation are public. Since real production systems are order of magnitudes larger, more dynamic, and more idiosyncratic, the gap we report is a lower bound on the engineering investment required before frontier coding agents can be safely entrusted with production reliability. We release the public set at https://hub.harborframework.com/datasets/orca-bench/ORCA-bench.

---

### 6. [2607.27677v1] Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness

- **Authors:** Fouad Bousetouane
- **Published:** 2026-07-30
- **Categories:** cs.MA, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.27677v1) | [PDF](https://arxiv.org/pdf/2607.27677v1)

**Abstract:**  
AI agents are moving into production workflows where they retrieve information, call tools, maintain state, and act on behalf of users or organizations, but many release decisions still rely on capability signals, demos, or behavioral tests that do not show whether an agent is ready to operate under production constraints. Capability is therefore not production readiness. This paper introduces the ProofAgent Index (PAI), a governance readiness index for AI agents. PAI combines four dimensions of deployment evidence: Evaluation, Context, Compliance, and Governance. Evaluation measures observed behavior, Context measures the operating environment that shapes that behavior, Compliance measures alignment with applicable rules and controls, and Governance measures whether the organization can authorize, monitor, audit, and control the agent during operation. PAI is implemented inside ProofAgent Harness, an open source infrastructure for auditable AI agent evaluation and governance. Validation across two heavily regulated domains, healthcare and finance, shows that PAI carries held out readiness signal and separates higher risk from lower risk configurations. The results show that context engineering strongly changes reliability, capability improves behavior but does not determine readiness, and governance evidence must remain visible rather than averaged away. PAI reframes agent release from a faith based deployment decision into an auditable readiness decision.

---

### 7. [2607.27853v1] FinanceHarness: Autonomous Financial Deep Research Framework

- **Authors:** Yijia Xiao, Rujun Han, Yanfei Chen, Zifeng Wang, Ke Jiang, Zhongying CuiZhu
- **Published:** 2026-07-30
- **Categories:** cs.CL, cs.AI, q-fin.CP
- **Links:** [Abstract](https://arxiv.org/abs/2607.27853v1) | [PDF](https://arxiv.org/pdf/2607.27853v1)

**Abstract:**  
Powered by advances in LLMs and autonomous agents, deep research has become one of the most widely adopted agentic products. However, most deep research systems write general-purpose reports, which are inadequate for financial deep research. Financial research demands specialized knowledge to analyze historical patterns and forecast upcoming events. Automating financial deep research therefore requires both a layered harness to drive the research agent and a verifiable, point-in-time benchmark that prevents leakage of future information. We present FinanceHarness, a harness that runs finance-oriented tools and practitioner-guided workflows, automating financial deep research end to end: environment and data construction, the agent execution loop, and reward modeling. We further propose FinanceGym, comprising thesis-driven research questions and rubrics that combine pre-cutoff and post-cutoff criteria. Professional expert validation yields an 82% pass rate. Even leading LLMs and agents score below 40% on the rubrics, showing that FinanceGym is challenging and leaves substantial headroom. With the same open-weight backbone, FinanceHarness improves the overall rubric score from 25.3% to 32.4%. FinanceHarness is available at https://github.com/Yijia-Xiao/FinanceHarness.

---

### 8. [2607.28573v1] Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs

- **Authors:** Woongkyu Lee, Jungwook Choi
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28573v1) | [PDF](https://arxiv.org/pdf/2607.28573v1)

**Abstract:**  
Deploying autonomous computer-use agents (CUAs) locally is increasingly important for privacy, cost efficiency, and practical usability, yet improving their performance under strict hardware constraints remains challenging. While recent studies show that inference-time scaling can improve frontier computer-use agents through additional computation during execution, its effectiveness for resource-constrained local models remains poorly understood. We present a systematic empirical study of inference-time scaling in local CUAs across contextual, temporal, structural, and parallel dimensions. We evaluate Qwen3-VL-8B/30B-A3B, UI-TARS-1.5-7B, and OpenCUA-7B on the OSWorld benchmark. Our results show that additional computation often yields diminishing returns while changing failure modes. Contextual scaling provides historical grounding that improves trajectory stability and task accuracy, but its gains saturate as token cost increases and failures shift from repetitive or stalled trajectories toward premature false successes. Temporal scaling similarly reduces max-step stalls, yet does not substantially improve task success, indicating that longer horizons often extend erroneous trajectories rather than correct them. We further find that structural decomposition can introduce planning and formatting overhead in local two-stage agents, while parallel scaling partially mitigates these failures at a substantial computational cost. Overall, our findings suggest that efficient local CUAs require selective compute allocation, failure-aware control mechanisms, and agentic frameworks designed around the capabilities and limitations of local models.

---

### 9. [2607.27973v1] TAPO: Transition-Aware Policy Optimization for LLM Agents

- **Authors:** Cong Li, Peixi Peng, Yisen Zhao, Xinyu Hu, Shudong Liu, Zhan Su
- **Published:** 2026-07-30
- **Categories:** cs.LG, cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.27973v1) | [PDF](https://arxiv.org/pdf/2607.27973v1)

**Abstract:**  
Recently, Reinforcement Learning (RL) has emerged as a crucial paradigm for the post-training of Large Language Model (LLM) agents. However, existing methods predominantly rely on sparse task rewards for policy optimization, failing to fully exploit another class of inherently dense supervisory signals naturally present during online interaction: environmental feedback following action execution. Recent theoretical studies suggest that generalization in multi-step, goal-oriented tasks hinges on predictive knowledge of environmental consequences. Inspired by this, we propose TAPO: Transition-Aware Policy Optimization for LLM Agents, a unified training framework that alternates between policy optimization and transition supervision. Beyond standard RL updates, TAPO repurposes rollout data to apply action-conditioned next-observation prediction supervision on a shared backbone model. This approach enhances the model's sensitivity to environmental transition dynamics and action consequences while concurrently optimizing the policy. It serves as a computationally lightweight, plug-and-play enhancement module for existing agent RL algorithms, requiring no additional expert data, extra sampling costs, or inference-time overhead. We conduct systematic experiments on WebShop and ALFWorld, integrating foundation models of various scales with different policy optimization algorithms. Empirical results demonstrate that TAPO consistently improves task performance over pure policy optimization baselines.

---

### 10. [2607.27929v1] Meta-Task: Turning Terminal Task Synthesis into a Terminal Task for Scalable Agent Training

- **Authors:** Zhihong Pan, Jiyuan He, Kai Zhang, Yupeng Han, Ze Liu, Yuze Zhao
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.27929v1) | [PDF](https://arxiv.org/pdf/2607.27929v1)

**Abstract:**  
Training terminal agents at scale requires diverse, verifiable terminal tasks and high-quality interaction trajectories, yet acquiring such data remains a significant challenge. Existing synthesis methods face two key limitations: (1) weak reliability caused by the disconnect between task generation and real execution, and (2) limited diversity and scalability due to dependence on existing repositories. We propose Meta-Task, a framework that redefines terminal task synthesis as a Terminal-Bench-format task itself: an agent operates within a real container environment to iteratively generate, execute, and verify tasks, so that synthesized components are checked for internal consistency and executability within the generation loop itself. Building upon this, we decouple the target task requirements along multiple dimensions, introduce a multi-phase mechanism that dynamically designs novel task specifications before producing the actual tasks, and incorporate optional external material support to enhance diversity and realism. We additionally apply LLM-as-Judge filtering to ensure the quality of the final training data. Experiments on Terminal-Bench 2.0 show that fine-tuning on only 3,221 Meta-Task synthesized trajectories achieves 22.5% and 31.8% Avg Pass@1 for Qwen3-14B and Qwen3-32B respectively, outperforming concurrent approaches with significantly less training data.

---

### 11. [2607.27733v1] VeriSkill: A Self-Evolution Framework for Program Verification Skills

- **Authors:** Changguo Jia, Tianqi Zhao, Zhiyou Xiao, Weiming Zhang, Minghui Zhou
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.27733v1) | [PDF](https://arxiv.org/pdf/2607.27733v1)

**Abstract:**  
Automating program verification with LLM agents requires generating specifications, annotations, auxiliary lemmas, and tool invocations, all of which depend on reusable skills. A natural remedy is skill self-evolution: distilling skills from trajectories and refining them through feedback. However, existing evolution methods struggle with program verification tasks because they cannot reliably identify skill-specific failures or extract actionable signals from opaque verifier feedback. In this paper, we propose VeriSkill, a self-evolution framework built for program verification. It attributes verification failures to skill deficiencies, distills diagnostic signatures into reusable lessons, and iteratively refines candidate skills, admitting only revisions that improve verification performance while preserving program semantics. Experiments show that VeriSkill consistently outperforms all baselines across multiple verification tools, agent frameworks, and LLM backends.

---

### 12. [2607.28103v1] MIND: Lightweight and Effective Memory Injection Defense for LLM Agents via Intent-Aware Information Bottleneck

- **Authors:** Dongyi Liu, Haixing He, Xiaobao Wu, Jia Li
- **Published:** 2026-07-30
- **Categories:** cs.AI
- **Links:** [Abstract](https://arxiv.org/abs/2607.28103v1) | [PDF](https://arxiv.org/pdf/2607.28103v1)

**Abstract:**  
Memory-augmented LLM-based agents are vulnerable to memory injection attacks: Agents may retrieve poisoned memory from attackers, which diverts their behavior from initial user intent and finally causes task failure. However, existing defense mechanisms either incur high computational cost or suffer from information redundancy in multi-turn contexts. To address these challenges, we propose Memory Intent-Aware Neural Denoising (MIND), a lightweight defense framework for memory injection attack. Our preliminary analysis reveals that benign and poisoned trajectories exhibit distinguishable relationships between the initial user intent and subsequent behavior. Building on this observation, MIND employs an intent-aware Information Bottleneck (IB) to extract compact intent–behavior representations from the initial intent and turn-level behavior. The IB preserves intent-relevant cross-turn attack signals while filtering task-irrelevant and repetitive information, and a lightweight detector identifies malicious memories from the resulting representations. As such, MIND mitigates information redundancy in multi-turn contexts while avoiding the overhead of repeated LLM auditing. Extensive experiments show that MIND reduces attack success rates while preserving task accuracy and inference efficiency. Notably, on ReAct-StrategyQA, MIND reduces mean ASR-r and ASR-a by 55.4% and 55.3%, respectively, while matching the undefended agent in average accuracy and latency.

---

## 🧭 主题速览

| # | 论文 | 一句话核心 | 与 Second Brain 的关联 |
|---|------|-----------|----------------------|
| 1 | OSReward | VLM judge 不可靠有宽松偏差；开源 reward model 平价替代 | Agent 评估的奖励信号设计 |
| 2 | MANTA | 多智能体通信拓扑推理时自进化 | 七大自举系统 → 协作架构自进化 |
| 3 | Σ-Mem | 多智能体可靠性记忆：谁可信、何时可信 | 自举系统的 peer 信任/加权投票 |
| 4 | Benchmarks Mis-Score | 15.3% 的 CUA FAIL 判定是错的 | 评估框架防自欺 |
| 5 | ORCA-bench | 生产级 oncall RCA，最强 agent 仅 25.3% | 可靠性工程差距量化 |
| 6 | ProofAgent Index | 能力≠生产就绪，四维治理指数 | 交付质量门（service-quality） |
| 7 | FinanceHarness | 金融 deep research 闭环 + 防泄漏基准 | Deep research 框架参考 |
| 8 | Local CUA Scaling | 本地推理扩展收益递减、失败模式转移 | RTX 4060 本地部署边界 |
| 9 | TAPO | 动作→下一观测预测作为密集监督 | Agent RL 低成本增强 |
| 10 | Meta-Task | 把终端任务合成本身变成 agent 任务 | 终端 agent 训练数据管线 |
| 11 | VeriSkill | 技能自进化：归因失败→提炼教训→迭代精修 | skill 自举系统直接相关 |
| 12 | MIND | 记忆注入攻击防御（意图感知信息瓶颈） | Agent 记忆安全红线 |

---

## ⚡ 应用到 Second Brain（learn → research → apply）

### 🔴 高优先级（1-2 周）

#### 1. **协作架构自进化**（参考 MANTA）
**实现目标**：
- 七大自举系统里，多智能体协作的通信拓扑（谁负责什么、信息流方向）不再固定
- 任务执行中监控协作轨迹，组织不够时做有界结构调整（改角色/链接/执行顺序/验证路径）

**预期收益**：
- 复杂任务（论文综述、PCB 方案评审）自动重组分工
- 参考其"保留任务接口 + agent 预算"的约束设计，避免架构漂移

---

#### 2. **Peer 可靠性记忆**（参考 Σ-Mem）
**实现目标**：
- 为多智能体系统增加"可靠性记忆"：记录每个 peer 的历史能力证据 + peer 间关系证据
- 用正确性反馈在线更新（Weyl 不等式保证谱变化有界，无需重训）
- 输出三用：中心模型残差引导 / 免响应 peer 路由 / 可靠性加权投票

**预期收益**：
- 多 agent 投票/路由从"盲信"变"按历史信用分配"
- 泛化到未见 peer 和未见任务域（论文验证了 OOD 泛化）

---

#### 3. **Agent 交付质量门升级**（参考 ProofAgent Index）
**实现目标**：
- 现有 service-quality 交付门扩展为四维就绪指数：Evaluation / Context / Compliance / Governance
- 关键洞见：**能力提升行为但不决定就绪**，上下文工程对可靠性影响更大；治理证据必须可见、不能被平均掉

**预期收益**：
- 闲鱼/接单交付从"能用就行"升级为可审计的就绪判断
- 避免"演示通过但生产失败"的信誉风险

---

### 🟡 中优先级（2-3 周）

#### 4. **本地 CUA 扩展策略**（参考 Local CUA Scaling）
**实现目标**：
- 在 RTX 4060 8GB 上跑本地 computer-use agent 时，明确推理扩展的边界
- 关键发现：上下文扩展提升轨迹稳定性但收益饱和；时间扩展只减少卡死不提升成功率；结构化分解有开销

**行动项**：
- 本地部署时优先"选择性计算分配 + 失败感知控制"，而非盲目加算力
- 警惕"过早假成功"这一新的失败模式

---

#### 5. **记忆注入防御**（参考 MIND）
**实现目标**：
- Agent 记忆（Obsidian 知识库、.learnings）防投毒：意图-行为表征检测恶意记忆
- 轻量：避免反复 LLM 审计的算力开销（ReAct-StrategyQA 上 ASR 降 55%，精度延迟不变）

**行动项**：
- 对从网页/共享链接读取后写入记忆的内容，增加意图一致性检查

---

### 🟢 长期跟踪（1 个月+）

#### 6. **Agent RL 过渡监督**（TAPO）
#### 7. **终端任务合成**（Meta-Task）→ 若自建终端 agent 训练管线
#### 8. **技能自进化验证**（VeriSkill）→ skill 自举系统的失败归因机制参考
#### 9. **VLM judge 可靠性**（OSReward / Benchmarks Mis-Score）→ 评估任何 agent 前先审计评估器本身

---

## 📌 值得注意的其他论文（本轮检索副产物）

- [2607.28587v1] PAIChecker: Uncovering and Checking PR-Issue Misalignment in SWE-Bench-Like Benchmarks (cs.AI) — SWE-bench 类基准的 PR-Issue 错位审计
- [2607.28330v1] Paying for Honesty Without Knowing the Truth: Reputation-Penalty Design for LLM Marketplace Agents (cs.AI) — LLM 商家 agent 的诚信声誉机制
- [2607.28520v1] Agents That Certify Their Own Exploits: Confidence-Scheduled Restricted Responses for Safe Opponent Exploitation (cs.AI) — 博弈论视角的安全利用

---

*生成时间：2026-08-03 | arXiv API 自动检索（cs.AI + agent / multi-agent / agentic+tool）| 状态：reading → processed*

**已处理:** 核心贡献精选 3 篇 → 📄 `knowledge/arXiv/arxiv-2026-08-03-core-contributions.md`（MANTA / VeriSkill / MIND）

*Generated automatically via arXiv API cron job. Last updated: 2026-08-03*
