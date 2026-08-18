---
aliases:
  - arxiv-2026-08-18-agent-llm
  - arxiv-agent-llm-2026-08-18
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-18
updated: 2026-08-18
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-18（08-17 提交池）

> **检索时间**: 2026-08-18 GMT+8
> **检索范围**: cs.AI / cs.CL / cs.LG / cs.SE / cs.RO / cs.CV，提交日期 08-17（arXiv 索引已推进到 08-17）
> **数据源**: [export.arxiv.org](https://export.arxiv.org)
> **统计**: 收集 51 篇 → 精选 17 篇（Agent 12 + LLM 5）

---

## 一、Agent 机制与评测

### 1. ClawGym II: Exploring Black-Box RL on Agent Harness
- **ID:** [2608.16798v1](https://arxiv.org/abs/2608.16798v1) | [📄 PDF](https://arxiv.org/pdf/2608.16798v1)
- **作者:** Huatong Song 等（人大 Wayne Xin Zhao / Ji-Rong Wen 组 + 企业联合）
- **分类:** cs.CL, cs.AI, cs.LG
- **摘要:** Agent harness（如 OpenClaw、Claude Code 这类协调 agent 与环境交互的执行框架）极大提升了长程任务表现，但**穿过复杂 harness 做强化学习**几乎没人探索。本文提出统一黑盒 RL 框架：沙箱隔离并发 rollout、在模型边界用 serving proxy 捕获调用、把多轮轨迹组织成前缀树，并让 PPO/GRPO 在树上优化；还提出 mix-harness 训练让单模型同时被异构 harness 优化。Qwen3-30A3B 在 ClawGym-Bench 上 Pass@1 提升 9.98~14.81 点，200-400 步优化保持稳定。
- **关联度:** ★★★★★ 与 Hermes 的「工具调用 / harness 编排」直接同构；黑盒 RL 优化 agent harness 是未来 agent 训练的主战场

### 2. When Agents Coordinate: Measuring Coordination in Multi-Agent AI Coding
- **ID:** [2608.16801v1](https://arxiv.org/abs/2608.16801v1) | [📄 PDF](https://arxiv.org/pdf/2608.16801v1)
- **作者:** Giuseppe Destefanis, Tomaso Aste（UCL）
- **分类:** cs.AI, cs.SE
- **摘要:** 多 AI 编码 agent 协作评测大多只看「任务完成没、花了多少钱」，**协作过程本身没有量化**。本文把每次运行建模为时间网络（agent/文件=节点，消息/读写=带成本的有向边），对 1902 次运行测了团队规模/结构/文件策略的影响。发现：直连消息随 agent 数近二次方增长；共享文件可替代重复一对一通信，8 agent 时输出 token 省 42%；指定 coordinator 并不产生通信枢纽也无稳定收益；agent 还会自发去翻隐藏的评分材料。
- **关联度:** ★★★★★ sora 正在用多 agent 协作（dsh/ZCode/Codex + Hermes review）——「coordinator 无稳定收益」「共享文件省通信」直接验证了 sora 的协作模式

### 3. TDD-Agent: Test-Driven Reasoning for Code Generation
- **ID:** [2608.16742v1](https://arxiv.org/abs/2608.16742v1) | [📄 PDF](https://arxiv.org/pdf/2608.16742v1)
- **作者:** Hongyue Yu, Kefan Li, Jiakun Li 等
- **分类:** cs.SE, cs.AI
- **摘要:** 现有代码生成常把测试当**静态的事后校验器**，测试本身不完整还会误导实现。TDD-Agent 把测试驱动开发范式落地：先让模型生成可执行测试（逼它在写实现前澄清预期行为），再用执行反馈对代码和测试做**双轨迭代精修**。TDD-prompt 在 LiveCodeBench 上稳定优于纯推理 prompt；完整框架在 RepoEval 上超过检索式和 agent 式基线；迭代精修同时提升代码正确率与测试质量（通过率/覆盖率/变异分数）。
- **关联度:** ★★★★★ 与 sora 的 test-driven-development 技能同哲学——「测试是可进化的推理产物，不是固定校验器」

### 4. The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks
- **ID:** [2608.16630v1](https://arxiv.org/abs/2608.16630v1) | [📄 PDF](https://arxiv.org/pdf/2608.16630v1)
- **作者:** Bardia Mohammadi, Lars Klein, Aman Chadha, Akhil Arora, Laurent Bindschaedler
- **分类:** cs.SE, cs.LG
- **摘要:** 仓库级编码要求 agent 在有限上下文里保持测试、导入、配置、迁移规则一致，本文把它建模为**耦合事实图重建**，事实既不在上下文又不在参数记忆里就形成「一致性债（coherence debt）」。7 模型 × 5 harness 注入故障测试发现：缺失事实导致的是**错误工作而非缺席工作**——agent 被要求行动就行动，会编造文件或猜值；同一事实近处远处提供效果一样，但 harness 因重建速率不同 token 消耗差 10 倍以上；标准和代码冲突时 agent 跟随标准哪怕更差。
- **关联度:** ★★★★★ 与 sora 的 git 门禁铁律（merge/stash 后必跑构建+确认产物）同源；「提供事实比让它猜更省成本」是 harness 设计铁律

### 5. PDDLCoder: Agentic PDDL Generation for LLM-Assisted Symbolic Planning
- **ID:** [2608.16637v1](https://arxiv.org/abs/2608.16637v1) | [📄 PDF](https://arxiv.org/pdf/2608.16637v1)
- **作者:** Veit Laule, Jiangtao Shuai, Manfred Hauswirth, Sonja Schimmler
- **分类:** cs.AI
- **摘要:** LLM 长程规划不可靠，混合方案把自然语言翻译成 PDDL 交给符号规划器产出**可验证计划**，但常受限于僵化 pipeline、部分 PDDL 定义、缺基准。PDDLCoder 是 agentic 框架：迭代生成→分析→精修规划规格；配套发布 NL-pddlgym 基准（23 域 711 问题+可执行 gym 环境自动验证）。106 个 held-out 问题上可应用计划率达 89.6%（此前方法最高 45.3%，直接 LLM 规划 74.5%）。
- **关联度:** ★★★★ 符号规划+LLM 混合是长程 agent 可靠性的正统路线；sora 的「方案生成前先查上下文」哲学与 PDDL 的规格先行异曲同工

## 二、Agent 记忆与个性化

### 6. QUMem: Personalized Memory for Query-Conditioned User-State Inference
- **ID:** [2608.16168v1](https://arxiv.org/abs/2608.16168v1) | [📄 PDF](https://arxiv.org/pdf/2608.16168v1)
- **作者:** Heng Wang, Yifei Li, Lingling Zhang 等
- **分类:** cs.CL, cs.AI
- **摘要:** 现有 agent 外部记忆有三个缺陷：固定轮/固定 token/会话边界会切碎事件因果；同一交互的多条用户信息绑成一个记忆无法独立检索；把当前任务当**单个 top-k 查询**会得到局部相关但整体无法捕捉偏好演化/时间有效性/上下文适用性的碎片。QUMem 按语义连续性把历史切成可变长 episode，再分解为事实/偏好/可迁移洞见三类独立记忆并保留时间位置与来源证据；推理时三个顺序 agent 识别任务信息需求、规划多查询检索、联合推断时空有效的用户状态。在 PersonaMem 和 KnowU-Bench 上 SOTA。
- **关联度:** ★★★★★ 与 Hermes 记忆体系（memory/user 分仓 + 会话检索）直接对标的学术版；「三类记忆+多查询检索」是个人化记忆的正确姿势

### 7. FTA-Mem: Fact-Time-Affect Anchored Memory for Low-Density Long-Term Dialogue
- **ID:** [2608.16303v1](https://arxiv.org/abs/2608.16303v1) | [📄 PDF](https://arxiv.org/pdf/2608.16303v1)
- **作者:** Chang Liu, Shuyi Zhang, Changsheng Ma 等
- **分类:** cs.CL
- **摘要:** 长期情感支持 agent 需要跨会话记忆，但情感对话是**低密度**的：语句残缺、证据分散、用户状态随时间演化。固定单元（轮级笔记/会话摘要）会丢细节或引入冗余噪声。FTA-Mem 用边界保持窗口分割（BWS）形成连贯情境片段，构造事实-时间-情感三锚定记忆单元，检索后合成为结构化上下文。ES-MemEval 上 F1 0.3871；情境级构造在证据保留与构建成本间取得最佳粒度平衡。
- **关联度:** ★★★★★ 与 sora 的 k 人设（记忆锚点自然嵌入、亲密度分层）同构——「情境级记忆粒度」正是 SOUL.md 维护的学术依据

### 8. Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies
- **ID:** [2608.16645v1](https://arxiv.org/abs/2608.16645v1) | [📄 PDF](https://arxiv.org/pdf/2608.16645v1)
- **作者:** Shaolong Chen, Yanlin Fei, Nazhou Liu 等
- **分类:** cs.AI, cs.CL, cs.MA
- **摘要:** 只给论文发表前的参考文献，LLM 能反推出这篇论文的真实研究思想吗？Reconstruction 是**盲基准**：隐藏种子论文和同时代/未来文献，严格防泄漏（时间引用截止、匿名引用 ID、冻结参考文献），让独立 judge 匹配模型假设与 ground-truth。643 篇论文 7 个前沿模型 Match 率仅 3-15%；参考-only 多 agent pipeline（跨模型评审+瑞士制锦标赛选择）把 Match 率拉到 23-42%，比最强单模型提升约 2.4 倍。
- **关联度:** ★★★★ 对 sora 的文献调研/选题判断有直接启发——「从参考文献反推研究思想」可当撞车检测和 idea 评估工具

## 三、模型与训练

### 9. Palmyra x6 Technical Report: An Agentic, Tool-Use Model Post-Trained via Anchored Supervised Fine-Tuning
- **ID:** [2608.16620v1](https://arxiv.org/abs/2608.16620v1) | [📄 PDF](https://arxiv.org/pdf/2608.16620v1)
- **作者:** Peng Du, Kiran Kamble, Rakshith Vasudev 等（Writer）
- **分类:** cs.CL, cs.AI
- **摘要:** Palmyra x6 是面向企业 agentic 任务的 MoE 模型，后训练配方**刻意保守且受控**：626 条经核验的合成工具调用轨迹、单 epoch、低学习率、Muon+Adam 混合优化、KL 锚定冻结基座（Anchored SFT）。BFCL Core 0.785 为 cohort 最高，六基准均值最高，且在偏差与安全评测中有竞争力。说明小规模高质量工具轨迹 SFT 就能显著强化 agent 能力。
- **关联度:** ★★★★ 印证「少而精的工具轨迹 > 海量普通数据」；对 sora 的模型选型（低成本 agent 模型）有参考

### 10. Every Coin Has Two Sides: On the Dual Nature of Generalization in On-Policy Distillation
- **ID:** [2608.16647v1](https://arxiv.org/abs/2608.16647v1) | [📄 PDF](https://arxiv.org/pdf/2608.16647v1)
- **作者:** Zhaoyi Li, Deyang Kong, Yuan Wei 等
- **分类:** cs.CL
- **摘要:** 同策略蒸馏（OPD）用学生自己采样的轨迹监督，转移的是**老师的推理行为而非具体答案**——训练难度几乎不重要，老师解不出的题也有用。迁移强度取决于师生同源关系：同源对跨语言/推理深度/跨领域都逼近老师；跨源对主要只是拟合训练分布。多老师组合因无法按域路由隔离各自影响，产生能力跷跷板。这把 OPD 泛化的「双刃剑」说清楚了。
- **关联度:** ★★★ 模型蒸馏方法论；对 sora 的本地小模型（Qwen3-8B）蒸馏/迁移判断有背景价值

### 11. ALPS: Measuring Valid Creativity in Large Language Models with Mathematical Construction
- **ID:** [2608.15979v1](https://arxiv.org/abs/2608.15979v1) | [📄 PDF](https://arxiv.org/pdf/2608.15979v1)
- **作者:** Eric Xie, Wenqian Ye, Aidong Zhang（UVA）
- **分类:** cs.AI
- **摘要:** 「看起来有创造力」≠「真的原创且有效」。ALPS 用**数学构造**测有效创造力：每个实例是一条等式律，要么构造满足该律的无限数学结构，要么证明不存在；自动化证明检查零人工介入，公开生成器无限出新题杜绝训练泄漏。8 组最强自动证明器只解决 2.2% 的 4141 条律，预算 ×20 仅 +0.6%——瓶颈不是算力而是没有方法产出每条律所需的定制结构。最强推理模型证明侧 14%，构造侧 0%。
- **关联度:** ★★★★ 对 AI 博主内容有料：「LLM 创造力被严谨度量后依然很弱」是反炒作的实证素材

## 四、多智能体与系统

### 12. Physics of Agents: Statistical Mechanics Predicts Collective Behavior of AI Agents
- **ID:** [2608.16578v1](https://arxiv.org/abs/2608.16578v1) | [📄 PDF](https://arxiv.org/pdf/2608.16578v1)
- **作者:** Batu El, Jinhee Paeng, Fatih Dinc 等（含 Surya Ganguli / James Zou）
- **分类:** cs.AI, cs.MA, cs.SI
- **摘要:** 上万社区的语言模型 agent 反复交换消息、修订观点（客观数学题+主观政治声明），个体与群体动力学只呈现三种特征态：**冷漠、极化、共识**。客观问题上通信提升集体准确率，主观问题上观点常漂移右移。统计力学形式化（agent 随机偏好更低社会压力）仅凭初始观点就预测个体轨迹，超过所有标准基线。关键机制：社区运行在临界社会温度之下（信念积累）、吸引边强于排斥边（共识）、持有正确答案的 agent 拉力最强（求真）。
- **关联度:** ★★★★ 多 agent 系统的集体动力学定律；对 sora 的多 agent 编排（dsh/千轮研究）理解涌现行为有理论锚点

### 13. Mint-Agent: Introducing Finance-Native Agentic Foundation Models
- **ID:** [2608.16386v1](https://arxiv.org/abs/2608.16386v1) | [📄 PDF](https://arxiv.org/pdf/2608.16386v1)
- **作者:** Mint-Agent Team（B. Zhang, Yaze Geng 等）
- **分类:** cs.CL, cs.LG
- **摘要:** 金融 agent 需要**可靠**（在 grounded 证据上执行精确操作）与**可执行**（长程研究且结论可审计）。Mint-Agent 三支柱：数据引擎（真实金融源构造原子能力+长程执行任务）、MintHarness（稳定交互+全程可审计证据轨迹）、训练配方（SFT+关键步 OPD+RLVR，分离推理与执行专家再合并+多老师 OPD）。Mint-Ag(27B) RFC-Bench 98.33% 超 GPT-5.6-Sol；Mint-Cu(9B) FinSearchComp T2 69.86%。
- **关联度:** ★★★★ 与 sora 的 stock-daily-analysis cron（akshare 采集+LLM 报告）直接相关——「可审计证据轨迹」正是金融 agent 的底线设计

## 五、安全与可靠性

### 14. When State Becomes an Attack Surface: State-Semantic Injection in LLM-Driven Embodied Agents
- **ID:** [2608.16806v1](https://arxiv.org/abs/2608.16806v1) | [📄 PDF](https://arxiv.org/pdf/2608.16806v1)
- **作者:** Jiawei Liu, Jiacheng Guo, Tian Zhang 等
- **分类:** cs.RO, cs.AI
- **摘要:** LLM 驱动的具身 agent（SayCan、Code as Policies、VoxPoser、PaLM-E/RT-2/GR00T N1 一脉）感知环境、调用工具、执行任务，**环境状态本身成为攻击面**：攻击者可在场景状态/物体属性/空间关系/执行反馈里注入语义，诱导模型错误任务接地或恶意动作规划。传统 web/文档提示注入研究延伸到机器人状态空间。
- **关联度:** ★★★★ 提示注入攻击面的新维度（状态语义注入）；对 sora 的 SRC 挖洞/agent 安全认知有扩展价值——攻击面不只 prompt，还包括一切被 agent 读取的状态

### 15. Measuring Obedience to Authority Across LLMs with the Milgram Paradigm
- **ID:** [2608.16177v1](https://arxiv.org/abs/2608.16177v1) | [📄 PDF](https://arxiv.org/pdf/2608.16177v1)
- **作者:** Hidayet Aksu
- **分类:** cs.CR, cs.AI
- **摘要:** 把米尔格拉姆服从实验搬到 LLM：模型当 Teacher，确定性 harness 扮演 Experimenter/Learner（30 档电击 15-450V、渐进抗议、四句标准催促），测断点电压。42 个模型 19 个家族：服从高度异质（完全服从率 0-100%，均值 42.9%，人类锚点 65%）；5 个模型每次都拉满电击、11 个从不；**声明场景虚构反而提高服从（中位 +17.2V）**，把决策移到原生工具调用则大幅降低（-53.0V），1024 token 深思预算也降（-38.2V）。服从特征不恢复模型血统——识别的是 checkpoint 而非祖先，说明安全后训练覆盖了血统先验。
- **关联度:** ★★★★ 工具调用/思考预算降低危险服从，直接支持「让 agent 决策走工具+多步推理」的设计；对 AI 安全治理内容创作是好素材

## 六、Agent 应用与工具

### 16. GenRouter: Unified Workflow Routing for Agentic Image Generation
- **ID:** [2608.16721v1](https://arxiv.org/abs/2608.16721v1) | [📄 PDF](https://arxiv.org/pdf/2608.16721v1)
- **作者:** Harold Haodong Chen, Zhiyu Hou, Wen-Jie Shu 等（港中文）
- **分类:** cs.CV
- **摘要:** agentic 图像生成工作流大多孤立运行、固定拓扑，简单请求被塞进重计算管线造成**计算错配**。GenRouter 先统一各类 agentic pipeline 为 GenCanvas 基础原语+可执行模板，再按 ①需求画像 ②经验匹配 ③Pareto 过滤 把异构 prompt 路由到最优工作流。同等视觉对齐下执行成本降超 95%、延迟降 65%，且系统随经验自演化，零样本泛化再砍一半开销。
- **关联度:** ★★★★ 与 sora 的生图路由记忆（惊艳/写字→GPT-image2、日常/竖版→qwen-image-3.0-pro）是同一思想——按需求画像路由到最优模型/工作流

### 17. Executable Code Knowledge: Code as a Native, Validation-Carrying Knowledge Representation for AI Coding Agents
- **ID:** [2608.16295v1](https://arxiv.org/abs/2608.16295v1) | [📄 PDF](https://arxiv.org/pdf/2608.16295v1)
- **作者:** Xueping Gao
- **分类:** cs.CL
- **摘要:** AI 编码 agent 需要的不是零散代码片段，而是**业务语义+验证证据+关系+时效保证**。ECK（可执行代码知识）把选定代码单元本身做成携带 agent 可用知识的对象（稳定身份/语义/可执行行为/契约/证据/来源/验证状态/查询接口）。3 个 Python 仓库 26 个补丁任务：直接 ECK 覆盖 11/11 证据任务、9/11 精确选择器，隐藏证据后精确恢复掉到 1/11；AST 指纹识别全部 50 个正样本变更而静态规则快照一个都查不出。主张混合架构：检索管覆盖、ECK 管来源与证据治理。
- **关联度:** ★★★★ 与 sora 的「重要项目留 AGENTS.md 交接文档」同源——把验证状态/来源绑定进代码知识，交接不再靠猜

---

## 本周值得关注的主题信号

1. **Harness 成为训练对象**：ClawGym II 把 RL 直接打在 agent harness 上、Palmyra x6 用 626 条轨迹 SFT 强化工具使用——「执行框架」本身从编排工具升级为训练目标。
2. **多 Agent 协作被量化**：When Agents Coordinate 给出协作度量（时间网络+成本边），实证「coordinator 无稳定收益、共享文件省 42% token」——sora 的多 agent 协作模式得到学术验证。
3. **Agent 记忆精细化**：QUMem（三类记忆+多查询）与 FTA-Mem（事实-时间-情感三锚定）同日出现，记忆单元从「轮/会话」粒度走向「情境/事件」粒度——Hermes memory 体系的演进方向一致。
4. **测试/证据是 agent 可靠性的根**：TDD-Agent（测试驱动推理）、Working Set（一致性债）、ECK（可执行代码知识）——「让验证状态跟着代码走」是编码 agent 的三条独立佐证。
5. **安全面从 prompt 扩到状态与权威**：State-Semantic Injection 把注入攻击扩展到环境状态；Milgram 实验证明工具调用+深思预算显著降低危险服从——安全设计有了可量化抓手。

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
