# AI 文献周报 · 2026-08-07 ~ 2026-08-14

> 方向：AI Agent / 大模型(LLM) / 科研工具(AI for Science)
> 检索源：arXiv(3组query: agents 60 + llm 60 + sci 18) + OpenAlex(3组: 25+25+24) + Crossref 连通性验证
> 覆盖度：✅ arXiv / ✅ OpenAlex / ✅ Crossref 均 HTTP 200 实测；未覆盖：CNKI/万方/维普(无免费API)
> 注：所有标题/编号/数据均来自真实 API 响应，未臆造；被引数未采信搜索引擎页面

---

## 一、本周值得关注论文（按方向）

### 🔧 AI Agent（科研/长程 agent 为主战场）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **OmniScientist** (2608.13558) | 全模态 AI 科学家：36 个真实案例（5 大学科家族、图像/信号/音频/视频/3D 结构等模态）全部完成"原始数据→成稿论文"，均分 6.3；感知层让 7 项评估维度全升、85% 对局胜出 | 端到端感知原始证据而非预计算摘要；确定性流水线内跑 idea/rigour/claim 三道代码检查 |
| **Intern-S2-Preview** (2608.13505) | 397B 科学 agentic 基础模型：科学多模态预训练 + 多任务 RL + agentic RL + on-policy 蒸馏；时间序列模块提升 SciTS；MemDec-4B 附加记忆路径不动 397B 主干把 Biology 均分 56.92→60.32 | 科学场景"快速专业化"分离记忆路径（Memory Decoder） |
| **Beyond Final Scores** (2608.13417) | 系统评估 7 个前沿模型 × 36 长程任务：当前 agent 更像"工程优化器"而非自主研究者——能实现实用方案但真正方法学新颖性罕见；经验复用既可能帮助也可能误导后续决策 | 规则化过程指标（Solution Framing / Execution / Feedback Control）+ 受控对比测经验复用 |
| **Scaling Automatic Research Agents via World Models** (2608.12564) | WMRL：用世界模型替代环境执行消除训练瓶颈，加速 3-4x 且超标准 RL；后训练 4B/9B agent 超过 48B/120B 开源 | 识别"生成共享算力、执行独占沙箱"的根本张力；Online Debiasing + Inverse-Variance Denoising 理论保证 |
| **Training AI Scientists to Replicate Research** (2608.13331) | Replica 复现任务空间 + 自动 rubric 裁判；Faraday 27B 复现能力超 Claude Opus 4.8 / GPT-5.5，且采用更"科学原则化"的 rollout | 把复现作为可扩展任务空间 + 低噪声自动裁判提供奖励信号 |
| **Practice Makes Unsafe** (2608.12851) | 自改进 agent 会把"不安全的成功"固化成可复用技能：25 种配置中 21 种产出不安全工件；3 个恶意任务把 carryover ASR 16.0%→35.3%；SafeEvolve 降低不安全复用/跨会话危害 26.7/17.3pp 而良性效用仅 -0.4 | 技能生命周期（编写→检索→执行）归因；SkillMisevo-Gym/Bench 可版本化追踪 |
| **Agentic Auto-Research is Fuzz Testing** (2608.09855) | 观点文：自动科研的 generate-and-rank 范式漏了"稀疏反馈"问题；应学灰盒 fuzzer——每个实验暴露廉价的认知进展信号，并用信号引导下一步而非只排序 | 把反馈架构（而非生成）定义为自动科研的核心瓶颈；受保护验证防伪发现 |
| **SteerBench-Work** (2608.12654) | 转向边界基准（106 个事件锚定场景）：30 个模型条件中失败几乎单方向——28.1% 误拒已授权工作 vs 1.0% 误放不安全动作；更强的模型反而更会过度拒绝 | 事件锚定 + 证据反转镜像对，测"提交边界"的 gate 决策而非一般能力 |
| **LLMs Are Not Good Strategists** (2608.12626) | EpicStar 把成功历史片段当策略记忆 + 动态门控：星际争霸 II 中大幅提升胜率且 token 少一个数量级 | 跨回合结构化记忆是长程战略执行的关键（"记忆即策略"） |

