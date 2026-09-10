---
aliases:
  - arxiv-2026-09-10-agent-llm
  - arxiv-agent-llm-2026-09-10
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-10
updated: 2026-09-10
status: adopted
source: arxiv.org list pages + abs pages（索引解冻，09-09+09-10 新窗口正常速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-10

> **检索时间**: 2026-09-10 GMT+8
> **窗口**: 索引解冻！list 页出现新日期分组 **2026-09-09（1,303 篇，疑似含 09-08 合并）+ 2026-09-10（447 篇）**——与已覆盖池（537）**零重叠**，全新窗口 → 正常速览。export.arxiv.org API 持续 429 限流 → HTML list 页路由。
> **收集**: 6 类别 list/recent 页全量 → 09-09+09-10 分组 **1,749 unique base ID** → 标题粗筛 278 候选（score≥2）→ 人工剔除领域应用（医疗/金融/交通/无人机/制造/农业等）→ 逐篇抓 abs 页精选 **22 主条目 + 16 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、Agent 记忆与持久化（5 篇）

### 1. Memory as Infrastructure: Reliability Engineering for Persistent Agent Memory in Months-Long LLM-Assisted Development

- **ID:** [2609.05510v1](https://arxiv.org/abs/2609.05510v1) | [📄 PDF](https://arxiv.org/pdf/2609.05510v1)
- **作者:** Mike Helwig
- **分类:** cs.SE
- **摘要:** LLM 编码 agent 正从任务级跨入项目级：单次辅助努力可运行数月、跨多次上下文压缩、代码库远超任何上下文窗口。作者报告真实运维经验：自 2026 年 1 月起在单条连续 Claude Code 会话线下驱动的 63.3 万行代码库研究项目，其记忆子系统被持续插桩——把记忆当作基础设施做可靠性工程。
- **关联度:** ★★★★★ 「记忆即基础设施」正是 k 在 Hermes 里做的事——单会话线长跑 + 上下文压缩 + 持久记忆，这篇的运维经验（插桩、可靠性工程）可直接映射到 k 的记忆体系设计；对墨题长期会话/知识库治理也有参照

### 2. When Does Memory Help? A Cost-Aware Evaluation of Long-Term Memory in Tool-Using LLM Agents

- **ID:** [2609.05441v1](https://arxiv.org/abs/2609.05441v1) | [📄 PDF](https://arxiv.org/pdf/2609.05441v1)
- **作者:** Shweta Mishra, Shashank Mishra
- **分类:** cs.AI
- **摘要:** 长时记忆评测现状用对话回忆基准（LoCoMo、LongMemEval），测的是「问答对话历史」，而非「记住的事实是否改变工具使用 agent 的行为」。提出 MERIT（Memory Evaluation for Realistic Instrumented Tasks）基准+harness，在显式成本约束下测记忆对执行型任务的边际效用。
- **关联度:** ★★★★★ 记忆的「边际效用」视角——k 的记忆/知识库到底有没有让行为变好，而不是「记得住」；成本约束下的记忆价值评估是给 Hermes 记忆系统做评估的现成框架

### 3. Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems

- **ID:** [2609.08258v1](https://arxiv.org/abs/2609.08258v1) | [📄 PDF](https://arxiv.org/pdf/2609.08258v1)
- **作者:** Yi Ting Shen, Kentaroh Toyoda, Alex Leung
- **分类:** cs.AI, cs.CR
- **摘要:** 长跑 agent 依赖持久记忆。许多记忆系统用「软撤销」：被矛盾的事实标记为无效并保留而非删除。但该标记在检索期是否被执行从未被检验。测量 5 个系统：加载被撤销的策略及其替代品，追踪被撤销事实是否被返回。
- **关联度:** ★★★★ 「删了但还在被用」——k 若在知识库/记忆里做纠正或红线撤销，需要验证检索端真的过滤；对闲鱼交付中「客户要求撤回某内容」的场景同样适用

### 4. Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent Coherence in LLMs

- **ID:** [2609.10413v1](https://arxiv.org/abs/2609.10413v1) | [📄 PDF](https://arxiv.org/pdf/2609.10413v1)
- **作者:** Ansuman Mullick, Eray Tüzün
- **分类:** cs.AI
- **摘要:** 现有 LLM 记忆系统把所有个人事实一视同仁，存储无限增长、检索精度退化。核心是生命周期管理：哪些记忆该持久、哪些该替换、以什么速率，取决于每条事实的行为类型。Fortunate Recall 是可组合策略层，把个人事实分类成 10+1 行为本体并按类型应用生命周期策略。
- **关联度:** ★★★★ 记忆生命周期治理——k 的记忆条目管理（合并/替换/淘汰）可套「按行为类型定生命周期」的策略层；与 memory 工具的字符预算治理直接相关

### 5. Graph-Based Personalized Memory for LLM Agents: Representation, Evolution, Retrieval, and Evaluation

- **ID:** [2609.08599v1](https://arxiv.org/abs/2609.08599v1) | [📄 PDF](https://arxiv.org/pdf/2609.08599v1)
- **作者:** Dac Duy Anh Nguyen, Zhangchi Qiu, Shigeng Chen, Alan Wee-Chung Liew
- **分类:** cs.AI
- **摘要:** LLM agent 从单会话工具进化为长期个人助理，记忆成为个性化的核心需求（用户偏好/目标/约束/关系/过往经验逐步累积且随时间变化）。本文给出图基个性化记忆的框架视角：表征、演化、检索与评估四段式。
- **关联度:** ★★★★ 图基记忆=知识图谱式 agent 记忆——k 的 Obsidian 图谱/知识库治理方向一致；「表征-演化-检索-评估」四段式是设计记忆系统的完整 checklist

---

## 二、Agent 技能与自进化（4 篇）

### 6. Grounded Skill Synthesis from Code at Scale for Agentic Intelligence

- **ID:** [2609.05571v1](https://arxiv.org/abs/2609.05571v1) | [📄 PDF](https://arxiv.org/pdf/2609.05571v1)
- **作者:** Yongqi Tong, Pan Wang, Hang Wang, Jianshe Li, Xin Zhang, Jiang-Ming Yang, Wei Wu
- **分类:** cs.CL, cs.SE
- **摘要:** 可复用技能给 agent 迁移性程序知识，规模化获取是关键。轨迹合成需与特定环境交互；文档派生技能缺乏可执行证据与验证。源码是互补路径：无需先验 agent 经验，从代码大规模合成有执行证据的技能。
- **关联度:** ★★★★★ 从源码合成可执行技能——k 维护大量技能，若技能能从代码库自动合成/验证，「可执行证据」比文档更可靠；对 document-to-skill 蒸馏是直接升级路径

### 7. SkillAdam: Stable and Efficient Skill Evolution for Agents

- **ID:** [2609.08944v1](https://arxiv.org/abs/2609.08944v1) | [📄 PDF](https://arxiv.org/pdf/2609.08944v1)
- **作者:** Gaoyuan Li, Meihao Fan, Yizhe Liu, Shaolei Zhang, Ju Fan, Siyi Wang, Jiaheng Hou, Xudong Weng, Honghan Tian, Zang Li
- **分类:** cs.AI
- **摘要:** 技能是给冻结模型 agent 装领域知识/程序性指导的轻量方式，但高质量技能获取贵且难规模化。专家手写费力；近期技能自进化方法用执行反馈迭代修订技能，但启发式更新策略不稳定。SkillAdam 把技能演化做成稳定高效的可优化过程。
- **关联度:** ★★★★ 技能演化优化器——k 的技能进化（skill-evolution）目前靠人工/启发式；SkillAdam 的「把技能更新本身当优化目标」是稳定化方向

### 8. Subagents vs Agent Skills: Executing Reusable Knowledge for Long-Horizon Agentic Tasks

- **ID:** [2609.09233v1](https://arxiv.org/abs/2609.09233v1) | [📄 PDF](https://arxiv.org/pdf/2609.09233v1)
- **作者:** Wasu Top Piriyakulkij, Rachel Lawrence, Alicia Curth, Sushrut Karmalkar, Niranjani Prasad
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** 语言模型 agent 如何有效利用可复用知识库解决长程任务？技能通常被表示为技能包（含指令/脚本/资源的多文件捆绑），执行方式有两类：把技能指令加载进 agent 上下文 vs 派 subagent 执行。系统对比两种执行方式。
- **关联度:** ★★★★ 「技能包执行方式之争」——k 的 Hermes 技能系统是「加载指令」模式；subagent 执行模式（delegate_task 已有雏形）对长程/资源密集技能是另一个选项，需按任务类型选

### 9. Closing the Consistency Gap: Self-Evolving Agents That Learn to Stay on Course

- **ID:** [2609.08832v1](https://arxiv.org/abs/2609.08832v1) | [📄 PDF](https://arxiv.org/pdf/2609.08832v1)
- **作者:** Evelyn Duesterwald, Benjamin Elder, Lilian Ngweta, Shashanka Ubaru, Malgorzata Zimon
- **分类:** cs.AI
- **摘要:** LLM agent 平均准确但生产不可靠：同一任务给 ReAct agent 跑 5 次（GPT-4.1、AppWorld），全 5 次成功的概率只有 53%，单次通过率却平均 77%——24 个百分点的「一致性缺口」。主张自进化 agent 学习保持航向。
- **关联度:** ★★★★ 「平均准≠可靠」——k 做自动化流水线时「跑一次成功」远不够；一致性缺口是交付质量门（service-quality）的量化参照

---

## 三、编码 Agent 安全（3 篇）

### 10. Authority Is Not a String: A Capability-Scoped Harness for Prompt-Injection-Resistant Coding Agents

- **ID:** [2609.08371v1](https://arxiv.org/abs/2609.08371v1) | [📄 PDF](https://arxiv.org/pdf/2609.08371v1)
- **作者:** Dimitrios Stamatios Bouras, Yihan Dai, Sergey Mechtaev
- **分类:** cs.SE
- **摘要:** 编码 agent 用系统级工具读写文件、执行命令、改源码。沙箱内工具常带「环境权限」：点名资源即可操作。间接提示注入正是利用这一点：仓库文件或工具输出里的指令让 agent 做用户没要求的事。提出 CapScope，能力作用域 harness。
- **关联度:** ★★★★★ 编码 agent 权限最小化——k 用 Codex/Claude Code 处理不可信仓库时，「能力作用域」比「提示词防线」可靠；可直接借鉴到 k 的代码委派安全基线

### 11. Scanning the Harness: An Empirical Study of Supply-Chain Defects in AI Coding-Agent Configurations

- **ID:** [2609.07360v1](https://arxiv.org/abs/2609.07360v1) | [📄 PDF](https://arxiv.org/pdf/2609.07360v1)
- **作者:** Benjamin Kapner, Carmel Soceanu, Alicia Petrunin, Hofni Gartner
- **分类:** cs.CR, cs.SE
- **摘要:** Claude Code、Cursor、GitHub Copilot、OpenAI Codex 都通过开发者编写/分享的工件配置：指令文件、技能、hooks、MCP server 声明、subagent。这个 harness 是从市场与公共仓库安装的依赖层，以开发者权限运行，没有 lockfile、没有安装期检查、没有组件词汇表。实证研究配置供应链缺陷。
- **关联度:** ★★★★★ 正是 k 的处境——k 从市场安装第三方技能/接 MCP；这篇定义了「技能供应链无 lockfile」问题，skill-installer / external-skill-installation 应加安装期校验与来源检查

### 12. An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks

- **ID:** [2609.09404v1](https://arxiv.org/abs/2609.09404v1) | [📄 PDF](https://arxiv.org/pdf/2609.09404v1)
- **作者:** Viet K. Nguyen, Mohammad I. Husain
- **分类:** cs.AI, cs.CR
- **摘要:** Agentic AI 框架让 LLM 规划、持记忆、调用能触及真实文件/邮件/服务的工具。多数 agent 还读图，攻击者可绕开用户把文本塞进 agent 上下文。MMPIBench 可复现基准：通过 6 种视觉载体（OCR 文本、覆盖等）投放固定攻击集，测攻击后果。
- **关联度:** ★★★★ 多模态注入攻击面——k 的 AI 图片/多模态服务若接入 agent 流程，读图=注入通道；基准方法可复用于自建服务的红队

---

## 四、Agent 评测可靠性（3 篇）

### 13. The Double Measurement Confound in Agent Benchmarks: De-Scaffolding, Ground-Truth Scoring, and Reliability Beyond the Mean

- **ID:** [2609.09218v1](https://arxiv.org/abs/2609.09218v1) | [📄 PDF](https://arxiv.org/pdf/2609.09218v1)
- **作者:** Yonghong Zhang, Shadi Motaali, Vu Phong Dinh, Avin Piroutiniya, Jorge E. López de Vergara, Luis de Pedro, Ricardo Correia, Isabel M. Parra, Yong Xie
- **分类:** cs.SE
- **摘要:** agent 基准用于比较 LLM 和指导部署决策，但分数只在「测的是模型能力而非评测管线属性」时才有意义。识别双重测量混杂：执行关键决策由固定 scaffold 完成（模型没做），而评分器用未让模型执行的判据打分。
- **关联度:** ★★★★★ 评测方法论核心——k 自建评测/看榜选模型时，「scaffold 替模型干活」会让分数虚高；de-scaffolding 是读榜第一原则

### 14. Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts

- **ID:** [2609.08236v1](https://arxiv.org/abs/2609.08236v1) | [📄 PDF](https://arxiv.org/pdf/2609.08236v1)
- **作者:** Yongxi Zhou, Wenbo Ye, Yuanzhe Liu, Zihan Dong, Junwei Yao
- **分类:** cs.AI
- **摘要:** 自动安全判官（Llama Guard、GPT-4o 打分 prompt）产出几乎所有越狱成功率/防御评估/安全榜的数字。问：判官评的是内容还是语气？保持回复内容不变，加内容无关的风格包装（固定字符串前缀等），判官判定被翻转。
- **关联度:** ★★★★★ LLM judge 的脆弱性——k 用 judge 做评测/质检时，表面风格会翻转判定；评测设计要控制风格无关变量（延续 09-09「评测反应性」主线）

### 15. What Does an LLM-Agent Leaderboard Rank Actually Compare?

- **ID:** [2609.07785v1](https://arxiv.org/abs/2609.07785v1) | [📄 PDF](https://arxiv.org/pdf/2609.07785v1)
- **作者:** Wei-Jung Huang
- **分类:** cs.AI
- **摘要:** agent 排行榜邀请一个自然推断：排上面的 agent 就是更好的。当系统在任务混合、标签来源、发布细节、成本规则上不同时，公开评测日志可能不支持该结论。研究排行榜分数在估计什么、何时能支持成对优劣结论，给出 estimand-aware 成对流程。
- **关联度:** ★★★★ 读榜方法论——k 选模型/服务看榜时，「可比性」要先声明；成对比较 + 测量目标明确是防被榜误导的做法

---

## 五、对齐与安全（4 篇）

### 16. How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE

- **ID:** [2609.09793v1](https://arxiv.org/abs/2609.09793v1) | [📄 PDF](https://arxiv.org/pdf/2609.09793v1)
- **作者:** Yi Shi, Tanyu Chen, Kai Shen
- **分类:** cs.AI, cs.CL, cs.CR, cs.LG
- **摘要:** 方向消融通过把「拒绝方向」从写残差流的权重中投影出去来移除对齐模型的拒绝能力。无需梯度训练/优化，只需几百个对比提示——是开源权重对齐的经典白盒攻击。此前只在 ~70B 以内的稠密模型验证过，本文首次推到 320B MoE 前沿尺度。
- **关联度:** ★★★★★ 对齐脆弱性的规模实证——「几百个提示即可移除拒绝」对 k 依赖开源权重模型做本地部署/服务是硬风险提示；防御与检测方向值得跟进

### 17. Difficulty-Adaptive Tree-Structured Policy Optimization for Expanding Reasoning Coverage in RLVR

- **ID:** [2609.08650v1](https://arxiv.org/abs/2609.08650v1) | [📄 PDF](https://arxiv.org/pdf/2609.08650v1)
- **作者:** Youngjun Yu, Sanghwan Jang, Hwanjo Yu
- **分类:** cs.AI, cs.CL, cs.LG
- **摘要:** RLVR 是大推理模型成功的关键，但显著提升单样本准确率的同时常因训练期探索不足无法扩展内在推理覆盖（pass@k）。分析训练期 rollouts 的结构设计对 pass@k 的影响，用难度自适应的树结构策略优化来扩展探索。
- **关联度:** ★★★★ pass@k 训练视角——k 若用 RLVR/GRPO 系列训练/微调推理模型，覆盖度比单样本准确率更接近真实能力；树结构 rollout 是低成本扩展探索的选项

### 18. Spillover-Aware Multi-Value Steering for Pluralistic LLM Alignment

- **ID:** [2609.05800v1](https://arxiv.org/abs/2609.05800v1) | [📄 PDF](https://arxiv.org/pdf/2609.05800v1)
- **作者:** Weici Pan, Xander Barron, Jiawei Zhou, Zhenhua Liu
- **分类:** cs.AI
- **摘要:** 激活 steering 在推理期控制 LLM 行为，但现有方法一次只处理一个概念。多元对齐需要同时 steering 多个维度。朴素 steering 产生大量溢出：为一个值设计的效果泄漏进其他值。提出溢出感知的多值 steering。
- **关联度:** ★★★★ 多值同时控——k 的 AI 人设/风格控制若用 steering，单方向会互相污染；「溢出感知」提示方向设计要正交化

### 19. Steering Under Compression: Dose-Response, Capability Cost, and Failure Asymmetry in Quantized LLMs

- **ID:** [2609.06473v1](https://arxiv.org/abs/2609.06473v1) | [📄 PDF](https://arxiv.org/pdf/2609.06473v1)
- **作者:** Saurav Bhandari, Benjamin Wade
- **分类:** cs.LG
- **摘要:** 推理期激活 steering 无需改参数即可控制行为，post-training 量化降低部署内存/计算。两者在实践中日益汇合，但其交互从未被刻画。系统研究 weight-only 量化（INT8/NF4）下的激活 steering，跨 4 个模型：剂量-反应、能力代价、失败不对称。
- **关联度:** ★★★★ 量化×steering——k 本地跑量化模型（4060 8GB），若叠加 activation steering 控制，需预知量化后 steering 的能力代价不对称

---

## 六、编码 Agent 与软件工程（3 篇）

### 20. ExecCritic: Learn to Test, Test to Improve for Coding Agents

- **ID:** [2609.09133v1](https://arxiv.org/abs/2609.09133v1) | [📄 PDF](https://arxiv.org/pdf/2609.09133v1)
- **作者:** Leitian Tao, Baolin Peng, Haorui Wang, Hang Wang, Hao Cheng, Wenlin Yao, Qianhui Wu, Tao Ge, Sharon Li, Jianfeng Gao
- **分类:** cs.AI, cs.CL, cs.SE
- **摘要:** 执行反馈能引导编码 agent 正确修仓库，但只在测试捕获 issue 请求的行为时有效。agent 生成的测试可能编码不完整/错误的行为目标；同一条轨迹既写补丁又写测试时，错误会互相一致、制造虚假信心。ExecCritic 组合 test-verify-revise scaffold 与角色分离 critic。
- **关联度:** ★★★★ 「测试与补丁同源=假信心」——k 用编码 agent 修 bug 时，critic 与 patch 分离是防止「自证清白」的关键；对 Codex/Claude Code 委派流程可加独立验证步

### 21. FrogNano: Training a 4B Coding Agent via Online Task Synthesis

- **ID:** [2609.07925v2](https://arxiv.org/abs/2609.07925v2) | [📄 PDF](https://arxiv.org/pdf/2609.07925v2)
- **作者:** Minseon Kim, Zhengyan Shi, Emiliano Penaloza, Christopher Cui, Roger Creus Castanyer, Maryam Hashemzadeh, Isadora White, Jonathan Light, Jeonghye Kim, Matheus Pereira, Darya Moldavskaya, Chinmay Singh, Fabio Vera, Baolin Peng, Xingdi Yuan, Marc-Alexandre Côté, Alessandro Sordoni
- **分类:** cs.AI
- **摘要:** 4B 编码 agent，面向资源受限环境高效解决 SWE 任务。只用 RL 在约 1,500 个合成任务 SWE 环境上 post-train。关键成分是 online task synthesis 流水线：创建贴合当前 checkpoint 可学习性前沿的任务。
- **关联度:** ★★★★ 小模型+在线任务合成——k 的 4060 8GB 若能跑 4B 级 coding agent，FrogNano 是「小模型通过合成任务 RL 追平大模型」的路线证据

### 22. Φ-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?

- **ID:** [2609.10226v1](https://arxiv.org/abs/2609.10226v1) | [📄 PDF](https://arxiv.org/pdf/2609.10226v1)
- **作者:** Leilei Ding, Shumin Wang, Yuting Huang, Fanqi Wan, Yinmin Zhang, Qi Han, Yiming Xu, Feiyuan Zhang, Xiaomeng Chu, Guoliang You, Wuyang Zhang, Daxin Jiang, Yanyong Zhang
- **分类:** cs.CL
- **摘要:** LLM 展示了推理与代码生成能力，能否帮助开发/优化「支撑它们的基础设施」？既有基准聚焦孤立 kernel、预定义算子、预指定优化目标，无法测 LLM 做开放式、长程的基础设施工程。Φ-Bench 提出新基准。
- **关联度:** ★★★★ 「LLM 自研基建」命题——与 k 的 Hermes 自举/知识吸收主线同构；基准设计（开放式长程而非孤立 kernel）对 k 评模型「能不能干活」有参考

---

## 七、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.05435](https://arxiv.org/abs/2609.05435v1) | AhaBench: Do Agents Learn from Prior Experience? | agent 是否从过往经验中学习的长程持续学习基准：固定模型收到有用经验后，后续行为在相关任务上是否真的改善——「经验复用」评测补盲区 |
| 2 | [2609.06059](https://arxiv.org/abs/2609.06059v1) | DAREBench: Deployment-Aware and Reliable Evaluation of Models as Agents | 部署感知的「模型作为 agent」评测：多模态感知/多步执行/工具使用/工件交付，跨任务类型可比性与可靠性 |
| 3 | [2609.08149](https://arxiv.org/abs/2609.08149v1) | SWE-Bench Pro Verified | 审计 SWE-Bench Pro 的两类不可靠源：金标泄漏导致的 reward hacking + 任务质量缺陷，给出修正版基准 |
| 4 | [2609.09875](https://arxiv.org/abs/2609.09875v1) | AgentAudit: Full-Lifecycle Trust Evaluation of AI Agents | 全生命周期信任评估框架：跨规划/工具选择/工具执行/记忆/推理十项能力审计执行轨迹，定位失败精确来源 |
| 5 | [2609.05901](https://arxiv.org/abs/2609.05901v1) | From Review to Authorization: Key-Isolated Signing for LLM Agents | 密钥隔离签名架构：个人密钥与阈值签名密钥隔离，「评审→授权」分离，防提示注入跨判断边界触及执行权 |
| 6 | [2609.05512](https://arxiv.org/abs/2609.05512v1) | Reasoning-Aware Compression | 推理感知压缩：识别并保护易损推理电路，量化条件下测 GSM8K/MATH-500 等五基准+GPU 能耗——k 4060 跑量化模型直接相关 |
| 7 | [2609.08189](https://arxiv.org/abs/2609.08189v1) | HeRo: History-Aware Routing for Efficient LLM Inference | 动态层路由需要记忆吗：历史感知路由让 skip 决策考虑路径依赖，提升推理效率 |
| 8 | [2609.08186](https://arxiv.org/abs/2609.08186v1) | Does Deeper Reasoning Compromise Alignment? | 深度推理可能诱发对齐崩塌：挑战「推理越深越安全」共识，量化 LRM 对齐机制在长推理下的稳定性 |
| 9 | [2609.09647](https://arxiv.org/abs/2609.09647v1) | Black-Box Red Teaming of Agentic AI | 黑盒 agent 红队框架：只给系统基础描述，taxonomy 驱动自动风险发现，覆盖多步 agent 漏洞 |
| 10 | [2609.08016](https://arxiv.org/abs/2609.08016v1) | A Layered Analysis of Disagreement in Multi-Agent LLM Debate | 分层分析多 agent 辩论的「分歧-质量」机制：报告的分歧≠文本实际反驳≠立场持续，4 个测量量拆穿假设 |
| 11 | [2609.07731](https://arxiv.org/abs/2609.07731v1) | The Profit Alignment Problem | 「利润对齐问题」：3,600 次对照试验中，加「最大化盈利」指令让 LLM 系统性把模棱两可的安全信号判为无风险（+6.8pp） |
| 12 | [2609.09769](https://arxiv.org/abs/2609.09769v1) | XAgent: Execution-Guided GitHub Issue Resolution | 执行引导的 GitHub issue 定位与解决：不只依赖静态 issue 描述，用执行反馈纠正定位偏差 |
| 13 | [2609.10248](https://arxiv.org/abs/2609.10248v1) | A-JIT: Agentic Just-In-Time Software Construction | Agentic 即时软件构造：用「代码+运行时 harness+嵌入式 agent」替代静态二进制，软件可随需求持续演化 |
| 14 | [2609.07051](https://arxiv.org/abs/2609.07051v1) | TrojanWorld: Backdooring World-Model Agents | 世界模型 agent 后门：通过「想象引导」投毒模型基 agent，暴露预训练世界模型供应链风险 |
| 15 | [2609.08765](https://arxiv.org/abs/2609.08765v1) | Benchmark Scores Are Pipeline-Dependent | 8 个网安 LLM 基准 × 10 模型审计：单个管线选择可改变模型排名/分数，识别 15 类系统失败模式 |
| 16 | [2609.05677](https://arxiv.org/abs/2609.05677v1) | Who Maintains Agent Skills? | 技能维护的纵向研究：人工治理+AI 辅助的技能维护实践，划出自动化技能策展的边界 |

---

## 今日要点（主题信号）

1. **Agent 记忆成为独立工程学科**：05510 以单条 Claude Code 会话线运行 7 个月、驱动 63.3 万行代码库的运维经验谈「记忆即基础设施」；05441 指出既有记忆评测（LoCoMo/LongMemEval）测的是对话回忆而非「记忆是否改变 agent 行为」，给出成本感知新基准 MERIT；08258 实证 5 个 agent 记忆系统的「软撤销」在检索期几乎不被执行。记忆的可靠性、成本、撤销语义三条线同时成熟。
2. **技能供应链（Skill Supply Chain）成为安全焦点**：07360 把 Claude Code/Cursor/Codex 的配置工件（skills/hooks/MCP server 声明）定义为无 lockfile、无安装期校验的依赖层；08371 提出能力作用域 harness（CapScope）抗间接提示注入；05901 用密钥隔离把「评审」与「授权」分离。对应 k 装第三方技能/接 MCP 的实际风险面。
3. **Agent 基准评测进入「去脚手架」时代**：09218 指出执行关键决策由固定 scaffold 完成而评分却算在模型头上（双重测量混杂）；08236 证明加内容无关的风格包装就能翻转 LLM 安全判官的判定；07785 质疑排行榜排名的可比较性。评测管线的可靠性成为比「模型能力」更优先的问题。
4. **安全对齐在超大 MoE 上的脆弱性被实证**：09793 把 refusal direction 消融攻击首次推到 320B MoE——单方向投影即可移除拒绝能力；06473 发现激活 steering 在量化模型上能力代价不对称。对齐-压缩-推理三者的交互成为新研究面。
5. **技能自进化从「启发式补丁」走向「稳定优化器」**：08944 SkillAdam 把技能更新当可优化过程；09233 系统对比 subagent 执行 vs 技能内联执行两种可复用知识执行方式；05571 从源码大规模合成可执行技能（免交互环境）。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Double Measurement Confound 2609.09218 | arxiv.org abs 页全文抓取 + web_search | ✅ 已确认（arXiv HTML 收录；跨源检索到同主题系列研究：2605.27898 统一评测框架、2606.08529 GAIA scaffold 对照、2607.22585 coding harness 40× token 差距，佐证主题活跃） |
| Memory as Infrastructure 2609.05510 | arxiv.org abs 页全文抓取 + web_search | ✅ 已确认（arXiv HTML 收录；跨源检索到同主题系列：2606.06448 agent memory 系统刻画、2605.26252 Is Agent Memory a Database、MemArchitect 治理层，佐证「记忆=基础设施」方向） |
| 其余 36 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **技能供应链审计**：07360「配置工件=无 lockfile 依赖层」+ 08371 CapScope——k 安装外部技能/接 MCP server 前，检查指令文件与 hooks 是否带提权能力；skill-installer / external-skill-installation 流程补一条「供应链检查」门禁（来源可信 + 无危险 hook + 权限最小化）
- 🔴 **记忆撤销语义检查**：08258 实证「软撤销在检索期不执行」——Hermes 记忆/知识库若做「删除/纠正」，确认检索端真的过滤，不只在存储端标 invalid（对应知识库治理与隐私红线）
- 🟡 **评测去脚手架自查**：09218 双重测量混杂 + 08236 风格包装翻转判官——k 自建评测/用 LLM judge 时，检查「关键决策是否由脚手架完成」「judge 是否被表面风格带偏」（延续 09-09「评测反应性」主线）
- 🟡 **量化模型 steering 代价预检**：06473 + 05512——k 4060 8GB 本地跑量化模型若用 activation steering，注意能力不对称（拒绝下降快于能力保持）；压缩时优先保护推理电路
- 🟢 **待深读**：05510 Memory as Infrastructure（真实数月长会话记忆工程）、09218（agent 基准方法论）、08371/07360（技能供应链安全）→ core-contributions 候选

---

*本速览由 cron 自动生成：09-10 索引解冻（list 页出现 09-09/09-10 新分组，09-09 含 1,303 篇疑似合并 09-08）→ 新窗口 1,749 唯一 base ID（与 covered 537 零重叠）→ 标题粗筛 278 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选（22 主条目 + 16 简评）→ 元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
