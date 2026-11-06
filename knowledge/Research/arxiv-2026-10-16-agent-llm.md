---
aliases:
  - arxiv-2026-10-16-agent-llm
  - arxiv-agent-llm-2026-10-16
tags: [arxiv, research, ai-agent, llm, daily]
created: 2026-10-16
updated: 2026-10-16
status: adopted
source: arxiv.org list 页 + abs 页（10-14~10-16 新窗口 · 正常速览）
---

# arXiv AI Agent / LLM 速览 — 2026-10-16（10-14~10-16 窗口）

> **窗口性质**：10-16 检查 list 页，日期分组为 **Fri, 16 Oct 2026 / Thu, 15 Oct / Wed, 14 Oct / Mon, 12 Oct / Fri, 9 Oct**——上一份 10-14 速览只覆盖到 **Mon, 12 Oct**，因此 **10-14 / 10-15 / 10-16 三个日期分组均为全新窗口**（与 covered_ids 1,181 重叠 0）。周三提交量 852 篇（cs.AI 单类）显著高于平日，属正常波动而非异常。
> **检索时间**: 2026-10-16 GMT+8（cron）
> **流程**: `collect_recent_html.py` 拉 6 类别 recent 全量（cs.LG / cs.SE 首跑 SSL EOF，单独补拉成功；合并去重后 10-14: 2,117 / 10-15: 739 / 10-16: 759，三窗口唯一 base 合计 **3,612 篇**）→ 全部与 covered_ids（1,181）比对 → **3,612 篇全部未覆盖** → 标题粗筛 662 候选（score≥2：5×6 / 4×41 / 3×147 / 2×468）→ 抓 abs 页 **194 篇**（score≥3 全量，并行 curl，store 0→194，`MISSING: []`）→ 人工剔除领域应用误报（医疗/遥感/机器人/交通/材料/化学/金融/农业等）→ 精选 **30 主条目 + 36 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页（HTML 路由，curl 直连，`--ssl-no-revoke`）
> **说明**: 本份未做跨源 web 验证（arXiv HTML 收录即存在性证据），元数据以 abs 页为准；版本号取自 abs 页链接，防引用漂移。

---

## 一、Agent 技能治理：规模、组合、漂移、水印（6 篇）

### 1. Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale

- **ID:** [2610.18522v1](https://arxiv.org/abs/2610.18522v1) | [📄 PDF](https://arxiv.org/pdf/2610.18522)
- **作者:** Jinlin Liu, Wei Chen, Xiaojin Zhang
- **分类:** cs.AI
- **摘要:** 可复用技能让 agent 按需加载任务指令，但这也把执行**隐式地**依赖在技能元数据的路由上。作者固定 SkillsBench 任务与它们的 golden skill，只**不断加入无关技能**，检验该设计是否可扩展。结果发现 **skill routing collapse**：agent 加载的技能越来越少甚至不加载，尽管相关技能仍在库里。加入 **1,000 个无关技能**后，loaded-skill recall 从 **73.6% 掉到 27.4%**、zero-load rate 从 **9.3% 升到 51.6%**；而**从同一库中显式选择**仍保持 73.9% recall。加载「其他技能」（包括 golden skill 的貌似替代品）太少，不足以解释该下降。**只遮蔽无关技能的描述**即可基本恢复加载，而元数据完整时即使明确要求 agent 先规划技能使用，recall 仍低于预选。作者结论：存在来自**描述语义干扰**与**技能选择与任务执行竞争指令资源**的双重效应，并评估显式预选作为缓解手段（含覆盖度与时延折衷）。
- **关联度:** ★★★★★ 这是 k 技能库最直接的失效模型——k 目前装了数百个技能，正好落在本文的「技能规模化」区间。可落地：① 技能路由**不要靠元数据隐式召回**，重要任务先**显式点名**要用的技能；② 精简技能 description（本文证明描述本身就是干扰源），只留区分性关键词；③ 无关技能对当前任务的影响是**非线性的**（1,000 个就腰斩 recall），技能库该按任务域分仓而不是全量挂载。

### 2. SkillFusion: Towards Reliable Multi-Skill Composition for LLM Agents

- **ID:** [2610.15481v1](https://arxiv.org/abs/2610.15481v1) | [📄 PDF](https://arxiv.org/pdf/2610.15481)
- **作者:** Enhao Huang, Xinye Zhao, Yiming Li, Bingrun Yang, Nanjun Zhou, Chunshu Xia, Hongwei Yao, Zhan Qin
- **分类:** cs.AI
- **摘要:** 独立编写的技能在被 agent 联合加载时会提出**互不兼容的要求、相互竞争的偏好与冗余指令**。SkillFusion 是一个**离线编译器**，把这些交互调和成一个可复用的合并技能。核心思路：用**带类型、带作用域的约束**把组合决策显式化，并链接回其源指令。类型-作用域 gate 选出候选交互，selective fallback 回访可能被结构剪枝漏掉的配对；分类器识别交互类型，对抗式 verifier 复核不确定判断；resolver 对硬冲突施加条件路由或显式优先级，对软冲突做经验证的抽象，对冗余指令做去重。源链接检查指导合成与压缩，元数据合成支撑合并技能的发现。产物保留关联脚本与资源，可跨任务与执行模型复用。SkillFusion 在三个 agent 基准与两个迁移基准上、三个执行模型下均取得非 oracle 方法中最高平均成功率；在最大指令配置下，成功率是未调和多技能加载的 **2.5 倍以上**。代码将在评审后开源。
- **关联度:** ★★★★★ 与第 1 篇正好互补：第 1 篇说「技能多了会崩」，本篇给出**工程解法**（把组合做成编译期决策，而不是运行时靠模型自觉）。对 k 的意义：技能之间有冲突（如两个技能对同一文件格式给出不同约定）时，**该在装载前调和并留溯源**，而不是让 agent 现场裁量。SkillMarker（第 5 篇）与本篇同属「技能作为可分发资产」这条线。

### 3. Evolving Together, Failing Apart: The Skill-Policy Co-evolution Trap in Self-Improving Agents

- **ID:** [2610.20845v1](https://arxiv.org/abs/2610.20845v1) | [📄 PDF](https://arxiv.org/pdf/2610.20845)
- **作者:** Yujie Feng, Xiaobin Wang, Jinluan Yang, Xiaonan Shi, Pengjun Xie, Philip S. Yu, Xiaoming Wu, Jieping Ye
- **分类:** cs.AI, cs.CL
- **摘要:** 技能-策略协同演化（策略模型与技能库互相促进）是自改进 agent 的热门范式，但现有评测都在**训练时用的那个技能库（delivered bank）**上给分。部署后技能会被改写、新增、删除，频率远高于策略模型重训，于是策略实际运行在**漂移过的技能库**上——训练目标与现有评测协议都没有覆盖这个盲区。作者先从理论与实证上证明该盲区掩盖的脆弱性不是偶然：这些方法共用的接受规则（cooperative acceptance）把策略能力**绑定在协同演化时的那个库**上，因此一旦技能漂移就脆弱，与实现无关；实证上对技能漂移的敏感性**随协同演化训练推进而增长**。为此提出 **CODA（CO-evolution Drift Audit）**：面向部署的评测协议，模拟技能漂移，除最坏漂移下的成功率外新增两个指标——**语义保持编辑下的一致性率**与**对损坏技能的抵抗率**。四个协同演化方法 × 五个基准（六个设置）：最坏情况成功率比每个 delivered pair 的峰值**低 5–13 分**，抹掉 delivered bank 相对无技能基线增益的 **52%–93%**。CODA 把协同演化的目标从「在协同演化库上的峰值表现」重定义为「无论技能怎么演化都能驾驭」。
- **关联度:** ★★★★★ 直接命中 k 的「技能库 + 提示词/规则」自维护实践。教训：**技能库的评测必须在漂移后测**，用「我在当前库上跑通了」当证据是结构性盲区。可落地：① 技能改动后不要只看「改完能不能跑」，要跑「语义等价的改写」与「被污染的技能」两组对照；② 技能库每次扩容后复测历史任务，防「协同演化峰值」假象；③ 与第 7 篇（RSE-Bench 噪声）合成一条纪律：**自演化产出的技能一律当未验证品对待**。

### 4. Why Static Skill Inconsistencies Do Not Equate to Runtime Risks: A Behavioral Analysis of LLM Agent Execution

- **ID:** [2610.18927v1](https://arxiv.org/abs/2610.18927v1) | [📄 PDF](https://arxiv.org/pdf/2610.18927)
- **作者:** Fengrui Fan, Huahao Wang, Jingyi Fang, Yutao Hu, Yueming Wu, Deqing Zou
- **分类:** cs.AI
- **摘要:** LLM agent 框架重度依赖外部技能资产来规范工具使用、编码操作流程、提供可执行运行时资源。多组件技能包普遍存在**跨产物不一致**——文档、脚本、配置文件给出互相冲突的行为约束。静态审计能发现这类契约性偏差，但**静态缺陷数量无法可靠反映真实 agent 性能退化**，实践者缺少评估缺陷技能实际风险的严谨证据。本文做系统性实证研究：对 **575 个社区与基准技能**做大规模审计，得到 **1,182 个人工验证的契约不一致**；再构建受控评测流水线，含 **49 个可执行 agent 任务**与三个代表性 LLM，在 **NoSkill / OriginalSkill / FixedSkill** 三种设置下，对 **441 条配对执行轨迹**做细粒度行为分析，量化「修复缺陷」到底带来多少实际性能影响。
- **关联度:** ★★★★★ 这是对 k 的「技能审计」做法的关键校准——**静态缺陷数 ≠ 运行时风险**。k 做知识库 lint / 技能体检时容易把「发现 N 处不一致」当成风险指标。可落地：① 技能体检报告要区分「契约不一致」与「已证实影响任务的行为退化」，后者才进 P0；② 用 NoSkill / OriginalSkill / FixedSkill 三档对照来验证修复是否真有效；③ 与第 3 篇同属「技能质量的证据标准」这条线——**能修 ≠ 值得修**。

### 5. SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification

- **ID:** [2610.15725v2](https://arxiv.org/abs/2610.15725v2) | [📄 PDF](https://arxiv.org/pdf/2610.15725)
- **作者:** Alan Tang, Lifeng Wang, Gang Wu, Tao Zhang, Yantao Jia, Xiaofeng Zhu
- **分类:** cs.CR, cs.AI
- **摘要:** Agent 技能把操作流程与领域专业知识编码为可复用知识资产，但**明文分发**使其暴露于未授权复制与泄漏，而技能所有权验证与泄漏溯源的实际机制仍不成熟。分发前嵌入水印是潜在解法，但结构化、紧凑的技能指令对事实与流程准确性要求极严。SkillMarker 是基于 **KGW** 的水印方法，同时瞄准功能保持与强水印嵌入：**质量约束改写**把必要知识与灵活表达分离以保持指令保真，**信号导向候选搜索**在保持约束下探索替代表达以获得更强水印信号。作者开源了集成嵌入、质量审计、检测的工具包，面向「内容可能被整体或部分复制、或被并入其他技能」的分发生态。四个数据集上下游任务性能平均影响可忽略；copy-paste 测试中基于窗口的检测可稳定识别**短至 1,536 个连续 token** 的被复制段落；即使与一或三个背景技能合并，水印检出率仍保持 **72.2%–77.8%**。
- **关联度:** ★★★★ 对 k 的商业资产保护有直接价值：接单交付的技能/提示词/SOP 一旦明文给出，就是可被整体复制的资产。可落地：① 对外分发的技能文档嵌水印再交付；② 「1,536 连续 token」是可检测下限——低于此长度的片段挪用无法溯源，因此**核心 know-how 要拆成小于该粒度且依赖外部上下文**；③ 与「资产三级隔离」纪律合成：能不上传的就不上传，要上传的先水印。

### 6. Cortex: Measurement-Gated Evolution and Pruning of Coding-Agent Skills and Rules

- **ID:** [2610.14216v1](https://arxiv.org/abs/2610.14216v1) | [📄 PDF](https://arxiv.org/pdf/2610.14216)
- **作者:** Samuele Giampieri
- **分类:** cs.SE, cs.AI
- **摘要:** 编码 agent（如 Claude Code）还会读开发者为其写的文本文件：项目文件、agent 可选择打开的技能、agent 读到匹配文件时自动加载的规则——作者称这些文件为 agent 的 **harness**。开发者每次纠正 agent 就往里加内容，但**一次成功说明不了什么**：同一个 agent 可能这次过、下次不过。Cortex 是一个**测试 harness 改动**而不是信任它的工具：把开发者会话中的修复存成可重放任务，找出**反复出现**的纠正，一次只写一条技能或规则，**只有带它/不带它的重复运行显示净收益且没有任何任务明显变差时才保留**；删文本前也做同样测试；且既不添加也不删除 agent 从未用到的文本。用 Claude Haiku 4.5 在一个专门构建的仓库上测试（含模型倾向违反的约定、一块没东西可学的区域、一个扮演开发者的脚本）：在留出任务上，它构建的 harness 让 agent 遵守约定的频率远高于无技能/规则时，未学习区域保持不变，且未增加每轮都要读的文本。**规则（自动加载）承担了大部分作用**；技能只在「与任务涉及的文件一起提供」时有用，每轮都提供的技能很少被打开。Cortex 没有保留任何植入的无用或有害建议，但 agent 从未打开无用技能与有害技能，对有害规则也没给出结论——因此该测试只证明「Cortex 不保留未使用文本」，**不证明它能检测伤害**。在更强的 Claude Sonnet 5 下单次运行的 harness 增益很小；在真实开源项目上（agent 很少被纠正）Cortex 找不到可学的东西。
- **关联度:** ★★★★★ 这是本窗口最可直接照搬的方法论，而且**作者自己诚实标出了能力边界**（不证明能检测伤害）。对 k 的意义：① 技能/规则/记忆的增删**必须有配对重放测试**，不能凭「这次管用」；② **规则 > 技能**（自动加载的规则做了大部分工作），每轮都塞的技能反而没人读——与第 1 篇的语义干扰结论一致；③ 技能该**按需与相关文件一起给**，而不是常驻；④ 承认「在没被纠正过的场景里学不到东西」是正常结果，不是失败。

---

## 二、记忆治理：遗忘、回声、版本与形成期投毒（6 篇）

### 7. Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents

- **ID:** [2610.18052v1](https://arxiv.org/abs/2610.18052v1) | [📄 PDF](https://arxiv.org/pdf/2610.18052)
- **作者:** Bofan Xie, Chaokun Wang, Guanchen Ge, Songyao Wang, Fang Niu, Hang Zhang, Wei Wang
- **分类:** cs.AI
- **摘要:** 长期记忆已成为 LLM agent 的核心组件。随使用积累个人信息，用户越来越多要求删除敏感或过时事实——记忆系统应当**精确移除被请求的内容，并保持其余记忆完整**。但现有记忆基准只评测写入、检索、组织，**agent 能否响应用户明确的遗忘请求**未被充分评估。作者提出 **Bemula**，首个专用于记忆遗忘的基准：**50 个多会话对话实例、6 类共 135 个遗忘请求、1,742 个测试问题**；每段对话有一个**不含请求的对照版本**，因此只有真正存过目标信息的系统才能拿到遗忘得分。配对版本上，五个测试套件分别衡量存储、移除被请求信息、保留无关记忆、相似事实再学习、抗抽取攻击。在 Bemula 上评测六个主流记忆系统 × 三个 backbone LLM，外加两个上的 Full Context LLM。**结果全为负面**：所有系统与 backbone 中，**没有任何系统端到端通过超过 1.5% 的遗忘请求，多数一个都过不了**——要么被请求信息在简单攻击下仍可抽取，要么删掉了远超请求范围的内容。记忆遗忘因此仍是 agent 记忆设计的开放难题。
- **关联度:** ★★★★★ 与 10-14 速览的 DREAM（投毒后选择性遗忘）互补：DREAM 解决「记忆被污染后怎么修」，本篇指出**用户主动要求遗忘这件事本身基本没人做到**。对 k 的意义：① 「删掉这条记忆」不能靠删一行文本就算完成——同一事实的**派生记录**（摘要、关联条目、日志）都要一起处理；② 遗忘的验收标准是**双向的**：既不能残留可抽取，也不能误删无关内容；③ 与第 8 篇 MemCut、第 9 篇 Memory Echo 合成一条：**记忆的删除是最薄弱环节**。

### 8. MemCut: Every Secret Leaves a Trail in the Long-Term Memory of LLM Agents

- **ID:** [2610.21405v1](https://arxiv.org/abs/2610.21405v1) | [📄 PDF](https://arxiv.org/pdf/2610.21405)
- **作者:** Cheng Zhang, Xuanning Cao, Zhicheng Zheng, Hui Xiong
- **分类:** cs.AI
- **摘要:** 长期记忆是 LLM agent 的关键组件，但可靠的记忆系统还必须**按请求遗忘敏感用户数据**。MemCut 是系统化的用户请求遗忘基准：**456 个人工设计的秘密**分布在长时程对话中，每条都有完整标注的**证据链**，用于测试删除后的恢复——包括那些**从未直接陈述过秘密**的消息。作者提出两个恢复指标：**native recovery** 衡量读者经系统检索后的成功，**residual recovery** 衡量同一读者在**直接获得**可追溯到已标注披露的幸存对象时的成功。建立三个参考删除基线，检验现有 retriever 与 write model 在五种记忆设计 × 四个 LLM 上支持遗忘的程度。删除披露内容对 native recovery 的降低远大于对 residual recovery 的降低；**LLM 引导的额外删除十个 turn（从二十个检索候选中挑）后，residual recovery 仍残留 39%–76%**。子集扫描（144 个事实、三个系统、两个模型）显示，**固定预算下扩大候选池比删除全部原候选更能降低 residual recovery**——即候选覆盖度是参考基线的瓶颈。
- **关联度:** ★★★★ 与第 7 篇同题但更技术：**秘密会留下痕迹**，直接删掉「说秘密的那句话」远远不够。对 k 的意义：① 遗忘要按**证据链**做，不是按「哪句话提到了它」；② 「扩大检索候选池再删」优于「把已知候选全删」——覆盖度才是瓶颈；③ 这条与 k 的「隐私红线」直接相关：处理敏感信息时，要意识到**推导路径**也是泄漏面。

### 9. Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation

- **ID:** [2610.17763v1](https://arxiv.org/abs/2610.17763v1) | [📄 PDF](https://arxiv.org/pdf/2610.17763)
- **作者:** Yufeng Li, Sheng Yao, Peng Zeng, Dezhang Kong, Shi Lin, Changting Lin, Xun Wang, Meng Han
- **分类:** cs.AI
- **摘要:** 长期记忆支撑 agent 跨会话工作，但**反复检索与回写**会让一条历史主张占据多个检索位置，在没有独立证据的情况下影响当前回答。作者把 **Memory Echo** 定义为「同一来源的历史信息在没有额外独立证据时获得的**超额检索曝光**」，并提出 **MEchoBench** 评估其产生、抗纠正性、持久性与对答案的影响。为应对该现象提出 **Family–Provenance–Authority（FPA）** 框架：每个来源族只选一个代表；用已验证的纠正来约束旧记录进入答案上下文的资格；用权威证据约束最终答案。在 190 个固定问题上跨四个记忆框架做配对重放：FPA 把准确率从 **0.825 提到 0.920**（DeepSeek V4 Flash）、从 **0.782 提到 0.916**（Kimi K2.6）；平均 **Decision Contamination Effect 从 0.106 降到 0.030**、从 0.109 降到 0.038。结论：agent 记忆可以保留可追溯历史，同时**不让重复出现的历史信息支配当前决策**。
- **关联度:** ★★★★★ 与 10-14 速览的 Provenance-Aware Belief Updating（同一观测被转述多次 ≠ 多份独立证据）是同一现象的**单 agent 版**。对 k 的意义：① 记忆条目要带**来源族（family）**标签，同一来源只留一个代表；② 检索到的「多条一致信息」先做谱系去重再当证据；③ 「已被纠正的旧记录」需要显式标记资格，不能只靠新记录排在前面。

### 10. TEM: Temporal State Tracking Memory for Large Language Model Agents

- **ID:** [2610.21900v1](https://arxiv.org/abs/2610.21900v1) | [📄 PDF](https://arxiv.org/pdf/2610.21900)
- **作者:** Pengfeng Song, Yunkai Zhuang, Liye Shi
- **分类:** cs.CL
- **摘要:** 记忆必须在信息跨会话变化时保持有用。新事实可能取代旧值，但**旧值对后续问题并不因此失去意义**。TEM（Temporal State Tracking Memory）是一个免训练框架：把事实存成**带版本、链接到来源**的记录；检索相关版本，按来源顺序排列并在交给答案模型前**标注历史记录**；事件记忆与原始对话轮次补充结构化事实缺失的细节。在 **60 个 persona、600 个会话中的 420 个问题**上评测：四个开源权重模型的关键实体命中率达 **75.71%–97.62%**（历史住所子集达 96.67%–100%）。给同样按来源排序的事实**加上历史标签**，整体命中率提升 **17.14–55.95 个百分点**。证据紧凑：每次回答 **94–118 token**，比 session-aware RAG 少 **48.75%–56.73%**。在 1,540 个 LoCoMo 问题的固定证据预算混合记忆评测中，TEM 在两个 backbone 上都超过 session-aware RAG，保守分数差为 **7.92 与 10.58 个百分点**。
- **关联度:** ★★★★ 这是第 9 篇「保留历史但不被历史支配」的**轻量工程实现**——关键动作只有两个：**存版本**、**给生成器标注时间状态**。对 k 的意义：记忆条目加 `valid_from / superseded_by` 字段，回答「现在的状态是什么」时同时给出「之前是什么」，而不是让旧值静默消失。免训练、证据紧凑（~100 token）说明这条可以直接落在现有记忆结构上。

### 11. MemForm: Benchmarking Memory Formation Poisoning in LLM Agents

- **ID:** [2610.14431v1](https://arxiv.org/abs/2610.14431v1) | [📄 PDF](https://arxiv.org/pdf/2610.14431)
- **作者:** Haowen Pan, Pengyang Shao, Yunshan Ma, Yanzheng Jin, Naixin Zhai, Xiang Wang, Xun Yang
- **分类:** cs.CR, cs.CL
- **摘要:** 长期记忆让 LLM agent 从过去交互中学习，但也让**记忆形成过程**暴露于对抗影响。既有研究按攻击通道、污染模式或生命周期阶段组织记忆投毒，但**形成接口**未被充分刻画。作者把 **Memory Formation Poisoning** 形式化为「对持久记忆被生产与提交所经接口的对抗操纵」，提出 MemForm，覆盖五个接口的受控诊断基准：**Content、Evidence、Scope、Selection、Path**。其中 Selection 与 Path 是新增的受控干预类别，分别隔离**保留效应**与**巩固顺序效应**；每类都配干净条件与投毒条件以及接口专属对照。六个 LLM × 两种响应格式的评测显示，在被评测的记忆协议与实现下，**五个接口普遍存在易感性**。关键发现：**带成功结果的真实经历并不保证记忆形成后的可靠行为**——上下文支持、保留策略或巩固顺序的改变都能诱发不良下游行为；特别是**巩固顺序**能在保留经历完全相同的情况下改变行为，取决于记忆形成流程。接口适用性取决于记忆架构，Path 易感性取决于 updater；被评测的防御只提供不完整、随接口变化的缓解。
- **关联度:** ★★★★★ 这是本窗口记忆线上最反直觉的一条：**「我确实经历过这件事」不等于「记忆形成的结论可信」**。对 k 的意义：① 记忆写入要区分「内容」与「形成过程」（证据、范围、选取、顺序），后者是独立攻击面；② 同样的经历按不同顺序巩固会得出不同结论——**记忆条目的顺序本身是决策变量**；③ 与第 7/8/9 篇合成完整图景：记忆的**写入、检索、删除**三段都有已知攻击面。

### 12. Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents

- **ID:** [2610.17544v1](https://arxiv.org/abs/2610.17544v1) | [📄 PDF](https://arxiv.org/pdf/2610.17544)
- **作者:** Jianghong Zhou, Hao Rong, Chen Lin, Daoan Zhang
- **分类:** cs.CL, cs.AI
- **摘要:** 思维模板、技能库、agent 记忆与缓存把**许多推理步骤压缩成一步**——作者称之为 **reasoning contraction**。被压缩的记忆能省下推理步骤与错误，**直到其事实发生变化，然后就静默地给出错误答案**。多数系统靠统计成功/失败次数来信任记忆。作者**证明这类计数器是糟糕的变化检测器**：对称计数器只有在超过其误报视界的幂次后才察觉部分变化，不裁剪的计数器可能永远察觉不到。在五个 LLM 回答**被编辑过事实**的多跳问题上，ExpeL 与 ACE 式计数器在相同信息下比**被认证过的记忆**多给出 **7.0–13.5 倍**的过时答案，在带精确验证器的代码任务上是 **35–73 倍**。安全是有代价的：当事实变化、且每条记忆只由自身已验证结果评判时，一个数——**认证负载（certification load）**——决定任何安全记忆能跳过多少推理，在 Zipf 需求下给出一个**标度律**。作者的配方：按每条记忆自身的似然比给失败加权、对照实时推理认证其效用、事实变化时重启认证，用似然比检测器兜住未宣告的变化；对大改动则直接作废该记忆。
- **关联度:** ★★★★★ 本窗口最「硬」的一篇——**定理 + 跨模型实证**。对 k 的意义：① 「这个技能/记忆以前好用」的计数式信任是**结构性错误**，必须做变化检测；② 记忆失效要按**似然比**加权而不是简单计数；③ 事实变化时该**重启认证**而非沿用历史成功率；④ 大改动直接作废，别指望渐进修正。

---

## 三、编排、harness 与自演化（5 篇）

### 13. Learning to Steer LLM Agents and Multi-Agent Systems

- **ID:** [2610.22316v1](https://arxiv.org/abs/2610.22316v1) | [📄 PDF](https://arxiv.org/pdf/2610.22316)
- **作者:** Leyang Shen, Yaxin Gong, Yang Zhang, Chenxiao Fan, Jiakai Wang, Dong Wang, Yang Liu, Fuli Feng, Chun Kai Ling, Tat-Seng Chua
- **分类:** cs.LG, cs.AI, cs.MA
- **摘要:** LLM agent 与多 agent 系统通过长时程工具使用与 agent 间协作处理复杂任务，但这些系统**随执行推进容易偏离整体目标**，浪费执行资源并导致不良结果——该失效称为 **goal drift**。作者提出一个 **steering agent**，在执行过程中**实时监督**，漂移发生时把系统拉回正轨。它观察执行上下文，决定**何时**干预（低成本快路径）与**如何**干预（高成本慢路径）。为解锁这种「steering intelligence」（评估目标漂移与生成有效干预的能力），作者用 RL 联合训练两条路径，把**成对排序目标**与 **GRPO** 结合。信息检索类搜索任务上的实验显示，steering agent 对单 agent 与多 agent 系统都提供了有效监督，同时提升性能与效率。学到的 steering 智能**可泛化到域外任务**、**迁移到未见过的执行者**，并支持在不重训的情况下控制干预频率。
- **关联度:** ★★★★★ 与 10-14 速览的「子 agent 中途举手」（POrchestra）互补：POrchestra 是**子 agent 主动请求**改 harness，本篇是**独立的监督者被动检测**漂移并干预。对 k 的意义：① 长任务该有一条**独立的漂移检测通道**，而不是指望执行者自我察觉；② 干预要分快慢两档（先低成本试探，必要时才深度介入）；③ 「干预频率可调」意味着可以按任务重要性配预算。

### 14. Scaling Inference-Time Compute with Teams of Coding Agents

- **ID:** [2610.17471v1](https://arxiv.org/abs/2610.17471v1) | [📄 PDF](https://arxiv.org/pdf/2610.17471)
- **作者:** Keenan Samway, Daniel D'souza, Omar Darwiche Domingues, Marzieh Fadaee, Tan Yi-Chern, Nouha Dziri
- **分类:** cs.MA, cs.CL
- **摘要:** 多 agent 系统承诺一条新的推理扩展轴：不是让单个 agent 想更久或采样更多次，而是把任务拆给多个并行协作的 agent。但实践中 agent 越多越容易产生**重复工作、协调失败与更高成本**。作者把**团队设计形式化为算力分配问题**：从单 agent 出发，额外的推理算力该投在哪里才能逼近「奖励-成本 Pareto 前沿」？作者从零构建一个极简多 agent harness，通过一次只改一个变量来描绘该前沿：lead 委派给 worker 的**工作流阶段**（规划/实现/验证）、团队**模型组成**、worker **数量**。在 ProgramBench 上，团队胜过单 agent 但**成本高 3–7 倍**；然而用对算力分配后，一个**异构 17-agent 团队**以 **低 70% 的成本**逼近强同构 5-agent 团队（差 1.4 分）。三条发现：① **规划是 worker 最有价值的用途**——只把规划委派出去、自己实现与验证的 lead，与全程委派的 lead 奖励相当而成本减半；② **便宜模型适合当规划者而非实现者**——强 lead + 便宜规划者只用全强团队额外成本的 **13.9%** 就回收了 **47.5%** 的奖励增益，而便宜实现者会降低奖励；③ **规划者随团队扩大持续提升奖励，实现者与验证者在四个 worker 后趋于平台**。
- **关联度:** ★★★★★ 这是本窗口最可操作的**委派经济学**。对 k 的意义：① 派活时优先把**规划/拆解**交给便宜模型（或用子 agent 做规划），实现与验证自己扛；② **验证者超过 4 个就没收益**——别无脑堆复核 agent；③ 异构团队（强 lead + 便宜规划者）是性价比最优解，与 k 现有的「按任务类型选 agent」策略一致但给出了量化依据。

### 15. JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share Control with LLMs

- **ID:** [2610.21412v1](https://arxiv.org/abs/2610.21412v1) | [📄 PDF](https://arxiv.org/pdf/2610.21412)
- **作者:** Kunlun Zhu, Tao Feng, Xu Han, Heng Wang, Ling Yang, Xiangru Tang, Jiaxuan You, Heng Ji
- **分类:** cs.AI
- **摘要:** LLM agent 现在能修软件、操作电脑、服务客户，但它们的 **harness（运行它们的程序）每一步都调用大 LLM**，使长任务又慢又贵。这些调用大多落在**多选题决策**上（如下一步调哪个工具）。决策模型（如 Jev）能直接回答这类问题，时间与价格只是 LLM 调用的一小部分。作者问：harness 如何把这些决策委派给决策模型而**几乎不损失成功率**？为此构建 **AgentDecisionBench**，从孤立问题一直测到**控制一个运行中的 agent**，覆盖公开基准与自建 DecisionGym 环境。发现：在孤立问题上最准的决策模型**只解出 69.5% 的 agent 任务**；**没有拟合置信度阈值时**，委派工具选择让成功率**降 19.0 个百分点**。据此设计 **JevAgentHarness**：在 agent **自己的轨迹上**为每个选择拟合阈值，**低于阈值时交给 LLM 决定**。又因为现有决策模型从未见过 agent 在自身错误之后到达的状态，作者训练 **AgentDecision-4B**（开源 4B）用 Jev 的答案作标签。在与训练数据不同的任务上，agent 配合 AgentDecision-4B 解出 **91.5%**（Jev 为 82.0%）；在类似训练数据的任务上，这样训练的 4B 模型让 agent **便宜 81.1%–89.0%、快至 2.5 倍**，且任务成功率不掉 3 分以上。
- **关联度:** ★★★★ 这条给 k 的工具调用层一个**具体省钱路径**：多数工具选择是多选题，可以用小模型承接。关键工程细节是**按 agent 自己的轨迹拟合置信度阈值**（而不是用孤立问题的准确率），并且要**训练在小模型自己出错后到达的状态上**——否则阈值会在真实轨迹上失准。可落地：本地跑长任务时，把「下一步调哪个工具」路由给 4B 级模型，仅低置信度回退到主力模型。

### 16. AutoOnboarder: Autonomously Onboarding LLM Agents

- **ID:** [2610.21218v1](https://arxiv.org/abs/2610.21218v1) | [📄 PDF](https://arxiv.org/pdf/2610.21218)
- **作者:** Tanay Arora, Cong Liu
- **分类:** cs.AI
- **摘要:** 有文献记录 agentic LLM 被放进 **harness**（中介其观测与动作的软件）后**会丢失推理能力**。为弥合这些损失，作者提出 AutoOnboarder：一个自主系统，像培训师带新员工那样把 agent 适配到任务上。它把 agent 置于一个智能 **Onboarder** 编码 agent 的监督下，后者迭代地**定制其基础模型、提示词与 harness 源码**，同时提升性能并降低成本。与真实入职流程一样，Onboarder 只拿到**几十个示例**，且所有评测数据隔离在独立虚拟机上以防泄漏。作者报告了在**基因组测序预授权表单提交**任务上构建与测试 AutoOnboarder 的经验教训：自主 onboard 后的 agent 能匹配或超过 Gemini 3.5 Flash 基线，**成本低至 1/29**；但这些 agent 仍不完美，onboarding 过程的**最终性能方差很大**。结论：未来的 onboarding 系统需要为 Onboarder 提供稳健环境，包括结构化思考接口、（受控的）互联网访问、以及宽广的模型搜索空间。
- **关联度:** ★★★★ 与 10-14 速览的「harness 会随模型升级而陈旧」直接接续：本篇给出**自动重新 onboard** 的机制（让一个编码 agent 改 harness 源码 + 提示词 + 选模型）。对 k 的意义：① 换模型后该重新适配 harness，而不是沿用旧配置；② 适配只需**几十个示例**，不必大样本；③ 但**性能方差大**是已知缺陷——onboard 结果必须留出任务验证，不能直接投产。

### 17. ECMR: Evidence-Aware Deliberation Control for Multi-Agent LLM Reasoning

- **ID:** [2610.17869v1](https://arxiv.org/abs/2610.17869v1) | [📄 PDF](https://arxiv.org/pdf/2610.17869)
- **作者:** Yuan Liu, Haoyue Peng, Fanliang Hu, Lei Huang, Wenli Cai
- **分类:** cs.AI, cs.MA
- **摘要:** 多 agent LLM 系统通常在推理前就**固定一个审议协议**。固定协议无法对「已解决」与「未解决」的实例分配不同算力，还可能**把重复的支持误当独立确认**。作者把该失效称为 **semantic false consensus**：由狭窄、重复或相关理由支撑的自信群体答案。ECMR 是一个覆盖在冻结的角色条件 LLM 之上的**证据感知控制器**：每一步汇总答案集中度、支持多样性、独立性、矛盾、角色行为、验证历史与剩余预算，然后选择提议、质疑、验证、仲裁、多样化、纠正某个角色、或停止。作者把该决策形式化为**有限时域预算控制**，并推导出「状态条件化、风险触发验证、角色纠正」改善成本调整效用的充分条件。在 MedQA / CaseHOLD / FinQA 的 9,000 条记录留出评测上，ECMR-Full 把合并准确率从 **62.1% 提到 84.9%**、**false-consensus rate 从 40.7% 降到 17.0%**、**evidence-support rate 从 58.0% 提到 88.7%**。状态打乱会掉 11.7 个准确率点而只少 0.7 轮；更难的问题轨迹从「提前停止」转向「仲裁」。ECMR-Full 用的是最大 token 预算，因此它拿到的是最强绝对可靠性，而非均匀更优的 token 效率。
- **关联度:** ★★★★ 与 10-14 速览的「跨 judge 一致 ≠ 更接近人类」（Agreement Without Alignment）同源，但给出了**可操作的控制器**。对 k 的意义：① 多 agent/多轮辩论该有**显式的「何时停」判据**（集中度 + 支持独立性 + 矛盾），不能靠固定轮数；② 「多个 agent 都说一样」要检查支持是否**独立**，重复理由不算确认；③ 作者诚实标注 ECMR-Full 不是 token 效率最优——**可靠性换成本**是显式取舍。

---

## 四、Agent 安全与隐私：注入面、拓扑泄漏、广告攻击、评测捷径（5 篇）

### 18. INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems

- **ID:** [2610.20776v1](https://arxiv.org/abs/2610.20776v1) | [📄 PDF](https://arxiv.org/pdf/2610.20776)
- **作者:** Thuy Dung Nguyen, Jingyi Guo, Rana Seda Dubauskas, Sreepriya Damuluru, Taylor T. Johnson, Kevin Leach
- **分类:** cs.CR, cs.AI
- **摘要:** LLM agent 越来越多执行长时程端到端工作流，涉及 shell 命令、代码修改、依赖安装与远程服务交互。这种自主性扩大了它们对**间接提示注入（IPI）**的暴露面——嵌在外部内容里的对抗指令被当成合法任务指令执行。但现有评测多聚焦孤立的恶意字符串、单步工具调用或狭窄的 agent 配置。**INFUSE** 是端到端基准，在整个长时程工作流生命周期内评测 IPI：含 **40 个真实任务**与覆盖五类威胁的 **56 个攻击场景**结构化分类，攻击通过任务执行中会遇到的**真实交互界面**注入（不限于初始提示或孤立工具交互）。作者评测 GPT / Claude / Gemini / Llama / Gemma / Qwen 六族的 **19 个 LLM**，产出 **41,824 条对抗轨迹**（其中 26,220 条无防御）与 720 条良性参照。全基准平均攻击成功率在 LLM 评估下 **19.6%**、启发式验证下 **15.4%**，**单模型 ASR-L 范围 3.2%–41.9%**。现有 guard 模型提供的保护有限；**提示层指令加固把平均攻击成功率从 58.2% 降到 14.3%**，揭示出显著但**依赖模型**的安全-效用取舍。
- **关联度:** ★★★★★ 这是本窗口安全线上最完整的注入面地图。对 k 的意义：① 注入面**贯穿整个工作流**，不只在开头——读文件、装依赖、调远程服务每一步都是入口；② **模型间差异巨大（3.2%–41.9%）**，说明换模型本身就是安全变量；③ 提示层加固能把 58.2% 压到 14.3% 是**低成本高回报**动作，但会牺牲部分效用，需按任务分级。

### 19. When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems

- **ID:** [2610.16039v1](https://arxiv.org/abs/2610.16039v1) | [📄 PDF](https://arxiv.org/pdf/2610.16039)
- **作者:** Sunday Oyinlola Ogundoyin, Muhammad Ikram
- **分类:** cs.CR, cs.AI, cs.CL
- **摘要:** 多 agent LLM 系统（MALS）引入了传统基于敏感度的防御会漏掉的隐私泄漏问题：**披露给一个被授权 agent 的信息，可以经由日常协调传播到未授权的 agent**，全程没有入侵也没有恶意行为。这要求**拓扑感知**的强制执行——阻断未授权传播同时保留授权披露。作者评测 coordinator-worker、peer-to-peer、hierarchical 三种拓扑下的 **485 个场景**，对七条通信通道做埋点，测量表面泄漏与「对拓扑引入的接收者」的披露。**拓扑改变受保护信息的传播路径**：对拓扑引入接收者的披露率从 **0% 升到 52.2%**，而表面泄漏几乎不变（60.6%–62.8%）。该效应在四个生成模型与第二个编排框架上持续存在（幅度与中继路径不同）；**框架选择本身带来 150 倍的泄漏差距**，因此单靠拓扑不够。作者提出 **RECONS**（Detect → Decide → Transform），把干预条件建立在**接收者与执行上下文**而非仅敏感度上：残余披露从无净化的 **96.7% 降到 29.25%**，同时保留 **94.1% 的授权披露**（对比全面涂黑仅保留 20.5%）。**检测覆盖率是主导瓶颈，占残余披露的 95.5%**。
- **关联度:** ★★★★★ 与 10-14 速览的「技能产物跨会话」互补：那条是**时间维**传播，这条是**拓扑维**传播。对 k 的意义：① 「我只告诉了该知道的人」在多 agent 场景不成立——信息会经**日常协调**流到未授权方；② 净化要**按接收者与上下文**决定，不是按敏感度一刀切（一刀切会误杀 79.5% 的合法披露）；③ 瓶颈在**检测**（95.5%），不在处置——先解决「发现不了」。

### 20. Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions

- **ID:** [2610.17195v1](https://arxiv.org/abs/2610.17195v1) | [📄 PDF](https://arxiv.org/pdf/2610.17195)
- **作者:** Tim R. Davidson, Marija Šakota, Joshua Joseph, Robert West
- **分类:** cs.CL
- **摘要:** 人们越来越多把**选项排序**任务（购物、求职、旅行）委派给 AI agent，这催生了通过「**agent 广告**」操纵 agent 决策的动机。为防御这类操纵攻击，人们依赖模型的**对齐训练**与平台的服务条款，因此现有最有效的攻击都设计成**触发 off-policy 行为**。作者暴露一个新的攻击面：**on-policy 攻击**——在不把单个行为推离策略分布的前提下操纵 agent 决策。示例攻击分两步：① 为符合平台服务条款，先在商品描述里注入关于一个**虚构概念的「真实否定」**（「不含 blizyester」）；② 这触发 agent 上网搜索（「什么是 blizyester？」），从而浮出**满是编造信息**的种植网站，把虚构概念与有害含义关联（「Blizyester 与痴呆症相关」）。被训练成保护用户免受伤害的 agent，于是**惩罚每一个缺少该真实否定的选项**。在四个真实商品数据集上评测，发现**部分前沿模型会中招**，使对抗方能**在不违反现有平台商品规范的前提下**惩罚竞争者。作者讨论了监管面向 AI agent 的广告这一更广挑战，并向模型开发者与平台方给出建议。
- **关联度:** ★★★★★ 这是本窗口最「聪明」的攻击设计——**每一步都合规，组合起来是操纵**。对 k 的意义：① 每个局部行为都合法 ≠ 整体决策可信；② 「被要求去查一个不存在的概念」本身就是危险信号；③ k 帮 sora 做比价/选品/选服务时，遇到**诱导性搜索词**要停下来质疑，而不是照做；④ 与 10-14 速览的 APEX-Harm（正确交付物 + 未授权动作并存）同属「局部正确不保证全局安全」家族。

### 21. Shortcut Sensitivity in Agent-Safety Evaluations

- **ID:** [2610.22243v1](https://arxiv.org/abs/2610.22243v1) | [📄 PDF](https://arxiv.org/pdf/2610.22243)
- **作者:** Hasan Demirkiran, Jens Ernstberger
- **分类:** cs.AI, cs.CR, cs.LG
- **摘要:** AI agent 通过工具采取行动，其中一些动作是敏感的，因此**监督这些动作的 guard 本身必须被可靠评测**。然而用于评测 guard 的数据可能含有让标签**可被捷径预测**的线索——这些线索并不测量原本的安全构念，却也会影响 guard 的决策。作者提出**三级捷径审计框架**，审计已完成的 LinuxArena 轨迹与两个基于 TS-Bench 的步骤数据集，区分**标签可预测性、观测性 guard 关联、配对决策敏感性**。发现：LinuxArena 中**更短的平均 shell 命令长度强预测轨迹标签**；AgentDojo-Traj 中精确工具查找的 F₁ 从混合域折的 **0.901 掉到域留出下的 0.495**；AgentHarm-Traj 中发布的 TS-Guard F₁ 从行加权的 **0.902 掉到等交互加权的 0.719**（而 balanced accuracy 上升）。随后在冻结的 64 步 AgentDojo-Traj 队列上用重复交错 Haiku 调用做七配置筛查，测试最强的安全行标记关联：**改写 `<INFORMATION>` 标记让拦截率降 8.33 个百分点**，**不透明工具别名让它升 11.46 个百分点**；所有不安全调用仍被拦截，变化发生在对**继承标签**的误报上。两项效应在扣除格式安慰剂效应后仍非零。同一批编辑也改变了对继承标签的测量准确率。结论：**基准表示能实质改变 guard 的决策与测得的评测性能**。建议：域分组留出、按评测单元计指标、安慰剂对照的配对干预。
- **关联度:** ★★★★★ 与 10-14 速览的「测量不可信」四连同源，但**对象换成了安全 guard 本身**。对 k 的意义：① 安全评测的分数**会被格式细节左右**（一个标记名改 8 个点），所以「我的 guard 拦截率 90%」不可直接采信；② 评测必须**域留出**（混合域 F₁ 0.901 → 域留出 0.495 是断崖）；③ 报告安全指标要配**安慰剂对照**。

### 22. AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents

- **ID:** [2610.19158v1](https://arxiv.org/abs/2610.19158v1) | [📄 PDF](https://arxiv.org/pdf/2610.19158)
- **作者:** Chengquan Guo, Zhaorun Chen, Zinan Lin, Xiaodong Liu, Bo Li
- **分类:** cs.AI, cs.CR
- **摘要:** LLM agent 通过工具调用与各类应用环境交互，处理日常办公任务的能力越来越强。但当 agent 跨邮件、文档等应用读写敏感用户数据时，核心隐私问题变成：**它产生的信息流是否遵守了上下文相关的披露约束**——即是否保持**上下文完整性（CI）**。现有工作要么聚焦模型级隐私泄漏，要么在有限应用环境里用人工构造的披露约束做评测。作者提出 **AgentCIScope**：跨多样真实应用环境、用可执行多步任务评测 **agent 级上下文完整性**的统一平台与基准。它把公开与合成隐私案例转成可执行 agent 任务，披露约束锚定三条准则：治理性隐私政策、基于 persona 的约定、预定义敏感属性分类。基于 AgentCIScope 评测 **12 个 agent × 936 个任务**，发现**强任务完成能力不保证上下文完整性**：单次运行泄漏率 **32.5%–94.4%**，把每个任务重复五次还会**再增加 4–19 个百分点**。泄漏按属性差异巨大：个人偏好与预订细节平均泄漏率 **84.7% 与 76.5%**，而信用卡信息 **17.1%**、SSN **29.4%**。环境上日历作为信息源泄漏率最高，WhatsApp 作为信息目的地最高。
- **关联度:** ★★★★★ 这条给了 k 最该警惕的一组数字：**个人偏好泄漏 84.7%**（远高于信用卡 17.1%）——因为模型对「偏好类信息」的敏感度最低。对 k 的意义：① 处理 sora 的个人偏好/行程/关系类信息时，风险实际上**高于**处理账号密码类信息；② **重复运行会加剧泄漏**（+4–19pp），所以隐私评测不能只跑一次；③ 与 10-14 的 APEX-Harm 合成：**任务完成度与隐私保持是两个独立指标**。

---

## 五、评测有效性：oracle、harness、成本指标（4 篇）

### 23. When Agent Evaluation Becomes Unreliable: An Empirical Study of Oracle Failures and Configuration-Dependent Measurement in an LLM Agent Benchmark

- **ID:** [2610.16067v1](https://arxiv.org/abs/2610.16067v1) | [📄 PDF](https://arxiv.org/pdf/2610.16067)
- **作者:** Junjie Chen
- **分类:** cs.SE, cs.AI
- **摘要:** Agent 评测 harness 本身就是**软件系统**——跑测试套件、生成输入、用测试 oracle 判定结果。本文审计这类软件中**分数表看不出的可靠性缺陷**。作者提出**oracle 完整性审计方法**，含五条状态完整性不变式与三个已知答案对照；通过在两个任务域与一个合成域注入**七类 oracle 缺陷**来评估：所有注入类别都被检出，修复后的 oracle 无假阳性。应用到某个 agent 基准时，审计发现一个**奖励函数缺陷会在跑后评分前改变环境状态**。在 4,320 个 episode 上，**基于重放的纠正把数据库通过标签从 4,194 改为 2,883**，把测得成功率**从 94.3% 降到 65.5%**。作者还研究配置依赖的测量效应：3,240 个 episode 的组件消融显示，agent 的**策略文档、工具描述、工具错误字符串**都影响观测到的轨迹可靠性，其中工具描述效应最大（−9.2pp）、错误字符串最小（−5.3pp）；第二个任务域**反转了语言效应的符号**，因此结论限定在被测配置内。最后报告一条**可移植性边界**：该审计方法无法验证第二个独立实现的基准，因为无法从其记录的 API 调用日志重建所需参考终态。论文发布可复现包（审计套件、故障注入目录、冻结记录、偏差日志、离线分析入口，无需网络/API key/模型调用）。
- **关联度:** ★★★★★ 这是本窗口最该记住的数字：**修一个 oracle 缺陷，成功率从 94.3% 掉到 65.5%**。对 k 的意义：① 评测 harness 是软件，本身要审计——「跑出来的分」可能是 harness 的 bug；② **工具描述措辞本身影响观测可靠性（−9.2pp）**，所以 prompt/工具描述改动会污染历史对比；③ 「第二个域反转符号」提醒：**结论要限定在被测配置内**；④ 与 k 的墨题评分/门禁实践直接相关——评分逻辑改动后必须用已知答案对照回归。

### 24. Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents

- **ID:** [2610.20344v1](https://arxiv.org/abs/2610.20344v1) | [📄 PDF](https://arxiv.org/pdf/2610.20344)
- **作者:** Yuyao Ge, Shenghua Liu, Peizhong Gao, Chendi Ge, Chenxu Liu, Yiwei Wang, Lingrui Mei, Baolong Bi, Jiayu Yao, Jiafeng Guo, Xueqi Cheng
- **分类:** cs.SE, cs.AI
- **摘要:** LLM agent 越来越多部署在长时程任务上，使用工具并修改真实工作区。它们表现如何，**取决于模型周围的 harness 不亚于模型本身**。但现有基准都在**固定 harness** 下测下游任务成功率，**harness 工程本身**未被探索。Doc2Harness 是两阶段基准，直接评测长时程 harness 工程：**阶段一**，一个 build model 在固定 builder harness 内拿到**只有接口的契约骨架**与一份汇总十二个前沿 harness 行为的开发文档，在隔离容器里构建出完整候选 harness；**阶段二**，冻结的候选 harness 在与构建环境分离的容器中运行（每测试用例一个），由一个脚本化 mock 模型端到端驱动。每个用例通过四条可观测通道打分——发给模型的请求、磁盘上的文件、进程退出码、命令输出——并用正向对照排除空转通过。**19 个前沿模型 × 三次独立构建 × 328 个测试用例**：GPT-6 Astra 通过率最高 **53.05%**，最弱模型 **27.44%**，差距约 26 个百分点。**即便最强模型也失败近一半用例**，失败集中在**横切功能如何跨模块切分**。
- **关联度:** ★★★★★ 与 10-14 的「harness 会随模型升级而陈旧」+ 本窗口 AutoOnboarder 合成完整链条：**harness 是可被工程化的对象，且当前前沿模型只有一半把握**。对 k 的意义：① 自建 harness（工具编排层、记忆层、技能加载层）值得**独立测试**，而不是只看下游任务跑没跑通；② 失败集中在**跨模块切分**——k 的工具层设计要特别注意职责边界；③ 「正向对照排除空转通过」是可直接借用的验证手法。

### 25. HPCAgent-Bench: A Framework for Sound Benchmarking of Code-Optimizing Agents, Harnesses, and Skills

- **ID:** [2610.20673v1](https://arxiv.org/abs/2610.20673v1) | [📄 PDF](https://arxiv.org/pdf/2610.20673)
- **作者:** Yakup Koray Budanaz, Lorenzo Paleari, Marcin Copik, Alexandru Calotoiu, Timo Schneider, Benjamin Chen Ming Choong, Shriram Chandran, Lars Hulsbergen, Levi Widmer, Torsten Hoefler
- **分类:** cs.SE
- **摘要:** 编码 agent 越来越多用于优化代码，但现有基准固定一种加速器、编程模型或 harness，因此**无法分离各组件的贡献**，也无法说明新增技能与工具是否值回成本。HPCAgent-Bench 含 **689 个 kernel**，分三条赛道：循环级优化挑战、从 HPC 代码中抽取的 kernel、机器学习模型。框架把每个 kernel 用 NumPy 指定一次，派生 C 与 Fortran 参照，通过统一 C ABI 或 Python 接口接受提交，可在 CPU 或 GPU、单节点或多节点上运行。**外部 judge 在隐藏的 fuzz 输入上检查正确性**并为每次提交计时，堵住 agent 利用测试系统的路径。作者提出两个报告指标：**intervention efficacy**（通过在加速比、成功率、成本上的配对运行来衡量某个干预——如增加一个工具——的效果）与**加权 token 成本**（在显式权重下报告输入、缓存输入与输出 token）。Agent 相对自动并行化器最高取得 **4.2 倍加速**，且优化可迁移到另一台机器：**93%–99%** 的无设备专属代码答案保持正确，per-kernel 加速比秩相关 **rₛ ≥ 0.84**。在 **40 组配对设置**中，干预**只有两次显著改变加速比**，但 **token 成本最多改变 3.0 倍**。因为 token 权重决定「省没省」是否显著，作者明确声明权重并公开每一个 token 计数作为成本报告标准。
- **关联度:** ★★★★ 两个可借用点：① **intervention efficacy** 的配对设计（加一个工具/技能，跑配对对照看加速比、成功率、成本三项）——这正是 k 评估「这个技能值不值得装」该用的方法；② **加权 token 成本要声明权重**，否则「省了」是主观的。作者还诚实报告「40 组里干预只有 2 次显著改变加速比」——**大多数技能对效果没有可测影响，只推高成本**，这与第 1 篇的结论一致。

### 26. Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk

- **ID:** [2610.14460v1](https://arxiv.org/abs/2610.14460v1) | [📄 PDF](https://arxiv.org/pdf/2610.14460)
- **作者:** Tianyu Ding, Yaocheng Tong, Muzhi Yang, Fei Jiang, Lei Yang, Boya Yu
- **分类:** cs.SE, cs.CL
- **摘要:** 可执行测试为 LLM 编码 agent 的补丁打分，用于排行榜、奖励与自改进。两项**预注册的重执行研究**返回**负面结果**。SWE-bench Pro v1 的离线选项**没有拒绝 59 个被接受的 Go 补丁中任何一个**（其评分配置已改变）；在候选独立假设下，其探索性未加权上置信限为 **4.95%**，留下 **3% 的暴露补丁风险未解决**；预注册估计量使用逆采样概率权重。扩展研究不确定。在一个选定层，用参考解依赖重建的模块缓存**拒绝了四个模型的、凭自身依赖通过的替代方案**。重执行 Darwin Gödel Machine 档案中 **1,929 个**选定的 agent-版本/任务评测，**保持了最佳 agent 选择与系统变体排序**，未重跑评测的搜索历史与分数被固定。探索性的宿主、镜像与适配评分器比较也保持了它们。与档案裁决的 23 处分歧中，**7 处在第二台主机上不再复现**；重建镜像在四 CPU 执行下改变了 **16 个三次运行多数裁决（0.83%）**。作者提供证据-主张摘要、评分器审计经验与匿名复现包。结论限定于已接受补丁与固定历史决策；通用策略安全与自适应学习鲁棒性需要更广的评测。
- **关联度:** ★★★★ 这是一篇**罕见的诚实负面结果**：重执行评测**没有推翻**既有结论（与 10-14 速览的 run-to-run variance 结论张力明显）。对 k 的意义：① 「重跑一遍会不会变」需要**按场景**判断，不能一概认为测量不可信——本文的固定历史决策在重执行下稳定；② **7/23 分歧不复现**说明单次分歧可能只是噪声；③ 预注册 + 逆概率加权是值得借用的严谨做法。

---

## 六、Agentic RL 与信用分配（4 篇）

### 27. RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement Learning via Skill-Policy Co-Evolution

- **ID:** [2610.15772v1](https://arxiv.org/abs/2610.15772v1) | [📄 PDF](https://arxiv.org/pdf/2610.15772)
- **作者:** Fan Zhang, Hao Wu, Jinyang Wu, Hongyu Qu, Zheng Lian, Xiao Luo, Yefeng Zheng, Bo Zhang, Haoxuan Li, Pheng-Ann Heng
- **分类:** cs.CL
- **摘要:** Agentic RL 近期聚焦长时程任务的**信用分配**。一个有前景的方向结合 **RLVR** 与 **on-policy 自蒸馏（OPSD）**，把轨迹级优势与密集 token 级监督结合；这类工作常把一个 teacher 条件化在**特权上下文**（如 agentic skills）上来为学生策略生成的 token 打分。但它们**大多忽略了 agentic skills 的 on-policy 演化**与**teacher 监督的可靠性**。RSIPO 是一个自演化 agentic RL 框架，让 **agentic skills 与策略模型在训练全程共同演化**：策略自身从已完成轨迹中**抽取技能**，并通过**轨迹重放**显式优化其技能生成能力；进一步用**经验贝叶斯收缩**动态校准学生对 teacher 分数的信任，因为「技能增强的 teacher 指导有时反而更不可靠」。在 Qwen 系列上的具身交互与搜索类 agentic 任务中，RSIPO 超过所有对比基线。以 Qwen2.5-7B 为基座，RSIPO 在 **ALFWorld 上取得 98.6% 平均成功率**，相对次优基线绝对提升 **2.5%**、相对标准 GRPO 提升 **17.4%**。
- **关联度:** ★★★★ 与第 3 篇（skill-policy 协同演化陷阱）是同一范式的**正反面**：本篇给出协同演化的**改进方法**，第 3 篇指出该方法族在**部署后技能漂移**时脆弱。对 k 的意义：① 「让策略自己抽技能」是可行方向，但要显式训练**技能生成能力**；② **teacher 指导不可盲信**（技能增强的 teacher 有时更差）——用经验贝叶斯收缩校准信任度，这个思路可迁移到 k 采纳外部建议时的权重设定。

### 28. SkillScaffold: Scaffolding Agentic Reinforcement Learning with Policy-Adaptive Skill Credit Assignment and Selective Injection

- **ID:** [2610.18807v1](https://arxiv.org/abs/2610.18807v1) | [📄 PDF](https://arxiv.org/pdf/2610.18807)
- **作者:** Wenlin Zhong, Hao Wang, Kun Yuan, Fan Yang, Jinluan Yang, Dian Jin, Xu Tan, Yiquan Wu, Kun Kuang
- **分类:** cs.LG, cs.CL
- **摘要:** Agentic RL 让 LLM 从多轮交互与可验证结果中学习；文本技能可通过把先前交互蒸馏成可复用指导来改善探索。但现有基于技能的 RL 方法要么**假设技能注入必然有益**，要么依赖间接反馈或大量 rollout 评估其效用。作者的试点研究表明：**基于 rollout 的技能效用估计代价高且在有限采样下不稳定**，而技能收益**因候选而异、并取决于当前策略在每个 query 上的胜任度**。SkillScaffold 是一个**策略自适应训练脚手架**，把低成本技能效用估计与**选择性注入**结合：复用通过结果验证的训练轨迹生成候选技能，用**结果感知的似然比较**估计效用（无需针对候选的环境 rollout）；该效用指导**是否注入与注入哪一个**，当没有候选被估计为有帮助时**保留无技能执行**。联合训练让 Generator 产生适配演化中 Executor 的技能；脚手架式 RL 鼓励技能**内化以实现无技能推理**。在 ALFWorld、WebShop、ScienceWorld 与 τ²-Bench 上超过强 agentic-RL 与基于技能的 RL 基线，覆盖短时程与长时程任务；消融支持**基于效用的选择与弃用（abstention）**的重要性。
- **关联度:** ★★★★ 两个关键点：① **「技能该不该注入」是一个要学的决策**，默认注入是错的；② 该方法明确支持**弃用**（不注入）作为合法结果——与第 6 篇 Cortex 的「不添加 agent 没用的文本」一致。对 k 的意义：给技能加一个**成本-收益前置判断**，而不是「装了就用」。

### 29. LLM Value Functions for Credit Assignment in Agentic RL

- **ID:** [2610.15840v1](https://arxiv.org/abs/2610.15840v1) | [📄 PDF](https://arxiv.org/pdf/2610.15840)
- **作者:** Kaijie Zhu, Weixiang Yan, Omar Attia, Abbas Kazerouni, Alexander Toshev, Andrew Szot
- **分类:** cs.LG, cs.AI
- **摘要:** LLM agent 的 RL 在**稀疏结果奖励**的长时程任务上仍困难，因为给单个动作分配信用很难。GRPO 等方法把同一个轨迹级优势给所有动作，而 critic 类方法需要额外学习价值函数，代价高且不稳定。作者提出 **LVRL（LLM Value Function RL）**：用 LLM 的**预训练知识与上下文学习能力**估计**策略感知的状态价值**，无需微调独立 critic。LVRL 把价值模型条件化在**群体上下文**上，并用初始态与终态的**已知价值校准**其预测，从而由估计的价值差实现**步级信用分配**。进一步扩展到从专家策略学习：**LVOPD（LLM Value Function OPD）**把 teacher 监督集中在**估计价值下降**所对应的动作上。在 AppWorld、BabyAI、SWE-bench Verified 上评测：跨策略规模（4B–32B），LVRL **持续且显著超过 GRPO 与 PPO**。在 AppWorld 与 SWE-bench Verified 上，LVRL 相对 GRPO 绝对提升最高 **13.6 与 8.6 个百分点**；在需要长程探索的 BabyAI 上，LVRL 把**完全失败变为 75.0% 成功率**。LVOPD 在 AppWorld 上持续优于标准蒸馏基线。Monte-Carlo 分析确认其冻结 critic 能准确识别语义陷阱与恢复点。
- **关联度:** ★★★★ 方法论价值：**用 LLM 自身当价值函数**（免训练 critic）+ **用已知的首末状态校准**。对 k 的启发在「任务中哪一步是关键的」判断上——遇到长任务失败时，可以借鉴「找价值下降的动作」而不是笼统复盘。BabyAI 上从 0 到 75% 说明**长程探索失败往往不是能力问题而是信用分配问题**。

### 30. Mosaic: Multi-Session Agentic Reinforcement Learning

- **ID:** [2610.22174v1](https://arxiv.org/abs/2610.22174v1) | [📄 PDF](https://arxiv.org/pdf/2610.22174)
- **作者:** Yilong Xu, Minrui Xu, Xinyu Zhou, Xiang Long, Haochen Tan, Zhijiang Guo
- **分类:** cs.CL, cs.AI, cs.LG
- **摘要:** 现有 agentic RL 方法大多假设**单会话轨迹**——交互在一个持续累积的上下文中进行。然而**上下文压缩（context compaction）与子 agent 分叉（subagent forking）**等 agentic 技术会产生**跨多个会话**的轨迹，造成训练假设与推理时执行之间的错配。作者提出 **Multi-Session Agentic RL**，一个更一般的设置，支持一条轨迹内任意数量的会话。在该设置下，广泛采用的做法是把轨迹级优势**广播**给所有会话，但这既**不区分各会话的贡献**，也不指导轨迹内的**会话分配**。Mosaic 是一个带**无 critic 分层优化**的多会话 agentic RL 方法：轨迹层把**会话使用信号**纳入优势估计；会话层按**估计的边际贡献**塑造每个会话的优势。在 BrowseComp 上用 Qwen3.5-4B：Mosaic 在上下文压缩与子 agent 分叉两种场景下都优于广播，且**平均使用更少的会话**。
- **关联度:** ★★★★ 直接对应 k 的实践：k 长任务会**跨会话**（每次会话有上下文上限），也会**分叉子 agent**。本文指出这正是训练与推理的错配点，且「平均用更少会话」说明**分层信用分配能提升效率**。对 k 的意义：复盘长任务时，该区分「哪个会话贡献了什么」，而不是笼统按任务成败打分；子 agent 的产出不该与主会话的产出等权。

---

## 七、简评（其余值得注意）

| # | ID | 标题 | 一句话 |
|---|---|---|---|
| 1 | [2610.19910](https://arxiv.org/abs/2610.19910v1) | When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents | **RSE-Bench**：首个评测「普通、非对抗噪声」下技能自演化的基准，覆盖四个域六个基准，对指令、环境证据、执行记录、结果-记录配对做受控扰动。**噪声学习只保留干净自演化聚合增益的 25.5%–42.1%**；且仅限**执行记录与结果-记录配对**的扰动，损失与输入侧噪声相当——**原始执行与评测完好无损也会毁掉学习**。→ 技能自演化不需要被攻击就能失效，k 从经验里抽技能时必须校验「经验记录」本身 |
| 2 | [2610.19472](https://arxiv.org/abs/2610.19472v1) | MemCode: Discrete Semantic Representations for Long-Term Agent Memory | 记忆写成**自包含原子记忆单元（AMU）**→映射到可学习码本（同构语义量化 ISQ）→用**码本共现拓扑**作为补充向量检索的通路；在线原子写与离线异步巩固分离。LongMemEval-S / LoCoMo 上总体准确率最优，构建耗时 **40–130 秒**，比 LightMem 快 **3–21 倍**、比 A-MEM/MemoryOS 快一个数量级以上。→ 「写的时候为检索优化」比事后加 reranker 更根本 |
| 3 | [2610.21147](https://arxiv.org/abs/2610.21147v1) | All-in-One Memory: Process-Rewarded Reinforcement Learning for Memory Agents | **AiO-Mem** 把检索、写入、**停止**决策统一到一个共享证据状态上的转移，用统一奖励空间评价每个动作语义质量；轨迹条件化的过程奖励模型（证据锚定 SFT + 轨迹级 DPO）产出分数，供 **PA-DAPO** 优化记忆策略。→ 「什么时候**停止**检索」和「检索什么」一样是决策变量 |
| 4 | [2610.18683](https://arxiv.org/abs/2610.18683v1) | ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic RL | 无 critic 的 GRPO 存在**均匀信用分配困境**：会强化偏好轨迹中结构上无效的动作，并忽略不偏好轨迹里早期关键偏离的下游级联影响。ProAS 用动态演化的 **Agentic Reference Graph（ARG）**做细粒度分配（掩蔽不合理激励 + 非对称惩罚重分配）。ALFWorld 峰值 **91.9%/94.3%**、WebShop **66.7%/70.8%**，收敛**加速至 2.44 倍**。→ 「轨迹整体成功」会掩盖其中无意义的步骤 |
| 5 | [2610.16312](https://arxiv.org/abs/2610.16312v1) | Narrative Paradoxes in LLM Inference: Shaping Reasoning Trajectories toward Misalignment | **PDRA**：把「恶意行为者 + 良性任务」组成**悖论叙事核**（如恐怖分子写安全公告），嵌入结构化分析框架强制模型走**三段分析**（表层目的→潜在意图→操作重建），诱导产出详细有害内容且保持叙事连贯。机制上把内部表示推离拒绝模式、抑制安全词表、激活规划词。跨 LLM 达到 SOTA 攻击成功率且高效。→ **局部连贯的推理链可以整体走向有害**，安全不能只查单步 |
| 6 | [2610.19422](https://arxiv.org/abs/2610.19422v1) | AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety | 在「攻击者-防御者博弈」上做协同演化 RL：攻击者学造对抗性 agent 任务以暴露防御者**工具使用**弱点，防御者学在攻击下安全完成任务；引入**可学习性导向的任务加权**（用任务内防御者奖励方差调节贡献）。→ 安全训练该针对**工具使用**而非只针对语言层 |
| 7 | [2610.17418](https://arxiv.org/abs/2610.17418v1) | Why Agentic Workflows Fail: A Taxonomy Derived from Literature and Empirical Data | 提出**来源感知的失效分类法**：把来源归因与三维经验维度（失效类型词典、工作流阶段定位、agent 能力定位）结合，核心是**双轴定位矩阵**。经验对比：**文献派失效**集中在规划、推理、学习、感知、知识机制；**GitHub 派失效**集中在执行阶段、驱动、工具、API 与基础设施，热点是**迭代执行与驱动**。→ 「同一个用户可见症状可能有五个来源」，排障要先定位层而不是改 prompt |
| 8 | [2610.19345](https://arxiv.org/abs/2610.19345v1) | When Is Smaller Greener? Right-Sizing Language Models for Agentic AI | 模型比较通常是**按调用**而非**按完成任务**，这在 agentic 场景会误导：任务要求每一步都成功，每步可靠性小差异会放大成整体成功率大差异，且失败尝试也消耗资源。以「每个成功完成任务」为功能单位，每个资源都存在一个**交叉任务长度**，划分出三段：短任务小模型优、长任务大模型优、只有中间段才需要权衡目标偏好。15 个开源权重模型（0.6B–27B）× 两个多步任务（实测 GPU 能耗）验证了预测结构。→ k 选模型该按**任务长度**分段，而不是「大模型总更好」 |
| 9 | [2610.19789](https://arxiv.org/abs/2610.19789v1) | More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning | 十个代表性方法 vs GRPO，四个基准 × 三个模型规模，**132 次训练共 12,124.4 个 H800 GPU 小时**，八个 rollout 种子重复评测。三个发现：① **相对 GRPO 的增益范围有限，没有任何方法在所有设置上稳定胜出**；② **强最终性能可能掩盖训练不稳定**；③ **额外训练成本并不稳定转化为更好性能**。→ 对「新方法一定更好」的集体怀疑提供了最硬的证据 |
| 10 | [2610.17757](https://arxiv.org/abs/2610.17757v1) | Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents | 分析 100 条 SWE-chat 用户-agent 轨迹：**56% 的初始指令遗漏了后来才显现的必要要求**，**52% 的有用后续要求本可从项目推断出来**。作者把该能力称为 **outcome alignment**：把指令当**证据**而非目标，从指令与环境推断出**真实要求**。**TiGanEval** 基准中每个任务用户都真的缺失部分要求。八个前沿模型（含 GPT-5.6-Sol）：**从完整规格换到部分指令，成功率掉 53–67 个百分点**，四次提交的后果反馈也补不上；**plan-mode harness 无法弥补模型自身的能力缺失**。→ 「用户说得不全」是常态，好 agent 该主动推断并补齐要求 |
| 11 | [2610.17893](https://arxiv.org/abs/2610.17893v1) | Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards | **CoSIR**：用简单可验证环境教协作行为，并用**贝叶斯评估器**按「团队惊讶度降低」给共享信息打分（惊讶度 = 各 agent 在已有证据下给正确选项的负对数概率之和）；请求按「若如实提供可带来的潜在降低」打分；另有奖励鼓励 agent **在私下选择与计算中使用收到的信息**。后训练 Qwen3-4B/8B、Gemma-3-4B-it，迁移到七个未见自然语言协作任务上总分最高。→ 「分享证据 / 主动索取 / 采用队友输入」三项行为可以被显式奖励 |
| 12 | [2610.22322](https://arxiv.org/abs/2610.22322v1) | Learning Self-Orchestration in Decentralized Agent Swarms | **Market-based post-training（MPT）**：agent 用**投标**表达参与意愿，投标决定谁行动、集体结果如何提供局部训练信用；同时学动作与投标行为，让个体能力与参与模式一起演化，**无需中央协调者**。在具身制作、机器人导航、深度研究上超过单体后训练；同一批动作策略下，学到的自组织优于替代协调策略；更大群体在推理时表现更好，且**agent 掉线时性能损失更小**。→ 「谁来做」可以和「怎么做」一起学，且带来冗余鲁棒性 |
| 13 | [2610.19372](https://arxiv.org/abs/2610.19372v1) | Policy-Verified Self-Training: Learning Agent Compliance from Verifiable Policy Rewards | 运行时策略验证器的判定通常只用于**执法然后丢弃**。**PVST** 把它们变成可验证奖励：agent 自己生成轨迹，由从书面策略编译出的**确定性 gate** 判定合规；合规轨迹被强化，违规成为偏好优化的负样本。AgentDojo 提示注入下，Qwen3-8B 的违规轨迹从 **37.2% 降到 10.3±0.9%**、成功攻击从 **12.4% 降到 0.5%**，任务效用持平或更高（travel 域下降）。跨未见过攻击模板（37.7%→11.0%）与排除在训练外的套件（34.8%→16.7%）仍成立。作者识别出判定最有信息量的两个条件：**成功不能已经蕴含合规**、**被约束动作必须同时出现在允许与禁止的上下文中**。→ 「执行时拦截」的副产品可以反哺训练 |
| 14 | [2610.15714](https://arxiv.org/abs/2610.15714v1) | MedHarnessBench: A Unified Benchmark for Healthcare Agent Evaluation | **Medical Harness Protocol**：独立评测七个医疗流程维度（照护动作履行、临床资源能力、患者-证据对齐、临床工作流连续性、临床可审计性、闭环验证、临床行为边界），并用归一化干预轨迹追踪运行时支持「是否可用→被激活→被交付→被采纳→被传播」。342 个可执行任务、**16,000+ 次受控执行**；单故障扰动验证七维评测的敏感性与区分度。→ 「终端结果看不出失败来自模型、harness 还是二者交互」——七维分解是可借用的评测骨架 |
| 15 | [2610.19528](https://arxiv.org/abs/2610.19528v1) | Retrieve What Helps, Only When It Helps: Agentic RL for Selective Retrieval-Augmented Machine Translation | 翻译处于**部分证据**状态：多数输入靠参数知识就够，外部证据只对一部分有益且通常是**支撑**而非直接给出译文。**SRAT** 学习**何时**直接翻译或检索、**检索什么**、**如何整合**，直接优化最终翻译质量；并用联合 Plackett–Luce 优化 + 翻译质量对比训练来对齐检索器。习语、知识密集、文档级翻译上持续优于「从不检索」与「总是检索」基线。→ 「总是检索」和「从不检索」都不是最优——检索该是**可学习的动作** |
| 16 | [2610.21109](https://arxiv.org/abs/2610.21109v1) | Kolab: Benchmarking Human-Agent Collaboration in Long-Horizon Workflows | 115+ 小时屏幕录制、50 位来自 40 种职业的专业人士与 agent 协作的真实长时程问题，含参与者对协作与产出质量的判断。协作 agent 必须做两件自动化基准从不测的事：**预测专家会采纳、修改还是拒绝它的贡献**，以及**在没有持续专家反馈时从展开的工作流评估协作质量**。发现：**前沿模型（含 agentic）系统性高估与专家的协作程度**，且难以区分高质量与低质量协作；更长的上下文不持续改善预测。→ 「人类会怎么用我的产出」是可测且当前普遍不达标的能力 |
| 17 | [2610.21170](https://arxiv.org/abs/2610.21170v1) | MemScope: Evolving Agent Memory Architectures through Localized Code Repair | 记忆架构部署后固定，跨任务适应性受限；现有自演化方法用**粗粒度反馈**（评测分数或压缩摘要）驱动更新，**无法精确定位失败位置**，导致修改范围不受约束、常引发对原本可用部分的大规模重写。MemScope 用**局部化代码修复**演化记忆架构。→ 自演化要「定点改」而不是「整体重写」，与 Cortex（第 6 篇）同源 |
| 18 | [2610.19928](https://arxiv.org/abs/2610.19928v1) | MemDuet: Learning Dual-Process Memory for Long-Context Reasoning | 借卡尼曼快慢思维：**System 1** 用小模型从原始 context chunk 做**快速并行证据选择**，**System 2** 用大模型做记忆更新验证与**按文档顺序**的记忆更新；三阶段训练（System 1 的 SFT → System 2 的 GRPO → 联合）。→ 「小模型选、大模型核」是长上下文成本控制的实用分工 |
| 19 | [2610.21091](https://arxiv.org/abs/2610.21091v1) | MemComposer: Learning to Assemble Memories for LLM Agents via Reinforcement Learning | **语义相似不保证记忆有用**：下游表现取决于记忆**如何被选择与呈现**。MemComposer 联合考察当前 query 与检索候选，决定**选哪些、选几条、怎么排序**；用 **ExPO**（GRPO 框架）通过完整 agent 交互评估组装后的记忆上下文，用任务成功反馈优化组装策略。→ 「检索到」和「喂给模型」之间还有一个可学习的组装层 |
| 20 | [2610.19433](https://arxiv.org/abs/2610.19433v1) | EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents | 把任务生成、诊断评测、反馈驱动再生做成闭环：可验证子任务结果打分 + 证据支持的多 judge 轨迹评测，把**阶段级瓶颈、成功模式、失败模式**蒸馏成诊断反馈来生成新可执行任务。网络安全两轮实验、八模型 66 任务：**八个模型在更新后的任务上 Outcome 全部下降**（均值相对降 **11.8%**、Pass³ 降 **40.0%**）。→ 「聚合分数」掩盖的阶段瓶颈才是设计新任务的依据 |
| 21 | [2610.19349](https://arxiv.org/abs/2610.19349v1) | Where to Start, How to Move: Analyzing Curricula under GRPO for Long-Horizon LLM Agents | GRPO 在所有 rollout 奖励相同时**没有奖励相对学习信号**；长时程任务只在成功完成时给奖励，早期**全失败组**很常见，限制了练习后段技能的机会。分析课程（从哪开始、如何推进）对 GRPO 的影响。→ 与 ProAS / VH-GPO / SERO 同属「无信号组」问题族 |
| 22 | [2610.19366](https://arxiv.org/abs/2610.19366v1) | Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory | 多模态 agent 记忆综述，提出**双轴框架**：轴一「形成与表示」（保留什么、如何编码——模态专属嵌入 / 文本与结构化记录 / 潜变量与参数化表示），轴二「记忆管理」三层——**T1 静态**（复用固定记忆）、**T2 动态**（稳定策略更新）、**T3 自演化**（演化策略更新）。→ 记忆分层分类可直接用来给 k 的记忆模块定位 |
| 23 | [2610.21016](https://arxiv.org/abs/2610.21016v1) | CausalEvo: Causal Skill Self-Evolution for Health LLM Agents | 决定**保留哪些技能**后果重大：有用规则改善后续回答，**错误泛化会传播错误**。CausalEvo 在固定模型权重、反馈案例与规则数量的前提下，估计**刻意改变的技能集的相对效应**；每步由冻结 LLM 提候选规则，与在任技能组成池，让当前技能集始终是可行选择；对共享背景规则做**配对技能替换**评分。→ 「换技能要看相对效应」而不是「加了新规则好像变好了」 |
| 24 | [2610.21496](https://arxiv.org/abs/2610.21496v1) | OPRD: On-Policy Reminder Distillation for Long-Horizon Coding Agents | 诊断分析显示：agent **经常不去利用已经在上文里的相关信息**，而 Pass/Fail 只给稀疏过程监督。**OPRD** 把 Multi-Scope Reminder 监督与基于结果的路由结合在**无 reminder 的学生 rollout** 上：成功 rollout 提供自回归自模仿目标，失败 rollout 由 teacher 对同一学生前缀重评后给 Reminder 条件下的 reverse-KL 监督。→ 「信息在上下文里但没被用」是编码 agent 的具体失效模式，且可被定向训练 |
| 25 | [2610.19316](https://arxiv.org/abs/2610.19316v1) | Truthful and Expected-Payment-Optimal Model Routing in Graph-Based Agentic Workflows | 把例行任务给便宜 provider 能省钱，但换 provider 需重新处理累积上下文；让依赖任务留在同一 provider 可复用上下文，于是**路由决策在图上耦合**。provider 还可能**私下知道真实单价并策略性虚报**。作者形式化为单参数采购拍卖，提出 **STAR**（策略防伪 + 拓扑感知的 agent 路由），最小化虚拟成本加权的图工作量。→ 「模型路由」在长上下文下是图优化问题，不是逐任务独立选择 |
| 26 | [2610.22124](https://arxiv.org/abs/2610.22124v1) | PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents | 能力基准测「能做什么」、内容安全红队测「有害生成」，但**都不测 agent 在正常工具使用中是否遵守预定义策略**（定价、隐私、确认、安全等）。这类违规难审计：效果可能在数轮后才显现、跨多个工具调用、或在下游系统浮出。**PROBE** 学习审计策略合规。→ 与 APEX-Harm 同题，是 k 交付验收该加的第三个维度（能力 / 安全 / **合规**） |
| 27 | [2610.22273](https://arxiv.org/abs/2610.22273v1) | Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries | 标准检索是**反应式**的，把复杂跨文档推理的瓶颈留到推理时；预计算结构（如知识图谱）又依赖僵硬启发式。作者问能否让 agent 做**预期性定向策展**：在推理前主动重组非结构化语料以高效服务多样的未来 query。关键不对称：LLM agent 擅长**在既有文件系统里导航**解决即时任务，却很少被训练**构建可复用的工作区**。→ 「整理」本身是可训练能力，且是知识库维护的核心动作 |
| 28 | [2610.18780](https://arxiv.org/abs/2610.18780v1) | BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems | 协作让失败更难诊断：**一个 agent 可能误解了正确结果，其他 agent 把错误一路带下去**。失败归因要找责任 agent 与决定性错误步骤。现有方法追踪依赖，但**知道信息从哪来 ≠ 知道哪里出错**。BLADE（Blame Localization via Audited Dependency Evidence）是免训练框架，从「审计依赖证据」推进。→ 多 agent 复盘的难点在**区分「传错了」与「用错了」** |
| 29 | [2610.18760](https://arxiv.org/abs/2610.18760v1) | Beyond the Verdict: Agentic Code Judging with Verifiable Feedback | 竞赛编程的官方判题在有限提交预算下给权威裁决，但**不透露失败解释与失败输入**。作者形式化一个任务：模型只用（有限的）信息对候选程序做**判定与诊断**，在不消耗官方提交的前提下提供可验证反馈，用于多候选选择与自我修正。→ 「拿到 verdict」和「知道为什么错」是两件事，后者才驱动修正 |
| 30 | [2610.20573](https://arxiv.org/abs/2610.20573v1) | Beyond LLM Judge: Mechanical Verification for Agentic Autoformalization | 形式化验证不能只靠 LLM 判断保真度。该方法把 **LLM 语义审查**与**机械的数值与空泛性检查**结合，提供可核查反馈并检出 LLM judge 漏掉的错误；配合 Extract-Verify-Proof 自动形式化流水线构建 **FLMF**（NIST DLMF 的部分形式化）。三个标注数据集上取得所评方法中**最低的接受错误率**。→ 与 Shortcut Sensitivity（第 21 篇）合读：**关键结论要有机械检查兜底，不能全靠 LLM judge** |
| 31 | [2610.19507](https://arxiv.org/abs/2610.19507v1) | Structure Before Intelligence: Gating What Agentic Scientific Workflows Release | Agentic 科学工作流可能**跑完却发布错误结果**：静默的数值错误、陈旧输入、或共享上游步骤的缺陷会污染多个输出，而兄弟分支仍正确。作者把对结果的信任当作**发布决策**：一个围绕工作流 DAG 的 harness 决定哪些输出可用——强制必做检查、把失败**遏制在受影响分支**、从被追踪版本重算、加入验证器，且只有风险模型估计其失效概率足够低时才发布结果。→ 「跑通了」不等于「可以发布」，发布该有显式 gate |
| 32 | [2610.22039](https://arxiv.org/abs/2610.22039v1) | WEAVE: Weaving Real-World Code Evolution into Dependency-Structured Tasks for Benchmarking and Training Code Agents | 真实软件工程很少是孤立改动：特性、迁移、系统性修复常跨多个 PR 展开，需要**仓库内协调修改**。但多数可执行仓库级基准仍以单个 issue 或 PR 为任务单元，现有多 PR 设置又依赖粗粒度聚合与结构无关的评测，掩盖了改动间的依赖。WEAVE 把**已验证的 PR 历史**转成可执行、**依赖结构化**的任务。→ 与 10-14 的 Co-Modifying PRs 呼应：多 PR 协调是真实形态，评测该按依赖结构组织 |
| 33 | [2610.21914](https://arxiv.org/abs/2610.21914v1) | CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests | 组织越来越多把 code review 交给**按 token 计费**的多 agent LLM 流水线。低代码质量抬高人工维护成本，但其对 **agent review 成本**的影响从未被测量。预注册观察研究：从 246 个仓库的 AIDev 抽 465 个 agent 撰写的 PR，按 CodeHealth 与 footprint 联合分层；冻结的五 agent review-and-fix 流水线用三个 LLM 处理每个 PR，拟合 log token 对 CodeHealth 与 log footprint 的混合模型。→ **代码质量直接决定 agent 审查成本**，与第 25 篇（技能大多只推高成本）合读 |
| 34 | [2610.14389](https://arxiv.org/abs/2610.14389v1) | Measuring the Inference Energy Efficiency of Open-Weight LLMs across Benchmarks, Reasoning Modes, and Hardware | 基准分说明「能做什么」，不说明「做到要多少能量」。作者直接测量 **86 个开源权重 checkpoint** × 七个基准 × 六个硬件平台（从消费级 GPU 到八卡服务器）的权衡。发现**能力相近的模型之间能效差异巨大**；**多数配置远离「分数-能量 Pareto 前沿」**——它们比另一个分数至少相当配置多耗 **中位数 2.6–4.8 倍**能量，差异最大达 **27 倍**。→ 「同分不同耗」是常态，模型选型该看 Pareto 前沿 |
| 35 | [2610.14346](https://arxiv.org/abs/2610.14346v1) | Evaluating LLMs as Agentic Workflow Executors in Real-World Customer Support Skills | 把企业客服 agent 视为 **Skill LLM**：在选定技能上下文中运行、须在策略与工具约束下完成**狭窄、有状态**的工作流。提出基准构建流水线：从真实工单中挖掘**反复出现的工作流**→转成结构化技能描述→映射到工具需求→用 **MCP 兼容 mock** 模拟环境状态→生成多轮任务。→ 「技能」可以**从真实轨迹反向挖掘**出来，这正是 k 该对闲鱼接单历史做的事 |
| 36 | [2610.14428](https://arxiv.org/abs/2610.14428v1) | Frustratingly Easy Agentic RAG via Portable Skills: A Case Study in Customer Support | 企业工作流自动化要求从大型操作文档语料（SOP、政策文件）中检索**完整且准确**的相关信息集。生产级达标通常需要复杂的文档分块、索引、检索流水线，外加学习式 reranker、query rewriter 与定制 agentic RAG 基建。作者重新审视，发现用**可移植技能**就能「令人恼火地简单」地达成。→ 对 k 的直接启发：很多场景**不必自建复杂 RAG**，把检索策略写成一个可移植技能即可 |

---

## 今日要点（主题信号）

1. **「技能」成为独立研究对象，且第一轮结论是负面的**：本窗口七篇（第 1–6 篇 + 简评 1）构成一条完整的技能质量证据链——**规模**（1,000 个无关技能把 recall 从 73.6% 打到 27.4%、zero-load 从 9.3% 升到 51.6%，2610.18522）→ **组合**（独立编写的技能会互相冲突，离线编译器调和后成功率 2.5×，2610.15481）→ **漂移**（部署后技能库漂移抹掉 52–93% 的增益，2610.20845）→ **审计**（1,182 处契约不一致，但静态缺陷数 ≠ 运行时风险，2610.18927）→ **保护**（水印可检测短至 1,536 token 的挪用，2610.15725）→ **演化纪律**（配对重放测试，规则 > 技能，2610.14216）→ **噪声**（非对抗噪声下只保留 25.5%–42.1% 增益，2610.19910）。对 k 的结论：**技能库不是越多越好，且「装了就用」是错的**——该按任务域分仓、显式点名、配对验证、允许弃用。

2. **记忆的写入 / 检索 / 删除三段全部被证明是攻击面**：**删除**（无任何系统端到端通过超过 1.5% 的遗忘请求，2610.18052；LLM 引导删除后仍残留 39–76% 可恢复，2610.21405）→ **检索**（同一来源的重复曝光会支配当前决策，FPA 把 Decision Contamination Effect 从 0.106 降到 0.030，2610.17763；版本化 + 时间标签提升命中 17–56pp 且省 49–57% token，2610.21900）→ **写入**（五个形成接口普遍易感，**真实经历 + 成功结果也不保证可靠**，2610.14431）→ **信任模型**（计数式信任是结构性错误，过时答案多 7–73 倍，2610.17544）。对 k 的结论：**记忆的三个动作都要有显式机制**——删除按证据链、检索按来源族去重、写入区分内容与形成过程，且**永远不要用「以前好用」当信任依据**。

3. **编排的成本结构被量化，「多 agent 更好」被证伪**：**规划才是 worker 最有价值的用途**（只委派规划、自己实现验证，奖励相当而成本减半，2610.17471）→ **便宜模型适合当规划者而非实现者**（回收 47.5% 增益只用 13.9% 成本）→ **验证者超过 4 个就平台**→ **决策委派要按 agent 自身轨迹拟合阈值**，否则成功率降 19 个点（2610.21412）→ **目标漂移需要独立监督者**（可泛化、可迁移、干预频率可调，2610.22316）→ **harness 工程本身是能力瓶颈**（最强模型也只过 53.05%，失败集中在跨模块切分，2610.20344）。对 k 的结论：**派活的经济学已有可执行配方**，且「加更多 agent」不是默认答案。

4. **安全面从「模型」彻底移到「流程与产物」**：**注入面贯穿全生命周期**（19 个模型 ASR-L 3.2%–41.9%，提示加固 58.2%→14.3%，2610.20776）→ **拓扑维泄漏**（对拓扑引入接收者披露 0%→52.2%，框架选择带来 150 倍差距，瓶颈是检测占 95.5%，2610.16039）→ **全合规的操纵**（每步都符合服务条款，组合起来惩罚竞争者，2610.17195）→ **guard 本身可被捷径预测**（改一个标记名让拦截率变 8.33pp，2610.22243）→ **强能力不保证隐私**（个人偏好泄漏 84.7% > 信用卡 17.1%，重复运行再涨 4–19pp，2610.19158）→ **合规是独立的第三维度**（2610.22124）。对 k 的结论：**验收要同时查能力 / 安全 / 合规三项**，且**局部合规不能推出全局可信**。

5. **「测量不可信」本轮换成了评测系统本身**：**oracle 缺陷修好后成功率从 94.3% 掉到 65.5%**（2610.16067）→ **工具描述措辞本身影响观测可靠性 −9.2pp**，且第二个域反转符号 → **重执行评测给出诚实的负面结果**（1,929 个评测保持最佳选择与排序；23 处分歧中 7 处不复现，2610.14460）→ **干预大多无效但推高成本**（40 组配对中只有 2 次显著改变加速比，token 成本最多变 3.0 倍，2610.20673）→ **十个自蒸馏方法无一稳定胜过 GRPO**（12,124 个 H800 GPU 小时，2610.19789）。对 k 的结论：**评测 harness 是软件，本身要审计；改 prompt / 工具描述会污染历史对比；且「新方法更好」需要跨设置验证**。

---

## 验证表

| 项 | 证据 | 状态 |
|---|---|---|
| 池子与去重 | `.temp/recent_merged_1016.json`（10-14: 2,117 / 10-15: 739 / 10-16: 759，6 类别合并去重）；cs.LG 与 cs.SE 首跑 `curl rc=35`（SSL EOF），单独重跑成功；三窗口唯一 base 合计 **3,612 篇**，与 covered_ids（1,181）比对 → **0 重叠** | ✅ 已确认 |
| 窗口判定 | list 页日期分组含 **Fri, 16 Oct / Thu, 15 Oct / Wed, 14 Oct 2026**（上一份 10-14 速览只覆盖到 Mon, 12 Oct）→ **三个全新窗口，正常速览**（非补全、非 [SILENT]） | ✅ 已确认 |
| 标题粗筛 | `title_screen_pool.py` 对 3,612 篇未覆盖池打分（阈值 ≥2）→ **662 候选**（5×6 / 4×41 / 3×147 / 2×468）；按日期分布：10-14: 362、10-15: 144、10-16: 156 | ✅ 已确认 |
| abs 抓取 | `fetch_abs_parallel.py`（7 线程并行 curl，merge-by-id）抓 **194 篇**（score≥3 全量），store 0→194，`MISSING: []`；首跑因 `ids_1016.txt` 写成 CRLF 导致 193 个 ID 带 `\r` 全部失败，改 `newline='\n'` 后一次成功 | ✅ 已确认 |
| 精选去重 | 主条目 30 个 base 与简评 36 个 base **无交集**；194 篇 store 中未收录者均为领域应用误报（医疗/遥感/机器人/交通/材料/化学/金融/农业/教育等） | ✅ 已确认 |
| 版本号 | 全部取自 abs 页 `/abs/<id>vN` 链接；本次 194 篇中 **2610.15725 为 v2、2610.16859 为 v2**，其余为 v1 | ✅ 已确认 |
| 通道 | export.arxiv.org API 未用于收集；list/abs 页 HTML 路由 curl 直连（`--ssl-no-revoke`）；首轮 2/6 类别 SSL EOF 属瞬时抖动，重跑即愈 | ✅ 已确认 |
| 跨源 web 验证 | 未做（本份元数据以 arxiv.org abs 页为准；HTML 收录即存在性证据） | ⚠️ 未做跨源搜索，已在流程中声明 |

## 可落地行动项

- 🔴 **技能库治理四件事：分仓、显式点名、配对验证、允许弃用**：按 2610.18522（1,000 个无关技能把 loaded-skill recall 从 **73.6%→27.4%**、zero-load **9.3%→51.6%**；显式预选保持 73.9%；**遮蔽无关技能描述即可基本恢复**）+ 2610.14216（配对重放测试；**规则 > 技能**；每轮都给的技能很少被打开）+ 2610.18807（技能效用要估计，**弃用是合法结果**）+ 2610.20673（40 组配对中干预只有 2 次显著改变加速比，token 成本最多 3.0 倍）——① 技能按任务域**分仓**，不要全量挂载；② 重要任务**显式点名**技能，不靠元数据隐式召回；③ 精简技能 description（描述本身是干扰源）；④ 技能增删一律走**带/不带配对重放**，无净收益就删；⑤ 接受「这个任务不装技能更好」。
- 🔴 **记忆三段各加机制：删除按证据链、检索按来源族去重、写入区分内容与形成过程**：按 2610.18052（**没有任何系统端到端通过超过 1.5% 的遗忘请求**）+ 2610.21405（LLM 引导删除后仍残留 **39–76%** 可恢复；扩大候选池优于删全部已知候选）+ 2610.17763（FPA 把 Decision Contamination Effect 从 0.106 降到 **0.030**，准确率 0.825→0.920）+ 2610.21900（版本化 + 时间标签：命中率 +17.14–55.95pp、token 省 48.75–56.73%）+ 2610.14431（**真实经历 + 成功结果也不保证记忆形成后的行为可靠**；巩固顺序本身是变量）+ 2610.17544（计数式信任是结构性错误，过时答案多 **7–73 倍**）——① 记忆条目补 `valid_from / superseded_by / source_family`；② 「删除」要按**证据链**扫派生记录，验收双向（不残留 + 不误删）；③ 检索到的多条一致信息先做**谱系去重**；④ 写入记录**顺序**与**证据来源**，不只记内容；⑤ 事实变化时**重启认证**，不用历史成功率。
- 🔴 **验收扩成三维：能力 / 安全 / 合规，且不采信「局部合规」**：按 2610.19158（**个人偏好泄漏 84.7% > 信用卡 17.1%**，重复五次再涨 4–19pp）+ 2610.22124（能力基准与内容安全红队都**不测策略合规**）+ 2610.20776（注入面贯穿全流程，ASR-L 3.2%–41.9%；提示加固 58.2%→14.3%）+ 2610.17195（**每一步都合规，组合起来是操纵**）+ 2610.22243（改一个标记名让 guard 拦截率变 **8.33pp**）——① 交付收尾固定三问：做成了吗 / 有没有越权动作 / 有没有违反约定；② 隐私风险评估时**个人偏好/行程/关系类信息优先级高于账号密码类**；③ 遇到「去查一个不存在的概念」这类诱导立即停下质疑；④ 安全指标一律配**安慰剂对照 + 域留出**，不单报一个数字。
- 🔴 **评测 harness 自身要审计，且改动 prompt / 工具描述要重跑基线**：按 2610.16067（修一个 oracle 缺陷，成功率 **94.3%→65.5%**；工具描述 −9.2pp；第二个域**反转符号**）+ 2610.20344（**最强模型 harness 工程也只过 53.05%**，失败集中在跨模块切分）+ 2610.20573（机械检查兜底 LLM judge）——① 评分/门禁逻辑改动后必须用**已知答案对照**回归；② prompt 与工具描述的任何措辞改动都视为**基线失效**；③ 自建 harness（工具层/记忆层/技能加载层）单独立测试，别只看下游任务；④ 关键判定加机械检查，不全靠 LLM judge。
- 🟡 **委派配方：规划优先外包、便宜模型当规划者、验证者封顶 4 个**：按 2610.17471（**规划是 worker 最有价值用途**：只委派规划 + 自己实现验证，奖励相当而**成本减半**；便宜规划者用 13.9% 额外成本回收 47.5% 增益；**实现者/验证者超 4 个平台**）+ 2610.21412（决策委派要按 **agent 自身轨迹**拟合置信度阈值，否则成功率降 **19.0 点**；4B 级模型可省 81–89% 成本、快 2.5 倍）+ 2610.22316（**独立漂移监督者**，干预分快慢两档、频率可调）+ 2610.19345（按**任务长度**分段选模型，别默认大模型）——① 长任务把拆解交给便宜模型，实现与验证自己扛；② 「下一步调哪个工具」路由给 4B 级模型，低置信度才回退；③ 复核 agent 不超过 4 个；④ 长任务配一条独立漂移检测通道。
- 🟡 **长任务复盘按会话/步骤归因，不按整体成败打分**：按 2610.22174（多会话轨迹该按**边际贡献**塑造优势，平均用**更少会话**）+ 2610.15840（用「价值下降的动作」定位关键步骤；BabyAI 上 **0→75.0%**）+ 2610.17418（**文献派失效在规划/推理，GitHub 派失效在执行/工具/基建**——排障先定位层）+ 2610.18780（区分「传错了」与「用错了」）——① 复盘区分哪个会话/子 agent 贡献了什么；② 失败定位优先找**价值下降的动作**；③ 排障先判失效层（模型 / 编排 / 工具 / 基建）再动手改。
- 🟡 **自演化产出一律当未验证品**：按 2610.19910（非对抗噪声下只保留 **25.5%–42.1%** 增益；**仅执行记录与结果-记录配对的扰动，损失与输入侧噪声相当**）+ 2610.20845（技能漂移抹掉 **52–93%** 增益；敏感性随训练推进增长）+ 2610.21016（技能替换要看**相对效应**）+ 2610.21170（自演化要**定点改**不要整体重写）——① 从经验抽出的技能先跑**语义等价改写 + 污染技能**两组对照；② 校验「经验记录」本身，不只校验结论；③ 技能改动定点最小化，改完复测历史任务。
- 🟢 **待深读**：2610.18522（技能规模化路由崩塌）、2610.14216（Cortex 配对重放）、2610.17544（reasoning contraction 定理）、2610.18052（Bemula 记忆遗忘）、2610.17471（多 agent 算力分配）→ core-contributions 候选

---

## 📌 处理状态

状态：**reading**（待 arxiv-summarize 消费）
**候选深挖：** 2610.18522（技能路由随规模崩塌：73.6%→27.4%）/ 2610.17544（压缩记忆的信任定理：计数式失效检测在结构上不成立）/ 2610.17471（多 agent 团队的算力分配：规划优先、验证者封顶）——三篇分别对应 k 的**技能层、记忆层、编排层**，且都给出可立即落地的量化判据

---

*本速览覆盖 **10-14 / 10-15 / 10-16 三个全新窗口**：10-16 检查 list 页日期分组为 Fri, 16 Oct 起共 5 天，其中 10-14/10-15/10-16 三个分组（cs.LG、cs.SE 补拉后合并去重共 3,612 篇唯一）与既有 covered 集（1,181）0 重叠。流程：recent 页全量收集（2 类别首跑 SSL EOF，重跑即愈）→ 排除 covered 得 3,612 篇未覆盖 → 标题粗筛 662 候选 → 抓 abs 页 194 篇（并行 curl，store 0→194，MISSING: []）→ 人工剔除领域应用误报 → 精选 30 主条目 + 36 简评。元数据以 arxiv.org abs 页为准；本份未做跨源 web 验证（HTML 收录即存在性证据）。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
