---
title: arXiv 2026-09-19 核心贡献总结
date: 2026-09-20
source: arxiv-2026-09-19-agent-llm.md (13 主条目 + 5 简评补全速览精选)
selected: EconSkills 技能库 / LLM Benchmarks 评测元研究 / 激活探针安全
status: 已深挖 3 篇（web_search 双源交叉验证）
data-cutoff: 2026-09-20
tags: [arxiv, research, knowledge/research]
---

# arXiv 核心贡献总结 · 2026-09-19（09-20 处理）

> 来源：arxiv-fetch cron 2026-09-19 13:13 输出（09-18 同池 602 篇补全速览，与昨日零重叠），web_search 双源交叉验证后深挖 3 篇
> 精选原则：fetch 明确推荐 4 篇待深读候选（19182 评测元研究 / 19523 技能库 / 19472 激活探针安全 / 19799 进化搜索评测）；跨周论文级去重确认与历史 55 个已深挖 ID 零重叠 ✅；选 3 篇 ★★★★★（其中 19182/19523/19472 已入 digest 验证表，19799 为 ★★★★ 转入延伸阅读）——分散 3 个方向：**技能库实证化 / 评测元视角 / 内部信号层安全**

## 🥇 EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data (2609.19523)

**标题**: EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data
**核心**: Web agent 反复重访同一站点却丢弃早前成功交互学到的流程。EconSkills 把已验证的 EconWebArena 轨迹蒸馏为**参数化标准操作程序（SOP）技能库**——每条技能记录范围/导航流程/站点特定指引/验证检查/恢复步骤，源实例值替换为占位符。分离两个问题：已知相关流程能否迁移到未见任务；agent 在库规模下能否保留收益。**受控迁移中匹配技能显著提升成功率、配对成功步数更少，抽象化远超重放原始轨迹；但库级检索整体只与无技能基线竞争、仅在直接覆盖任务上最佳——近似匹配的收益抵消**。给 coverage-aware 选择与上下文投递提供具体设计目标。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **SOP 抽象化 > 重放原始轨迹** | 受控迁移：匹配技能提升成功率、配对成功步数更少；抽象化「substantially more effective」 | 实证背书 k「写技能不存日志」的做法——技能应是参数化抽象（占位符+验证检查+恢复步骤），不是 raw 轨迹回放 |
| **技能结构 = 五要素** | scope / navigation procedure / site-specific guidance / verification checks / recovery steps | 直接可抄进 k 的 SKILL.md 骨架：范围声明 + 导航步骤 + 站点/领域特定指引 + 验证检查 + 恢复步骤 |
| **覆盖分层决定检索收益** | 库级检索整体与无技能基线竞争、直接覆盖任务最佳；未覆盖任务的近似匹配**抵消**增益 | k 技能匹配要标记「直接覆盖/近似/未覆盖」——近似匹配的收益抵消是实证警告（接单技能匹配误报要纳入决策） |
| **覆盖感知设计目标** | 结果为 coverage-aware selection 与 context delivery 提供设计目标 | 技能加载不能只看语义相似度——要显式感知覆盖度，否则库越大近似匹配噪声越多 |

### 方法/架构

```
已验证 EconWebArena 轨迹（真实经济数据站点）
    ↓ 蒸馏为参数化 SOP 技能库
    ├─ scope（适用范围）+ 站点特定指引
    ├─ navigation procedure（导航流程）
    ├─ verification checks（语义验证检查）
    └─ recovery steps（恢复步骤）+ 源实例值→占位符
    ↓ 分离两个问题
    ├─ Q1 受控迁移：已知相关流程 → 未见任务（匹配技能提升成功率、步数更少）
    └─ Q2 库级检索：从技能库选择时能否保留收益（直接覆盖最佳、近似匹配抵消）
    ↓
    覆盖分层（direct / approximate / uncovered）评估检索收益
    + Browser 轨迹识别「程序化指引何时缩短门户导航 / 语义验证何时仍必要」
```

| 问题 | 结果 |
|:---|:---|
| 受控迁移（匹配技能 vs 无技能） | 成功率提升、配对成功步数更少 |
| 抽象化 vs 重放原始轨迹 | 抽象化大幅更有效 |
| 库级检索（整体） | 与无技能基线竞争（持平） |
| 库级检索（直接覆盖任务） | 最佳（收益保留） |
| 库级检索（未覆盖任务近似匹配） | 抵消增益（噪声） |

### 与 sora 的关联

