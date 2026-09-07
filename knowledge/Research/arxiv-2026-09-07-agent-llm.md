---
aliases:
  - arxiv-2026-09-07-agent-llm
  - arxiv-agent-llm-2026-09-07
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-07
updated: 2026-09-07
status: adopted
source: arxiv.org list pages + abs pages（API 429 限流期间，HTML 路由）
---

# arXiv AI Agent / LLM 速览 — 2026-09-07

> **检索时间**: 2026-09-07 GMT+8
> **新窗口**: 索引解冻——export.arxiv.org API 持续 429 限流(HTML 路由),list 页出现 **2026-09-07 新分组 480 篇**(09-05/06 周末提交并入周一池),与 covered_ids 比对 **0 重叠**(全新窗口)。6 类别 recent 全量 → 标题粗筛 97 候选 → 人工剔除领域应用(交通/医疗/金融/能源/零售等)→ 逐篇抓 abs 页精选 **22 主条目 + 10 简评**。
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、Harness / 编码 Agent（4 篇）

### 1. What Does Multi-Harness RL Learn? Credit Assignment and Portability in Coding Agents

- **ID:** [2609.04518v1](https://arxiv.org/abs/2609.04518v1) | [📄 PDF](https://arxiv.org/pdf/2609.04518v1)
- **作者:** Chenqian Le 等（6 人）
- **分类:** cs.AI
- **摘要:** Agent RL 越来越多跑在完整执行 harness 上,multi-harness 配方混了两个选择:把策略暴露给多个 harness、在同一个 relative-advantage 组里比较它们的 reward。本文在仓库级编码上把第二个选择单独隔离:从单个 Qwen3-8B 监督微调起点出发,用同一批冻结的 task-harness 记录(Aider / OpenHands / Qwen Code / SWE-agent)以相同更新步数回放,在 GRPO 的 **Within**(每个 task-harness 对一组)与 **Cross**(task 内 harness 合并)两种归组规则下训练,给每个 checkpoint 打分——分离「credit assignment 怎么做」对编码 agent 可迁移性的影响。
- **关联度:** ★★★★★ 跨 harness RL 的 credit assignment——k 若做多后端(Codex/OpenCode/Claude Code)的 RL/微调,Within vs Cross 归组是直接影响学习效率的设计决策;与 09-06 的 Harness Engineering(00006)同属 harness 研究主线

### 2. RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents

- **ID:** [2609.04898v1](https://arxiv.org/abs/2609.04898v1) | [📄 PDF](https://arxiv.org/pdf/2609.04898v1)
- **作者:** Aziz Ben Amor 等（7 人）
- **分类:** cs.CL, cs.AI
- **摘要:** 仓库级重构要求编码 agent 把一个变更跨多文件传播且不改变程序行为,但现有 harness 没有一个能隔离决定 agent 成败的设计轴。**RefactorPlatform** 是开源受控评估 harness:固定环境、逐轴显式变化——模型 backbone(经 OpenRouter 与 GitHub Copilot CLI)、执行体制(baseline / retrieval-augmented / multi-agent)、prompt 具体度;每次运行在隔离工作区、实时终端流、逐任务记录 token/diff。
- **关联度:** ★★★★ 「固定环境、单轴变化」的受控评估范式——k 评编码 agent 产出时,RefactorPlatform 三轴设计可直接迁移为验收矩阵;开源 harness 本身是可复用评估基建

### 3. How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method

- **ID:** [2609.05274v1](https://arxiv.org/abs/2609.05274v1) | [📄 PDF](https://arxiv.org/pdf/2609.05274v1)
- **作者:** Konstantin Grotov, Valentin Malykh
- **分类:** cs.LG
- **摘要:** 部署在软件工程的 LLM agent 失败代价昂贵:自信地犯错,坏动作要等昂贵的执行与重试后才被发现。**Speculative Uncertainty (SU)** 只从输出 token 恢复黑盒 agent 的预测性失败信号——不需要 logits/权重/激活/重复采样。反着用 speculative decoding:小开放权重 draft model 对 agent 已生成的轨迹做单次前向打分,从 speculative cross-likelihoods 分离 reasoning 与 action 片段、提取 phase-aware 特征并校准——即「用便宜模型给昂贵 agent 的每条动作线即时预警」。
- **关联度:** ★★★★ 低成本失败预警门——k 的长任务自动化若加一道「draft-model gate」可在坏动作落地前拦下;与 09-06 的 00038(outcome-only judge 盲区)互补,这是执行前/执行中的预测信号

### 4. Reviewer Capability Governs Rejection Targeting, Not Repair Skill

- **ID:** [2609.04270v1](https://arxiv.org/abs/2609.04270v1) | [📄 PDF](https://arxiv.org/pdf/2609.04270v1)
- **作者:** Faizan Tanveer
- **分类:** cs.SE, cs.CL, cs.MA
- **摘要:** 多 agent LLM 流水线常用不同能力档次的模型分派执行与验证角色(旗舰模型跑每阶段太贵)。既有文献已知验证阶段不总是有益,但把 reviewer 能力大致固定在与 executor 同档。本文变化它:用覆盖能力范围、直到完全解不了题的模型替换 reviewer,测量每次单独 rejection 的结果——发现 reviewer 能力决定的是「**拒错**(rejection targeting)」而不是「**修对**(repair skill)」。
- **关联度:** ★★★★ 委派中的角色-能力匹配实证——k 编排多 agent 流水线(执行/审查分层)时,「审查者能力决定拒错还是修复」是关键角色设计变量;与 09-06 的 00267 授权、委派主线呼应

---

## 二、Agent 安全（4 篇）

### 5. HackProbe: Harness-agnostic Detection and Immunization of Reward Hacking

- **ID:** [2609.04665v1](https://arxiv.org/abs/2609.04665v1) | [📄 PDF](https://arxiv.org/pdf/2609.04665v1)
- **作者:** Rongxin Yang 等（13 人）
- **分类:** cs.AI
- **摘要:** 自进化语言模型靠「提出候选更新、保留能提高可见分数的」来进步;当那个分数是想要能力的次优代理时,持续选择会拉大两者差距——这就是 reward hacking。**HackProbe** 是挂到任意自进化循环上的监视器:两个黑盒 hook,不看权重与激活;维护一个**秘密的、分布固定的比较核心**(frozen distribution 让能力代理跨代可比),外加轮换的新鲜层捕捉跨代漂移——即 harness 无关的 reward hacking 检测与免疫。
- **关联度:** ★★★★★ 自进化/RLVR 的 reward hacking 检测——k 若跑任何「按分数选改进」的自我改进流程,HackProbe 的「秘密冻结比较核心」是防投机取巧的通用设计;与 09-06 的 01519(构造效度)同属「分数不可信」主线

### 6. CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls

- **ID:** [2609.05269v1](https://arxiv.org/abs/2609.05269v1) | [📄 PDF](https://arxiv.org/pdf/2609.05269v1)
- **作者:** Chris Zheng, Geng Yang
- **分类:** cs.CR, cs.AI
- **摘要:** LLM agent 系统越来越常组合溯源、授权、策略执行、协议适配器与执行控制,但「各自正确的安全机制」未必组合成端到端安全系统:安全关键上下文在跨组件边界时可能被丢弃、放宽、重绑或重解释——称之为 **security-context discontinuity**。**CONTINUITY** 提出可验证的安全控制组合框架:给每个组件建模、以契约形式保证安全上下文跨边界组合后不被破坏。
- **关联度:** ★★★★★ 「组合安全 ≠ 组件安全之和」——k 的多 agent 编排(溯源/授权/策略/适配器叠加)直接命中:安全上下文跨边界必须显式契约化;与 09-06 的 00267(授权 broker)、01035(风险 vesting)构成安全组合主线三连

### 7. Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents

- **ID:** [2609.04875v1](https://arxiv.org/abs/2609.04875v1) | [📄 PDF](https://arxiv.org/pdf/2609.04875v1)
- **作者:** Chao Yao 等（8 人）
- **分类:** cs.CR, cs.AI
- **摘要:** 长运行 LLM agent 是有状态的:除 transcript 外还累积压缩摘要、明文记忆、待办工具计划,以及每个 serving API 下的 KV cache。今天的「forget」操作删一条明文记忆记录就停,把从被撤销信息派生的所有工件留在原地。本文形式化 **execution-state unlearning**:forget 请求后 agent 必须表现得像从未见过目标。把运行时建模为确定性转移系统,证明 pre-target 轨迹前缀与反事实世界免费共享、post-target 后缀不可恢复——「不重启地抹除执行状态」。
- **关联度:** ★★★★★ agent 的「真忘记」——k 的记忆/知识库若有敏感信息撤回需求,execution-state unlearning 给出「派生工件一起抹除」的正式框架;与 09-06 的 00546/01235 记忆主线、合规场景直接相关

### 8. Rethinking Indirect Prompt Injection as a Test-Time Search Problem

- **ID:** [2609.04495v1](https://arxiv.org/abs/2609.04495v1) | [📄 PDF](https://arxiv.org/pdf/2609.04495v1)
- **作者:** Duong M. Nguyen, Joon Sik Kim, Blazej Manczak, Vaikkunth Mugunthan
- **分类:** cs.AI, cs.CL, cs.CR
- **摘要:** 把间接 prompt 注入重表述为在「环境、用户任务、注入任务」共同决定的攻击面上的 **test-time 搜索**。为落地,提出带专用搜索 harness 的 **agentic attacker**:环境侦察、对攻击策略结构化推理、用 victim-agent 反馈做自适应评估。跨异构任务发现:增加 attacker 的 test-time compute 会提高漏洞发现率——「注入攻击能力随推理预算增长」。
- **关联度:** ★★★★★ IPI 是 agent 接外部内容(网页/工具输出)的头号风险——「攻击者也是带预算的 agent」说明安全评估要按 attacker compute 分级;与 09-06 的 HookPry、00267 同属 agent 安全主线

---

## 三、Agent 记忆（3 篇）

### 9. Does Your Agent's Memory Survive a Model Upgrade? A Controlled Study of Memory Portability

- **ID:** [2609.05339v1](https://arxiv.org/abs/2609.05339v1) | [📄 PDF](https://arxiv.org/pdf/2609.05339v1)
- **作者:** Ankit Goyal, Jaideep Ray
- **分类:** cs.AI, cs.CL, cs.IR
- **摘要:** 模型升级是常态、记忆迁移不是:agent 可以保留同一份记忆存储却仍然「忘记」——新模型可能用不同方式解读旧笔记、混合 embedding 版本可能弄坏检索、修复时缺原始证据。在相同历史**逐字保留**(long-context)、**分块 RAG**、**模型压缩成自然语言笔记**、**固定 schema 知识图谱**四种表示下对照记忆表现——「升级模型后,同库记忆还认不认」的受控研究。
- **关联度:** ★★★★★ 直击 k 的跨模型/升级场景:记忆可移植性 = 表示形式 × 检索栈的联合问题;与 09-06 的 00546(运行时无关持久 agent)、跨 agent 记忆设计直接相关——「模型升级 ≠ 记忆无缝」

### 10. Compact-Memory LLM Agents via Online Max-Member Clustering and Atom-Aware Packing

- **ID:** [2609.04915v1](https://arxiv.org/abs/2609.04915v1) | [📄 PDF](https://arxiv.org/pdf/2609.04915v1)
- **作者:** Jiahe Geng, Jinpeng Wang, Kun Yuan
- **分类:** cs.AI
- **摘要:** 长程 LLM 部署常面临紧 prompt 预算:延迟、成本与上下文限制使全上下文提示不现实。关键问题不是原始 recall,而是紧凑记忆体制下「什么记忆设计给出最好的质量-token 权衡」。**RSM-full** 是在线聚类记忆流水线:cosine 门控 **max-member merge** 写入规则 + **atom-aware** 分组上下文打包器,在 AMA-Bench 上以约 3/… 的 token 达到 Full-Context 质量的 83%——紧凑记忆的质量-token Pareto 点。
- **关联度:** ★★★★ 记忆压缩的质量-token 权衡——k 的成本/上下文敏感场景(墨题 RAG、长 agent 会话)可直接迁移「max-member merge + atom-aware 打包」;与 09-06 记忆主线并列工程侧

### 11. ICM-Bench: Person-Level Identity Reasoning in Multimodal Agents with Long-Term Memory

- **ID:** [2609.04438v1](https://arxiv.org/abs/2609.04438v1) | [📄 PDF](https://arxiv.org/pdf/2609.04438v1)
- **作者:** Shidu Ren 等（6 人）
- **分类:** cs.CV
- **摘要:** 长时多模态 agent 不仅该记得发生了什么,还要记得**谁**参与了——把重复出现的脸、声音、名字、人物相关物件、事件、社交关系跨时间关联到一致身份。现有长视频与多模态 agent 基准测宽泛记忆 QA,但没隔离「维持重复人物身份 + 跨时间关系推理」的能力。**ICM-Bench**(Identity-Centric Memory Benchmark)据称是第一个专门针对该能力的基准。
- **关联度:** ★★★★ 「人级身份推理」是长时记忆的缺失维度——k 的多模态/记忆 agent 若要记「谁」而不只是「什么」,ICM-Bench 的身份链路是设计参照

---

## 四、技能演化与编排（4 篇）

### 12. CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hierarchical Skill Evolution

- **ID:** [2609.04865v1](https://arxiv.org/abs/2609.04865v1) | [📄 PDF](https://arxiv.org/pdf/2609.04865v1)
- **作者:** Jinyuan Feng 等（7 人）
- **分类:** cs.AI
- **摘要:** 技能库让 LLM agent 复用程序性知识、提升 agentic RL 样本效率,但现有范式有结构性缺陷:要么把技能演化与策略优化解耦,要么把 meta-skill 实例化成固定工作流——都把技能当被动管理对象。**CoSkill** 是统一的多 agent RL 框架:把静态 meta-skill 工作流重铸为可演化结构,让技能演化与推理 agent 协同适应。
- **关联度:** ★★★★★ 「技能演化与策略优化联合」——直接映射 k 的技能自进化(skill-evolution/蒸馏链)与 RL 路线;与 09-06 的 01437(HarnessDev)同属「让 agent 自造/自演化组件」共识潮

### 13. From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents

- **ID:** [2609.04869v1](https://arxiv.org/abs/2609.04869v1) | [📄 PDF](https://arxiv.org/pdf/2609.04869v1)
- **作者:** Longtao Hu, Xiao Liang, Linchao Zhu
- **分类:** cs.AI
- **摘要:** Computer-use agent 能在图形界面执行复杂任务,但交互经验通常是瞬时的:一次 rollout 习得的程序性知识没有被系统化保留、精炼、复用于后续任务。既有技能库提供外部程序性知识,但其相对「无技能同一 agent」的增量价值与跨重复交互的纵向动态刻画不足。提出**在线技能演化框架**:把交互轨迹与评估器反馈转化为持久的、版本化的可复用技能库。
- **关联度:** ★★★★★ 「轨迹→持久技能库」的在线演化——正是 k 的「知识→技能」蒸馏方向(learn→research→apply);computer-use 场景与 k 的桌面/浏览器自动化直接相关

### 14. TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing

- **ID:** [2609.05019v1](https://arxiv.org/abs/2609.05019v1) | [📄 PDF](https://arxiv.org/pdf/2609.05019v1)
- **作者:** Tianxing Wang 等（7 人）
- **分类:** cs.AI
- **摘要:** Agent 倾向于在决定性运行结果出现前就优化/选择/约束执行结构,这种执行前承诺造成编排瓶颈:中间证据让待续路线失效时,agent 要么执行过时步骤、要么大范围重规划——错误累积、算力浪费、进度丢弃。**TROVE** 只修正被运行时证据否决的部分:离线把评估过的工作流搜索轨迹蒸馏为原子/复合技能与 outcome-conditioned 转移图,在线按证据增量修订。
- **关联度:** ★★★★ 「只重做被证据否决的部分」——k 的编排/规划流程可借鉴「路由验证 + 局部编辑」避免全盘重规划;与技能编排、harness 主线相关

### 15. Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents

- **ID:** [2609.05261v1](https://arxiv.org/abs/2609.05261v1) | [📄 PDF](https://arxiv.org/pdf/2609.05261v1)
- **作者:** Jiazheng Sun 等（5 人）
- **分类:** cs.AI, cs.SE
- **摘要:** LLM agent 越来越靠执行轨迹掌握复杂交互任务,但现有范式被浅层轨迹检索与扁平技能摘要卡住,忽略行为的时间依赖与 outcome-conditioned 拓扑。**Trace2Tower** 是 transition-aware EigenTrace 框架:把原始轨迹蒸馏为稳健技能层级——把 step 级交互抽象为规范事件,构建由语义兼容性/转移动态/outcome 证据共同约束的统一图,经对比谱方法提取多级技能。
- **关联度:** ★★★★ 轨迹→**层级**技能(而非扁平库)——k 的技能库若按「转移拓扑 + outcome 证据」组织成层级,检索与复用会更有结构;与 CoSkill/TROVE 构成技能主线

---

## 五、多智能体系统（3 篇）

### 16. DCFA: Dual-view Causal-inspired Attribution for Failure Reasoning in LLM-based Multi-agent Systems

- **ID:** [2609.04749v1](https://arxiv.org/abs/2609.04749v1) | [📄 PDF](https://arxiv.org/pdf/2609.04749v1)
- **作者:** Zehao Wang 等（5 人）
- **分类:** cs.AI
- **摘要:** 基于 LLM 的多 agent 系统增长快但仍脆弱,常出现推理与协调错误导致系统级失败。失败归因要追溯 agent 间自然语言交互找「**决定性错误**」(纠正最早动作即可反转失败)。两大挑战:浅层归因(只抓不完整检索等微小偏差)与深层因果追踪。**DCFA** 用双视角因果启发归因处理多 agent 失败推理。
- **关联度:** ★★★★ 多 agent 失败定位——k 调试多 agent 流水线(委派/编排)时「决定性错误 = 最早可反转动作」是实用排查框架

### 17. ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning via Outcome Reward Densifying

- **ID:** [2609.04648v1](https://arxiv.org/abs/2609.04648v1) | [📄 PDF](https://arxiv.org/pdf/2609.04648v1)
- **作者:** Shi-Qi Yan 等（6 人）
- **分类:** cs.CL
- **摘要:** RL 是 LLM 推理增强的主要范式,GRPO 及其变体用 outcome-level reward 表现强,但只依赖最终答案、不反馈哪些中间步骤促成成败。任务复杂、轨迹变长时稀疏最终奖励越来越不够。**ConsensusBench** 通过 **outcome reward densifying** 评测共识节点——把稀疏最终奖励稠密化,让中间步骤获得 credit。
- **关联度:** ★★★★ reward 稠密化/共识节点——k 跑 RLVR/GRPO 类训练时「中间步骤 credit 怎么分」是核心;与 04518 的 credit assignment 形成对照(前者 harness 归组、后者 reward 稠密化)

### 18. Testing Interchangeability in LLM Agent Teams

- **ID:** [2609.05279v1](https://arxiv.org/abs/2609.05279v1) | [📄 PDF](https://arxiv.org/pdf/2609.05279v1)
- **作者:** Jianxin Gao 等（5 人）
- **分类:** cs.AI, cs.MA
- **摘要:** 生产多 agent 系统不断替换 agent,假设是「填某个角色的 agent 与任何能干这活的 agent 可互换」。本文测试该假设:从同一基础模型独立组建每设定 8 个团队、每个 agent 在 10 个 formation episode 里持有私有笔记本,然后在团队间交换角色匹配的 agent,测 held-out 任务上的变化——对照 placebo 复现 roster 变动的扰动,分离「换人」与「换人带来的 disruption」。
- **关联度:** ★★★★ 「角色可互换性」实证——k 的多 agent 协作/委派若要动态换人(模型/agent 轮换),互换成本必须显式测量;直接映射 k 的模型 fallback/agent 轮换场景

---

## 六、评估基础设施与工具（2 篇）

### 19. Harbor Adapters and Harbor-Index: Infrastructure and a Curated Meta-Dataset for Large-Scale Agentic Evaluation

- **ID:** [2609.04298v1](https://arxiv.org/abs/2609.04298v1) | [📄 PDF](https://arxiv.org/pdf/2609.04298v1)
- **作者:** Lin Shi 等（80+ 人）
- **分类:** cs.AI, cs.CL
- **摘要:** 评估越来越多的 agentic benchmark 困难:它们常要求复杂环境与 agent 集成。**Harbor Adapters** 是统一的 agentic benchmark 评估基础设施:①开发把 **80+ benchmark** 移植到任意 agent 的适配器,经严格代码审查与 parity 实验验证;②跨能力档次的 **8 模型 × 54 benchmark** 大规模评估(每模型用 Terminus-2 与另一 harness 跑);③ curated meta-dataset(Harbor-Index)。
- **关联度:** ★★★★ 大规模 agentic 评估基建——k 做「评 agent」时,Harbor 的「适配器 + parity 验证」是评估复用的模板;与 09-06 的 01271(SNC profile)互补(基建 vs 内容)

### 20. SiLR: Structure-Preserving Admission and Process Reward for LLM Tool Agents

- **ID:** [2609.04629v1](https://arxiv.org/abs/2609.04629v1) | [📄 PDF](https://arxiv.org/pdf/2609.04629v1)
- **作者:** Chenyu Zhou 等（4 人）
- **分类:** cs.AI, cs.LG, eess.SY
- **摘要:** LLM 工具 agent 的运行时门通常被当成过滤器:ReAct 循环里被拒的提议会在同一状态重来,所以门是对提议流的**搜索算子**,准入准则决定哪些轨迹可达。研究违例后恢复准入:系统仍在违例时必须允许进展,并指出 **scalar projection trap**——聚合分数门接受局部改进提议就把轨迹推向平台。**SiLR** 改为 shadow-execute 每个提议、在乘积结构下准入——结构保持的准入与过程奖励。
- **关联度:** ★★★★ 工具 agent 的运行时门「结构保持」——k 设计 agent 工具准入/审批门时,「聚合分数陷阱」与 shadow-execute 准入是防平台期设计的直接参照

---

## 七、综述与对齐（2 篇）

### 21. From Language Models to World-Acting Systems: Progress and Limits of Agentic AI

- **ID:** [2609.04894v1](https://arxiv.org/abs/2609.04894v1) | [📄 PDF](https://arxiv.org/pdf/2609.04894v1)
- **作者:** Linsen Zhu, Mengqing Cai
- **分类:** cs.AI, cs.LG, cs.MA
- **摘要:** LLM 在周围系统让输出改变外部状态时成为有后果的 agent:调工具、操作界面、委派工作、保留状态、进驻生成世界、控制机器人或实验室设备。这类进展常被讲成一条通往自主的直线,把模型能力、系统集成、持久性与安全授权混为一谈。这份批判性综述综合截至 2026-08-31 的主要研究与官方技术规格,沿「**委派授权 / 时间持久性 / 环境耦合**」三轴组织证据,同时区分 model/harness 各层的进展与边界。
- **关联度:** ★★★★ 截止 08-31 的 agentic AI 综述——按授权/持久/耦合三轴 + model/harness 分层,直接可作 k 的 Agent OS/harness 知识框架的骨架

### 22. Moral Competence Before Moral Content: Why LLM Agents Lack the Prerequisites for Coherent Alignment

- **ID:** [2609.05036v1](https://arxiv.org/abs/2609.05036v1) | [📄 PDF](https://arxiv.org/pdf/2609.05036v1)
- **作者:** Arno Libert 等（3 人）
- **分类:** cs.AI, cs.CL, cs.CY
- **摘要:** AI 对齐要求系统遵守人类规范/价值观/意图。在价值多元主义下没有唯一正确目标,但共享前提是系统行为表达「**连贯策略**」:对保留道德相关特征的情境不变、改变时敏感的映射。提出四个结构条件:verdict stability、monotonicity、decisiveness、Pareto……——「先有道德能力(连贯策略),再谈道德内容」。
- **关联度:** ★★★★ 对齐的「连贯策略」前提——k 做安全/对齐相关评测时,四个结构条件把「对齐」从内容检查提升为结构检查的框架

---

## 八、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.04802](https://arxiv.org/abs/2609.04802v1) | Linguistic Trajectory Encoding | 具身 agent 长时空间记忆:把动态物体状态转移编成可语言查询的逐物时间线(clip 级视频语言嵌入丢细粒度运动、几何 SLAM 只有坐标、工作记忆只有即时任务上下文)——长时具身记忆的可查询物体级时间线 |
| 2 | [2609.04485](https://arxiv.org/abs/2609.04485v1) | Cultural Misalignment | 三开源模型 vs World Values Survey W7 的 63 人口画像 × 3 国,归一化 Wasserstein 距离量化文化错位:无模型偏爱本国(中国造的 Qwen3-4B 在自己中国人口上最差 W1=0.436),targeted LoRA 微调最差 5 画像可缓解——中文场景文化对齐「本国未必更好」 |
| 3 | [2609.04778](https://arxiv.org/abs/2609.04778v1) | Diffusion LMs for Mobile Edge Agentic AI | 扩散语言模型(DLM)作移动边缘 agentic AI 的非自回归底座:并行更新多不确定 token + 双向上下文,质量-延迟权衡更灵活——边缘 agent 的替代生成范式综述 |
| 4 | [2609.04641](https://arxiv.org/abs/2609.04641v1) | DevRev NL2SQL | 企业级嵌套 schema 的 NL2SQL:900 条执行验证查询 + Semantic Depth Score + cost-aware 单次生成 agentic 架构——生产 schema 与学术基准的鸿沟 |
| 5 | [2609.04667](https://arxiv.org/abs/2609.04667v1) | ERPBench | 六轮 ERP 模拟(定价/生产/采购/库存/财务/共享市场竞争)评企业决策 agent:同一 100 固定问题跨市场生态看结论可迁移性 |
| 6 | [2609.05401](https://arxiv.org/abs/2609.05401v1) | ROBORMBENCH | 视觉语言 reward model 的改写脆弱性:语义等价目标描述改写可显著改变预测进度、甚至把同一行为从失败翻成成功——VLM 当 reward 必须先过 paraphrase invariance |
| 7 | [2609.05117](https://arxiv.org/abs/2609.05117v1) | TIER | 威胁隐含度安全行为基准:四风险域 × 四威胁层级(显式→复杂越狱)+ 六标签行为量表 + 双 LLM judge——安全评估从二值走向分层 |
| 8 | [2609.04444](https://arxiv.org/abs/2609.04444v1) | HarvestBench | 第一个给「避免副作用」定价的基准:农场模拟、agent 开拖拉机收割、场上动物是副作用,给避开动物定价、测 agent 愿不愿意「花钱」避免杀生 |
| 9 | [2609.05079](https://arxiv.org/abs/2609.05079v1) | TruthInsightBench | 面向发现的 AI-scientist 基准:40 盲任务来自 10 科学领域 40 篇同行评审研究,复现 ≠ 发现——测「自主发现」而非复现 |
| 10 | [2609.04290](https://arxiv.org/abs/2609.04290v1) | Evidence Integration in LLMs | 分布理论:证据按 receiver 先验权重 + 候选证据倾斜移动初始答案分布;三个可测预测——评估 RAG/多 agent 证据接入的先验-倾斜模型 |

---

## 今日要点（主题信号）

1. **harness/编码 agent 从「跑分」进入「可控实验」阶段**：04518 隔离 multi-harness RL 的 credit assignment(Within vs Cross 归组)、04898 固定环境单轴变化评重构 agent、05274 用 draft-model gate 在执行前预警坏动作、04270 量化审查者能力对拒错/修复的影响——与 09-06 的 Harness Engineering(00006)连读,「agent = model + harness」的工程面全面落地。
2. **agent 安全从「单点机制」转向「组合 + 状态 + 预算」**：05269 安全上下文契约(组件安全≠组合安全)、04875 执行状态 unlearning(派生工件一起抹除)、04495 把 IPI 重铸为带预算的 test-time 搜索——延续 09-06 的 untrusted-model 范式,新增「组合连续性 / 状态可遗忘 / attacker 也有预算」三个维度。
3. **技能演化成显学,四篇并进**：04865 CoSkill(技能演化与策略优化联合)、04869 在线轨迹→持久版本化技能库(computer-use)、05019 TROVE(只重做被证据否决的路由)、05261 Trace2Tower(轨迹→层级技能)——直接背书 k 的 learn→research→apply 蒸馏路线,「轨迹→技能」是当下最强共识。
4. **记忆工程关注「升级后还认不认」**：05339 模型升级后记忆可移植性(表示形式×检索栈联合问题)、04915 紧凑记忆质量-token Pareto、04438 人级身份推理基准——与 09-06 的 00546/01235 记忆主线延续,新增「可移植性实证 + 身份维度」。
5. **reward hacking 检测进 harness 无关**：04665 HackProbe 黑盒双 hook + 秘密冻结比较核心——「分数不可信」主线再添一套通用监视器设计,与 09-06 的 01519/00038 构成反身性 + 防御双线。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Multi-Harness RL 2609.04518 | arxiv.org abs 页全文抓取(存在性 + 完整元数据);尝试 web_search(Exa)交叉源 | ✅ 已确认(arXiv 收录;跨源 web 验证被 Exa 后端代理 ConnectionError 阻断,待后续补) |
| HackProbe 2609.04665 | arxiv.org abs 页全文抓取;尝试 web_search(Exa)交叉源 | ✅ 已确认(同上) |
| Memory Portability 2609.05339 | arxiv.org abs 页全文抓取;尝试 web_search(Exa)交叉源 | ✅ 已确认(同上) |
| 其余 29 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认(HTML 收录即存在性证据 + 全文摘要) |

## 可落地行动项

- 🔴 **harness RL 与记忆可移植性深读**：04518(Within vs Cross 归组)与 05339(表示形式×检索栈)——对照 k 的多后端 RL/微调与模型升级流程,先验证「同库记忆在新模型下是否仍可检索」再谈升级
- 🔴 **agent 安全补「组合 + 遗忘」两维**：05269 安全上下文契约 + 04875 执行状态 unlearning——k 的多 agent 编排(溯源/授权/策略/适配器叠加)与敏感数据撤回流程逐条对照
- 🟡 **技能蒸馏四篇并读**：04865/04869/05019/05261 覆盖「演化-持久化-路由-层级」四环节,k 的 learn→research→apply 蒸馏链按这四环补强(尤其 04869 的轨迹→持久版本化技能库,与 k 的 knowledge→skill 直接同构)
- 🟡 **reward hacking 监视器参考**：04665 的「秘密冻结比较核心」——k 若跑任何按分数选改进的自我改进/RLVR 流程,先挂一个跨代可比的固定基准再选
- 🟢 **待深读**：04518 Multi-Harness RL、05339 Memory Portability、05269 CONTINUITY、04869 Online Skill Evolution → core-contributions 候选

---

*本速览由 cron 自动生成：09-07 索引解冻(list 页出现 09-07 新分组 480 篇,09-05/06 周末提交并入;API 持续 429 限流 → HTML list 页路由)→ 与 covered_ids 比对 0 重叠(全新窗口)→ 标题粗筛 97 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选(22 主条目 + 10 简评)→ 关键论文尝试 web 交叉验证被 Exa 代理阻断,元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
