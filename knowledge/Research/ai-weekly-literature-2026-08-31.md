# AI 文献周报 · 2026-08-24 ~ 2026-08-30

> 方向：AI Agent / 大模型(LLM) / 科研工具(AI for Science)
> 检索源：arXiv(3组query: agent/llm/research_tools，08-24→08-30 窗口) + OpenAlex(25) + Crossref(40)
> 覆盖度：✅ arXiv HTTP 200 / ✅ OpenAlex HTTP 200 / ✅ Crossref HTTP 200 实测；**arXiv 索引冻结于 08-28T17:59Z**（08-29/08-30 无新提交可查）；未覆盖：CNKI/万方/维普（无免费 API）
> 注：与 08-31 daily 速览（08-20→08-28 补全，28 主+16 简评）同池。本报告精选速览强相关 8 篇 + 独立多源查询补录 7 篇速览漏网强相关（标注"新"）。所有标题/数据来自真实 API 响应，未臆造；被引未采信搜索引擎页面

---

## 一、本周值得关注论文（按方向）

### 🔧 AI Agent（技能系统 / RL 训练 / 多智能体 / Harness）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **WikiSkill** (2608.27454, Google) | 技能演化需要"持久 wiki"层沉淀知识：三层架构（原始轨迹/wiki/可执行技能），wiki 永不回滚；5 基准×5 模型一致优于 Trace2Skill/SkillOpt；wiki 消融 +15.0pp；小模型+演化技能可反超更大无技能模型；技能跨模型族可迁移 | 把优化历史里散落的洞见编译成可寻址的持久知识层（Karpathy LLM Wiki 观落地），增益归因于"持久记忆基质"而非更好的改写提示 |
| **The Collaboration Tax** (2608.22152) | 两 agent 必须协作时性能损失（协作税）可形式化为团队去中心化损失：32 任务×11 模型沿"类别排序/能力单调"两条无例外轴结构化；根因是四阶段对话级联（无依据断言/不追问/不整合/不重推导） | 把协作代价变成可测成本；提示词干预可关闭部分差距；异质配对税被拉向强伙伴而非中点 |
| **MCP-Universe RL** (2608.22167, Salesforce 开源) | 用 MCP 做统一环境接口训练工具 agent：任何 MCP server 零集成接入 RL；三阶段 rollout 流水线解耦后吞吐×2.8；同一配置训出软件工程/深度研究/通用工具三 agent | 一次性环境编排层+rollout 编排层（acquire→run→evaluate 分阶段并发掩盖工具等待）；训练后端无关（veRL/slime） |
| **ContextPilot** (2608.28476, 新) | 长程 agent 上下文管理：扩展工具集（规划/长记忆/软卸载）+ 按"上下文/熵变化"识别高影响编辑动作的细粒度 RL | 把"主动上下文管理"当 RL 优化目标，解决旧法缺全局规划、探索不均、粗粒度信用分配三局限 |
| **SAPO** (2608.19842) | 策略与价值共享单自回归骨干 + λ-returns 轨迹级 GAE：比 PPO/GRPO 平均 +15.1/+12.1pp，省独立 critic 显存、单次迭代时间 -33.2% | 单 rollout 的省钱 Agent RL，对 8GB 本地 GPU 的微调路线友好 |
| **SymTrace: Repair or Resample** (2608.25920) | 多智能体失败调试：无引导重跑失败复现率仅 67.97%、修复率仅 6.90%；症状驱动干预修复 20.15%（比 SOTA +191.89%） | 受控重放框架（干预锚点+日志重建锚点前执行）+ SymFail 536 条人工标注失败轨迹 |

