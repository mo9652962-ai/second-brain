---
aliases:
  - arxiv-2026-09-15-agent-llm
  - arxiv-agent-llm-2026-09-15
tags: [arxiv, research, ai-agent, llm, daily]
created: 2026-09-15
updated: 2026-09-15
status: adopted
source: arxiv.org list pages + abs pages（09-14 冻结池补全速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-15（补全）

> **⚠️ 补全性质声明**：09-15 检查 list 页**无新日期分组**（最新仍为 **2026-09-14，432 篇**）——export.arxiv.org 索引冻结、无新提交。09-14 正常速览仅覆盖 30/432（≈7%，远低于 20% 阈值）→ 本份为**补全速览**：补录同一 09-14 提交池的漏网强相关论文，不重复已收录内容。
> **检索时间**: 2026-09-15 GMT+8（cron）
> **窗口**: list 页最新分组 2026-09-14（432 unique base ID）→ 与 covered_ids（642）比对未覆盖 **402 篇** → 标题粗筛（score≥1）124 候选 → 人工剔除领域应用（医疗/交通/无人机/语音识别/控制等）→ 逐篇抓 abs 页补录 **15 主条目 + 14 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、Agent 工具接口与记忆（5 篇）

### 1. Is Bash All You Need? An Empirical Study of Tool Interfaces for Enterprise Digital Worker Agents

