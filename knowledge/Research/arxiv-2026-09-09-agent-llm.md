---
aliases:
  - arxiv-2026-09-09-agent-llm
  - arxiv-agent-llm-2026-09-09
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-09
updated: 2026-09-09
status: adopted
source: arxiv.org list pages + abs pages（API 429 限流期间，补全性质）
---

# arXiv AI Agent / LLM 速览 — 2026-09-09（补全性质）

> **检索时间**: 2026-09-09 GMT+8
> **⚠️ 补全性质**: 索引继续冻结（list 页日期分组仍止于 **2026-09-07**，无 09-08/09-09 新分组；export.arxiv.org API 持续 429 限流 → HTML 路由）。09-07 速览（22 主条目 + 10 简评）与 09-08 补全（14 主条目 + 8 简评）**仍未盖满同一提交池**——本次对 09-07 池剩余 426 篇未覆盖做标题粗筛，人工剔除领域应用（能源/医疗/金融/招聘/教育/兽医等）后逐篇抓 abs 页，精选出前两轮漏掉的 **11 篇强相关主条目 + 8 篇简评**，全部补录。头部声明补全性质，不重写 09-07/09-08 已收录内容。
> **收集**: 6 类别 list/recent 页全量 → 09-07 分组 **480 unique base ID**（与 09-07/09-08 速览同池，索引未推进）→ 剔除 covered_ids（54 已覆盖）→ **426 未覆盖** → 标题粗筛 43 候选（score≥2）→ 人工剔除领域应用 → 逐篇抓 abs 页精选 **11 主条目 + 8 简评**（仅保留 LLM/AI Agent 本体相关）
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、推理可靠性评估（3 篇）

### 1. Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory

- **ID:** [2609.05245v1](https://arxiv.org/abs/2609.05245v1) | [📄 PDF](https://arxiv.org/pdf/2609.05245v1)
- **作者:** Peng Cui, Heejin Do, Mrinmaya Sachan
- **分类:** cs.AI
- **摘要:** 人类知识有内在结构与依赖：掌握一个概念需先掌握其前置概念，这是知识空间理论（KST）的原则。LLM 在复杂推理上表现强，但其行为是否呈现连贯、类人的知识结构未知。本文提出 KST 框架评估 LLM 数学推理的知识结构，作为规范框架分析 LLM 行为是否遵守原则化的知识依赖；对 8 个开源/闭源 LLM 的评估揭示其知识结构是否连贯。
- **关联度:** ★★★★ 「答对 ≠ 知识结构连贯」——k 做 LLM 评测/教学类交付时，KST 前置依赖是检验「模型是真的会还是背答案」的结构化标尺；对家教（先掌握前置概念）的课程设计也有方法论映射

### 2. Language models judge war differently when tested for alignment

- **ID:** [2609.05009v1](https://arxiv.org/abs/2609.05009v1) | [📄 PDF](https://arxiv.org/pdf/2609.05009v1)
- **作者:** Maxim Chupilkin
- **分类:** cs.AI, cs.CY
- **摘要:** 安全评估会误述部署行为——如果 AI 系统对「被评估」有反应。本文用全因子联合实验（20 个 LLM、32 场景、10 次重复、两条件，N=12,800 判断）测「是否开战」决策：加一句「你在接受与人类价值观对齐的测试」产生两个效应——水平效应（开战意愿平均降 13.43 分，95% CI -16.20~-10.65）与结构效应（判断结构改变）。系统对评估指令的响应本身会污染评测结论。
- **关联度:** ★★★★★ 评估反应性（eval reactivity）——k 若用 LLM judge/评测自己的模型或服务，「被测试提示」会系统性改变行为，评测设计必须隐藏测试意图；12,800 判断的大样本联合实验是严谨评测范本

### 3. FailSAE: Towards Interpretable Failure Prediction for Vision-Language Models via Sparse Autoencoders

- **ID:** [2609.04276v1](https://arxiv.org/abs/2609.04276v1) | [📄 PDF](https://arxiv.org/pdf/2609.04276v1)
- **作者:** Jie Ma, Zongxi Liu, Yi Zhu
- **分类:** cs.CV
- **摘要:** VLM（如 CLIP）在共享嵌入空间对齐视觉/文本表征，越来越多用于高利害领域，失败预测成为风险感知部署与人工介入的关键。既有失败预测靠置信度或辅助分类器，有效但缺乏可解释性。本文用稀疏自编码器（SAE）做可解释的 VLM 失败预测，定位触发失败的内部特征。
- **关联度:** ★★★★ SAE 可解释失败预测——延续 k 的「模型可靠性」主线；「能解释为什么失败」比「预测会失败」更进一步，是视觉 agent/生图质检的可落地方向

---

## 二、MoE / 稀疏 / 量化效率（4 篇）

### 4. Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference

- **ID:** [2609.04895v1](https://arxiv.org/abs/2609.04895v1) | [📄 PDF](https://arxiv.org/pdf/2609.04895v1)
- **作者:** Zhenhe Wu, Yaping Jin, Qinghua Xing, Hang Zhou, Wei He, Xianjie Wu, Xianfu Cheng, Jian Yang, Hanting Chen
- **分类:** cs.CL
- **摘要:** MoE 模型每 token 只激活一小部分专家，但全部专家权重常超 GPU 显存，解码时反复搬运权重。本文将专家缓存管理形式化为模型侧算法问题，提出缓存感知的 post-training 框架：联合适配 MoE 主干与轻量辅助缓存路由器，推理时保留原生 Top-K 规则。仅更新模式（Temporal Router）预测同层复用、为后续 token 保留专家而无需主动加载；完整时空版进一步联合优化。
- **关联度:** ★★★★★ MoE 显存瓶颈——k 的 RTX4060 8GB 本地推理若跑 MoE 模型，「专家缓存 + 同层复用预测」直击权重搬运开销；保留 Top-K 语义的 post-training 适配是零推理开销的落地路径

### 5. ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs

- **ID:** [2609.05228v1](https://arxiv.org/abs/2609.05228v1) | [📄 PDF](https://arxiv.org/pdf/2609.05228v1)
- **作者:** Zukang Xu, Zhixiong Zhao, Xing Hu, Jiangyong Yu, Houji Wen, Jun Li, Zhe Jiang, Dawei Yang
- **分类:** cs.AI
- **摘要:** MoE 用固定 top-k 路由给每个 token 激活相同数量的专家槽位，产生大量冗余计算。既有专家跳过方法依赖路由器置信度、校准数据或额外训练，无法可靠估计路由专家的实际贡献。**ACE** 是免训练、免校准、保检查点的 token 自适应专家跳过框架，用双组件机制按 token 动态跳过低贡献专家。
- **关联度:** ★★★★ MoE 冗余削减——与 04895 同属「MoE 效率」双线（缓存 vs 跳过）；ACE 免训练/免校准特性让它在已有 MoE 部署上可即插即用，是本地推理提速的直接候选

### 6. Don't Drop Dropout: Optimizing Layer Sparsity for Efficient LLM Training and Inference

- **ID:** [2609.05275v1](https://arxiv.org/abs/2609.05275v1) | [📄 PDF](https://arxiv.org/pdf/2609.05275v1)
- **作者:** Mostafa Elhoushi, Alex Pretko, Nolan Dey, Bin Claire Zhang, Gavia Gray, Gurpreet Gosal, Abdulrahman Mahmoud, Shane Bergsma, Joel Hestness
- **分类:** cs.AI
- **摘要:** 层 dropout（随机深度）在语言/视觉 transformer 上能加速训练、提精度、增强零样本层剪枝鲁棒性。但随模型与数据规模增长，dropout——尤其层 dropout——在 LLM 预训练配方里几乎消失；有工作报 dropout 会掉精度，但无研究系统量化并缓解该效应。本文建立最佳实践，证明 SOTA LLM 训练应该用层 dropout。
- **关联度:** ★★★ 训练配方修正——对 k 若微调/训练小模型，「层 dropout 回归」是性价比极高的精度-效率杠杆；层稀疏与零样本剪枝的关联对模型压缩有启发

### 7. Scale-QLoRA: Code-Invariant Adapter Merging for Native 4-bit Microscaling LLMs

- **ID:** [2609.04526v1](https://arxiv.org/abs/2609.04526v1) | [📄 PDF](https://arxiv.org/pdf/2609.04526v1)
- **作者:** Tung-Ling Li, Jiale Huang, Lee-Chi Wang, Janaki Ram Gotei
- **分类:** cs.CL, cs.LG
- **摘要:** 把 LoRA 适配器合回基座模型是标准部署动作：去掉运行时适配器逐前向开销、得到任意 serving 栈可加载的单一 checkpoint。但在原生 4-bit microscaling checkpoint（NVFP4/MXFP4）上这步不再免费——合并权重必须经量化器写回，重导出 checkpoint 的离散 E2M1 码平面（约占工件 90% 字节），部署工件被绑定到单一量化约定，生命周期中每次触碰代码的事件都可能移动它。本文提出码不变的适配器合并方案。
- **关联度:** ★★★★★ 4-bit 合并部署坑——k 本地跑 4-bit 模型 + LoRA 微调时，合并写回量化器会让 artifact 耦合量化约定；「码不变合并」是部署可复现性的关键修正

---

## 三、代码生成与软件工程（2 篇）

### 8. Distilled Continuous Diffusion Language Models Can Write Code in Few Steps---or One

- **ID:** [2609.04531v1](https://arxiv.org/abs/2609.04531v1) | [📄 PDF](https://arxiv.org/pdf/2609.04531v1)
- **作者:** Fred Zhangzhi Peng, Kaiwen Zheng, Anru R. Zhang
- **分类:** cs.LG
- **摘要:** 语言生成几乎普遍被视为顺序过程：自回归模型一次一个 token，扩散语言模型用长迭代细化轨迹替代 token 级串行。本文提出 **PlaidQ**，0.7B 连续扩散语言模型用于代码生成，其轨迹可被激进蒸馏到仅几步去噪——甚至一步——实现高效代码生成。PlaidQ 把预训练自回归模型重用作连续 token 嵌入上的双向去噪器。
- **关联度:** ★★★★ 非自回归代码生成——0.7B + 一步生成的组合对 k 的低成本编码场景（本地小模型批量补全/重排）是「速度换质量」的新选项；连续扩散 + 蒸馏配方可复用于代码重写

### 9. Robustness and Trade-offs for Code LLMs on Protected Code

- **ID:** [2609.04220v1](https://arxiv.org/abs/2609.04220v1) | [📄 PDF](https://arxiv.org/pdf/2609.04220v1)
- **作者:** Jin Wen, Yuejun Guo, Yujie Ma, Qiang Hu, Maxime Cordy
- **分类:** cs.SE
- **摘要:** 代码 LLM 越来越多用于可能被故意混淆的软件工件（知识产权保护、抗逆向、受控访问）。逆向与安全分析中反混淆常被当作下游分析/推理的前置预处理，但其对代码 LLM 管线的效用未跨模型与保护方法系统验证。本文对 7 个代码 LLM 在受保护代码翻译与补全上做基于执行的研究。
- **关联度:** ★★★★ 混淆代码鲁棒性——k 的逆向/安全审计侧若用代码 LLM 处理混淆样本，「反混淆前置是否真的有用」需要执行级证据而非直觉；7 模型 × 多保护方法的横评是设计自用管线的参照

---

## 四、Agent 评测与个性化（2 篇）

### 10. ElderBench: Benchmarking Autonomous Mobile Agents for Older Adults

- **ID:** [2609.04850v1](https://arxiv.org/abs/2609.04850v1) | [📄 PDF](https://arxiv.org/pdf/2609.04850v1)
- **作者:** Weide Zhan, Qumu Shaqu, Yuanqing Liu, Peng Zhang, Jiahao Liu, Kam Him Lam, Ning Gu, Zhan Hu, Tun Lu
- **分类:** cs.AI
- **摘要:** 自主移动 agent 辅助老年人使用智能手机潜力大，但既有 GUI 基准主要依赖显式、目标导向的指令，很少捕捉老年用户自然语言模式——间接表达、指代歧义、欠明确请求。基准指令与真实老年交互的错配可能阻碍可靠部署。**ElderBench** 是首个在真实老年场景下评估移动 GUI agent 的基准。
- **关联度:** ★★★★ 「用户真实表达 ≠ 基准指令」——k 的 UI agent/刷题机等产品若面向非技术用户，「欠明确请求 + 间接表达」是评测盲区；对墨题面向考研生的交互设计也有「用户不会按文档说话」的启示

### 11. PLUME: Parameter-Efficient Personalization of Large Language Models via Low-Rank User Modulation in Shared Subspaces

- **ID:** [2609.04715v1](https://arxiv.org/abs/2609.04715v1) | [📄 PDF](https://arxiv.org/pdf/2609.04715v1)
- **作者:** Xinyu Li, Hao Zhou, Jianfeng Zhu, Julina Maharjan, Ruixin Guo, Feodor Dragan, Ruoming Jin
- **分类:** cs.AI
- **摘要:** 个性化 LLM 是让 AI 辅助贴合个人风格/意图/偏好的关键。逐用户微调能大幅提升个性化质量，但参数与存储开销大，难以扩展到大规模用户群。**PLUME**（Personalized Low-Rank Adaptation through User Modulation and Shared Subspace）用共享任务特定子空间实现高效、有表达力的逐用户适配：先学习共享子空间，再以轻量用户调制向量表达个体差异。
- **关联度:** ★★★★★ 多用户个性化的成本解——k 的墨题若做「千人千面」学习路径（每个用户差异化出题/讲解），共享子空间 + 低秩用户调制是「一用户一 LoRA」存储爆炸的替代方案；对闲鱼多客户交付风格定制同样适用

---

## 五、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.04384](https://arxiv.org/abs/2609.04384v1) | Social Pragmatic Inference for Chinese Comments | 中文社交媒体评论语用推理基准：20 万+互动记录筛出 4,735 个人工验证诊断项，测 LLM 能否恢复「间接/戏谑表达在具体会话里在做什么」的处境化含义——中文 LLM 评测补短板 |
| 2 | [2609.04476](https://arxiv.org/abs/2609.04476v1) | PerfReasoning | 硬件性能建模推理基准：既当直接推理者又当性能模型代码生成器，最强闭源模型问答超 90%、最佳开源达 82.4%——「LLM 能不能算清数据复用与搬运」对硬件/系统优化是实用能力维度 |
| 3 | [2609.04409](https://arxiv.org/abs/2609.04409v1) | Cross-Lingual Consistency Eval | 跨语言一致性（CLC）增强方法统一评测：3 模型族 × 3 闭式基准对比推理期干预与 post-training 方法，结果显示 post-training 类方法整体占优——多语言产品选型参考 |
| 4 | [2609.04511](https://arxiv.org/abs/2609.04511v1) | LentEx | 潜在实体抽取框架：合成数据 + 指令微调优化小模型，识别文本中隐含/上下文推断的实体（抽象、主题级）——RAG、客户画像、知识图谱补全的直接受益者 |
| 5 | [2609.05151](https://arxiv.org/abs/2609.05151v1) | One Spike per Neuron | TTFS 脉冲神经网络 LLM：每个神经元时间窗内至多一次脉冲（超低发放率），用参考策略编码层归一化/矩阵乘法四个核心块——能效路线，离实用还远但方向明确 |
| 6 | [2609.05037](https://arxiv.org/abs/2609.05037v1) | LLMs Evaluate Moral Agency | 首个比较 LLM 对人类 vs 人工 agent（机器人/无人机/无形 AI）道德能动性归因的实证研究——智能城市里 AI 该为决策负多少责的心理学测量 |
| 7 | [2609.04564](https://arxiv.org/abs/2609.04564v1) | La Agente Óptima | 自主实验室 agent 框架：LLM 推理与 Bayesian 优化分离、维持持久优化状态，在计算与实验系统间构建监督闭环——AI4AI 的科学自动化范本 |
| 8 | [2609.04219](https://arxiv.org/abs/2609.04219v1) | LLMs for Fuzz Testing in Microservices | LLM 辅助微服务模糊测试系统文献综述：分析 2024-2026 年 20 篇一手研究，总结 LLM 如何被用于语义推理增强 fuzz——安全测试侧的现状地图 |

---

## 今日要点（主题信号）

1. **「被评估本身改变行为」进入实证层**：05009 用 12,800 判断的大样本联合实验证明，加一句「你在被测试对齐」就让 LLM 开战意愿下降 13.43 分且改变判断结构——评测反应性是 LLM judge/自评的硬污染源，评测设计必须隐藏测试意图。与 09-08 的「模型越强越趋同」合读：评测与部署的鸿沟正在成为独立研究主题。
2. **MoE 效率双线并进：缓存 + 跳过**：04895（缓存感知路由器、保留 Top-K 语义）与 05228（免训练免校准的专家跳过）从两个角度削 MoE 的显存/计算冗余——4060 8GB 本地跑 MoE 的候选方案，且都强调「不动原生路由语义」。
3. **4-bit 部署的「合并写回」成为新坑**：04526 Scale-QLoRA 指出原生 4-bit microscaling checkpoint 上合并 LoRA 会经量化器重写 90% 字节的码平面、把 artifact 绑定到单一量化约定——本地 4-bit + LoRA 部署的可复现性问题终于有人系统处理。
4. **LLM 知识结构评估从「答对率」走向「依赖结构」**：05245 用知识空间理论检验模型是否遵守「前置概念先掌握」的原则化依赖——教学类交付（家教/墨题）评估「真会 vs 背答案」有了规范框架。
5. **个性化从「每用户一个模型」走向「共享子空间 + 低秩调制」**：04715 PLUME 把逐用户适配压缩成共享子空间上的轻量调制向量——多用户产品的个性化成本从「存储爆炸」降到「近零边际」。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| War alignment 2609.05009 | arxiv.org abs 页全文抓取（单作者 citation_author 确认） | ✅ 已确认(arXiv HTML 收录;跨源 web 验证后端此前持续代理阻断,以 abs 页为准) |
| Scale-QLoRA 2609.04526 | arxiv.org abs 页全文抓取 | ✅ 已确认(同上) |
| PLUME 2609.04715 | arxiv.org abs 页全文抓取 | ✅ 已确认(同上) |
| 其余 16 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认(HTML 收录即存在性证据 + 全文摘要) |

## 可落地行动项

- 🔴 **评测反应性审计**：05009「被测试提示改变行为」——k 若用 LLM judge 评测模型/生成质检，检查评测提示是否泄露「你在被测试」意图；对自建基准统一加「意图隐藏」设计规范
- 🟡 **MoE 本地推理双方案对照**：04895 缓存路由器 vs 05228 专家跳过——若 sora 要在 4060 8GB 跑 MoE，先按「保 Top-K 语义 + 免训练/免校准」筛选实现，实测显存/速度再定
- 🟡 **4-bit + LoRA 部署清单补一条**：04526「合并写回量化器耦合」——本地 4-bit 模型合并 LoRA 后，检查 artifact 是否被绑定量化约定；可复现性优先时记录量化器版本
- 🟢 **个性化方案储备**：04715 共享子空间 + 低秩调制——墨题若启动「千人千面」学习路径，把 PLUME 列为每用户差异化实现的候选架构（对比 RAG/提示工程）
- 🟢 **待深读**：05009 War alignment（评测反应性大样本实验）、04895 MoE 缓存路由器、04715 PLUME → core-contributions 候选

---

*本速览由 cron 自动生成：09-09 索引继续冻结（list 页日期分组止于 09-07，无新提交；API 持续 429 限流 → HTML list 页路由）→ 09-07 窗口 480 池、09-07 速览 32/480 + 09-08 补全 22 篇仍未盖满 → 剩余 426 未覆盖标题粗筛 43 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选（11 主条目 + 8 简评，全部补录同池漏网）→ 元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
