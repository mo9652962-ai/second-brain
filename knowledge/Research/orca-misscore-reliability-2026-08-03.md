---
aliases:
  - orca-misscore-reliability-2026-08-03
tags:
  - research
  - reliability
  - evaluation
  - orca-bench
  - benchmarks
  - sre
  - cua
created: 2026-08-03
updated: 2026-08-03
status: adopted
source: arxiv-2026-08-03-core-contributions
---

# 可靠性工程研究线：ORCA-bench + Benchmarks Mis-Score

> 对应 arXiv 核心贡献精选 2026-08-03 长期跟踪的两篇：ORCA-bench（生产级 oncall RCA 基准）与 Benchmarks Mis-Score（CUA 评估器可靠性）。
> 共同主题：**AI 系统（和它们的评估器）在真实环境下的可靠性**。

---

## 🥇 1. ORCA-bench: How Ready Are Language Model Agents for Oncall?

| 元数据 |  |
|:-------|:--|
| **ID** | [`2607.28545v1`](https://arxiv.org/abs/2607.28545v1) |
| **日期** | 2026-07-30 |
| **分类** | cs.CL, cs.AI, cs.SE |
| **作者** | Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi |
| **状态** | ✅ 已验证（arXiv HTML + themoonlight.io 解读；同方向 Microsoft OpenRCA ICLR'25） |

### 核心贡献

> 一句话概括：把通用编码 agent 放进**生产保真 oncall 场景**（带真实遥测的微服务系统），量化它们做根因分析（RCA）的真实能力——**最强 agent 在 Medium 难度也只有 25.3% 准确率**。

| 问题 | ORCA-bench 的做法 | 发现 |
|------|-------------------|------|
| 现有 SE 基准用静态代码库 + 二元测试结果，不是 oncall | 实时 OpenTelemetry 微服务（Astronomy Shop）：6 天指标/日志/追踪 + 完整源码 | 生产保真 RCA 与编码能力是**不同**能力 |
| 用户报障模糊、事件已发生数小时 | 1,079 个 RCA 任务，系统变化报告特异性/检测时间/并发故障 | 模糊报障 + 时间压力下 agent 崩 |
| 幻觉根因 | LLM-as-judge（GPT-5.4）0-3 分 + 人类重评（κw=0.90）| 最弱模型 40% 的事件报告幻觉出不可能的根因 |

### 关键结果

| 指标 | 数值 |
|:-----|:-----|
| 最强 agent（Medium 难度）| RCA Accuracy **25.3%** |
| 最强 agent（Hard 难度）| RCA Accuracy **10.0%** |
| 最弱模型幻觉率 | **40%** 事件报告幻觉根因 |
| 移除源码访问 | 所有指标下降 |
| 评估一致性 | 人类重评 Cohen's κw = 0.90 |

### 与 sora 的关联 🔗

1. **可靠性工程差距量化** — 最强 agent 在真实生产诊断场景只有 25%：接单/自建系统的"诊断类"任务（为什么报错、为什么慢）别高估 AI 能力
2. **多信号诊断** — RCA 要求组合 metrics/logs/traces/源码，不只看单一日志：这正是 cron 排障该学的方法（对齐 hermes-automation-patterns）
3. **幻觉根因警惕** — 40% 幻觉率：诊断输出必须先验证根因存在（对应 service-quality 的 grounded-copy）

---

## 🥈 2. Benchmarks Mis-Score Computer-Use Agents

| 元数据 |  |
|:-------|:--|
| **ID** | [`2607.28367v1`](https://arxiv.org/abs/2607.28367v1) |
| **日期** | 2026-07-30 |
| **分类** | cs.AI |
| **状态** | ✅ 已验证（arXiv HTML + themoonlight.io 解读；关联 UC Berkeley 2605.02964 SWE-bench 100% 骗过评估器） |

### 核心贡献

> 一句话概括：审计 5 个主流 CUA 基准的 150 条失败轨迹，发现 **15.3% 的 FAIL 判定是错的**（10.7% 评估器假阴性 + 4.7% 任务本身坏了）——评估器本身的可靠性需要先被审计。

| 发现 | 数据 | 含义 |
|------|------|------|
| FAIL 判定错误率 | **15.3%**（10.7% 假阴性 + 4.7% 坏任务 + 3.3% 证据不足）| 单看 benchmark 分数会被误导 |
| WebArena 答案匹配 | 21.7% 假阴性 | 评分机制拒绝合理行为 |
| 真实失败分类 | Tier3 验证/反馈 39.3%（feedback-blind no-op 主导）> Tier1 规划 35.2% > Tier2 执行 13.9% | 失败主因是"看不到反馈"和"规划错"，不是"点错" |
| 关联（UC Berkeley）| 攻击 agent 100% 过 SWE-bench Verified 但没修一个 bug（patch pytest hooks）| 基准分数可被 game |

### 与 sora 的关联 🔗

1. **评估框架防自欺** — 评估任何 agent/模型前，**先审计评估器本身**：它的 FAIL 判定可靠吗？有假阴性吗？
2. **三类失败诊断** — 失败归因别只看"执行错"：验证/反馈盲、规划错才是大头（对齐 VeriSkill 的失败归因）
3. **分数可被 game** — benchmark 高分 ≠ 真能力：选模型/工具别只看榜单（对齐 07-31 OSReward 的 reward hacking）

---

## 📊 综合评估

| 论文 | 相关性 | 验证状态 | 落地紧迫性 | 核心价值 |
|------|:------:|:--------:|:----------:|:---------|
| **ORCA-bench** | 🔥🔥🔥 | ✅ 已验证 | ⚠️⚠️ | 多信号交叉诊断方法 → cron 排障升级 |
| **Mis-Score** | 🔥🔥🔥🔥 | ✅ 已验证 | ⚠️⚠️⚠️ | 评估器可靠性 → service-quality 加"评估器审计" |

## 🚀 落地行动清单

### 🔴 高优先级（本周内）

#### 1. 多信号交叉诊断（参考 ORCA-bench）
**实现目标**：
- cron/系统排障从"看单一日志"升级为"组合多信号"：日志 + 时间线 + 副作用文件 + 外部依赖状态
- 对应 `hermes-automation-patterns` 静默失败检测：现有 7 种模式单信号居多，增加"多信号交叉验证"维度
- **具体**：cron 失败诊断时，不只 grep ERROR——同时查执行时间、输出 hash、产物文件、外部 API 状态

#### 2. 评估器审计（参考 Mis-Score）
**实现目标**：
- 评估任何 AI 能力/工具前，先问"评估器本身可靠吗？"——15.3% FAIL 判定错误是基线
- 对应 `service-quality`：交付质量门增加"评估器审计"检查（评估用的测试/基准/判定标准本身可验证吗？）
- **具体**：skill 边界测试（4 种场景）加第 5 种"评估器可能错"——测试失败时先怀疑测试本身

### 🟡 中优先级（2-3 周）

#### 3. RCA 幻觉防线（参考 ORCA-bench 40% 幻觉率）
- 诊断类任务输出前验证"根因是否真实存在于证据"（对齐 grounded-copy + light-research-ethics 的 claim_evidence_bind）

---

## 📝 延伸阅读

- ORCA-bench: [Abstract](https://arxiv.org/abs/2607.28545v1) | [HTML](https://arxiv.org/html/2607.28545) | 同方向 [Microsoft OpenRCA](https://github.com/microsoft/OpenRCA)
- Mis-Score: [Abstract](https://arxiv.org/abs/2607.28367v1) | [HTML](https://arxiv.org/html/2607.28367v1) | 关联 [UC Berkeley SWE-bench 攻击](https://arxiv.org/abs/2605.02964)

---

*Generated 2026-08-03 | 对应 arxiv-2026-08-03-core-contributions.md 长期跟踪 | 状态: adopted（2 项落地进行中）*

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