### 🧠 大模型（评测 / 检索 / 推理）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **Think-Probe-Respond** (2608.25660, 新) | LLM 判研究想法新颖性有系统性"中等新颖"偏见：理由看似像人、最终判断偏中（最强模型宏F1 仅 ~17）；从推理期隐藏态探针提取判断条件化最终回答，新颖性判断 +22.30% | 隐藏态探针矫正 judge 偏差（轻量逻辑回归），给"LLM 当新颖性裁判"一条可落地校准路径 |
| **AgentJudgeBench** (2608.26623) | LLM judge 在 agentic 工具调用评测有结构性上限：对齐随难度单调退化、无 ground truth 时六 judge 全收敛 77-82% 窄带；暴露 ground truth 未必有益（过度锚定）；CoT/温度无效、rubric 最高 +6.5pp | 首个系统研究 agentic DAG 工作流上 LLM-as-judge 可靠性的基准（3808 实例/6 拓扑/3 难度档） |
| **MetaRAG** (2608.24214) | agentic RAG 搜索决策对齐"内部信念"：先显式验证、信念探针估计可答性，一致性奖励+正确性门控避免强化"内部一致但错"轨迹；7 基准一致改善精度-效率权衡、推理零开销 | 信念-动作对齐的 RL 奖励，增益迁移到深度研究/不同优化器/多骨干 |
| **Don't Overthink, Don't Underthink** (2608.26442) | agentic 场景推理需求动态演化：over-reasoning 关联更高成本无比例精度增益、under-reasoning 关联错误/不完整解（MATH-500/GAIA 实测） | 把 over/under-reasoning 刻画为"推理错配"复发失败模式，提示按任务动态分配推理量 |

### 🧪 科研工具（AI for Science / 评测 / 执行引擎）

| 论文 | 核心发现 | 创新点 |
|---|---|---|
| **Accelerating Scientific Research with Gemini** (2608.26701, Google, 新) | Co-Scientist 从"in silico 假设生成"升级为执行落地研究伙伴：CVD 反应器设计 MXene 安全前驱体路线并实机长出类 MXene 层状 2D 材料；Gemini 3 Deep Think 几分钟调配方、单次尝试长成单层 MoS₂/MoSe₂/WS₂；全自主设计推理期缩放架构 Agent_H 超 6 个前沿模型（HealthBench）；双盲评审（30 专家/450 评）下可靠性模块把关键结果捏造率 46%→4% | 人-AI 协作按领域物理约束自适应 + 日志基验证/安全机制，实证回答"AI 科研 agent 离真实闭环还差什么" |
| **HypoForge** (2608.25770, 新) | 假设生成与测试两阶段监督信号不同：生成（无显式反馈）用对抗生成-判别器迭代精炼、测试（有 ground-truth）从执行结果学测试技能；不微调基座即持续改进，超现有 AI scientist 框架 | 按阶段匹配技能学习策略——"经验→可复用技能"的通用自改进范式 |
| **EarthVerse** (2608.23525, 新) | 地学科学 agent 基准（405 可复现任务/199 事件/19 灾害族）：最优均值答案准确率 84.65% 但 Strict@95 仅 34.81%——"能算对但难严格达标"；受控研究定位失败于证据获取/工具选择/记忆/推理/执行 | 包作用域调查 + 可执行 ground truth 细粒度答案单元 + 过程评分 rubric（允许多路径） |
| **FrontierChallenge** (2608.24979, 新) | 300 端到端科学工作流基准（发布 97 任务/6 域）：最强配置仅完成 20/97（Pass Rate 20.6%）；分析化学/电化学部分进度高（Avg 87.6/94.9）但完整交付仅 4%/0%；Claude Code 失败轨迹 75.5% 仍以"声称完成"结尾 | 跨域"完整交付"判据，暴露"部分进度→完整交付"鸿沟 + 语言声称 vs 实际完成的可靠性问题 |
| **Fidelity Is Not Enough** (2608.28439, 新) | agentic 文档抽取里保真度标准会漏静默失败（结构化输出约束禁用工具仍答题且文本是编的）；每工具调用级痕迹 + 两条规则检测器：207 条干净抽取零误报、50 个植入故障全召回 | dispatch 级 instrumentation + "只看工具调用不看抽取值"的静默失败检测 |

---

## 二、推荐精读（3 篇）

1. **WikiSkill** (2608.27454) — **本周"技能系统"主线最强机制论文**，也是 sora skill-evolution / 知识库设计最该借鉴的一篇。三层架构（原始轨迹/wiki/技能）可直接映射到 Hermes 的 memory/skills；"wiki 永不回滚 + 技能门控回滚"= 失败也沉淀为知识的持久化机制，正对症 knowledge-absorption 的"经验→可复用技能"痛点（消融 +15.0pp 证明持久知识才是增益来源）。
2. **The Collaboration Tax** (2608.22152) — **把多 agent 协作代价形式化**。四阶段级联归因（无依据断言/不追问/不整合/不重推导）可直接对照 sora 的 WorkBuddy/dsh/Gemini 联合工作流：先独立产出再定向评审、避免全量互读。配 **SymTrace**（失败归因：只让"肇事 agent"反思）一起读，多 agent 排障闭环完整。
3. **Accelerating Scientific Research with Gemini** (2608.26701) — **AI 科研 agent 走向真实实验闭环的最强实证**：CVD 实机、单次生长单层材料、全自主发现超前沿模型的架构、双盲防幻觉数字（4% vs 46% vs 90%）——既回答"科研工具离落地差什么"，也给出"可靠性模块"（日志验证+惩罚捏造）的工程样板。
   - 备选：**Think-Probe-Respond** (2608.25660) — 直接给 light-idea-critique 的 LLM judge 环节提效：隐藏态探针矫正"中等新颖"偏见（+22.30%）；配读 RQ-Bench（2606.12071）"LLM 与人类专家新颖性判断仅 22% 一致"会更清醒。