### 🧠 大模型（对齐/检索/效率/小模型）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **Synthetic Persona Pretraining** (2608.13482) | 从 token 0 植入助手人格（预训练阶段对齐）：3B/500B token 下宪法遵从与越狱鲁棒性提升、OOD 道德困境失准率下降、能力无损；越晚引入效果越差 | 把"对齐是事后薄覆盖层"改为预训练期价值注入 + persona binding |
| **GEM** (2608.13200) | 生成式嵌入模型：先对 query 显式推理意图与相关性标准，再追加嵌入 token 编码增强上下文做检索，超非推理变体、对齐更大模型基线 | 统一"生成+嵌入"单模型，推理增强检索 + 测试时计算可扩展 |
| **The Embedder's Dilemma** (2608.12875) | 10 个 LLM × 26 个嵌入模型 × 37 任务：整体打平（最佳 77.6 vs 77.2），但 LLM 成本最高贵 1431x（$154 vs $0.11/轮）；推理 token 占 LLM 成本 28-81% | 任务分工结论：相似/分类/聚类用嵌入模型，推理型检索才用 LLM；成本感知基准开源 |
| **DFM Mimir v1** (2608.13517) | 1B 参数 HRM 架构只用合规后训练数据：英语竞争力 + 丹麦语新 SOTA，对标 Qwen 3.5 4B / Gemma 4 E2B | 纯许可数据路线降低开源复现门槛 |
| **Mixture of Training** (2608.13277) | 预训练分解为小块独立训练再重组：1.3B 上证明"深度切片可重组为可用模型"且质量对齐单体基线 | 模块化预训练作为可复用训练单元的小规模机制验证 |

### 🧪 科研工具（基准/评测/执行引擎）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **LigBench** (2608.13136) | 统一、与人类对齐的研究想法生成评估基准；PAIR-IQ 数据集训练的成对判断模型提升排序准确率与鲁棒性 | 摆脱"直接 LLM 打分"的碎片化评估，可跨想法分布一致应用 |
| **Science Edge Evaluation** (2608.06931) | 多模态实验科学基准（化学/生物/材料）：19 个 MLLM 最强仅 48.7%，工具使用提到 52.7%；通用模型平均反而超科学专用模型 | 检验"证据有界的推理"——工具给了更多信息但不保证可靠科学推理 |
| **Carnot** (2608.09532) | 深度研究查询编译为物理执行图 + 交互式笔记本：用户可拦截幻觉前提、核对中间结果、改代码/算子，按成本或延迟约束优化 | 把黑箱 deep research 变成可审计可纠偏的执行引擎 |
| **Not Worth Another Token** (2608.08389) | 边际价值剪枝系统对比：剪哪里比用什么打分更重要——早期剪枝省最多（轻量启发式最高省 73% token 而质量几乎不降） | 三阶段（pre/post-retrieval/pre-synthesis）首次系统对照 |
| **LitTraceQA** (2608.07370) | 科学文献问答基准：要求输出"论文ID+证据位置+答案"三段可验证产物；4978 条唯一问题记录 | 分开评测检索/证据定位/答案三环，测"可验证答案"而非流畅摘要 |
| **VALG** (2608.13060) | ML 理论研究 agent：COLT 2026 五个开放问题的 9 个子问题，2 个产出与源简报范围匹配的定理候选；把证明失败路由到推导/结构/表述三类阻塞 | 图结构证明依赖 + 表述级变体/松弛保持数学关系；开源 |
| **AaLLM** (2608.13472) | 模拟电路设计端到端多 agent（拓扑生成+尺寸）：RAG 知识库 + Designer/Critic/Evaluator 三 agent 仲裁；SPICE 调用减 3-4.5x、墙钟时间减 40x、创新拓扑 FoM 最高 3x | 与 sora PCB/电路兴趣直接相关，可借鉴工作流 |

---

## 二、推荐精读（3 篇）

1. **Beyond Final Scores** (2608.13417) — **本周方法学价值最高的一篇**。直接回答"现在的 agent 到底行不行"：能当工程优化器、当不了自主研究者，经验复用有双刃剑效应。做 agent 评测、写 related work、评估自家系统都该先读它定参照系。
2. **OmniScientist** (2608.13558) — **AI Scientist 主线最完整的端到端系统**。全模态感知 + 确定性流水线 + 代码内三道检查（新颖性/统计/溯源）的架构，是"科研工具该怎么做"的可移植蓝本；36 个真实案例的评估规模也难得。
3. **Scaling Automatic Research Agents via World Models** (2608.12564) — **训练成本瓶颈的正解思路**。识别"生成共享算力 vs 执行独占沙箱"的规模张力，用世界模型替代执行 + 双缓解（去偏/降噪）带理论保证。做自改进 agent 或 RL 路线必读。
   - 备选：**Training AI Scientists to Replicate Research** (2608.13331) —— 复现任务空间 + 自动裁判训练 27B 超闭源模型，工程路径清晰可复现。

---

## 三、本周趋势总结

