---
aliases:
  - arxiv-2026-09-19-agent-llm
  - arxiv-agent-llm-2026-09-19
tags:
  - arxiv
  - research
  - ai-agent
  - llm
  - daily
created: 2026-09-19
updated: 2026-09-19
status: adopted
source: arxiv.org list pages + abs pages（09-18 窗口补全速览）
---

# arXiv AI Agent / LLM 速览 — 2026-09-19（补全）

> ⚠️ **补全性质**：2026-09-19（周六）检查 arXiv list 页**无新日期分组**（最新仍为 2026-09-18，602 篇窗口），09-19 窗口 HTML 搜索查询 0 条 —— 无新提交池。但 09-18 速览从 602 篇仅精选 27 篇（20 主 + 7 简，covered ≈4.5%），同池大概率仍有强相关漏网 → 本份为**补全速览**：对 09-18 同池补录漏网强相关论文（与昨日零重复，全部未覆盖）。
> **检索时间**: 2026-09-19 GMT+8（cron）
> **流程**: 09-18 分组 602 篇 → 与 covered_ids（740）比对 → 标题粗筛 53 候选 → 人工剔除领域应用（医疗/驾驶/交易/交通/视觉）→ 逐篇抓 abs 页精选 **13 主条目 + 5 简评**
> **数据源**: [arxiv.org/list](https://arxiv.org/list/cs.AI/recent) + 逐篇 abs 页

---

## 一、评测方法论与基准设计（3 篇）

### 1. What Do We Expect from LLMs? Mapping the Design of LLM Benchmarks

- **ID:** [2609.19182v1](https://arxiv.org/abs/2609.19182v1) | [📄 PDF](https://arxiv.org/pdf/2609.19182v1)
- **作者:** Chao Wang
- **分类:** cs.AI, cs.CL
- **摘要:** 对 LLM 评测需求的系统性元研究：映射 2022-01 至 2026-08 arXiv 上**14,767 篇**提出或更新评测资源的论文，用分期筛选 + 自动化全文编码考察目标系统/领域、评测材料与条件、打分机制的变化。发现：①对**行动、交互、专业应用**的评测日益增长，新旧设计元素长期并存；②模型参与不均衡——**LLM 打分**在 agent 与非 agent 组都增长，而**模型生成材料**近期未持续增长。核心反思：AI 参与构造测试、执行任务、评判回答时，「更多评测」是在提供更多独立证据，还是复制参与模型的偏好与盲点？
- **关联度:** ★★★★★ 评测设计元视角——k 的技能验证/产物断言体系（verify_digest_note、服务质检）的「由谁构造测试、由谁打分」同题；「LLM-as-judge 复制的偏好盲点」直接回应 k 的 Gemini 跨源盲评设计动机

### 2. PetriBench: Benchmarking LLM Reasoning over Dynamic State Spaces

- **ID:** [2609.19883v1](https://arxiv.org/abs/2609.19883v1) | [📄 PDF](https://arxiv.org/pdf/2609.19883v1)
- **作者:** Pyrros Koussios, Benjamin Jäger, John Hua Yao, Ajay Sridhar, Violet Xiang, Chenhao Li
- **分类:** cs.CL, cs.AI, cs.LO
- **摘要:** 用 Petri 网（建模并发/分布式系统的成熟形式化）评测 LLM 在**动态状态空间**上的推理：四类任务族按范围与时间视界区分，Easy/Medium/Hard 由结构复杂度递增生成、对照精确 ground truth。多模型评测：准确率随难度一致下降，难例暴露越来越不同的任务能力画像；测试时计算提升表现但与不同推理任务交互方式不同；程序化生成随结构复杂度平滑扩展。提供统一、可扩展的 LLM 推理探索设定。
- **关联度:** ★★★★ 「动态状态空间 + 程序化难度生成 + 精确 ground truth」——k 的评测基准设计（基准由可扩展生成而非静态集合）与 agent 状态跟踪的评测思路参考；并发/分布式系统的形式化建模与 k 的多步任务验证同构

### 3. Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search

- **ID:** [2609.19799v1](https://arxiv.org/abs/2609.19799v1) | [📄 PDF](https://arxiv.org/pdf/2609.19799v1)
- **作者:** Tal Oved, Roi Pony, Oshri Naparstek, Udi Barzelay
- **分类:** cs.CL, cs.AI, cs.LG
- **摘要:** 揭穿 LLM 驱动进化搜索的评测假象：现有论文只报单一预算设置（通常一个种子跑固定迭代数）并据此排名方法。本文在 3 个进化策略 × 5 个优化任务上跑**种子 × 迭代的全网格**：①固定预算在「更多种子（宽度）」与「更多迭代（深度）」之间的最优分配随策略/任务/总预算改变；②策略排名也随预算改变——某任务上 1 个种子时最差的策略在 40 个种子时最好；③某任务最佳迭代数远低于实践常用值，多余深度浪费预算。给出 seeds-by-iterations frontier 测量协议。
- **关联度:** ★★★★ 「单一预算点排名方法不可靠」——k 的技能/提示词 A/B 评估（进化搜索式迭代）的测量协议参考：评估要扫宽度×深度 frontier 而非单点；对 k 的批量生成/自我强化循环（skill-evolution）是评测方法论级提醒

---

## 二、LLM 安全与对齐（3 篇）

### 4. Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models

- **ID:** [2609.19472v1](https://arxiv.org/abs/2609.19472v1) | [📄 PDF](https://arxiv.org/pdf/2609.19472v1)
- **作者:** Alizishaan Khatri, Chiquita Prabhu, Omkar Neogi
- **分类:** cs.AI, cs.CL, cs.CR, cs.LG
- **摘要:** 外部 guardrail 模型对模型内部运作「失明」，且在资源受限/时间关键部署中引入延迟与算力开销。问题：模型本身是否已经知道内容有害？从 LLaMA-3.1-8B 提取激活，训练轻量 MLP 探针（**12.6M 参数**）检测有害 prompt：WildJailbreak/Beavertails/AEGIS 2.0 上 F1 分别 **99%/83%/84%**，与 1000 倍大的 guard 模型竞争持平，同时大幅降低延迟与算力成本。
- **关联度:** ★★★★★ 轻量激活探针做有害检测——k 的本地安全/内容过滤（资源受限场景）的方向参考；「外部 guardrail 看不见内部状态」提醒 k 的提示注入/有害内容防线可以叠加内部信号层，且 12.6M 参数对 k 的本地约束极友好

### 5. The Role of Fine-grained Harm Signals in LLM Safety

- **ID:** [2609.19366v1](https://arxiv.org/abs/2609.19366v1) | [📄 PDF](https://arxiv.org/pdf/2609.19366v1)
- **作者:** Soyeon Park, Seogyeong Jeong, Sunwoo Kim, Alice Oh
- **分类:** cs.CL
- **摘要:** 内部有害性表征跨风险类别变化、但共享一般有害表征成分。本文从各类别表征中**移除共享一般有害成分**得到类别残余（每层与一般有害正交），在 3 个指令微调 LLM × 11 个风险类别上用激活引导：①类别残余是否编码有害性跨类别不同，类别层面模式跨模型相似；②是否诱发拒答也跨类别不同、但模式更依赖模型；③类别残余增强模型下游与共享一般有害表征的内部对齐。结论：细粒度类别残余应被纳入 LLM 安全理解；一层与概念正交的方向也可贡献概念的下游放大。
- **关联度:** ★★★★ 细粒度安全表征 + 激活引导——k 的安全/拒答调优（alignment 方向工程）的方法论参考；「类别残余增强下游一般有害对齐」对多类别安全干预的叠加效应是设计警告

### 6. Fingerprinting Multimodal Large Language Models

- **ID:** [2609.20457v1](https://arxiv.org/abs/2609.20457v1) | [📄 PDF](https://arxiv.org/pdf/2609.20457v1)
- **作者:** Chao Huang, Meng Tong, Kejiang Chen
- **分类:** cs.CR, cs.AI
- **摘要:** 多模态 LLM 易受非法部署与未授权蒸馏侵害，现有溯源方案被 MLLM 共享语言骨干混淆、难以检测蒸馏违规。首个多模态模型指纹研究：受「自注意力是低通滤波、低频成分有信息量」启发，提出 **AttnPrint** 白盒溯源——提取跨模态注意力分布并隔离低频成分作模型指纹；同时设计黑盒变体检测蒸馏。应对共享语言骨干与跨模态注意力分布，保障模型所有权。
- **关联度:** ★★★ 模型指纹/蒸馏检测——k 的 GitHub 隐私门禁（模型/代码溯源）与本地模型部署的所有权保护参考；「共享骨干混淆溯源」对 k 的墨题/刷题机模型供应链的版权追溯有实际意义

---

## 三、可解释与干预（2 篇）

### 7. Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models

- **ID:** [2609.20722v1](https://arxiv.org/abs/2609.20722v1) | [📄 PDF](https://arxiv.org/pdf/2609.20722v1)
- **作者:** Frank E. Bobe III, Gregory D. Vetaw, Darshan W. Bryner, Matthew G. Cook, Jose L. Salas-Vernis
- **分类:** cs.AI
- **摘要:** 激活引导（activation steering）能推理时改 LLM 行为，但「在哪引导、多强引导」仍靠手工。Deep Noir 用 **Logit Lens 收敛 + 因果 head 级归因**自动发现最优引导参数：跨 3 个规模（1B×3、2-3B×2、7-9B×4），垃圾邮件任务 1B 提升 **16.7pp**（std 4.7，39 次运行），7-9B 增益增至 **21-42pp** 跨 4 架构；SST-2 情感零改代码提升 **13.1pp**。机制化 grounding 让干预点发现跨任务/跨架构泛化；RepE 不做 head masking 时在情感任务上不优于基线。
- **关联度:** ★★★ 自动引导发现——k 的模型行为干预（对齐/去毒/风格）自动化方向参考；「Logit Lens 收敛 + head 归因定位干预点」比手工挑层强，对 k 的本地模型行为调优是更省力的路径

### 8. Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading to LLM Assistants

- **ID:** [2609.20143v1](https://arxiv.org/abs/2609.20143v1) | [📄 PDF](https://arxiv.org/pdf/2609.20143v1)
- **作者:** Sebastian Maier, Kai Schwabe, Manuel Schneider, Stefan Feuerriegel
- **分类:** cs.HC, cs.AI
- **摘要:** 认知卸载到 AI 会减少技能练习机会、带来去技能化风险，但限制 AI 访问不可取。设计两种干预：①**元认知反馈**——让卸载对用户的后果显式化；②**努力奖励**——激励更少使用 LLM 辅助。预注册在线实验（N=704，2×2 设计 + 无 AI 对照，练习分数运算 + 事后无辅助测试）：元认知反馈降低答案卸载（OR=0.47）并提升测试表现（OR=1.51）；努力奖励也有效但机制不同。证明不必限制 AI 访问也能防去技能化。
- **关联度:** ★★★★ 「防止认知卸载而不限制访问」——k 的家教/学习陪伴（primary-education-tutoring、考研辅导）的核心矛盾：AI 帮手是否让学生变懒；元认知反馈（让后果显式）是可落地设计，直接进家教技能的设计原则

---

## 四、Agent 技能与记忆（2 篇）

### 9. EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data

- **ID:** [2609.19523v1](https://arxiv.org/abs/2609.19523v1) | [📄 PDF](https://arxiv.org/pdf/2609.19523v1)
- **作者:** Yinzhu Quan, Zefang Liu
- **分类:** cs.AI, cs.CL
- **摘要:** Web agent 常重访同一站点，但多数评测丢弃早期成功交互学到的流程。EconSkills：把已验证 EconWebArena 轨迹蒸馏为**参数化标准操作程序（SOP）技能库**——每条技能记录范围、导航流程、站点特定指引、验证检查、恢复步骤，源实例值替换为占位符。分离两个问题：已知相关流程能否迁移到未见任务（受控迁移中匹配技能显著提升成功率、配对成功步数更少，**抽象化远超重放原始轨迹**）；agent 能否在库规模下保留收益（库级检索整体与无技能基线竞争、直接覆盖任务最佳，覆盖分层显示未覆盖任务的近似匹配抵消增益）。识别程序化指引何时缩短门户导航、语义验证何时仍必要。
- **关联度:** ★★★★★ 技能库（SOP 抽象化 + 检索 + 覆盖分层）——与 k 的**技能体系直接同构**：skill 蒸馏（成功轨迹→参数化技能）、按需检索加载、覆盖分层评估；「抽象化远超重放原始轨迹」验证 k 写技能不存日志的做法；「近似匹配的收益抵消」对 k 的技能匹配误报是实证警告

### 10. Beyond Depth Truncation: Controlled Evaluation of Depth Utilization in Recursive Language Models

- **ID:** [2609.19934v1](https://arxiv.org/abs/2609.19934v1) | [📄 PDF](https://arxiv.org/pdf/2609.19934v1)
- **作者:** Ha Van Dau, Thanh Tung Khuat, Nguyen Thanh Dung
- **分类:** cs.AI
- **摘要:** 深度循环语言模型用小层栈迭代应用、解耦逐 token 计算与参数量。判断模型是否真利用深度时，循环与层剪枝文献共用同一评测：推理时截断深度、画质量 vs 保留深度比例曲线、读斜率。该指标有未检视缺陷：**同时改变多个模型属性**——减少 block 应用次数、降低不同计算量、把 readout head 推到分布外残差流，观测斜率混淆三者。提出受控评测分离这些因素，避免把「截断伪影」当「深度未利用」。
- **关联度:** ★★★ 「单一干预同时改多属性→观测混淆」——k 的评测设计铁律参考：改一个变量却归因错对象（与 harness 组件归因 20804 同理），k 的 A/B 验证要检查干预是否混杂

---

## 五、模型机制与综述（2 篇）

### 11. From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models

- **ID:** [2609.19553v1](https://arxiv.org/abs/2609.19553v1) | [📄 PDF](https://arxiv.org/pdf/2609.19553v1)
- **作者:** Shuo Cai, Yanggan Gu, Zihao Wang, Yuanyi Wang, Yibo Yan, Wenjun Wang, Yuhang Liu, Guanghao Zhu, Sirui Huang, Ming Li, Hongxia Yang
- **分类:** cs.CL
- **摘要:** 模型融合把源模型能力整合进单一目标模型。截至 2026-06 HuggingFace 托管超 **200 万模型**，为复用与能力整合提供丰富基础，但现有综述只覆盖零散子空间、无统一定义与系统分类。本综述定义模型融合并组织为三层：**参数级、表征级、行为级**，回顾相关指标/基准/应用，总结挑战与未来方向，附论文清单。
- **关联度:** ★★★ 模型融合全景——k 的多模型配置（模型容灾链、fallback 矩阵、多供应商）的供给侧地图；「行为级融合」与 k 的多 agent 协作/盲评设计相通；200 万模型池对 k 的本地推理选型是背景参考

### 12. Code-as-Auditor: Executable Compliance Reasoning via Regulation-to-Code

- **ID:** [2609.19199v1](https://arxiv.org/abs/2609.19199v1) | [📄 PDF](https://arxiv.org/pdf/2609.19199v1)
- **作者:** Jisoo Kim, Taeyoon Kwack, Jinwoo Jang, Woo Kyung Kim, Honguk Woo
- **分类:** cs.SE, cs.AI
- **摘要:** LLM 用于合规/法律推理日益普遍，但输出常缺法律逻辑与证据的显式 grounding。Code-as-Auditor：把法规信息转译为①形式化检查清单 + 可执行决策树（法规与条件编码为可解释代码结构），推理时②每项动态展开为事实性与反事实问题，引导模型基于个案证据与潜在违规推理。建立从证据识别到违规判定的可执行推理流水线。
- **关联度:** ★★★ 「法规→可执行代码结构 + 反事实问题展开」——k 的合规/审核类流程（GitHub 隐私门禁、服务质检门禁）的「规则可执行化」参考；反事实提问引导证据推理对 k 的审查类技能是提示工程模板

---

## 六、社会影响（1 篇）

### 13. Geopolitical Divisions Across Languages in Large Language Models

- **ID:** [2609.20005v1](https://arxiv.org/abs/2609.20005v1) | [📄 PDF](https://arxiv.org/pdf/2609.20005v1)
- **作者:** Maxim Chupilkin
- **分类:** cs.AI, cs.CL, cs.CY
- **摘要:** 人们越来越多用 AI 聊天机器人获取新闻与世界事件解释，但**用不同语言提问会得到不同的政治答案吗**？让 GPT/Claude/Gemini 用 **112 种语言**评估 20 条关于乌克兰战争的陈述，收集 **67,200 条响应**：俄倾向与乌倾向响应平衡随语言变化；按国家官方语言分组后，响应模式类似全球政治分裂——更亲俄的回答对应公众对俄观感更正面、联合国投票对乌支持更少、对乌援助更少。语言成为政治立场的隐性调制器。
- **关联度:** ★★★ 「同一模型跨语言政治漂移」——k 的中英双语内容生产（公开署名、多语言交付）的政治中立性提醒；也揭示 LLM 输出的语言层系统性偏差，对 k 的翻译/改写类交付是质量风险点

---

## 七、简评（其余值得注意）

| # | ID | 标题 | 一句话简评 |
|---|---|---|---|
| 1 | [2609.20712](https://arxiv.org/abs/2609.20712v1) | Summarization Bias: The Directional Collapse of Objective Projection into Told-Mode Labels in Large Language Models | 提出「摘要偏差」概念框架：LLM 倾向把叙事意义坍缩为抽象摘要标签而非可重建的推理结构（told-shown 轴）——叙事语义学的 LLM 行为理论，对 k 的长文档压缩/摘要技能是「丢了可重建结构」的警告 |
| 2 | [2609.20752](https://arxiv.org/abs/2609.20752v1) | Large Language Models as Falsifiers for Cyber-Physical Systems | LLM-Falsifier：把 STL 规格 falsification（鲁棒性优化）与 LLM-as-optimizer 迭代提示结合——LLM 当黑盒优化的又一实证，k 的提示即优化器工具箱参考（领域在 CPS） |
| 3 | [2609.19680](https://arxiv.org/abs/2609.19680v1) | FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA | 自进化多智能体财务 QA：把错误转成受控行为、精确定位修正作用域——「自我改进 + 修正控制」对 k 的自我强化循环（skill-evolution）的结构参考，领域在金融 |
| 4 | [2609.19721](https://arxiv.org/abs/2609.19721v1) | LearnActCoder: Role-Aware Error Memory for Adaptive Clinical Coding Agents | Learn-Then-Act 推理时自适应：小标注批次错误→结构化 MistakeKDB，假阴性教训路由到召回向 Coder、假阳性路由到精度向 Judge——角色感知错误记忆对 k 的代理分工（recall/judge 分离）有设计价值，领域在临床编码 |
| 5 | [2609.19615](https://arxiv.org/abs/2609.19615v1) | Semantic Layer Induction from Raw Telemetry via Hierarchical LLM and RAG Abstraction | 层级 LLM+RAG 从原始遥测自动构建业务语义层——端到端 RAG 抽象化框架，k 的数据语义层/知识库自动分层参考 |

---

## 今日要点（主题信号）

1. **评测方法论进入「元评测」成熟期**：19182 元研究映射 14,767 篇评测论文（质疑 LLM-as-judge 复制偏好盲点）+ 19883 PetriBench 程序化生成 ground-truth 基准 + 19799 进化搜索「单预算点排名不可靠」——评测自己的评测成为独立研究轴，k 的 verify_digest_note/服务质检门禁的方向与之一致。
2. **安全从「外部 guardrail」走向「内部信号层」**：19472 激活探针（12.6M 参数 F1 99% 平 1000 倍大模型）+ 19366 类别残余细粒度安全表征 + 20457 模型指纹——「模型自己知道有害 + 内部表征可做轻量防线」成为安全新路线，对 k 的本地资源约束极友好。
3. **技能库与记忆体系实证化**：19523 EconSkills 证明「SOP 抽象化远超重放轨迹、覆盖分层决定检索收益」——与 k 的技能蒸馏/按需加载体系直接同构，且给出覆盖分层评估方法（k 的 covered_ids/去重机制同思路）。
4. **激活引导自动化 + 深度评测去混淆**：20722 Deep Noir 自动发现引导点（跨规模 16-42pp）、19934 指出深度截断混淆多属性——「干预要能自动定位、评测要分离混杂因素」，k 的模型行为调优与 A/B 设计各取一条。
5. **认知卸载/去技能化有干预解**：20143 N=704 预注册实验证明元认知反馈降低卸载（OR=0.47）且提升学习表现——「不限制 AI 访问也能防依赖」对 k 的家教/学习产品（墨题、考研辅导）是可直接落地的设计原则。
6. **LLM 社会影响的语言层维度**：20005 跨 112 语言 67,200 响应显示政治立场随语言漂移——多语言交付的政治中立性是 k 的公开内容生产需意识到的系统性偏差。

## 验证表

| 论文 | 验证方式 | 结果 |
|---|---|---|
| LLM Benchmarks 元研究 2609.19182 | arxiv.org abs 页 + web_search 跨源（评测方法论研究群：PetriBench/进化搜索评测同题，方向一致） | ✅ 已确认（arXiv 收录 + 同题研究群互证） |
| EconSkills 2609.19523 | arxiv.org abs 页 + web_search 跨源（WebArena/EconWebArena 同族研究群印证 web agent 技能库方向） | ✅ 已确认（arXiv 收录 + 同族研究群互证） |
| Safety Beyond Interface 2609.19472 | arxiv.org abs 页 + web_search 跨源（activation probe/guardrail 研究群：WildJailbreak/Beavertails 数据集真实存在，方向印证） | ✅ 已确认（arXiv 收录 + 数据集/研究群互证） |
| 其余 11 篇 | arxiv.org HTML 收录 + 逐页抓完整元数据 | ✅ 已确认（HTML 收录即存在性证据 + 全文摘要；跨源 web 验证非必需） |

## 可落地行动项

- 🔴 **评测元视角进质检门禁**：19182「LLM 参与构造测试/评判回答时可能复制模型偏好盲点」——k 的 verify_digest_note/服务质检（service-quality）加「谁构造测试、谁打分」的自检；Gemini 跨源盲评的独立性是有意为之，保持并文档化
- 🔴 **技能库覆盖分层评估**：19523「抽象化远超重放原始轨迹 + 近似匹配抵消收益」——k 的 skill 蒸馏按「参数化抽象」而非存日志；技能检索匹配加覆盖分层（直接覆盖/近似/未覆盖）标记，近似匹配的收益抵消进 ai-freelance-pricing/接单技能匹配决策
- 🟡 **内部信号层安全探索**：19472「12.6M 参数激活探针平 1000 倍大模型」——k 的本地安全过滤（成本受限场景）评估加激活探针方案；19366「类别残余增强下游一般有害对齐」提醒多类别安全干预要查叠加效应
- 🟡 **进化搜索式迭代的评测协议**：19799「seeds×iterations frontier 而非单预算点」——k 对提示词/技能指令做批量迭代优化时，评估扫宽度×深度网格，不单点排名
- 🟡 **去技能化干预进学习产品**：20143「元认知反馈降低卸载 OR=0.47 且提升表现」——墨题/家教辅导加「让卸载后果显式」的反馈设计，不强制限制 AI
- 🟢 **待深读**：19182（评测元研究）、19523（EconSkills 技能库）、19472（激活探针安全）、19799（进化搜索评测）→ core-contributions 候选

---

*本速览由 cron 自动生成（补全性质）：2026-09-19 无新日期分组（周六，最新仍 09-18）→ 09-18 同池 602 篇与 covered_ids（740）比对 → 标题粗筛 53 候选 → 人工剔除领域应用 → 逐篇抓 abs 页精选（13 主条目 + 5 简评），与昨日零重复。关键论文跨源 web 验证（LLM Benchmarks 元研究 / EconSkills / Safety Beyond Interface）。元数据以 arxiv.org abs 页为准。数据源 arxiv.org。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

---
状态：reading
