---
aliases:
  - arxiv-2026-08-16-agent-llm
  - arxiv-agent-llm-2026-08-16
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-16
updated: 2026-08-16
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-16（补全 08-13 提交池）

> **检索时间**: 2026-08-16 GMT+8
> **检索范围**: cs.AI / cs.CL / cs.LG / cs.MA / cs.CR / cs.CV / cs.SE,提交日期 08-13
> **数据源**: [export.arxiv.org](https://export.arxiv.org)
> **⚠️ 补全性质**: arXiv 索引冻结在 08-13T17:59Z,无 08-14~08-16 新提交。08-14 速览已收录 18 篇,本笔记补录**同一提交池中 08-14 未收录**的强相关论文(收集 53 篇去重 → 精选 15 篇 + 简评 5 篇)。下一份速览若仍无新提交应 [SILENT]。

---

## 一、Agent 自我改进与训练

### 1. SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback
- **ID:** [2608.13120v1](https://arxiv.org/abs/2608.13120v1) | [📄 PDF](https://arxiv.org/pdf/2608.13120v1)
- **作者:** Qianxi Yan, Chunrong Chen, Jiuzhou Zhao, Min Zhang, Yongzhou Xu, Xiaochuan Xu
- **分类:** cs.AI
- **摘要:** Agent Skills 要么手工编写、要么单次 LLM 生成,缺乏从交互失败中改进的闭环;现有闭环从单轮问答取反馈,第一轮修补后**演化梯度衰减**,跨轮缺陷不可见、演化停滞。SkillEvo 提出从**多轮交互反馈**提取自更新演化梯度,并强化治理机制,让技能在真实失败中持续演化而非一次定型。
- **关联度:** ★★★★★ 直接对应 Hermes 技能自举/「失败→规则沉淀」理念;多轮反馈闭环正是技能库维护的痛点

### 2. SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents
- **ID:** [2608.13173v1](https://arxiv.org/abs/2608.13173v1) | [📄 PDF](https://arxiv.org/pdf/2608.13173v1)
- **作者:** Chang Liu, Yuqi Zhang, Yiman Zhong, Boyi Liu, Hengjun Wang, Shuyue Wei
- **分类:** cs.AI
- **摘要:** Agent 技能是执行长程任务(编码/文档处理)的关键外部指令,但每步对整体技能的贡献缺乏量化。SkillShapley 将技能步骤归因建模为 **Shapley 值贡献估计**,提出边界自适应(边界适应)估值方法,回答"技能里哪一步真正有用"。
- **关联度:** ★★★★ 技能工程可解释性;可借鉴评估自己技能库中各步骤的有效性

### 3. Teach the Magnitude, Not the Direction: Verifier-Bounded Credit Assignment for Multi-Turn Multi-step LLM Agents
- **ID:** [2608.13179v1](https://arxiv.org/abs/2608.13179v1) | [📄 PDF](https://arxiv.org/pdf/2608.13179v1)
- **作者:** Zechuan Wang, Siyuan Lu, Hongxuan Zhang, Linjian Mo, Chenyi Zhuang, Leilei Gan
- **分类:** cs.AI
- **摘要:** 可验证奖励 RL(RLVR)给多轮工具 Agent 设了验证器边界上限,但轨迹级信用分配把异构每轮结果混成一个信号;on-policy 蒸馏给稠密 token 监督却受教师限制或梯度坍缩。提出 **CrEST 层次化信用分配**:保留 RL 的验证器边界,同时从特权自教师引入稠密 token 级信号,教"幅度"而非"方向"。
- **关联度:** ★★★★★ Agent 训练前沿;与 Hermes 模型容灾/RL 配置思路可对照

### 4. AQuA: Recursively Self-Improving Quantitative Trading Research Agents
- **ID:** [2608.12841v1](https://arxiv.org/abs/2608.12841v1) | [📄 PDF](https://arxiv.org/pdf/2608.12841v1)
- **作者:** Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, Mengdi Wang
- **分类:** cs.CL, cs.AI
- **摘要:** 研究**递归自改进**能否发生在量化投资研究层面:系统是否能用早期实验证据改进后续迭代的假设与候选。AQuA 含两个独立 LLM 研究系统(符号因子发现 + 可训练模型开发),互不共享 Agent/记忆/候选空间,各自用密封沙箱(固定数据划分/特征/评估器)闭环保留验证证据并指导后续提案。
- **关联度:** ★★★★ 与 sora 股票分析 cron 直接相关;封闭沙箱 + 证据回流的自改进范式可借鉴

### 5. Training AI Scientists to Replicate Research
- **ID:** [2608.13331v1](https://arxiv.org/abs/2608.13331v1) | [📄 PDF](https://arxiv.org/pdf/2608.13331v1)
- **作者:** Damon Falck, Samer Sabri, Anja Surina, Thom Foster, Anya Sims, Sam Devlin, Dylan Rogers, Tantum Collins, Kaloyan Aleksiev, Louis Kirsch, Edward Hughes
- **分类:** cs.LG, cs.AI
- **摘要:** 论文可复现性是科学基石。提出 **Replica**,可扩展的论文复现任务空间;用自动生成 rubric 判官(低噪声、与人类复现质量评估一致)提供奖励信号。后训练 **Faraday**,27B 参数"AI Scientist" Agent(以编码 Agent 为工具),在留出复现任务上**超越 Claude Opus 4.8 和 GPT-5.5**,且个体 rollout 分析显示其采用更科学化方法。
- **关联度:** ★★★★★ AI Scientist 前沿 + 27B 小模型胜闭源大模型;rubric 判官设计可迁移到 sora 的学术/评测工作

### 6. Beyond Final Scores: A Systematic Evaluation of Agents for Long-Horizon AI Research and Development
- **ID:** [2608.13417v1](https://arxiv.org/abs/2608.13417v1) | [📄 PDF](https://arxiv.org/pdf/2608.13417v1)
- **作者:** Yiwei Li, Wanli Yang, Hexiang Tan, Xiangzhou Huang, Zhengyu Chen, Ziran Li, Borun Chen, Shanglin Lei, Huaisheng Zhu, Hao Tian, Fei Sun, Xunliang Cai
- **分类:** cs.AI
- **摘要:** 评估长程 AI 研发 Agent 不能只看最终分数——分数不揭示进步发生在哪、失败在哪、经验是否改善后续决策。对 **7 个前沿模型 × 36 个长程任务**做系统评估:基于规则指标刻画运行内行为(Solution Framing / Execution / Feedback Control)+ 受控对比评估跨任务经验复用。结论:当前 Agent 更像**工程优化器而非自主研究员**——能提出并实现实用方案,但体验复用与自主研究能力有限。
- **关联度:** ★★★★★ Agent 能力边界实证;评估方法论(过程指标而非最终分)对 Hermes 自评/技能评测有直接参考

---

## 二、多 Agent 系统与通信

### 7. StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems
- **ID:** [2608.13317v1](https://arxiv.org/abs/2608.13317v1) | [📄 PDF](https://arxiv.org/pdf/2608.13317v1)
- **作者:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- **分类:** cs.AI
- **摘要:** LLM 多 Agent 通常用离散 token 通信,存在信息瓶颈;潜空间通信(直接传隐藏表示)无需转文本,但现有方法要么逐层注入工作记忆、要么需训练投影器(可移植性差)。StateBridge 用**闭式正交变换**对齐发送方末层隐藏态到接收方输入空间,轻量范数校准 + 词汇锚定保证与预训练输入分布兼容,**免训练**即可跨模型通信。
- **关联度:** ★★★★ 免训练潜通信是工程友好方向;多 Agent 协作效率参考

### 8. Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference
- **ID:** [2608.12921v1](https://arxiv.org/abs/2608.12921v1) | [📄 PDF](https://arxiv.org/pdf/2608.12921v1)
- **作者:** Junzhi Li, Peng He, Qirui Ji, Wei Wang, Lixiang Liu, Chuxiong Sun
- **分类:** cs.MA, cs.AI
- **摘要:** LLM 多 Agent 系统性能依赖通信拓扑,但现有拓扑生成用黑盒优化(仅任务奖励驱动),不解释为何选某条通信边。提出 **E2-Explainer**,模型无关框架:把拓扑解释建模为**因果归因问题**,识别保持任务表现的紧凑通信子图(边缘级证据,Granger 风格因果检验),回答"哪条通信边真正关键"。
- **关联度:** ★★★★ 多 Agent 拓扑可解释性;对理解/优化 Agent 协作结构有参考

### 9. BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Deliberation through Evolving Decision Graphs
- **ID:** [2608.13046v1](https://arxiv.org/abs/2608.13046v1) | [📄 PDF](https://arxiv.org/pdf/2608.13046v1)
- **作者:** Sanjeev Manivannan
- **分类:** cs.AI, cs.CE, cs.ET
- **摘要:** 传统多 Agent 系统:人类给初始问题 → Agent 内部协商 → 返回结果,人无中途干预。BoardroomAI 把人类当作**持续参与者**:可质疑假设、改约束、调优先级、引入证据、重定向决策。四组件:类型化决策图(证据/假设/约束/主张/异议/替代/风险/决策/语义依赖/专家职责)、干预编译器(人类动作→显式图更新)、依赖感知传播(识别受影响子图、保留未受影响工件)、选择性重激活。
- **关联度:** ★★★★ 人机共存决策范式;与 Hermes"用户中途 steering/纠偏"理念契合

### 10. Agent Behavioral Contracts II: Certifying Compositional Reliability Without Assuming Independence
- **ID:** [2608.12895v1](https://arxiv.org/abs/2608.12895v1) | [📄 PDF](https://arxiv.org/pdf/2608.12895v1)
- **作者:** Varun Pratap Bhardwaj, Garima Singh, Arun Pratap Bhardwaj
- **分类:** cs.AI, cs.MA
- **摘要:** 多 Agent 组合可靠性上界=各组件可靠性相乘,前提是**条件独立假设**——常被声明却从不检验。本文检验:同一模型两个实例在双 Agent 交接中,**90.0% 的失败任务会同败**(log OR 6.66,phi 0.916,预注册 18,000 任务、确定性代码评分、无 LLM 判官)。换模型降低六组对比中的关联;换厂商(模型已不同)则不降——正依赖使联合失败高于独立乘积,**冗余被过度信任恰因组件共享模型**。无假设替代往往空洞,拟合依赖模型更糟(证明 bootstrap 上界)。
- **关联度:** ★★★★★ 对 Agent 系统可靠性设计是硬核提醒:同模型冗余不等于可靠;预注册 + 确定性评分的方法论值得学习

### 11. ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification
- **ID:** [2608.12877v1](https://arxiv.org/abs/2608.12877v1) | [📄 PDF](https://arxiv.org/pdf/2608.12877v1)
- **作者:** Runze Zhao, Zixin Tang, Xiaoshuai Hao, Leyuan Chang, Xiaopeng Fu, Boyu Qiao, Dongyang Zhang
- **分类:** cs.AI
- **摘要:** 多跳事实核查对抗社交媒体虚假信息。现有多 Agent 协作方法两大缺陷:子任务执行缺乏全局目标意识、参数知识与证据冲突破坏证据推理。ReflectFact 引入三个关键机制:显式推理路径规划(构建证据锚定推理路径)、自反思(执行后对照全局目标修正)、证据冲突消解。
- **关联度:** ★★★ 事实核查/证据链推理参考;与知识库真实性维护弱相关

---

## 三、Agent 记忆与知识

### 12. RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory
- **ID:** [2608.13334v1](https://arxiv.org/abs/2608.13334v1) | [📄 PDF](https://arxiv.org/pdf/2608.13334v1)
- **作者:** Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, Yunxiao Qin
- **分类:** cs.CL
- **摘要:** LLM Agent 长期记忆的瓶颈不是存储,而是**当相关信息分散在许多交互中时如何取回正确证据**。全文上下文噪声大、平面检索返回孤立不完整记录、图记忆系统构建贵且压缩事件上下文。RippleMem 用**联想式回忆**替代一次性检索:交互历史存为线索丰富的**情节记忆单元**,组织成事件中心记忆图;查询时先混合线索回忆记忆锚点,再沿图联想扩散取回完整证据集。
- **关联度:** ★★★★ 与 Hermes 记忆/会话检索机制直接相关;联想式取回 vs 平面检索的取舍值得研究

### 13. Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research
- **ID:** [2608.12984v1](https://arxiv.org/abs/2608.12984v1) | [📄 PDF](https://arxiv.org/pdf/2608.12984v1)
- **作者:** Xing Zhang, Yanwei Cui, Guanghui Wang, Peiyang He
- **分类:** cs.MA, cs.CL
- **摘要:** LLM 长报告会漂移、自相矛盾、丢来源(同一指标多个值、谣言被当审计文件引用)。提出双层 Agent 系统:确定性 **librarian** 把带时间戳来源摄入**信任分层本体**(证据卡 + 权威指标账本 + 声明图,始终最新的真值源,非逐查询 RAG);可移植多 Agent **writer** 在任意知识截止点 T 组合报告,只读 as_of ≤ T 的证据(无前视);红队裁决回流 librarian。自有 6,130 来源语料,555,926 张证据卡(SEC EDGAR 295 发行人 + 11 个行业)。
- **关联度:** ★★★★★ 与 sora 文献周报/知识库工作**高度相关**;信任分层 + 时间点查询解决"报告漂移/来源丢失"痛点,可借鉴到 Obsidian 知识管护

---

## 四、Agent 安全与治理

### 14. Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents
- **ID:** [2608.12977v1](https://arxiv.org/abs/2608.12977v1) | [📄 PDF](https://arxiv.org/pdf/2608.12977v1)
- **作者:** Jiajun Ruan, Peiyang Li, Yukun Chen, Fengting Li, Chao Feng
- **分类:** cs.CR, cs.AI
- **摘要:** LLM Agent 能力扩张带来复杂安全威胁;运行时防御(把安全机制集成进 Agent 执行环)有效,但现有防御高度依赖手工设计干预、缺乏构建与维护的原则框架。本文先给出 **harness 级运行时防御形式化**:系统刻画 harness 机制如何支撑防御构建,为自进化防御(自动发现/更新防御策略)奠基。
- **关联度:** ★★★★ 与 Hermes harness/安全审计视角契合;"harness 级防御形式化"思路可直接映射

### 15. RAIL: An Automatic Classifier of the Artificial Intelligence Readiness Level
- **ID:** [2608.13428v1](https://arxiv.org/abs/2608.13428v1) | [📄 PDF](https://arxiv.org/pdf/2608.13428v1)
- **作者:** Juan Irving Vasquez, Juan Terven, Laura-Ivoone Garay-Jimenez
- **分类:** cs.AI
- **摘要:** AI 技术成熟度评估对投资/项目管理/政策监控重要,但现框架异构难自动应用。统一三个框架为 **Unified AI Readiness Level (AIRL)**:九级序数刻度(环境证据阶梯)+ 维度上限(规格/数据存在/数据质量/数据合法性/专家知识/算法成熟度)+ 通用性锚定规则 + 显式分级纪律,使就绪度可从自然语言描述自动判定(分类器实现)。
- **关联度:** ★★★ 通用方法论;对项目选型/技术评估有参考

---

## 简评

| ID | 标题 | 一句话 | ★ |
|----|------|--------|---|
| 2608.13552 | PlayWorld: Benchmarking World Models with Agent Players | 用多模态 Agent 玩家交互评估视频世界模型,避免固定动作序列不适配跨模型比较 | ★★★ |
| 2608.13463 | MLLM-Routed Heterogeneous Ensembles (ARMDIL) | MLLM Agent 动态路由图像到最合适视觉骨干,混合 CNN/SSL/VLM 集成 | ★★ |
| 2608.13420 | Enhancing Virtual Agents through SLMs and Edge-Computing | 边缘 SLM 支撑虚拟世界 Agent 的 Think/Memory 组件(NVIDIA Jetson) | ★★ |
| 2608.13344 | LongEarth-R1 | 遥感长程推理基准(12 任务/117k 图)+ VLM 对齐 | ★★ |
| 2608.13258 | Self-Referential Induction Increases Response Instability | 自指提示(主观体验类)响应最不稳定(0.343),无解哲学次之,可验证问题最稳 | ★★ |

---

## 今日要点

- **主线**:08-13 提交池的最后一批强相关论文,集中在**技能自改进(SkillEvo/SkillShapley)**、**Agent 训练信用分配(CrEST)**、**长程研发评估(Beyond Final Scores)**、**组合可靠性实证(Behavioral Contracts II)** 与 **记忆/知识(Reconcile Once/RippleMem)**
- **与 sora 直接相关**:Reconcile Once(文献防漂移,映射 Obsidian 管护)、AQuA(股票分析自改进)、Faraday 27B 胜闭源(AI Scientist 小模型路线)、Behavioral Contracts II(同模型冗余不可靠——Hermes 模型容灾链的独立供应商兜底正好印证)
- **理论前沿**:StateBridge 免训练潜通信、BoardroomAI 人机共存决策、E2-Explainer 拓扑因果解释
- **下次判定**:arXiv 索引仍冻结在 08-13 时,下一份速览应 [SILENT],不再重报本池

---

*关联:上一份 [arxiv-2026-08-14-agent-llm](arxiv-2026-08-14-agent-llm) · 上一份 core-contributions · [arxiv-digest](arxiv-digest) · [HOME](../HOME.md)*
