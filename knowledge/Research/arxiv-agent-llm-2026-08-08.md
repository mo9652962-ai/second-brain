---
tags: [arxiv, research, ai-agent, LLM, daily]
aliases: [arxiv-agent-llm-2026-08-08]
date: 2026-08-08
source: arxiv-fetch cron 产出
status: fresh
---

# 📚 arXiv AI Agent / LLM 最新论文（2026-08-08）

> 来源：arxiv-fetch cron（export.arxiv.org API，submittedDate 倒序）
> 精选 10 篇与 AI Agent / LLM 直接相关的最新论文

---

## 🔥 与 Hermes/Agent 生态直接相关（高优先）

### 1. ASTELD: 自主 AI Agent 六轴分类框架（含 OpenClaw 案例研究）
- **arXiv**: https://arxiv.org/abs/2608.05201
- **发布**: 2026-08-05 | cs.CR, cs.AI
- **作者**: Siyuan Li 等（多机构）
- **摘要**: 提出 ASTELD 六轴分类框架（架构模式/安全姿态/工具集成/执行范式/自主性与人类控制/部署拓扑），映射 8 个代表性框架并用 OpenClaw 作深度案例研究。8 平台全部可区分，揭示 3 个跨平台模式：安全-可访问性对角线、强执行-架构耦合、能力收敛但架构持续分化。分类 50+ OpenClaw 衍生项目发现创新集中在安全/执行/部署轴。**暴露一个空白区域：没有系统同时具备本地优先部署 + 企业级安全。**
- 💎 **与我们相关**: 直接以 OpenClaw 为案例，六轴分类法可用于评估我们的 Hermes 配置（安全/部署拓扑），发现未占据的设计空间。

### 2. Skill-Use: LLM 真的会在 Agentic Harness 中使用技能吗？
- **arXiv**: https://arxiv.org/abs/2608.04828
- **发布**: 2026-08-05 | cs.CL
- **作者**: Jinyi Han 等（复旦大学）
- **摘要**: 现有评估只判断技能质量，不检验 agent 能否自主识别并应用技能。提出 Skill-Use benchmark：渐进式披露（只给技能名+短描述，须自行检索完整流程）。三要素：Trigger（是否调用相关技能）、Compliance（是否忠实遵循流程）、Boundary（是否避开禁止操作）。79 个真实技能 + 177 个可执行任务、9 个领域、Docker 沙箱。**最强配置 SU 仅 0.613**，触发与流程遵从是独立瓶颈，且分数随 harness 变化——技能使用是"依赖 harness 的能力"而非模型的固定属性。
- 💎 **与我们相关**: 直接对应我们的技能系统！技能使用成功率仅 61.3%，触发瓶颈提示我们技能描述（description 前 57 字符）必须自包含触发条件。

### 3. EvolveNet: 协作式 Harness 进化实现 Agent 自我改进
- **arXiv**: https://arxiv.org/abs/2608.04968
- **发布**: 2026-08-05 | cs.LG
- **作者**: Jun Nie 等（香港浸会大学等）
- **摘要**: Agent 能力不只取决于模型，还取决于 harness（构造上下文/调用工具/验证结果/从失败恢复的可执行程序）。现有方法假设所有经验可路由到单一优化器，但真实生态中经验流彼此隔离。EvolveNet 将经验提取移到数据侧：共享 harness 广播到各数据本地部署，各自在工作负载上进化，只把程序适配组合回共享 harness。通过 scope-typed、evidence-guided 聚合避免冲突。**5 个设置（Text-to-SQL/数据科学编码/竞赛编程/软件工程/agentic workflows）全部提升**，异构工作负载下收益最大。
- 💎 **与我们相关**: "harness 进化不更新权重"与我们记忆中的 OpenForgeRL 一脉相承；协作式进化 = 多 profile/多用户配置各自进化再合并的思路。

