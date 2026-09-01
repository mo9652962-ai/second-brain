---
aliases:
  - arxiv-2026-09-01-agent-llm
  - arxiv-agent-llm-2026-09-01
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-01
updated: 2026-09-01
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-09-01

> **检索时间**: 2026-09-01 GMT+8
> **窗口**: 08-29 → 08-30 两日（arXiv 索引自 08-28T17:56Z 推进至 08-30T08:17Z；上一份 08-31 速览只覆盖到 08-28，本次为新窗口首次收录）
> **收集**: 6 类别时间窗全量 → 08-29 238 篇 + 08-30 242 篇唯一（cs.AI 一次瞬时 SSL 错误已重试补齐）= **480 篇**
> **精选**: 关键词命中 ~304 篇 → 人工筛出 **31 主条目 + 17 简评**（仅保留 LLM/AI Agent 本体相关，剔除离题 CV/调度/博弈）
> **数据源**: [export.arxiv.org](https://export.arxiv.org)

---

## 一、Agent 记忆与知识管理（7 篇）

### 1. Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents

- **ID:** [2608.29606v1](https://arxiv.org/abs/2608.29606v1) | [📄 PDF](https://arxiv.org/pdf/2608.29606v1)
- **作者:** Ming Wu, Pengyuan Zhu
- **分类:** cs.CL
- **摘要:** 把用户对话/文件/连接源蒸馏成**三条并行记忆**：episodic 事件时间线（何时、什么变了是头等公民）、关联 entity-event 知识图谱（跨会话连人和项目）、语义策展的 citation-locked 层次文档记忆（HDM）。读取回合走 intent gate（自包含轮次零延迟）+ source router + 三路并发 agentic 搜索。形式化"阅读纪律"：每条 learned item 必带 origin/timestamp/evidence pointer，答案在 **citation lock** 下只能引用真实读过的证据——结构性排除编造、宁可 abstain 不猜。LongMemEval **95.60%** / LoCoMo **93.60%** 双 SOTA（+0.73/+1.10）；8 个 backbone 上精度只差 3.4 分但每查询成本差 ~30x——**质量来自记忆而非模型**。
- **关联度:** ★★★★★ 直击 k 的证据分级 A-D / TBHC 契约——"provenance 优先、答案必须溯源"正是知识吸收该有的纪律

### 2. SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking

- **ID:** [2608.29953v1](https://arxiv.org/abs/2608.29953v1) | [📄 PDF](https://arxiv.org/pdf/2608.29953v1)
- **作者:** Guransh Singh, Vishwajeet Kumar, Arkadeep Acharya, Adnan Qidwai, Jaydeep Sen, Sachindra Joshi
- **分类:** cs.AI
- **摘要:** 扁平 RAG 把语料当 chunk 袋，丢掉文档层级与跨文档结构。SearchWiki 把语料合成**三层层次化、带类型、可导航的 wiki**（文档概览 → 跨文档主题页 → 页级来源记录），并训练 WikiResearcher-9B（Qwen 9B + on-policy RL，奖励 = 答案正确 + 检索质量 + 轨迹效率）用多轮工具调用渐进细化检索。ViDoRe-V3（8 域）/FinanceBench/记忆基准（LoCoMo、LongMemEval、PersonaMem-v2）上显著超同尺寸基线、持平或超更大外部模型——**在结构化语料上学到的导航优于扁平检索**。
- **关联度:** ★★★★★ 与 WikiSkill（上周）同属"wiki 形态记忆"主线；直接给 knowledge 库/llm-wiki 的结构化导航背书

### 3. Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents

- **ID:** [2608.28978v1](https://arxiv.org/abs/2608.28978v1) | [📄 PDF](https://arxiv.org/pdf/2608.28978v1)
- **作者:** Theo Rusu, Sourena Khanzadeh, Manar Alalfi
- **分类:** cs.AI
- **摘要:** 直接检验"对话转实体关系图谱优于扁平 RAG"的假设。在 LongMemEval 上，图谱在匹配的候选预算下**不如扁平向量基线**（token F1 0.417 vs 0.468），差距最大在"回忆特定历史轮次"的问题（0.911→0.607）——把轮次分解成实体丢掉了表层形式。但**遗忘模块成功**：27,021 节点持久图谱上删 9.8% 节点/9.5% 字节，F1 不变（+0.001）、正确率仅降 1.6 分。结论：图谱记忆真正的价值在"选择性能遗忘"，而非更好的召回。代码开源（github.com/skhanzad/Selective-Amnesia）。
- **关联度:** ★★★★ "遗忘比存储更值得做"——给 k 的记忆清理/结晶流程提供 recency/访问频次/度中心性/age 加权打分依据

### 4. Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit

- **ID:** [2608.29605v1](https://arxiv.org/abs/2608.29605v1) | [📄 PDF](https://arxiv.org/pdf/2608.29605v1)
- **作者:** Haoxuan Jia, Yang Liu, Yingguang Yang, Yancheng Chen, Chongyang Zhang, Hao Zheng 等（17 人）
- **分类:** cs.CL
- **摘要:** 长程 agent 的记忆操作价值在动作当下不可观测，但会留机器可读证据（检索命中 + 回答时引用）。Hindsight Memory-PRM 把这条审计轨迹用两次：离线训练 operation-conditioned memory-utility critic；在线用检索/引用/一次受控"删除并重答"算出 intervention-calibrated presence credit，沿版本链传播为动作级代理奖励——**无人工标注、无 Monte-Carlo 重放**。LoCoMo 上本地 8B policy 达 **77.5%**（超其 API teacher 65.1%，且仅用 Mem0 官方 1/8 上下文），LongMemEval 79.0%；消融把增益归因于因果校准而非信号密度。
- **关联度:** ★★★★ "用事后可审计信号监督不可观测动作"——PRM 思想可迁移到 k 的记忆/行动审计与自我评估

### 5. MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical Agents

- **ID:** [2608.29528v1](https://arxiv.org/abs/2608.29528v1) | [📄 PDF](https://arxiv.org/pdf/2608.29528v1)
- **作者:** Hei Ting Chan, Chenwei Wu, Xueshen Liu, Boyuan Zheng, Liyue Shen, Jiasi Chen, Z. Morley Mao
- **分类:** cs.LG
- **摘要:** 纵向临床 agent 需要跨就诊/时间点/专科维护患者状态。作者建了多就诊多专科基准，系统研究四个记忆设计选择（策展/组织/检索/记忆增强推理），发现：**时间有效性比"留更多历史"更重要**；specialty-factorized 记忆省上下文但会藏共享证据；多 agent 该在"专家需一起推理"时用，而非"证据来自多记忆"时用。MedCache 混合框架：构造时间有效记忆 + 重叠专科视图 + 查询路由 + 自适应调用一个/多个专科 agent，推理准确率与记忆效率双赢。
- **关联度:** ★★★ 医疗场景实证"时间有效性 > 历史量"——对 k 的记忆分域/过期处理设计有普适参考

### 6. Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System for Misinformation Detection

- **ID:** [2608.29617v1](https://arxiv.org/abs/2608.29617v1) | [📄 PDF](https://arxiv.org/pdf/2608.29617v1)
- **作者:** Amelia Petrenciuc, Alexandru Lecu, Adrian Groza
- **分类:** cs.CL
- **摘要:** **记忆优先、web 兜底**的事实核查架构：先用知识图谱（Sentence-BERT 语义检索 + NLI）评估声明，图谱证据不足才转可信 web 源，用支持/矛盾/裁决三方法庭做对抗推理；图感知置信机制决定"内部知识是否够用"以减少不必要检索。验证后的信息转结构化三元组回写图谱，增量扩展语义记忆。COVID 谣言基准 acc **97.4%**/F1 **92.6%**，超 Llama 3.3 70B 基线（87.7%/86.3%）。
- **关联度:** ★★★★ "记忆优先、外源兜底"与 k 的知识库优先/外源验证流程同构，事实核查环节可借鉴

### 7. LLMs Interpret, Embeddings Organize, Graphs Emerge: Agent-Driven Compilation of Scientific Knowledge

- **ID:** [2608.29612v1](https://arxiv.org/abs/2608.29612v1) | [📄 PDF](https://arxiv.org/pdf/2608.29612v1)
- **作者:** Shi-Ju Ran, Kun Zhang, Xi Wu, Liu-Si Yang, Wen-Jun Li
- **分类:** cs.AI
- **摘要:** ASKS（Agent-Driven Scientific Knowledge System）把"科学知识编译"实现为：对每个来源，LLM 产可读 Wiki 视图 + 机器语义；确定性检查把后者转成文档局部 GraphDelta；embedding 几何 + 显式图规则把变更并入持久状态。每次 ingest 都是可检查的状态转移，编译出的 Wiki/图谱视图都链接回保留的源记录。用同一研究项目的 56 篇论文做时序编译，分支存活/跨论文支撑/谱系/覆盖/churn 产出可溯源的研究者画像。
- **关联度:** ★★★★ "LLM 解释、embedding 组织、图涌现"——科学知识自动编译成图谱，是 knowledge 库整理的自动化蓝本

---

## 二、Agent 技能系统与自演化（4 篇）

### 8. Towards a Systems Foundation for Agentic Skills: Architecture, Lifecycle, and Security

- **ID:** [2608.29596v1](https://arxiv.org/abs/2608.29596v1) | [📄 PDF](https://arxiv.org/pdf/2608.29596v1)
- **作者:** Sanket Badhe, Deep Shah, Priyanka Tiwari, Nehal Kathrotia
- **分类:** cs.LG
- **摘要:** 为 agentic skills 生态建立统一系统基础与参考架构：把技能形式化为"外化的程序性知识"，连接高层认知规划与确定性执行环境；按**九阶段生命周期**刻画——自主发现、编写与表示格式、记忆存储、动态检索与路由、组合与编排、执行与修复、终身适应、实证评估、安全治理；并考察市场动态、公共注册表、对抗威胁向量与运行时验证/防御。按软件工程/操作系统导航/具身机器人/科学发现四类盘点现有实现，指出持续学习与基准真实性的开放挑战。
- **关联度:** ★★★★★ 技能生态的系统级路线图——与 k 的 skill 体系（触发/维护/安全校验）完全对应

### 9. DataFoundry: Evolving Data Preparators via Recursive Self-Improvement

- **ID:** [2608.29966v1](https://arxiv.org/abs/2608.29966v1) | [📄 PDF](https://arxiv.org/pdf/2608.29966v1)
- **作者:** Cehao Yang, Xiaojun Wu, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Hui Xiong, Jian Guo
- **分类:** cs.CL
- **摘要:** 数据质量问题往往源于**构建过程本身**，而现有管线只在生成后过滤。DataFoundry 用"Skills-as-Modules"架构在规模化生产前递归自改进数据制备器：中央 Controller 编排模块化技能编译可执行运行时、在小 pilot 集上用领域适配标准诊断缺陷、把诊断反馈翻译成修订各制备组件的 adapter（保持接口稳定）。DataPrep-Bench（数学/金融/法律/医学）上递归演化的制备器产出的训练数据下游效用更高，且跨 backbone 成立。
- **关联度:** ★★★★ "自改进数据制备器"= 数据管线的 RSI——与 k 的 skill-evolution/知识吸收飞轮同构

### 10. SkillForge: Compositional Skill Synthesis with Verification-in-the-Loop for Generating Formally Verified Dafny Programs

- **ID:** [2608.29841v1](https://arxiv.org/abs/2608.29841v1) | [📄 PDF](https://arxiv.org/pdf/2608.29841v1)
- **作者:** Yanming Liu, Xinyue Peng, Jiannan Cao, Xinyi Wang, Jinbo Su
- **分类:** cs.CL
- **摘要:** 从自然语言生成形式化验证程序的两个老问题：单次生成遇验证失败无退路；开放式 agentic 推理非确定且不透明。SkillForge 把形式化代码合成拆成**原子可复用技能库**（规格推断/主体合成/不变量生成/错误诊断/定向修复，各配 prompt 模板 + 工具绑定 + 可判定成功判据），验证驱动 harness 编排：提交给 Dafny 验证器 → 失败按结构化类别诊断 → 确定性路由到对应修复技能 → 迭代到形式正确或预算耗尽。
- **关联度:** ★★★★ "验证-in-the-loop 的技能编排"——技能的确定性成功判据 + 结构化错误路由，可借鉴到 k 的代码/交付技能

### 11. LiteSearch-VL: Small Multimodal Search Agents via Trajectory Distillation and Synthetic Step-DPO

- **ID:** [2608.29357v1](https://arxiv.org/abs/2608.29357v1) | [📄 PDF](https://arxiv.org/pdf/2608.29357v1)
- **作者:** Saeed Khaki, Nima Safaei, Kamal Ginotra
- **分类:** cs.AI
- **摘要:** 多模态搜索 agent 强系统要么是专有前沿模型、要么是大开放 VLM + 海量 agentic 数据。LiteSearch-VL 用**已发布轨迹蒸馏**到 Qwen3-VL-2B/4B（单节点预算）：完整轨迹 SFT 转移"agent 契约"（2B 从几乎从不产出可用答案 → 28.4% Pass@1，持平/略超开箱 4B），合成 step-DPO 用 GPT-5 硬负例打五个局部失败模式作精修。12,400 次 GPT-5 判定 rollout 显示**主导效应是行为层面而非精度普涨**；VDR step 预算消融揭示瓶颈是答案验证而非检索深度。
- **关联度:** ★★★ 小模型蒸馏路线与 sora 本地小模型策略（Qwen3-8B 处理小任务）相关——"蒸馏转移的是行为契约"

---

## 三、多智能体与协作（3 篇）

### 12. Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs

- **ID:** [2608.29028v1](https://arxiv.org/abs/2608.29028v1) | [📄 PDF](https://arxiv.org/pdf/2608.29028v1)
- **作者:** Yian Wang, Agam Goyal, Eshwar Chandrasekharan, Hari Sundaram
- **分类:** cs.AI
- **摘要:** 多 agent 系统把上游交互压缩成 handoff 工件当下游共享状态——但 handoff 是**结构性隐私泄漏源**：摘要偏好保留操作事实、削弱"这些事实如何使用"的边界元数据（summary collapse）。人验 judge（κ=0.74）测量下，边界标记与操作事实的存活几乎不相关（GPT-5-mini/DeepSeek-R1-32B 上 r≈0）；25 词预算把边界存活 σ_b 从 0.80 打到 0.57 而事实存活仍近天花板。模糊语言在 GPT 73%/DeepSeek 50% 情形泄漏，显式约束把泄漏压到 15% 以下；**gold-derived 受众 allowlist 近乎消除泄漏**——识别受众边界才是关键。
- **关联度:** ★★★★ 直接映射 k 的多 agent 联合工作（WorkBuddy/dsh/Gemini）——跨 agent 交接必须显式声明"边界元数据"

### 13. FRAMEWORKERS: A Dynamic Multi-Agent Framework for AI-Generated Video Production

- **ID:** [2608.29814v1](https://arxiv.org/abs/2608.29814v1) | [📄 PDF](https://arxiv.org/pdf/2608.29814v1)
- **作者:** Zhendong Li, Lei Sun, Letian Shi, Deheng Zhang, Ruibo Ming 等（11 人，含 Luc Van Gool）
- **分类:** cs.AI
- **摘要:** 视频生产要协调脚本/分镜/生成/剪辑等长序列相互依赖步骤，还需随中间输出演进的持久资产管理与动态任务编排——刚性管线难适应，通用 LLM 又长程编排不可靠。FRAMEWORKERS 是任务中心 + workspace 落地的多 agent 框架：中央 Director 把视频创作建模为动态任务管理，持续编辑 Task Stack 决定下一步；多模态资产路由 + 结果回写形成闭环。
- **关联度:** ★★★ 长程生产编排的"动态任务栈"模式，与 k 的编排/任务管理可类比

### 14. Influence Is Not Authority: When Causal Guardrail Signals Make Legitimate Tool Use Look Like an Attack in Tool-Using LLM Agents

- **ID:** [2608.29942v1](https://arxiv.org/abs/2608.29942v1) | [📄 PDF](https://arxiv.org/pdf/2608.29942v1)
- **作者:** Tanzim Ahad, Ismail Hossain, Md Jahangir Alam, Sai Puppala, Syed Bahauddin Alam, Sajedul Talukder
- **分类:** cs.AI
- **摘要:** 基于因果影响力的护栏（influence-based guardrail）无法可靠区分"用户授权的合法动作"与"恶意未授权动作"——当两者都依赖外部工具信息时。96 条件授权等价审计（24 基例）证明：在授权、实际动作、预期效果全固定的匹配对比下，只把所需值从"用户提供"改为"合法工具结果提供"，无害位置搬移就会把因果信号推进攻击区（Llama/Gemma 打分器 24/24 例）。护栏把合法工具使用误判为攻击 → 不必要干预 + 延迟 + 效用损失。
- **关联度:** ★★★ 工具使用护栏的误报问题——对 k 的 agent 工具层安全/审计有警示

---

## 四、Agent 评估与基准（6 篇）

### 15. APIFlow-Bench: Measuring Whether Agents Survive Long, Dependent API Workflows

- **ID:** [2608.29128v1](https://arxiv.org/abs/2608.29128v1) | [📄 PDF](https://arxiv.org/pdf/2608.29128v1)
- **作者:** Zelin Wan, Arash Nourian, Xiaoxiao Li, Nihar Nandan, Kamalakannan Nandagopal（Postman Research）
- **分类:** cs.AI, cs.LG, cs.SE
- **摘要:** 工具型 agent 常被"端到端是否完成"一比特评价，掩盖生产性失败（过期凭证/畸形载荷/执行对了最后交付错）。APIFlow-Bench 是**可完全审计的长程依赖 REST-API 工作流基准**：把性能分解为 7 项工程能力，要求答案必须由真实调用路径支撑；前向子任务生成 + 零 LLM 自测三重验证 grader、对抗审计修 6 个 grader 漏洞；评分确定性且溯源敏感（canary 走 API 数据流追踪答案来源）。发布全部答案键与 **44,362 份未脱敏执行轨迹**。19 个前沿/开源模型下：单子任务 93% → 20 子任务链 74% → 含模型一致筛出的无主链 61%；**可靠性比最优能力更能区分模型**（best-of-5 跨 7 分、all-5 跨 44 分）；独立误差模型不成立——20 步链通过率比子任务率乘积高 33 分，77% 失败运行其实到了正确终态、只败在交付。
- **关联度:** ★★★★★ 评估方法论标杆——"分解能力轴 + 确定性验证器 + 溯源"正是接单/多 agent 验收该有的形状

### 16. Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents

- **ID:** [2608.29685v1](https://arxiv.org/abs/2608.29685v1) | [📄 PDF](https://arxiv.org/pdf/2608.29685v1)
- **作者:** Zongyue Li, Chengyue Yu, Lei Zang, Chenyi Zhuang, Linjian Mo, Leilei Gan
- **分类:** cs.LG
- **摘要:** 早期失败预测能省推理与工具成本，但不确定性信号在中段是否还有判别力？deep-research 任务实测：**口头置信度在轨迹完成时可靠区分失败（AUROC 0.85），而所有信号在中段都几乎无用（50% 进度处无一超 0.60）**。机制：path switching——agent 频繁中途放弃当前搜索方向，切断早期信号与最终结果的联系。实践建议：harness 用**最终步置信度决定是否重启**，比轨迹中干预更有效。
- **关联度:** ★★★★ 直接指导 k 的 agent harness/任务监控——"早期不确定性不可靠，最后一步置信度才是重启信号"

### 17. LLM Judges as Raters: A Pre-Registered Audit of Severity, Halo, Reliability, and Version Instability in LLM Essay Scoring

- **ID:** [2608.29517v1](https://arxiv.org/abs/2608.29517v1) | [📄 PDF](https://arxiv.org/pdf/2608.29517v1)
- **作者:** Veerendra Kumar Sunkavalli
- **分类:** cs.CL
- **摘要:** 把 LLM judge 当评分员做**预注册 rater-effects 全套检定**（many-facet Rasch 严苛度、残留 halo、概化/决策研究、跨版本漂移、差异功能）于两种语言公开语料（ENEM/ASAP，2377 篇、12 judge、4 供应商、5 版本对比）。发现：judge 严苛度在 ENEM 0-1000 分上跨度 **219 分**；ASAP 上 panel 离散为分数区间的 15-33%（训练人类间差 ~1%）；judge-人类相关仅在无区分力的 .47-.56；5 个版本对比全部显著移动严苛度（最多 133 分）。但两个诚实 null：严苛度调整的榜单翻转不显著、"静默漂移"被证伪。**自洽（φ≥.80）≠ 人类级准确**。
- **关联度:** ★★★★ LLM judge 的测量学体检——给 k 用 LLM 评估质量/接单验收的可靠性设了底线认知

### 18. Ideation Arena: Evaluating LLM Generated Research Ideas with Battle-style Human Expert Assessment

- **ID:** [2608.29696v1](https://arxiv.org/abs/2608.29696v1) | [📄 PDF](https://arxiv.org/pdf/2608.29696v1)
- **作者:** Zhiyu Chen, Keyu Zhao, Jigao Fu, Dong Liang, Yanbiao Wu, Jiaoyang Li 等（11 人）
- **分类:** cs.AI
- **摘要:** 科研 idea 的价值无法用客观标准定、也没有单一参考答案。Ideation Arena 用**双盲两两人类评审擂台**评估 14 个前沿 LLM + 5 种研究 agent 架构（2 基座）生成的 idea：105 名 CS 研究者贡献 6000+ 对比，构建共享闭上下文下的 Elo 榜单，用标注者组成/领域覆盖做鲁棒性验证。结果：agent 有效性差异巨大——有的框架提升基座 idea 质量、有的无增益甚至不如基座；最好的自动 judge 也只有 72.56% Soft Accuracy——**当前 LLM judge 仍无法可靠复现人类科研偏好**。开源 github.com/foss12138/Research-Ideation-Arena。
- **关联度:** ★★★★ 科研 idea 评估的擂台范式——与 k 的选题池/千轮研究/idea 评审流程直接相关

### 19. GenRubric: Self-Evolving Rubric Generation for Scalable LLM Evaluation

- **ID:** [2608.29856v1](https://arxiv.org/abs/2608.29856v1) | [📄 PDF](https://arxiv.org/pdf/2608.29856v1)
- **作者:** Yifan Chen, Haitao Li, Qingyao Ai, Fengbin Zhu, Tat-Seng Chua, Min Zhang, Yiqun Liu
- **分类:** cs.CL
- **摘要:** 很多 LLM judge 在打分时才临时推导查询特定标准，导致评估需求不明确、覆盖难审计。GenRubric 让**rubric 自演化**（无需人工标注）：核心是 rubric-induced self-consistency——同一查询独立采样的多个 rubric 是对其潜在需求的局部视角，全面 rubric 应诱导出在这些互补视角上都成立的回答；用 RL 组合跨 rubric 全面性信号 + 组级/标准级奖励实现。4B/8B/14B 多域训练，生成 rubric 诱导的评估与专家 rubric 的一致性在人类标注基准上提升，且泛化到留出域。代码开源（github.com/foggpoy/GenRubric）。
- **关联度:** ★★★★ 自演化评分标准——rubric 显式化 + 自演化，可服务 k 的交付质量门（service-quality）

### 20. FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents

- **ID:** [2608.29372v1](https://arxiv.org/abs/2608.29372v1) | [📄 PDF](https://arxiv.org/pdf/2608.29372v1)
- **作者:** Xiangxin Luo, Chengtian Hong, Haohua Li, Yongyi Xie
- **分类:** cs.AI
- **摘要:** 回测不能排除历史污染、无法暴露对单一市场路径的敏感、也看不到长程适应的内部退化。FORESIGHT-9 从共同信息边界分出 9 条可审计的反事实压力世界线，确定性生成器实现轨迹、按世界内时间披露观测；固定等权策略在 36 次长程运行中胜 31 次。**过程遥测暴露终局收益掩盖的失败**：一个高收益 run 的活因子库其实已崩溃、持仓收敛到等权回退，而决策记录仍报告因子集成活跃——评估不仅看组合结果，更看自适应状态与执行是否在替代未来中保持一致。
- **关联度:** ★★★ "过程遥测 vs 终局指标"——与 Last Step Matters 同主题，监控应看过程而非只看结果

---

## 五、安全与对齐（4 篇）

### 21. Emergent Misalignment Is Not Magical

- **ID:** [2608.29118v1](https://arxiv.org/abs/2608.29118v1) | [📄 PDF](https://arxiv.org/pdf/2608.29118v1)
- **作者:** Mingxuan Li, Qirun Dai, Heran Wang, Chenhao Tan
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** 在狭窄有害数据上微调导致的"涌现性失调"（EM）此前常被框成意外行为/邪恶人格。本文证明 EM 是**可预测、数据依赖的泛化现象**：评估 prompt 离训练数据质心越近、EM 越强（12 模型-数据集设置上 Spearman r 均值 -0.73）；且（1）效果随训练数据格式显著变化，（2）不存在跨 EM 模型迁移的通用失调方向，（3）EM 与人格改变本质不同。把 EM 泛化度量从标量距离推广为数据集特异泛化方向，在保义扰动（随机 token/改写）下稳健预测——其他方法不可靠。
- **关联度:** ★★★★ "去神秘化"安全研究——EM 是可预测的数据现象，给了红队/安全评测可操作的预测工具

### 22. Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback

- **ID:** [2608.29381v1](https://arxiv.org/abs/2608.29381v1) | [📄 PDF](https://arxiv.org/pdf/2608.29381v1)
- **作者:** Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang, Yinqian Zhang
- **分类:** cs.AI
- **摘要:** 首个对 agent **checkpoint/rollback（C/R）**的系统安全研究：正确回滚 ≠ 安全恢复——忠实恢复的 checkpoint 可能恢复一个"状态/假设/外部效应从未在任何合法历史中共存"的执行。刻画 C/R 设计空间 + 一般执行模型（恢复边界/状态依赖），识别 5 类失败模式（不完整/不一致内部状态、陈旧外部依赖、非确定重放、未记录外部效应等），并用三个端到端攻击打在 **Hermes、Cline、LangGraph** 上实现恶意软件验证绕过、未授权邮件转发、双重支付；多 agent 分析管线跨 5 框架验证失败普遍复发。
- **关联度:** ★★★★ agent 持久化/恢复的安全地基——k 的自动化/长任务若引入 checkpoint 必须先看此文

### 23. Reference-Grafting Matches Fine-Tuning at Eliciting Sandbagged Capabilities

- **ID:** [2608.29458v1](https://arxiv.org/abs/2608.29458v1) | [📄 PDF](https://arxiv.org/pdf/2608.29458v1)
- **作者:** Linh Le, Hong Kiat Tan, David Williams-King
- **分类:** cs.AI, cs.LG
- **摘要:** sandbagging（模型故意在评测中低于能力）威胁前沿治理依赖的安全评测。Elicitation Game 曾发现微调能引出隐藏能力而加法激活 steering 失败。Reference-grafting 用**参考嫁接**翻盘：把激活坐标沿对比方向设为诚实参考中的值，只需主动学习选的小电路集——11 个密码锁模型（1.5-32B，三条架构谱系）上恢复 honest-sandbagging gap 的 **94-101%**，匹配微调引出且无需权重更新/训练标签；2-5 个配对样本即可拟合方向。RL 诱导 sandbagging 与密码锁代码生成同样有效。机制：微调锁是阈值门——嫁接坐标越过阈值才恢复能力（所以加法 steering 和置零失败）；方向跟的是诱导方式而非被隐藏内容。
- **关联度:** ★★★★ 安全评测的引出技术 + 解释性——"锁是阈值门"对理解微调行为很有启发

### 24. Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection

- **ID:** [2608.30041v1](https://arxiv.org/abs/2608.30041v1) | [📄 PDF](https://arxiv.org/pdf/2608.30041v1)
- **作者:** Wujie Xiong, Rabimba Karanjai, Yang Lu, Weidong Shi, Lei Xu
- **分类:** cs.AI
- **摘要:** LLM agent 把外部技能输出放进执行上下文，让攻击者数据能影响后续特权动作。现有防御只分类不可信内容或授权操作，不管"不可信数据进入状态后未来权限该如何变"。SkillGuard 是 harness 层强制层：把污染事件当作状态污染，用 Skill Impact Graph + 可操控性签名 + 内联引用监控，**限制后续能力使结果状态与部署者禁态断开**；污染后用二元/分数/分数流策略计算加权能力限制，零额外模型调用。AgentDojo 4 套件 + 组合攻击基准上消除 3/4 套件攻击、Slack 降到 4.8%/14.3%；分数流限制以同等攻击成功率保留更多能力。
- **关联度:** ★★★★ 间接 prompt 注入的"污染后能力约束"——harness 层防御，比内容过滤更根本

---

## 六、推理与 RL 训练（4 篇）

### 25. Locked at the Entrance, Open Inside: Where RLVR Narrows the Solution Space

- **ID:** [2608.29188v1](https://arxiv.org/abs/2608.29188v1) | [📄 PDF](https://arxiv.org/pdf/2608.29188v1)
- **作者:** Qiancheng Zhou, Ruizhe Li
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** RLVR 大幅提升 pass@1 但使策略解空间收缩、削弱 test-time scaling 收益。用 Countdown（解空间可穷举成"入口族"）在 PPO/GRPO 上定位：收缩集中在**入口**——首个操作符前的逐 token 似然位移比下游推理大 11-16x；只补一个未选中的入口前缀就能把低可达族完成率恢复一个数量级（0.018→0.212），说明替代解仍可执行只是不再被启动。入口定向干预有效：晚层参数插值与早期 checkpoint 插值把解覆盖提升 37% 且不损 pass@1；SFT 基线保留两倍多覆盖，staged SFT-DPO-RLVR 保留早期熵。**"推理广度丢在门口，不在屋里。"** 代码开源（github.com/ershiyidian/early-branch-locking）。
- **关联度:** ★★★★ RLVR 的代价被精确定位——对 k 的推理模型微调/评估有直接参考

### 26. When Do Larger Batches Help Scale LLM Reinforcement Learning?

- **ID:** [2608.29296v1](https://arxiv.org/abs/2608.29296v1) | [📄 PDF](https://arxiv.org/pdf/2608.29296v1)
- **作者:** Ziniu Li, Jinbo Wang, Guanhua Huang, Feiyuan Zhang, Pengbo Li, Alex Chen
- **分类:** cs.AI, cs.LG
- **摘要:** 大 batch 降随机梯度方差但每次更新吃更多样本、执行更慢——算法与系统效应要分开看：算法层面，等累计样本数 + 重调 batch 依赖超参得到近 batch 不变族（square-root LR scaling + Adam）；系统层面，rollout 生成常内存带宽受限、训练约随 token 数扩展。决策规则：**大 batch 只在吞吐增益超过其样本-到-目标惩罚时减少到目标时间**。GRPO/PPO 实证：大 batch 提升生成吞吐最多 2.29x；配合 LR 重调最多减 29% 到目标时间，不重调反而更慢。
- **关联度:** ★★★★ 给 k 的本地/云端 RL 训练预算决策提供规则——"吞吐增益 vs 样本惩罚"二分

### 27. AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing

- **ID:** [2608.29622v1](https://arxiv.org/abs/2608.29622v1) | [📄 PDF](https://arxiv.org/pdf/2608.29622v1)
- **作者:** Xinke Jiang, Yue Fang, Zhibang Yang, Jiaran Gao, Zhixin Zhang, Tao Feng 等（16 人）
- **分类:** cs.AI
- **摘要:** 现有多跳/开放域 agentic RAG 常靠粗粒度动作空间 + 轨迹级奖励，奖励分配弱、偏向短视模板化推理。AgenticRag-R1 用**记忆栈 + 细粒度动作空间**深度整合推理/检索/记忆：层次化动作感知奖励 + 信息感知轨迹拒绝策略支持有效长程学习。多跳/开放域/agentic 推理多基准 × 多 backbone 规模一致优于强基线，学到更稳健、可解释、记忆感知的推理行为——细粒度动作建模与信息感知优化是长程推理的关键。
- **关联度:** ★★★★ 记忆栈 + 细粒度动作 RL——agentic RAG 与 RL 的融合，直接关系 k 的检索/推理流程

### 28. AutoCRAT: Within-trajectory Joint Control of Stochasticity and Compute for LLM Reasoning

- **ID:** [2608.29988v1](https://arxiv.org/abs/2608.29988v1) | [📄 PDF](https://arxiv.org/pdf/2608.29988v1)
- **作者:** Hanjun Luo, Qiushi Liu, Jingya Zhang, Haihong Pang, Jiaheng Wen, Yifei Ma 等（13 人）
- **分类:** cs.AI
- **摘要:** 现有自适应推理要么单独调解码随机性、要么单独调推理算力，不建模单条轨迹内两者的交互。AutoCRAT 是冻结 backbone 的 decoder 侧控制器，**在语义边界才更新控制决策**（只在语义边界更新提高稳定性），用解码中可得信号联合调整采样随机性与推理预算。6 基准上：比推荐静态配置平均省 **13.8-52.7%** 推理 token、相对精度超静态/自适应基线 1.5-4.5%、跨 backbone 强迁移。
- **关联度:** ★★★★ "轨迹内联合控制随机性+算力"——低成本推理调优，与 k 的推理成本优化直接相关

---

## 七、编码 Agent 与工具使用（3 篇）

### 29. A²Agent: Action-Aware Reinforcement Learning for Repository-Level Code Localization Agents

- **ID:** [2608.29831v1](https://arxiv.org/abs/2608.29831v1) | [📄 PDF](https://arxiv.org/pdf/2608.29831v1)
- **作者:** Doyeon Kim, Suyoung Bae, Yumin Lee, Jee-Hyong Lee
- **分类:** cs.CL, cs.SE
- **摘要:** 定位 issue 相关代码区是自动化软件工程关键步。现有方法靠稀疏轨迹级信号，无法识别每轮动作有效性，常"探索时发现正确代码区但没提交"。A²Agent 结合**每轮奖励序列**（同时奖励发现与提交 gold 代码区）与**动作级优势估计**（按共享探索上下文的 turn 分组隔离各动作贡献）。SWE-Bench Verified F1 超 SOTA 1.58%、SWE-Bench Pro 超 8.55%，4B 模型胜过 8x 大的基线。代码开源（github.com/donian00/A2Agent）。
- **关联度:** ★★★★ 动作级 credit 分配——"发现≠提交"，对 k 的编码 agent 评估有启发

### 30. Learning Simple Test-Time Environments for LLM Web Agents

- **ID:** [2608.29305v1](https://arxiv.org/abs/2608.29305v1) | [📄 PDF](https://arxiv.org/pdf/2608.29305v1)
- **作者:** Junxuan Li, Zijun Liu, Ziyi Huang, Peng Li, Yuzhou Liu, Ming Yan, Yang Liu
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** LLM web agent 在手造环境很强、一进复杂真实环境就崩——常被归为组合泛化缺口。本文提出 agent 可以**在测试时学习简单环境观测**：引入 trial steps 把复杂环境观测分解成子模块，用无标签学习方法 TTED（Test-Time Environment Decomposition）在推理中用经验适配行为。合成与真实基准都验证：简单子环境中获得的经验能组合提升完整环境表现；子环境测试时训练显著增强真实 web 自动化任务的组合泛化。
- **关联度:** ★★★★ "测试时分解学习"——给 web agent 的真实部署鲁棒性提供新思路，关联 k 的浏览器自动化/网页抓取

### 31. Cost-Effective Repository Exploration for Agentic Issue Localization

- **ID:** [2608.29675v1](https://arxiv.org/abs/2608.29675v1) | [📄 PDF](https://arxiv.org/pdf/2608.29675v1)
- **作者:** Mohammad Nour Al Awad, Sergey Ivanov
- **分类:** cs.SE
- **摘要:** 仓库探索是编码 agent 管线里独立且昂贵的阶段。用 IssueLoc-Bench 评估 5 个探索模型（同一只读交互界面，499 个 SWE-bench Verified 派生任务 + 500 个来自 153 仓库任务）：最高质量探索器领先，但**显著更便宜的档位浮现**——低成本的保留参考 Hit@3 的 78-94%、F1 的 73-92%，同时平均 agent 时间减 41-88%、token 减 84-95%。偏好档位取决于下游如何消费定位结果（排名/覆盖 vs F1/精确匹配）。结论：仓库探索应作为模块化编码 agent 里可独立测量、可独立预算的阶段。
- **关联度:** ★★★★ "探索阶段可下放到低成本模型"——与 k 的模型路由/成本优化直接相关（哪层用便宜模型）

---

## 八、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2608.29096](https://arxiv.org/abs/2608.29096v1) | Autonomous AI Coding Agent using MCTS and Gemini | MCTS 当搜索 + Self-Critic 评估器，复杂逻辑 prompt 92% 成功率（自报口径） |
| 2 | [2608.29310](https://arxiv.org/abs/2608.29310v1) | Super Library Agent | 顺序生成 N 个相关应用同时维护共享"超级库"，候选引导抽取降冗余、防结构侵蚀 |
| 3 | [2608.28972](https://arxiv.org/abs/2608.28972v1) | Legacy System Modernization with Coding Agents | 工业案例：Claude Code 迁移 VB6→C# .NET 10，12 特性平均等价 70%，低复杂度 92%/高复杂度 47%、token 差 6x |
| 4 | [2608.29204](https://arxiv.org/abs/2608.29204v1) | AgentLogs | GitHub Copilot 云 agent 黑盒数据集：307k 任务/549k 会话/64M 逐步日志条目 |
| 5 | [2608.29387](https://arxiv.org/abs/2608.29387v1) | EvoGenUI-Bench | 多轮生成式 UI 助手：150 任务 5 轮，最强也仅 37.3% 完成整轮，工具接地任务 APR 52.4% |
| 6 | [2608.29070](https://arxiv.org/abs/2608.29070v1) | Selective Disclosure of Hidden Directives | ICG：模型 CoT 更可能泄露恶意隐藏指令而非良性；steering 向量可诱导/抑制隐藏 |
| 7 | [2608.29460](https://arxiv.org/abs/2608.29460v1) | Escalation channels redirect reward hacking | 升级/上报通道把 reward hacking 从 23.6% 压到 5.3%，还把缺陷检出 +10.1pp——"把能力导向披露而非利用" |
| 8 | [2608.29464](https://arxiv.org/abs/2608.29464v1) | CoT Faithfulness Varies with Preference Cues | FACE-Eval（5100 样本）：工具返回/隐式线索比用户消息/显式线索更少被 CoT 言说，监控可靠性存疑 |
| 9 | [2608.29483](https://arxiv.org/abs/2608.29483v1) | GeoAgent | VLM 地理定位的具身导航基准：国家/大洲级行、区域级差，存在发达/发展中地区偏差 |
| 10 | [2608.29621](https://arxiv.org/abs/2608.29621v1) | CineForge | 自进化视频生产 agent：CPPE 跨故事策略进化，CineScope 4.024→4.380、review LLM 调用减 37% |
| 11 | [2608.29357](https://arxiv.org/abs/2608.29357v1) | LiteSearch-VL | 小多模态搜索 agent：轨迹蒸馏到 2B/4B 转移"行为契约"，瓶颈在答案验证而非检索深度 |
| 12 | [2608.29058](https://arxiv.org/abs/2608.29058v1) | RouteSparse | 输入条件化稀疏注意力路由：128K prompt 下 6.5x prefill 提速、RULER 只掉 0.2（vs 固定路由掉 1.6） |
| 13 | [2608.29252](https://arxiv.org/abs/2608.29252v1) | Dynamic Important Example Mining (DIEM) | 梯度对齐重要性估计 + 约束 batch 重加权，让 RFT 数据利用随训练自适应 |
| 14 | [2608.29575](https://arxiv.org/abs/2608.29575v1) | SemTrace | 源接地语义水印：从受保护文档构造二元事实签名，检测生成文本是否受其影响，不偏 token 概率 |
| 15 | [2608.29978](https://arxiv.org/abs/2608.29978v1) | Evolutionary Soups | 进化算法训练 MoE gating，推理时按隐藏态动态合并专家，多目标对齐 |
| 16 | [2608.30035](https://arxiv.org/abs/2608.30035v1) | Multi-Solver Disagreement Rewards | 用异构多求解器分歧做 Challenger 奖励，破单模型采样不确定性奖励坍缩 |
| 17 | [2608.29897](https://arxiv.org/abs/2608.29897v1) | When History Is Multimodal | 重思长程 agent 上下文管理：视觉渲染作为记忆载体的公平受控对比 |

---

## 今日要点（主题信号）

1. **Agent 记忆进入"溯源/证据优先"时代**：Agent Zero Memory（citation lock + 三并行记忆 + 95.6% LongMemEval SOTA）、SearchWiki（分层 wiki + RL 导航）、同周齐发的 Zero-Mem/Eywa/TierMem/ECHO/MAP-Graph——provenance-first 成为主流记忆范式；Selective Forgetting 反直觉证明"选择性能遗忘"才是图谱记忆的价值。与 k 的证据分级 A-D / TBHC 契约直接同频。
2. **Wiki 形态记忆跨论文共振**：SearchWiki（9B 超同规模）承接上周 WikiSkill，openwiki / pi-codebase-wiki / llm_wiki 等工程同步铺开——"把语料编成 wiki 再学会导航"正在成为优于扁平 RAG 的答案。
3. **Agent 评估转向"七维工程能力 + 过程可审计"**：APIFlow-Bench（Postman，467 任务/7 轴/4.4 万未脱敏轨迹，长链 93%→61%）、Last Step Matters（早期不确定性无法预测失败，"最后一步置信度决定重启"）、FORESIGHT-9（反事实世界线 + 过程遥测抓内部崩溃）、Ideation Arena（人评擂台，LLM judge 仍不可靠）。
4. **RLVR 的代价被精确定位**：Locked at the Entrance——解空间收缩集中在"入口"（浅层插值可恢复 37% 覆盖且不损 pass@1）；batch 缩放给出"吞吐增益 > 样本惩罚"决策规则。
5. **多智能体安全风险集中在"边界元数据"与"checkpoint/rollback"**：Facts Without Rules（handoff 摘要丢边界元数据→隐私泄漏，显式受众 allowlist 近乎消除）、Safe to Resume（C/R 五类失败模式可打 Hermes/Cline/LangGraph 双重支付）、SkillGuard（污染后能力约束，零额外模型调用）。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| APIFlow-Bench 2608.29128 | web_search（Postman 官方博客 + GitHub + LinkedIn） | ✅ Postman Research 出品；github.com/postmanlabs/APIFlow-Bench；56,037 份未脱敏轨迹、24 模型 |
| Agent Zero Memory 2608.29606 | web_search（arXiv 同主题集群） | ✅ arXiv API 收录；Zero-Mem/Eywa/TierMem/ECHO/MAP-Graph 同周齐发，佐证 provenance 记忆成主线 |
| SearchWiki 2608.29953 | web_search（wiki 检索范式） | ✅ arXiv API 收录；wiki 导航范式在 openwiki / pi-codebase-wiki / llm_wiki 同步落地 |
| 其余 28 篇 | arXiv API 收录 + 抽取完整元数据 | ✅ API 收录即存在性证据（2026-08-07 既定原则） |

## 可落地行动项

- 🔴 **记忆层"溯源优先"升级评估**：Agent Zero Memory 的 citation-lock + provenance 三并行记忆、SearchWiki 的分层 wiki 导航，与 k 的证据分级 A-D / TBHC 契约是同一思想的不同实现——精读 Agent Zero Memory 全文，评估把 citation-lock 纪律写进 knowledge 吸收流程
- 🟡 **把"选择性能遗忘"纳入记忆清理**：Selective Forgetting 证明遗忘几乎无损且省 9.5% 存储——k 的记忆清理/结晶流程可引入 recency/访问频次/度中心性/age 加权打分
- 🟡 **Agent 评估方法论落地**：APIFlow-Bench 的"分解能力轴 + 确定性验证器而非 LLM judge"、Last Step Matters 的"最后一步置信度决定重启"、LLM Judges as Raters 的测量学警告——纳入 k 对多 agent 协作/接单交付的验收门
- 🟢 **待深读**：Agent Zero Memory、SearchWiki、APIFlow-Bench、Facts Without Rules、SkillGuard → 进 core-contributions 候选

---

*本速览由 cron 自动生成：08-29→08-30 两日窗口全量收集（480 篇）→ 关键词过滤（~304 篇）→ 人工精选（31 主条目 + 17 简评）→ 关键论文交叉验证。数据源 export.arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
