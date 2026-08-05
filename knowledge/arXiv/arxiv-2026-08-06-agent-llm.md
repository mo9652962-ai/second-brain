---
aliases:
  - arxiv-2026-08-06-agent-llm
  - arxiv-agent-llm-2026-08-06
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-06
updated: 2026-08-06
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-06

> **检索时间**: 2026-08-06 07:13 GMT+8
> **检索范围**: cs.AI / cs.CL / cs.LG / cs.MA / cs.SE / cs.RO / cs.HC / cs.CV / cs.CR / cs.DB,提交日期 08-04 ~ 08-06
> **原始检索**: 7 组查询(Agent 框架/LLM Agent/多 Agent/工具调用/代码 Agent/Agent 记忆/Agent 安全),去重后 **29 篇**,精选 **14 篇**与 AI Agent / LLM 强相关
> **数据源**: [export.arxiv.org](https://export.arxiv.org) + [Semantic Scholar](https://www.semanticscholar.org)

---

## 一、Agent 自我改进与训练

### 1. PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents
- **ID:** [2608.04003v1](https://arxiv.org/abs/2608.04003v1) | [📄 PDF](https://arxiv.org/pdf/2608.04003v1)
- **作者:** Shuhan Xue, Zixin Ding, Yichen Shen, Yinjie Wang, Zhenfei Yin, Yingcheng Wu, Yuxin Chen, Mengdi Wang, Ling Yang
- **分类:** cs.CL
- **摘要:** 递归自我改进要求 Agent 把积累的经验转化为更好的未来行为,但"保留的经验是否真的随时间提升表现"从未被系统测试。PAST-Bench 在**匹配条件下开关保留经验**,隔离这一能力:26 个场景、204 个回合,覆盖记忆、程序复用、信息收集与更新四个维度;既报告后续任务的增益,也检查增益是否走 save→retrieve→update 预期路径。
- **关联度:** ★★★★★ 直接对应 Hermes/Obsidian 记忆体系 —— "保留经验是否真的提升表现"正是 Second Brain 的核心假设,PAST-Bench 可作记忆系统评估框架

### 2. TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning
- **ID:** [2608.04007v1](https://arxiv.org/abs/2608.04007v1) | [📄 PDF](https://arxiv.org/pdf/2608.04007v1)
- **作者:** Changle Qu, Sunhao Dai, Hengyi Cai, Yuqi Zhou, Xinran Chen, Simon, Jun Xu
- **分类:** cs.CL, cs.AI
- **摘要:** 工具集成推理(TIR)中,现有 RL 方法依赖轨迹级监督,长程任务里信用分配粗糙;token 级监督又抓不住工具交互的回合结构。TurnSight 提出**回合级事后自蒸馏**:监督直接来自执行条件化的事后视角,教师分支用特权上下文提供更密集的信号,解决长程 TIR 的细粒度信用分配。
- **关联度:** ★★★★ Agent 工具调用训练新方法,对编码/搜索 Agent 的长链任务有参考价值

### 3. ReflectRL: Learning from Golden Negative Trajectories via Reflective-to-Direct Reasoning
- **ID:** [2608.03972v1](https://arxiv.org/abs/2608.03972v1) | [📄 PDF](https://arxiv.org/pdf/2608.03972v1)
- **作者:** Jinhe Bi, Chennan Zhou, Zengjie Jin, Aniri, Shuo Lu, Wenke Huang, Hu Cao, Xun Xiao, Zhihong Zhu, Volker Tresp, Fei Shen, Yunpu Ma, Tat-Seng Chua
- **分类:** cs.AI
- **摘要:** 专家模型在难题上失败时,现有轨迹引导训练失去监督来源,失败轨迹通常被丢弃。作者主张这些**"黄金负轨迹"**(Golden Negative Trajectories)是有价值的推理信号 —— 不是作为模仿示范,而是作为反思对象。发现"反思优势":难题上反思一条有缺陷的轨迹,比从零直接求解更容易、更有效。
- **关联度:** ★★★★ RL 后训练新思路;与 sora 的 ERRORS.md(从错误中学习)理念一致

---

## 二、Deep Research / 多模态 Agent

### 4. Video-DeepResearch: Towards the Next-Generation Multimodal Deepresearch Agent
- **ID:** [2608.03979v1](https://arxiv.org/abs/2608.03979v1) | [📄 PDF](https://arxiv.org/pdf/2608.03979v1)
- **作者:** Zhen Fang, Yu Zeng, Wenxuan Huang, Yiming Zhao, ... Wanli Ouyang, Shaosheng Cao, Feng Zhao
- **分类:** cs.CV, cs.AI
- **摘要:** 把多模态 Agent 从静态图像扩展到连续视频流(需要密集时空定位 + 开放网页探索)。预评估揭示两大瓶颈:**模态偏差**(Agent 绕过视觉工具改用文本搜索)和**参数知识泄漏**(依赖内部记忆而非真正的工具增强执行)。Video-DR 用解耦的感知-探索流水线 + 阶段式工具解锁,强制跨帧视觉定位先于网页检索;两阶段训练:SFT + GRPO。
- **关联度:** ★★★★★ 深度研究 Agent 是多模态演进方向;模态偏差/知识泄漏两个诊断维度可直接用于评估现有 deep-research 工作流

### 5. ETA: A New Agentic Paradigm for Embodied Tasks
- **ID:** [2608.03924v1](https://arxiv.org/abs/2608.03924v1) | [📄 PDF](https://arxiv.org/pdf/2608.03924v1)
- **作者:** Yitong Chen, Zezheng Huai, Sixian Li, Yubang Wang, Haozhe Zhang, Yifei Zhang, Hechang Chen, Jingjing Gong, Yu-Gang Jiang, Xipeng Qiu
- **分类:** cs.RO
- **摘要:** 机器人何时迎来"ChatGPT 时刻"?ETA(Embodied Task Agent)提出把数字 Agent 范式延伸到物理世界的新架构:机器人围绕一个 **Planner 每次选择一个 Tool 调用**,配 Interface 层连接感知与动作,而非端到端 observation-to-action。开源实现 OpenETA。
- **关联度:** ★★★★ 把 LLM Agent 的 tool-calling 架构搬到具身场景;sora 的硬件/机器人兴趣线可跟进

---

## 三、多 Agent 与社会智能

### 6. A Game Theory for Foundation Models: New Paths to Rational Cooperation through Similarity Inference
- **ID:** [2608.03958v1](https://arxiv.org/abs/2608.03958v1) | [📄 PDF](https://arxiv.org/pdf/2608.03958v1)
- **作者:** Alexander Meulemans, Maciej Wołczyk, Marissa A. Weis, ... James Manyika, Blaise Agüera y Arcas (DeepMind 系)
- **分类:** cs.AI
- **摘要:** 经典博弈论建立在"解耦能动性"假设上(Agent 把自己决策与环境/其他行动者独立)。现代基础模型 Agent 会**联合预测自己的未来行动与外部观测**。研究发现:在典型社会困境中,做最优规划的基础模型 Agent 会稳定收敛到**合作**,直接违背经典博弈论的背叛预测 —— 相似性推理为理性合作开辟了新路径,对多 Agent 系统的安全与协作有深远意义。
- **关联度:** ★★★★ 多 Agent 合作理论前沿;DeepMind 大牛阵容,可作多 Agent 编排的理论支撑

### 7. SocietyBench: Forecasting Counterfactual Social-World Evolution
- **ID:** [2608.04009v1](https://arxiv.org/abs/2608.04009v1) | [📄 PDF](https://arxiv.org/pdf/2608.04009v1)
- **作者:** Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
- **分类:** cs.CL
- **摘要:** LLM 及其 Agent 被大量基准测试"能否完成任务"(修 bug、开浏览器、操作 GUI),但**理解并预测真实社会事件如何展开**的能力几乎没被测量。SocietyBench 用一句话事件主题,跨 5 个平台收集新闻与社交媒体,蒸馏成带日期的时间线(事实层与舆论层分离),每个截止日生成审计过的预测问题,按概率校准与时间准确性两个正交维度打分。
- **关联度:** ★★★ Agent 社会智能评估新维度;与 WorldCup Arena 同组作者,前瞻评测方向

---

## 四、Agent / LLM 评估

### 8. WorldCup Arena: Prospective, Leakage-Free Evaluation of Frontier LLMs on a Live Tournament
- **ID:** [2608.04008v1](https://arxiv.org/abs/2608.04008v1) | [📄 PDF](https://arxiv.org/pdf/2608.04008v1)
- **作者:** Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
- **分类:** cs.CL
- **摘要:** 大多数 LLM 预测能力基准都是回顾式的(事件已发生、答案在网上、评测要防记忆)。本工作反其道而行:2026 世界杯 39 天期间,6 个前沿 LLM(带扩展思考 + 原生服务端搜索)在每次开球前填写 104 场比赛的 7 市场预测卡,外加 12 个小组头名与赛前冠军池 —— **提问时答案尚不存在,评测构造上就无泄漏**。冻结存档含 4,494 条已评分预测。
- **关联度:** ★★★★ "前瞻式无泄漏评测"方法论标杆;评测设计思路可迁移到任何时效性任务

### 9. HIVE: Should We Type or Talk to LLM Agents?
- **ID:** [2608.03970v1](https://arxiv.org/abs/2608.03970v1) | [📄 PDF](https://arxiv.org/pdf/2608.03970v1)
- **作者:** Zizhao Hu, Nathan Elijah Segura, Mohammad Rostami, Jesse Thomason
- **分类:** cs.AI
- **摘要:** 人类输入通过打字或说话到达语言模型,每条通道留下独特痕迹:键盘有拼写噪声,语音有转写口吃与 AI 听写工具的重组。HIVE(Human Input-Variation Engine)是语音转写扰动 + QWERTY 键盘扰动套件,测试模型鲁棒性,7 个发现:(i) 语音转写扰动普遍拉低准确率,成本来自**转写结构**而非填充词;(ii) 键盘扰动代价较小,模型能吸收大量拼写错误……
- **关联度:** ★★★ 人机交互鲁棒性;对语音输入 Agent 场景(如语音助手)有工程指导

### 10. Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility
- **ID:** [2608.04001v1](https://arxiv.org/abs/2608.04001v1) | [📄 PDF](https://arxiv.org/pdf/2608.04001v1)
- **作者:** Mohsen Hariri, Weicong Chen, Nahal Shahini, ... Vipin Chaudhary
- **分类:** cs.LG, cs.AI
- **摘要:** 更多推理期算力让 LLM 能解更难的问题,但"测试时缩放"一词现在涵盖三类差异巨大的算法:单轨迹内扩展思考、采样候选后投票/验证聚合、在未完成部分状态上搜索。把它们当作可互换的"预算"或只报准确率不报推理协议,结果难以跨研究比较。本文沿三个轴系统化:预算化推理的形式化、算法分类、可复现报告协议。
- **关联度:** ★★★★ 推理期优化系统性综述;配置模型 reasoning_effort 时理解"预算"语义的基础文献

---

## 五、LLM 应用与工具

### 11. SeGaBench: Can Large Language Models Recover Semantic Optimization Opportunities That Compilers Miss?
- **ID:** [2608.03983v1](https://arxiv.org/abs/2608.03983v1) | [📄 PDF](https://arxiv.org/pdf/2608.03983v1)
- **作者:** Hailong Jiang, Feng Yu, Emran Hossain, Jianfeng Zhu, Mengfei Ren, Qiang Guan, Chunwei Xia
- **分类:** cs.PL, cs.AI
- **摘要:** 编译器会错过"前置语义不在程序表示中"的有利可图的变换。SeGaBench 是一个可执行基准:100 个合成 + 20 个源码用例,覆盖底层假设、数据结构不变量、高层语义提升,每个用例含隐藏使能语义、oracle 工件、正确性与语义验证器。5 个 LLM × 5 次响应,最强模型 94.8% 响应产生正确工件,至少 1.05x 加速。
- **关联度:** ★★★★ 代码 Agent 的"语义级优化"能力测试;LLM 编译器方向的严谨基准

### 12. TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring
- **ID:** [2608.03952v1](https://arxiv.org/abs/2608.03952v1) | [📄 PDF](https://arxiv.org/pdf/2608.03952v1)
- **作者:** Dongjie Yang, Siyan Lin, Leixian Shen, Rui Sheng, Huamin Qu, Zixin Chen
- **分类:** cs.AI
- **摘要:** LLM 越来越常用于 ESL 学习者的对话练习,但有效辅导不止于流利生成:导师须根据学习者行为与对话上下文选择**合适的教学动作**。TACT(Taxonomy-Aligned Conversational Tutor)提出人本框架:两个互补分类法 —— 13 种导师响应策略的 Tutor-Strategy Taxonomy + 学习者状态分类 —— 用于后训练与评估教学自适应的 ESL 导师。
- **关联度:** ★★★★ 与 sora 的英语刷题机项目(english-practice-machine)直接相关:教学策略分类法可借鉴到刷题机的讲解环节设计

### 13. Semantic Bundling: Interactive Node and Edge Bundling to Simplify Knowledge Graphs using LLMs
- **ID:** [2608.04002v1](https://arxiv.org/abs/2608.04002v1) | [📄 PDF](https://arxiv.org/pdf/2608.04002v1)
- **作者:** Adam Coscia, Zeyu Hua, Eric Krokos, Timothy Lin, Alex Endert
- **分类:** cs.HC
- **摘要:** 文档语料表示为知识图谱(KG)后,关系显式化,但图增长后难以解释与可视化("毛球问题")。Semantic Bundling 用 LLM 支持用户驱动的节点/边捆绑:超节点折叠并总结图区域,超边总结连接 —— 把密集源文本中的关系含义提取到更高层结构。
- **关联度:** ★★★ 与 sora 的 graphify(代码知识图谱)可视化理念相通;KG 简化的交互范式

### 14. Calibrating Trustworthiness: Co-Designing Metrics and Visualizations for Evaluating LLMs in Education
- **ID:** [2608.04006v1](https://arxiv.org/abs/2608.04006v1) | [📄 PDF](https://arxiv.org/pdf/2608.04006v1)
- **作者:** Adam Coscia, Sujata Duwal, Langdon Holmes, Scott Crossley, Alex Endert
- **分类:** cs.HC
- **摘要:** LLM 重塑教育技术,但"响应是否符合教学法"的评估依赖学习工程师的经验。本文以**可信度**为结构化评估透镜,与开发 LLM 数字教科书的学习工程师共创:5 个可信度指标 × 20 个度量,把可信度违规映射到 LLM 响应上的可视化,帮助学习工程师做 A/B 比较。
- **关联度:** ★★★ 教育场景 LLM 评估框架;与 TACT 同属教育 Agent 线,可组合参考

---

## 📌 今日要点

- **主题主线**: Agent 评估与自我改进是今日最大热点(PAST-Bench 递归自改进、SocietyBench 社会智能、WorldCup Arena 无泄漏评测、HIVE 输入鲁棒性)
- **训练方法**: 回合级事后蒸馏(TurnSight)、黄金负轨迹反思(ReflectRL)代表工具型 Agent 训练的新探索
- **与 sora 直接相关**: PAST-Bench(记忆体系评估)、Video-DeepResearch(深度研究工作流)、TACT(英语刷题机)、Semantic Bundling(graphify 可视化)
- **理论前沿**: DeepMind 的基础模型博弈论(合作涌现)值得跟踪

---
> 关联: [[arxiv-2026-08-05-core-contributions|08-05 核心贡献]] · [[arxiv-digest|arXiv 周报]] | [[HOME|🏠 首页]]
