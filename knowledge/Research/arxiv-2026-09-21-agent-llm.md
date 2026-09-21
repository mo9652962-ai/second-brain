---
aliases:
  - arxiv-2026-09-21-agent-llm
  - arxiv-agent-llm-2026-09-21
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-21
updated: 2026-09-21
status: adopted
source: arxiv.org list pages + abs pages（2026-09-21 窗口正常速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-21

> **正常速览**：2026-09-21（周一）arXiv list 页出现**新日期分组 2026-09-21（460 篇）**——周末（09-19/09-20）提交并入周一分组属正常现象；与 covered_ids（777）比对 **0 重叠**，为全新窗口，写正常速览。
> **检索时间**: 2026-09-21 GMT+8（cron）
> **流程**: 09-21 分组 460 篇 → 标题粗筛（56 候选）→ 人工剔除领域应用（医疗/交通/分子/手术/无人机/桥梁/芯片布局等）→ 逐篇抓 abs 页精选 **16 主条目 + 7 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、Agent 训练与 RL 环境（2 篇）

### 1. CodeMidas: Scaling Agentic Coding RL Environments from Code Itself

- **ID:** [2609.22068v1](https://arxiv.org/abs/2609.22068v1) | [📄 PDF](https://arxiv.org/pdf/2609.22068v1)
- **作者:** Bowen Ye, Lei Li, Shicheng Li, Zihao Yue, Linghao Zhang, Hanglong Lv, Yuanxin Liu, Wenhan Ma, Hao Tian, Rang Li, Jinhao Dong, Yikai Zhao, Xiangwei Deng, Hailin Zhang, Liang Zhao, Qi Liu, Lingpeng Kong, Tong Yang, Fuli Luo
- **分类:** cs.AI
- **摘要:** 训练编码 agent 的 RL 需要多样任务 + 可靠验证器；开源代码库是丰富来源，但现有方法依赖 issue/commit 等开发痕迹，可提取任务范围受限。CodeMidas：以源码为**唯一任务输入**，把代码库中已实现功能转成可执行 RL 环境的 agentic 流水线——为环境构建每个阶段分配 agentic 计算：agent 探索已实现功能→形成行为规格→构建测试→验证环境。解决「环境构建本身是瓶颈」的规模化问题。
- **关联度:** ★★★★★ 编码 agent RL 训练的环境基建——k 的编码委派（Codex CLI/dsh）与墨题/刷题机测试基建的「从代码自身生成可执行验证环境」思路；「agent 构建 agent 的训练环境」与 skill-pipeline/六段质检门同构

### 2. Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models

- **ID:** [2609.20846v1](https://arxiv.org/abs/2609.20846v1) | [📄 PDF](https://arxiv.org/pdf/2609.20846v1)
- **作者:** Polina Tsvilodub, Max Höth, Michael Franke, Björn Deiseroth, Carina Kauf
- **分类:** cs.CL, cs.LG
- **摘要:** 大推理模型（LRM）擅长答对问题，却常不会「弃权」：人类对不可答任务的推理努力有上界，LRM 反而在不可答提示上生成更长 CoT、浪费算力。受资源理性认知启发，提出新型 GRPO 奖励：奖励高效推理（含弃权），让模型学会「不答」或简短答——与人类行为对齐，避免在欠指定任务上过度推理。
- **关联度:** ★★★★ 「知道何时不答」——k 的产物断言/「不臆造、标不确定」原则的模型侧版本；对 k 的评测与交付（不确定就标注而非硬凑）是行为层参考

---

## 二、Agent 记忆与技能进化（4 篇）

### 3. Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design

- **ID:** [2609.22086v1](https://arxiv.org/abs/2609.22086v1) | [📄 PDF](https://arxiv.org/pdf/2609.22086v1)
- **作者:** Hongyang Du, Lan Yan, Christian Flores, Asim Kadav
- **分类:** cs.AI, cs.CV
- **摘要:** 专业平面设计是长程 agentic 任务：结构化可编辑产物由大量相互依赖动作涌现，且无可靠程序化 oracle。Designer-RSI：冻结前沿模型操作专业设计软件（230+ 工具）+ 外部**程序记忆**（自然语言技能库）从经验持续积累/精炼可复用设计流程——记忆通过获取重复未覆盖子任务的流程而**变宽**、通过对照自身成功/失败执行修订既有流程而**变深**；匹配回放门只放行能修复失败的改动。从用户流量学习。
- **关联度:** ★★★★★ 冻结模型 + 外部程序记忆 RSI——与 k 的技能体系（SOUL.md/skill_manage 即外部程序记忆）完全同构；「记忆变宽/变深 + 回放门只放行修复失败的改动」正是 k 的 skill-evolution 门禁逻辑；「从用户流量学习」对 k 的闲鱼/PPT 交付复盘是流程参考

### 4. MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems

- **ID:** [2609.21533v1](https://arxiv.org/abs/2609.21533v1) | [📄 PDF](https://arxiv.org/pdf/2609.21533v1)
- **作者:** Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li
- **分类:** cs.LG
- **摘要:** LLM 多智能体系统产生协作轨迹（规划/验证/修复）。复用这些流程需保留动作前提与后续 agent 所需输出；实证：把依赖分组为**功能记忆单元**提升保留，连接单元提升联合检索；最佳组合随格式（指令 vs 清单）而变。MACE：从每个组合-格式配对的结果更新选择，自适应记忆图让记忆与 agent 共同进化。
- **关联度:** ★★★★★ 记忆-代理共进化——k 的 multi-agent-research（k/WorkBuddy/dsh/Gemini 分工）的记忆复用参考；「功能单元分组 + 连接 + 格式感知」对 k 的上下文/技能记忆设计（skill 触发词 vs 清单）是结构参考

### 5. An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency

- **ID:** [2609.22043v1](https://arxiv.org/abs/2609.22043v1) | [📄 PDF](https://arxiv.org/pdf/2609.22043v1)
- **作者:** Yiming Zhang, Jinghong Zhang, Haoran Zhao, Yiren Ma, Chunlei Zhao
- **分类:** cs.CL
- **摘要:** 记忆系统偏重高效检索，忽视「检索到的记忆是否可信」。记忆库含冲突立场时，标准 RAG 盲目注入记忆并放大幻觉（冲突记忆下 RAG 幻觉率显著高于无记忆基线）。受前额叶记忆信号机制启发，提出 Memory Decision Layer（MDL）：检索与生成之间的**零参数记忆决策控制器**，解耦置信度与一致性，三信号互补决定信任哪些记忆。
- **关联度:** ★★★★★ 「记忆信任决策层」——k 的 RAG 管道（墨题 DashScope embedding、知识库检索）缺的正是「检索结果可信度门」；三信号互补对 k 的多源验证（跨源盲评）是控制器级思路

### 6. GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills

- **ID:** [2609.21749v1](https://arxiv.org/abs/2609.21749v1) | [📄 PDF](https://arxiv.org/pdf/2609.21749v1)
- **作者:** Rui Sun, Zhi Zheng, Zhenkun Wang, Zhichao Lu
- **分类:** cs.LG
- **摘要:** 技能提升 LLM agent 表现，技能优化进一步迭代精炼；但现有方法把技能表示为无结构自然语言指令：缺显式流程级指导、冗余多、无约束搜索空间大导致优化低效。GraphSkillEvo：把技能表示为**图结构自然语言**（节点=子技能/动作，边=依赖/流程关系），在图上做进化优化——结构化表示缩小搜索空间、显式流程关系可执行。
- **关联度:** ★★★★★ 技能图结构化进化——k 的 skill 体系（SKILL.md 是扁平自然语言技能）的进化版蓝图：「技能图 + 进化优化」对 k 的 skill-evolution/skill-pipeline 是结构升级方向

---

## 三、Agent 评估与能力边界（4 篇）

### 7. When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success

- **ID:** [2609.21187v1](https://arxiv.org/abs/2609.21187v1) | [📄 PDF](https://arxiv.org/pdf/2609.21187v1)
- **作者:** Md Tahmid Rahman Laskar, Xue-Yong Fu, Gundeep Singh, Karol Chang, Kevin Sanders, Shi Zong, Tania Habib, Julien Bouvier Tremblay, Shayna Gardiner, Harsh Saini, Matthias Lee, Elena Khasanova, Quinten McNamara, Shashi Bhushan TN
- **分类:** cs.CL
- **摘要:** agent 模型常被「一次决策一步」地评估：基于 gold 交互历史预测下一步，对参考答案打分。本文研究此协议下的改进是否预示自主工作流执行改进：pre-SFT vs SFT 的 Qwen3 4B/14B 与 Gemma3 4B/12B 在多轮客服工作流上——SFT 一致提升 next-turn 成功率（gold-history 评估），但这些改进**不迁移到自主执行**；工具特定失败是主要瓶颈。
- **关联度:** ★★★★★ 「单步指标 ≠ 工作流成功」——k 的验证门禁（verify_digest_note/产物断言）的评估层级警告：「分步对」不代表「闭环成」；对 k 的多步骤 cron/交付流程要测端到端而非单步

### 8. Efficient Benchmarking in Production: A Study of an Evolving LLM Agent

- **ID:** [2609.21267v1](https://arxiv.org/abs/2609.21267v1) | [📄 PDF](https://arxiv.org/pdf/2609.21267v1)
- **作者:** Yining She, Lei Lin
- **分类:** cs.AI, cs.SE
- **摘要:** 生产 LLM agent 随演化被反复评估，但全量基准重跑昂贵。针对月活数万的生产分析 agent 首次报告部署经验：用 574 次历史运行按时间切分校准/留出，比较随机采样、历史缓存、固定代表子集、IRT 自适应测试——**多维 2PL 自适应测试**保真度最佳：只跑 200 题（全量 38.5%）MAE 仅 1.03pp；最终部署混合方案。
- **关联度:** ★★★★★ 生产级重复评测降本——k 的 apikey 探活/健康巡检/cron 门禁的评估成本问题同题；IRT 自适应「少跑题保持保真」对 k 的每日速览/周报抽样策略是统计参考

### 9. LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers

- **ID:** [2609.21492v1](https://arxiv.org/abs/2609.21492v1) | [📄 PDF](https://arxiv.org/pdf/2609.21492v1)
- **作者:** Jingyu Hu, Shu Yang, Weiru Liu, Di Wang
- **分类:** cs.AI, cs.LO, cs.SC
- **摘要:** CoT 提升 LLM 表现，但现有优化多靠结果反馈，中间推理步骤逻辑有效性未验证——模型可能用逻辑有缺陷的中间链得到正确终答。LogicTrack：神经符号框架，自动把每步推理形式化为符号表示并用自动定理证明器验证；引入 Solver-Based Backtracking Reward (SBR) 逐步评分机制量化逻辑有效性。
- **关联度:** ★★★★ 推理轨迹的符号审计——与 k 的「验证链」同题：产物断言/门禁不只查结果也要查过程；SBR 逐步奖励对 k 的 agent 轨迹复盘是形式化工具

### 10. What Stops a Small Language Model From Driving a Database Agent

- **ID:** [2609.21341v1](https://arxiv.org/abs/2609.21341v1) | [📄 PDF](https://arxiv.org/pdf/2609.21341v1)
- **作者:** Cevheri Bozoglan, Yusuf Gundogdu, Abdullah Kaya, Koray Sirin
- **分类:** cs.SE, cs.DB
- **摘要:** 小开源模型被认为缺推理能力而无法做 agentic 数据库工作——本文在生产系统实测：11 天用 39 个本地开源模型 + 1 个托管控制组驱动开源 SQL 客户端 agent 模式，覆盖 6 类任务面：8,199 次运行、110,711 个账本事件、14,008 次被拒工具调用。2,100 次模型归因的 agent 模式损失中 1,590（75.7%）来自至少调用过一次工具的运行，该多数在重采样中稳定成立——瓶颈在工具调用环节而非推理本身。
- **关联度:** ★★★★ 小模型 agent 失败归因实证——k 的本地推理（RTX4060 8GB）选型参考：「工具调用环节」而非「推理能力」才是小模型瓶颈；对 k 的本地 agent 部署（dsh/Codex 本地）是成本-能力权衡实证

---

## 四、LLM 安全与隐私（3 篇）

### 11. HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference

- **ID:** [2609.21484v1](https://arxiv.org/abs/2609.21484v1) | [📄 PDF](https://arxiv.org/pdf/2609.21484v1)
- **作者:** Byeongseo Min, Yongwoo Lee, Young-Sik Kim, Yongjune Kim
- **分类:** cs.CR, cs.AI
- **摘要:** 同态加密（HE）实现隐私保护 LLM 推理：客户端提交加密输入，服务器在密文上评估模型。但暴露关键漏洞：HE-LLM 推理易受恶意客户端提交对抗提示（jailbreak）攻击——保护良性客户端的机密性同时使服务器无法检查输入/输出，对抗尝试难检测。HE-Guardrail：加密域护栏检测/缓解 jailbreak 攻击。
- **关联度:** ★★★★ 加密推理的安全盲区——k 的隐私边界（隐私红线/DPAPI 密钥管理）的攻防视角：「加密保护隐私」引入「无法审计内容」新攻击面；对 k 的 apikey-manager/凭证保护是威胁建模参考

### 12. CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents

- **ID:** [2609.21686v1](https://arxiv.org/abs/2609.21686v1) | [📄 PDF](https://arxiv.org/pdf/2609.21686v1)
- **作者:** Tao Huang, Guosen Wu, Guolong Zheng, Jiayang Meng, Chen Hou, Xu Yang, Xuechao Yang, Feng Xia
- **分类:** cs.CR, cs.AI
- **摘要:** LLM agent 隐私泄露常在单组件（记忆/检索/工具调用）内评估，难以区分内部暴露与外部观察者实际可恢复信息。CIPL（Channel Inversion for Privacy Leakage）：黑盒隐私泄露的**通道感知**评估框架——通过敏感源、选择、组装、执行、观察、提取阶段表示目标，在共享协议下评估「敏感单元 → 攻击者可恢复输出」的转换；覆盖记忆型/检索中介型/工具中介型目标。
- **关联度:** ★★★★ 隐私泄露的可恢复性评估——k 的多 agent 协作/知识库的「内部暴露 vs 外部可恢复」区分；「通道感知 + 共享协议」对 k 的 GitHub 隐私门禁（github-privacy-gate）是评估框架升级

### 13. A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal

- **ID:** [2609.21996v1](https://arxiv.org/abs/2609.21996v1) | [📄 PDF](https://arxiv.org/pdf/2609.21996v1)
- **作者:** Hiskias Dingeto
- **分类:** cs.AI
- **摘要:** LLM 可以持有知识但不报告：模型可能在能力评估上 sandbag，或违背内部所知作答——仅靠输出无法判断它在藏答案还是真没有。借用法医隐藏信息测试（CIT）：给嫌疑人呈现真实细节与似是而非的干扰项，测量对识别项的更强反应。PIR（Probe of Internal Recognition）在模型内部做同样的事：提问+候选答案，从内部状态读模型识别哪个候选为正确。
- **关联度:** ★★★★ 内部知识探测（防 sandbag）——k 的模型评估/盲评的「隐藏能力」检测；「从内部状态识别认知」对 k 的 agent 评测（模型会不会但不说）是方法论补充

---

## 五、推理模型与遗忘（1 篇）

### 14. GUARD: Natural Forgetting in Large Reasoning Models via Guided Answer-Reasoning Distillation

- **ID:** [2609.21677v1](https://arxiv.org/abs/2609.21677v1) | [📄 PDF](https://arxiv.org/pdf/2609.21677v1)
- **作者:** Zeyu Yan, Guanghao Zhou, Minghui Qiu, Ming Gao, Cen Chen
- **分类:** cs.AI
- **摘要:** 大推理模型（LRM）让机器遗忘更难：受保护事实/不安全理由可能在最终答案前的中间 CoT 痕迹中浮现。现有遗忘目标抑制目标内容或重定向内部表征，但不指定遗忘后轨迹应如何继续→幻觉替代/畸形边界/重复输出。GUARD：LRM 遗忘应学习**自然遗忘轨迹**——连贯不披露的 CoT + 稳定拒答式答案替换原始披露；用引导式答-推理蒸馏实现。
- **关联度:** ★★★★ 推理模型的「自然遗忘」——k 的内容边界/隐私红线的模型侧对应：「遗忘不是删掉而是重写行为轨迹」；对 k 的脱敏/抹除流程（GitHub 隐私门禁、私密材料处理）是行为层设计参考

---

## 六、LLM 应用（2 篇）

### 15. AutoRecLab: Describe the Experiment, Get the Code!

- **ID:** [2609.21863v1](https://arxiv.org/abs/2609.21863v1) | [📄 PDF](https://arxiv.org/pdf/2609.21863v1)
- **作者:** Moritz Baumgart, Philipp Meister, Justus Krell, Michael Schmidt, Bela Gipp, Joeran Beel
- **分类:** cs.AI, cs.IR, cs.LG
- **摘要:** 推荐系统实证评估是把实验设计转成可执行代码的手工易错过程。AutoRecLab：Python 自主 RecSys 实验室，从自然语言提示自动化 RecSys 实验——给定研究想法，推导显式实验需求、构建验证原型、迭代扩展为完整实验；工作流组合 RAG 文档查找 + 静态类型验证 + 执行引导树搜索。
- **关联度:** ★★★★ 自然语言→可执行实验——k 的「描述→代码」流水线（数模代写/论文实验/PCB 自动化）的通用形态；「RAG+类型验证+执行引导搜索」对 k 的交付质检是流程参考

### 16. CoLearn: An Agentic Tutor that Learns its Learner in a Human--AI Co-Learning Loop

- **ID:** [2609.21154v1](https://arxiv.org/abs/2609.21154v1) | [📄 PDF](https://arxiv.org/pdf/2609.21154v1)
- **作者:** Kailai He, Zhihao Wu, Linhai Zhang, Runcong Zhao, Yulan He, Jiazheng Li
- **分类:** cs.CL
- **摘要:** 好家教适配个体：跟踪学习者知道什么、发现为什么错、问最有帮助的下一题。多数部署的辅导工具只服务固定题单、把错题当单比特信号。CoLearn：交互式 agentic 家教，迭代辅导循环——学习者练习，系统构建基于证据的学习者掌握度/误解记忆，证据积累时更新并用它生成下一个个性化问题；组件含持久学习者状态记忆（软证据变量更新主题掌握度）。
- **关联度:** ★★★★★ agentic 家教 = k 的家教业务（primary-education-tutoring、数学每日一练）的 AI 版：「学习者状态记忆 + 证据驱动出题」正是 sora 家教/墨题刷题机的差异化方向；「软证据掌握度」对 k 的词汇/题库数据管道（vocabulary-db-enrichment）是产品参考

---

## 七、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.21386](https://arxiv.org/abs/2609.21386v1) | AgentVidBench: A Multi-Hop Video Question Answering Benchmark for Evaluating MLLM Agents | 多跳视频 QA 的 agent 能力基准：真实世界视频理解需多跳多模态推理，现有基准只测单步场景级查询——k 的多模态 agent 评测（图片/视频素材审核）的缺口清单 |
| 2 | [2609.21527](https://arxiv.org/abs/2609.21527v1) | OpenMAS-GCom: A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems | G-MAS 组件归因诊断基准：受控干预把性能差异归因到通信结构/角色分配/信息流而非总分数——k 的多 agent 分工（k/WorkBuddy/dsh/Gemini）的「谁贡献了什么」评测方法 |
| 3 | [2609.21554](https://arxiv.org/abs/2609.21554v1) | MIRAGE: Multi-Perspective Creative Language Model Reasoning with Reinforcement Learning Guidance | 多视角推理框架：Selector 优先有效概念视角 + Reasoner 顺序求解到置信出现，否则聚合多视角——k 的「跨源盲评/多方观点」的推理版 |
| 4 | [2609.21113](https://arxiv.org/abs/2609.21113v1) | Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models | 微调如何重塑内部机制：EAP 识别组件集中在特定层（功能定位），表征变化分布 vs 因果重要性解耦——对 k 的模型选型/微调判断是「看内部因果而非表面分数」提醒 |
| 5 | [2609.20888](https://arxiv.org/abs/2609.20888v1) | Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding | 端到端可训练稀疏注意力：从查询表征预测动态上下文阈值，难检索/推理步保留稠密上下文、常规 token 剪枝——k 的本地推理（8GB）长上下文效率路线 |
| 6 | [2609.21899](https://arxiv.org/abs/2609.21899v1) | ExpBoN: Exponential-Noise Best-of-$n$ for Efficient Test-Time LLM Alignment | 软 BoN 的指数噪声变体：精确有限-n 分解，总变差/期望奖励/双向 KL 指数收敛——k 的低成本对齐/评测（test-time 而非微调）理论工具 |
| 7 | [2609.21857](https://arxiv.org/abs/2609.21857v1) | Do Personality-Tuned LLMs Make Better Social Agents? | 人格感知微调 vs 指令提示：Qwen2.5-7B/Ministral-8B 人格条件对话的一致性与可控性——k 的 SOUL.md 人格稳定性的实证问题：「人格靠微调还是靠提示」 |

---

## 今日要点（主题信号）

1. **编码 agent 的 RL 环境从「代码自身」规模化**：22068 CodeMidas 把已实现功能转成可执行 RL 环境——「agent 构建 agent 的训练环境」；同方向 21187 证明单步指标不迁移自主执行——环境真实性决定训练有效性。
2. **记忆进入「可信决策 + 结构化进化」阶段**：22043 MDL 给检索记忆加零参数信任门（RAG 幻觉的根因在盲目注入）、21533 MACE 记忆-代理共进化、22086 Designer-RSI 程序记忆变宽变深 + 回放门——k 的 RAG/记忆/技能体系的三个升级件。
3. **技能图结构化是技能体系下一站**：21749 GraphSkillEvo 把技能表示为图结构自然语言做进化优化——k 的 SKILL.md 扁平技能的进化版蓝图。
4. **评测「端到端 + 降本」双轨**：21267 生产 agent 用 IRT 自适应少跑题保真、21492 LogicTrack 符号审计中间推理步骤、21341 小模型数据库 agent 失败 75.7% 在工具调用环节——k 的验证门禁要「分步对≠闭环成」。
5. **安全隐私向「可恢复性/隐藏知识」深入**：21686 CIPL 区分内部暴露与外部可恢复、21996 PIR 探测模型隐藏知识、21484 HE 加密推理的 jailbreak 盲区——k 的隐私门禁/安全评估的威胁建模升级。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| CodeMidas 2609.22068 | arxiv.org abs 页 + web_search 跨源（编码 RL 环境研究群：CodeGym/Agent RL Scaling 同族互证） | ✅ 已确认（arXiv HTML 收录 + 同族研究群互证） |
| MACE 2609.21533 | arxiv.org abs 页 + web_search 跨源（记忆-代理共进化研究群：MAGE/CoMem/CoEvo-Mem/HyperSkill 互证） | ✅ 已确认（arXiv HTML 收录 + 同族研究群互证） |
| GraphSkillEvo 2609.21749 | arxiv.org abs 页 + web_search 跨源（技能图研究群：SkillGraph/EvoSkill/HyperSkill 互证） | ✅ 已确认（arXiv HTML 收录 + 同族研究群互证） |
| LogicTrack 2609.21492 | arxiv.org abs 页 + web_search 跨源（符号审计研究群：SymDiag/ReasoningLens/FOL-Traces 互证） | ✅ 已确认（arXiv HTML 收录 + 同族研究群互证） |
| 其余 19 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **记忆信任门试点**：22043 MDL「检索后加零参数可信决策」——k 的墨题 RAG（DashScope embedding）+ 知识库检索加「冲突检测/置信门」，防盲目注入放大幻觉
- 🔴 **技能图进化探索**：21749 GraphSkillEvo「技能图 + 进化优化」——k 的 skill-evolution 从「扁平文本技能」升级为「图结构技能 + 依赖边」试点（如把 skill-pipeline 九流派建模成图）
- 🟡 **端到端验证门**：21187「单步指标不迁移自主执行」——k 的 cron/交付流程验证从「分步检查」补「端到端闭环断言」（如 verify_digest_note 之外加整链 smoke）
- 🟡 **Agentic 家教方向**：21154 CoLearn「学习者状态记忆 + 证据驱动出题」——sora 的家教/墨题刷题机的 AI 差异化：错题记忆 → 下题生成，接 vocabulary-data-pipeline
- 🟡 **生产评测降本**：21267 IRT 自适应测试「200 题 ≈ 全量 38.5% 保真」——k 的每日速览/周报/健康巡检的抽样策略
- 🟢 **待深读**：22068（CodeMidas）、22086（Designer-RSI）、21533（MACE）、22043（MDL）、21749（GraphSkillEvo）、21187（next-turn gap）→ core-contributions 候选

---

*本速览由 cron 自动生成：2026-09-21（周一）arXiv list 页出现新日期分组（09-21，460 篇，周末提交并入）→ 与 covered_ids（777）比对 0 重叠（全新窗口）→ 标题粗筛 56 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选（16 主条目 + 7 简评）。关键论文跨源 web 验证（CodeMidas / MACE / GraphSkillEvo / LogicTrack）。元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
