---
aliases:
  - arxiv-2026-08-14-agent-llm
  - arxiv-agent-llm-2026-08-14
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-08-14
updated: 2026-08-14
status: adopted
source: export.arxiv.org API
---

# arXiv AI Agent / LLM 速览 — 2026-08-14

> **检索时间**: 2026-08-14 GMT+8
> **检索范围**: cs.AI / cs.CL / cs.LG / cs.SE / cs.CV / cs.RO,提交日期 08-13
> **原始检索**: cat:cs.AI+cs.CL+cs.LG 按提交日期倒序,Top 40 篇中精选 **18 篇**与 AI Agent / LLM 强相关
> **数据源**: [export.arxiv.org](https://export.arxiv.org)

---

## 一、Agent 系统与设计

### 1. AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design
- **ID:** [2608.13560v1](https://arxiv.org/abs/2608.13560v1) | [📄 PDF](https://arxiv.org/pdf/2608.13560v1)
- **作者:** Yaxin Luo, Haobin Jiang, Jialv Zou, ... Zhiqiang Shen, Xiaotong Li
- **分类:** cs.CV, cs.AI, cs.CL
- **摘要:** 把多模态源转化为结构化媒体输出可视为以 model-harness 系统为中心的长程 agentic 过程。现有范式静态、无法积累可复用经验。AutoDesign 提出**元 harness 优化器**指导代码 Agent 基于 rollout 反馈递归改进 harness。在论文→海报生成任务 PosterBench(100 篇论文、五学科)上,主赛道得分 78.32,超过闭源商业系统 Claude Design 7.45 分;7 种配置下集成 DesignHarness 平均提升 +12.4%;全自动长程循环 40 分钟执行 253 次工具调用、11 轮编辑,成本 <$3。
- **关联度:** ★★★★★ 递归自我改进 Agent 前沿;与 Hermes "知识自举/自动打磨"理念一致,媒体生成 agentic 化方向

### 2. OmniScientist: An Omni-Modal Omni-Discipline AI Scientist
- **ID:** [2608.13558v1](https://arxiv.org/abs/2608.13558v1) | [📄 PDF](https://arxiv.org/pdf/2608.13558v1)
- **作者:** Bobo Li, Hao Fei, Tianjie Ju, Mong-Li Lee, Wynne Hsu
- **分类:** cs.AI, cs.CL
- **摘要:** 现有 AI 科学家系统只在文本/代码/标签或预计算摘要上推理,缺少对科学起决定作用的空间、时间、跨通道、过程关系。OmniScientist 是端到端全模态 AI 科学家:感知层 + 3 个自主 Agent(idea/experiment/writeup)在确定性流水线中协作,直接处理异构原始证据(图像/信号/音频/视频/3D/轨迹/表格/公式/图)。36 个真实数据集全部完成"原始数据→成稿"全流程,平均论文分 6.3;与只接收预计算标量特征的盲版相比,直接感知在 7 个维度全胜,85% 配对判断获胜。
- **关联度:** ★★★★★ AI Scientist 全流程自动化标杆;论文写作流水线可借鉴其 novelty/rigour/claim 三道代码级检查

### 3. Intern-S2-Preview: Scientific Agentic Foundation Model
- **ID:** [2608.13505v1](https://arxiv.org/abs/2608.13505v1) | [📄 PDF](https://arxiv.org/pdf/2608.13505v1)
- **作者:** Intern 团队(多模态科学智能)
- **分类:** cs.LG, cs.CL, cs.CV
- **摘要:** 面向科学发现的 agentic 基础模型系列,支持多模态理解、推理、生成与长程任务。训练管线:科学多模态预训练 → 统一后训练(SFT + 可扩展多任务 RL + 黑/白盒 agentic RL + on-policy 蒸馏)。工程技巧含 partial rollout with off-policy correction、自适应长度正则、在线投机解码。397B 主模型扩展时间序列建模到数值预测;Memory Decoder 作为独立记忆增强路径,不改 397B 骨干即可快速科学特化(Biology-Instructions 56.92→60.32)。
- **关联度:** ★★★★ 科学 Agent 基础模型架构参考;agentic RL + 记忆增强路径设计值得关注

### 4. MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination
- **ID:** [2608.13476v1](https://arxiv.org/abs/2608.13476v1) | [📄 PDF](https://arxiv.org/pdf/2608.13476v1)
- **作者:** Saisha Shetty, Satvik Tripathi, Austin Lin, ... Tessa S Cook (Penn)
- **分类:** cs.AI, cs.CL
- **摘要:** 用确定性多 Agent 编排替代单体 LLM 提示的临床推理框架:抽取/推理/答案生成/评估四类角色专用 Agent 协作,显式上下文传递 + 可追溯中间输出,支持分阶段故障归因。Decomposer 模块从自然语言描述自动生成任务专用 Agent 提示,消除手动 prompt 工程。支持 API 和本地 CPU 部署,YAML 全配置免改码,模型无关、可解释。开源:https://github.com/Penn-RAIL/MARC-v1
- **关联度:** ★★★★ 多 Agent 编排 + 自动 prompt 生成的工程化参考;开源可本地部署

---

## 二、编码 Agent 与软件验证

### 5. Vero: Can AI Agents Build Formally Verified Software Repositories?
- **ID:** [2608.13522v1](https://arxiv.org/abs/2608.13522v1) | [📄 PDF](https://arxiv.org/pdf/2608.13522v1)
- **作者:** sunblaze-ucb 团队
- **分类:** cs.LG, cs.AI, cs.LO, cs.PL, cs.SE
- **摘要:** 首个评估 Agent 在**仓库级**联合实现+证明合成的基准。43 个多模块实例,源自真实仓库(Python/Dafny/Verus/Coq,覆盖密码协议到分布式系统),每个实例是 Lean 4 多模块仓库,含预定义 API 接口、人工精修形式化规格、参考实现;支持 proof-only 和 code-and-proof 两种模式。内置审计机制(允许 Agent 证明规格不可满足或参考代码不正确,暴露潜在缺陷)。最强 agent 仅完整解决 43 题中 27 题,最难仓库零规格关闭。开源:https://github.com/sunblaze-ucb/vero
- **关联度:** ★★★★★ 可信 AI 生成代码方向标杆;编码 Agent 能力边界实证(仓库级验证仍远未达标)

### 6. QuoteBench: How Matched Scores Can Hide Command-Path Failures
- **ID:** [2608.13547v1](https://arxiv.org/abs/2608.13547v1) | [📄 PDF](https://arxiv.org/pdf/2608.13547v1)
- **作者:** (LLM 编码 Agent 评估)
- **分类:** cs.AI, cs.SE
- **摘要:** LLM 编码 Agent 通过接口发 Bash 命令,接口会序列化、包装、重新解析模型输出——匹配执行分数无法区分"生成错误"和"执行路径引入的错误"。QuoteBench 用 14 个 incident 衍生的 56 个一次性任务 + 精确最终状态验证测量这个边界:同一 reply 经额外解析器回放,成功率下降 55.4~73.2 个百分点;披露边界后 6/8 配置恢复 30.4~60.7 点。GPT-5.6-sol 的匹配差仅 -3.6 点,却掩盖了 -64.3 点损伤和 +60.7 点补偿。**结论:评估命令型 Agent 必须报告模型配置/生成契约/执行路径/操作点/最终状态验证器,匹配分数不是模型固有属性。**
- **关联度:** ★★★★★ 直接适用于 Hermes/Claude Code 类工具型 Agent 的评测设计;防止"分数好看但实际失败"的评估陷阱

### 7. AaLLM: An End-to-End Analog Circuit Design Framework from Topology Generation to Sizing Using Large Language Models
- **ID:** [2608.13472v1](https://arxiv.org/abs/2608.13472v1) | [📄 PDF](https://arxiv.org/pdf/2608.13472v1)
- **作者:** (LLM 电路设计)
- **分类:** eess.SY, cs.AI
- **摘要:** 开源端到端多 Agent LLM 工作流:输入用户规格 → 输出网表(拓扑生成 + 电路 sizing)。自动从论文/教科书构建相关知识库,用 RAG 模拟电路设计专长;核心是**三 Agent 反馈系统**(Designer 定元件值 / Critic 审查 / Evaluator 仲裁,最小化迭代)。新拓扑 FoM 与已知拓扑相当,部分电路最高 3 倍;推理时 SPICE 调用减少 3x-4.5x,墙钟时间比现有方法快 40 倍。
- **关联度:** ★★★★ 与 sora 的 PCB/模拟电路兴趣直接相关;多 Agent 设计迭代 + RAG 知识库的工程范式可迁移到硬件设计自动化

---

## 三、LLM 训练与对齐

### 8. Synthetic Persona Pretraining: Alignment from Token Zero
- **ID:** [2608.13482v1](https://arxiv.org/abs/2608.13482v1) | [📄 PDF](https://arxiv.org/pdf/2608.13482v1)
- **作者:** (对齐研究)
- **分类:** cs.LG, cs.AI, cs.CL
- **摘要:** 传统对齐在预训练之后才引入助手身份,价值是"薄覆盖层"。SPP 从 token 零就把期望的助手人格安装进预训练:①用规范性价值宪法给预训练文档标注价值对齐的第一人称反思;②标准交叉熵同时训练原文+反思;③后训练用对话数据把人格绑定到助手身份(persona binding)。3B 模型 / 500B token 实验:改进宪法遵循和 jailbreak 鲁棒性,OOD 道德困境中的 misalignment 率下降,能力不损。早期干预关键:只在预训练末尾引入 SPP 效果显著更弱,且优势随预训练预算增加。
- **关联度:** ★★★★ 对齐范式新思路;"价值要从底层扎根而非事后覆盖"对 Agent 人格塑造有启发

### 9. LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure
- **ID:** [2608.13545v1](https://arxiv.org/abs/2608.13545v1) | [📄 PDF](https://arxiv.org/pdf/2608.13545v1)
- **作者:** (LLM 训练研究)
- **分类:** cs.CL, cs.AI, cs.LG
- **摘要:** 提出 LITTLECURRICULUM:面向美国小学教材的 88B-token 预训练语料,明确排除五年级以上概念/事实/词汇。从头训练 5B 模型得 LITTLELEARNER——语言能力足够开放评测,但知识与能力边界清晰映射到可解释的课程大纲。作为"发展受限沙盒"研究模型如何获取/表示/使用数据。首批实验:后训练和 in-context learning 能让模型更好利用已有知识,但**不会提升超范围能力**。
- **关联度:** ★★★ 受控知识暴露实验设计有方法论参考价值;"训练范围=能力边界"实证

### 10. Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining
- **ID:** [2608.13515v1](https://arxiv.org/abs/2608.13515v1) | [📄 PDF](https://arxiv.org/pdf/2608.13515v1)
- **作者:** Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda, ... Max Müller-Eberstein, Masaru Isonuma
- **分类:** cs.CL
- **摘要:** 提出不依赖下游任务/验证集选择的数据影响力度量:一个样本的影响力 = 其梯度更新在多大程度上缩小到给定预训练运行最终参数的平方距离,可从中间 checkpoint 估计,无需重训。应用于 Pythia/PolyPythia 18 个配置,发现系统性时间变化:训练早期文学类数据与"走向最终参数"的轨迹更对齐,后期 STEM 数据更强对齐,跨配置一致。
- **关联度:** ★★★ 预训练数据影响力分析新方法;对训练数据配比决策有理论参考

### 11. DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters Using Only Permissible Post-Training Data
- **ID:** [2608.13517v1](https://arxiv.org/abs/2608.13517v1) | [📄 PDF](https://arxiv.org/pdf/2608.13517v1)
- **作者:** Danish Foundation Models
- **分类:** cs.CL, cs.AI
- **摘要:** 1B 参数 HRM(Hierarchical Reasoning Model)架构语言模型,仅用许可数据从头训练,161 个数据集混合。英语性能强,丹麦语刷新 SOTA;20 个基准(英语/数学&代码/丹麦语)上超过原 HRM-Text 1B,与 Qwen 3.5 4B、Gemma 4 E2B 等更大模型竞争。开源:https://huggingface.co/danish-foundation-models/DFM-Mimir
- **关联度:** ★★★ 小模型 + 合规数据路线实证;对本地 LLM 部署有参考(1B 级别可本地跑)

---

## 四、LLM 行为与可解释性

### 12. Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent Specificity
- **ID:** [2608.13484v1](https://arxiv.org/abs/2608.13484v1) | [📄 PDF](https://arxiv.org/pdf/2608.13484v1)
- **作者:** Dananjay Srinivas, Saksham Khatwani, Maria Pacheco
- **分类:** cs.CL, cs.AI
- **摘要:** LLM 面对知识边界外的实体习惯性编造逼真细节,而非退回到更安全的一般性表述(幻觉根源)。用 Grice 合作原则框架:不确定指称时,合作说话者会沿特异性层级"退却",用信息量换真实性。T-REx 基准探测两个问题:①激活是否编码"指称是否在知识边界内"→ 是;②是否预期即将生成的指称特异性 → 是。**但两个信号在生成时没有调和**:模型即使实体未知也偏好具体指称。Gricean 对齐(把知识边界意识耦合到生成的特异性)是下一步。
- **关联度:** ★★★★★ 幻觉机理新解释 + 可操作的探测方法;"知识边界→生成策略"耦合可作为幻觉缓解研究方向

### 13. SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization
- **ID:** [2608.13538v1](https://arxiv.org/abs/2608.13538v1) | [📄 PDF](https://arxiv.org/pdf/2608.13538v1)
- **作者:** Weihan Meng, Hongzhu Guo, Yi Jing, ... Lei Hou, Juanzi Li
- **分类:** cs.CL
- **摘要:** SAE 特征解释目前依赖外部观测(浅层且昂贵)。SAEVerbalizer 把 SAE decoder 方向注入 LLM 表示并微调下游层,让 LLM 直接生成注入特征的自然语言解释。训练后的 verbalizer 能泛化到未见特征、跨独立训练的 SAE 字典迁移;轻量 adapter 可扩展到不同 LLM 的 SAE 特征。干预实验:注入多个方向得到含义组合,反转单个方向产生对应含义偏移。
- **关联度:** ★★★ 可解释性效率突破;SAE→自然语言解释的直接映射

### 14. Are You Sure You're Sure? On the Impact of Instruction Tuning on Confidence and Lexical Diversity
- **ID:** [2608.13430v1](https://arxiv.org/abs/2608.13430v1) | [📄 PDF](https://arxiv.org/pdf/2608.13430v1)
- **作者:** Irina Proskurina, Mayank Kumar, Oyindolapo O. Komolafe
- **分类:** cs.CL, cs.AI
- **摘要:** 指令微调模型表现出语言化过度自信。三组 matched base/instruction-tuned 模型在 QA 基准上:指令微调一致改变答案信心(预测准确率变化有限、基于似然的校准下降);对 rationale 多样性的影响非均匀——**跨 rationale 多样性一致下降,表层词汇多样性方向幅度因模型/基准而异**;控制答案选择和 rationale 长度后差异仍在,证明信心与 rationale 多样性捕捉的是指令微调的不同效应。
- **关联度:** ★★★ 指令微调副作用(过度自信 + 思维多样性下降)实证;对 Agent 输出可靠性有警示

---

## 五、推理加速与理论

### 15. DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees
- **ID:** [2608.13524v1](https://arxiv.org/abs/2608.13524v1) | [📄 PDF](https://arxiv.org/pdf/2608.13524v1)
- **作者:** (推理加速)
- **分类:** cs.LG
- **摘要:** 投机解码用并行验证多个 draft token 无损加速自回归 LLM。扩散 drafters 并行预测整块 token,但位置分布是边际的而非沿 draft 路径条件化。DARTree 无训练扩展 AR 修正头从链到树:单批扩展+评分固定宽度候选树,仅用 best-first 剪枝选验证树。7 个数学/代码/聊天基准、4 种模型-温度配置全部取得最高平均接受长度和加速:单轮最多接受 12.97 token(比 DFlash 多 98.6%、比 Domino 多 27.9%),最高 9.73 倍无损加速。
- **关联度:** ★★★ 本地 LLM 推理加速方案(对 sora 本地 Qwen3-8B 部署有潜在价值)

### 16. Algebraic Decomposition Theory for Transformer Length Generalization
- **ID:** [2608.13433v1](https://arxiv.org/abs/2608.13433v1) | [📄 PDF](https://arxiv.org/pdf/2608.13433v1)
- **作者:** (LLM 理论)
- **分类:** cs.FL, cs.AI
- **摘要:** Transformer 有时能泛化到比训练更长的序列,但缺乏精确刻画。论文首次完整刻画**哪些正则语言 transformer 能长度泛化**,并给出在语言语法幺半群规模上的多项式时间判定算法。关键洞察:Krohn-Rhodes 分解理论的构件(flip-flop 和简单群)在 C-RASP 中不可表达,而 C-RASP 的基本构件(无界计数)也不被有限半群表达——长度泛化由一个经典有限分解理论看不到的代数性质控制。把经典分解理论从有限半群推广到整数上的无限加法群,用整数迭代圈积刻画 C-RASP。
- **关联度:** ★★★ 长度泛化理论前沿;理解模型外推能力的数学基础

### 17. A Unifying Perspective on Causal World Models: From Observations to Representations to Structure
- **ID:** [2608.13456v1](https://arxiv.org/abs/2608.13456v1) | [📄 PDF](https://arxiv.org/pdf/2608.13456v1)
- **作者:** (世界模型综述/统一视角)
- **分类:** cs.AI, cs.CV
- **摘要:** 世界模型(WM)被视为智能 Agent 在分布外预测/规划/行动的基础。从因果视角统一研究多抽象层级的 WM:感知观测 → 环境动力学结构的表征。论证有用 WM 必须超越生成能力:捕获实体属性、实体间/实体-环境交互。给出因果 WM(CWM)的形式定义,连接因果表征学习、object-centric learning、因果发现、结构因果模型、基于模型的决策;并联系可辨识性文献,澄清 WM 组件何时可恢复、到什么等价程度。
- **关联度:** ★★★★ 世界模型 + 因果理论的统一框架;Agent 规划/推理的基础理论参考

### 18. AlayaWorld: Interactive Long-Horizon World Modeling — Full Technical Report (v1.1)
- **ID:** [2608.13492v1](https://arxiv.org/abs/2608.13492v1) | [📄 PDF](https://arxiv.org/pdf/2608.13492v1)
- **作者:** AlayaWorld Team, Kaipeng Zhang, Chuanhao Li, ... Zihui Gao
- **分类:** cs.AI
- **摘要:** 交互式长程世界模型改进版(骨干/分块自回归生成/训练数据不变)。核心原则:**条件信号应在潜在表示和时间结构上尽可能匹配生成内容**。两大改动:①用流式 3D 点缓存渲染器替代 depth-warping 空间记忆;②条件流水线重构——视觉条件编码进同一 causal-VAE 潜在空间,时间统计与生成视频一致。六项修改:运动感知潜在条件、因果编码重渲染空间记忆、像素空间时间记忆窗口对齐、hard memory dropout、训练/推理 VAE 编解码协议统一、移除 camera AdaLN 分支。
- **关联度:** ★★★ 长程世界模型工程细节;对交互式生成/游戏 AI(如 inZOI/Sims 类)有前瞻参考

---

## 今日要点

1. **编码 Agent 评测陷阱(QuoteBench)**:匹配分数会掩盖执行路径失败——评估工具型 Agent 必须报告完整配置链。对 Hermes 类 Agent 评测设计直接可用。
2. **Agent 递归自我改进落地(AutoDesign)**:meta-harness 优化 + rollout 反馈,低成本(<$3/40min)达到会议海报质量,媒体生成 agentic 化是实打实的方向。
3. **仓库级形式化验证仍是硬骨头(Vero)**:最强 agent 43 题仅 27 题全解,"可信 AI 代码"离实用还有距离。
4. **幻觉新解释(Gricean Retreat)**:模型内部有知识边界信号,但生成策略不消费它——"边界意识→生成耦合"是缓解幻觉的可行抓手。
5. **对齐前置(SPP)**:从预训练 token 零注入人格比事后对齐更有效且随预算增长优势扩大。

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