✅ **与 k 技能体系直接同构**：skill 蒸馏（成功轨迹→参数化技能）、按需检索加载、覆盖分层评估——k 的 covered_ids/去重机制、skill-pipeline 九流派六段质检同思路；「抽象化远超重放原始轨迹」验证「写技能不存日志」；「近似匹配收益抵消」是技能匹配误报的实证警告
✅ **技能结构可直接落地**：五要素（scope/导航/指引/验证/恢复）正好是 k 写 SKILL.md 的骨架，占位符思想与「模板参数化」一致
✅ **外部佐证同方向活跃**：Break It Down Pass It On (2608.20274 跨任务技能迁移) / Optimal Skill Selection (2608.19993 技能选择子模优化+BPS 算法) ——技能库/技能选择是 2026 活跃研究轴，k 的技能体系走在前沿同题

## 🥈 What Do We Expect from LLMs? Mapping the Design of LLM Benchmarks (2609.19182)

**标题**: What Do We Expect from LLMs? Mapping the Design of LLM Benchmarks
**核心**: 系统映射 **14,767 篇**（2022-01 至 2026-08 arXiv）提出/更新评测资源的论文，用分期筛选 + 自动化全文编码考察目标系统/领域、评测材料与条件、打分机制的变化。**LLM 打分在 agent 与非 agent 组都增长（25.8%→40.3%），而模型生成材料近期未持续增长**；action/interaction/专业应用评测日益增长。核心反思：AI 参与构造测试、执行任务、评判回答时，「更多评测」是提供更多独立证据，还是复制参与模型的偏好与盲点？

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **LLM-as-judge 持续扩散** | LLM 打分占比 25.8% (2024) → 35.5% (2025) → 40.3% (2026)；agent 组 26.3%→44.0%，非 agent 组 25.7%→38.8%（组内增长贡献 13.95/14.51pt） | k 的 verify_digest_note / service-quality 门禁要自问「由谁构造测试、由谁打分」——LLM judge 复制偏好盲点是系统性风险 |
| **打分机制迁移** | execution/environment 16.9%→28.4%；reference/metric 72.6%→59.6%；人工直评 9.8%→4.7% | 「可执行环境打分」在涨、「人工评审」在跌——k 的质检门禁往「可执行验证 + 证据链」走是顺应大方向 |
| **模型生成材料未同步增长** | 近期 cohort 无持续增长（与 LLM 打分不同轨迹） | 「AI 出题」没有「AI 打分」普及快——评测不是均匀自动化，是分维度演进（判断材料真实性时区分维度而非一刀切） |
| **混合设计是常态非全自动** | 22.2% 记录含模型材料+LLM 打分；其中 77.3% 同时含人类/真实世界材料、61.7% 另有打分机制 | 「混合评测」不自动等于「有效评测」——mixture 不建立监督或效度，k 的评测要显式声明材料来源与打分机制组合 |

### 方法/架构

```
arXiv 2022-01 ~ 2026-08 论文流
    ↓ 分阶段筛选（introduce/update 可复用评测资源）
    ↓ 自动化全文编码（14,767 篇）
    ├─ RQ1 目标系统/领域：agent vs 非 agent、专业应用、随时间分布
    ├─ RQ2 评测材料/条件：模态、任务语言、评测设定
    └─ RQ3 打分机制：LLM 打分 / execution-environment / reference-metric / 人工直评
    ↓
    发现：action/interaction/专业应用增长；新旧设计并存；LLM 打分↑ 模型生成材料持平
    ↓ 核心问题：AI 构造测试+评判回答时——更多独立证据，还是复制偏好盲点？
```

| 打分机制 | 2024 | 2026 |
|:---|:---|:---|
| LLM 打分 | 25.8% | 40.3% |
| Execution/Environment | 16.9% | 28.4% |
| Reference/Metric | 72.6% | 59.6% |
| 直接人工评判 | 9.8% | 4.7% |
| LLM 打分（agent 组） | 26.3% | 44.0% |

### 与 sora 的关联

✅ **直接回应 Gemini 跨源盲评设计动机**：k 坚持 Gemini 跨源盲评的「独立性」是有意为之——本论文把「由谁构造测试、由谁打分」问题摆到台面；「LLM judge 复制的偏好盲点」是 k 盲评设计要防的核心风险，保持并文档化
✅ **评测设计元视角进质检门禁**：verify_digest_note / service-quality 加「谁构造测试、谁打分」自检项——评测自己的评测成为独立研究轴，k 的方向与前沿一致
✅ **agent 评测数据可引用**：agent 组 LLM 打分 26.3%→44.0% 的量化数据可用于 k 的产品/方案文档中论证「可执行环境 + 独立证据链」的评测设计

## 🥉 Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models (2609.19472)