---

## 三、本周趋势总结

1. **技能 = 智能体最便宜的成长杠杆（本周最高密度主线）**：WikiSkill（wiki 持久记忆）、SPT（技能当训练数据）、SkillForge（技能验证而非只追加）、BASM（技能边界防误用）、ContextPilot（上下文管理技能化）、HypoForge（技能学习）——"经验→可复用技能→持续改进"成了跨任务的统一解法；同时攻击面同步转移（SkillBloat token 放大 / MaliciousSkillBench 恶意技能检出跨源泛化仅 0.65-0.67）。
2. **多智能体协作被"计税"与成本工程**：Collaboration Tax 形式化协作损失 + 四阶段级联归因；ProgRouter 按进度路由、Routed Graph Handoff 省 40-60% token、COVER 路由评估合约；SymTrace/DoCtOR 把失败归因到"肇事 agent"——协作讨论从"能不能"转向"多贵、谁错了、怎么修"。
3. **Harness 工程成为独立可靠性学科**：The Empire（dsh/pi/deepagents 收敛五要素、全员缺"外部可验证性"）、Logos（跨进程总线）、EvoUndo（自演化可恢复性）、LoopArena（loop 控制器评测）——harness 从外围胶水变一等人研究对象，可验证性被预判为溯源敏感域下一个分化轴。
4. **AI 科研 agent 从 demo 走向真实世界闭环**：Gemini Co-Scientist 实机执行（CVD/单层材料/表型预测/HealthBench 架构）、HypoForge（假设技能化）、EarthVerse/FrontierChallenge（端到端交付基准）、Fidelity Is Not Enough（静默失败 instrumentation）——"能不能跑通"已不是问题，"证据可信、交付完整、可验证"才是。
5. **Agent RL 工程化降本 + 监督信号变细**：MCP-Universe RL（MCP 统一环境）、SAPO（单 rollout 省显存）、EDGE（经验蒸馏进权重）、VICT（verifier 内部分子做信用追踪）——训练 agent 更便宜、信用分配更细。
6. **评测与安全双轨下沉到过程/循环级**：AgentJudgeBench（judge 天花板）、Think-Probe-Respond（judge 偏差矫正）、AI4AI-Bench（RSI 只闭合 1/5）、LoopHarness（跨迭代非衰减安全状态）、ClawSentry（四层安全网关）——"测什么/怎么防"都在从单点最终分数下沉到过程、循环、生命周期。

---

## 数据说明

- **检索源与 HTTP 码**：arXiv 3 查询（agent/llm/research_tools，08-24→08-30 窗口）=200；OpenAlex=200（25 条）；Crossref=200（40 条），全部真实 HTTP 200
- **覆盖度**：✅ arXiv / ✅ OpenAlex / ✅ Crossref；**arXiv 索引冻结于 08-28T17:59Z**——08-29/08-30 无新提交（08-31 速览已核该窗口为空）；未覆盖 CNKI/万方/维普（无免费 API），不假装查全
- **同池去重**：与 08-31 daily 速览（08-20→08-28 补全速览）同池；本报告精选其强相关 8 篇 + 补录 7 篇独立多源查询检出的漏网强相关（标注"新"）
- **验证**：4 篇精读候选 + 关键新论文经 web_search 交叉验证（arxiv abs/html / alphaXiv / DAIR.AI 等）✅；其余 arXiv API 收录即存在性证据；未臆造 DOI/被引/年份
- **原始数据**：`C:\Users\31954\.openclaw\workspace\.temp\week_last.json`（可复现证据，用完清理）

---

*生成：Hermes cron · light-literature-search 方法论（多源回退）· 2026-08-31*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
