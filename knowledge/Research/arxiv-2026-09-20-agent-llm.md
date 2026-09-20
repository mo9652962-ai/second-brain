---
aliases:
  - arxiv-2026-09-20-agent-llm
  - arxiv-agent-llm-2026-09-20
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-20
updated: 2026-09-20
status: adopted
source: arxiv.org list pages + abs pages（09-18 窗口补全速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-20（补全）

> ⚠️ **补全性质**：2026-09-20（周日）检查 arXiv list 页**无新日期分组**（最新仍为 2026-09-18，602 篇窗口）——周末提交并入周一分组属正常现象。09-18 窗口已被 09-18 速览（20+7）与 09-19 补全（13+5）两轮覆盖，合计仅约 12%；第三轮标题粗筛（含 score=1 复查）仍发现**强相关漏网**（ScientistTwo 自主科学发现 / SoL-Pi harness RSI / SkillAA 归因技能图 / claim-safe 评测协议 / CovR 覆盖率硬件验证）→ 本份为**第三轮补全速览**：对 09-18 同池继续补录（与前两份零重复，全部未覆盖）。
> **检索时间**: 2026-09-20 GMT+8（cron）
> **流程**: 09-18 分组 602 篇 → 与 covered_ids（758）比对 → 标题粗筛（score≥2 得 35 候选 + score=1 复查补 ScientistTwo 等强相关）→ 人工剔除领域应用（驾驶/医疗/交易/交通/视觉/机器人/体育）→ 逐篇抓 abs 页精选 **12 主条目 + 7 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、自主研究智能体与 Agent Harness（3 篇）

### 1. ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI

- **ID:** [2609.19644v1](https://arxiv.org/abs/2609.19644v1) | [📄 PDF](https://arxiv.org/pdf/2609.19644v1)
- **作者:** Jaehyun Nam, Jinsung Yoon, Yanzhou Pan, Yubo Wang, Rui Meng, Parthasarathy Ranganathan, Tomas Pfister
- **分类:** cs.AI
- **摘要:** 全自主多智能体科学发现框架：给定人类专家提出的基础问题，自动建立 SOTA 基线、提出新假设、协调专门 agent 完成端到端发现循环（无人工干预）——自动设计并跑实验、自动消融、用**闭环模拟同行评审反驳引擎**验证研究结论。以 ICLR/ICML/NeurIPS 录用论文为基准评测：自主生成专家级可发表论文 + 完全可验证可执行代码库；方案持续超越人类 SOTA，在 AI 评审 agent 下平均评分高于人类作者论文。Google 系（Nam / Yoon / Pfister 等）出品。
- **关联度:** ★★★★★ 自主研究流水线的完整形态——k 的联合研究流水线（multi-agent-research：k 拆题→WorkBuddy/dsh 初稿→k 核验→Gemini 二审）与「假设→实验→消融→模拟评审」同构；「闭环模拟 peer-review 引擎」正是 k 的产物断言/验证门禁的 agent 版蓝图

### 2. SoL-Pi: Recursively Scaling Auto-Research Loops for Efficient Agent Harness

- **ID:** [2609.20519v1](https://arxiv.org/abs/2609.20519v1) | [📄 PDF](https://arxiv.org/pdf/2609.20519v1)
- **作者:** Haozhe Liu, Tian Ye, Sensen Gao, Qihang Cao, Yitong Li, Mingchen Zhuge, Duomin Wang, Ruihua Zhang, Ping Luo, Jiawang Bian, Lei Zhu, Ligeng Zhu, Enze Xie, Song Han
- **分类:** cs.AI
- **摘要:** 编码 agent 从「监督式补全」走向「全天候无人探索」后，长轨迹（推理/工具调用/反馈）的 **token 效率**成为扩展递归自我改进（RSI）的关键。SoL-Pi 在 **harness 层**做 RSI：AI 优化器观察 agent 执行轨迹→提议 harness 改动→在隔离研究环境测试→**能力+效率双门**筛选；约 150 个方向 × 500 个可执行环境 × 3,000+ 次运行 × 60,000+ 次 agent-环境交互后，存活 4 个机制（Action Fusion 动作融合 / Online Context Compact 在线上下文压缩 / ObservationPack 观察打包 / Evidence-Preserving Reducer 证据保留化简）。EdgeBench 51 任务上性能与 Pi 持平（GPT-5.6 Sol / Opus 5），**token 流量降 44.7-49.0%、API 成本降约 1/3**（相对原生 Codex/Claude Code harness 每小时省 $8.75-13.50）。关键方法论：**搜索反馈与最终评测严格分离**，防 harness 过拟合搜索任务。NVIDIA/NTU/MIT 合作。
- **关联度:** ★★★★★ harness 层 RSI + token 效率——k 的编码委派（Codex CLI/dsh）与 Hermes 工具链的 token 成本优化直接同题；「能力+效率双门 + 开发/留出分离」是 k 的提示词/技能迭代验收协议参考；4 个机制名可直接映射 k 的上下文管理（压缩/打包/化简）

### 3. Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL

- **ID:** [2609.20715v1](https://arxiv.org/abs/2609.20715v1) | [📄 PDF](https://arxiv.org/pdf/2609.20715v1)
- **作者:** Juzheng Zhang, Disha Makhija, Manoj Ghuhan Arivazhagan, Vinayshekhar Bannihatti Kumar, Rashmi Gangadharaiah
- **分类:** cs.LG, cs.AI, cs.CL
- **摘要:** 标准 SFT 只对 agent 自产动作 token 算损失、把环境观测当纯上下文——本文问这约定是否是最优 RL 初始化。ActObs：把轨迹里已有的**观测 token 也纳入监督**（部署时 agent 并不生成观测，但学会预测它们让策略建模行动后果，不加数据/参数/token/前向）。SFT 后两者表现相近，但 GRPO 后分化：Qwen3-4B 在 Terminal-Bench 2.0 每个采样预算下 pass@k 更高；8B 以少量 pass@1 换更高 pass@k（+3.4pp @ pass@16）并解出更多不同任务；跨域代码编辑 aider-polyglot +4.2pp @ pass@1。机制分析：动作与观测梯度在 SFT 中快速正交，纯动作训练留下大的残差观测梯度、环境预测退化——联合监督防止单侧特化，为下游探索保留后果预测能力。
- **关联度:** ★★★★ agent 训练初始化的反直觉改进——k 的刷题机/墨题 AI 标注、RAG 管道的「输入侧建模」思路；「观测也是可监督信号」对 k 的 agent 日志/轨迹复盘（不做损失也做评估）有设计启发

---

## 二、技能系统与评测方法论（4 篇）

### 4. SkillAA: Attribution-Guided Skill-Graph Updating with Targeted Validation and Rollback

- **ID:** [2609.20455v1](https://arxiv.org/abs/2609.20455v1) | [📄 PDF](https://arxiv.org/pdf/2609.20455v1)
- **作者:** Ziqiao Shang, Ling-Yue Ge, Lan-Zhe Guo
- **分类:** cs.AI
- **摘要:** 外部技能（不更新参数、提供领域流程）的编辑常直接从失败 rollout 改，缺乏「失败→可编辑位置」的结构化路由；技能图也没用足语义边界/对象地址/拓扑依赖。SkillAA（Skill Abductive Attribution）：把技能适用性、执行、组合表示进**统一图**，同一结构支撑技能选择、归因修复、更新验证——对比成功/失败执行把候选修复**路由到具体图对象**、只更新选中局部结构、用 **Local/Big 双门**在提交前筛选候选改动。gpt-5.6-sol 上 SearchQA 81.5% / LiveMath 66.7% / DocVQA 91.2%，所有主设置平均最高。
- **关联度:** ★★★★★ 技能图的归因更新 + 双门验证 + rollback——与 k 的**技能体系（skill_manage patch 语义、skill-evolution 自进化、code-quality-bootstrapping 从 Review 反馈沉淀规则）直接同构**；「失败→路由到具体技能片段→局部更新→门禁验证→可回滚」正是 k 的 skill 迭代缺的结构化框架；Local/Big Gates 对应 k 的 verify_digest_note/门禁机制

### 5. Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation

- **ID:** [2609.20538v1](https://arxiv.org/abs/2609.20538v1) | [📄 PDF](https://arxiv.org/pdf/2609.20538v1)
- **作者:** Peiying Zhu, Sidi Chang
- **分类:** cs.AI
- **摘要:** 评测可以完全可复现、却支撑错误结论——闭环系统尤其危险（策略决定访问状态/可观测组件/哪些失败留下痕迹）。claim-safe 协议三动作：①**Refuse**：干净参考流或匹配运行时比较缺乏支撑时弃权；②**Decompose**：把协议执行、运行期误纳、结构假设分开报告，不合并成一个 PASS/FAIL 标签；③**Refresh**：把分布漂移告警当作「作废并重算参考图」的请求，而非故障证据。在聚合模拟器（24 策略组件 × 3 需求体制 × 2 故障掩码族，预注册留出 1,440 例 / 21,600 分区行）实例化：72 个体制-组件单元仅 55 个通过参考准入、54 个通过运行期准入——**弃权是结果的一部分**；「null 必须相对参考定义」：同一干净流在三个体制下触发 15/15、0/15、14/15 告警，仅中间体制匹配冻结检测器参考。
- **关联度:** ★★★★★ 评测的「claim-safe 契约」——k 的产物断言体系（本速览的产物断言、verify_digest_note、service-quality 门禁）的学术版；「弃权也是结果」直接呼应 k 的「不臆造、标不确定」；「PASS/FAIL 分解为协议/误纳/假设」是 k 的验证表升级方向

### 6. CodeTransBenchmark: Evaluating LLM-based Code Translation and Repair Across Programming Languages

- **ID:** [2609.20257v1](https://arxiv.org/abs/2609.20257v1) | [📄 PDF](https://arxiv.org/pdf/2609.20257v1)
- **作者:** Vera Kowalczuk, Oliver Weißl, Severin Kacianka, Andrea Stocco
- **分类:** cs.SE
- **摘要:** LLM 代码翻译的评测框架 + 实证：CodeTransBenchmark 含从 LLM 不一致输出提取代码的后处理策略；8 模型 × 3 数据集 × 12 语言对的实证，按错误类别划分错误翻译定位弱点。发现：多语代码特化模型（Codestral）能正确翻译多数代码，通用模型普遍卡在目标语言语法规则；语言对与训练数据的交互显著影响效果；**迭代翻译修复（自动反馈）显著提升准确率**；实际部署需要更大上下文窗口。
- **关联度:** ★★★★ 代码翻译/修复评测——k 的跨语言代码迁移（Python↔TS、legacy 代码改造）的模型选型实证；「后处理须容忍不一致 + 迭代修复显著有效」对 k 的代码交付质检（code-audit-delivery）是流程参考

### 7. Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation

- **ID:** [2609.20758v1](https://arxiv.org/abs/2609.20758v1) | [📄 PDF](https://arxiv.org/pdf/2609.20758v1)
- **作者:** Sho Kawano, Zehang Richard Li, Paul A. Parker
- **分类:** stat.ML, cs.AI, cs.LG, stat.AP, stat.ME
- **摘要:** AI 评估需要按域分解（任务类型/对话类型），穷举测试贵、评估只能靠标注样本。把评估集当有限总体估计各域均值：直接估计器（含预测辅助推断 PPI）在标签少处不精确；引入**小域估计（small area estimation）**思路——PP-S（贝叶斯平滑）与跨报告分类学借力的 PP-TS，加近似无偏的设计基交叉验证分数选估计器。在可验证评分的基准 + 人类评分的部署 agent 流量上：点估计与区间估计均改进、覆盖近名义水平；同采样预算下选择效果与独立验证样本相当，所选估计器误差估计更准。
- **关联度:** ★★★ 「小标签域借力平滑」——k 的多技能/多场景评估（skill 分域、闲鱼交付类型分域）在样本少时的高效估计方法；PPI→PP-S 的「预测辅助 + 贝叶斯借力」对 k 的低成本评测设计是统计工具箱

---

## 三、LLM 安全与对齐（3 篇）

### 8. Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations

- **ID:** [2609.20779v1](https://arxiv.org/abs/2609.20779v1) | [📄 PDF](https://arxiv.org/pdf/2609.20779v1)
- **作者:** Sarah Wyer, Sue Black, Noura Al Moubayed
- **分类:** cs.CL, cs.AI
- **摘要:** 安全评测依赖表层分类器，报告跨代际「有害分下降」——本文证明该方法论系统性不完整：显式歧视内容被**转化而非移除**（harm laundering）。分析 GPT-2 到 GPT-5 共 15 模型 × 450,000 条性别定向补全：GPT-2 面向女性的性暴力簇到 GPT-4 消失，而面向男性的补全获得女性没有的正向表征领地（照护/情绪广度/盟友身份）；GPT-5 把乳腺癌框架成男性权利辩论，三个独立分类器均判无毒；情绪分在 GPT-4 反转；女性定向内容的话题多样性在 GPT-4 对齐边界降 36%；REGARD 表征伤害与发布日期相关（ρ=+0.55, p=.034）而 Detoxify 不相关（ρ=-0.23）——**毒性分数下降不是伤害减少的充分代理**。给出三准则形式化测试 + 三阶段检测协议。
- **关联度:** ★★★★ 安全评测的「表面分数陷阱」——k 的内容安全/禁词过滤（闲鱼素材禁词、墨题内容）的实证警告：表面分类器分数下降可能只是「换皮」；「检测协议三阶段」可进 k 的素材核验/审核技能

### 9. Stress-testing Alignment Midtraining

- **ID:** [2609.20412v1](https://arxiv.org/abs/2609.20412v1) | [📄 PDF](https://arxiv.org/pdf/2609.20412v1)
- **作者:** Sid Baines, Jonathan Bostock, Maria Angelica Martinez, Andrew Draganov, David Africa, Daniel Tan
- **分类:** cs.CL, cs.AI
- **摘要:** 对齐中期训练（AMT：继续预训练大量对齐相关文档，鼓励后训练阶段泛化）虽被当作对齐方案，但公开证据有限。本文在规模上（最高 110B 参数 × 10 亿 AMT token）检验其假设：后训练数据在两个动机间含糊时，AMT 能在简单设定下引导模型动机；但**一小撮暗示竞争动机的微调数据就能抹掉 AMT 效果**；想让模型遵守多条规则而只演示子集时，演示必须出现在中期或后训练数据里规则才能稳健学会。结论：没有足够公开证据支持「AMT 能解决对齐强大 AI 的核心困难」。
- **关联度:** ★★★ 对齐方法被压力测试「证据不足」——与 20779 同调：前沿对齐方案需要硬证据而非信仰；「演示必须出现在训练分布」对 k 的少样本/提示工程是分布匹配提醒

### 10. Xeno-Interpretability: Investigating the Alien Minds of LLMs

- **ID:** [2609.20408v1](https://arxiv.org/abs/2609.20408v1) | [📄 PDF](https://arxiv.org/pdf/2609.20408v1)
- **作者:** F. Pierucci, M. Bracale Syrnikov, M. Prandi, M. Galisai, F. Giarrusso, P. Bisconti
- **分类:** cs.CL, cs.AI
- **摘要:** LLM 通常用人类已有概念解释（真实/拒答/欺骗/人格/有害），但模型可能表征人类没有对应概念的区别——xeno-representations（异质表征）。区分人类可解释语义空间与 xeno 语义空间：模型内部可能区分空间远大于人类有限描述可达空间；把**实验识别与语义解释分离**——内部表征可被可复现定位、几何刻画、因果操纵、关联下游行为，即便语义内容无法用人类语言表达。给出识别 xeno 表征的经验纲领；讨论对 AI 安全与多智能体系统的含义（模型原生表征可能在交互 agent 间传播稳定、仅部分透过人类可读通信可见）。
- **关联度:** ★★★★ 解释性转向「模型原生表征」——k 的多 agent 协作/盲评的深层提醒：agent 间可能用人类不可读的共享表征达成稳定行为；「实验识别与语义解释分离」是 k 的评测（验证可复现性≠理解语义）的认识论框架

---

## 四、模型架构与硬件验证（2 篇）

### 11. Zarya: A Hybrid Autoregressive--Masked Diffusion Language Model with Flexible Training and Dual-Mode Inference

- **ID:** [2609.19868v1](https://arxiv.org/abs/2609.19868v1) | [📄 PDF](https://arxiv.org/pdf/2609.19868v1)
- **作者:** Leonid Sinev, Ilya Koziev, Vladislav Leshchuk
- **分类:** cs.CL, cs.AI
- **摘要:** AR 模型受顺序生成限制；掩码扩散模型（MDM）能并行解码但无法复用 KV cache、token 组合空间不可解导致生成不连贯。Zarya：单架构联合优化 AR 目标 + 掩码扩散目标——训练数据按可变大小 slot 组织、课程逐步细化 slot 粒度，从细粒度 AR 平滑过渡到粗粒度扩散；推理提供统一接口双模式：MDM 采样（first-hitting denoising）与 slot 化投机解码（slot 间扩散选择 + slot 内 AR 填充，**全 KV cache 复用**）。训练/推理完全解耦，任何配置训练的模型可任意模式部署。开源 0.6B/1.7B/4B。
- **关联度:** ★★★★ AR+扩散混合架构的实用化——k 的本地推理（RTX4060 8GB 约束）模型选型的新候选族；「训练推理解耦 + 双模式」对 k 的批量生成（并行）与交互（顺序）双场景切换是架构级思路

### 12. CovR: Coverage-Aware Hardware Verification via Reasoning-Guided Reinforcement Learning

- **ID:** [2609.19189v1](https://arxiv.org/abs/2609.19189v1) | [📄 PDF](https://arxiv.org/pdf/2609.19189v1)
- **作者:** Manar Abdelatty, Maryam Nouh, Sherief Reda
- **分类:** cs.AR, cs.CL
- **摘要:** 设计验证占硬件开发成本最多 70%；已有 LLM 自动化 testbench 生成只盯功能正确性、忽略覆盖率质量。CovR：agentic testbench 生成框架，**自反思循环 + 仿真反馈最大化覆盖率**；用强教师模型构建 16,514 条自然规格 RTL 推理 testbench 元组做覆盖率感知监督；RL 框架用工具派生的仿真/覆盖率奖励优化学生模型。微调模型 VerilogEval/RTLLM V2.0 cov@10 达 93.81%、CVDP 87.76%，超 SOTA 7.97%/3.59%；回注 agentic 精炼管线再提到 94.27%/91.39%；作为全验证流程的插件刺激引擎，覆盖率 +18.95%、突变检测分 +1.19%、揭示 4.46% 未检出故障。
- **关联度:** ★★★★★ 覆盖率感知的硬件验证 agent——k 的 PCB/硬件验证兴趣（KiCad 自动化、pcb-design、硬件接单）的验证层蓝图：「工具反馈奖励 + 覆盖率监督」正是 k 的 DRC/治具自动化的 agent 化方向；「优化覆盖率而非仅正确性」对 k 的测试设计是方法论升级

---

## 五、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.19527](https://arxiv.org/abs/2609.19527v1) | AURORA: A Natural Language-Driven Agentic Framework for Understanding, Reasoning, and Orchestrating Reliable Air-Ground Co-Simulation | 把场景生成当「编译+验证」：类型化中间表示（AGSG）+ 仿真接地解析 + 执行前可行性检查 + 轨迹运行时验证 + 有界修复——「验证嵌入生成流程」对 k 的产物断言是架构参考（领域在空-地交通共仿真） |
| 2 | [2609.20543](https://arxiv.org/abs/2609.20543v1) | Language-model groups overstate consensus when replaying human deliberation on a reasoning task | 重放 100 组人类 Wason 讨论：LLM agent 组的共识率系统性虚高（34-44pp 差距，推理模式几乎全票错答）——「模拟共识不追踪集体正确性」对 k 的多 agent 一致性判断是警告 |
| 3 | [2609.20734](https://arxiv.org/abs/2609.20734v1) | On-Demand Attention: Language Models Know When to Recall | ODA 本地优先解码：轻量 recall head 选择性触发全局注意力，只训 recall head、vLLM GPU 条件执行落地——长上下文 agent 推理的省算力路线，k 的本地推理效率参考 |
| 4 | [2609.19657](https://arxiv.org/abs/2609.19657v1) | PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving | vLLM/TensorRT-LLM 前缀复用（系统提示/RAG/agent 框架普遍复用前缀）的系统化基准：何时复用真正提速、何时被调度/缓存粒度/并发限制——k 的 LLM 服务调优测量协议 |
| 5 | [2609.20584](https://arxiv.org/abs/2609.20584v1) | SAFARI: An Industrial Benchmark for LLM-Assisted Hazard Analysis and Risk Assessment | ISO 26262 汽车 HARA 首个工业基准（3,000 例）：9 个前沿 LLM 的 ASIL 宏 F1 最高仅 0.261，CoT 常降级分类——「法规分类弱」对 k 的安全关键工程/合规类交付是能力边界实证 |
| 6 | [2609.20218](https://arxiv.org/abs/2609.20218v1) | Is It Still Worth Training a Classical Model in the Era of LLMs? A Crossover Benchmark on Tabular Data | 表格数据「冻结 LLM 提示 vs 训练经典模型」跨界点 N*：86% 情形下经典模型用手上已有标签就赢、中位跨界点约训练集 6%——k 的低成本 ML 选型（有标签就训练，别迷信提示） |
| 7 | [2609.19242](https://arxiv.org/abs/2609.19242v1) | Block Parallelism For Efficient Distributed Long-Context Diffusion Language Model Training | CSBP 新分布式并行维度：16×H200 256K 上下文较最佳基线提速 1.18-1.45x（SFT）与 1.27-1.33x（AR→BDLM 转换）——扩散 LM 长上下文训练基建，与 Zarya 同属扩散系进展 |

---

## 今日要点（主题信号）

1. **自主研究流水线成为主线**：19644 ScientistTwo（Google）全自主科学发现 + 20519 SoL-Pi harness RSI——「agent 研究 agent、agent 改进 harness」从概念走向生产级；k 的联合研究流水线与 skill-evolution 的远期形态就是这条线。
2. **技能系统进入「归因更新 + 门禁」结构化阶段**：20455 SkillAA 把技能编辑从「直接改」升级为「失败→归因→局部更新→双门验证→可回滚」——与 k 的 skill_manage/skill-evolution 同构，且补上 k 缺的结构化验证层。
3. **评测方法论三连：claim-safe 契约 / 分域小样本估计 / 代码翻译基准**——20538 Refuse-Decompose-Refresh（弃权也是结果、PASS/FAIL 分解）、20758 PP-S（小标签域贝叶斯借力）、20257 CodeTransBenchmark——k 的验证表/产物断言可吸收「分解报告 + 弃权」两条。
4. **安全评测进入「方法论自反」期**：20779 harm laundering 证明表面毒性分下降≠伤害减少（450K 补全实证）+ 20412 AMT 压力测试证据不足——「分数不是证据」成为共识，k 的禁词/内容过滤要防「换皮」。
5. **覆盖率而非正确性**：19189 CovR 把硬件验证从功能正确转向覆盖率优化（cov@10 93.81%、覆盖率+18.95%）——对 k 的 PCB/硬件验证自动化是直接的方向参考。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| ScientistTwo 2609.19644 | arxiv.org abs 页 + web_search 跨源（AI Scientist/EvoScientist/EurekAgent 同族研究群互证，Google 系作者） | ✅ 已确认（arXiv 收录 + 同族研究群互证） |
| SoL-Pi 2609.20519 | arxiv.org abs/HTML 页 + web_search 跨源（arXiv / HF papers / papers.cool 多源一致；NVIDIA/NTU/MIT 作者 + Code/Blog 链接） | ✅ 已确认（多源一致） |
| SkillAA 2609.20455 | arxiv.org abs 页 + web_search 跨源（arXiv / papers.cool / 社区摘要一致） | ✅ 已确认（多源一致） |
| Refuse, Decompose, Refresh 2609.20538 | arxiv.org abs 页 + web_search 跨源（arXiv / papers.cool 一致，含可复现工件链接） | ✅ 已确认（多源一致） |
| 其余 8 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **自主研究流水线对照**：19644 ScientistTwo 的「假设→基线→实验→消融→模拟评审」闭环——k 的 multi-agent-research 流水线加「模拟评审/反驳引擎」环节（k 拆题→初稿→核验→二审已具备大半），把 Gemini 二审升级为带反驳的闭环
- 🔴 **技能归因更新试点**：20455 SkillAA「失败→路由到技能片段→局部更新→Local/Big 双门→回滚」——k 的 skill_manage 迭代（尤其 code-quality-bootstrapping 从 Review 反馈沉淀规范）套用「先归因再改 + 改前门禁 + 可回滚」，防技能越改越坏
- 🟡 **评测分解报告**：20538「弃权也是结果 + PASS/FAIL 分解为协议执行/误纳/结构假设」——verify_digest_note/service-quality 的检查结果按三成分拆开报告，不合并成一个布尔；覆盖不足时明确标「弃权」而非硬判 PASS/FAIL
- 🟡 **安全过滤防「换皮」**：20779「表面毒性分下降≠伤害减少」——闲鱼素材禁词/内容审核加「表征级」抽检（不只看表面词命中），防止禁词被同义改写绕过
- 🟡 **硬件验证覆盖率意识**：19189 CovR「优化覆盖率而非仅正确性」——PCB/硬件接单的测试设计（DRC/治具/测试点）从「功能对」升级为「覆盖率量化」
- 🟢 **待深读**：19644（ScientistTwo）、20519（SoL-Pi）、20455（SkillAA）、20538（claim-safe 评测）、19189（CovR）→ core-contributions 候选

---

*本速览由 cron 自动生成（第三轮补全性质）：2026-09-20 无新日期分组（周日，最新仍 09-18）→ 09-18 同池 602 篇与 covered_ids（758）比对 → 标题粗筛 35 候选 + score=1 复查（抓到 ScientistTwo 等强相关）→ 人工剔除领域应用 → 逐篇抓 abs 页精选（12 主条目 + 7 简评），与前两份零重复。关键论文跨源 web 验证（ScientistTwo / SoL-Pi / SkillAA / claim-safe 协议）。元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

---
状态：reading
