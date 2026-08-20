---
aliases:
  - arxiv-2026-08-20-agent-llm
  - arxiv-agent-llm-2026-08-20
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-20
updated: 2026-08-20
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-20

> **检索时间**: 2026-08-20 GMT+8
> **说明**: arXiv 索引已推进到 08-19T17:58Z（最新 2608.19197 SPADE），脱离 08-17 冻结池。本次收集 08-18 + 08-19 两日时间窗全量（6 类别 × 时间窗），共 **652 篇唯一**，筛选出强相关论文 **20 篇**。
> **数据源**: [export.arxiv.org](https://export.arxiv.org)

---

## 一、Harness 原生 RL 与 Agent 训练（7 篇）

### 1. SPADE: Self-Play in Adaptive Synthetic Executable Environments
- **ID:** [2608.19197v1](https://arxiv.org/abs/2608.19197v1) | [📄 PDF](https://arxiv.org/pdf/2608.19197v1)
- **作者:** Bo Liu, Simon Yu, Yiding Jiang, Ao Qu, Andrew Zhao, Zichen Liu, Junsu Kim, Zijian Zhou, Seungone Kim, Tongzheng Ren, Mickel Liu, Hanfei Yu, Zhaorun Chen, Weiyan Shi, Paul Pu Liang, Luke Zettlemoyer, Yejin Choi, Natasha Jaques (UW, Meta, CMU, 等)
- **分类:** cs.AI, cs.CL
- **摘要:** 自进化需要持续扩张的自生成多样化目标池。现有训练环境池（手工编排、静态合成、冻结验证器）保持目标分布固定。SPADE 让同一个 LLM 扮演两个角色：Environment Designer 用 Gym-style reset()/step() 接口写完整长时程训练环境（可执行代码），Reasoning Agent 在其中学习。Environment Designer 通过优化 agent 的 regret 信号（有/无特权 hint 的奖励差）自动生成处于 agent 能力边界的可行环境。关键组件：在预训练语料文档上 grounding + 累积环境记忆。30B 参数下，SPADE 在 8 个数学/科学/代码/推理基准上平均 +5.3，BFCL-v4 多轮 +5.7，ACEBench-Agent +13.9。
- **关联度:** ★★★★★ 环境设计可学习化——自进化 agent 从「在固定环境训练」到「环境本身被训练」；与 sora 的 harness 自进化主线完全同轴（Zetta/ClawGym II 之后第三个「环境/训练对象可进化」工作）

### 2. Agent Lightning v1.0: Towards Harnessed Agentic RL
- **ID:** [2608.17528v1](https://arxiv.org/abs/2608.17528v1) | [📄 PDF](https://arxiv.org/pdf/2608.17528v1)
- **作者:** Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo (Microsoft)
- **分类:** cs.AI, cs.SE
- **摘要:** 现代 agent 运行在 agent harness 中（管理工具/上下文/控制流），使得 harness 成为 agent 系统的关键组成部分。Agent Lightning 提出解耦架构，通过 LLM 端点代理连接任意 agent 到 RL 训练。**Harnessed agentic RL** 范式：部署时 harness 直接参与模型后训练，与传统 agentic RL 根本不同——harness 拥有环境交互循环，trainer 只看到 LLM 请求-响应对序列。识别 retokenization/sample merging/advantage/loss normalization/后端调度 5 大挑战。v1.0 仅 ~3500 行代码，支持任意 agent harness。Qwen3.5-9B 在 SWE-bench Verified 从 41.8% 提升到 56.4%（+14.6 绝对提升），仅用 6K 训练样本。
- **关联度:** ★★★★★ 与 OpenForgeRL/ClawGym II 同属「harnessed agentic RL」三剑客；Microsoft 开源，与 sora 的 Hermes 训练方向直接相关；skill 知识中已有 OpenForgeRL 铺垫

### 3. LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents
- **ID:** [2608.17393v1](https://arxiv.org/abs/2608.17393v1) | [📄 PDF](https://arxiv.org/pdf/2608.17393v1)
- **作者:** Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, Chaofan Tao, Xianzhi Yu, Lifeng Shang, Kam-Fai Wong, Xiaohui Li, Haoli Bai
- **分类:** cs.AI
- **摘要:** 编码 agent 的 RL 越来越依赖长时程 agent harness（工具/仓库上下文/执行反馈），但原生执行环境与策略梯度训练不兼容：环境崩溃和 reward hacking 污染信号，train-inference 差异解耦 rollout 行为与策略更新。LEGO-RL 三个支柱：①in-process LLM 代理捕获原始生成流做 token 级对齐；②可扩展沙箱编排（镜像缓存+阶段式防御 reward hacking）；③可观测训练插件+Live UI。Qwen3.5-35B-A3B (MoE) 在 OpenHands SDK (64.0%→70.4%)、Claude Code (62.4%→68.2%)、OpenCode (57.2%→66.6%) 三个 harness 上一致提升，rollout-training 概率相关性 >0.99。
- **关联度:** ★★★★★ 与 Agent Lightning 互补——同一「harness-native RL」范式的不同实现；LEGO-RL 侧重编码 agent，与 sora 的 Codex/OpenCode 委派相关

### 4. RTPO: Reverse-Turn Policy Optimization for Stabilizing Agentic RL Training
- **ID:** [2608.18682v1](https://arxiv.org/abs/2608.18682v1) | [📄 PDF](https://arxiv.org/pdf/2608.18682v1)
- **作者:** Yugu Li, Jimmy Cao, Jianglin Qiao, Siyi Hu
- **分类:** cs.AI
- **摘要:** 多轮 agentic 工作流 RL 训练高度不稳定。识别三个耦合根因：rollout-training 上下文不匹配、稀疏终端奖励下弱 turn 级 credit assignment、短/长轨迹在不同策略版本下优化导致的异步漂移。RTPO 提出反向回合公式：多轮 rollout 组织为稀疏反向树，按时间逆序做 turn 级策略更新，对齐每个决策与下游延续。理论保证消除上下文不匹配和异步漂移。多轮 agentic RL 基准比轨迹级和 turn 级基线分别提升 21.50% 和 10.76%。
- **关联度:** ★★★★ 多轮 agentic RL 训练稳定性方法论；与 sora 的 Hermes 多轮 agent 训练相关

### 5. PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs
- **ID:** [2608.17289v1](https://arxiv.org/abs/2608.17289v1) | [📄 PDF](https://arxiv.org/pdf/2608.17289v1)
- **作者:** Dayang Liang, Liyuan He, Xuan Feng, Shuxin Li, Bo An, Yunlong Liu
- **分类:** cs.AI
- **摘要:** GRPO 等组相对策略优化在成功轨迹间无法区分——绕路的成功与高效成功分配相同奖励，导致 advantage collapse。PlanPO 引入 coarse-to-fine advantage 信号，捕获轨迹级长度和 turn 级响应长度的相对差异，让 agent 同时学习交互规划和文本生成中的高效率行为。在 ALFWorld、WebShop、SciWorld 上比 GRPO 平均提升 27.2%，几乎无额外训练成本。
- **关联度:** ★★★★ 多轮 agent 规划的 RL 方法；与组件 4 (RTPO) 互补——一个解结构稳定性、一个解信号质量

### 6. SkillGate: Training In-Policy Skill Selection in Long-Horizon Agents
- **ID:** [2608.18852v1](https://arxiv.org/abs/2608.18852v1) | [📄 PDF](https://arxiv.org/pdf/2608.18852v1)
- **作者:** Qingyao Li, Wenxiang Jiao, Shuai Shao, Kangning Zhang, Yuan Lu, Yi Guo, Weiwen Liu, Weinan Zhang, Yong Yu
- **分类:** cs.AI
- **摘要:** Agent 框架把过程知识打包为 skills（agent 按需读的指令文件），公共库已有数千 skills。但「读哪个 skill」是 episode 中期策略自行做出的决策，没有任何训练信号。识别**selector credit starvation**：广播序列级 advantage 下，命名选中 skill 的少数 token 承担 vanishing loss share，且随轨迹增长 credit 越来越错——正确选择因后续执行失败受罚。SkillGate 通过两个 disjoint credit channel 解决：outcome credit 只到执行 token，action-local advantage 只到 skill 命名 token。9B 模型在 16 候选 slate 下 trial success 从 40.8% 提升到 53.2%，误导候选暴露减少 2/3。
- **关联度:** ★★★★ 直接与 sora 的 skill 库/技能检索相关——skill 选择是 agent 的核心决策点，credit starvation 解释了为什么 outcome reward 难以教会 agent 选对 skill

### 7. What is Missing from AI Post-Training AI: An Empirical Analysis
- **ID:** [2608.19072v1](https://arxiv.org/abs/2608.19072v1) | [📄 PDF](https://arxiv.org/pdf/2608.19072v1)
- **作者:** Joy Jia Yin Lim, Xin Huang, Hao Peng, Yaxi Lu, Xin Cong, Zhong Zhang, Maosong Sun, Yankai Lin
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** LLM agent 可以端到端后训练 LLM——写代码、启动训练、评估 checkpoint、提升下游性能。但实证发现 agent 的训练策略在开始时被锁定，剩余预算全花在选定策略内的局部调整。三类干预：经验驱动 scaffold 提升执行但策略不变；人类指引能重定向初始策略但训练开始后回退到局部调整；额外推理 compute 在简单任务有效但最难任务几乎无收益。结论：agent 缺少的不是经验/指引/推理 compute，而是在执行过程中自发重新评估策略的机制。
- **关联度:** ★★★★ 对「AI post-train AI」的冷静实证——揭示当前 agent 在策略级决策的瓶颈，与 sora 的 Hermes 后训练/self-improving 设计相关

---

## 二、Agent 安全与审计（5 篇）

### 8. HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety
- **ID:** [2608.17597v1](https://arxiv.org/abs/2608.17597v1) | [📄 PDF](https://arxiv.org/pdf/2608.17597v1)
- **作者:** Yajing Bai, Jinhao Duan, Jie Peng, Xianfeng Wu, Sijia Liu, Song Wang, Tianlong Chen (UNC Chapel Hill, UCF, MSU)
- **分类:** cs.AI
- **摘要:** LLM 通过 agent harness 部署，但现有安全基准只关注单一攻击机制或有限操作设置。HarnessRisk 将 harness 安全组织为 **6 个生命周期阶段**：配置/能力扩展/运行时操作/状态持久化/动作控制/事件恢复。128 个沙箱案例，每个配对良性用户目标与嵌入在不受信任工作流产物中的对抗指令。跨越 3 个 harness（**OpenClaw、Hermes、Nanobot**）、6 个模型、14 项配置，ASR 12.6%-80.9%，Utility 75.0%-97.6%。**Harness Configuration 是三个 harness 中最脆弱的阶段**。风险识别率 >90% 的配置仍保留显著 ASR（如 MiniMax M3 on OpenClaw 检测率 97.9% 但 ASR 31.2%）。**注意：Hermes harness 上的 DeepSeek-V4-Pro ASR 高达 65.4%**，与 sora 的 Hermes+DeepSeek 配置高度相关。
- **关联度:** ★★★★★ **本周最与 sora 直接相关的论文**——HarnessRisk 直接评测 Hermes harness，且 DeepSeek-V4-Pro on Hermes 安全表现不佳（ASR 65.4%）；与 sora 的安全配置/代理审批策略直接相关；项目页: [baiyajing.github.io/harness-risk/](https://baiyajing.github.io/harness-risk/)

### 9. One Gate Is Not Enough: Composing Stateful Pre-Action Controls for Agentic AI
- **ID:** [2608.18360v1](https://arxiv.org/abs/2608.18360v1) | [📄 PDF](https://arxiv.org/pdf/2608.18360v1)
- **作者:** Gaston Besanson
- **分类:** cs.AI, cs.SE
- **摘要:** Agentic AI 系统受多个预动作控制（权限/资源/证据门）约束。核心发现：**remediation-induced control coupling**——一个控制应用的 remediation 可能改变另一个控制评估的动作/证据/上下文，使后者的判断失效。提出 remediate-and-regate 协议，在 bounded idempotent 设定下恢复逐动作正确性。两个 remediation 算子（证据替换和资源预算降级）不交换，有限模型检查器找到具体的反例实例。组成不制造新的检测覆盖（诚实声明）。在确定性开源数据上 CH1-CH5 在 30 个预注册种子下达标。
- **关联度:** ★★★★ 与 HarnessRisk 同属「安全需要在整个生命周期评估」主线；与 sora 的 Hermes 多级审批策略相关

### 10. Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents
- **ID:** [2608.18351v1](https://arxiv.org/abs/2608.18351v1) | [📄 PDF](https://arxiv.org/pdf/2608.18351v1)
- **作者:** Alexander Tu, Michael Tu
- **分类:** cs.AI, cs.LG
- **摘要:** 工具使用 LLM agent 可能行使用户未授予或任务不需要的权限（excess-authority errors）。传统权限门控系统不足。研究 post-training 能否教会 4B 模型在终端和 MCP 环境中选择任务条件权限。审计框架：6 个风险维度进行预执行和后执行审核，用确定性验证器打分。后训练后 Qwen3.5-4B 在 2,896 评估 episode 中 safe success 从 64.36% 提升到 98.48%，excess-authority 事件从 4.56% 降至 0.79%。但强调：**不替代权限门和沙箱隔离**。
- **关联度:** ★★★★★ MCP 环境最小权限后训练——与 sora 的 MCP 工具链 + Hermes 权限管理直接相关；补充了「训练时学习权限约束」的可行性证据

### 11. When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling
- **ID:** [2608.17275v1](https://arxiv.org/abs/2608.17275v1) | [📄 PDF](https://arxiv.org/pdf/2608.17275v1)
- **作者:** Rabimba Karanjai, Yang Lu, Nour Diallo, Wujie Xiong, Lei Xu, Weidong Shi
- **分类:** cs.AI
- **摘要:** AI agent 越来越多「行动」而非仅「读取」——MCP 生态中修改外部状态的工具占比从 27% 升至 65%。当 agent 在公链上通过 MCP/skills/tool calling 行使权限，攻击后果由区块链执行层管辖（不可逆性/签名权威/持续自主/序列级组合），量变到质变。整理 MCP-安全文献为攻击面分类法，贡献 Web3 风险映射矩阵（每攻击类→放大影响→放大器→缓解→残余缺口）。实测缓解手段拦截 <30% 攻击，模型级安全拒绝 <3%。
- **关联度:** ★★★★ MCP 攻击面 survey；与 sora 的 MCP 工具链 + 区块链/Web3 兴趣相关；「不可逆损失」视角与常规 agent 安全不同

### 12. LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents
- **ID:** [2608.18398v1](https://arxiv.org/abs/2608.18398v1) | [📄 PDF](https://arxiv.org/pdf/2608.18398v1)
- **作者:** Daehong Kim, Haichao Miao, Shusen Liu (LLNL)
- **分类:** cs.AI
- **摘要:** LLM agent 执行长时程技术工作流（工具调用/代码执行/文件编辑/产物生成），产出瓶颈从生产转向审计。LEDGER 构建分层 trace 图：Trace Records → Evidence Nodes → Workflow Nodes，制品作为证据锚点，加上语义边连接 claim 到支持性动作/产物/检查。通过数据分析与编码示例展示 trace 暴露工作流决策、制品谱系、修复步骤、验证覆盖和 claim-支持路径。
- **关联度:** ★★★★ 与 sora 的交付验证/审计理念相关——LEDGER 的 evidence-centered audit 与 08-19 的 HarnessEval-W 证据树同属「可审计 agent 执行」主线

---

## 三、Agent 评估与鲁棒性（5 篇）

### 13. Grading the Graders: Verification Autonomy Levels (L0-L5) for LLM Reasoning
- **ID:** [2608.19009v1](https://arxiv.org/abs/2608.19009v1) | [📄 PDF](https://arxiv.org/pdf/2608.19009v1)
- **作者:** Yajie Yin
- **分类:** cs.CL
- **摘要:** LLM 越来越多 paired with verifiers（步骤检查器/自洽过滤器/工具事实检查器/形式化证明助手），但文献中「level」指至少 5 种不同事物。提出 **Verification Autonomy Levels (VAL)** 元标准：验证 spec 从哪里来，verdict 保证什么。L0（LLM 自声明，无确定性锚点）→ L2（客观 ground truth，仅正确性）→ L3/L4（可判定系统，单属性/域级完备性），L5 在无限制情况下不可能。核心：**完备性盲区**——substitution/sampling 验证器可确认候选成立但不能证明无遗漏候选。形式化可规约属性才可达完备性，经验性开放世界验证（事实核查/诊断）上限为 L2。跨 4 个领域（符号数学/行为监控/医学诊断/代码生成），基于 17 篇调查论文。
- **关联度:** ★★★★ 验证元标准框架——与 sora 的 Hermes 验证/评测体系设计相关；VAL 的「完备性盲区」点出了验证器基本局限

### 14. A Jagged Frontier: Evaluating Robustness of Code Agents to Semantics-Preserving Transformations
- **ID:** [2608.18389v1](https://arxiv.org/abs/2608.18389v1) | [📄 PDF](https://arxiv.org/pdf/2608.18389v1)
- **作者:** Hasan Najib Mahmud, Shreya Gupta, Isha Chaudhary, Nathaniel Enis, Ravi Mangal, Gagandeep Singh, Corina Pasareanu (CMU / UIUC)
- **分类:** cs.AI
- **摘要:** 代码 agent 在代码库被语义等价改写（控制流重写/死代码注入/标识符重命名）后可靠性如何？4 个 frontier 模型（Claude Opus 4.5/Kimi K2.5/MiniMax M2.5/Qwen 3.6-27B）× 2 个 scaffold（mini-SWE agent/OpenCode）在 SWE-bench Verified/Pro 上评估。多数配置小退化（最多 6.7pp），但**没有跨 scaffold 的鲁棒性排名**——Qwen 在 mini-SWE 下最鲁棒、在 OpenCode 下最脆弱。简单 scaffold 更鲁棒。揭示「jagged robustness frontier」。
- **关联度:** ★★★★ 代码 agent 部署可靠性；与 sora 的编码 agent 委派（Codex/Claude Code/OpenCode）相关；jagged frontier 发现说明鲁棒性是 scaffold × model 联合属性

### 15. ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents
- **ID:** [2608.18307v1](https://arxiv.org/abs/2608.18307v1) | [📄 PDF](https://arxiv.org/pdf/2608.18307v1)
- **作者:** Tianchen Guan, Xinlei Lin, Royce Cheng-Yue, Xiangjun Wang, Shuyan Zhou (CMU)
- **分类:** cs.AI, cs.CL
- **摘要:** CUA 评估在长时程工作流基准和原子 GUI 测试之间留下未检测的中间层：真实组件级交互（如切换按钮组）——短到可诊断、丰富到可捕捉现代界面负担。ComponentBench 包含 97 个规范 UI 组件（2,910 个编程验证任务）和人工参考轨迹。7 个模型 + 4 种观察/动作空间评估：**仅改变观测/动作空间，同模型任务成功率差 >30%**（GPT-5 mini 从 83.1% 辅助树观测降至 48.9% 纯像素控制）。最快配置仍比人工参考慢 3.7×。
- **关联度:** ★★★★ CUA/浏览器 agent 组件级评估——与 sora 的 Hermes desktop 插件/浏览器自动化相关；obs/action space 选择对性能影响巨大

### 16. On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification
- **ID:** [2608.18066v1](https://arxiv.org/abs/2608.18066v1) | [📄 PDF](https://arxiv.org/pdf/2608.18066v1)
- **作者:** Qinyuan Ye, Yu Li, Yada Pruksachatkun, Jiaxin Zhang, Chien-Sheng Wu (Salesforce)
- **分类:** cs.AI, cs.LG, cs.CL
- **摘要:** 记忆型自改进 agent 从在线任务流学习并维护文本记忆库。但可靠性方面被严重忽视。多运行评估揭示：①agent 评估在复杂环境中本身有噪声，自改进循环放大噪声；②改进高度依赖任务顺序（默认顺序隐含课程，是成功的隐藏前提）；③任务和环境的 underspecification 是脆弱性的根因。加入详细 rubric 和环境反馈部分缓解但仍有显著差距。呼吁更严格的评估协议。
- **关联度:** ★★★★ 与 SPADE 形成对照——SPADE 在「如何让自进化可行」、Fragility 在「为什么自进化可能不可靠」；给 sora 的 self-improving agent 设计提供重要警示

### 17. Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck
- **ID:** [2608.18931v1](https://arxiv.org/abs/2608.18931v1) | [📄 PDF](https://arxiv.org/pdf/2608.18931v1)
- **作者:** Davide Romano, Kanak Raj, Jerrod Parker, Daniele Giofrè
- **分类:** cs.AI, cs.CL
- **摘要:** TTS 在数学/代码上大获成功，但几乎只在验证简便的任务上测试。首次在 5 个开放域生成基准（医学/法律/金融/通用聊天/创意写作）上做 compute-normalised 比较。分解 token 预算为探索和利用。**探索有效**：候选池最优稳步提升。**利用崩溃**：SOTA reward model 与真实质量相关性仅 ρ≈0.12，选择近随机。树搜索因多样性崩溃放大失败。精炼在 1/5 基准有效。只有 Fusion（跨候选合成）一致改善但仅恢复 ~40% 可用质量。结论：候选池不是瓶颈，选择才是。
- **关联度:** ★★★★★ 对 TTS 信任度的关键警示——开放域利用瓶颈意味着 sora 的模型路由/评测系统不能依赖 reward model 做选择；与 Hermes 的 smart_model_routing 验证直接相关

---

## 四、Agent 应用与工作流（3 篇）

### 18. Eureka: Task-Conditioned Meta-Agent Orchestration for Scientific Discovery
- **ID:** [2608.19047v1](https://arxiv.org/abs/2608.19047v1) | [📄 PDF](https://arxiv.org/pdf/2608.19047v1)
- **作者:** Alizer Wong, Heng Cui, Yi Tan, Xiongchao Zhan, Liang Lin, Yuxiang Guo, Zhaorong Dai, Zixin Zeng, Wenyuan Li
- **分类:** cs.AI
- **摘要:** 科学发现 meta-agent 架构：编译长时程任务为动态义务图（显式接受语义）；运行时形成 Macro-Agent（专用状态/记忆/算子/工具/验证器/局部拓扑）；瓶颈复发时做 cost-benefit-gated 架构更新。理论建立 regret/planning invalidation/amortization 等结果。实验：170/170 递归任务完成，生成 3,948 证书零假阳性；上下文压缩到 4,005 tokens（中位数），增量处理避免 65.38% 重计算。同一架构实例化 Theory-Discovery Agent（量子过程/时空理论结构结果）和 Math/Conjecture Agent（Riemann 假设研究瓶颈识别 + Suzuki 局部 Weil 二次型正性证到 0<a≤69/200=0.345 ≈ 99.55% 的 (log 2)/2）。
- **关联度:** ★★★★ 科学发现 agent 架构设计；与 sora 的 research 自动化/知识吸收相关；义务图 + Meta-Agent 模式可借鉴

### 19. SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution
- **ID:** [2608.18933v1](https://arxiv.org/abs/2608.18933v1) | [📄 PDF](https://arxiv.org/pdf/2608.18933v1)
- **作者:** Silin Chen, Han Li, Xiaodong Gu, Yuling Shi, Haibing Guan
- **分类:** cs.AI, cs.SE
- **摘要:** LLM agent 编码 issue 解决缺乏项目特定知识。现有自进化方法依赖历史 issue-resolution 信号或在线修复轨迹，成本高。SkillForge 通过**重实现测试覆盖的核心功能**合成项目特定 issue → 解决它们 → 蒸馏为实体接地技能（entity-grounded skills）→ 关联到仓库实体供未来 issue 使用。开源和闭源模型实验一致提升 issue 解决性能。
- **关联度:** ★★★★ 与 SkillGate(组件6)互补——一个选 skill、一个造 skill；与 sora 的编码 agent 技能蒸馏/知识库沉淀相关

### 20. StagedWorkspace: A Versioned Workspace for Knowledge-Work Agents
- **ID:** [2608.18050v1](https://arxiv.org/abs/2608.18050v1) | [📄 PDF](https://arxiv.org/pdf/2608.18050v1)
- **作者:** Yining Hua, Hongbin Na, Yifan Zhou, Akshay Kalose, Cyrus Ayubcha, Levi Lian
- **分类:** cs.AI
- **摘要:** AI agent 执行知识工作（产生/修改代码/文档/表格/幻灯片/报告），但搜索的解析视图、编辑的原生文件、审查的 diff、提交的制品可能指代不同版本。提出 **workspace-state contract**：每个视图必须显式绑定到工作区状态的版本。StagedWorkspace 绑定解析记录和审查 diff 到原生文件内容哈希。在 OfficeQA Pro 和 APEX-Agents 上，双视图（parsed+native）比单视图提升 8.3-12.1 点。SW-AGENT 在 OfficeQA 达 63.9%（vs 公布基线 29.3%）。标记 workspace state 为知识工作 agent 的实验变量。
- **关联度:** ★★★★★ 与 sora 的闲鱼业务直接相关——文档/PPT/表格/报告的知识工作恰恰是 sora 的代做业务核心；版本化工作区可以提升交付质量

---

## 本周值得关注的主题信号

1. **Harnessed agentic RL 成为独立子领域**：本周 SPADE（环境设计可学习化）+ Agent Lightning v1.0（Microsoft 开放）+ LEGO-RL（三 harness 训练）+ OpenForgeRL（前序）——四篇独立工作在同一周出现，标志 harnessed RL 从零散方法走向独立子领域。每个提出不同的「training-harness interface」：proxy/API 边界/沙箱/反向树——但核心共识一致：部署时 harness 应直接参与训练，而非被重新实现。

2. **Agent 安全进入「生命周期评估」时代**：HarnessRisk（直接评测 Hermes）+ One Gate（组合控制耦合）+ Task-Conditioned Least-Privilege（MCP 最小权限后训练）+ Web3 MCP（攻击面分类）——安全不再只是 prompt injection 或 jailbreak，而是配置/能力/运行时/持久化/动作/恢复的全生命周期问题。**Heremes 的 HarnessRisk 安全结果是 sora 的 1 号信号**（DeepSeek-V4-Pro on Hermes ASR 65.4%）。

3. **TTS 的开放域瓶颈**：Test-Time Scaling in the Wild 实证发现利用（exploitation）是开放域瓶颈，reward model 相关性仅 0.12——即使是 SOTA 模型的选择能力近乎随机。这挑战了 TTS 在内容生成场景的适用性，与 sora 的模型路由/评测系统设计直接相关。

4. **自改进 agent 从「能做」到「可靠」的转折**：SPADE（环境可进化，理论保障）+ Fragility of Self-Improving Agents（方差/任务顺序/underspecification 警示）——一边推进自进化能力边界，一边揭示当前方法的可靠性隐患。两篇对照阅读是本周最佳视角。

5. **Agent 评估：从标量分到结构化诊断**：ComponentBench（组件级故障诊断）+ LEDGER（证据 trace 图）+ VAL 验证级别（完备性盲区）——评估正在从「一个分数+pass/fail」走向「结构化诊断+证据链」。与 sora 的 service-quality 交付门/验证循环理念一致。

---

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]