**标题**: Safety Beyond the Interface: Detecting Harm via Latent States in Large Language Models
**核心**: 外部 guardrail 模型对模型内部运作「失明」，且在资源受限/时间关键部署中引入延迟与算力开销。**从冻结 LLaMA-3.1-8B 提取激活（末层 4096 维 last-token pooling）训练 6 层 MLP 探针（12.6M 参数，仅 0.16%），WildJailbreak/BeaverTails/AEGIS 2.0 上 F1 99.1%/82.7%/83.5%，与 1000× 更大 guard 模型竞争持平**；探针与生成并发执行、<1ms 延迟、可提前终止，不占独立 GPU、无网络传输。内部状态是黑盒攻击者结构性不可达的信号层。

### 核心贡献表

| 发现 | 数据 | 对 sora 的意义 |
|:---|:---|:---|
| **12.6M 参数平 1000× guard 模型** | BeaverTails 82.7% vs WildGuard 84.4% / MD-Judge 86.7%（7B），超 LlamaGuard2 71.8%；AEGIS 83.5% 超 WildGuard 81.9% / LlamaGuard3 77.3% | 本地资源约束下「内部信号层」是可行防线——RTX4060/本地部署可评估激活探针替代大 guard 模型 |
| **延迟可忽略** | 探针 <1ms vs 生成 50-500ms；并发执行（延迟取 max 非叠加） | 安全过滤不再拖慢推理——时间关键/流式场景可内嵌检测 |
| **提前终止能力** | 生成中即可标记有害内容并终止，节省算力、限制暴露 | 流式输出的有害内容「边生成边拦截」比事后审核强 |
| **黑盒攻击者结构性不可达** | 内部激活是外部接口看不到的信号 | 外部 guardrail 可被接口级绕过（构造过表面过滤的输入），激活探针提高绕过成本 |
| **副作用警示** | 激活检测可能继承模型/数据偏见，过度过滤语言风格/话题 | 部署需透明 + 治理；k 的提示注入防线叠加内部信号层时注意误伤正常中文表达 |

### 方法/架构

```
冻结 LLaMA-3.1-8B（不动权重）
    ↓ Stage1：prompt → 末层 4096 维激活（last-token pooling）
    ↓ Stage2：6 层 MLP（12.6M 参数，0.16% of 8B，AdamW 50 epochs）
    → 二进制 harmful/benign 分类
    ↓ 部署（与生成并发、同主机）
    ├─ T_probe <1ms（vs 生成 50-500ms）→ 延迟 ≈ 免费
    ├─ 不占独立 GPU / 无网络传输
    └─ 生成中早期终止（flag → terminate）
    ↓
    F1: WildJailbreak 99.1% / BeaverTails 82.7% / AEGIS 2.0 83.5%
```

| 基准 | 激活探针 (12.6M) | 对照 guard 模型 |
|:---|:---|:---|
| WildJailbreak | **99.1%** | — |
| BeaverTails | 82.7% | WildGuard 84.4% / MD-Judge 86.7% / LlamaGuard2 71.8% / BeaverDam 89.9%* / GPT-4 86.1%*（*1000×+ 更大） |
| AEGIS 2.0 | **83.5%** | WildGuard 81.9% / LlamaGuard3 77.3% / LlamaGuard2 76.8% |

### 与 sora 的关联

✅ **本地安全过滤方向参考**：k 的本地/资源受限场景（本地推理、低成本部署）——「外部 guardrail 看不见内部状态 + 12.6M 参数」提示提示注入/有害内容防线可叠加内部信号层；与 09-19 安全簇（19366 类别残余细粒度安全信号）合读，多类别安全干预要查叠加效应
✅ **流式安全护栏**：墨题/刷题机若接 LLM 流式输出，「边生成边拦截」设计可参考探针的提前终止机制
✅ **部署治理警示**：激活探针可能继承模型偏见——做安全过滤时要评估误伤风险，避免对特定语言风格/话题过度过滤（对 k 的中文内容场景尤其相关）

## 综合评估矩阵

| 维度 | EconSkills (19523) | LLM Benchmarks 元研究 (19182) | 激活探针安全 (19472) |
|:---|:---|:---|:---|
| 相关性 (Hermes 体系) | ★★★★★ 技能体系直接同构 | ★★★★★ 评测设计元视角 | ★★★★★ 本地安全/流式护栏 |
| 可落地性 | 五要素技能结构可直接抄 | 质检门禁自检项可立即加 | 需模型激活访问（本地可评估） |
| 证据强度 | 双源验证（arXiv/GenAI Secret Sauce + 同族研究群） | 双源验证（arXiv/bittide 全文数据） | 双源+第三方（arXiv PDF/Zenodo/ResearchGate/ScholarFeed） |
| 数据截止 | 2026-09-20 | 2026-09-20 | 2026-09-20 |
| 吸收状态 | adopted（技能结构/覆盖分层入 skill 体系） | adopted（评测自检入质检门禁） | trial（本地安全方案待评估） |

