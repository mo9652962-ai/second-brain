---
aliases:
  - arxiv-2026-08-07-agent-llm
  - arxiv-agent-llm-2026-08-07
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-07
updated: 2026-08-07
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-07

> **检索时间**: 2026-08-07 07:13 GMT+8
> **检索范围**: cs.AI / cs.CL / cs.LG / cs.MA / cs.SE / cs.RO / cs.HC / cs.CV / cs.CR / cs.DB,提交日期 08-05 ~ 08-07
> **原始检索**: 7 组查询(Agent 框架/LLM Agent/多 Agent/工具调用/代码 Agent/Agent 记忆/Agent 安全),去重后 **32 篇**,精选 **15 篇**与 AI Agent / LLM 强相关
> **数据源**: [export.arxiv.org](https://export.arxiv.org) + web_search 交叉验证(arXiv 页/HF papers/官方 X 帖)

---

## 一、Agent 运行时与长程推理

### 1. Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning
- **ID:** [2608.05144v1](https://arxiv.org/abs/2608.05144v1) | [📄 PDF](https://arxiv.org/pdf/2608.05144v1)
- **作者:** Boxiu Li, Zimo Wen, Yijia Fan, ... Xuanhe Zhou, Zhijie Deng(26 人)
- **分类:** cs.AI
- **摘要:** 长程推理需要能在证据支持时坚持、在测量暴露失败/隐藏约束时转向的 agentic runtime。Argus 是持久、自进化的运行时:Manager/Planner/Engineer/Reviewer 在持久项目状态上执行有界任务,模型权重固定,自我进化发生在运行时状态与控制策略层面。在 7 个 GPT-5.5 基准竞技场,SWE-Bench Pro 约 78%(Direct Copilot 59%),验证门控自进化后成熟任务用 21% 更少的 solve-input token;AARRI-Bench 76.8%;优化过的 RWKV6 kernel 已合入上游。
- **关联度:** ★★★★★ 与 Hermes 的自进化 harness 理念直接同构(角色分工/验证门控/拒绝路线记录),Argus 的「固定权重+持久状态自进化」可作为 harness 演进路线图参考

### 2. Chained Recursive Language Models for Multi-Iteration Reasoning
- **ID:** [2608.05124v1](https://arxiv.org/abs/2608.05124v1) | [📄 PDF](https://arxiv.org/pdf/2608.05124v1)
- **作者:** Purbesh Mitra, Sennur Ulukus
- **分类:** cs.CL, cs.AI
- **摘要:** 单条推理轨迹要同时做探索上下文、存中间状态、验证证据、产出答案,早期错误会一路传播。Chained RLM 提出推理时架构:同一模型被反复调用为**全新推理根**,每个根不继承完整对话历史,只接收紧凑纯文本摘要 + 黑板 + 前辈根写下的持久工件;后续根可检查、修正、扩展中间工件。把长任务切成部分任务管理上下文,而非一次大推理。
- **关联度:** ★★★★ 上下文管理型 harness 设计(黑板/工件工作区);与 Hermes 的会话外记忆、任务分段模式理念相通

### 3. OctoLong: Mid-Training On Cross-Repository Code Contexts Enhances Long-Context Modeling
- **ID:** [2608.05141v1](https://arxiv.org/abs/2608.05141v1) | [📄 PDF](https://arxiv.org/pdf/2608.05141v1)
- **作者:** Indraneil Paul, Falko Helm, Goran Glavaš, Iryna Gurevych(UKP 实验室)
- **分类:** cs.AI, cs.LG, cs.SE
- **摘要:** 长上下文语料被书籍/论文/单仓库代码主导,缺乏跨文件长程依赖。OctoLong 用 AST 解析器 + language server + 包管理器做递归代码引用检索,构造百万级 token 的依赖丰富代码上下文;600M~14B 基座模型在 ~50B token 混合语料上中间训练。仅把 12% 传统扩展语料换成 OctoLong 数据,就在长程检索、长期状态跟踪、仓库级代码理解与下游 agentic 任务上显著提升。
- **关联度:** ★★★★ 代码 Agent 的长上下文基建;与 sora 的代码库理解/graphify 场景直接相关

---

## 二、Agent 训练与评估

### 4. Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horizon Reasoning
- **ID:** [2608.05139v1](https://arxiv.org/abs/2608.05139v1) | [📄 PDF](https://arxiv.org/pdf/2608.05139v1)
- **作者:** Yinghui He, Ling Yang, Jiarui Liu, ... Mengdi Wang, Sanjeev Arora(Gen-Verse)
- **分类:** cs.CL, cs.LG
- **摘要:** 长程推理要求模型在推理链内切换技能(先数学推导、再调度规划),但现有基准只测单技能。本文提出 **Skill Entropy**(衡量技能切换难度)、Skill²-Bench(558 技能 × 9 域)、Skill-Entropy RL(每步同时预测答案与所用技能,reward 对齐模型预测技能序列与金标技能序列)。Qwen3-4B: 34.4%→68.4%,Qwen3-1.7B: 14.6%→40.1%;同一信号可迁移到 OpenR1-Math 等现成数据。
- **关联度:** ★★★★★ 「技能获取给能力,技能编排才给可靠长程智能」——与 sora 技能库(skills/)的组织思想同构;skill-switching 度量可评估 Hermes 多技能编排质量。代码:github.com/Gen-Verse/Skill-Entropy-RL

### 5. ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment
- **ID:** [2608.05102v1](https://arxiv.org/abs/2608.05102v1) | [📄 PDF](https://arxiv.org/pdf/2608.05102v1)
- **作者:** Yijun Lu, Rui Ye, Jiajun Wang, Yuwen Du, Tian Jin, Songhua Liu, Siheng Chen
- **分类:** cs.AI
- **摘要:** 长程搜索 Agent 的训练把所有步骤一视同仁,无法区分有用/错误/冗余动作。ABC(Answer-Backtracked Credit Assignment)把稀疏轨迹级结果转为密集步骤级监督:先从验证过的答案回溯恢复中间线索,再按线索对齐给每步打分,用于 SFT 重加权与 GRPO 奖励。Qwen3.5-4B 仅 8.5k 样本 → BrowseComp 37.3%(加上下文管理 55.3%),追平约 30B 大模型。模型已发布 PolarSeeker/ABSeeker-4B-RL。
- **关联度:** ★★★★★ 搜索/研究 Agent 训练的 credit assignment 新方法;对 Hermes 的 web_search 多步研究流程的「步骤级质量评估」有直接借鉴

### 6. Reasoning Core: Designing Broad Procedural Data for Completion-Supervised Reasoning Training
- **ID:** [2608.05148v1](https://arxiv.org/abs/2608.05148v1) | [📄 PDF](https://arxiv.org/pdf/2608.05148v1)
- **作者:** Damien Sileo, Valentin Lacombe, Dimitri Kachler
- **分类:** cs.CL
- **摘要:** 程序化生成器能大规模产出可验证推理题,但很少作为 completion-supervised 微调数据被研究。Reasoning Core 收集 50 个生成器(数学/逻辑/规划/状态跟踪/形式语言/博弈/因果/代码),带语义打分器、难度控制与任务评估器。3B 对比中在 DROP/LogiQA/ARC-Challenge 上超过 Reasoning Gym、SynLogic 等替代集合;关键发现:**语义有效性≠训练有用性**,紧凑目标与校准难度才是设计要素。
- **关联度:** ★★★★ 推理训练数据工程的方法论对照;与 sora 的题库工程(刷题机 40 天去重校验)理念相通——数据质量审计是共同主线

### 7. Reward Structure Shapes the Interaction Between Episodic Exploration and Neural Memory in RL
- **ID:** [2608.05111v1](https://arxiv.org/abs/2608.05111v1) | [📄 PDF](https://arxiv.org/pdf/2608.05111v1)
- **作者:** Jai Malegaonkar, Rohan Patil, Henrik I. Christensen
- **分类:** cs.LG
- **摘要:** 部分可观测 RL 中,探索奖励与记忆架构通常被孤立评估。本文做交叉控制实验:同一奖励信号在三种环境中产生三种截然不同的交互模式(放大架构差异/拉平到天花板/完全无效);提出 observation-anchored reward machines 把「奖励稀疏」拆成结构性稀疏与潜在性稀疏两个正交维度。结论:**探索与记忆是互补品而非替代品**——奖励激励暴露,只有记忆把暴露转化为回报。
- **关联度:** ★★★ 记忆×探索的受控实验方法论;对 Agent 记忆系统设计(记忆不是越大越好,取决于奖励结构)有启发

---

## 三、Agent 记忆与安全

### 8. HiGram: Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite
- **ID:** [2608.05095v1](https://arxiv.org/abs/2608.05095v1) | [📄 PDF](https://arxiv.org/pdf/2608.05095v1)
- **作者:** Xiawei Yue, Boran Wang, Xiaoqing Zhang, Shuxin Zheng, Ziwei Zhang
- **分类:** cs.AI
- **摘要:** 现有图记忆把所有记忆存进扁平图,历史累积引入无关上下文,且单元级重写需要反复覆盖相关变更。HiGram 用**层级图记忆**(上层抽象节点 + MemoryUnit 细粒度事实)粗到细组织;MicroGraph 路径级定位找出受查询/更新影响的证据路径;协调重写机制联合修订单元内状态与单元间依赖。LoCoMo/MemConflict 上显著提升答案质量与 token 效率,冲突场景下证据选择更准。
- **关联度:** ★★★★★ 与 Second Brain/Obsidian 图谱+MOC 分层思想同构(粗到细组织=知识域 MOC→笔记);「定位→重写」范式可评估 Hermes 记忆更新的效率

### 9. Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming
- **ID:** [2608.05108v1](https://arxiv.org/abs/2608.05108v1) | [📄 PDF](https://arxiv.org/pdf/2608.05108v1)
- **作者:** Yanting Wang, Chenlong Yin, Runpeng Geng, Jinyuan Jia
- **分类:** cs.CR
- **摘要:** 现有提示注入红队主要靠 RL,攻击者模型对新目标 LLM 泛化差。PIMiner 是 agentic 红队系统:训练时在(数据集, 目标模型)序列上构建**策略库**,测试时策略库零训练直接迁移到未见过的目标 LLM,每个测试样本只需约 10 次查询。IPIArena 上对 Gemini-2.5-Pro 达 76.2% ASR、GPT-5.1 61.9%、Claude-Sonnet-4.5 42.9%;AgentDojo 上 86.7%/53.3%/40.0%。
- **关联度:** ★★★★★ Agent 安全前沿;策略库迁移=「攻击技能沉淀为可复用资产」,与 sora 技能库的组织逻辑形成镜像,可直接用于评估 Hermes 自身的注入防护

---

## 四、多 Agent 与人机协同

### 10. CoPlan: A Trustworthy Co-Intelligence Interface for Care Planning through Role-Based Contestable Argument Graphs
- **ID:** [2608.05107v1](https://arxiv.org/abs/2608.05107v1) | [📄 PDF](https://arxiv.org/pdf/2608.05107v1)
- **作者:** Hung Truong Thanh Nguyen, Hélène Fournier, Piper Jackson, ... Hung Cao
- **分类:** cs.AI, cs.MA, cs.SE
- **摘要:** 多数 AI 系统把建议当作固定输出,用户无法检查/质疑/修订。CoPlan 是「共同智能+可争议性」的护理规划界面:多 Agent 工作流中,专门 Agent 生成候选干预与支持/反驳论证,人类护理规划者可接受/拒绝/修改/添加论证后再生成最终计划。角色化争议参数图让推荐保持可检查、可修订、可举证,保留人类能动性与临床责任。
- **关联度:** ★★★ 可争议式人机协同范式;与 Hermes 的 human-in-the-loop 审批设计(外部动作需确认)理念一致

---

## 五、LLM 应用与工具

### 11. Spoken Function Calling: A New Perspective on Spoken Language Understanding for Large Audio Language Models
- **ID:** [2608.05126v1](https://arxiv.org/abs/2608.05126v1) | [📄 PDF](https://arxiv.org/pdf/2608.05126v1)
- **作者:** Yuezhang Peng, Yuxin Liu, Changfeng Gao, Zhifu Gao, Xiangang Li, Xie Chen
- **分类:** cs.CL, cs.MM
- **摘要:** 传统口语理解(SLU)闭集任务靠领域内微调,开放域上下文学习能力弱。本文提出**口语函数调用(SFC)**:用结构化规则定义做语义理解,把传统 SLU 数据集扩展成口语函数套件,多 Agent 系统合成 SFC-Bench,再对 LLM/LALM 评估与后训练增强,语义抽取准确率显著超过传统 SLU。
- **关联度:** ★★★ 语音 Agent 的 function calling 标准化;与 sora 语音输入场景(TTS/语音助手)可对接

### 12. Characterizing Visual Accessibility Issues in AI Developer Tools: An Empirical Study
- **ID:** [2608.05116v1](https://arxiv.org/abs/2608.05116v1) | [📄 PDF](https://arxiv.org/pdf/2608.05116v1)
- **作者:** Sabrina Haque, Christoph Csallner
- **分类:** cs.SE, cs.HC
- **摘要:** AI 辅助开发工具(聊天面板、终端 Agent、diff、流式状态)可能对盲人/低视力/色觉缺陷开发者造成视觉无障碍障碍。从 5 个工具生态(Copilot、Cursor、Claude Code、Codex、OpenCode)2,652 个候选里三模型集成筛出 600 个一致确认的无障碍报告:三类问题——屏幕阅读器/辅助技术障碍、视觉呈现/对比度问题、AI 界面可读性/缩放/控件限制。
- **关联度:** ★★★ 编码 Agent 生态的实证质量研究;对 Hermes 桌面端 UI 的可达性设计有检查清单价值

### 13. Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding Generation for Modern Greek across Specialist Domains
- **ID:** [2608.05138v1](https://arxiv.org/abs/2608.05138v1) | [📄 PDF](https://arxiv.org/pdf/2608.05138v1)
- **作者:** Ayoub Kirouane, Christos Petrocheilos
- **分类:** eess.AS, cs.AI, cs.CL
- **摘要:** 现代希腊语缺失于 Nemotron 检索模型与主流多语基准。端到端适配:语料挖掘、合成监督、检索模型训练、reranker 适配、reader 微调,并发布首个希腊语 RAG 基准 HERA。关键实证:BM25 无参数基线竟超过多个开箱即用的多语稠密检索;65,773 对希腊语微调后 Nemotron 1B embedder nDCG@10 从 0.362→0.835;LoRA 微调 30B-A3B MoE reader 使答案正确率 29.4%→66.9%。
- **关联度:** ★★★ RAG 栈适配完整实战(含「稠密检索未必赢 BM25」的反直觉发现);对 Hermes 搜索后端多语言/垂直领域配置有参考

### 14. Same Formulas, Different Semantics: Do Language Models Follow Modal Logic Specifications?
- **ID:** [2608.05097v1](https://arxiv.org/abs/2608.05097v1) | [📄 PDF](https://arxiv.org/pdf/2608.05097v1)
- **作者:** Rémi Andrieu, Damien Sileo
- **分类:** cs.CL
- **摘要:** 必然/可能性推理依赖世界可达性与对象存在性假设,同一推理在不同模态系统下结论相反。构造前提与猜想相同但框架条件不同的配对问题,自动推理验证相反标签。5 个近期模型中 4 个直接提示下低于「只看条件」基线;但开启 reasoning 模式后 **DeepSeek V4 Flash 从 4.4%→88.1%**(提示词不变)。遵循规定语义既依赖模型也强烈依赖推理模式。
- **关联度:** ★★★ 推理模式(reasoning_effort/推理开关)如何决定逻辑能力——正好印证 sora 全程 reasoning_effort=high 的配置直觉;且本论文直接测评了 sora 在用的 DeepSeek V4 Flash

### 15. DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery
- **ID:** [2608.05120v1](https://arxiv.org/abs/2608.05120v1) | [📄 PDF](https://arxiv.org/pdf/2608.05120v1)
- **作者:** Roberto Aliaga Medina, Paulina Quintanilla, Antonio del Rio Chanona
- **分类:** cs.LG, cs.CE, cs.SC
- **摘要:** 化学工程动力学模型发现里,符号回归常无领域知识、探索物化不合理模型。LLM 注入领域专长的迭代式 SR 框架:LLM 每轮做两件事——(1) 对最优候选做定性物化批评;(2) 基于 SR 生成模型+内嵌化学知识提出新候选表达式。相比 SOTA SR 框架,迭代次数减少 41.7~79.3%,超过一半运行中 LLM 直接提出正确模型结构。
- **关联度:** ★★★ AI4Science 的 LLM-in-the-loop 范式(批评+提案双角色);「LLM 批评 SR 候选」可类比 Hermes 的 code review/方法论审计流程

---

## 📌 今日要点

- **主题主线**: Agent 运行时与训练方法双热点 —— Argus 固定权重自进化运行时、Chained RLM 黑板式上下文管理代表 harness 演进;Skill Entropy 与 ABSeeker 代表训练侧「技能编排」「步骤级信用分配」新方法
- **记忆系统**: HiGram 层级图记忆与昨日 PAST-Bench 递归自改进形成连续研究线,说明 Agent 记忆正成为系统级工程问题
- **安全**: PIMiner「策略库迁移」提示注入红队,攻击资产可复用的思路值得跟踪
- **与 sora 直接相关**: Argus(Harness 自进化)、Skill Entropy(技能库组织)、ABSeeker(研究流程步骤评估)、HiGram(Obsidian 图谱分层)、模态逻辑评测(DeepSeek V4 Flash 推理模式实证)
- **理论前沿**: 奖励结构×记忆的互补性结论、RL 中探索与记忆的统一视角值得长期跟踪

---

## 🔗 关联

- 上一份核心贡献精选: [[knowledge/arXiv/arxiv-2026-08-05-core-contributions|arXiv 核心贡献 08-05]]
- 上期速览: [[knowledge/arXiv/arxiv-2026-08-06-agent-llm|arXiv 今日速览 08-06]]
- 总索引: [[knowledge/arXiv/arxiv-digest|arXiv Digest]]
- 回到: [[HOME]]
