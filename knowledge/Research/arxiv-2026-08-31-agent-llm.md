---

aliases:
  - arxiv-2026-08-31-agent-llm
  - arxiv-agent-llm-2026-08-31
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-31
updated: 2026-08-31
status: adopted
source: export.arxiv.org API

---

# arXiv AI Agent / LLM 速览 — 2026-08-31（⚠️ 补全性质）

> **检索时间**: 2026-08-31 GMT+8
> **⚠️ 补全性质声明**: arXiv 索引自 08-19T17:58Z 冻结后于本周恢复推进，当前全局最新 **08-28T17:56Z（2608.28583）**。上一份速览（08-21）只覆盖 08-18/19 同池；本次对 **08-20→08-28 累计 9 天窗口（3071 篇唯一）** 做全量比对，从 1255 篇标题命中 AI/LLM 的论文中精选 28 篇强相关 + 14 篇简评，不重写已收录内容。08-29 起窗口为空（索引尚未推进到 08-29）。
> **数据源**: [export.arxiv.org](https://export.arxiv.org)

---

## 一、Agent 技能系统与自演化（5 篇）

### 1. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

- **ID:** [2608.27454v1](https://arxiv.org/abs/2608.27454v1) | [📄 PDF](https://arxiv.org/pdf/2608.27454v1)
- **作者:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
- **分类:** cs.AI, cs.CL
- **摘要:** 技能演化中指导技能改进的洞见通常散落在优化历史里，无法跨轮次复用。WikiSkill 把智能体工作区拆成三层——不可变的原始执行轨迹层、结构化累积知识层（wiki）、可执行技能层——由 Inference Agent / Wiki Maintainer / Skill Proposer / 门控回滚四组件构成持续循环：经验持续沉淀进 wiki，后续技能更新在其上生长，技能更新可回滚但 wiki 永不回滚。在 5 基准 × 5 模型上持续优于既有技能演化方法：技能演化与模型缩放互补（大模型获益更多，但小模型+好技能可反超大模型无技能）；演化技能跨模型/跨模型族迁移有效，他模型演化出的技能可优于自演化；消融证实持久知识累积是增益关键（Skill Proposer 有无 wiki 访问 = 48.7% vs 63.7%）。受 Karpathy "LLM Wiki" 观点启发，是目前对"智能体记忆应为 wiki 形态"最清晰的表述。
- **关联度:** ★★★★★ 直击 k 的 skill-evolution / LLM Wiki 主线——wiki 形态持久记忆正是知识库该有的形态

### 2. SPT: Skills as Pre-Training Data for Agentic Language Models

- **ID:** [2608.26563v1](https://arxiv.org/abs/2608.26563v1) | [📄 PDF](https://arxiv.org/pdf/2608.26563v1)
- **作者:** Yufei Sun, Yudong Li, Yiming Cheng
- **分类:** cs.CL
- **摘要:** 工具型（agentic）语言模型主要在 post-training 阶段用工具调用轨迹训练，但轨迹数据需真实环境、执行与验证，覆盖贵且有限。公开的多文件 skill 包编码了可复用工具语义与工作流，却只被当作推理时上下文。SPT 提出把 SkillCorpus（公开多文件 skill 包集合，可混入通用数据）当作 mid-training 数据做因果语言建模；并提出 Reference Insert——把支撑文件放到主指令被提及处附近的引用感知组装策略，保留包内文件关系。多模型规模与多种 post-training 配方下，SPT 一致优于在通用或轨迹数据上的 mid-training，且基本不损通用能力；与通用 annealing 语料混合还有额外增益。
- **关联度:** ★★★★ "技能即训练数据"——把 skill 从上下文搬到权重里，与 sora 的 skill 体系 + 本地小模型路线直接相关

### 3. SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents

- **ID:** [2608.24747v1](https://arxiv.org/abs/2608.24747v1) | [📄 PDF](https://arxiv.org/pdf/2608.24747v1)
- **作者:** Shidong Yang, Ziyu Ma, Tongwen Huang, Xucong Wang, Renda Li, Yiming Hu, Yong Wang, Xiangxiang Chu
- **分类:** cs.CL
- **摘要:** 多数 RL 训练的智能体是"情景式"的，无法跨 episode 积累可复用知识。SkillRL 从原始轨迹抽技能，但把技能库当"只追加仓库"，从不验证存量技能是否仍有效。SkillForge 让技能在环境交互中被验证与精炼：使技能调用显式化，RL 同时优化环境动作与技能调用决策；引入基于证据的技能验证 + 多路径技能归纳，让技能库在持续增长的同时保持质量。在 ALFWorld、WebShop、AppWorld 上一致优于 SkillRL。
- **关联度:** ★★★★ 技能库"验证而非只追加"——对应 k 的知识吸收/技能维护里"过时技能清理"痛点

### 4. When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents

- **ID:** [2608.22339v1](https://arxiv.org/abs/2608.22339v1) | [📄 PDF](https://arxiv.org/pdf/2608.22339v1)
- **作者:** Zihan Lin, Zhenyu Chen, Jiawen Wei, Xiaohan Wang, Jie Cao, Jiajun Chai, Wei Lin, Guojun Yin, Ran He
- **分类:** cs.CL
- **摘要:** 自演化智能体默认假设"从成功轨迹蒸馏技能会单调提升能力"，但探测发现这会让模型陷入 **Skill Imitation Trap**：任务看似像过去的成功却需要不同工具时，检索越多技能反而越自信地调用错误工具（procedure skills 比无记忆基线把错误工具边际提高 47%）。BASM 给每个技能显式附加边界字段——适用条件、风险提示、规避规则、恢复笔记——把技能从无条件动作模板变成状态条件化指引：条件成立才应用、不成立则抑制、执行失败则定向修复。在 AppWorld 任务成功率最高 +23.8%，BFCL 精度最高 +5.0%，AgentDojo 攻击成功率 -4.6%。
- **关联度:** ★★★★ 给 k 的技能/提示词加"适用边界"字段的实证依据——检索式技能（含 Hermes skill 触发条件）都存在误用风险

### 5. Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents

- **ID:** [2608.20274v1](https://arxiv.org/abs/2608.20274v1) | [📄 PDF](https://arxiv.org/pdf/2608.20274v1)
- **作者:** Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
- **分类:** cs.AI, cs.CL
- **摘要:** 智能体能从已完成任务归纳技能并复用于成长，但归纳出的技能可能迁移不可靠甚至伤害检索它的智能体。本文对技能迁移做受控研究：比较 task-level vs subtask-level 归纳、text vs code 技能格式。任务级技能大多把性能压到无记忆基线之下，子任务级技能平均拉高；文本技能比代码技能迁移更好。提出 skill utility score（特异性 × 抽象性），只需技能与任务描述即可在跑任何新任务前诊断技能记忆质量，无需执行。
- **关联度:** ★★★ 技能"怎么归纳"决定"能不能迁移"——对 k 的跨任务技能复用设计有直接参考

---

## 二、Agent RL 训练与工具使用（5 篇）

### 6. MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning

- **ID:** [2608.22167v1](https://arxiv.org/abs/2608.22167v1) | [📄 PDF](https://arxiv.org/pdf/2608.22167v1)
- **作者:** Ziyang Luo, Yan Yang, Xiangru Jian, Ziji Shi, Xiaoqiang Lin, Jun Hao Liew, Silvio Savarese, Junnan Li
- **分类:** cs.AI, cs.LG
- **摘要:** 多数 RL 框架在策略更新处止步，新域要么手动搭数百并发轨迹的隔离环境并接训练，要么在长多轮 episode 卡在慢工具调用上空转 GPU。MCP-U RL（Salesforce，Apache-2.0 开源，MCP-Universe 2508.14704 的后续）用 MCP 作为统一环境接口：任何已暴露为 MCP server 的工具零 RL 集成代码直接接入训练；一次性构建环境编排层（容器后端弹性供给/隔离/回收）与 rollout 编排层（三阶段流水线：acquire→run→evaluate，分阶段并发重叠掩盖工具等待，run 阶段 worker ≥ 2× acquire）；训练层后端无关（veRL / slime 适配）。同一配置只改任务规格，即在 gpt-oss-20b 上训出软件工程、深度研究、通用工具三个智能体并全部提升任务奖励；解耦 rollout 阶段吞吐 ×2.8。
- **关联度:** ★★★★★ sora 用 MCP + 有 4060 本地 GPU——"用 MCP 统一环境训练工具智能体"与多智能体协作/本地微调路线强相关（已验证，开源可复用）

### 7. SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning

- **ID:** [2608.19842v1](https://arxiv.org/abs/2608.19842v1) | [📄 PDF](https://arxiv.org/pdf/2608.19842v1)
- **作者:** Dayang Liang, Lang Feng, Bo An, Yunlong Liu
- **分类:** cs.AI
- **摘要:** 现有 critic-free / group-relative 方法（如 GRPO）避开了 PPO 的大显存开销，但有三大局限：缺显式价值泛化与时间信用分配、长程任务优势崩塌、采样预算与策略性能难权衡。SAPO 让策略与价值函数共享单一自回归骨干：利用 LLM 自回归结构在不同因果边界上产出策略与价值预测，独立优化 PPO 目标 + 辅助 on-policy SARSA 目标；再引入结合 λ-returns 与 batch normalization 的轨迹级广义优势估计器。在 ALFWorld/WebShop 用 Qwen2.5-1.5B/7B，比 PPO/GRPO 平均高 +15.1/+12.1 pp，同时省掉独立 critic 的显存，单次迭代运行时间比 PPO 降 33.2%。
- **关联度:** ★★★★ 单 rollout + 共享骨干的省钱 Agent RL——对 8GB 显存的本地 RL 微调路线很有价值

### 8. EDGE: Experience-Distillation for Guided Exploration in Agentic Reinforcement Learning

- **ID:** [2608.21946v1](https://arxiv.org/abs/2608.21946v1) | [📄 PDF](https://arxiv.org/pdf/2608.21946v1)
- **作者:** Can Xie, Yuyi Zhou, Wen Yang, Ziyi zhang, Siyao Song, Yingzhuo Deng, Shuo Ren, Jiajun Zhang
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** GRPO 等基于结果的 RL 让智能体解决长程任务，但轨迹里可复用的探索模式在一次策略更新后就被丢弃；现有经验增强方法在推理时检索历史，却不考虑策略能力演化、且依赖外部检索。EDGE 把检索经验当作临时训练脚手架，逐步内化进参数策略：把每个 rollout 组切成经验条件化/无经验两组，估算并只采纳正向边际增益（不多采样）；再用 reverse-KL 目标在自身经验支撑上把诱导行为蒸馏进基础策略。协同演化的经验库随策略演化合成新失败模式指引、剪除过时条目。在具身/网页/搜索 QA 任务上比强 RL 基线最高 +12.5 分，推理时不需脚手架或专有 reflect。
- **关联度:** ★★★★ 经验"蒸馏进权重而非每次检索"——与记忆外置 vs 参数内化的权衡主线直接相关

### 9. SMITH: Joint Optimization of Tool Creation and Use for LLM Agents

- **ID:** [2608.24571v1](https://arxiv.org/abs/2608.24571v1) | [📄 PDF](https://arxiv.org/pdf/2608.24571v1)
- **作者:** Zhi Rui Tam, Chieh-Yen Lin, Yun-Nung Chen, Shao-Hua Sun, Hung-yi Lee
- **分类:** cs.AI, cs.SE
- **摘要:** 工具增强 LLM 被"人类愿意写的 API"束缚；现有工具创建系统在推理时提示冻结 LLM，写工具的模型与用工具的模型解耦。SMITH 在单一策略内联合训练工具创建与使用：每个 rollout 是 build 任务（照例子写工具）或 use 任务（在池化工具上解留出题）。三维奖励轴分别捕捉 schema / code / 结果失败。4B Qwen3 训 13 个带精确验证器的程序推理任务，留出任务 79.8 宏平均准确率，胜过未训练 30B-A3B 工具写手；TabMWP-Hard 40.4、跨域 GQA 42.6（比最佳同骨干推理时基线 +7.6），且无需视觉/表格训练数据。
- **关联度:** ★★★★ "工具创建与使用一体训练"——让模型写自己调得动的 schema，对 k 的自建工具链有启发

### 10. MidTool: Mid-training Data Synthesis for Agentic Tool Use

- **ID:** [2608.20314v1](https://arxiv.org/abs/2608.20314v1) | [📄 PDF](https://arxiv.org/pdf/2608.20314v1)
- **作者:** Fengqing Jiang, Yite Wang, Boyi Liu, Zhaoyang Wang, Canwen Xu, Zhewei Yao, Radha Poovendran, Yuxiong He
- **分类:** cs.AI
- **摘要:** mid-training 已被证明能强化推理密集型能力与软件工程 agentic 能力，但通用工具使用这一条线少有人做。MidTool 是面向 agentic 工具使用 mid-training 的开放语料构建流水线：大规模 web/PDF/代码数据 + 来自真实工具 API、MCP skills、文档落地工作流的合成监督，教模型识别工具 affordance、从上下文落地参数、组合工具调用工作流、从不完整信息恢复。在 Qwen3-4B/8B-Base 上 mid-train 后接 SFT 与 RL，BFCL、tau2-Bench、MCP Universe 一致提升——通用工具使用也受益于专门的 mid-training 而非全交给 post-training。
- **关联度:** ★★★☆ "工具使用需要专属 mid-training"——与 SPT（技能做训练数据）互为补充的证据链

---

## 三、多智能体协作（5 篇）

### 11. The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate

- **ID:** [2608.22152v1](https://arxiv.org/abs/2608.22152v1) | [📄 PDF](https://arxiv.org/pdf/2608.22152v1)
- **作者:** Weixiang Sun, Zehong Wang, Hong Huang, Colby Nelson, Yanfang Ye
- **分类:** cs.CL
- **摘要:** 两个 LLM 必须协作而非各自单干时，性能损失多少？本文把协作税形式化为带私有信息的双人合作博弈的"团队去中心化损失"，给出两个命题刻画其符号与 max-superadditivity 违反的等价性；在 32 个单人可解任务、11 个模型（7 家供应商）上实证。结果：协作税沿两条无例外轴结构化——跨所有模型的类别排序、随能力单调下降；近端机制不是推理缺陷而是四阶段对话级联（无依据断言、不追问伙伴、不整合双方、不重新推导就接受答案）。提示词干预针对四阶段可关闭相当一部分差距；异质配对中税被拉向较强伙伴而非中点。
- **关联度:** ★★★★★ 量化"多智能体协作的代价"——k 的多 agent 协作（WorkBuddy/dsh/Gemini）该把协作税计入成本与设计

### 12. Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation

- **ID:** [2608.25277v1](https://arxiv.org/abs/2608.25277v1) | [📄 PDF](https://arxiv.org/pdf/2608.25277v1)
- **作者:** Pratyay Banerjee, Ankit Chadha
- **分类:** cs.AI, cs.CL
- **摘要:** 多智能体 LLM 系统靠自然语言消息协作，消耗 40–60% 的 token 预算；换结构化图省成本却在需自适应推理的任务上失败。Routed Graph Handoff 让轻量 LLM 路由器（155 token，0.15% 开销）为每次委派在类型化依赖图与自然语言间选格式。4 基准（1050+ 轨迹）上路由系统每项都匹配或超过纯 NL：τ-retail +12.7pp（3.2× 压缩）、BrowseComp +8.7pp（2.2×）、BFCL/AppWorld 持平；无路由器时纯图在 AppWorld 回退 14.6pp，路由器近零成本消除之。需图感知执行提示词；oracle 分析显示还有 8.6pp 空间，指向执行时自适应路由。
- **关联度:** ★★★★ 委派格式自适应选择——多 agent 通信 token 优化的实用方案，对应 dsh/多代理编排的成本控制

### 13. ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs

- **ID:** [2608.25992v1](https://arxiv.org/abs/2608.25992v1) | [📄 PDF](https://arxiv.org/pdf/2608.25992v1)
- **作者:** Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang
- **分类:** cs.AI
- **摘要:** 多智能体工作流反复调用 LLM、长程上下文累积，成本高；现有 cascade 路由做一次性查询级决策，无法适应多步工作流的状态依赖（每步该用哪个 LLM 取决于任务进展、剩余难度、成本效率）。ProgRouter 做在线进度引导路由：多视角任务进度评分器（粗粒度结果体制 + 细粒度子任务完成/趋势/状态质量信号）+ 双路径进度预测器 + 自适应元门控，逐步入轨选择 LLM，平衡进度增益、时间预算与长期成本效率。在 HumanEval Plus、MBPP、MATH-500、ASQA 上，相对关键基线降低运行成本同时保持强任务表现。
- **关联度:** ★★★★ "按进度动态路由模型"——直接对应 k 的 smart_model_routing 演进方向（本地/云端按任务状态切换）

### 14. Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems

- **ID:** [2608.25920v1](https://arxiv.org/abs/2608.25920v1) | [📄 PDF](https://arxiv.org/pdf/2608.25920v1)
- **作者:** Zhongwen Luan, Xiaoyu Zhang, Ming Hu, Yue Yang, Jiongchi Yu, Xiaohong Chen
- **分类:** cs.AI, cs.SE
- **摘要:** 现有多智能体系统（MAS）调试/修复方法常重跑+重采样整条轨迹——这到底是因果修复还是靠 LLM 采样随机性"随机修复"？SymTrace 是受控评估框架：记录执行轨迹、建立干预锚点，重放时用日志重建锚点前执行、只重新生成下游轨迹，可靠复现 MAS 失败；配套 SymFail 数据集含 536 条人工标注失败轨迹（图链接位置/类别/痕迹证据）。三套主流 MAS 框架大规模实证：无引导重跑极不可靠——失败复现率仅 67.97%、修复率仅 6.90%；症状驱动干预方法修复 20.15% 失败案例（比 SOTA 修复方法提升 191.89%）。
- **关联度:** ★★★★★ 直击 k 的 multi-agent 排障痛点——"重跑撞运气 vs 症状驱动修复"，验证了 Hermes 3连败即停/重新分析的合理性

### 15. Consilience: Conformally Calibrated Communication Control for Hidden-Profile Multi-Agent Reasoning

- **ID:** [2608.20564v1](https://arxiv.org/abs/2608.20564v1) | [📄 PDF](https://arxiv.org/pdf/2608.20564v1)
- **作者:** Abhijith Babu, Ramneet Kaur, Vishal Pramanik, Olivera Kotevska, Nathaniel D. Bastian, Susmit Jha, Sunny Raj, Yanzhao Wu, Sumit Kumar Jha, Anirban Roy
- **分类:** cs.AI
- **摘要:** 隐藏档案（hidden-profile）场景每个 agent 只持部分证据，多智能体通信协议（固定排程/轮询/无结构辩论）无法保证某次对话动作是否恰当。Consilience 是推理时编排框架：用压缩状态（不确定性/分歧/证据增益/冗余/过早共识）总结讨论，每轮选通信干预（challenge/clarify/seek evidence/route）与发言者；核心贡献是逐轮 conformal 校准——分布无关、有限样本保证每轮一步遗憾以 ≥1-α 边际概率被校准阈值约束，接受机制把不合格提案替换掉。12 个开闭源模型在 HiddenBench 式任务上提升决策精度与通信效率，有时超过全信息基线。
- **关联度:** ★★★☆ 带统计保证的通信控制——多 agent 该何时/对谁说话的形式化，偏理论但对编排设计有参考

---

## 四、Harness 架构与工程（3 篇）

### 16. The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses

- **ID:** [2608.23953v1](https://arxiv.org/abs/2608.23953v1) | [📄 PDF](https://arxiv.org/pdf/2608.23953v1)
- **作者:** Dai Jiahong
- **分类:** cs.SE
- **摘要:** agent harness 是把 LLM 变成自主 agent 的外围代码（构上下文、中介工具、跑循环、跨长程持久状态），正日益成为 agent 行为的绑定约束。这是对三个哲学对立的开源编码 agent harness 的源码级多案例研究：LangChain deepagents（电池全含）、Earendil pi（激进极简）、DeepSeek dsh（一切皆插件）。两个成熟 harness 反向演化（deepagents 减自带脚手架、pi 累积持久基建）却收敛到同一中间形态的五要素：商品化循环、append-only 可重放会话记录、模型怪癖当数据、上下文渐进披露、显式扩展接缝。第三个（held-out）五要素齐备且在某一接缝直接复用了另一个的实现；收敛拆解为平行发现、扩散与字面复用。唯一无收敛且缺席的承重维度：外部可验证性（不信任运行时也能查证的防篡改记录）——预判为溯源敏感领域下一个分化轴。
- **关联度:** ★★★★★ 直接解剖 dsh（sora 主力 harness）与 pi/deepagents 的架构收敛——append-only 日志/AGENTS.md/渐进披露正是 k 日常依赖的机制（已验证，GitHub discussion 有 pi2dsh 呼应）

### 17. Harness Engineering for Predictable Agentic Systems: An Empirical Study of Deterministic Execution Constraints

- **ID:** [2608.26197v1](https://arxiv.org/abs/2608.26197v1) | [📄 PDF](https://arxiv.org/pdf/2608.26197v1)
- **作者:** Saransh Dhage
- **分类:** cs.SE
- **摘要:** LLM agent 即使任务工具相同也有显著 run-to-run 执行方差，探索可用但受监管域（金融/合规）不可接受。本文研究 harness 工程：用确定性执行层（有限状态控制、强制工具选择、输出验证、有界重试、结构化规划）包住 agent 并测对确定性与成功率的影响。两个合成任务（金融/法律）× 两个开源模型（Qwen-2.5-7B、Gemma-3-27B）：第一版 harness 结果混合（4 个模型-任务格中 1 显著改善复现、2 显著恶化）；轨迹级诊断发现工具/状态/输出已高度一致时，未约束的自由文本规划成为最大方差源；加 Structured Planning（调任何工具前先按固定 schema 验证计划）彻底消除：3/4 格复现率与确定性指数在 N=100 达 1.000，成功率 3/4 格到 100%；token 成本每格都降，但延迟按模型一快一慢。
- **关联度:** ★★★★ "harness 工程"是独立可靠性命门——确定性执行层/结构化规划正是 k 可落地到编排层的低成本加固手段

### 18. Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering

- **ID:** [2608.24271v1](https://arxiv.org/abs/2608.24271v1) | [📄 PDF](https://arxiv.org/pdf/2608.24271v1)
- **作者:** Zahra Seyedghorban, Egor Klimov, Arie van Deursen, Annibale Panichella, Burcu Kulahcioglu Ozkan
- **分类:** cs.SE
- **摘要:** 基于 LLM 的多智能体系统难检查、难调试、难在受控故障下评估。llmmas-otel 是轻量框架无关工具：OpenTelemetry 分布式追踪 + 故障注入，跨工作流阶段/agent 步/agent 间通信/工具调用/LLM 调用对齐遥测，并支持在选定交互点定向注入故障，使基线 vs 故障执行可复现对比。
- **关联度:** ★★★ 可观测性 + 故障注入——对 k 的多 agent 排障（联机/多代理调试）是可借鉴的追踪设计

---

## 五、安全、越狱与鲁棒性（4 篇）

### 19. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

- **ID:** [2608.27141v1](https://arxiv.org/abs/2608.27141v1) | [📄 PDF](https://arxiv.org/pdf/2608.27141v1)
- **作者:** Chenhao Wu, Haoxuan Jia, Yang Liu, Yingguang Yang, Yuhan Lin, Chongyang Zhang, Hao Zheng, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Shang Luo, Kefu Xu, Jifeng Zhu, Bin Chong
- **分类:** cs.AI
- **摘要:** LLM agent 越来越以自主循环部署：从一个人工目标出发，反复发现工作、规划、执行工具、验证、跨多次无人值守迭代持久状态。而现行安全防护定义在单条轨迹上、每条轨迹开始就重置安全状态——这是组合失败而非实现细节。核心分离定理：面对跨多迭代碎片化证据的攻击，任何轨迹级监控器的真阳率=假阳率（无论多强）；保留跨迭代状态的监控器能完美分离（TP=1, FP=0）。几何衰减风险分也救不了——耐心攻击者要等的冷却期是常数、不随视界 N 增长。LoopHarness 在循环级恢复持久非衰减安全状态：五块永不重置的状态（intake/provenance 监控、跨迭代风险累积器 xrc 且循环结构证据触发即闩锁、内存完整性守卫、对抗鲁棒停止仲裁、复合风险治理器）；在仲裁检测下限 δ_M 下把未授权不可逆动作期望数上界压到与 N 无关的常数 B+m-1+m/δ_M，其中模型无关部分即使验证器完全合谋也成立。
- **关联度:** ★★★★★ 对无人值守自动循环（cron/自主 agent）的安全建模——轨迹级防护不组合、需跨迭代非衰减状态，直接关系到 k 的 cron 与自主执行安全设计

### 20. SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents

- **ID:** [2608.21929v1](https://arxiv.org/abs/2608.21929v1) | [📄 PDF](https://arxiv.org/pdf/2608.21929v1)
- **作者:** Yuanjin Zheng, Jingbang Chen
- **分类:** cs.CL
- **摘要:** Agent skills 给编码 agent 扩展任务指令/脚本/资源，也创造了可被滥用的"受信指令通道"。本文研究 skill 注入下的 token 放大——经济型资源滥用威胁：恶意 skill 让 agent 为正常任务消耗远超需要的 token。SkillBloat 两阶段：先筛选攻击类型条件库（跨多种放大机制），再通过 LLM 引导的全文档 skill 重写精炼最强候选。真实 skill 基准上多编码 agent 配置平均放大 5.42×–10.15×；第二阶段精炼循环一致提升 Phase-1 攻击类型筛选。
- **关联度:** ★★★★ skill 生态暴露资源放大攻击面——对 sora 装第三方技能的安全意识（成本侧攻击不亚于恶意代码）

### 21. MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection

- **ID:** [2608.19901v1](https://arxiv.org/abs/2608.19901v1) | [📄 PDF](https://arxiv.org/pdf/2608.19901v1)
- **作者:** Yue Wang, Yi Liu, Gelei Deng, Ying Zhang, Yuekang Li, Zhenyu Chen, Leo Zhang
- **分类:** cs.AI
- **摘要:** Agent Skills 是含脚本/资源/服务配置的可复用指令包，成为恶意行为直接分发渠道。MaliciousSkillBench 整合 13 个公开源（11 个贡献核心恶意产物），把 8,414 条原始恶意记录归一为 7,539 个唯一身份、4,588 个操作结构族；保守排除跨标签冲突后主基准 9,740 个 Skill（7,505 恶意 / 2,235 良性）。评估 3 个学习式文本检测器 + 3 个现成扫描器：学习式随机 Macro-F1 0.882–0.932，但 Source-Disjoint 评估只剩 0.653–0.665；最强 TF-IDF SVM 0.932/0.916/0.665，保持 95.6% 恶意召回却产生 62.4% 良性 FPR——可靠检测需更广跨源覆盖 + 同时测攻击检出与良性误报。
- **关联度:** ★★★★ 恶意 skill 检测基准——sora 装第三方技能（GitHub 400K+ 技能市场）前的安检参考，跨源泛化仍是大缺口

### 22. ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

- **ID:** [2608.21101v1](https://arxiv.org/abs/2608.21101v1) | [📄 PDF](https://arxiv.org/pdf/2608.21101v1)
- **作者:** Kai Wang, Zeming Wei, BiaoJie Zeng, Chang Jin, An Wang, Xiaokun Luan, Zhixiao Lin, Jingjing Qu, Xia Hu, Xingcheng Xu
- **分类:** cs.AI
- **摘要:** agentic 风险是渐进式的，可在 agent 控制环的四个位点进入（skill 准入、调用时意图、执行时效果、动作后后果），被拒的危险目标可跨表面形式/工具/轮次重现；现有防护通常只覆盖单一生命周期边界或单次调用。ClawSentry 是开源框架无关的安全监督网关：skill 执行前 First-use Skill Package Review（FSPR）在确定性证据下限下审计，未决升级为有界只读 agentic 审查；运行时三层渐进决策引擎（确定性 L1 / 规则锚定 L2 语义审查 / 只读 L3 取证 agent）只对残余歧义花上下文审查；会话级反绕过识别工具切换与改写重试；Agent Harness Protocol 抽象不改 agent 内部即在 Codex/Claude Code/Kimi CLI/Gemini CLI 上应用同一策略。SkillInject 上上下文 ASR 从 39.55%→2.61%（TSR 83.78%→83.05%）；SkillsSafety 五 Work Agent 上 ASR 从 33.5–49.7% 压到 9.09–15.03%。
- **关联度:** ★★★★ 渐进式多层级安全网关 + 跨 harness 策略抽象——对应 sora 技能安检（skill-vetter）的工程化升级方向

---

## 六、Agentic RAG 与推理（3 篇）

### 23. MetaRAG: Belief-Action Aligned Policy Optimization for Agentic RAG

- **ID:** [2608.24214v1](https://arxiv.org/abs/2608.24214v1) | [📄 PDF](https://arxiv.org/pdf/2608.24214v1)
- **作者:** Qiuyi Qi, Tian Liang, Jiamu Wang, Jinjian Zhang, Wei Zhou, Pengcheng Zhu, Linjian Mo, Ming Kong, Jie Liu, Qiang Zhu
- **分类:** cs.AI
- **摘要:** agentic RAG 要模型决定何时继续搜索、何时作答。现有 RL 方法靠外部监督、忽略模型"当前证据是否充分"的内部信念。MetaRAG 把搜索决策质量重述为信念-动作对齐：Verify-first Action Generation 在每个真实动作前引出显式验证过程，Internal Belief Probing 从同一问题-历史上下文估计策略自身的可答性信念；据此导出一致性奖励并再用答案正确性门控，避免强化"内部一致但错误"的轨迹。信念探针只在训练用、推理零开销。7 个公开 QA 基准上一致改善精度-效率权衡，增益迁移到深度研究设置/不同优化器/多骨干。
- **关联度:** ★★★★ "内部信念"参与搜索决策——RAG 何时停止检索的自我校准，与 sora 的检索/知识吸收链路相关

### 24. GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrieval-Augmented Reasoning

- **ID:** [2608.22479v1](https://arxiv.org/abs/2608.22479v1) | [📄 PDF](https://arxiv.org/pdf/2608.22479v1)
- **作者:** Jun Chen, Yongchao Liu, Pengyu Qiu, Jiajun Zheng, Juelu Zhang, Yujie Zeng, Qin Zhang, Ziyue Qiao, Xiao Luo
- **分类:** cs.CL, cs.LG
- **摘要:** 多跳问答把 RAG 变成反复检索整合证据的迭代过程；现有 agentic RAG 的 RL 用最终答案奖励，监督稀疏、忽略模型是否真的取回所需证据链。GTA-RAG 从实体-文档图采样连通文档路径、合成多跳 QA 轨迹、用已部署检索器验证得到可执行的轨迹级监督；再用 GRPO + 轨迹引导奖励优化检索策略（同时鼓励答案正确与取回目标证据文档），之后在自然 QA 实例上做答案奖励训练。Qwen2.5-3B/7B 骨干、3 多跳 + 2 简单 QA 基准上一致优于 RL 版 RAG 基线，且显著提升证据链覆盖。
- **关联度:** ★★★☆ 用"证据链"做轨迹级监督——比最终答案奖励更细的 RAG 训练信号，对 k 的检索增强链路设计有参考

### 25. Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI

- **ID:** [2608.26442v1](https://arxiv.org/abs/2608.26442v1) | [📄 PDF](https://arxiv.org/pdf/2608.26442v1)
- **作者:** Md Jueal Mia, M. Hadi Amini
- **分类:** cs.AI, cs.CL
- **摘要:** 现有推理控制多是固定或预分配的（固定 token 预算、预先难度估计、激活空间干预），且常在独立推理基准而非完整 agentic 工作流上评测。agentic 系统里推理需求经规划/工具使用/记忆检索/agent 间交互动态演化，推理会过量或不足：不必要计算、延迟上升、规划漂移、过度工具使用或不完整解。本文把 over/under-reasoning 刻画为推理错配的复发失败模式，在 MATH-500 与 GAIA 验证集上用工具决策延迟、token 消耗、token 上限耗尽、答案正确性评测：over-reasoning 关联更高计算成本而无比例精度增益，under-reasoning 关联错误或不完整解。
- **关联度:** ★★★☆ 推理量要按任务需求分配而非固定——对 k 的 reasoning_effort=high 偏好给出"何时该降档"的思考框架

---

## 七、评测基准（3 篇）

### 26. AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement

- **ID:** [2608.20318v1](https://arxiv.org/abs/2608.20318v1) | [📄 PDF](https://arxiv.org/pdf/2608.20318v1)
- **作者:** Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** 递归自改进（RSI）的关键是 agent 能否设计训练算法（目标/更新规则/正则/调度）——更好的算法改变算力-能力兑换率，让后续每次训练（包括产出下一个 agent 的那次）都继承增益（Adam/LN/DPO/GRPO 都付过一次钱持续受益至今）。但没有基准隔离这一层：现有套件靠收集数据或调超参取胜。AI4AI-Bench = 10 个冻结研究仓库、覆盖 10 个训练算法族（SFT/多轮 agentic RL/on-policy 蒸馏/BT 奖励建模/偏好优化/扩散 RL/机器遗忘/离散图扩散/权重平均/一次性剪枝）。每任务 agent 4 小时在单张 B300 上改写训练算法，其代码从头重跑至多 12 小时由隐藏评估器按统一尺度打分（0=无信息模型, 0.1=仓库原算法, 1.0=任务最优）。29 配置 × 6 系统全 10 任务均值 0.166、最强 0.250——最强也只闭合了"已有算法→最优"不到 1/5 的距离；263 份改动中 141 份完全没碰学习过程（只动预算/checkpoint/超参/容量），碰了算法层的 122 份均值 0.226 vs 0.126；更多推理努力主要买到"愿意去动算法层"（占比 8%→64%，均值 0.094→0.196）。
- **关联度:** ★★★★★ 隔离"算法设计层"的 RSI 基准——sora 的 AI4AI/自我改进主线核心测量，结论"多数 agent 不敢动学习过程"是对自改进工程的清醒提醒

### 27. AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling

- **ID:** [2608.26623v1](https://arxiv.org/abs/2608.26623v1) | [📄 PDF](https://arxiv.org/pdf/2608.26623v1)
- **作者:** Abhigya Verma, Amit Kumar Saha, Seganrasan Subramanian, Sai Harshitha Aluru
- **分类:** cs.AI
- **摘要:** LLM judge 被广泛用于评测 agentic 工具调用，但它在结构化、依赖驱动工作流上的可靠性几乎没被检验。AgentJudgeBench 是首个系统研究 agentic 工具调用（工作流 DAG）上 LLM-as-a-judge 可靠性的基准：3,808 实例、6 种 DAG 拓扑、3 难度档，5 个生成器（3B–70B 开源 + GPT-5.4）× 6 个 judge（20B 到前沿）在有/无 ground truth 配对下评测。法官对齐随难度单调退化、无 ground truth 时快 1.5×；最难无 ground truth 时六法官全收敛到 77–82% 窄带——结构性上限由任务难度驱动、模型容量无法突破。暴露 ground truth 并非总有益（GPT-5.4 -1.5pp、Gemini-2.5-Pro -3.9pp，符合过度锚定）；CoT 与温度几乎无效，结构化评估 rubric 最高 +6.5pp 但不统一泛化。QwQ-32B 最接近程序化参考，人类验证显示 GPT-OSS-120B 最像人。
- **关联度:** ★★★★ LLM 评测法官有结构性天花板——对 k 用 LLM 当评测/质检（服务质检、交付门）的校准参考

### 28. Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling

- **ID:** [2608.26199v1](https://arxiv.org/abs/2608.26199v1) | [📄 PDF](https://arxiv.org/pdf/2608.26199v1)
- **作者:** Leonardo Liparulo, Francesco Pierri
- **分类:** cs.AI, cs.SE
- **摘要:** 本地部署 LLM 能否可靠自动化专家定义的硬件设计工作流？工业场景里工程师通过专门工具做重复、依赖有序的操作（建元件、加端口、接线），组件规格与命名受保密约束、常禁托管专有 API，故用本地模型。作者建了一个复现专有硬件设计工具状态与依赖逻辑的 MCP server，构造覆盖单操作编辑、多步依赖链、非法请求、拼错提示、多 server 工具上下文的基准，评测 7 个开源模型，比较系统提示词、工具描述粒度、上下文范围、单/多 agent 架构。强模型能近完整覆盖期望调用，但可靠性强依赖任务结构与 agent 配置：完整工具描述一致降失败、few-shot 提示会让部分模型严重"不作为"、累积上下文伤受限模型、多 agent 分解帮弱 worker 或长会话但多花调用。
- **关联度:** ★★★★ 硬件设计自动化 + MCP——与 sora 的 PCB/EDA agent 自动化（KiCad/EasyEDA MCP）路线直接呼应，含"完整工具描述""多 agent 权衡"实操结论

---

## 八、简评（其余值得注意）

| # | ID | 论文 | 一句话 |
|---|---|---|---|
| 1 | [2608.24302](https://arxiv.org/abs/2608.24302v1) | VideoHarness-RSI | 把长视频理解做成"可执行上下文构造程序"的递归搜索（RSI），冻结 VLM 下自动找 harness——harness 是独立优化层 |
| 2 | [2608.22793](https://arxiv.org/abs/2608.22793v1) | TRACE: A Self-Evolving Skill Bank | 轨迹对比演化 + 技能库，GPT-5.5 上 Pass^3 59.9%→94.5%，CAR-bench 官方隐藏集第一（GPT-5.6-Sol, 70%） |
| 3 | [2608.27439](https://arxiv.org/abs/2608.27439v1) | RedEvoAgent | 黑盒红队 agent：把跨案例攻击轨迹蒸馏为可读攻击技能，工具有效性画像 + 验证棘轮演化 |
| 4 | [2608.19993](https://arxiv.org/abs/2608.19993v1) | Optimal Skill Selection with Bicriteria Guarantees | 技能选择首个可证明双准则 (1-1/e,1) 近似（BPS），BigCodeBench 0.73 vs 0.20–0.52、省 28% token |
| 5 | [2608.20614](https://arxiv.org/abs/2608.20614v1) | ACES: Agentic Continuous Evaluation of Skills | NVIDIA 技能评估框架：活体配对试验测 Skill Lift（均值 0.2134），结构扫描与 LLM judge 互补（ρ=0.14） |
| 6 | [2608.21808](https://arxiv.org/abs/2608.21808v1) | MCite-RL | 多模态 RAG 引用增强 RL：迭代检索+递归裁剪让引用变成证据驱动推理过程 |
| 7 | [2608.26004](https://arxiv.org/abs/2608.26004v1) | AsymSpec | 非对称投机解码：轻量 drafter 读全量、大 verifier 读压缩视图，agentic 场景 ~90% 全上下文精度、1.3–1.7× 吞吐 |
| 8 | [2608.24017](https://arxiv.org/abs/2608.24017v1) | WebMCP-Phalanx | 浏览器集成 agent 信任边界：能力凭证绑定工具主体 + 双 agent 隔离，80 次 prompt 注入全拦 |
| 9 | [2608.24069](https://arxiv.org/abs/2608.24069v1) | Poisoning Agentic Alpha | 多智能体交易系统首个系统性投毒研究：无架构天然鲁棒，数据/提示层即可达成低门槛攻击 |
| 10 | [2608.26237](https://arxiv.org/abs/2608.26237v1) | CTF-ABACUS | CTF 评估从"数旗子"转向轨迹级溯源验证：仅 62–87% 旗子有实证利用支撑 |
| 11 | [2608.26867](https://arxiv.org/abs/2608.26867v1) | BekchiAI | 13 个 ReAct agent / 2057 确定性任务测 agentic 技能 + 实时观测控制平台 |
| 12 | [2608.23035](https://arxiv.org/abs/2608.23035v1) | MobilePA-Bench | 移动规划 agent 基准：13 功能域 212 真实工具，子 agent 协作/记忆/技能三维评测 |
| 13 | [2608.23179](https://arxiv.org/abs/2608.23179v1) | NetConfArena | 闭环网络配置基准：96 协议模板 × 480 实例，失败不止命令错误、还有规范遵循缺口 |
| 14 | [2608.24650](https://arxiv.org/abs/2608.24650v1) | Simthesizer | agent 驱动 LLM 服务模拟器：自然语言需求→可组合动态图，吞吐误差 2.51% vs 6.03% |
| 15 | [2608.20631](https://arxiv.org/abs/2608.20631v1) | Weighted Memory Tree | 层次化记忆 + 动态保留分，GAIA-Text 平均 +9.97pp、省 32.8% prompt token，抗记忆投毒 |
| 16 | [2608.22963](https://arxiv.org/abs/2608.22963v1) | Buried in Textual Debt (SPARE) | 多模态工具 agent 上下文剪枝：KL 引导去冗余推理文本、保留视觉证据，去 37.9–64.6% 推理 token |

---

## 本周关键信号

1. **技能系统成为 Agent 主线**：WikiSkill（wiki 形态持久记忆）、SPT（技能当训练数据）、SkillForge/BASM（技能需验证与边界）、RedEvoAgent/TRACE（技能自演化）——"技能 = 智能体最便宜的成长杠杆"已成共识；且 WikiSkill 直接呼应 Karpathy 的 LLM Wiki 观，与 sora 的 knowledge 库/技能体系同频。
2. **多智能体协作被"计税"**：The Collaboration Tax 把协作损失形式化为可测成本，Interaction Tax（2608.23541，ICML2026）证明全量交互一轮就抹掉模型多样性——"少交互、独立生成 + 定向评审"才是稳健默认；k 的多 agent 协作应主动核算协作税。
3. **Harness 收敛与安全缺口**：deepagents / pi / dsh 收敛到同一中间形态（append-only 会话记录、AGENTS.md 渐进披露、显式接缝），但"外部可验证性"全员缺席——这正是溯源敏感域的下一战场；LoopHarness 则证明自主循环安全需要跨迭代非衰减状态。
4. **RSI 的现实体温**：AI4AI-Bench 显示最强 agent 也只闭合"已有算法→最优"的 1/5，多数提交根本不敢改学习过程——自改进从"改数据/超参"到"改算法层"还有巨大鸿沟。
5. **安全攻击面转移到 Skill 层**：SkillBloat（token 放大）、MaliciousSkillBench（恶意技能检出跨源泛化差）、WebMCP-Phalanx（浏览器信任边界）——装第三方技能的安全成本正在成为 agent 生态的核心风险。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| WikiSkill 2608.27454 | web_search（arxiv.org/HTML + alphaXiv + DAIR.AI） | ✅ Google 团队（Tang/Rashtchian/Ferng/Tomkins/Juan/Vu）；无官方仓库 |
| The Empire 2608.23953 | web_search（arxiv.org + GitHub discussion #1023） | ✅ 确认 dsh/pi/deepagents 三 harness 分析；dsh 实为 service-locator 事件源架构 |
| Safety Does Not Compose 2608.27141 | web_search（arxiv.org/abs + HTML） | ✅ 确认 LoopHarness 与上界定理；cs.CR 有 replaced 版 |
| MCP-Universe RL 2608.22167 | web_search（arxiv HTML + GitHub/Salesforce） | ✅ Salesforce 开源 Apache-2.0，MCP-Universe 2508.14704 后续，veRL/slime 集成 |
| The Collaboration Tax 2608.22152 | web_search（arxiv abs + 相关 Interaction Tax 2608.23541） | ✅ 确认 32 任务/11 模型；姐妹篇 Interaction Tax 已投 ICML2026 |
| AI4AI-Bench 2608.20318 | web_search（arxiv abs/PDF/alphaXiv） | ✅ 确认 10 仓库/29 配置均值 0.166、最强 0.250 |
| 其余 22 篇 | arXiv API 收录 + 抽取完整元数据 | ✅ API 收录即存在性证据（2026-08-07 既定原则） |

## 可落地行动项

- 🔴 **技能安检升级**：把 SkillBloat / MaliciousSkillBench 的威胁模型并入 skill-vetter——装第三方技能时除恶意代码外，还要查"token 放大/资源滥用"与跨源泛化局限（技能安检现覆盖恶意代码为主，成本侧攻击是空白）
- 🟡 **多智能体编排核算协作税**：借鉴 Collaboration Tax 四阶段级联（无依据断言/不追问/不整合/不重推导）+ Interaction Tax"独立生成优于全量交互"，优化 WorkBuddy/dsh/Gemini 联合工作流：先独立产出再合成，避免全量互读
- 🟡 **Harness 学习**：读 The Empire 全文，对照 dsh 的五要素收敛结论（append-only 日志/渐进披露/显式接缝），评估 k 的编排层是否缺"外部可验证性"这一轴
- 🟢 **待深读**：WikiSkill（wiki 三层架构可借鉴到 knowledge 库）、AI4AI-Bench（RSI 测量）、LoopHarness（跨迭代安全状态）、AgentJudgeBench（LLM 评测天花板）→ 建议进 core-contributions 候选

---

*本速览由 cron 自动生成：08-20→08-28 九日窗口全量收集（3071 篇）→ 关键词过滤（1255）→ 人工精选（28 主条目 + 16 简评）→ 关键论文交叉验证。数据源 export.arxiv.org。*