## 落地行动清单

- 🔴 **待办 · 技能结构五要素对照**：EconSkills 五要素（scope/导航/指引/验证/恢复）对照 k 的 SKILL.md 骨架——检查现有技能是否缺「验证检查 + 恢复步骤」两要素；技能检索加「直接覆盖/近似/未覆盖」覆盖分层标记（近似匹配收益抵消进 ai-freelance-pricing/接单技能匹配决策）
- 🔴 **待办 · 评测自检项**：verify_digest_note / service-quality 加「谁构造测试、谁打分」自检（LLM-as-judge 复制偏好盲点）；Gemini 跨源盲评的独立性保持并文档化
- 🟡 **待办 · 内部信号层安全探索**：本地/资源受限场景评估激活探针方案（12.6M 参数平 1000× guard 模型）；与 19366 类别残余合读，多类别安全干预查叠加效应；部署注意偏见/过度过滤治理
- 🟢 **待办 · 延伸阅读**：Evolution or Illusion? (2609.19799，★4 未选——进化搜索评测「单预算点排名不可靠」→ seeds×iterations frontier 测量协议) / Break It Down Pass It On (2608.20274) / Optimal Skill Selection (2608.19993) / Fine-grained Harm Signals (2609.19366)

## 延伸阅读

- [EconSkills arXiv](https://arxiv.org/abs/2609.19523) · [LLM Benchmarks 元研究 arXiv](https://arxiv.org/abs/2609.19182) · [Safety Beyond the Interface arXiv](https://arxiv.org/abs/2609.19472)
- [Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search](https://arxiv.org/abs/2609.19799) — 进化搜索评测：seeds×iterations frontier 而非单预算点（★4，本期未选入 3 篇）
- [Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents](https://arxiv.org/abs/2608.20274) — 技能迁移：子任务级/文本技能迁移更好，skill utility score 诊断
- [Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees](https://arxiv.org/abs/2608.19993) — 技能选择子模优化 + BPS 算法（首个技能选择性能保证）
- [The Role of Fine-grained Harm Signals in LLM Safety](https://arxiv.org/abs/2609.19366) — 类别残余安全表征，多类别安全干预叠加效应

---

## MANTA 试点记录（2026-09-20）

| 项 | 值 |
|:---|:---|
| 是否触发拓扑变更 | **否** |
| 触发的变更类型 | 无变更（保持固定流程） |
| 监控点1（候选池）判定 | fetch 明确推荐 4 篇待深读（19182 评测元 / 19523 技能库 / 19472 安全 / 19799 评测协议）**分散 4 个方向** → 判定**分散** → 保持常规 3 篇精选，未触发合并调研 |
| 监控点2（草稿）判定 | 3 篇选文均双源验证通过（arXiv 全文 + 独立第三方：GenAI Secret Sauce / bittide.aicompass 全文数据 / Zenodo+ResearchGate+ScholarFeed）→ 证据**充分** → 保持固定验证路径，未触发独立验证者 |
| 子代理预算使用 | 0/3（全部主进程完成，无 delegate_task） |

**质量/成本观察**：
- fetch 输出自带「验证表 + 🟢 待深读清单」（本次直接点名 4 篇候选），summarize 直接消费清单、无需重扫全池 → 选文决策成本 ≈ 0；验证 3 次 web_search 全命中、零修正（含精确数字：12.6M/99.1%/82.7%/83.5%、14,767 篇/25.8%→40.3%），固定拓扑下总成本与历史持平
- **「簇内合并调研」触发条件的二次校准**：本次候选里 19182 与 19799 同属「评测方法论」簇，但只选了 19182（★5），19799（★4）经延伸阅读兜底——被牺牲的强相关簇 = 1（评测协议方向），低于 09-06 确立的「牺牲簇 ≥2 才合并调研」阈值 → 未触发；与 09-13 观察一致：牺牲簇 ≤1 且用延伸阅读补偿即可，无需合并
- 新观察：**fetch 待深读清单直接决定选文**（本次 4 候选 = 3 篇 ★5 + 1 篇 ★4，全部按清单消费，零自选），「fetch 推荐清单升级为正式接口字段」信号第三次验证（09-06/09-13/09-20）——建议后续把 fetch 输出结构固定为「待深读候选 + 验证表 + 行动项」三段，summarize 完全消费化

*本总结由 arxiv-summarize cron 自动生成（2026-09-20），选文/数字基于速览 + web_search 双源交叉验证。*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
