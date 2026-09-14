---
aliases:
  - arxiv-2026-09-14-agent-llm
  - arxiv-agent-llm-2026-09-14
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-14
updated: 2026-09-14
status: adopted
source: arxiv.org list pages + abs pages（09-14 新窗口正常速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-14

> **检索时间**: 2026-09-14 GMT+8（cron）
> **窗口**: list 页出现新日期分组 **2026-09-14（432 篇）**——周末（09-12/13）提交并入、与已覆盖池（607）**零重叠** → 全新窗口 → 正常速览。export.arxiv.org API 持续 429 限流 → HTML list 页路由。
> **收集**: 6 类别 list/recent 页全量 → 09-14 分组 **432 unique base ID**（剔除 1 个 re-listing 异类 2602.09490）→ 标题粗筛 55 候选（score≥2）→ 人工剔除领域应用（无人机/医疗/运输/化工/金融等）→ 逐篇抓 abs 页精选 **17 主条目 + 12 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、Agent 记忆与技能（3 篇）

### 1. Skill Issue: Lessons from Optimizing Repository SKILLs for Coding Agents

- **ID:** [2609.12742v1](https://arxiv.org/abs/2609.12742v1) | [📄 PDF](https://arxiv.org/pdf/2609.12742v1)
- **作者:** Mykhailo Kozyrev, Andrei Kozyrev, Anton Podkopaev
- **分类:** cs.AI
- **摘要:** 编码 agent 越来越多地从随代码版本化的 SKILL（纯 `.md` 文件）读取仓库知识。近期工作通过针对基准优化文档来自动合成这些文件。但裸仓库没有基准，先前构建的合成任务太小，能干 agent 无需文档就能饱和。作者改用**更硬的任务**——仓库的已合并 PR 在冻结基线提交上回退——用「同一 agent 有文档 vs 无文档谁做得更好」给候选文档打分。在三个 Kotlin 仓库上验证。核心问题：如何在没有基准的仓库上优化 SKILL 文档。
- **关联度:** ★★★★★ 直接命中 Hermes 技能体系——「技能文档质量 = 同一 agent 有无文档的表现差」给 k 的 skill 治理提供可操作度量；「合成任务太小会饱和」警示技能测试别只建简单用例

### 2. AIM: A Privacy-Aware Interoperable Memory Framework for Multi-Agent Multi-User LLM Systems

- **ID:** [2609.12320v1](https://arxiv.org/abs/2609.12320v1) | [📄 PDF](https://arxiv.org/pdf/2609.12320v1)
- **作者:** Zachary Johnson, Nigel Boachie Kumankumah, Somya Chatterjee, Tejas Sathyamurthi, Min Chen, Xinyi Alice Li, Xiao Wang, Emily Morgan Gelchie, Jessica Lin, Sadid A. Hasan, Sulaiman Vesal
- **分类:** cs.AI, cs.LG
- **摘要:** 传统 LLM 限定在单用户会话，无法学习随时间演化的用户偏好。现有 agentic 记忆系统一般只做单用户级别，限制跨用户可共享的公共知识。AIM（Agentic Interoperable Memory）提出**隐私感知的互操作记忆框架**：多 agent、多用户 LLM 系统可持久管理私有与共享记忆。
- **关联度:** ★★★★ 多用户记忆共享与隐私隔离——墨题多用户题库/记忆（已补齐 user_id 隔离）的架构参考；「私有 vs 共享记忆分层」与 k 的隐私红线（私人规划只留本地）同构

### 3. LifeMem: Enabling Lifelong Experience Reuse for LLM Agents

- **ID:** [2609.12655v1](https://arxiv.org/abs/2609.12655v1) | [📄 PDF](https://arxiv.org/pdf/2609.12655v1)
- **作者:** Yuli Qiu, Yutong Li, Wei Su, Zeming Liu, Wanxiang Che, Heyan Huang, Haifeng Wang, Yuang Guo
- **分类:** cs.CL
- **摘要:** LLM agent 预期在生命周期内通过复用过往经验持续适应新任务/环境。但现有基于记忆的 agent 难以跨环境迁移可复用经验，且随经验积累遭受灾难性遗忘。LifeMem 提出终生学习框架：学习阶段按底层 workflow 聚类交互轨迹提取可复用技能；求解时用这些技能解决新任务，对抗灾难性遗忘。
- **关联度:** ★★★★★ 「跨环境技能迁移 + 抗灾难性遗忘」——与 k 的 skill-evolution / 技能蒸馏（COBRA-Skills 主线）直接呼应；「按 workflow 聚类轨迹提取技能」是技能自举的另一种形态

---

## 二、Agent 安全与治理（4 篇）

### 4. K-Bench: A Benchmark for LLM Unlearning in Agentic Deployments

- **ID:** [2609.12808v1](https://arxiv.org/abs/2609.12808v1) | [📄 PDF](https://arxiv.org/pdf/2609.12808v1)
- **作者:** Guangsheng Yu, Yanna Jiang, Qin Wang, Baihe Ma, Xu Wang
- **分类:** cs.AI
- **摘要:** TOFU、MUSE 等 unlearning 基准通过读模型最终答案认证遗忘——模型拒绝回答就算已遗忘。作者证明：一旦模型部署为 agent，这种模型级证书不再成立。K-Bench 专门评测 **agentic 部署下的 LLM unlearning**：检查 ReAct agent 暴露的全部六个通道——链式思维（CoT）、工具调用、工具观察、总结——任一通道泄露秘密即算泄漏。
- **关联度:** ★★★★ 「模型级遗忘证书在 agent 部署下失效」——对 k 的多端 AI provider / 记忆注入安全审计的警示：只检查「最终回答」会漏掉 CoT/工具调用的泄露面

### 5. SoK: Rethinking Jailbreaking in the Era of Agentic AI: Attacks, Defenses, and Practical Consideration

- **ID:** [2609.12413v1](https://arxiv.org/abs/2609.12413v1) | [📄 PDF](https://arxiv.org/pdf/2609.12413v1)
- **作者:** Md Jueal Mia, Yanzhao Wu, Selcuk Uluagac, M. Hadi Amini
- **分类:** cs.AI
- **摘要:** LLM 正从对话助手演化为 agentic AI：推理、规划、调用工具、维护持久记忆、与其他 agent 通信、执行多步任务。同时现代模型原生安全对齐显著强于早年研究 jailbreak 攻击/防御时的模型。SoK 系统性重审：**哪些既有 jailbreak 安全发现在现代 LLM 与 agentic AI 时代仍然成立？**
- **关联度:** ★★★★★ agentic 安全系统性重审——与 09-11「安全焦点转向评估与验证基础设施」主线延续；k 的 agent 安全审计（MCP server 预检/Codex 红线）需按「现代模型对齐更强」校准旧假设

### 6. Guardrailed Meta-Agent Loops: Stress-Testing Policy Pinning, Budget Bounds, and Crash Recovery

- **ID:** [2609.12216v1](https://arxiv.org/abs/2609.12216v1) | [📄 PDF](https://arxiv.org/pdf/2609.12216v1)
- **作者:** Qinzhen Ma, Jialin Wu
- **分类:** cs.RO
- **摘要:** 自改进 agent 工作流产生审计问题：同一控制器既能改变自身行为，也能改变行为被评判的条件。GuardrailLoop 提出基于模拟的测试台，让三个运维契约可联合测试：人类定义策略的保留、每个执行前缀的计算记账、崩溃后恢复指定科学状态。**哈希固定策略**锁定目标/范围/评估身份/预算/发布条件，机器驱动的演化限制在代码拥有的特性目录内。
- **关联度:** ★★★★★ 自改进 agent 的护栏契约——与 k 的 skill-evolution / 自进化引擎直接同题；「哈希固定策略 + 计算记账 + 崩溃恢复」可成为 k 自举系统（技能自进化、自我完善）的治理模板

### 7. Look Before You Leap: Pre-Action Verification for LLM Agents

- **ID:** [2609.11957v1](https://arxiv.org/abs/2609.11957v1) | [📄 PDF](https://arxiv.org/pdf/2609.11957v1)
- **作者:** Asaad Althoubi
- **分类:** cs.LG, cs.MA
- **摘要:** LLM agent 通过发出动作作用于世界：shell 命令、编辑等。错误动作不总是大声失败——可能静默失败，产生看似合理但错误的效果且不报错。作者主张：**在动作生效前运行廉价确定性检查**是一种有效且被低估的 agent 监督形式，跨两种动作模态统一研究。想法：在执行前固定动作的正确效果，直接测量静默失败，验证器可弃权而不猜测。
- **关联度:** ★★★★★ 「动作前验证 = 廉价确定性检查」——与 k 的验证门禁（patch 前 grep 冲突、build+pytest、GitHub 隐私门禁）哲学完全一致；「验证器可弃权不猜测」对 k 的门禁设计有直接启发

---

## 三、Agent 评估与基准（4 篇）

### 8. Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction

- **ID:** [2609.13082v1](https://arxiv.org/abs/2609.13082v1) | [📄 PDF](https://arxiv.org/pdf/2609.13082v1)
- **作者:** Baoyang Jiang, Fengchun Zhang, Leyuan Wang, Haotian Li, Yida Wang, Zhe Ji, Jinshan Lai, Xi Ren, Danyang Li, Zheng Yang, Jianwei Hu, Qiang Ma
- **分类:** cs.AI
- **摘要:** Agentic 系统有望自动化具身基准构建，但现有方法只覆盖孤立阶段或专用于预定义环境/任务族。更关键：多步构建产生**相互依赖的中间工件**，常不经验证直接传给下游，局部缺陷会传播进最终基准。Embodied-BenchForge 把用户评测意图转化为完整具身基准工件，构建流程带工件级验证。
- **关联度:** ★★★★ 「中间工件必须逐件验证、防缺陷传播」——与 k 的多步交付（AI 标注→3库同步→门禁）直接同构；「agentic 生成基准 + 闭环验证」对 k 自建评测流程有参考

### 9. ParaRecover: A Process-Level Benchmark for Error Localization and Recovery in Parallel Tool-Use Agents

- **ID:** [2609.12345v1](https://arxiv.org/abs/2609.12345v1) | [📄 PDF](https://arxiv.org/pdf/2609.12345v1)
- **作者:** Bowen Guan, Zhentao Yin, Yanming Shen
- **分类:** cs.LG, cs.SE
- **摘要:** 现有 agent 基准主要评测最终任务成功或工具调用正确性，很少检验 agent 能否可靠诊断并恢复**中间执行失败**。这在多轮并行工具使用场景尤为关键：错误可能跨依赖分支传播、触发级联失败。ParaRecover 提出进程级基准：14 种错误类型分类（规划依赖、并行工具调用等）覆盖错误定位与恢复。
- **关联度:** ★★★★★ 「级联失败恢复评测」——与 k 的 delegate_task 并行子代理 / 多 agent 编排的故障恢复直接相关；14 种错误类型分类可对照 k 的 32 项写码前扫坑清单

### 10. VRL-Bench: Benchmarking agents on computer control tasks under finite trial budgets

- **ID:** [2609.12404v1](https://arxiv.org/abs/2609.12404v1) | [📄 PDF](https://arxiv.org/pdf/2609.12404v1)
- **作者:** Yu Bai, Yukai Miao, Dawei Wang, Li Chen, Yanyu Ren, Yuqian Shi, Dan Li, Ying Xiong, Chengqiu Tan, Run Zhou, Li Li
- **分类:** cs.AI
- **摘要:** 从试错中学习是提升语言 agent 复杂任务（如计算机控制）的可行路径。Reflexion 引入口头强化学习：把失败试次转成文本指导后续尝试，不更新模型参数。VRL-Bench 提供**有限试次预算下公平评测试错学习**的 harness：MiniWoB 和 WebShop 上三模型评估多种口头记忆方法——各方法都在某些设置提升观察成功率，但相互比较结果参差。
- **关联度:** ★★★★ 口头 RL 基准 harness——与 09-11「T1 终端 agent RL」+ VRL 评估主线延续；「有限试次预算」对 k 评模型/评测方法的成本约束视角

### 11. GTA: Graph Theory Agent and Benchmark for Algorithmic Graph Reasoning with LLMs

- **ID:** [2609.12265v1](https://arxiv.org/abs/2609.12265v1) | [📄 PDF](https://arxiv.org/pdf/2609.12265v1)
- **作者:** Zixiang Xu, Yanbo Wang, Chenxi Wang, Lang Gao, Zirui Song, Yue Huang, Zhaorun Chen, Xiangliang Zhang, Xiuying Chen
- **分类:** cs.AI
- **摘要:** LLM 越来越多被要求推理图等结构化数据，但它们在语言中可靠执行多步图算法的能力尚不清楚。现有评测用简单任务小图、评代码生成而非图本身推理、或固定单一输入格式。GT Bench 覆盖 24 个经典图问题的 44 种任务结构设置、10 万+样例，四种表示：自然语言、结构化语言、邻接表、邻接矩阵。
- **关联度:** ★★★ 结构化图推理基准——PCB/电路网络等结构化数据的 LLM 推理参考；四种输入表示对比对评测设计有方法论价值

---

## 四、Agent 执行与推理（4 篇）

### 12. Granularity-Adaptive Credit Assignment for Long-Horizon LLM Agent Reinforcement Learning

- **ID:** [2609.12424v1](https://arxiv.org/abs/2609.12424v1) | [📄 PDF](https://arxiv.org/pdf/2609.12424v1)
- **作者:** Taoran Liang, Yang Liu, Shang Luo, Yingguang Yang, Rongrong Zhang, Yingzong Min, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Kefu Xu, Congjing Ran, Bin Chong
- **分类:** cs.LG
- **摘要:** RL 是训练长程 LLM agent 的标准方式，数十个相互依赖动作后只有一个稀疏奖励。GRPO 等免 critic 分组相对方法适合此场景，但把整个轨迹级标量广播到每步，无法区分哪步决策驱动了结果。GiGPO 通过按共享 anchor 状态分组时间步恢复步级信号，但用固定权重合并步级与轨迹级估计——在关键分支决策和常规步骤上花同样分辨率。本文提出粒度自适应信用分配。
- **关联度:** ★★★★★ 长程 agent RL 信用分配——与 09-11「T1 终端 agent RL」+ 09-10「Multi-Harness RL credit assignment」主线延续；「粒度自适应 = 关键决策高分辨率」对 k 的 RL/奖励设计（墨题 AI 评分）有方法论启发

### 13. EvoRS: On-Policy Self-Evolution of Reward Systems for Open-Ended Reinforcement Learning

- **ID:** [2609.12459v1](https://arxiv.org/abs/2609.12459v1) | [📄 PDF](https://arxiv.org/pdf/2609.12459v1)
- **作者:** Weiyuan Li, Aili Chen, Xintao Wang, Yikai Zhang, Qingqing Dong, Jinghan Xu, Hongru Hou, Wenxuan Zhao, Chengkun Lang, Jun Gao, Yuanli Guo, Hongcheng Guo, Yanghua Xiao, Deqing Yang
- **分类:** cs.AI
- **摘要:** 开放端 RL 常依赖基于 rubric 的奖励处理无直接可验证答案的任务。但策略与奖励系统形成动态反馈环：策略优化当前奖励时，初始有用的奖励系统可能因 reward hacking 或响应可区分度下降而变得不可靠。奖励系统应随训练演化而非固定。现有动态 rubric 方法只调整评估标准，但奖励失败也可能源于评分机制或信号组合。EvoRS 提出自演化奖励系统。
- **关联度:** ★★★★★ 「奖励系统本身要随策略共演化」——与 k 的技能自进化（self-improving-agent）/ 自举循环直接同题；「奖励失败三来源：hacking/可区分度/评分机制」对 k 的门禁与评估设计有启发

### 14. Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Controlled Private Suite

- **ID:** [2609.11987v1](https://arxiv.org/abs/2609.11987v1) | [📄 PDF](https://arxiv.org/pdf/2609.11987v1)
- **作者:** Mohsen Arjmandi
- **分类:** cs.AI, cs.CL, cs.SE
- **摘要:** Agentic 编码系统把语言模型与 harness 耦合：工具、提示、控制流把聊天模型变成自主软件工程师。厂商为自己的模型调校 harness，从业者假设厂商原生配对解决更多任务。作者用**256 个仓库 + cutoff 后竞赛任务的私有污染受控套件**、同模型配对对比测量该假设：claude-agent-sdk vs deepagents 跑 claude-opus-4-8，openai-codex SDK vs deepagents 跑 gpt-5.5，gemini-3.5-flash 等。
- **关联度:** ★★★★★ 直接命中 k 的工具分工（Codex 编码 / Antigravity 前端 / harness 选型）——「harness vs model 谁贡献了提升」的对照实验方法；污染受控私库对 k 评估模型/harness 的可信度关键

### 15. Reality Is the Final Verifier: On Two Key Gaps in Agentic Software Engineering

- **ID:** [2609.12039v1](https://arxiv.org/abs/2609.12039v1) | [📄 PDF](https://arxiv.org/pdf/2609.12039v1)
- **作者:** Alexander Krentsel, Shubham Agarwal, Mert Cemri, Shu Liu, Sidharth Sankhe, Ziming Mao, Matei Zaharia, Ion Stoica
- **分类:** cs.SE, cs.AI
- **摘要:** 软件开发遵循实现-验证循环：开发/agent 反复修改实现直到测试套件等评估器接受。评估器在部署环境模型下对照需求检查实现。但即便形式证明实现满足模型下的需求，也不能保证部署后可接受行为——需求只近似利益相关者意图，模型只近似真实部署环境。作者称这两个缺口为**需求缺口与模型缺口**（requirement gap + model gap）。
- **关联度:** ★★★★★ 「测试套件通过 ≠ 部署可接受」——k 的交付门禁（build+pytest 通过 ≠ 真实环境可用）的理论框架；需求缺口/模型缺口双视角对 k 的验收标准设计（WPS 渲染验证/UI 实测）有启发

---

## 五、Agentic 软件工程（2 篇）

### 16. Test-Driven Approaches to Software Engineering with Large Language Models: A Survey of Phases, Tasks, and Agent Skills

- **ID:** [2609.12012v1](https://arxiv.org/abs/2609.12012v1) | [📄 PDF](https://arxiv.org/pdf/2609.12012v1)
- **作者:** Yunhao Liang, Chengguang Gan, Ruixuan Ying, Hanjun Wei, Zhe Cui, Shiwen Ni
- **分类:** cs.SE
- **摘要:** 测试越来越多参与 LLM 与 SE agent 的决策：指定预期行为、指导程序构建与修复、选择候选、约束转换、为软件分析提供执行证据。这些用法借鉴 TDD，但在测试顺序、oracle 可用性、可编辑工件、执行角色上差异显著。本综述围绕「测试改变了什么决策」组织，整合 87 篇研究与支撑记录。
- **关联度:** ★★★★ TDD×LLM 系统综述——k 的 test-driven-development 技能 / 交付门禁的学术版图；「测试参与哪些决策」框架对 k 的验证策略设计有参考

### 17. What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ: An LLM Agent Self-Refinement Framework

- **ID:** [2609.12746v1](https://arxiv.org/abs/2609.12746v1) | [📄 PDF](https://arxiv.org/pdf/2609.12746v1)
- **作者:** Ioannis Prokopiou, Athanasios Aidinis, Panagiotis-Christos Kyrmpatsos, Pantelis Vikatos
- **分类:** cs.AI, cs.CL, cs.LG, cs.MA, cs.SE
- **摘要:** Agentic 结构化查询生成流水线快速扩张，但哪部分循环带来增益不明。LAST-CQ 是五 agent、免训练、执行接地的 Text-to-Cypher 框架，用作仪表化测试台：2,471 条真实数据库查询、六个跨三档厂商规模的 backbone 上跑三个反事实。移除纠错 = 对单遍系统 3.1% 聚合执行-BLEU、对无精炼反事实 12.3%（最弱 backbone 达 80.7%）。
- **关联度:** ★★★★ 「哪个环节驱动 agent 增益」反事实方法论——k 的墨题 RAG/题库检索、多步流水线做消融实验的参考；「执行接地 + 反事实归因」对 k 的评估习惯有启发

---

## 六、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.12495](https://arxiv.org/abs/2609.12495v1) | Information Specialization and Constrained Synthesis in Multi-Agent LLM Forecasting: A Prospective Live-Study of the 2026 FIFA World Cup | 2026 世界杯 56 场前瞻实测：量化专家 vs 新闻专家两个专职 agent 是否产出不同预测、合成是否提升效用——多智能体专精化的现场证据 |
| 2 | [2609.12475](https://arxiv.org/abs/2609.12475v1) | Zipbench: Low-Cost Framework for Compressing Comprehensive Benchmarks of Large Language Models | 主流基准冗余严重、评测昂贵，而强压缩方法依赖大量已公开逐样本结果；Zipbench 用低成本框架压缩基准（无需大规模样本集合） |
| 3 | [2609.12317](https://arxiv.org/abs/2609.12317v1) | Sampling via Decision-Flow: Training-Free Extraction of Improved Latent Reasoning Paths in Large Language Models | 基于分布锐化假设：RL 只是重分配基座模型已潜藏的高奖励轨迹概率。DF-Sample 免训练、免数据构建分层推理树、给终节点打分、提取更优潜在推理路径 |
| 4 | [2609.12373](https://arxiv.org/abs/2609.12373v1) | Toward Robust Personalized Alignment for LLMs: Mitigating Persona Drift in Multi-Turn Dialogue | CORE：分离「回合局部证据」与「持久人设状态修订」，不确定性感知信念修订选择性更新接地用户偏好；配套 PERSIST 人设状态鲁棒基准 |
| 5 | [2609.13005](https://arxiv.org/abs/2609.13005v1) | Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning for Language Models | TAM 基准：现有评测多为短程（几步检索/推理），而真实任务是遵循数百页相互依赖手册的长程程序推理——暴露长程可靠性缺口 |
| 6 | [2609.12896](https://arxiv.org/abs/2609.12896v1) | Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents | 单 LoRA 免路由开销但异构轨迹学习有挑战；行为商学习按行为划分 LoRA 容量，低秩适配 LLM agent |
| 7 | [2609.12551](https://arxiv.org/abs/2609.12551v1) | RoofLang: Enabling AI-Driven Architecting of LLM Inference Systems | 现有 AI 推理优化都是 profiling 约束（锁死现有软件栈）；RoofLang DSL = 通用工作负载表示 + 可验证变异空间 + 实现无关评估器，让 AI 重构 LLM 推理系统架构 |
| 8 | [2609.12439](https://arxiv.org/abs/2609.12439v1) | Debiasing as a Measurement Intervention: Calibrated Ties and Resolution Loss in LLM-as-a-Judge Evaluation | 让 judge 忽略引用格式等呈现线索可压偏置，但会损坏测量分辨率；TraceJudgeBench 诊断基准：审计 RAG/agent 评测中引用类伪影 |
| 9 | [2609.12191](https://arxiv.org/abs/2609.12191v1) | GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Evaluation of Task-Oriented Agents | 25 个 agent × 6 提供方、τ²-bench 与 SimulatorArena 上测「LLM 用户模拟器 + judge 排名」是否匹配可验证奖励，分离排名有效性与构念有效性 |
| 10 | [2609.12127](https://arxiv.org/abs/2609.12127v1) | Local Edits, Global Ripples: Replay-Informed Policy Adaptation for Workflow Synthesis | 提示策略编辑的两个耦合性质：编辑局部性≠效果局部性（编辑会涟漪到下游执行）；效果合成敏感（单独有效的编辑组合后互相干扰）。重放知情策略适配 |
| 11 | [2609.11956](https://arxiv.org/abs/2609.11956v1) | Performance, Efficiency and Collapse -- Advantages and Challenges in Offline Post-training of Code LLMs | 代码 LLM 的 RL 后训练通常需昂贵样本生成 + GPU-CPU 通信验证；本研究考察能否用既有数据集完全离线后训练（免生成新样本），含性能/效率/崩塌三面 |
| 12 | [2609.13003](https://arxiv.org/abs/2609.13003v1) | Judging by the Cover: Cleaning LLM Truthfulness Benchmarks to Avoid Surface-Level Feature Leakage | TruthfulQA 中二选一答案在表层特征上系统可分（6 特征逻辑回归即可高精度区分正误），模型可不做目标推理就超过随机；给出通用机制清洁基准防表层泄漏 |

---

## 今日要点（主题信号）

1. **技能/记忆的「可度量优化」与「跨环境迁移」**：12742 用「同一 agent 有/无文档的表现差」给仓库 SKILL 打分（合成任务太小会饱和，改用回退 PR 做硬任务）；12655 LifeMem 按 workflow 聚类轨迹提技能、跨环境迁移对抗灾难性遗忘；12320 AIM 打通多 agent 多用户私有/共享记忆。与 09-11「记忆策展主动验证」主线无缝延续。
2. **Agent 安全从「测最终答案」走向「全通道 + 动作前」**：12808 K-Bench 证明 unlearning 的模型级证书在 agent 部署下失效（CoT/工具调用/观察六通道都会泄露）；11957 主张动作生效前的廉价确定性检查（验证器可弃权不猜测）；12413 SoK 重审 jailbreak 结论在现代对齐模型下哪些仍成立。
3. **自进化系统需要「护栏契约」**：12216 GuardrailLoop 让策略固定、计算记账、崩溃恢复三个契约联合可测；12459 EvoRS 奖励系统本身随策略共演化（hacking/可区分度/评分机制三来源）；12424 粒度自适应信用分配（关键决策高分辨率 vs 常规步骤粗粒度）。自举循环从「自由进化」走向「带护栏 + 分粒度」。
4. **Agentic 编码的「真实世界验证」收紧**：11987 Harness or Model 用污染受控私库（256 仓库 + cutoff 后竞赛）隔离 harness 效应，直接拆「厂商原生配对更好」假设；12039 形式证明通过仍不等于部署可接受（需求缺口 + 模型缺口）；12012 TDD×LLM 综述 87 篇。「测试通过 ≠ 能用」成为主流框架。
5. **评测基准的「进程级 + 消融」深化**：12345 ParaRecover 测并行工具 agent 的中间错误定位与级联恢复（14 种错误类型）；12746 LAST-CQ 反事实归因哪个环节驱动增益；13082 中间工件逐件验证防缺陷传播。评测从「最终成功」下沉到「过程可靠性」。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Skill Issue 2609.12742 | arxiv.org abs 页全文抓取 | ✅ 已确认（HTML 收录 + 全文摘要；回退 PR 硬任务方法论） |
| Harness or Model 2609.11987 | arxiv.org abs 页全文抓取 | ✅ 已确认（HTML 收录 + 全文摘要；256 仓库污染受控套件 / claude-agent-sdk vs deepagents 对照） |
| GuardrailLoop 2609.12216 | arxiv.org abs 页全文抓取 | ✅ 已确认（HTML 收录 + 全文摘要；哈希固定策略 + 计算记账 + 崩溃恢复三契约） |
| 其余 26 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **技能质量度量化**：12742「同一 agent 有无文档的表现差」——k 的 skill 治理（skill-evolution / skill-pipeline）补「对照测试」：对核心技能建一个「有技能 vs 无技能」任务对，用表现差追踪技能文档是否真有用，别只靠文档长度/覆盖度
- 🔴 **动作前验证进门禁**：11957「动作生效前的廉价确定性检查 + 验证器可弃权不猜测」——k 的写码门禁（grep 冲突前置检查、patch 前锚点唯一性、build 前置）已部分实践，补「验证器不确定时明确 abstain 而非硬猜」的原则
- 🟡 **agent 泄露面全通道自查**：12808「模型级遗忘证书在 agent 部署下失效，六通道都查」——k 的多端 AI provider / 记忆注入审计从「只看最终回答」扩展到 CoT/工具调用/日志等通道
- 🟡 **harness vs model 对照**：11987「厂商原生配对未必更好」——k 评估模型/harness（Codex/opencode-go/deepseek-harness）时建污染受控私有对照，别只信厂商默认配对
- 🟢 **待深读**：12742 Skill Issue（仓库 SKILL 优化方法论）、11987 Harness or Model（harness 效应隔离）、12216 GuardrailLoop（自进化护栏契约）、12459 EvoRS（奖励系统自演化）→ core-contributions 候选

---

*本速览由 cron 自动生成：09-14 检查 list 页出现 09-14 新分组（432 篇，周末提交并入，与 covered 607 零重叠）→ 标题粗筛 55 候选 → 人工剔除领域应用（无人机/医疗/运输/化工/金融等）→ 逐篇抓 abs 页精选（17 主条目 + 12 简评）→ 元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

---
状态：reading