- **ID:** [2609.11999v1](https://arxiv.org/abs/2609.11999v1) | [📄 PDF](https://arxiv.org/pdf/2609.11999v1)
- **作者:** Hazel Mak, Susheel Suresh, Sahil Bhatnagar, Barry Wang, Chhaya Methani, Alejandro Gutierrez Munoz
- **分类:** cs.CL, cs.SE
- **摘要:** 通用 shell 能否超越专用工具？企业工作涉及跨应用/服务移动、与同事协作、专业分析。在 TheAgentCompany 和 APEX-Agents 上用 Opus-4.8 与 GPT-5.5 对比五种工具接口：typed tools、typed tools+bash、bash alone、bash+持久 agent 合成工具、programmatic tool calling（PTC，动作限制在 typed tool 目录中的程序调用）。**bash alone 在两个基准上都优于 typed tools**（TheAgentCompany 提升 21.8-24.5pp）。
- **关联度:** ★★★★★ 「通用 shell > 专用工具接口」的实证——直接支持 k 的 terminal 优先哲学；「bash + agent 合成工具」「程序化工具调用」两种形态对 k 的工具链设计（脚本沉淀→技能化）有启发

### 2. LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory

- **ID:** [2609.12436v1](https://arxiv.org/abs/2609.12436v1) | [📄 PDF](https://arxiv.org/pdf/2609.12436v1)
- **作者:** Hanyu Zhao, Yuqian Feng, Zhenyu Song, Yuanchao Cheng, Yance Jiao, Tengfei Pan, Li Du
- **分类:** cs.AI
- **摘要:** 长运行 LLM agent 需要跨交互维持连贯内部状态的记忆机制。研究 lifecycle-labeled memory：训练时写事件带生命周期元数据，评测时按阶段感知读。生命周期不匹配会让**临时信息覆盖持久知识 → 持久 agent 行为漂移**。LifeFuse-Mem 是生命周期感知的神经记忆框架。
- **关联度:** ★★★★★ 记忆生命周期分层——与 k 的记忆体系（瞬时/会话/任务/核心四级）直接同题；「临时信息覆盖持久知识→行为漂移」正是 k 的记忆整合（memory-crystal-consolidation）要防的核心风险

### 3. CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory

- **ID:** [2609.12354v1](https://arxiv.org/abs/2609.12354v1) | [📄 PDF](https://arxiv.org/pdf/2609.12354v1)
- **作者:** Changjian Wang, Rongzhen Li, Weili Guan, Shuming Shi, Quan Lu, Ning Jiang
- **分类:** cs.CL
- **摘要:** 长程对话 agent 需从扩展对话历史回忆信息回答查询，但直接用全历史昂贵且不可靠，压缩记忆单元又会丢细粒度证据。CueMem 基于自传体记忆的建构主义视角：**把记忆记录当作检索线索而非自包含证据**，从源轮次重建查询相关的对话上下文。构建阶段提取细粒度记忆线索并链接到源轮次；查询时检索线索并重建上下文。
- **关联度:** ★★★★ 记忆「线索→重建」范式——与压缩记忆/RAG 互补；「记忆记录=线索不是证据」对 k 的检索增强对话与记忆注入方式有方法论价值

### 4. Residual Vector-based Reconstruction as Long-Context Recall Regardless of Context Window Size

- **ID:** [2609.12686v1](https://arxiv.org/abs/2609.12686v1) | [📄 PDF](https://arxiv.org/pdf/2609.12686v1)
- **作者:** MyungHoon Ryu, XinYu Piao, Jong-Kook Kim
- **分类:** cs.AI, cs.CL
- **摘要:** LLM 处理长上下文时 token 级显存随输入线性增长；模型优化与有损提示压缩都解决不了超出预训练与尺寸受限窗口的长上下文回忆。提出**免训练的长上下文回忆**：用 FFN 层参数激活（残差向量存储源文本事实）重建事实，随上下文增长 GPU 显存近恒定。
- **关联度:** ★★★ 免训练常显存长上下文回忆——本地推理（RTX 4060 8GB）长文档场景的可行方向；「残差向量=事实存储」对 k 的上下文管理/压缩策略有参考

### 5. Online Video Agent Harness for Long Video Understanding

- **ID:** [2609.12818v1](https://arxiv.org/abs/2609.12818v1) | [📄 PDF](https://arxiv.org/pdf/2609.12818v1)
- **作者:** Sen Yang, Boqiang Duan, Jing Yang, Weihao Bo, Jie Liu, Boyuan Tong, Ze Feng, Wenkang Zhang, Jingdong Wang, Hua Wu
- **分类:** cs.AI, cs.CV
- **摘要:** 长视频理解=视觉大海捞针：查询相关证据稀疏分布长时轴，密集帧塞进单 VLM 上下文会 context rot + 高成本。现有视频 agent 依赖查询无关离线预处理或临时工具集。VideoXAgent 是**纯在线视频 agent harness**：从视频文件+用户查询出发，规划分解任务、按需调用专用专家工具、聚合多模态证据出最终答案。
- **关联度:** ★★★ 在线视频 agent harness——sora 的抖音视频流水线/长视频分析的参考；「按需调专家工具、避免整段塞上下文」与 k 的 tool routing / 上下文预算同构

---

## 二、Agent 治理与评估（6 篇）

### 6. Scan the Skill, Govern the Action: Composing Registry Verdicts with Runtime Consequence Control

- **ID:** [2609.12001v1](https://arxiv.org/abs/2609.12001v1) | [📄 PDF](https://arxiv.org/pdf/2609.12001v1)
- **作者:** Rohit Taneja, Travis Weber
- **分类:** cs.CR, cs.SE
- **摘要:** Agent 技能注册表筛选发布内容。OpenClaw 安全团队报告：**扫描器组合重叠最多 10.4%，81.9% 被标记技能只被单一扫描器抓住**。作者认为开放问题不是「哪个扫描器对」而是「在问什么问题」——每个扫描器回答「这技能是否恶意？」，但「此操作此刻在此 operator 下是否被允许？」不是它们设计的。对 66,192 个公开 ClawHub 技能版本做三个测量：705 个技能（135 个发布者）所有扫描器与注册表 judge 都判干净……
- **关联度:** ★★★★★ 直接命中 k 的 skill-vetter / 外部技能安装安全门禁——「单扫描器覆盖 81.9% 独中」证明不能只信一个扫描器；「组合注册表判决 + 运行时后果控制」对 k 的 skill 审批门禁有直接设计启发

### 7. Can We Trust LLM Judges: A Study of Capability-Dependent Biases and Multi-Judge Ensemble for Bias Calibration

- **ID:** [2609.12002v1](https://arxiv.org/abs/2609.12002v1) | [📄 PDF](https://arxiv.org/pdf/2609.12002v1)
- **作者:** Gemma Zhang, Prachi Badarayani, Asmi Kumar, Sadid Hasan, Sulaiman Vesal
- **分类:** cs.AI, cs.LG
- **摘要:** LLM 越来越多当自动裁判（训练+评测），但个体裁判有系统偏差。聚焦绝对评分任务：四个基准 × 六模型（36 judge-examinee 对）——**模型任务精度强预测判分精度（Pearson r≥0.90）且反向预测方向性偏差（r≤-0.83）**；更能力强的被评模型一致得到更宽松评分（能力依赖偏置）。多裁判集成可校准该偏置。
- **关联度:** ★★★★ LLM judge 偏置实证——k 的多源盲评（Gemini 二审/跨源评估）的学术依据；「能力依赖偏置 + 多裁判集成校准」对 k 的模型评估方法直接可复用

### 8. When Agent Metrics Measure Different Things: An Evidence-Grounded Audit of the Praxa AI Pipeline

- **ID:** [2609.12017v1](https://arxiv.org/abs/2609.12017v1) | [📄 PDF](https://arxiv.org/pdf/2609.12017v1)
- **作者:** Stefan G. Creadore, Peyton Woakz
- **分类:** cs.AI, cs.SE
- **摘要:** Agent 评估可能在数值上正确但测量的构念与标签暗示的不同。对 Praxa AI 实施文件/历史评估工件/运行记录做回溯测量审计：139 例离线路由报告 112 过 27 败却零 gating 失败（已知缺口被明确豁免于门禁）；8,843 行工具尝试中 121 个时长等于 int32 最大值且带 abandoned-client 标签（数据库代码钳制生命周期年龄）——指标被豁免清单与钳制值静默扭曲。
- **关联度:** ★★★★ 「指标数字对但构念错」——k 的交付门禁（G5/服务质检/agent-self-evaluation）要防的典型陷阱：豁免清单、钳制值会让门禁静默失真；「审计评估工件本身」对 k 的自评体系有方法参考

### 9. EduFair-Bench: Evaluating Pedagogical Fairness of LLM Tutors Across Student Demographics

- **ID:** [2609.12949v1](https://arxiv.org/abs/2609.12949v1) | [📄 PDF](https://arxiv.org/pdf/2609.12949v1)
- **作者:** Jiaxu Zhao, Bahar Radmehr, Fares Fawzi, Tanya Nazaretsky, Tanja Käser
- **分类:** cs.AI
- **摘要:** LLM 越来越多当导师，但不清楚是否平等支持所有学生。EduFair-Bench 审计 LLM 导师的**教学公平**：多领域题库（数学/物理/化学）+ 受控模拟（固定 LLM 学生与每个导师交互，跨四维九层人口统计：性别/移民背景/第一语言/社会经济地位）。教学质量按 5 个回合级教学指标 + 4 个对话级指标评分。
- **关联度:** ★★★★ LLM 导师公平基准——墨题 AI 辅导/家教业务的评测模板；「固定学生 × 导师 × 人口统计分层」对 k 的 AI 教学功能验收（primary-education-tutoring）有参考

### 10. How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks

- **ID:** [2609.13009v1](https://arxiv.org/abs/2609.13009v1) | [📄 PDF](https://arxiv.org/pdf/2609.13009v1)
- **作者:** Ali Ansari, Haoran Sun, Andy Zeyi Liu, Mark Jabbour, Yongshan Ding, Steven Girvin, Yu He, Sohrab Ismail-Beigi, Aleksander Kubica, Owen D. Miller 等
- **分类:** cs.AI
- **摘要:** 主流物理基准（含 Artificial Analysis Intelligence Index 2026）低分暗示前沿模型仍挣扎于高级物理，但专家实际使用体验不符。在六个常用物理基准上重评 + 专家审计（仅文本、可验证最终答案；各子领域教授/研究生逐题复评）——**发现评测损坏与领先基准接近饱和**：低报告分数部分源于评测本身的问题。
- **关联度:** ★★★ 「专家复评揭示基准损坏 + 饱和」——评测可信度方法论：专家复评是检测基准损坏/饱和的黄金标准；对 k 评估模型/技能评测时的「基准是否坏了」意识有启发

### 11. Beyond Vector Similarity: Hierarchical Context-Aware Graph RAG vs Standard RAG in Enterprise Code Migration

- **ID:** [2609.12464v1](https://arxiv.org/abs/2609.12464v1) | [📄 PDF](https://arxiv.org/pdf/2609.12464v1)
- **作者:** Nilesh Jaiswal, Aniket Agrawal, Arjit Shukla, Divya Malhotra, Saurabh Garg, Suchit Puri, Suddhasatwa Bhaumik
- **分类:** cs.AI
- **摘要:** 企业把遗留单体迁移微服务时大量用 LLM 自动代码翻译；传统向量 RAG 抓孤立 chunk 切断继承链 → 高编译失败率。HCRG 方法：tree-sitter 提取 AST、架构边映射进 Google Cloud Spanner Property Graph、序列化进 Gemini Context Cache 做拓扑感知检索。
- **关联度:** ★★★ 图 RAG 解决「向量相似度切碎拓扑」——墨题代码库/知识图谱检索、GraphRAG 应用的工程参考；「AST + 属性图 + 上下文缓存」对 k 的代码理解工具链有启发

---

## 三、Agent 人设与代码质量（4 篇）

### 12. Creating an Atomic User Model for Personality-Aware Large Language Model Interaction

- **ID:** [2609.12086v1](https://arxiv.org/abs/2609.12086v1) | [📄 PDF](https://arxiv.org/pdf/2609.12086v1)
- **作者:** B. Sankar, Deepthika S, Pawni Yadav, Amogh A S
- **分类:** cs.AI, cs.CL, cs.HC
- **摘要:** LLM 助手应写得像用户本人；主流是单通道：从对话历史总结偏好再插回上下文——这颠倒了推理顺序。**偏好是任务相关的表层，人格结构相对稳定**；只存偏好的系统每次任务变化都要重新认识用户。提出 personality seepage（提示词语言表面带人格指纹，助手镜像它却访问不到背后人格）与 Atomic User Model（AUM，人类可读的用户人格组织表示）。
- **关联度:** ★★★★ 「偏好≠人格，存人格不存偏好」——k 的 SOUL.md / 人设与用户画像设计的理论支撑；「单通道偏好重插入颠倒推理顺序」对 k 的记忆注入方式有直接警示

### 13. BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents

- **ID:** [2609.12394v2](https://arxiv.org/abs/2609.12394v2) | [📄 PDF](https://arxiv.org/pdf/2609.12394v2)
- **作者:** Tong Ye, Kunyang Han, Guozhi Wang, Longqiang Luo, Zhifeng Ding, Yongxiang Zhang 等
- **分类:** cs.AI
- **摘要:** 移动 GUI agent 从多模块框架转向端到端原生模型，工业部署三缺口：**沙箱训练与生产环境分布不匹配、昂贵真机失败未被利用、固定基准饱和失去迭代引导力**。BlueLM-GUI（35B-A3B）真机为中心飞轮：Every Sample Matters（双轨流水线：异构三系统共识评估 + 纠错推导模块把每条轨迹救成可用监督）、Every Rollout Counts……
- **关联度:** ★★★★ 真机飞轮自改进 GUI agent——sora 的安卓真机自动化（uiautomator2/adb）与 computer-use 的工业级参考；「沙箱→真机分布不匹配 + 失败轨迹回收」对 k 的 UI 自动化测试有启发

### 14. What is the Difference Between Me and You? Benchmarking the Quality Gap Between Human-Written and AI-Generated Code

- **ID:** [2609.12708v1](https://arxiv.org/abs/2609.12708v1) | [📄 PDF](https://arxiv.org/pdf/2609.12708v1)
- **作者:** Cristina Improta, Pietro Liguori, Domenico Cotroneo
- **分类:** cs.AI, cs.SE
- **摘要:** AI 编码助手成为生产软件合著者，但评测聚焦功能正确性，忽略决定生命周期成本的代码质量维度。**787,562 个函数对**（Python/Java/C）：每个人类函数从开源仓库挖掘、按 docstring 用三个 AI 助手（OpenAI GPT、DeepSeek-Coder、Qwen2.5-Coder）生成配对实现。刻画结构复杂度与统计自然度，静态分析发现映射到 Orthogonal Defect Classification 与 CWE。
- **关联度:** ★★★★ 大规模 AI 代码质量差距实证——k 的 Codex 委派产出 review（ai-code-review / requesting-code-review）的量化依据；「功能正确≠质量」对 k 的代码门禁设计有支撑

### 15. Hieronym: Leveraging Hierarchical Multi-Source Information for Function Renaming in Stripped Binary

- **ID:** [2609.12457v1](https://arxiv.org/abs/2609.12457v1) | [📄 PDF](https://arxiv.org/pdf/2609.12457v1)
- **作者:** Xiaoling Zhang, Jian Sun, Dawei Wang, Chongyu Wang, Li Chen, Zhaoteng Yan, Peipei Liu, Lixiao Zhang, Dan Li
- **分类:** cs.SE
- **摘要:** 剥离二进制函数重命名显著提升逆向工程师效率。难点：跨指令集/架构/编译器优化从底层二进制捕获函数语义并表达为简洁可读名字。现有方法要么语义捕获不全面、要么泛化到未见二进制有限。Hieronym 是生成式 LLM 框架：**分层总结多源信息**做函数重命名。
- **关联度:** ★★★★ LLM 剥离二进制函数重命名——sora 的逆向技能（ai-assisted-reversing / vmp-reversing / miniapp-reversing）直接可用工具方向；「分层多源信息总结」对 k 的逆向分析提示词模板有参考

---

## 四、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.12471](https://arxiv.org/abs/2609.12471v1) | AMDKernelVault: Large-Scale Datasets and Agentic Training for AMD GPU Kernel Optimization | 开放 HIP/Triton 内核语料 + agent 流水线（HIPKernelGen/TritonKernelGen：PyTorch→内核、ROCm 编译验证、AMD 硬件延迟画像）；62,153 个执行验证 HIP 样本 + Qwen3-8B SFT——GPU kernel agent 训练基建，k 本地推理对照参考 |
| 2 | [2609.12757](https://arxiv.org/abs/2609.12757v1) | GraphAHA: Graph-Based Adaptive Search with Heterogeneous Actions for Test-Time Code Generation | 测试时代码生成的图搜索：树搜索把每段生成历史当独立状态导致重复评估；图结构共享收敛轨迹统计 + 异构动作（采样/修复/推理）在线分配有限预算 |
| 3 | [2609.12704](https://arxiv.org/abs/2609.12704v1) | Implicit Personality Representations in Humans and LLMs | 数百万众包人格评分构建人类内隐人格矩阵，与 Qwen2.5-7B 对比激活矩阵对齐（Mantel r=0.77）——LLM 内部表征复现人格关系结构 |
| 4 | [2609.12162](https://arxiv.org/abs/2609.12162v1) | Can LLMs in Draft-Verify-Revise Pipelines Resolve Deictic Ambiguity? | D-V-R 流水线各阶段 LLM 对「previous」等指示语解析不同 → deictic shift 改变所指——编排模式的下游陷阱：阶段间上下文级联会漂移指代 |
| 5 | [2609.12486](https://arxiv.org/abs/2609.12486v1) | Adaptive Agent Design | 非马尔可夫环境下 agent 自由选择状态转移核 + 优化状态反馈策略的双层设计；soft Q-learning 几乎必然收敛到 soft Bellman 不动点——控制论视角的 agent 设计 |
| 6 | [2609.13073](https://arxiv.org/abs/2609.13073v1) | Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval | 把自主端到端 ML 研究框架适配开放端工业级问题（电信工单检索）——AI for Science 从窄搜索空间走向开放问题的案例 |
| 7 | [2609.12437](https://arxiv.org/abs/2609.12437v1) | Beyond the Query: Do Retrieval Signals Improve Adaptive Multimodal RAG Routing? | 文档/音频/视频 RAG 对比 query-only 与 query+retrieval 路由器：加检索信号没有可靠提升路由决策——自适应 RAG 路由消融实证 |
| 8 | [2609.12403](https://arxiv.org/abs/2609.12403v1) | Beyond ID Embeddings: Process-Grounded Language Modeling for Cognitive Diagnosis | 传统认知诊断模型用 ID 嵌入表示学生/习题/概念；PLCD 用语言派生结构做认知先验 + 答题记录校准学生后验状态——墨题错题诊断/学情分析建模参考 |
| 9 | [2609.12366](https://arxiv.org/abs/2609.12366v1) | ORQA: An Occupation-Realistic Question and Answer Framework for LLM Professional Knowledge | O*NET 职业 ↔ 权威职业网站（监管/执照/专业组织/政府出版物）→ 可溯源 QA 对，覆盖 110+ 职业——职业级 LLM 知识评测生成框架 |
| 10 | [2609.12623](https://arxiv.org/abs/2609.12623v1) | SteerDuplex: Steerable Duplex Speech Dialogue Models | 全双工语音对话模型的可操控性（语调/人设/语速/声音风格按指令切换）缺失；Moshi 基座微调 + 文本/音频可操控性分类学 |
| 11 | [2609.13058](https://arxiv.org/abs/2609.13058v1) | Expert-Space Exploration in MoE Reinforcement Learning | 扰动专家路由可改变输出、增加 rollout 多样性（类似提升解码温度）；直接扰动会激活不合适专家 → 专家空间探索策略 |
| 12 | [2609.12769](https://arxiv.org/abs/2609.12769v1) | Unified Agentic Video Editing Across Levels of Complexity and Creativity | agentic 工具做自动化视频剪辑：三任务（场景预览/视频摘要/电影预告片）跨编辑目标/复杂度/创造力评估——sora 的抖音/视频剪辑流水线参考 |
| 13 | [2609.12923](https://arxiv.org/abs/2609.12923v1) | Dissecting GPU Utilization for LLM Inference on Nvidia Hopper | 单个 SM 利用率百分比把多种机制压成一个数字，decode 阶段（单请求单 token、GMMA 64 行片段只填一小部分）最严重；H100 NVL 上剖析 vLLM+FA3+cuBLASLt |
| 14 | [2609.12482](https://arxiv.org/abs/2609.12482v1) | When Does AI Augment Work? A Workflow-Level Framework for Human-Agent Collaboration | 定义 AI 增强六条件（持久净价值/有意义人类控制/问责与恢复/长期人类发展等），把分析从原子任务扩展到整个工作流——人机协作价值框架化评估 |

---

## 今日要点（主题信号）

1. **技能治理从「静态扫描」走向「运行时后果控制」**：12001 用 66,192 个 ClawHub 技能实测证明单扫描器覆盖不足（81.9% 只被一个扫描器抓住），把问题从「技能是否恶意」重构为「此操作此刻是否允许」；与 09-14「动作前验证」主线延续——治理从扫描层下沉到执行层。
2. **工具接口「简单通用优先」**：11999 实证 bash alone 优于 typed tools 21.8-24.5pp；与 09-14「Harness or Model」呼应——agent 工具链往「少而通用 + 合成工具」收敛，接口选择是可测量的事。
3. **记忆系统「生命周期分层」+「线索重建」双线**：12436 防临时信息覆盖持久知识（行为漂移）；12354 记忆记录=检索线索而非自包含证据；12686 免训练常显存长上下文回忆。记忆从「存什么」深化到「信息寿命 + 如何重建」。
4. **评测可信度「专家复评 + 构念审计」**：13009 专家复评揭示物理基准损坏与饱和；12017 审计发现指标数字对但构念错（豁免清单/钳制值）；12002 LLM judge 能力依赖偏置需多裁判集成——「评测评测器」成为独立主题。
5. **代码质量「功能正确≠质量」**：12708 78 万函数对实证 AI 代码与人类代码的质量差距；与 09-14「测试通过≠部署可接受」同构——结构复杂度/统计自然度/缺陷分类等质量维度进入评测视野。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| Scan the Skill 2609.12001 | arxiv.org abs 页全文抓取 | ✅ 已确认（HTML 收录 + 全文摘要；ClawHub 66,192 技能版本测量） |
| Is Bash All You Need 2609.11999 | arxiv.org abs 页全文抓取 | ✅ 已确认（HTML 收录 + 全文摘要；TheAgentCompany/APEX-Agents 五接口对比） |
| LifeFuse-Mem 2609.12436 | arxiv.org abs 页全文抓取 | ✅ 已确认（HTML 收录 + 全文摘要；生命周期记忆框架） |
| 其余 26 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **技能扫描「单扫描器不足」进 skill-vetter**：12001「81.9% 被标记技能只被单一扫描器抓住」——k 装外部技能时不能只信一个扫描器/一次判断，组合判决 + 运行时权限上下文（此操作此刻是否允许）双检查
- 🔴 **LLM judge 能力依赖偏置**：12002「更能力强的被评模型得到更宽松评分」——k 的多源盲评（Gemini 二审等）固定「评谁」组合防系统性偏置，可考虑多裁判集成校准
- 🟡 **记忆生命周期元数据**：12436「临时信息覆盖持久知识→行为漂移」——k 的记忆整合（memory-crystal-consolidation）给条目加生命周期标记，防止短期任务信息污染核心记忆
- 🟡 **评测构念审计**：12017「数字对但构念错」——k 的门禁/自评（agent-self-evaluation）定期审计评估工件本身：豁免清单、钳制值、指标标签是否匹配
- 🟢 **待深读**：12001 Scan the Skill（技能注册表治理）、11999 Is Bash All You Need（工具接口实证）、12436 LifeFuse-Mem（记忆生命周期）、12002 LLM Judges（裁判偏置）→ core-contributions 候选

---

*本速览由 cron 自动生成：09-15 检查 list 页无新日期分组（最新仍 09-14，432 篇，索引冻结）→ 与 covered_ids（642）比对未覆盖 402 篇（09-14 正常速览仅盖 30/432≈7%）→ 标题粗筛（score≥1）124 候选 → 人工剔除领域应用 → 逐篇抓 abs 页补录（15 主条目 + 14 简评）。元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

---
状态：reading