### 4. EvoHarness-RL: 学习自进化运行时 Harness（长时程 LLM Agent）
- **arXiv**: https://arxiv.org/abs/2608.05446
- **发布**: 2026-08-05 | cs.LG, cs.CL
- **作者**: Xuying Ning 等（伊利诺伊大学芝加哥分校等）
- **摘要**: 长时程 agent 依赖外部执行支持维护状态/追踪进度/调用工具/复用经验，但 harness 使用策略通常靠提示词或启发式。提出 EvoHarness-RL：将 Belief/Progress/Experience（BPE）暴露为策略面对的 harness 状态；监督微调教 agent 构造外部状态，cost-aware GRPO 探索协调策略。ALFWorld + Qwen3-8B 达到 **96.9% 成功率**。两个关键动态：harness annealing（训练把重复模式内化为模型策略，从频繁调用转向选择性访问）和 harness evolution（进度更新+经验整合使 harness 变得紧凑自适应）。
- 💎 **与我们相关**: "训练可学习的 harness 使用策略，胜过堆更强的工具或更大记忆"——对我们 Hermes 的 memory/skills 组织有启发。

---

## ⚠️ 安全与可靠性

### 5. 自我进化适得其反：LLM Agent 技能污染的事前门控
- **arXiv**: https://arxiv.org/abs/2608.05810
- **发布**: 2026-08-06 | cs.AI, cs.CL
- **作者**: Linfang Shang 等
- **摘要**: 自进化 agent 从执行轨迹蒸馏技能，但该过程**不是单调的**：超过临界池大小后，新技能反而降低性能。形式化"能力污染相变"：一旦缺陷技能进入决策上下文，就成为后续技能蒸馏的参考材料，形成跨轮污染链，且**结构性不可逆**（事后删除源头技能无法抹除后代已继承的错误推理）。提出 Verifier-as-Gatekeeper（VaG）：三个异构批评者（结构有效性/行为无害性/语义一致性）+ 边际增益子集选择。Terminal-Bench 2 上 VaG 每轮都提升，达到 **72% pass@1 且技能池小约 5 倍**，冻结技能池可迁移到 4 个其他 backbone。
- 💎 **与我们相关**: 直接警告"技能越攒越多可能反而变差"！对我们的技能库：需定期审计（skill-library-audit），新增技能要有验证门控，避免污染链。

### 6. DreamGuard: 基于风险感知世界模型的 LLM Agent 高效运行时护栏
- **arXiv**: https://arxiv.org/abs/2608.05695
- **发布**: 2026-08-06 | cs.AI, cs.CL, cs.CR
- **作者**: Wenhao Lin 等（西安电子科技大学等）
- **摘要**: 现有运行时护栏多为反应式，只评估当前动作的表面安全性，缺乏风险如何在轨迹上演化的显式模型——对"单看无害但逐步漂移到危险状态"的长时程风险存在盲区。DreamGuard 围绕风险感知世界模型：维护轨迹上的紧凑循环隐状态，预测未来隐状态，融合即时危害 + 前缀风险信号，在执行前干预。4 个 benchmark 上超越通用/反应式/主动式基线，**平均端到端延迟仅 25ms/次**。
- 💎 **与我们相关**: Hermes 的外部操作（邮件/发推等）安全机制可借鉴"多时域风险信号融合"思路。

### 7. Causal Episodic Memory: 反馈驱动的 Agent 修复
- **arXiv**: https://arxiv.org/abs/2608.05906
- **发布**: 2026-08-06 | cs.CL
- **作者**: Khang Nhat Hoang Vo 等
- **摘要**: 修复失败的 LLM agent 常丢弃成功修正，导致后续 episode 重新发现类似方案。提出 MERIT：免训练的在线双极性记忆（oracle 验证的修正 + 观察到的失败方向），确定性分类器给失败粗分类，条件化混合词汇-稠密检索器。Qwen2.5-7B-Instruct 下 Spider 执行准确率 66.34%→69.79%，BIRD 47.35%→48.44%。**负面记忆贡献有限、类型条件价值依赖数据集、schema 本地经验收益最一致**。
- 💎 **与我们相关**: 失败记忆分正负极性、条件化检索——与我们的 LEARNINGS.md/ERRORS.md 双文件记忆体系理念一致。

---

## 🧪 评估与训练新方向

