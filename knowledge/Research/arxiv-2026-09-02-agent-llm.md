---
aliases:
  - arxiv-2026-09-02-agent-llm
  - arxiv-agent-llm-2026-09-02
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-02
updated: 2026-09-02
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-09-02

> **检索时间**: 2026-09-02 GMT+8
> **窗口**: 08-31 → 09-01 两日（arXiv 索引自 08-30T08:17Z 推进至 09-01；上一份 09-01 速览只覆盖到 08-30，本次为新窗口首次收录）
> **收集**: 6 类别时间窗全量 → 08-31 578 篇 + 09-01 452 篇唯一 = **1030 篇**
> **精选**: 关键词命中 496 篇 → 人工筛出 **35 主条目 + 17 简评**（仅保留 LLM/AI Agent 本体相关，剔除离题 CV/调度/博弈/物理）
> **数据源**: [export.arxiv.org](https://export.arxiv.org)

---

## 一、Agent 记忆与知识管理（6 篇）

### 1. Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems

- **ID:** [2609.00237v1](https://arxiv.org/abs/2609.00237v1) | [📄 PDF](https://arxiv.org/pdf/2609.00237v1)
- **作者:** Rakibul Hasan Rajib, Mengxing Zheng, Qian Lou
- **分类:** cs.AI, cs.CL
- **摘要:** 多 agent 编排的核心矛盾：只按 query 路由看不到中间进展或错误（伤准确率）；按完整执行历史路由虽补上缺失上下文，却强迫后续决策处理每一个先前步骤（含冗余低效的），执行历史过载、成本膨胀。Gated-Memory Routing 让每个决策同时条件于 query 与一个**可学习执行记忆**——Memory Write Gate 只提交非冗余推理步，学到的检索机制从紧凑执行记忆中取有用进展，把编排决策从"完整历史"降维到"非冗余状态"。
- **关联度:** ★★★★ 多 agent 编排的"执行状态压缩路由"——k 的多 agent 协作/任务路由可直接借鉴"只保留非冗余执行状态"而非喂全量历史

### 2. EM²Mem: Event-Centric Multimodal Memory for Large Language Models

- **ID:** [2609.00551v1](https://arxiv.org/abs/2609.00551v1) | [📄 PDF](https://arxiv.org/pdf/2609.00551v1)
- **作者:** Yijun Chen, Yaqi Zheng, Yanya Li, Boyi Xiao, Buqiang Xu, Shuofei Qiao, Jizhan Fang, Xinle Deng, Yunzhi Yao, Xuehai Wang 等（13 人）
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** 多模态记忆常用于长视频 QA，但现有方法把字幕/帧/转写/摘要/图事实当孤立片段检索——可搜索但"未生成就绪"：语言模型必须在推理时、上下文受限且溯源困难的情况下重建跨模态与时间对齐。EM²Mem 在记忆构建期把异构证据**绑定到事件锚点**：每个事件索引的记忆单元对齐多模态记录、时间上下文、图关联关系、语义事实与溯源，实现"基于接地多模态事件的紧凑证据读取"而非模态特异片段。三个长视频 QA 基准上平均准确率提升。
- **关联度:** ★★★★ "事件锚点绑定多模态证据 + 溯源"——与 k 的多模态/视频内容吸收、证据分级 A-D / TBHC 溯源纪律直接呼应

### 3. UTILMEM: Benchmarking Evidence Utilization in Long-Term Conversational Memory

- **ID:** [2608.30508v1](https://arxiv.org/abs/2608.30508v1) | [📄 PDF](https://arxiv.org/pdf/2608.30508v1)
- **作者:** Peijun Qing, Fobo Shi, Soroush Vosoughi
- **分类:** cs.CL
- **摘要:** 长时记忆基准大多只测"逐点事实回忆"（能否恢复孤立事实/事件细节），但真实记忆使用需要更难的能力：把**跨长历史分布、隐含、有噪的证据**整合成连贯、面向任务的输出——memory utilization。UtilMem 含 1,717 实例、5 域，评估记忆利用四个被忽视的维度：密集历史上的推理、隐含相关记忆的识别、把分布式证据综合成摘要/分析/计划、抵抗语义相似干扰。
- **关联度:** ★★★★ "记忆利用 ≠ 事实回忆"——给 k 的记忆质量评估提供"把分散证据整合成任务输出"的维度，比点状召回更有实用判别力

### 4. Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents

- **ID:** [2609.01272v1](https://arxiv.org/abs/2609.01272v1) | [📄 PDF](https://arxiv.org/pdf/2609.01272v1)
- **作者:** Jinqing Zhao, Chengcan Wu
- **分类:** cs.AI
- **摘要:** 前瞻记忆 = 在继续其他工作的同时、于正确未来线索上执行延迟意图。基准已把它孤立成 agent 技能，但前沿 LLM 仍吃力：最佳已发布 PM-Bench scaffold 只有 65.1% Set-F1。作者论证这是"模式约束的状态跟踪"而非开放推理，小模型在**类型化动作空间**下也能执行：Prospective Intention Store (PIS) 把生命周期逻辑放进代码、把范围化的语言工作留给模型——agentic 且免训练（无 selector 微调、无轨迹蒸馏）。PM-Bench 上 DeepSeek-Chat + PIS 达 **82.9%** Set-F1；Gemma-E2B 无 store 4.2%、七条回溯记忆至多 6.6%，PIS 达 66.2%。
- **关联度:** ★★★★ "类型化动作空间让小模型做前瞻记忆"——k 用 SLM 处理小任务可直接借鉴"把生命周期逻辑沉淀进代码，模型只做窄范围语言工作"

### 5. Invalidation Contracts for Cross-Episode Agent Memory

- **ID:** [2609.00243v1](https://arxiv.org/abs/2609.00243v1) | [📄 PDF](https://arxiv.org/pdf/2609.00243v1)
- **作者:** Michael Wu, Arquimedes Canedo
- **分类:** cs.AI
- **摘要:** agent 缓存 API 错误恢复建议可跨 episode 复用，省 token 和模型调用；但服务器端数据漂移会让缓存修复静默失效，而"每 episode 重新推导"又把节省全部还回去。Invalidation contracts 是协议层：给每条恢复建议附**版本戳 + 可缓存性提示**，客户端无需试错即可驱逐过期条目、保留其余。契约把实现节省分解为两个独立因子：有效性（漂移事件后仍正确的比例，只取决于协议、与厂商无关）与合规性（planner 首次即采用的比例）。
- **关联度:** ★★★★ 缓存失效协议——k 的自动化任务/知识缓存防陈旧可直接套"版本戳 + 失效契约"，比"定期全量重建"省得多

### 6. Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents

- **ID:** [2608.31057v1](https://arxiv.org/abs/2608.31057v1) | [📄 PDF](https://arxiv.org/pdf/2608.31057v1)
- **作者:** Le Chen, Zishen Wan, Baixi Sun, Xiaolong Ma, Chih-Hsuan Yang, Feng Yan, Sheng Di, Franck Cappello, Rajeev Thakur
- **分类:** cs.AI
- **摘要:** agent 工作记忆是异构的：指令/工件/工具输出/agent 生成状态语义角色不同、规模/保留/表示各异，近年才开始有考虑这种异质性的管理机制研究。对 55 条归档编码 agent 轨迹分析发现：语义不同的工作记忆对象呈现不同的保留与压缩行为，因此需要**语义知情的管理**。研究两种策略：对象感知压缩策略与检索式策略；评估显示校准收益可能不会自动转化为端到端提升。
- **关联度:** ★★★ "先测再管"——k 对编码 agent/长任务的上下文管理可借鉴"按对象语义分治压缩"，而非一刀切截断

---

## 二、Agent 技能系统与自演化（6 篇）

### 7. EvoSkill Injection: Red-Teaming Autonomous Skill Generation and Evolution in Self-Evolving Agents

- **ID:** [2608.30429v1](https://arxiv.org/abs/2608.30429v1) | [📄 PDF](https://arxiv.org/pdf/2608.30429v1)
- **作者:** Doyun Kim, Chanwoo Kim, Sugyeong Eo, Yeo-Chan Yoon, Chanjun Park
- **分类:** cs.AI, cs.CL
- **摘要:** LLM agent 系统越来越多采用基于技能（skill-based）的架构以降重复推理成本、提升稳定高效执行。自进化 agent 从过往经验自主生成、精炼、复用技能以实现持续能力进化——但自主技能进化引入新攻击面：**恶意能力被生成、存储、复用为合法技能**。本文把 EvoSkill Injection 定义为针对自进化技能生成/进化管线的威胁模型，并提出 SARGE——通过迭代生成、升级、强化交互评估该威胁的红队框架，配套构建 Evo...数据集支撑。
- **关联度:** ★★★★★ 直击 k 的 skill 体系安全——"技能管线本身是攻击面"，与 skill-vetter 的安全前置校验直接呼应，外部技能必须过审查

### 8. ARISE-RL: Agentic Rubric-Grounded Iterative Self-Evolution with Reinforcement Learning

- **ID:** [2609.01058v1](https://arxiv.org/abs/2609.01058v1) | [📄 PDF](https://arxiv.org/pdf/2609.01058v1)
- **作者:** Fanrui Zhang, Ruixue Ding, Qiang Zhang, Xi Chen, Boli Chen, Shihang Wang, Qiuchen Wang, Hongmin Zhan, Jinxin Bian 等（11 人）
- **分类:** cs.AI
- **摘要:** 用 RL 训练开放长程 agent 被"缺乏可验证金标 + 可扩展 rubric"阻碍；且即便接近模型能力边界，长程开放 agentic 任务也常给脆弱不稳的奖励，组相对策略学习的对比信号弱而有噪。ARISE-RL 提出全周期自进化框架：任务/rubric Generator 与推理 Solver 通过 **rubric 中介共进化**——Generator 把工具相关 rubric 标准接地到真实工具观测，被奖励产出"有效、中间难度、与 Solver 能力边界对齐"的任务；Solver 从细粒度 rubric 满足信号学多步推理与工具使用。
- **关联度:** ★★★★★ "rubric 中介的生成器-求解器共进化"——与 k 的 service-quality 质量门、rubric 显式化思路同频，且解决"开放任务无金标"的 RL 落地

### 9. AgentFactory: Towards Automated Agentic System Design and Optimization

- **ID:** [2609.01045v1](https://arxiv.org/abs/2609.01045v1) | [📄 PDF](https://arxiv.org/pdf/2609.01045v1)
- **作者:** Enci Zhang, Haofeng Wang, Yuesheng Zhu, Xiaole Cui, Guibo Luo
- **分类:** cs.AI
- **摘要:** 手动设计/优化 agentic 系统高度依赖人工，限制适应性与可扩展性；近期工作探索自动优化工作流设计，但常忽略模型能力这一关键角色、只盯单一性能指标，不回应真实部署约束。AgentFactory **联合优化基座模型 + 工作流结构**，把性能、成本、效率作为多目标一并考虑，用高级 LLM 作优化器导航"模型×结构"的巨大搜索空间。
- **关联度:** ★★★★ "联合优化模型+结构、多目标"——k 的模型路由/成本优化（哪层用便宜模型）可借鉴"把成本和效率写进目标函数而非事后砍"

### 10. Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents

- **ID:** [2609.00549v1](https://arxiv.org/abs/2609.00549v1) | [📄 PDF](https://arxiv.org/pdf/2609.00549v1)
- **作者:** Seonghyeon Cho, Chanjun Park
- **分类:** cs.CL
- **摘要:** 标准评估混淆"检索技能是否真有用"：聚合指标比较检索 vs 未检索任务引入严重选择偏差，无法隔离技能使用的真实效果。作者形式化 Skill Following (SF) 能力，提出 **RAE（Retrieval-Invoked Actual-Use Effect）**——只在 agent 主动检索技能的任务上，计算匹配的技能启用 vs 禁用执行之间的同任务结果差。17 个 LLM、编码与数学两域评估揭示悖论：模型常呈正聚合检索增益但 RAE 为负——MBPP+ 上多个看似整体受益的模型实际在伤害自身表现。
- **关联度:** ★★★★★ 直击 k 的 skill 评估——"聚合提升 ≠ 真用上了技能"，RAE 可成为 k 判断自身技能/工具是否真有用的标尺

### 11. HarnessEvolve: Learning from Reference Trajectories for Reliable Agent Self-Evolution

- **ID:** [2609.00829v1](https://arxiv.org/abs/2609.00829v1) | [📄 PDF](https://arxiv.org/pdf/2609.00829v1)
- **作者:** Wen Jiang, Mingmin Chu, Yimeng Tian, Qianxin Zhang, Haofei Yang, Rui Yang, Yang Liu, Tao Lv, Fangming Li
- **分类:** cs.AI, cs.LG
- **摘要:** 自进化 agent 通过环境反馈优化 harness（提示/技能/工具/执行逻辑）走向自主，但受三大挑战制约：**credit assignment failure**（终态成败反馈难定位是哪一步出错）、**shortcut learning**（记住任务特定模式而非获得通用能力）、**catastrophic forgetting**（无守卫更新退化已获能力）。HarnessEvolve 从参考轨迹学习实现可靠自进化：把执行 agent 与进化管线解耦，执行、评估、优化、门控分给独立模块。
- **关联度:** ★★★★ 自进化的三坑与解耦方案——k 的 skill-evolution 可对照"参考轨迹学习 + 解耦门控"，避免 shortcut 记忆与能力遗忘

### 12. ASPIRE: Can Models Self-Evolve from Vague Goals?

- **ID:** [2608.31111v1](https://arxiv.org/abs/2608.31111v1) | [📄 PDF](https://arxiv.org/pdf/2608.31111v1)
- **作者:** Yuhao Wu, Jingyuan Zhang, Jiajun Shi, Yuxuan Zhang, Xinping Lei, Junting Zhou, Zexuan Wang, Yuchen Wu, Huan Zhou 等（12 人）
- **分类:** cs.CL
- **摘要:** 人类许多重要学习始于模糊目标（"成为更好的物理学家""把研究做好"）——学习者须自己解释目标、识别能力缺口、决定怎么学、判断是否真进步。而现有 LLM 自进化研究常由人类指定任务与评估指标，把自进化退化为优化显式目标。ASPIRE 基准只提供自然语言能力目标、隐藏下游评估任务：agent 必须自己操作化目标——选择数据与更新方法、构建训练与验证信号、决定何时评估；同时支持模型权重更新与上下文更新两种路径。
- **关联度:** ★★★★ "模糊目标自进化"——给 k 的自我提升/学习流程"自己定义学什么、怎么验证进步"的范式，摆脱纯指标驱动

---

## 三、多智能体与协作（4 篇）

### 13. EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems

- **ID:** [2609.01360v1](https://arxiv.org/abs/2609.01360v1) | [📄 PDF](https://arxiv.org/pdf/2609.01360v1)
- **作者:** Jun Hou, Priya Pitre, Yi Fang, Xuan Wang
- **分类:** cs.AI
- **摘要:** agent 失败常含多个相关错误而非单一错误；现有归因方法通常锁定责任 agent、步骤或根因，不显式建模错误间的依赖关系。EDGE 从观测错误事件构建**错误依赖图**，用反事实 rollout 验证可靠因果子集；推理图引导两阶段 LLM-as-judge 检测器做错误归因，干预验证后的子图提供更可靠的解释与修复分析依据。TRAIL/MAST 上类别级多错误归因在多数模型与设置下提升。
- **关联度:** ★★★★ "错误依赖图 + 反事实验证"——k 的多 agent 协作（WorkBuddy/dsh/Gemini/Codex）调试可借鉴"不只找单个根因，还要建模错误间关系再修"

### 14. Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs

- **ID:** [2609.00621v1](https://arxiv.org/abs/2609.00621v1) | [📄 PDF](https://arxiv.org/pdf/2609.00621v1)
- **作者:** Wentao Zhang, Syed Shariyar Murtaza, Junaid Ahmad Bhatti, Utkarsh Soni, Yifan Nie, Eugene Wen, Yuntian Deng
- **分类:** cs.AI, cs.CL
- **摘要:** prompt 优化能改进多 agent LLM 系统，但被优化的 prompt 常同时承担两个纠缠角色：生成任务相关内容 + 指定执行关键协议（消息路由、输出格式、终止信号），而底层代码依赖后者。于是"为改进内容生成的 prompt 编辑"可能意外破坏协议、整个管线失败。关键观察：两种角色表示不同——执行协议通常是结构化的，任务内容是无结构语言。据此提出 **control-data flow separation**：执行关键控制表示为类型化、经校验的程序对象，任务相关语言保留为可优化的数据。
- **关联度:** ★★★★ 直击 k 的 prompt/多 agent 系统——"控制流与数据流分离"防止 prompt 优化/改写破坏协议，k 调优 agent prompt 时应把路由/格式/终止信号抽成程序对象

### 15. SoK: When Safe Agents Fail Together: The Security of Multi Agent LLM Systems

- **ID:** [2609.00595v1](https://arxiv.org/abs/2609.00595v1) | [📄 PDF](https://arxiv.org/pdf/2609.00595v1)
- **作者:** Rui Yang, Junjie Xu, Zhengyu Liu, Neil Fendley, Yang Hong, Ziyang Li, Yinzhi Cao
- **分类:** cs.AI
- **摘要:** 安全 agent 会一起失败。多 agent 系统跨主体边界传递信息/状态/决策/权威，制造局部检查发现不了的失败；没有执行级视图，多 agent 场景很容易被误当作多 agent 安全效应的证据。对 197 篇工作的执行中心分析：6 个交互接口、4 个对抗位置、7 个系统级风险、8 条重复攻击路径。提出 A-I-R 框架按对抗位置/交互接口/系统级风险组织攻击；防御用五部分契约（路径目标、观测、干预、信任边界、恢复），并指出**路径闭合与恢复**是关键缺口。
- **关联度:** ★★★★★ MAS 安全系统化——k 的多 agent 协作（WorkBuddy/dsh/Gemini/Codex 联合工作）的检查清单：跨 agent 交接必须先定义信任边界与恢复路径

### 16. SwarmBench: Can Large Language Models Act as Agent Swarm Orchestrators?

- **ID:** [2608.30661v1](https://arxiv.org/abs/2608.30661v1) | [📄 PDF](https://arxiv.org/pdf/2608.30661v1)
- **作者:** Jinshan Gao, Zhuoran Jin, Tianyi Men, Kang Liu, Jun Zhao
- **分类:** cs.CL
- **摘要:** 基于 LLM 的多 agent 系统正从固定交互拓扑走向动态编排的 Agent Swarms，但现有基准仍是单 agent/通用 agent 任务，难以系统评估关键编排能力。SwarmBench 从准确率、效率、成本、**过程质量**多维评估编排能力。实验显示当前模型编排能力差异巨大，不仅体现在终局准确率/效率/成本，也体现在编排过程本身的质量；据此提出 SwarmExp——基于经验提取的简单有效方法。
- **关联度:** ★★★★ "动态 swarm 编排的过程质量评估"——k 评估多 agent 编排时"过程质量也是硬指标"，不能只看终局结果

---

## 四、Agent 评估与基准（5 篇）

### 17. GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space

- **ID:** [2608.30188v1](https://arxiv.org/abs/2608.30188v1) | [📄 PDF](https://arxiv.org/pdf/2608.30188v1)
- **作者:** Boqi Chen, Xudong Liu, Yunke Ao, Heejin Do, Jianing Qiu
- **分类:** cs.CL
- **摘要:** LLM 作为临床 agent 潜力巨大，但现有基准把临床工作流退化成静态预测或粗动作集的非约束 MDP。GPAgentBench-2K 是首个**约束 MDP (CMDP) 初级诊疗决策基准**，来自专家验证的真实全科门诊记录：环境建模六种基础临床动作的全谱、对动作空间施加拓扑工作流先验、把"安全知情的弃权"作为一等结果。16 个 SOTA LLM 评估显示动作空间扩大时性能显著退化；并揭露**临床质量-安全缺口**：诊断准确率最高的前沿模型也在一半以上案例违反安全约束。
- **关联度:** ★★★★ "约束动作空间 + 安全弃权一等公民"——k 的 agent 评估/验收可借鉴"动作空间拓扑先验 + 安全约束与质量分开测"，前沿模型也会高分高风险

### 18. Calibration is the Bottleneck: An Action-Class Diagnostic of Multi-Turn Tool-Calling

- **ID:** [2609.00949v1](https://arxiv.org/abs/2609.00949v1) | [📄 PDF](https://arxiv.org/pdf/2609.00949v1)
- **作者:** Kangjia Zhao, Jiajun Li, Haozhen Shen, Wei Chow, Linfeng Li, Hang Song, Lingdong Kong, Chen Zhi, Tiancheng Zhao 等（11 人）
- **分类:** cs.AI, cs.CL
- **摘要:** 开放权重模型在公共工具调用基准的聚合准确率上已逼近甚至超过闭源前沿，但该指标平均了多种多轮情境，掩盖"进步是否均衡"。提出动作类导向诊断框架：把多轮失败分解为两个正交模式——**动作类误校准**与动作执行失败。四类动作空间（TOOL_CALL/ASK/REFUSE/CONFIRM）+ 自揭示上界 **Acc ≤ GAR (Gold Action Recall)**：界违（Acc>GAR）暴露状态评分器掩盖误校准，大界隙（GAR≫Acc）把执行失败定位在 TOOL_CALL 内部。
- **关联度:** ★★★★ "诊断工具调用的两类失败"——k 的 web/tool agent 评估可借鉴"动作类级分解 + 自揭示上界"，别被聚合准确率骗过

### 19. E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation

- **ID:** [2608.30730v1](https://arxiv.org/abs/2608.30730v1) | [📄 PDF](https://arxiv.org/pdf/2608.30730v1)
- **作者:** Wei Fan, Xinjie Shen, Xudong Guo, Jianhong Tu, Yang Su, Yinger Zhang, Lianghao Deng, Fengyu Wang, Baohua Dong 等（11 人）
- **分类:** cs.CL, cs.LG
- **摘要:** 长程 agent 任务超出"把短任务链接更多轮"：动态演化环境 + 长程依赖要求 LLM 在数千步内持续探索、从经验学习、适应策略。E-Commerce Bench 是首个把**多轮对手谈判 + 动态事件**整合进一年期经营的开源基准：365 天里 agent 并发运营多家线上店铺，调研市场、与供应商谈判采购、优化销售策略、履约、处理退货、管理现金流，最大化年末总资产。产品与供应商数据来自真实电商平台，构建商户侧运营环境。
- **关联度:** ★★★★ "365 天经营 = 真实长程适应"——与 k 的闲鱼/店铺运营类比："持续探索、从经验学习、适应策略"正是经营真谛，长程 agent 基准可作经营沙盘参考

### 20. TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution

- **ID:** [2609.01428v1](https://arxiv.org/abs/2609.01428v1) | [📄 PDF](https://arxiv.org/pdf/2609.01428v1)
- **作者:** Ruocan Wei
- **分类:** cs.LG
- **摘要:** ReAct 范式每个 query 从头跑完整推理循环，相似 query 重复相同步骤、不利用历史经验。TRIAGE 是三级路由框架，核心创新 TaaS（Trajectory-as-a-Skill）把历史执行轨迹抽象为可复用技能，实现"experience as a service"：(1) 直接复用——相同 query 0 token；(2) 技能替换——相似 query 确定性参数替换 0 token；(3) 完整 ReAct——新 query 自动存储供未来复用。
- **关联度:** ★★★★ "轨迹即技能 + 三级路由"——k 的重复任务/自动化直接可借鉴"历史轨迹沉淀为技能 + 三级路由省钱"，与 TaaS 的"经验即服务"同构

### 21. You Shouldn't Have Asked: A Pragmatics-Inspired Taxonomy for Evaluating LLM Refusals

- **ID:** [2608.30856v1](https://arxiv.org/abs/2608.30856v1) | [📄 PDF](https://arxiv.org/pdf/2608.30856v1)
- **作者:** Ruoxuan Li, Pinqiao Wang, Sheng Li, Cameron Robert Jones
- **分类:** cs.CL
- **摘要:** 拒绝在语用学中是威胁面子的行为，LLM 被训练拒绝不安全/不恰当请求，但拒绝不当会伤害用户。现有研究把 LLM 不配合当作安全对齐结果，缺少"在不同有害语境下拒绝是否得体"的评估方式。本文提出（据作者所知）首个基于语用理论的 LLM 拒绝分类法；应用于 16 个现代 LLM × 14 类危害：模型拒绝方式各异，但整体明确且强烈道德评价，交互修复发生...
- **关联度:** ★★★ "拒绝得体性评估"——k 评估 agent 合规行为时的"得体拒绝"视角：拒绝不仅要有，还要管理互动代价

---

## 五、安全与对齐（4 篇）

### 22. Distributed Implicit Harm: Compositional Safety Blind Spot in MLLM-Based Video Moderation

- **ID:** [2609.00206v1](https://arxiv.org/abs/2609.00206v1) | [📄 PDF](https://arxiv.org/pdf/2609.00206v1)
- **作者:** Ruotong Wang, Zihao Zhu, Siwei Lyu, Xin Tao, Baoyuan Wu
- **分类:** cs.AI, cs.CV
- **摘要:** 视频审核 MLLM 存在组合安全盲点：**由看似良性组件组成的视频、整体可传达有害含义**——Distributed Implicit Harm (DIH)，危害源于沿视频分解轴分布的组件间关系，而非任何单一显式线索。研究两个代表：跨视觉段的时间分布危害 (DIH-T) 与音视频流之间的跨模态危害 (DIH-M)。这类视频缺组合危害标注、避过基于局部视觉线索/关键词/单模态信号的检索，因此现有安全数据集里不存在。
- **关联度:** ★★★★ "组合安全盲点"——k 的安全评估/内容审核需警惕"单组件无害、组合有害"，单点检查不够

### 23. Uncovering and Mitigating Aggregation-Induced Reward Hacking in Multi-Reward Reinforcement Learning

- **ID:** [2609.00213v1](https://arxiv.org/abs/2609.00213v1) | [📄 PDF](https://arxiv.org/pdf/2609.00213v1)
- **作者:** Yu Yuan, Yaoyou Fan, Lili Zhao, Guangting Zheng, Kai Zhang, Lu Pan, Ke Zeng, Qi Liu
- **分类:** cs.CL
- **摘要:** LLM 的 RL 微调越来越多采用多奖励维度（可验证规则、任务特定评估器、学习奖励模型）提供跨能力的更丰富监督，通常用固定聚合权重标量化。识别出失败模式：**聚合本身诱导 reward hacking**——静态投影把性质不同的奖励画像别名成单一标量，把优化推向最易、最密或被信号系统偏向的维度；训练中把策略困在次优画像，阻止收敛到能带来更高任务性能的更平衡画像。提出 AMRP（Adaptive Multi-Reward Projection）：轻量在线方法，用当前策略的奖励结构重分配聚合权重。
- **关联度:** ★★★★★ 直击 k 的多目标优化——"聚合方式本身就是 hacking 源"，对多奖励/多目标设计有普适警示：固定加权会偏袒易得奖励维度

### 24. VerTox: Verifiable Reward-Guided Corpus Poisoning Against Neural Ranking Models

- **ID:** [2609.01325v1](https://arxiv.org/abs/2609.01325v1) | [📄 PDF](https://arxiv.org/pdf/2609.01325v1)
- **作者:** Zhiqi Huang, Vivek Datla, Zhichao Xu, Puxuan Yu, Vivek Srikumar, Alfy Samuel
- **分类:** cs.CL
- **摘要:** 神经排序模型是现代信息检索系统与 RAG 等 AI 系统的核心组件，但对 LLM 大规模生成流畅欺骗内容的鲁棒性理解不足。VerTox 是首个把语料投毒形式化为**可验证奖励引导的 RL (RLVR)** 的框架：通过专用奖励塑形把"排序扭曲"与"事实腐坏"显式耦合，微调紧凑 LLM 为对抗生成器。实验显示注入少量恶意构造文档即可扭曲排序行为。
- **关联度:** ★★★★ "RLVR 用于攻击生成"——安全评估的对抗侧，k 的 RAG/检索管线加固可参考"攻击可被形式化为可验证奖励优化"

### 25. When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning

- **ID:** [2609.01455v1](https://arxiv.org/abs/2609.01455v1) | [📄 PDF](https://arxiv.org/pdf/2609.01455v1)
- **作者:** Yitong Guo, Xiaoyi Chen, Siyuan Zhang, Xiaofeng Wang, Haixu Tang
- **分类:** cs.AI
- **摘要:** 良性微调严重削弱 LLM 安全对齐。先前研究常归因梯度冲突，本文提出不同的 **Fisher 几何解释**：安全 Fisher 是低秩的，对齐使安全几何更平坦、同时保留一条输出路由通路；约 100 个良性微调样本后，这条通路在输出侧 MLP 模块被选择性重新锐化——解释不对称脆弱性：安全可崩到高攻击成功率，而生成质量保持。
- **关联度:** ★★★★ "安全脆弱性的几何解释"——k 微调/对齐模型时理解"为何安全先崩而生成不崩"，低秩安全方向 + 输出路由重锐化是关键机制

---

## 六、推理与 RL 训练（6 篇）

### 26. Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents

- **ID:** [2609.01245v1](https://arxiv.org/abs/2609.01245v1) | [📄 PDF](https://arxiv.org/pdf/2609.01245v1)
- **作者:** Liming Pu, Xiaoxia Li, Yifu Liu, Teng Cao, Bin Yang
- **分类:** cs.AI, cs.LG
- **摘要:** 对只由端到端任务验证打分的长期交互任务，RL 是自然的后训练方式，但共识认为 outcome-only RL 在小型开放模型上很快触顶，于是人们用更密奖励、SFT 先验、技能库、策展记忆、多 agent 编排来补偿。作者论证触顶是**两种常见实践失败**的人工产物：①信号饥饿——组相对 RL + 稀疏 outcome-only 奖励只在任务的 rollout 组混入成功与失败时才产生梯度，欠扩展的探索恰好压制最难、最有教益的任务；②策略漂移——在小任务池上挤大量更新使策略本身退化，无锚目标让采样分布在饱和、组内信息已枯竭时坍缩。修复这两点（扩展探索 + 锚定参考分布），outcome-only RL 在长程交互上可以充分——不需额外奖励工程。
- **关联度:** ★★★★★ 直击 k 的 RL/训练认知——"触顶是实践失败而非能力上限"，扩展探索 + 防漂移比堆奖励工程更根本

### 27. Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence

- **ID:** [2608.31075v2](https://arxiv.org/abs/2608.31075v2) | [📄 PDF](https://arxiv.org/pdf/2608.31075v2)
- **作者:** Zhiqin Yang, Jingwen Fu, Yuhan Liu, Hengyu Liu, Yonggang Zhang, Kainan Cao, Zizhuo Zhang, Chenxin Li, Ruibin Yuan 等（14 人）
- **分类:** cs.AI
- **摘要:** RLVR 在数学与代码（结果可自动检查）上显著提升大推理模型（LRM），但扩展到开放与 agentic 任务很难：可靠奖励更难获得，直接人类监督跟不上模型生成经验的规模与复杂度。本文研究 LRM 在人类监督逐渐退出学习回路后如何继续提升，沿两个维度展开：**奖励轴**——从逐实例人类判断演进到可复用验证器、乃至无需人类反馈的奖励；**经验轴**——从人工策展任务与环境走向自生成课程。
- **关联度:** ★★★★★ "奖励与经验两轴的监督退化"——k 的自动化自我评估/验证器设计直接相关：验证器可复用化、课程自生成化是走向免人类监督的两条主线

### 28. GMTS: Gradient Magnitude-based Token Selection Improves RLVR Training for LLM Reasoning

- **ID:** [2608.30632v1](https://arxiv.org/abs/2608.30632v1) | [📄 PDF](https://arxiv.org/pdf/2608.30632v1)
- **作者:** Outongyi Lv, Yuanwei Zhang, Xiaoqun Zhang
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** RLVR 已成提升 LLM 推理能力的中心范式。近期研究发现高熵 token 对训练异常重要（只用最高 20% 熵 token 即有显著增益），但"为何高熵有益"理解不足。本文发现：答案内高熵 token 倾向与大幅值梯度相关，但**熵本身跨答案不能一致反映 token 重要性**（要考虑答案级奖励信号的差异）。据此提出基于**梯度幅值**的 token 选择 (GMTS)——用更直接的训练信号判据替代熵。
- **关联度:** ★★★★ "按梯度幅值选 token"——比熵更直接的 RLVR token 选择依据，对 k 的 RLVR 微调/推理训练可参考

### 29. One Policy, Any Budget: Internalizing Budget-Aware Search via Reinforcement Learning

- **ID:** [2609.00813v1](https://arxiv.org/abs/2609.00813v1) | [📄 PDF](https://arxiv.org/pdf/2609.00813v1)
- **作者:** Xiaowei Sun, Jin Li, Yili Hong, Yikun Fu, Yanghua Xiao
- **分类:** cs.AI
- **摘要:** RL 已让 LLM 搜索 agent 能调用外部工具，但现有方法在固定预算下训练，部署时预算变化就无法适应。AnySearch 让**单一策略在任意预算约束下做预算感知搜索**：阶段一用显式预算状态注入 + 结构化推理 prompt 引导在线性衰减预算下的高效分配；阶段二移除脚手架，agent 在自适应采样的预算约束下自主运行、匹配推理条件。两阶段用复合奖励把答案准确率与预算效率（绝对 + 相对）耦合优化。
- **关联度:** ★★★★ "单策略适配任意预算"——k 的模型路由/成本控制可借鉴"把预算约束内化进策略"，而非部署时临时降级

### 30. Where the Verifier Fails: A Category-Level Audit of Reward Signals in RLVR

- **ID:** [2609.01354v1](https://arxiv.org/abs/2609.01354v1) | [📄 PDF](https://arxiv.org/pdf/2609.01354v1)
- **作者:** Esther Xin
- **分类:** cs.CL, cs.LG
- **摘要:** RLVR 与标准基准评估都依赖自动验证器把自由文本答案变成二元奖励。既有报告指出某评估 harness 只接受约 94% 自己的标准答案（归因 LaTeX 解析），但那是聚合值。本文对验证器而非模型做变形测试：生成构造上保义的等价答案变体（按构造保留数学含义的改写，任何拒绝都是可证明的假阴性、无需人工裁决），在 307,420 条判定、四个广泛使用验证器上按答案类别测拒绝率。发现：自验证范围从 53.8% 到 95... 不等，三类关键发现。
- **关联度:** ★★★★ "验证器本身是评估误差来源"——k 用 LLM judge/自动验证器验收时先审计"验证器自身偏见"，别把验证器误差当模型误差

### 31. Context-Grounding Gains Are Mediated by Pre-existing Machinery: Auditing GRPO, SFT, and DPO

- **ID:** [2609.00925v1](https://arxiv.org/abs/2609.00925v1) | [📄 PDF](https://arxiv.org/pdf/2609.00925v1)
- **作者:** Prakhar Gupta, Vaibhav Gupta
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** 模型会忽略与记忆知识冲突的 prompt 证据；后训练能让模型更可靠地跟随证据，但不清楚这些增益是否需要新机制、还是强化既有机制。从同一初始 checkpoint 对比 9 个后训练臂（GRPO/SFT/DPO），训练前估计接地方向：五个 GRPO 变体的接地增益都很小；两个跨 seed 复制的变体，其效应被等价检验界定在 conflict-SFT 增益之下（即便奖励指标在提升）；conflict-SFT 适度提升接地，DPO 在匹配分布上把接地推到接近上限；conflict-SFT 与 DPO 基本走同一因果机制。
- **关联度:** ★★★★ "接地增益靠既有机制"——k 评估后训练/微调方案时需区分"真新机制 vs 强化既有机制"，奖励指标涨不代表接地真的涨

---

## 七、编码 Agent 与工具使用（4 篇）

### 32. Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement

- **ID:** [2609.01481v1](https://arxiv.org/abs/2609.01481v1) | [📄 PDF](https://arxiv.org/pdf/2609.01481v1)
- **作者:** Haoyang Yan, Min-le Su, Hangfan Zhang, Zhanhao Li, Chen Zhang, Shao Zhang, Yang Chen, Lei Bai, Shuyue Hu
- **分类:** cs.AI
- **摘要:** 研究编码 agent 在无人类干预下把高层需求转成完整、可用软件系统的自主开发。Harness-of-Harness (HoH) 让编码 agent 在自主开发中**持续改进**：在现有编码 agent harness 之上运行，把执行组织成迭代规划-编码-测试循环。为跨循环维持改进，HoH 平衡修复与能力增长、把开发范围切小到可验证增量、把实现期测试与独立评估分离、约束可验证输出而非规定 agent 工作流；并渐进暴露交付物、角色特定工具与技能，鼓励复用而非重建，维护版本化项目历史。
- **关联度:** ★★★★★ "在 harness 之上持续改进 + 约束可验证输出而非规定流程"——与 k 的编码委派/验收门直接同构：小步可验证增量 + 独立评估 + 渐进授权

### 33. Compile, Don't Memorize: A Context Compilation Architecture (CCA) for In-Context Learning

- **ID:** [2609.00759v1](https://arxiv.org/abs/2609.00759v1) | [📄 PDF](https://arxiv.org/pdf/2609.00759v1)
- **作者:** Jinhu Qi, Minda Hu, Wentao Zhang, Weiqiang Jin, Yanyu Chen, Junli Wang, Irwin King
- **分类:** cs.CL
- **摘要:** ICL 任务由长而新颖的上下文定义规则/知识/输出模式，按上下文每个细节评分时，强开放权重模型也只过 12-16%——漏一条规则整个响应失败。作者论证脆弱性是结构性的：主流"读-思"范式要求模型在一次前向里提取、规划、生成、自验证。提出 Context Compilation Architecture (CCA)，核心创新是**带固定槽位的类型化中间表示 (IR)**：把长上下文显式编译成结构化中间表示再推理，并比较 gist 检索、多 agent 自博弈等现有长上下文策略，考察 harness 收益跨任务结构与模型规模的保持。
- **关联度:** ★★★★★ "上下文编译成类型化 IR"——k 的长上下文/文档理解可借鉴"先编译结构再推理"，破一次性"读-思"的脆弱性

### 34. Schwarz: Solver-Aware Agentic Program Verification

- **ID:** [2608.30803v1](https://arxiv.org/abs/2608.30803v1) | [📄 PDF](https://arxiv.org/pdf/2608.30803v1)
- **作者:** Jingyu Ke, Ling-I Wu, Guoqiang Li
- **分类:** cs.SE
- **摘要:** agentic 验证系统常能生成看似合理的源级规格，但验证器必须把规格转成 SMT 义务让求解器证明；这一步失败时，现行 LLM 循环只暴露粗糙的验证器错误/超时/未知求解结果，模型分不清是规格错、缺辅助引理、证明上下文含无关事实、还是义务需要不同理论视角。Schwarz 让 SMT 证明失败**局部化、可检查、可修复**：程序点快照暴露边界上已检查的事实、局部引理让 agent 提出缺失证明步、把失败验证转成义务局部修复任务。
- **关联度:** ★★★★ "证明失败局部化可修复"——k 的代码验证/交付质量门可借鉴"把验证失败拆成可定位、可修复的局部任务"，而非只报粗粒度错误

### 35. Framework and Benchmark for Code-Driven Agentic Testing in Web Development

- **ID:** [2609.00081v1](https://arxiv.org/abs/2609.00081v1) | [📄 PDF](https://arxiv.org/pdf/2609.00081v1)
- **作者:** Bin Hong, Zhenchao Zhang, Jiyuan He, Kai Zhang, Zhenya Huang
- **分类:** cs.SE
- **摘要:** 端到端 GUI 测试对验证 web 应用必不可少，但现有评估依赖预定义检查清单、局限在 web 生成基准的数据与框架内，VLM 的 bug 发现能力未被系统测试。提出 **Code-driven Agentic Testing (CAT)**：agent 写 Playwright 代码驱动浏览器、收集反馈、自主探索 web 应用找 bug。CATJudge 在单一环境统一 Browser-Use 与 Computer-Use 工具；CATTest 是 102 个 AI 生成 web 应用、带人工标注 bug（复杂交互 + 细微缺陷）的基准，经紧密人-AI 协作构建。
- **关联度:** ★★★★ "代码驱动 agentic 测试"——k 的 web 测试/验收可借鉴"agent 写代码驱动浏览器自主找 bug"，比预定义检查清单更能发现真缺陷

---

## 八、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2608.31100](https://arxiv.org/abs/2608.31100v1) | S3Gym | 自测/自判/自改进三能力耦合交互基准：宽松探索 + 严格留出评估，七个文本游戏验证 agent 能否把交互经验转成行为改进 |
| 2 | [2609.00232](https://arxiv.org/abs/2609.00232v1) | VeriOCRBench | OCR 推理先做任务验证：判 Image/Text/Question 是否构成可执行任务，1,800 样本人验，8 个 OCR 域 |
| 3 | [2608.30724](https://arxiv.org/abs/2608.30724v1) | BAITBENCH | 三个含"可选捷径"的表格 ML 任务：agent 可夸大公开测试分但隐藏集失败——量化 agent reward hacking |
| 4 | [2609.00624](https://arxiv.org/abs/2609.00624v1) | TUSA | 弱监督器普遍高熵、稠密干预频繁低置信打扰——按不确定性稀疏对齐，只在确定时干预，降低效用损失 |
| 5 | [2609.01056](https://arxiv.org/abs/2609.01056v1) | WorldBench | 1,600 任务 × 7 语言 × 8 文化的人格接地日常工作流基准，沙箱结构化动作，测状态保持与跨语言 |
| 6 | [2609.01161](https://arxiv.org/abs/2609.01161v1) | CopyShield | 对比解码(输出)/DPO(行为)/激活干预(表示)三层版权防御统一协议，LLaMA-3.1-8B/Mistral-7B 受控记忆 |
| 7 | [2608.30748](https://arxiv.org/abs/2608.30748v1) | Fragility of Jailbreak Robustness | 固定攻击只改普通系统提示即可大幅改变 ASR——7 个对齐模型 × 3 类运行状态，越狱鲁棒性对运行状态高度脆弱 |
| 8 | [2608.30686](https://arxiv.org/abs/2608.30686v1) | CIPR | 用户侧 Prompt-Level Configurations（委派任务/措辞/技能规则）塑造编码 agent 对仓库投毒的脆弱性，首个系统变化基准 |
| 9 | [2608.30303](https://arxiv.org/abs/2608.30303v2) | Lazy Grounding | 检索 agent 会被**完全事实但分心**的证据诱导（懒接地）——注入答案改写附近的邻近证据即可操控响应 |
| 10 | [2609.00865](https://arxiv.org/abs/2609.00865v1) | MemoryWalker | 压缩训练下学习对象是"树"非"序列"：LogitTree 分段 K-forward + 打包 4D 注意力掩码，梯度等价修正泄漏/失配 |
| 11 | [2608.30785](https://arxiv.org/abs/2608.30785v1) | SkillZip Pro | 生产技能是目录包（根/引用/模式/脚本/子技能渐进加载）：跨文件压缩 + 保路由，免评估压缩器不破坏渐进加载边界 |
| 12 | [2609.00296](https://arxiv.org/abs/2609.00296v1) | Workflow-Aware Healthcare | 医疗 NLP agent 的 episode 级评估协议：五字段 episode 模式 + 状态连续性/证据可溯源/升级决策评分 |
| 13 | [2609.00470](https://arxiv.org/abs/2609.00470v1) | TRIS | RAG 检索完整性三层筛：跨 embedding 聚类 + 独立 judge + LLM 一致性验证，抗 PoisonedRAG 式语料投毒 |
| 14 | [2608.30877](https://arxiv.org/abs/2608.30877v1) | DeepSeek 175B on RTX 4060 | 消费级 32GB 笔记本 + 8GB VRAM 本地部署 175B 完成 20 万级蛋白配体虚拟筛选（k 同款 4060，本地大模型可行参考） |
| 15 | [2609.00570](https://arxiv.org/abs/2609.00570v1) | VoiceLongMemEval | 记忆基准忽略"怎么说的"：答案依赖副语言元数据（情绪标签/韵律描述）——多会话助手记忆新维度 |
| 16 | [2609.00833](https://arxiv.org/abs/2609.00833v1) | Dense Process Supervision | 搜索 agent 事实效用估计的稠密过程监督：抽取结构事实→显式事实库→语义聚类做信用分配 |
| 17 | [2609.00714](https://arxiv.org/abs/2609.00714v1) | ChatDev 2.0 | 无代码多 agent 平台：声明式可执行图 + 循环感知执行引擎 + 可视化 IDE，异构 agent 与动态循环单框架表达 |

---

## 今日要点（主题信号）

1. **Agent 记忆从"存什么"转向"忘什么 / 用得上什么"**：UTILMEM 立起"记忆利用 ≠ 事实回忆"（整合分布式隐含证据成任务输出）；Gated-Memory Routing 学执行记忆只留非冗余步；Invalidation Contracts 给缓存加版本戳防漂移；PIS 用类型化意图存储让 SLM 做前瞻记忆（DeepSeek-Chat 82.9% Set-F1）。与 k 的记忆清理/证据分级 A-D 直接同频——"会忘、会用得上"比"存得多"更值钱。
2. **自进化技能的"信任边界"成为新安全主线**：EvoSkill Injection 红队自进化技能管线（恶意能力被生成存储为合法技能）；ARISE-RL / AgentFactory / HarnessEvolve / ASPIRE 齐发力"可靠自进化"；Skill Following 揭穿"聚合检索增益"假象（RAE 才能测真用上）。k 的 skill 体系 / skill-evolution / skill-vetter 正好对接——技能安全校验必须前置。
3. **评估转向"动作类诊断 + 过程可审计 + 验证器自身审计"**：Calibration is the Bottleneck（Acc≤GAR 自揭示上界拆两类失败）、GPAgentBench-2K（约束动作空间 + 安全弃权一等公民）、E-Commerce Bench（365 天长程经营）、Where the Verifier Fails（验证器自验证差异 53.8%-95%）——聚合准确率正在失去可信度。
4. **RLVR 的成本与边界被精确刻画**：Explore More Drift Less（触顶是"信号饥饿 + 策略漂移"双失败而非能力上限）、GMTS（梯度幅值比熵更准选 token）、Aggregation-Induced Reward Hacking（固定加权聚合本身诱导 hacking，需自适应投影）、Auditing GRPO/SFT/DPO（接地增益靠既有机制）——RL 训练方法论进入"审计期"。
5. **多智能体安全系统化 + 编码 agent 持续改进**：SoK MAS 安全（197 篇 / A-I-R 框架 / 五部防御契约）、Control-Data Flow Separation（控制流与数据流分离防协议破坏）、Harness-of-Harness（harness 之上持续改进，小时级→天级自主开发）、CCA（上下文编译成类型化 IR 破"读-思"一次性缺陷）——harness 与 meta-harness 成为差异化主战场。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Harness-of-Harness 2609.01481 | web_search（SUFE 学术讲座"Agent Harness" + meta-harness 生态文章） | ✅ 确认：SUFE 讲座明确把"Harness of Harness"框定为把自主软件开发从小时级扩展到天级并持续改进，与 2026 meta-harness 产业讨论共振 |
| 其余 34 篇 | arXiv API 收录 + 抽取完整元数据 | ✅ API 收录即存在性证据（2026-08-07 既定原则） |

## 可落地行动项

- 🔴 **自进化技能安全前置校验**：EvoSkill Injection 证明技能生成/复用管线是新攻击面——对照 k 的 skill 体系：外部技能安装必须过 skill-vetter（触发/依赖/安全校验），把"恶意技能混入自进化管线"写进检查清单
- 🟡 **技能价值的真标尺 RAE**：Skill Following 的 RAE（匹配任务上技能启用 vs 禁用的同任务差）揭穿聚合检索增益假象——k 评估自身 skill/工具是否真有用时改用"同任务对照"，而非聚合指标
- 🟡 **记忆利用维度入库**：UTILMEM 定义"整合分布式隐含证据成任务输出"、Invalidation Contracts 的版本戳防漂移——纳入 k 的知识库/记忆评估维度与缓存失效设计
- 🟡 **验证器自身审计**：Where the Verifier Fails 证明 RLVR 验证器自验证差异巨大（53.8%-95%）——k 用 LLM judge/自动验证器做验收时，先审计验证器偏见，别把验证器误差当模型误差
- 🟢 **待深读**：Explore More Drift Less、ARISE-RL、EvoSkill Injection、Harness-of-Harness、Compile Don't Memorize (CCA) → 进 core-contributions 候选

---

*本速览由 cron 自动生成：08-31→09-01 两日窗口全量收集（1030 篇）→ 关键词过滤（496 篇）→ 人工精选（35 主条目 + 17 简评）→ 关键论文交叉验证。数据源 export.arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
