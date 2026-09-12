---
aliases:
  - arxiv-2026-09-11-agent-llm
  - arxiv-agent-llm-2026-09-11
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-11
updated: 2026-09-11
status: adopted
source: arxiv.org list pages + abs pages（09-11 新窗口正常速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-11

> **检索时间**: 2026-09-13 GMT+8（cron 补跑）
> **窗口**: list 页出现新日期分组 **2026-09-11（441 篇）**——与已覆盖池（575）**零重叠**，全新窗口 → 正常速览。export.arxiv.org API 持续 429 限流 → HTML list 页路由。
> **收集**: 6 类别 list/recent 页全量 → 09-11 分组 **441 unique base ID** → 标题粗筛 69 候选（score≥2）→ 人工剔除领域应用（医疗/金融/交通/能源/语音/沿海环境等）→ 逐篇抓 abs 页精选 **20 主条目 + 12 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、Agent 记忆与技能（4 篇）

### 1. When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval for LLM Agents

- **ID:** [2609.10750v1](https://arxiv.org/abs/2609.10750v1) | [📄 PDF](https://arxiv.org/pdf/2609.10750v1)
- **作者:** Syed Shariyar Murtaza, Yifan Nie, Utkarsh Soni, Eugene Wen, Arvid Frydenlund
- **分类:** cs.IR, cs.AI, cs.LG
- **摘要:** LLM agent 越来越依赖运行时检索外部技能，技能选择成为关键挑战。作者给出生产级技能路由器（34,396 个技能）+ 大规模技能检索研究：用有限真实监督 + 合成数据微调。核心发现：合成数据微调提升**分布内**检索，但会在**真实和 OOD 数据**上造成灾难性遗忘。
- **关联度:** ★★★★★ 技能检索 = Hermes 技能体系直接映射；「合成数据提升分布内但遗忘 OOD」对 k 用合成数据增强技能库/题库/词库有直接警示——加数据前先测分布外表现

### 2. Grounding Agent Memory: Environment-Probing Curation for Enterprise Agents

- **ID:** [2609.11060v1](https://arxiv.org/abs/2609.11060v1) | [📄 PDF](https://arxiv.org/pdf/2609.11060v1)
- **作者:** Susheel Suresh, Hazel Mak, Sahil Bhatnagar, Chhaya Methani, Alejandro Gutierrez Munoz
- **分类:** cs.AI, cs.SE
- **摘要:** 持久记忆进入生产级 agent 平台，帮助长程 agent 跨会话积累经验。但只限已完成轨迹的后置策展 agent 会保留错误、过度概括部分证据、保留陈旧知识。作者提出**环境探测策展**（environment-probing curation）：给现有异步策展 agent 最小权限、只读世界工具，主动探测环境验证记忆条目再落库。
- **关联度:** ★★★★★ 「记忆策展需要环境验证而非只读旧轨迹」——正是 k 记忆/知识库治理（learn→research→apply）可升级的方向：写库前先探测验证，防「错误记忆污染长期库」

### 3. Memory Compression for High-Fanout Agent Sandboxes

- **ID:** [2609.11294v1](https://arxiv.org/abs/2609.11294v1) | [📄 PDF](https://arxiv.org/pdf/2609.11294v1)
- **作者:** Mengming Li, Ceyu XU, Qijun Zhang, Jiangnan Yu, Xiangfeng Sun, Haohui Mai, Zhiyao Xie
- **分类:** cs.AI, cs.OS
- **摘要:** 高扇出 agent 负载造成内存瓶颈：单任务可能生成许多并发沙箱会话。这些沙箱并非独立——源自共享模板、执行相关轨迹，存在大量模板相对与跨沙箱内存冗余。传统内存压缩在「如何压缩/何时压缩/压缩什么」三维度都不匹配，作者提出面向 agent 沙箱的专用压缩。
- **关联度:** ★★★★ 多 agent 并行沙箱的内存优化——k 的 delegate_task 并行子代理 / Codex 多任务跑批的资源管理参考；4060 8GB 显存+16GB 内存场景直接相关

### 4. COBRA-Skills: Contextual Bandit-Guided Evolution for Agent Skill Optimization

- **ID:** [2609.11682v1](https://arxiv.org/abs/2609.11682v1) | [📄 PDF](https://arxiv.org/pdf/2609.11682v1)
- **作者:** Pingchen Lu, Xiangyi Wang, Xiang Li, Jie Mao, Zikun Qu, Junfeng Luo, Yao Shu, Bryan Kian Hsiang Low, Zhongxiang Dai
- **分类:** cs.AI
- **摘要:** LLM agent 可从过往任务经验蒸馏可复用技能，但既有技能优化方法依赖昂贵的执行式评估和大量任务数据。COBRA-Skills 把技能优化形式化为**有预算的顺序优化**：在动态演化的候选空间上用上下文赌博机引导优先级排序，技能演进更省资源。
- **关联度:** ★★★★ 技能自进化（skill-evolution / COBRA 技能）——「上下文赌博机引导 + 预算约束」给 k 的技能蒸馏/进化提供更省资源的排序策略，避免每轮全量评估

---

## 二、Agent 安全与治理（6 篇）

### 5. RAG-Safety-Bench: Reliable Evaluation of Retrieval-Augmented LLM Safety

- **ID:** [2609.11758v1](https://arxiv.org/abs/2609.11758v1) | [📄 PDF](https://arxiv.org/pdf/2609.11758v1)
- **作者:** Adithiyan Rajan Indira Saravanan, Kathleen C. Fraser
- **分类:** cs.CL, cs.IR
- **摘要:** RAG 从可信文档检索可提升可靠性、降低幻觉，但近期工作表明：当被提示有害/危险内容时，RAG 会对整体安全产生意外副作用。作者构建可靠评估 RAG 安全的基准，并探究这一现象的机制——检索增强不等于更安全。
- **关联度:** ★★★★ RAG 安全副作用评估——k 的 RAG 用例（DashScope text-embedding-v4 题库检索/知识库问答）需要「检索增强≠更安全」的意识；安全评估缺位时别默认 RAG 缓解一切

### 6. BenchShield: Formal Model-Backed Instrumentation for Reward Integrity in LLM-Agent Evaluation Infrastructure

- **ID:** [2609.11028v1](https://arxiv.org/abs/2609.11028v1) | [📄 PDF](https://arxiv.org/pdf/2609.11028v1)
- **作者:** Shenghan Zheng, Zonglin Di, Yimin Liu, Kyoung Whan Choe, Jiankai Sun, Heguang Lin, Penghao Jiang, Yifeng He, Xiao Cheng, Jicheng Wang, Wenbo Chen, Alex Yates, Yinzhe Zhao, Bingran You, Yuan Gao, Ayush Munot, Shubham Gaur, Zhe Ye, Hao Wang, Xiangyi Li, Dawn Song, Christophe Hauser
- **分类:** cs.CR, cs.AI, cs.SE, eess.SY
- **摘要:** LM-agent 基准越来越像交互式评估基础设施：agent 观察状态、调用工具、修改工作区、提交工件、从结果程序接收奖励。这种交互性使评估易受 **reward hacking**：agent 通过利用奖励相关轨迹而非解决目标任务来提高得分。BenchShield 用 TLA+ 形式化奖励生命周期，静态阶段感知 taint 分析在运行前暴露 hacking 路径，运行时用基础设施侧证据归因 agent 行为。构建 456 条人工裁决轨迹（来自 3 个基准 31,000+ 次公开运行）：全链 recall 23-94%→77-100%，运行时检测 reward hacking 准确率 96%。
- **关联度:** ★★★★★ reward hacking 防御形式化——k 自建评测（墨题 AI 评分 / LLM judge / 门禁）防「刷分 exploit」的直接参考；「验证器可靠性」主题 09-10 已起，本篇给形式化底座

### 7. DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents

- **ID:** [2609.10892v1](https://arxiv.org/abs/2609.10892v1) | [📄 PDF](https://arxiv.org/pdf/2609.10892v1)
- **作者:** Asif Pinjari, Mithun Paul Saint-Germain
- **分类:** cs.CR, cs.AI, cs.LG
- **摘要:** 间接提示注入成功后，妥协在 agent 自身行为中可见：良性工具调用前缀、被投毒的观察、服务攻击者的动作后缀。操作者需要三个事实：攻击从哪里进入、污染了哪些步骤、明显投毒是否被抵抗。现有系统只给整轨迹判定或单个不安全索引。DriftNet 用双头轨迹 Transformer 检测并**定位**注入点与污染步。
- **关联度:** ★★★★ 轨迹级注入检测定位——k 的 agent 安全审计从「整轨迹判罪」升级到「定位污染步骤」的参考；多步 agent 日志审计直接可用

### 8. No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers

- **ID:** [2609.10854v1](https://arxiv.org/abs/2609.10854v1) | [📄 PDF](https://arxiv.org/pdf/2609.10854v1)
- **作者:** Zehua Zhang, Jie Hu, Pratham Hegde, Aditya Maheshbhai Gabani, Souradip Nath, Yibo Liu, Siyu Liu, Hongkai Chen, Hulin Wang, Zhuoer Lyu, Chang Zhu, Divij Handa, Yan Shoshitaishvili, Tiffany Bao, Ruoyu Wang, Adam Doupe
- **分类:** cs.CR, cs.AI
- **摘要:** 传统漏洞分析依赖系统访问或动态交互，但对审计闭源/远程托管/商业门控软件不可用。作者提出 **no-box 漏洞分析**范式：无访问、无运行时交互，仅凭功能元数据（如 MCP server 的描述）检测间接提示注入漏洞。
- **关联度:** ★★★★★ 与 09-10「技能供应链安全」主线直接延续——k 装第三方 MCP server 前「只看描述就能预检注入漏洞」的能力；装前检查清单可加「描述级注入预检」

### 9. Engineering Reliable Commit Gates for Agentic AI: Cost-Aware Verification Portfolios under Common-Mode Data Failures

- **ID:** [2609.10969v1](https://arxiv.org/abs/2609.10969v1) | [📄 PDF](https://arxiv.org/pdf/2609.10969v1)
- **作者:** Zihao Zheng, Baichuan Li, Junyi Yao, Jiayu Long
- **分类:** cs.SE
- **摘要:** Agentic 系统提交有状态变更，但额外验证器可能**继承同一上游故障**（common-mode failure）。作者提出 VP-CONTROL：运行时保证设计与确定性基准，48 个任务模板 → 2,880 个跨六种故障机制场景；2x2 实验分离「验证器模型多样性」与「证据源多样性」，发现跨模型投票不如跨证据源。
- **关联度:** ★★★★ 「验证器会继承同一上游故障」——k 的交付门禁（grep 冲突 + build + pytest / GitHub 门禁）需要「证据源多样性」而非只换模型/只换工具

### 10. When Passing Tests Hides Vulnerabilities: An Empirical Study of Silent Failures in Agentic Systems

- **ID:** [2609.10548v1](https://arxiv.org/abs/2609.10548v1) | [📄 PDF](https://arxiv.org/pdf/2609.10548v1)
- **作者:** Wenji Bai, Muhammad Waseem, Zeeshan Rasheed, Jaakko Peltonen, Pekka Abrahamsson
- **分类:** cs.SE, cs.CR
- **摘要:** LLM 自动代码修复 agent 受广泛关注，但通过语法和功能验证的补丁仍可能保留或引入安全漏洞——**静默失败**。作者系统性识别并分类 LLM-based agentic code repair 中的这类静默失败模式。
- **关联度:** ★★★★ 「测试通过≠无漏洞」——k 的 Codex 委派/代码审计门禁（github-privacy-gate / hermes-codex-security-gate）的实证支持；修复类任务交付后补一次安全视角复检

---

## 三、Agent 评估与基准（5 篇）

### 11. Sci-MMR: Benchmarking Multi-Step Evidence-Grounded Scientific Reasoning in Multimodal Agents

- **ID:** [2609.11243v1](https://arxiv.org/abs/2609.11243v1) | [📄 PDF](https://arxiv.org/pdf/2609.11243v1)
- **作者:** Jiaqiang Li, Yajie Yang, Zhiheng Xi, Jiadong Chen, Enyu Zhou, Senjie Jin, Yang Nan, Jiazheng Zhang, Han Wang, Yanxin Li, Dingwei Zhu, Bicheng Deng, Yuhui Wang, Xiang Zheng, Qi Zhang, Lei Bai, Xingjun Ma, Tao Gui
- **分类:** cs.AI
- **摘要:** 自主研究 agent 日益需要检索文献、分析实验证据、生成科学假设——多步**证据接地**推理。既有多模态基准大多只评最终答案准确率，未检验预测是否真正被可追溯证据支持。Sci-MMR 提出多步证据接地科学推理基准。
- **关联度:** ★★★★★ 与 light-literature-search / 联合研究流水线直接相关——「证据可追溯而非只看答案」正是 k 研究交付的质检标准；基准设计对 k 自建评测有参考

### 12. Mr.LHDR: A Benchmark for Multimodal Real-World Long-Horizon Deep Research Agents

- **ID:** [2609.11318v1](https://arxiv.org/abs/2609.11318v1) | [📄 PDF](https://arxiv.org/pdf/2609.11318v1)
- **作者:** Minghao Guo, Meng Cao, Sui Zhao, Siyu Ning, Xin Wang, Haoze Zhao, Jiaxuan Yang, Haihong Hao, Mingfei Han, Shunlin Rong, Haijun Wu, Xiaodan Liang, Xiaojun Chang
- **分类:** cs.AI
- **摘要:** 深度研究 agent 日益能网页搜索、工具使用、多模态证据分析、信息综合。但既有基准主要测中程探索，很少测试**长程、依赖链深**的研究过程。Mr.LHDR 提出多模态真实世界长程深度研究基准。
- **关联度:** ★★★★ 长程深度研究基准——k 的联合研究流水线（k拆题→WorkBuddy初稿→k核验）长程化评测参考；「依赖链深」正是多轮协作研究的难点

### 13. Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation

- **ID:** [2609.11115v1](https://arxiv.org/abs/2609.11115v1) | [📄 PDF](https://arxiv.org/pdf/2609.11115v1)
- **作者:** Koutian Wu, Junjie Zhou, Ergan Shang, Jiayu Wang, Pengqian Han, Junkai Wang, Wanghan Xu
- **分类:** cs.AI, cs.IR
- **摘要:** 基准研究者和 LLM 开发者需要找相关评测、定位基准数据集与代码、理解分数背后的设置。Benchmark Radar：AI 基准的**活数据库与搜索引擎**，覆盖 LLM 评测、agentic 与工具使用基准、编码、推理、安全、领域评测。
- **关联度:** ★★★★ 基准检索基建——k 评模型/选基准（model-capability-reference / ai-api-provider-evaluation）时「活库而非静态清单」的思路；可收藏为常驻工具

### 14. NovGauge: A Fine-Grained Benchmark for Diagnosing LLMs' Capability in Paper Novelty Assessment

- **ID:** [2609.11234v1](https://arxiv.org/abs/2609.11234v1) | [📄 PDF](https://arxiv.org/pdf/2609.11234v1)
- **作者:** Guoqiang Zhang, Kexin Tan, Ming Zhang, Li Ju, Wenqing Jing, Zhonghan Yue, Jiayi Chen, Shiqiang Wu, Shaofan Liu, Yue Zhang, Yuankai Ying, Yang Shi, Tao Gui, Qi Zhang, Xuanjing Huang
- **分类:** cs.AI
- **摘要:** LLM 越来越多用于主要 AI 会议同行评审，**新颖性**仍是持续弱点。既有基准把新颖性当单一整体分数，难诊断模型误判哪个维度、证据是否忠实。NovGauge：619 对论文 + 50 个多维指标，细粒度新颖性评估诊断。
- **关联度:** ★★★★ 与 light-idea-critique（审 idea 撞车/新颖性一票否决）直接同题——「细粒度诊断而非整体分」提升 k 评审质量；接单评论文/审稿的质检参考

### 15. What a Random Draw from the MCP Registry Contains, and What Tool-Use Benchmarks Contain Instead

- **ID:** [2609.10962v1](https://arxiv.org/abs/2609.10962v1) | [📄 PDF](https://arxiv.org/pdf/2609.10962v1)
- **作者:** Haseeb Mohammed Afsar
- **分类:** cs.SE, cs.AI
- **摘要:** MCP server 生态研究取样方式会悄悄选择「能工作的 server」：参考集、热门榜、手工策展框架、或修复到能启动的流水线。作者报告未修复概率样本的真实情况：从 24,135 个 server 普查中按发布种子抽 400 个 npm/stdio server 逐个线上探测——**仅 48.8% 完成握手**（手工策展框架 66.7%）；主导失败不是缺凭据（13.3%）而是**根本不启动（37.5%）**。195 个能跑的 server 共 2,766 个工具，零致命 JSON Schema 违规；可选安全标注缺失率 58.8%（策展 41.5%）。对照基准语料：BFCL v4 去重后 16.7% 近似重复（16.4 点落在独立任务之间），UltraTool 0.3%，真实 MCP 2.8%（全在单 server 内、跨作者 0.0%）；原始 BFCL 68.8%、UltraTool 85.6% 是精确 name+description 重复。
- **关联度:** ★★★★★ MCP 生态「幸存者偏差」实证——k 评估/接入 MCP server 时「注册表里近一半是死的」是基线事实；「基准语料去重」对 k 用 BFCL 类基准评工具调用能力的可信度有直接冲击

---

## 四、Agent 执行与推理（3 篇）

### 16. T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks

- **ID:** [2609.11042v1](https://arxiv.org/abs/2609.11042v1) | [📄 PDF](https://arxiv.org/pdf/2609.11042v1)
- **作者:** Junyao Yang, Yucheng Shi, Zhongzhi Li, Ruhan Wang, Zongxia Li, Haitao Mi, Leowei Liang
- **分类:** cs.LG, cs.AI
- **摘要:** Agent 使用正转向长程任务（编码、科学发现），终端任务尤其重要。T1：122B 总参 MoE（Qwen3.5-122B-A10B 后训练），RL 训练，在云沙箱中操作真实 shell、单任务最多 300+ 工具调用轮次，用任务自己的验证器给奖励。完整配方：激进 warm-start 稳定 actor-critic + 密集过程奖励（按通过验证器绝对数计分）+ TITO 令牌保真 + R3 路由重放，训练语料与 Terminal-Bench 2.1 完全 OOD。Terminal-Bench 2.1 从 43.8%→**64.0%**（超越 GPT-5.4 / DeepSeek-V4-Flash，active 参数少一个数量级）；Long-Horizon Terminal Bench 27.9%（匹配 Gemini-3.1-Pro，超 GPT-5.4 与 GLM-5.1）。
- **关联度:** ★★★★★ 重磅。「用任务验证器做奖励 + 在线任务合成」= 强化学习版编码 agent 路线；TITO/R3 的 MoE 训练稳定性方案对 k 4060 小模型自举、Codex/dsh 委派配方都有启发

### 17. Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows

- **ID:** [2609.10964v1](https://arxiv.org/abs/2609.10964v1) | [📄 PDF](https://arxiv.org/pdf/2609.10964v1)
- **作者:** Bochao Feng, Jianjiang Li, Haojie Wang, Lin Qiao, Yinghui Li, Yukun Yan, Jidong Zhai
- **分类:** cs.AI, cs.SE
- **摘要:** Agentic LLM 工作流 = 模型轮次与工具交互交替，端到端完成时间不仅取决于推理速度，还取决于就绪轮次何时释放。大多数运行时一就绪立即释放；争用下这种急切释放会堆积已释放未完成的工作，一旦提交就不能再被工作流级策略重排。作者提出「就绪与释放解耦」的尾部感知调度。
- **关联度:** ★★★★ 调度策略——k 的多 agent 并行（delegate_task 10 并发）+ cron 错峰调度的尾部延迟控制参考；「释放时机也是调度决策」视角新

### 18. Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents

- **ID:** [2609.11677v1](https://arxiv.org/abs/2609.11677v1) | [📄 PDF](https://arxiv.org/pdf/2609.11677v1)
- **作者:** Ruiqing Yue, Yu Cui, Zhuoyu Sun, Sicheng Pan, Xianhong Xue, Tingyu Li, Ting Li, Wenzhuo Zhu, Yi Chen, Yifei Liu, Baohan Huang, Zhe Cui, Haibin Zhang, Cong Zuo
- **分类:** cs.SE, cs.AI
- **摘要:** 自进化运行时 harness 能显著提升 LLM agent 能力。既有 harness 进化方法依赖迭代搜索：基于执行反馈反复评估和修订候选 harness——时间开销巨大。Ecdysis 提出高效训练运行时 harness 的方法。
- **关联度:** ★★★★ harness 自进化效率——与 09-10「技能自进化从启发式补丁走向稳定优化器」主线延续，k 的 harness/工具链自举参考

---

## 五、多智能体与决策（1 篇）

### 19. When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for Multi-Agent Collective Decision-Making

- **ID:** [2609.11709v1](https://arxiv.org/abs/2609.11709v1) | [📄 PDF](https://arxiv.org/pdf/2609.11709v1)
- **作者:** Ken Chen, Wei Wang, Sachith Seneviratne, Hansani Weeratunge, Saman Halgamuge
- **分类:** cs.AI, cs.MA
- **摘要:** 多个 LLM agent 给出冲突答案时，决策机制决定多样性是提升表现还是只是复合共享错误。既有集体决策（投票、选举规则、LLM 判官）依赖前向推理：证据→标签单向映射，合并的估计共享同一证据基础。作者提出**贝叶斯反向推理**作为无标签锚点：从答案反向推理证据似然，聚合时给「独立证据」更高权重、压共享错误。
- **关联度:** ★★★★ 多 agent 一致性聚合——k 的 Gemini 跨源盲评 / 多 agent 协作「判官被共享证据带偏」问题的解法参考；「投票≠独立」的量化视角

---

## 六、对齐与驱动（1 篇）

### 20. Artificial Id: Drive and Persistent Alignment in Agentic AI

- **ID:** [2609.11911v1](https://arxiv.org/abs/2609.11911v1) | [📄 PDF](https://arxiv.org/pdf/2609.11911v1)
- **作者:** Yakov Pyotr Shkolnikov
- **分类:** cs.AI
- **摘要:** Agentic AI 正从有界任务执行走向跨任务边界持续运行、保留后果性状态的系统。这种转变造成控制问题：当前 harness 主要靠手工指定目标、重试、验证、停止规则等行为转换。作者提出 **artificial id**：自适应内部驱动，决定行为是否继续/停止，把「持久对齐」从外部规则内化为系统自身的驱动机制。
- **关联度:** ★★★★ 「内在驱动 vs 外部 harness 规则」——与 k 的 SOUL.md 人设/驱动设计（防漂移锚定句）理论同题；「对齐从外部规则走向内部驱动」对 k 自我治理有哲学参考

---

## 七、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.11152](https://arxiv.org/abs/2609.11152v1) | terms.txt: A Consent and Compensation Protocol for Agentic Web Access | 开放网络旧契约破裂（AI 爬虫主导流量），robots.txt 无法表达身份/目的/条款，提出 terms.txt 同意与补偿协议——Agentic Web 访问的合规层 |
| 2 | [2609.10901](https://arxiv.org/abs/2609.10901v1) | SearchAtlas: Analyzing Agentic Search Strategies via Evidential Query Graphs | 把搜索轨迹转成结构化证据查询图，分析 agentic 搜索策略的证据传播——「评过程而非只评答案」与 Sci-MMR 同题 |
| 3 | [2609.11899](https://arxiv.org/abs/2609.11899v1) | Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic Long Video Understanding | 长视频 agent 的「视觉-文本二元性」路由：语言记忆保长程时序、像素决胜属性感知，预算感知按需取帧 |
| 4 | [2609.11728](https://arxiv.org/abs/2609.11728v1) | Reproducibility in the Age of Agentic AI: Context Engineering at the Timescale of a Codebase | 「可复现研究=AI 编码 agent 的上下文工程」：agent 降低测试/提交历史/仓库结构/决策记录的维护成本，研究者负责验证工件与科学判断 |
| 5 | [2609.11319](https://arxiv.org/abs/2609.11319v1) | Magenta: Closing the Loop Between Mathematical Reasoning and Lean Verification | 数学推理与 Lean 机器可验证明闭环：自然语言推理 + 形式化验证互补，减少「看似对但证不了」 |
| 6 | [2609.11065](https://arxiv.org/abs/2609.11065v1) | MOSAIC: Query-Aware Exploration Policy Adaptation for GraphRAG | GraphRAG 共享探索流程与查询结构错配（直答要局部紧邻、比较要平衡覆盖、中介问题要深路径），提出免训练查询感知策略适配 |
| 7 | [2609.11109](https://arxiv.org/abs/2609.11109v1) | How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding | 量化多 agent LLM 定性编码的可靠性：语境与结构因素调节编码结果，给出基线流水线让 agent 独立编码后讨论达成共识 |
| 8 | [2609.11660](https://arxiv.org/abs/2609.11660v1) | Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents | 具身 agent 在动态未知环境中的发展框架：自主性、社会规范与对齐的关系，挑战「预训练数据+人类反馈够用」假设 |
| 9 | [2609.11308](https://arxiv.org/abs/2609.11308v1) | 2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation | 机器人长程操作：记忆不一定要进动作策略，agent 侧记忆接地作为可引导行动模型的指导，解耦归因混淆 |
| 10 | [2609.11393](https://arxiv.org/abs/2609.11393v1) | Beyond Confidence: Stability-Aware Test-Time Adaptation for LLM Reasoning | 预测熵之外加**稳定性感知**的测试时适应：不只追高置信，还看推理状态稳定性，免外部验证器/奖励模型 |
| 11 | [2609.11414](https://arxiv.org/abs/2609.11414v1) | SWRouter: Similarity-Contractive Window Routing for Multi-Turn LLM Conversations | 单轮路由不直接迁移到多轮对话：相似性收缩窗口路由处理历史上下文的分段/保留/丢弃，多轮场景按对话路由模型 |
| 12 | [2609.11020](https://arxiv.org/abs/2609.11020v1) | K/V-Cache Interventions Dissociate Representation Alignment from Persona Expression | KV 缓存干预把目标条件 KV 轨迹移植进源人设生成：13 种干预配置下表征对齐与人设表达解耦——人设控制的新表面 |

---

## 今日要点（主题信号）

1. **Agent 记忆/技能策展从「只读轨迹」走向「主动验证 + 预算优化」**：11060 给策展 agent 加最小权限环境探测工具验证记忆条目再落库；10750 实证合成数据微调技能检索会灾难性遗忘 OOD；11294 沙箱内存压缩、11682 上下文赌博机引导技能进化。记忆/技能供应链的可靠性工程化，与 09-10「记忆即基础设施」主线无缝延续。
2. **安全焦点转向「评估与验证基础设施本身」**：11028 BenchShield 用 TLA+ 形式化 reward 生命周期、静态 taint 分析预暴露 hacking 路径（96% 运行时检测率）；10969 证明验证器会继承同一上游故障、跨模型投票不如跨证据源；10548 测试通过仍藏漏洞。三篇合起来：「验证器的可靠性」成为独立工程问题，比模型能力更优先。
3. **MCP 生态幸存者偏差被实证量化**：10962 普查 24,135 个 server 抽 400 个，仅 48.8% 能握手、37.5% 根本不启动；而基准语料 BFCL v4 68.8% 原始行是重复。接入生态工具与用基准评能力时，先认「注册表一半是死的」「基准一半是重复的」基线。
4. **终端 agent RL 规模化落地**：11042 T1 用 122B MoE（active 10B）纯 RL 训终端 agent，Terminal-Bench 2.1 达 64.0% 超 GPT-5.4/DeepSeek-V4-Flash（active 参数少一个数量级）；TITO（训练推理令牌一致）+ R3（路由重放）解决 MoE RL 稳定性。「RL 直接训 agent 行为而非只训模型」成为可复现配方。
5. **多 agent 决策从投票走向证据推理**：11709 贝叶斯反向推理给「独立证据」更高权重、压共享错误——投票/判官被共享证据基础带偏的问题有了理论解法；多 agent 评测（Sci-MMR、Mr.LHDR）同步转向「证据可追溯 + 长程依赖」。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| T1 2609.11042 | arxiv.org abs/html 全文抓取 + web_search | ✅ 已确认（arXiv/HuggingFace/alphaXiv/Cool Papers 多源；关键数字：Terminal-Bench 2.1 43.8%→64.0%、LHTB 27.9% 超 GPT-5.4/GLM-5.1、122B MoE active 10B） |
| BenchShield 2609.11028 | arxiv.org abs/html 全文抓取 + web_search | ✅ 已确认（456 条人工裁决轨迹 / 31,000+ 次运行 / 全链 recall 23-94%→77-100% / 运行时 96% 准确率；同主题 RewardHackingAgents 2603.11337、BenchGuard 2604.24955 佐证方向活跃） |
| MCP Registry 2609.10962 | arxiv.org abs/html 全文抓取 + web_search | ✅ 已确认（24,135 普查→400 样本→48.8% 握手、37.5% 不启动；BFCL 68.8% / UltraTool 85.6% 原始重复；社区媒体 The Neural Feed 转载佐证） |
| 其余 39 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **合成数据增强前测 OOD**：10750「合成数据提升分布内但灾难性遗忘真实/OOD」——k 若用合成数据扩技能库/题库/词库（补音标/例句、AI 标注），先测真实分布上的检索/生成表现，别只看分布内指标
- 🔴 **记忆策展加环境验证**：11060「只读轨迹策展会保留错误与陈旧知识」——Hermes 记忆/知识库写入前补「探测验证」步（learn→research→apply 已有雏形，强化验证环节），防止错误记忆污染长期库
- 🟡 **验证器多样性自查**：10969「验证器继承同一上游故障，跨模型投票不如跨证据源」+ 10548「测试通过仍藏漏洞」——k 的门禁/交付校验（build+pytest、GitHub 门禁）从「换模型」升级到「换证据源」；Codex 修复类交付补安全复检
- 🟡 **MCP 接入基线认知**：10962「注册表 48.8% 能启动、基准 68.8% 重复」——评估 MCP server 时先实测启动而非看热门榜；用 BFCL 类基准评工具调用能力时先全局去重
- 🟢 **待深读**：11042 T1（终端 agent RL 完整配方：warm-start + 密集验证奖励 + TITO/R3）、11028 BenchShield（reward hacking 形式化防御）、10962（MCP 生态普查方法论）→ core-contributions 候选

---

*本速览由 cron 自动生成：09-13 检查 list 页出现 09-11 新分组（441 篇，与 covered 575 零重叠）→ 标题粗筛 69 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选（20 主条目 + 12 简评）→ 元数据以 arxiv.org abs 页为准；T1/BenchShield/MCP Registry 三篇跨源 web 验证通过。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