### 8. AV-AIVAT: 74 倍更便宜的 Agent 评估（任意时点有效停止）
- **arXiv**: https://arxiv.org/abs/2608.06362
- **发布**: 2026-08-06 | cs.GT, cs.AI, cs.CL, cs.LG, cs.MA
- **作者**: Boning Li, Yu Chen, Longbo Huang
- **摘要**: 判断两个 agent 谁更强需要打很多局，每局都花钱。AIVAT 通过条件均值零校正降方差（中位 54×），但不说何时停。AV-AIVAT 结合连续监测的置信序列（CS）实现任意时点有效停止：原始结果需要中位 **74×** 的手数才能达到 AIVAT 校正结果的停止条件。精确有限样本认证用 Empirical-Bernstein CS。把方差缩减转化为高效、可审计的提前停止。
- 💎 **与我们相关**: agent 对比评估成本优化——可用于我们模型 fallback 链/模型选型的对比测试方法论。

### 9. EcoAgent-Bench: 预算约束下 LLM Agent 的经济决策评估
- **arXiv**: https://arxiv.org/abs/2608.05519
- **发布**: 2026-08-06 | cs.AI, cs.CL, cs.LG
- **作者**: Jie Wu 等
- **摘要**: 现有 benchmark 只测任务完成，把资源使用当辅助统计。EcoAgent-Bench 每个任务都有定价动作和显式预算，304 个任务覆盖 5 个家族（GAIA/HotpotQA/MuSiQue 改编），测 4 类决策：避免不必要升级、本地证据不足时升级、选择模型档位、在无支撑前提时停止。**工具 API agent 仅 3.9-24.0% 微严格成功率（经济一致性最多 7.3%）**——"预算下完成任务"和"经济地选择动作"是两个独立属性。
- 💎 **与我们相关**: 闲鱼接单成本核算/模型选型的经济决策可直接套用该框架：什么时候用贵模型、什么时候本地查。

### 10. State2State: 环境派生的 LLM Agent 中期训练
- **arXiv**: https://arxiv.org/abs/2608.04934
- **发布**: 2026-08-05 | cs.CL, cs.LG
- **作者**: Xuanyu Lei 等（阿里云等）
- **摘要**: Agent 训练通常依赖专家轨迹 SFT 或人工任务 RL，都被外部指定的任务和监督信号瓶颈化。State2State 只通过环境交互获取能力：把探索到的环境状态转成训练目标（到达指定目标状态），规则化状态匹配验证成功。ALFWorld/ScienceWorld 上多数设置提升，作为下游 RL 初始化进一步提升最终性能和学习效率，有跨环境泛化证据。
- 💎 **与我们相关**: "无需人工任务设计的可扩展验证训练"——启发未来自监督 agent 训练方向。

---

## 📌 一句话总结

| # | 论文 | 一句话 |
|---|------|--------|
| 1 | ASTELD | OpenClaw 六轴分类框架；本地优先+企业级安全仍是空白区 |
| 2 | Skill-Use | 技能真实使用率仅 61.3%，触发是瓶颈，且依赖 harness |
| 3 | EvolveNet | 协作式 harness 进化，5 个场景全提升 |
| 4 | EvoHarness-RL | 可训练 harness 策略胜过堆工具/大记忆，ALFWorld 96.9% |
| 5 | 自我进化反噬 | 技能池超临界会污染退化且不可逆，需事前门控 |
| 6 | DreamGuard | 风险世界模型护栏，25ms/次，防长时程漂移 |
| 7 | MERIT | 双极性因果记忆修复，Schema 本地经验收益最稳 |
| 8 | AV-AIVAT | Agent 评估可 74× 降本 + 任意时点有效停止 |
| 9 | EcoAgent-Bench | 预算约束下经济决策是独立能力，agent 普遍不合格 |
| 10 | State2State | 环境派生目标训练，无需人工任务设计 |

**行动项**: ① 用 ASTELD 六轴评估我们 Hermes 配置（找设计空白）；② 技能库执行 skill-library-audit（防污染退化）；③ Skill-Use 触发瓶颈 → 检查技能 description 自包含性。

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