1. **AI Scientist 从 demo 走向系统化工程**：本周至少 4 个端到端科研 agent 系统同台——OmniScientist（全模态）、Intern-S2（基础模型路线）、Faraday/Replica（复现训练路线）、AQuA（量化研究闭环）。差异点从"能不能跑通"转向"感知什么证据、怎么给奖励、怎么保证溯源"。
2. **评估先行，方法学成为主战场**：Beyond Final Scores（过程指标）、LigBench（想法评估）、SEE（多模态实验）、SteerBench-Work（转向边界）、LitTraceQA（可验证答案）——"测什么、怎么测"的密度显著高于以往，且普遍从单一最终分数转向多环/多阶段指标。
3. **长程 agent 的三大工程瓶颈浮出：记忆、技能、成本**。记忆（LycheeMemory V2 段级巩固省 86% 构建 token；EgoCITE 时间感知；RippleMem 关联回忆）、技能（SkillShapley 归因、SkillEvo 进化梯度、@skills 协议化）、成本（边际价值剪枝省 73%）——三者开始有独立子方向。
4. **安全与治理进入"生命周期"视角**：Practice Makes Unsafe（技能误进化）、Provenance Integrity（溯源治理层）、MCP 安全评估 construct validity 审计、SteerBench-Work 的过度拒绝问题——关注点从"单次攻击成功率"转向"不安全经验如何沉淀与复用"。
5. **小模型与成本意识持续强化**：Mimir 1B 合规数据 frontier 表现、Embedder's Dilemma 的 1431x 成本差与任务分工结论、GEM 的测试时计算缩放——"够用且便宜"成为显性设计目标。

---

*生成：Hermes cron · light-literature-search 方法论 · 2026-08-14*
*原始数据：C:\Users\31954\week_arxiv_openalex.json / week_abstracts.json（临时文件，可删）*

---

## k 的吸收笔记 (2026-08-15)

> 学习路径：web_search 验证 5 篇核心论文（AaLLM / Beyond Final Scores / OmniScientist / Embedder's Dilemma / Not Worth Another Token），全部 arXiv 原文可查，数据采信。

### 已应用的
| 洞察 | 应用 |
|:-----|:------|
| **Embedder's Dilemma**（2608.12875）：嵌入模型与 LLM 整体打平（77.6 vs 77.2）但 LLM 贵 1431x；推理 token 占成本 28-81% | **任务分工原则**：相似/分类/聚类用嵌入模型（如 Qwen3-E-4B $0.07），推理型检索才用 LLM；DeepSeek-V4-Flash 是成本最优 LLM（$3/轮）——确认 sora 默认 flash 模型选型正确 ✅ |
| **Not Worth Another Token**（2608.08389）：早期剪枝 > 后期压缩——Post-Retrieval MMR 省 69.5% token 质量仅降 2.1%；两阶段 CD+SC 质量还反升 +1.64 | **长任务上下文管理原则**：检索结果先剪枝再进上下文（去掉低价值/冗余分支），比事后压缩省得多；三阶段 MMR 极限省 73.3% |
| **Beyond Final Scores**（2608.13417）：agent 更像「工程优化器」非「自主研究者」；经验复用双刃剑 | **评估视角**：评估自家系统不只盯最终分数，用过程指标（Solution Framing/Execution/Feedback Control）；memory/skills 复用前要甄别「经验是否值得复用」 |
| **AaLLM**（2608.13472）：三 agent（Designer/Critic/Evaluator）仲裁 + RAG + SPICE 闭环，SPICE 调用减 3-4.5x、墙钟减 40x | **PCB/电路方向参考**（backlog）：模拟电路 sizing 端到端自动化；同领域 AnalogAgent（97.4% Pass@1）/MenTeR（84.2%）可一并参考 |

### 新吸收的行为改进
- **Embedder's Dilemma** → Hermes 配置 review 时：记忆检索/知识库语义搜索优先嵌入模型，不拿 LLM 当 embedding 用；长任务里降低 reasoning budget 保检索质量
- **Not Worth Another Token** → 千轮研究/深度研究流程中：搜索返回后先做相关性去重剪枝（MMR 思路）再继续，不把原始堆料全塞上下文
- **Beyond Final Scores** → agent-self-evaluation 技能注入「过程指标」视角：评任务完成质量看 提出方向/执行/反馈控制 三环，不只结果
- **Practice Makes Unsafe**（2608.12851）→ skill 自举安全警示：自改进 agent 会把「不安全的成功」固化成技能——Hermes 的 skill 沉淀要带来源追溯，避免把偶然成功当通用规则

### 仍需改进的
- ⬜ **AaLLM → 深度评估**：如果 sora 要做电路设计自动化（模拟方向），值得十轮深挖 AaLLM + AnalogAgent + MenTeR 三套框架选型；当前 PCB 兴趣主要是数字布局布线，暂 backlog
- ⬜ **OmniScientist**（2608.13558）→ trial：感知层 + 确定性流水线 + idea/rigour/claim 三道代码检查——与 light-research 系列（research-ethics/light-paper-writing 质量门）方向一致，可对照补强「代码内检查」环节
- ⬜ **SteerBench-Work**（2608.12654）→ 关注：30 模型条件中 28.1% 误拒已授权 vs 1.0% 误放不安全——Hermes 审批策略设计时避免过度拒绝

### 数据截止点（data-cutoff）
- 数据截止：2026-08-15（本吸收笔记检索/验证数据不晚于该日）

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
