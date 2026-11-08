---
aliases:
  - arxiv-2026-11-08-agent-llm
  - arxiv-agent-llm-2026-11-08
tags: [arxiv, research, ai-agent, llm, daily]
created: 2026-11-08
updated: 2026-11-08
status: adopted
source: arxiv.org HTML 搜索端点（start_date/end_date 精确日期窗 + 相关度排序 + 完整摘要）+ 逐篇 abs 页复核版本号与作者
---

# arXiv AI Agent / LLM 速览 — 2026-11-08

> **⚠️ 补全性质声明**：索引仍冻结。实测 `cat:cs.AI` 按提交日期倒序的最新条目依旧是 `2611.08483v1`（2026-11-05T18:59Z）；HTML 搜索端点用 `start_date=2026-11-06 & end_date=2026-11-08` 查询返回 **0 条**。也就是说 11-06 / 11-07 / 11-08 三天没有任何新提交被公布——周末投稿按 arXiv 公告节奏要等周日 20:00 ET（周一 09:00 CST）才出批次。
> **那今天写什么**：同一批 11-05 的论文，11-07 那份只补了 24 篇，覆盖仍是少数。今天换路线——不走 API（易限流），直接打 arXiv **HTML 搜索端点**，用相关度排序 + 精确日期窗拿到 150 篇带完整摘要的 11-05 论文，其中 **125 篇此前从未被收录**，逐篇读摘要后选出 **24 篇**分六组。
> **数据源**：arXiv abs 页原文摘要与论文自报数字；未做跨源 web 验证；ID 保留版本号（全部 v1）防引用漂移。同批次论文 Semantic Scholar 引用数尚无可比意义，故不列。
> **这一份的三句话**：① 编码 agent 的失败大多是**「跑通了但结果是错的」**——迁移后 41% 的错误修复能过全断言门禁，一条来自 release note 的边界输入就能把漏放率压到 6.5%；② 轨迹级失败预测器基本没学到「这一次 run」——issue 难度一个不看 run 的参考分就有 AUROC 0.92，轨迹预测器只有 0.62，所以「换模型」的收益不超过随机波动，**该重试而不是该换模型**；③ 省钱靠**保留执行知识**而不是换更强模型——标准化复现工件把成功率从 76.4% 拉到 92.6%，还顺带把 API 花费降了 19.7%。

---

## 一、评测与可靠性：数字到底在测什么（5 篇）

### 1. XStack: A Benchmark for ML Repo Migration

- **ID:** [`2611.08472v1`](https://arxiv.org/abs/2611.08472v1) | [📄 PDF](https://arxiv.org/pdf/2611.08472)
- **作者:** Linrong Cai, Taiming Lu, Haozhe Chen, Zhuang Liu
- **分类:** cs.LG / cs.AI | **提交:** 2026-11-05
- **摘要:** ML 代码应该跑在研究者选择的地方，而不是它最初被写下的地方。今天 ML 代码基本只活在两个生态里：PyTorch + NVIDIA GPU、JAX + Google TPU。跨这两个生态迁移仓库意味着跨框架、跨硬件地构建与测试。作者把「迁移」本身做成基准：agent 收到一个 PyTorch 仓库和一台干净的 TPU 机器，必须交出一个 JAX 仓库，判分依据是**源仓库已发表的结果**（由作者认证并校准）。结果很不乐观：**Claude Opus 5 通过率 75%，GPT-5.6-sol 45%，其余所有 agent 不超过 40%**。
- **关联度:** ★★★★ 这是「整仓多文件一致性」任务的标准形态，和 sora 让 Codex 改墨题后端、迁移依赖是一类问题。可落地：验收锚点用**原仓库已发布的结果**（测试/指标），而不是「能跑起来」；迁移类任务先要一份可执行的对拍基线。

### 2. Hard Issue, Weak Model, or Bad Run? Rethinking Failure Prediction for Coding Agents

- **ID:** [`2611.08285v1`](https://arxiv.org/abs/2611.08285v1) | [📄 PDF](https://arxiv.org/pdf/2611.08285)
- **作者:** Xingyue Shi, Wesley K. G. Assunção
- **分类:** cs.SE | **提交:** 2026-11-05
- **摘要:** 轨迹式失败预测器读 agent 的部分轨迹，判断这次 run 是在往对的方向走还是走歪了，走歪就中止、重试或换模型。作者问：这些预测器真的学到了「这次 run」吗？在 SWE-bench Verified 上（每个模型对每个 issue 只跑一次），两个**与 run 无关**的因素主导了预测器表现：① **issue 难度**——一个完全不看 run、只看「这题对别的模型有多难」的参考分就能到 **AUROC 0.92**，而轨迹预测器只有 **0.62**；② **模型能力**——同一 issue 内，知道是哪个模型跑的，比预测器本身还准。除掉难度和能力之后，**轨迹带来的增益统计上等于零**。这个混淆也污染了下游动作：换模型的理论收益来自「最好单模型 vs 任意模型 oracle」的差距，而这个差距**不超过随机波动**；按 issue 换模型在留出集上零收益。重复跑实验里，同一个模型对同一 issue 有时成有时败——**重试确实有修复空间，但只救「坏 run」，救不了「超出能力」**，而现有预测器分不清这两者。
- **关联度:** ★★★★★ 直接改写 k 的失败处理规则。现状是「3 连败即停」——方向对，但停完该做的是**同模型重试 + 加预算**，不是换模型。可落地：① 失败归因先分「题难 / 模型弱 / run 坏」，只有连续多次同模型失败才判定为「超出能力」；② 换模型只在能力档位明确不足时做，不做「按题切换」。

### 3. Accepted but Wrong: Silent Failures of LLM Code Repairs after API Migrations

- **ID:** [`2611.08269v1`](https://arxiv.org/abs/2611.08269v1) | [📄 PDF](https://arxiv.org/pdf/2611.08269)
- **作者:** Xiaobo Chen, Genliang Zhu, Ziyuan Wang, Chu Wang
- **分类:** cs.SE / cs.AI | **提交:** 2026-11-05
- **摘要:** 运行时或 API 迁移之后，LLM 修好的函数**能干净跑完却返回错误结果**，而基于典型测试输入的发布检查会把它放出去。作者做了预注册研究：73 个任务、覆盖 CPython / 某数据库库 / SQLite 的 60 处有文档记录的变更，每个候选都在**真实运行时**上对着 withheld contracts 执行。全量修复空间上，**典型输入的全断言门禁放过了 0.410 的错误修复**；从 release note 里写出的**一条边界输入**把它压到 **0.065**（15 个未见簇上 0.061）；让一个没看过程序的盲写模型（GPT-5.6-luna）写三条输入，达到 0.070。继续加难：菜单扩到 1,491 个片段、再加 233 个在典型输入上与旧输出一致的**硬干扰项**后，边界输入仍有 0.168、前沿模型写手 0.153 的错误程序通过——说明难度可以无限逼近，但边际收益仍然可观。四个模型族里，边界输入在三套菜单、三个开放权重族上都降低了错发率（如 0.233→0.057），且不降低正确完成率。
- **关联度:** ★★★★★ 这就是 sora 刚踩的坑：pydantic ABI 错位（3.14 解释器调 cp311 扩展）——「装上了、导入了、没报错」，但语义是错的。可落地：任何迁移/依赖修复，验收必须加**一条从 release note 抄来的边界输入**（不是自己想的典型输入），这一条把漏放率降了 6 倍。

### 4. Measuring the Marginal Value of Verifier-Based RL Beyond Supervised Fine-Tuning

- **ID:** [`2611.07639v1`](https://arxiv.org/abs/2611.07639v1) | [📄 PDF](https://arxiv.org/pdf/2611.07639)
- **作者:** Amit Sagtani, Saloni Garg
- **分类:** cs.LG / cs.AI | **提交:** 2026-11-05
- **摘要:** RLVR 通常被当成 SFT 的替代或后续阶段，隐含假设「RL 阶段自己有增益」。作者直接测这个增量：自建 `gpu-train-debug`，1,877 个合成 GPU / LLM 训练故障诊断任务、30 个原型，程序化 verifier 给部分分，难度校准到中档模型落在 0.60–0.75。试点就出意外：**1,200 条 gold 示范几乎把基准解了**（硬 split 上 SFT 0.785），而 **15 步 GRPO 完全没动**（0.314 vs 基线 0.311）。于是作者在正式跑之前**书面修改研究问题**：验证型 RL 在示范之外还能加什么？预注册规模（60 步 GRPO、lr=1e-6）的答案：**分布内 +0.22 分，95% CI [−0.06, +0.51]，无可检测提升**；**分布漂移下 +0.33 分，CI [+0.02, +0.68]，小幅但可测**。SFT 吃掉了大部分可得增益；SFT 残留的错误大多是**系统性、跨样本一致**的，这恰恰削弱了 GRPO 需要的组内信号。整个研究只花了 **$8.69** 算力，且可从归档生成物、冻结配置和带 tag 的代码完全复现。
- **关联度:** ★★★★ 对「微调就能提升」的期待降温：先看 SFT 天花板，再谈 RL。可落地：任何自训/微调实验先报三个数——SFT 后的分数、RL 后的分数、两者的 CI；只有 CI 不跨 0 才叫有效。

### 5. ReproBridge: Building Reproducibility into ML Research Artifacts

- **ID:** [`2611.08452v1`](https://arxiv.org/abs/2611.08452v1) | [📄 PDF](https://arxiv.org/pdf/2611.08452)
- **作者:** Yubo Wang, Rui Meng, Jaehyun Nam, Tomas Pfister, Jinsung Yoon
- **分类:** cs.AI | **提交:** 2026-11-05
- **摘要:** 复现 ML 实验要从论文、发布代码、辅助工件里拼出过程。对编码 agent 来说，复现成功往往取决于它们能不能**补齐缺失细节**，而不只是工件本身。作者定义一套标准工件设计——精修代码库、环境安装、实验启动器、复现指南——并提出 ReproBridge 这个构建工件的工作流。ReproBridge-Bench 含 **1,029 个任务、387 个实验、36 篇论文**，每个任务配 5 个人工核验的参考分；独立 Auditor 检查执行证据。四个模型上，精修工件把平均复现成功率从 **76.4% 提到 92.6%**，下游 API 花费平均**降 19.7%**，跨模型成功率差距从 **21.6pp 收窄到 3.9pp**（四个模型全部 >90%）。消融显示任何组件拿掉都掉分，其中**代码与环境**影响最大。
- **关联度:** ★★★★★ 这条最省钱：提升不来自更强模型，来自**把执行知识写下来**。可落地：sora 的交付包（论文服务/数模/PCB）统一四件套——精修代码 + 环境脚本 + 一键启动 + 复现指南，验收时用 Auditor 式检查（不是「我跑过了」而是留下执行证据）。

---

## 二、编码 Agent 与「理解债」（4 篇）

### 6. Cognitive Tours: Making Understanding a Deliverable in AI-Assisted Development

- **ID:** [`2611.08456v1`](https://arxiv.org/abs/2611.08456v1) | [📄 PDF](https://arxiv.org/pdf/2611.08456)
- **作者:** Margaret-Anne Storey
- **分类:** cs.SE | **提交:** 2026-11-05
- **摘要:** Agentic coding 在加速开发，也带来技术债之外的两种更不显眼的债：**认知债**（团队共享理解缺失，没人能自信解释系统怎么运作、改动会波及什么）和**意图债**（目标、约束、理由没有被清晰表达，系统「为什么这样」无从追溯）。作者提出 Cognitive Tours：一个 web 原型，让人创建并沿「curated path」走——路径串起用户需求、设计决策、代码、测试、开放问题；AI 技能负责审计已有 waypoint 与 tour 是否过时、是否有问题、并建议新增候选，**人负责决定什么重要、验证关系、构建叙事**。这种分工是刻意保留「productive friction」：挑选、解释、修订 tour 的过程本身就是理解的形成与传递。
- **关联度:** ★★★★ 知识库的 MOC 就是 tour，但 k 现在只做「链接」，没做「叙事」。可落地：给核心项目（墨题 / PCB 工作流）各写一条 tour：需求 → 设计决策 → 代码位置 → 测试 → 未解问题，并标出哪几段已经 stale（AI 审计、人确认）。

### 7. ReConMem: A Graph-Based Dual Memory System for Repository-Oriented Conversations

- **ID:** [`2611.07759v1`](https://arxiv.org/abs/2611.07759v1) | [📄 PDF](https://arxiv.org/pdf/2611.07759)
- **作者:** Zhishuo Yang, Li Zhang, Yang Liu, Donghao Yang, Fang Liu
- **分类:** cs.SE | **提交:** 2026-11-05
- **摘要:** 仓库级迭代开发里，助手必须同时用上**演化中的对话历史**和**仓库上下文**。现有记忆系统是为通用对话设计的，没有把对话信息和它指向的代码实体协调起来。ReConMem 提出图式双记忆：把蒸馏后的对话记忆与对话相关代码实体组织成**语义图 + 结构图**，并随交互演化维护跨图关联；召回时用**代码草稿做查询落地**（code-draft-based query grounding）把自然语言和代码对齐，再沿图内/图间关系扩展，并按结构粒度压缩检索到的代码。LoCoEval 上 Pass@1 比最强基线高 **7.917 / 7.292 个百分点**（单跳 / 多跳），上下文压缩程度相当；CodeAssistBench 上 **27.61% Correct / 44.03% Partially Correct**，比「全量历史」高 4.10 / 7.09 个百分点，交互质量也更好。
- **关联度:** ★★★★ 记忆要挂在**代码实体**上，而不是纯文本块。可落地：给墨题项目建一份「实体记忆」——文件/函数/表名 ↔ 相关决策与踩坑，用代码片段当检索键，而不是靠自然语言回忆。

### 8. SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking

- **ID:** [`2611.07558v1`](https://arxiv.org/abs/2611.07558v1) | [📄 PDF](https://arxiv.org/pdf/2611.07558)
- **作者:** Moonseok Choi, Jongwon Jeong, Minki Kang, Giung Nam, Juho Lee
- **分类:** cs.CL / cs.AI | **提交:** 2026-11-05
- **摘要:** Agent 越来越多在**结构化生成**（grammar 约束输出格式）下部署，而现有压缩方法都针对无约束生成。作者先指出一个根本错配：结构化生成把输出分布压到合法 token 上，**logits 只在少数决定 agent 动作的位置才真正重要**。据此提出 SKIM——首个面向结构化生成下 LLM agent 的剪枝 + 蒸馏框架，两个阶段都由 token 角色引导：把位置分成 context / decision / format 三类，① 类别感知的剪枝显著性分数，优先保住对 decision 位置最相关的参数；② on-policy 蒸馏，让学生在**合法 token** 上对齐教师，并配类别感知的特征匹配。在工具调用基准和多步 agent 循环上、跨多个模型规模与稀疏度，SKIM 都稳定优于基线，**高稀疏率下优势最明显**（传统方法在此崩得最厉害）。
- **关联度:** ★★★ 与「本地小模型跑 tool-calling」直接相关（4060 8GB 的现实约束）。可落地：将来做本地 agent 压缩时，评估指标要盯 decision 位置的准确率，不是整体困惑度。

### 9. Enhancing Repository-Level Code Completion with Reinforcement Learning in Real-World Scenarios

- **ID:** [`2611.07510v1`](https://arxiv.org/abs/2611.07510v1) | [📄 PDF](https://arxiv.org/pdf/2611.07510)
- **作者:** Zhenlong Dai, Zhuoluo Zhao, Xiu Tang, Sai Wu, Chang Yao, Zhipeng Gao, Jingyuan Chen
- **分类:** cs.CL | **提交:** 2026-11-05
- **摘要:** 仓库级补全的难点在于**从仓库里挑对上下文**和**跨文件依赖推理**。作者提出一个 RL 框架，三个部件：① identifier-driven intent recognition——用标识符捕捉补全意图，改善文件内与跨文件上下文理解；② reward-driven completion learning——在复杂仓库场景里对补全结果给奖励；③ selective-exploration——把探索集中在**低置信、高回报**的 token 上，促使模型探索有价值但少见的补全模式。实验显示相对 Code LLM 基线有显著提升，代码与数据集已公开。
- **关联度:** ★★★ 方法学可借鉴（「低置信高回报才探索」），但和 sora 当前工作距离较远。

---

## 三、记忆与长程上下文（2 篇）

### 10. MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents

- **ID:** [`2611.07631v1`](https://arxiv.org/abs/2611.07631v1) | [📄 PDF](https://arxiv.org/pdf/2611.07631)
- **作者:** Mayank Anand, Subham Raj, Aman Vaibhav Jha, Sriparna Saha
- **分类:** cs.IR | **提交:** 2026-11-05
- **摘要:** 长程 agent 需要跨会话保留有用信息并在需要时取回。现有系统把「写」和「取」当成两个独立问题：记忆在写入时就打了静态重要性分，**用完之后永不修订**。这产生两个耦合的失效模式——**压缩会静默销毁未来查询需要的证据**，而检索会持续偏向已经过时的记忆。MEMOIR 提出一个免训练的记忆生命周期：压缩前用**筛查门**测试「与答案相关的证据是否被保留」，每次查询后用**归因**估计哪些被检索的记忆支撑了答案，并据此更新它们的检索优先级；再加一个 UCB 式探索奖励，鼓励取回曝光不足的记忆，避免高频记忆挤掉有用但少见的证据。在 1,905 条去重 LoCoMo QA 上，完整检索栈把 **evidence recall@5 提升 11.92 个百分点**（对比裸余弦），confidence-gated 反馈在**无参考答案、无 reranker 训练**的前提下再加 1.50 分；judge-gated merge 让文本证据召回从 58.82% 到 59.08%，活跃库减小 1.42%，100 次独立审计合并 **0 次损失**（单边 95% 上界 2.95%）。在线写路径**不需要额外 LLM 调用**，merge 筛查放在周期性离线整合里。
- **关联度:** ★★★★★ 这就是 mnemon 的失效风险说明书：现在的 consolidation 只看「重不重要」，不看「以后还会不会用到」。可落地：① 记忆条目加「上次被哪次回答用上」的归因字段；② 压缩/合并前跑一次保留筛查（拿最近 20 个真实问题回测，看证据是否还在）；③ 保留 UCB 式探索，别让高频记忆垄断召回。

### 11. SMART: State-based Multi Agent Reasoning Traces for Verification-oriented Problem-Solving

- **ID:** [`2611.08196v1`](https://arxiv.org/abs/2611.08196v1) | [📄 PDF](https://arxiv.org/pdf/2611.08196)
- **作者:** Sai Vallurupalli, Francis Ferraro
- **分类:** cs.AI / cs.CL | **提交:** 2026-11-05
- **摘要:** 上下文有限的问题（比如事实核查）需要额外知识才能推理。SMART 用多 agent 框架去捕捉问题上下文中参与实体的**隐式状态**，并把这些状态知识组织成**多样、互补、对解题显著**的前提（premises）——用多种 LLM + 结构化角色化提示策略生成。用这些「真实世界可核验」的前提做知识引导的解题推理，在跨 3 个数据集的复杂科学论断验证上**最高提升 20%**；消融显示把前提锚定到真实世界知识是必要的，单独这一项带来**最高 5%** 提升。
- **关联度:** ★★★ 「先把实体状态抽出来再推理」是低成本的结构化技巧，可用于 k 做文献/客户需求核查时的前置步骤。

---

## 四、安全：注入、欺骗与幻觉（4 篇）

### 12. Decision Models as Retrieval Gates Against Injection and Pollution

- **ID:** [`2611.08325v1`](https://arxiv.org/abs/2611.08325v1) | [📄 PDF](https://arxiv.org/pdf/2611.08325)
- **作者:** Mahdi Ghadamyari, Reza Habibi
- **分类:** cs.CR / cs.IR | **提交:** 2026-11-05
- **摘要:** 检索到的网页文本可能夹带针对模型的指令，也可能是为误导而造的合成页面。作者测试：**开放权重的决策模型**（对文本回答类型化问题、不生成 token）能否当检索门同时挡这两种威胁。在 1,000 个问题、论坛式网页、隐藏注入指令的基准上，Kev-4B 门读每个段落的 HTML：攻击成功率从**无防御 27.9% → 现有缓解（清洗/归一化/引用提示）13.6% → 加门 5.7%**；门耗时 **76ms/段**，186 个良性页面误报 4 个（含面向人类的说明），干净查询响应率几乎不变（85.6%→86.2%）。在 200 查询、三分之二候选页是假的污染测试里，**在选 top10 之前先过滤池**能把假页面暴露压到 0.5%、准确率保持 83%（无过滤仅 28%）；只过滤 top10 则留给生成器的页面不够用。LLM-as-judge 排序更好（AUROC 0.99 vs 0.94）但贵 10 倍。**读 HTML 比读纯文本抓到的攻击更多**。所有模型均开放权重。
- **关联度:** ★★★★★ sora 的 web_extract 会把外部内容直接塞进上下文，这是现成的低成本门（76ms/段、4B 模型本地可跑）。可落地：抓取→入库前加一道「决策模型门」，并且**在排序前过滤池**，不要只过滤最终 top-k。

### 13. A Gingerbread House for LLM Agents: Source-Planned Honeypots That Lure Autonomous Attackers into an Isolated Shadow

- **ID:** [`2611.07611v1`](https://arxiv.org/abs/2611.07611v1) | [📄 PDF](https://arxiv.org/pdf/2611.07611)
- **作者:** Seungdeok Roh, Seokjun Ryu, Sohee Park, Daeseon Choi
- **分类:** cs.CR | **提交:** 2026-11-05
- **摘要:** LLM agent 利用 Web 漏洞的速度快到「补丁来不及打」。以往的欺骗防御大多是把 agent 从仍然可达的真目标引开；本文研究另一种安排：防御方 LLM 从应用源码规划一个静态蜜罐，路由器把**被确认是攻击者的客户端的后续所有请求（包括可用的 exploit）**送到隔离的影子副本。40 个 CVE-Bench 关键任务上，静态方案把真实沦陷从 **26/40 降到 5/40**（Claude Opus 4.8）、从 **20/40 降到 0/40**（ARTEX 攻击框架，31 次有效 run）；20 个设计时未用过的新任务上 ARTEX 从 15/20 到 0/20。关键细节：约一半欺骗组里 **exploit 在影子上成功了而真目标完好**——这是「把攻击搬走」而不是「挡住」，残余风险在那些仍打到真目标的请求。
- **关联度:** ★★★★ 思路可迁移到「危险动作沙箱化」：给 agent 一个影子环境跑写操作，真环境只接受通过校验的请求。

### 14. From Twisted Facts to Rogue Agents: Can LLMs Reliably Detect Multi-Dimensional Hallucinations?

- **ID:** [`2611.08231v1`](https://arxiv.org/abs/2611.08231v1) | [📄 PDF](https://arxiv.org/pdf/2611.08231)
- **作者:** Hanyu Qiu, Ze Liu, Zhe Zhao, Kuang Xiong, Blaze Chen, Zhenxiang Yan, Renfen Hu
- **分类:** cs.CL | **提交:** 2026-11-05
- **摘要:** 提出 HaluCheck：大规模双语基准，**42k+ 实例**，覆盖文本中的**事实幻觉**与 **agent 轨迹中的忠实性幻觉**，带细粒度多级标注（检测 / 定位 / 纠正），跨任务与不同扰动强度。14 个 LLM 上的实验显示：模型有基本的样本级检测能力，但在**细粒度定位、纠正、以及 agent 轨迹幻觉**上明显吃力；thinking、web search、SFT 各自带来部分改善，但没有一个能解决问题。
- **关联度:** ★★★★ 提醒「验收只看最终答案」是不够的——轨迹里的虚构步骤（比如声称跑过某命令）是独立的一类幻觉。可落地：交付验收加「执行证据」检查（日志/产物/退出码），而不是只看结论对不对。

### 15. JailBound: FOL-Guided Jailbreak Evaluation for Exploring LLM Behavioral Boundaries

- **ID:** [`2611.07530v1`](https://arxiv.org/abs/2611.07530v1) | [📄 PDF](https://arxiv.org/pdf/2611.07530)
- **作者:** Fazong Wu, Xin Wang, Ming Yang, Zhenyong Zhang, Xiaoming Wu
- **分类:** cs.CR | **提交:** 2026-11-05
- **摘要:** 现有越狱基准多靠人工设计/收集 prompt，难以系统扩展到新威胁条件；攻击搜索又通常只优化攻击成功率（ASR），看不出模型行为在「安全拒绝」与「不安全回答」之间如何局部变化。JailBound 把自动基准构建与 **FOL（一阶损失）引导的双分支搜索**结合：按风险类别 / 应用域 / 攻击类型组织威胁，用微调过的 meta-attack generator 按条件合成评估 prompt，再用 FOL 作为局部敏感性信号去探索高风险的边界区域。
- **关联度:** ★★★ 方法论价值大于结论：用「局部敏感性」而不是「成功率」衡量安全边界，和 SOUL 里「不把没报当没有」的态度同源。

---

## 五、模型选择与路由：把不确定性挪到确定性一侧（3 篇）

### 16. RouteAlign: Aligning Task Requirements with Model Profiles for LLM Service Selection

- **ID:** [`2611.08162v1`](https://arxiv.org/abs/2611.08162v1) | [📄 PDF](https://arxiv.org/pdf/2611.08162)
- **作者:** Jihao Zhao, Ding Chen, Yanfang Chen, Bo Tang, Feiyu Xiong, Junchi Yan, Zhiyu Li
- **分类:** cs.SE / cs.CL | **提交:** 2026-11-05
- **摘要:** 选 LLM 服务需要**反映当前任务需求**的性能证据；聚合分数会掩盖能力与难度的差异，而语义相近的样本可能考的是不同技能组合。RouteAlign 用「任务需求」同时结构化**性能度量**与**服务选择**：需求描述能力要求与难度，从而与对应的模型性能测量对齐；历史需求决定结果如何计入全局 profile 与局部能力估计，新需求决定这些测量如何影响当前决策；共享 scorer 整合证据，生成成本偏好控制最终选择。跨多样任务与异构服务，RouteAlign 把经验上的**质量-成本前沿推向更高质量**，且生成成本低于对比的 Jev 式决策后端最强配置；消融支持局部性能证据的贡献，目录更新实验显示 scorer 可复用。
- **关联度:** ★★★★ 直接对应 sora 的模型路由（smart_model_routing 目前是禁用状态）。可落地：路由表按「任务需求类型」而不是「模型总分」维护，并且每类任务单独攒局部样本，而不是全局平均。

### 17. Route Before Response: Fail-Closed Routing for LLM-Enabled Customer-Service Software

- **ID:** [`2611.07534v1`](https://arxiv.org/abs/2611.07534v1) | [📄 PDF](https://arxiv.org/pdf/2611.07534)
- **作者:** Yuchen Cao, Zhenyu Mao, Jacky Wai Keung, Yifei Wang, Guancheng Lin, Jingyu Zhang
- **分类:** cs.SE | **提交:** 2026-11-05
- **摘要:** 金融机构的 LLM 客服软件必须在回答之前**先选一个下游服务**；分类器和 LLM router 能给出标签或目的地，但一个组合应用还必须校验**派发权限**与**实体登记**。作者把这个问题当成 boundary-aware pre-response routing，提出 RouteBR：一次模型调用提议「主服务动作 + 登记对象」，然后由**确定性代码**检查标识符与版本化规则，之后才派发或给出明确的「不派发」结果；**低排名候选不能顶替被阻断的主路由**。用某真实金融机构的机密请求模式构造 600 个隐私保护场景（三名工程师共同复核）。200 例 CONFIRM MAIN 上 **final-path exact match 97.5%**；给同样规则的单调用基线 95.5%；**没有规则程序的诊断基线 action accuracy 94.0%，但 final-path 只有 41.0%**；166 个非派发案例中 **0 次误派发**。
- **关联度:** ★★★★★ 「模型提议 + 代码裁决」正是 k 的工具调用该有的形状：报价、发邮件、删文件这类动作，模型只提议，规则程序（标识符、版本、权限、金额上限）说了算。注意那组对照——**动作准确率 94% 看着很好，端到端路径只有 41%**，这正是「只测一步」的陷阱。

### 18. ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation

- **ID:** [`2611.07928v1`](https://arxiv.org/abs/2611.07928v1) | [📄 PDF](https://arxiv.org/pdf/2611.07928)
- **作者:** Petru Neague, Quinten Stokkink, Martijn de Vos, Rafael Pires, Mathis Randl, Anne-Marie Kermarrec, Johan Pouwelse
- **分类:** cs.DC / cs.AI / cs.IR / cs.NI | **提交:** 2026-11-05
- **摘要:** 现有 RAG 都把文档集中收集、索引、服务，但现实中文档归属于组织、设备和个人，他们**不愿或不能**把保管权交给中心方（隐私、版权、合规）。现有去中心化检索要么重新引入协调权威，要么依赖需要全网持续协调的全局数据结构（如 DHT）。ZeroRAG 提出一个去中心化路由层：在 peer 覆盖网上做**语义查询路由**，不需要全局数据结构或中心编排；文档留在所有者手里，每个 peer 只保留轻量索引。
- **关联度:** ★★★★ 与 sora 的「私人知识库不上云」红线同向：不是把数据搬走，而是让检索走到数据那里。

---

## 六、群体智能、AI-Scientist 与基准污染（6 篇）

### 19. SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization

- **ID:** [`2611.08483v1`](https://arxiv.org/abs/2611.08483v1) | [📄 PDF](https://arxiv.org/pdf/2611.08483)
- **作者:** Qile Jiang, George Em Karniadakis
- **分类:** cs.AI / cs.NE | **提交:** 2026-11-05
- **摘要:** LLM 引导的演化搜索用 agent 反复改进程序，但很慢：每轮都要生成一长串思维链，而且为了维持种群多样性得重复生成很多次。SwarmEvolve 让**每轮数百个低成本 agent** 以 swarm 形式工作，**在潜空间推理、不解码成文本**，通过**传 KV cache** 共享信息；每个 swarm 从不同角度研究问题；新颖性过滤器直接量隐藏状态向量之间的距离来保留最不同的想法；交叉在潜空间自然发生——一个 summarizer agent 接收所有成员合并后的 KV cache。21 个数学发现与科学计算问题上，SwarmEvolve 平均分最高，**中位只需 3–8 分钟就达到其他 SOTA 框架 60 分钟的最好成绩**；若干问题上 Qwen3 8B 就超过了 AlphaEvolve 用前沿 LLM 找到的解。
- **关联度:** ★★★★★ 潜空间通信对 4060 8GB 不现实，但「多角度 swarm + 用嵌入距离做新颖性过滤 + 汇总者做交叉」可以纯文本实现——这正好是 k 做选题/调研时可以套的循环。

### 20. Scientist World: Grow a Research World for AI-Scientists

- **ID:** [`2611.08478v1`](https://arxiv.org/abs/2611.08478v1) | [📄 PDF](https://arxiv.org/pdf/2611.08478)
- **作者:** Taiming Lu, Sachin Konan, Zhuang Liu
- **分类:** cs.AI / cs.CL / cs.LG | **提交:** 2026-11-05
- **摘要:** AI-Scientist 来了，但没有供它们成长的世界。人类科学家把「几个世纪的开放问题 + 共享想法」当成理所当然，而这对 AI-Scientist 只是**可读不可跑**。Scientist World 把**每一篇论文变成一个可执行环境**：自动管线抽取论文的开放式研究问题、把它的方法复现为 baseline；进入环境的 AI-Scientist 直接与人类作者的成绩比。首批发布 **1,000 个已验证环境**。用这个世界做评测，前沿 AI-Scientist **74% 的情况下能超过人类研究者**；同时它记录了 **6,400 小时研究轨迹**（每个想法、实验、失败与成功）；作为训练场，它把一个**小模型的研究 ideation 提升 158%**，追平前沿模型。
- **关联度:** ★★★★ 评测范式在变：从「答题」到「跑通别人的实验并超过原作者」。可落地：k 读论文时把「复现 baseline」当成理解的标准动作，而不是读懂摘要就算完。

### 21. Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies

- **ID:** [`2611.07667v1`](https://arxiv.org/abs/2611.07667v1) | [📄 PDF](https://arxiv.org/pdf/2611.07667)
- **作者:** Mete Erdogan, Mirac Suzgun, Aneesh Pappu, Guowei Xu, Batu El, Andrew A. Schoen, Furong Huang, John P. Dickerson, Mert Pilanci, James Zou
- **分类:** cs.AI | **提交:** 2026-11-05
- **摘要:** 多 agent LLM 系统的表现不只取决于模型能力，还取决于**信息共享策略**——每个 agent 看到什么、看到多细。给更多细节总是更好吗？作者提出 empirical information design：固定交互规则与模型，只变披露策略。10 个前沿 LLM 在三种市场上测：多资源交易、双边议价、双重拍卖，用 ground-truth 效用把「发现机会」和「实现结果」分开。结论是**高度模型依赖**：交易中给精确估值而非序数偏好，GPT-6 Sol 的实现收益反而下降（98%→91% 的最大值），Claude Sonnet 5 则上升（72%→86%）；议价中精确信息让 Grok 4.7 谈得更不平衡，而 Claude Opus 5.5 分配对称；双重拍卖中完全披露抬高报价、引发市场崩溃，Gemini 3.1 Pro 97%→78%、Opus 5.5 94%→64%、Grok 4.7 97%→62%。结论：**模型选择与信息设计必须联合优化**。
- **关联度:** ★★★★ 多 agent 协作里「共享多少上下文」不是越多越好，要按模型分别调。可落地：subagent 派活时，先给结构化需求（能力/难度），细节按 agent 类型分档披露。

### 22. Cleaning or Recalling? Knowledge Dependence in LLM-based Data Cleaning

- **ID:** [`2611.08106v1`](https://arxiv.org/abs/2611.08106v1) | [📄 PDF](https://arxiv.org/pdf/2611.08106)
- **作者:** Jingru Yang, Honglu Zhang, Jiayi Mi, Ju Fan, Zheng Chen, Xiaoyong Du
- **分类:** cs.DB | **提交:** 2026-11-05
- **摘要:** 公开数据清洗基准上的高分可能只是**认得这些实体**，于是无法判断模型修不修得了陌生的数据。作者提出 CoRE 协议：把公开基准与新采集的真实记录、以及由英文单词/音节构造的**成对名称替身**放在一起比——替身保留错误位置与非身份字段，只转移错误机制。21 个受控表 × 8 个 LLM 上，修复表现随实体名大幅波动：把实体名替换成词式替身后，**DeepSeek-V4-Pro 的年份准确率从 91% 掉到 18%**；在 Hospital 与 Movies 上，商业模型在新鲜记录上的分数反而高于词式替身（说明它们「记得」实体）。
- **关联度:** ★★★★★ 这是「基准分数=记忆」的干净证据，和 sora 关心的「AI 痕迹/查重」是同一族问题：**换掉实体名就崩的能力不是能力**。可落地：任何评测/自测，加一组「实体替换」变体，看分数掉多少。

### 23. RoboARCade: Benchmarking Agentic Robot Control

- **ID:** [`2611.08209v1`](https://arxiv.org/abs/2611.08209v1) | [📄 PDF](https://arxiv.org/pdf/2611.08209)
- **作者:** Satvik Sharma, Hengyuan Hu, Mihika Kamat, Dorsa Sadigh, Jeannette Bohg
- **分类:** cs.RO | **提交:** 2026-11-05
- **摘要:** 多模态能力提升后，agent 可以直接当机器人策略，作者称之为 agentic robot control（ARC）。RoboARCade 是跨三种具身的长程操作基准，专门测**上下文内适应、记忆与精确控制推理**；任务基于现有开源基准并**扩大初始条件范围**来加难。工程上强调可扩展：全部跑在 MuJoCo 单后端、每个任务是自包含 data pack、agent 通过可替换接口接入。结果区分度不错：**GPT-6 Astra 49.8%，Claude Fable 5.1 43.6%**，仍有大量空间；更丰富的视觉接口只带来 1.5–6.8 分提升，成本却是 1.7–2.3 倍。
- **关联度:** ★★★ 与 sora 的 PCB/机械臂兴趣沾边；「更贵的接口只多几分」是个通用的成本提醒。

### 24. Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety

- **ID:** [`2611.08438v1`](https://arxiv.org/abs/2611.08438v1) | [📄 PDF](https://arxiv.org/pdf/2611.08438)
- **作者:** Fazl Barez, Tung-Yu Wu, Hunar Batra, Gabriele Dominici, Florent Draye, Yanai Elazar, Damiano Fornasiere, Antía García, Abir Harrasse, Riley Harris, Sara Hooker 等（14+ 人）
- **分类:** cs.CL / cs.AI / cs.LG | **提交:** 2026-11-05
- **摘要:** 综述文章，问一个直白的问题：**理解模型如何工作，真的让它更安全吗？** 作者把机制可解释性放回可解释性研究的大图景里，比较「机制证据」与「行为评测」各自能支撑什么结论，梳理基础概念、方法与证据标准，并讨论在评估、预测与控制行为上的实际可用性。
- **关联度:** ★★★ 作为方法论参照：机制证据 ≠ 安全保证，和 k 的「没报 ≠ 没有」是同一条认知纪律。

---

## 给 sora 的 5 条行动项

| # | 行动 | 依据 | 成本 |
|:--|:--|:--|:--|
| 1 | 迁移/依赖修复的验收，强制加**一条从 release note 抄来的边界输入**（不是自己想的典型输入） | Accepted but Wrong（2611.08269）：全断言门禁放过 41.0% 的错误修复，一条边界输入降到 6.5% | 每次 10 分钟 |
| 2 | 失败处理改成「**先同模型重试、再谈换模型**」，并给重试设预算 | Hard Issue/Weak Model/Bad Run（2611.08285）：难度参考分 AUROC 0.92 vs 轨迹预测器 0.62，换模型收益不超过随机波动 | 改规则 5 分钟 |
| 3 | 交付包统一四件套：精修代码 + 环境脚本 + 一键启动 + 复现指南，并留执行证据 | ReproBridge（2611.08452）：成功率 76.4%→92.6%，API 花费 −19.7%，跨模型差距 21.6pp→3.9pp | 半天 |
| 4 | mnemon 记忆加「用后归因」字段 + 压缩前保留筛查（拿最近 20 个真实问题回测） | MEMOIR（2611.07631）：evidence recall@5 +11.92pp，100 次合并 0 损失，在线写路径零额外调用 | 1 天 |
| 5 | 抓取外部网页入库前加「决策模型门」，且**先过滤池再排序**（不要只过滤 top-k） | Retrieval Gates（2611.08325）：ASR 27.9%→5.7%，76ms/段；只过滤 top10 会让生成器页面不够 | 半天 |

---

*以上：观察 24 项（均为 arXiv abs 页原文摘要与论文自报数字，版本号已复核为 v1）/ 推断 3 项（①「11-06~11-08 无新提交」由 API 最新时间戳 2026-11-05T18:59Z + HTML 日期窗 0 条共同支撑，但未核对 arXiv 公告原文；② 各篇「关联度」为判断而非论文结论；③ 论文实验的独立可复现性未验证）/ 未知 2 项（① 11-05 批次是否还有未被我检索到的强相关论文——HTML 搜索按相关度取前 150 篇后人工筛，非全池枚举；② 各论文代码/环境是否已公开未逐一确认）。生成于 2026-11-08 14:5x cron（补全轮：11-05 批次第三轮，150 篇检索池中 125 篇未覆盖，本篇收 24 篇）。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
