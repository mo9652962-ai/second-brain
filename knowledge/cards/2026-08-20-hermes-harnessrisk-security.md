---
aliases:
  - 2026-08-20-card-hermes-harnessrisk-security
tags:
  - knowledge-card
  - ai-agent
  - security
  - hermes
  - harness
created: 2026-08-20
source: "[[knowledge/Research/arxiv-2026-08-20-agent-llm]]"
status: fresh
---

# 🃏 知识卡片 · Hermes+DeepSeek-V4-Pro 安全风险：ASR 65.4%，检测率仅 34.6%

> **来源**：arXiv 2608.17597v1 *HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety*（UNC Chapel Hill / UCF / MSU，08-18 提交）· 2026-08-20 入库 · ✅ web_extract arxiv 原文 + 项目页安全矩阵双重核实
> **一句话**：HarnessRisk 直接评测 Hermes 安全——在 6 个生命周期阶段 128 个沙箱用例下，**sora 的日常配置（Hermes + DeepSeek-V4-Pro）攻击成功率 65.4%，检测率仅 34.6%**，是 Utility 最高但最不安全的组合。

---

## 核心洞察

| 维度 | 内容 |
|------|------|
| 基准设计 | 6 生命周期阶段（配置/能力扩展/运行时/状态持久化/动作控制/事件恢复）× 128 沙箱用例，每例配对良性目标 + 对抗指令 |
| 评测指标 | ASR（攻击成功率）、Utility（有用性）、Persistence（持续性）、Detection（检测率） |
| 3 个 Harness | OpenClaw、**Hermes**、Nanobot — 这是首次有公开发表的工作直接评测 Hermes |
| 关键发现 | **Harness Configuration 阶段最脆弱**——攻击者只需在授权工作流内改安全敏感参数即可成功 |

## 对 sora 的影响（安全矩阵对照）

**Hermes 上 4 个模型的安全对比：**

| 模型 | ASR ↓ | Utility ↑ | Persistence ↓ | Detection ↑ |
|:---|:---:|:---:|:---:|:---:|
| DeepSeek-V4-Pro 🟡 | **65.4%** | **97.6%** | 20.5% | **34.6%** |
| GLM-5.2 | 23.8% | 96.8% | 4.0% | 61.9% |
| Kimi K2.6 | 65.6% | 93.8% | 15.6% | 11.7% |
| MiniMax M3 | **14.8%** | 96.1% | **5.5%** | **85.2%** |

1. ⚠️ **DeepSeek-V4-Pro 是 Utility 最高（97.6%）但最不安全的组合**：ASR 65.4%（14 个配置中第 3 高），Detection 仅 34.6%（14 配置中第 3 低）。攻击成功率高、检测率低 → 攻击者可以持续作恶不被发现
2. ⚠️ **Utility 高不等于安全**：MiniMax M3 的 ASR 仅 14.8% 而 Utility 高达 96.1%——安全与能力不必然冲突，但 V4-Pro 恰好是那个最危险的折中点
3. ✅ **我们已有的防护层仍有价值**：Hermes 的审批策略（approval policy）、dsh 禁 auto-mode、外部动作谨慎——这些是「模型外强制」措施，HarnessRisk 测的是模型本身在 harness 内的行为，两者互补
4. 💡 **Harness Configuration 是最大弱点**：攻击者可以在授权工作流内改安全参数——这提醒检查所有配置项（包括工具开关、审批策略、权限预设）

## 行动项

- [ ] 阅读 HarnessRisk 论文细节，了解哪些攻击向量在 Hermes 上成功率最高（尤其是 Configuration 阶段）
- [ ] 检查 Hermes 配置：`hermes config` 查看当前审批策略、工具开关、权限设置——看是否有可收紧的安全配置面
- [ ] 后续内容选题素材：「你的 AI 助手比你想象中更脆弱——HarnessRisk 实测 Hermes 攻击成功率 65%」

## 为什么重要

- **直接评测 Hermes 的首次公开发表工作**——不是通用 agent 安全，而是 sora 正在用的 harness
- **sora 的默认模型（DeepSeek-V4-Pro）是最高风险组合**，但注意 Utility 97.6% 也是最高——这是能力与安全的经典权衡，不是「换模型」的简单结论
- **与昨天卡片（Bounded Agents 授权架构）形成互补**：昨天讲「授权防注入」，今天讲「harness 本身的安全基准」——两篇合起来看清了全貌
- **可行动性强**：有明确的检查方向（配置审计、审批策略、攻击向量理解）

---

*卡片来源：当天知识库精选 · [[knowledge/Research/arxiv-2026-08-20-agent-llm]]（🥇 HarnessRisk 直接评测 Hermes + DeepSeek-V4-Pro ASR 65.4% 数字经项目页核实——这是 sora 的生产环境配置，安全风险有具体数字，不是空谈）*

**亚军候选**：同一 arXiv 池的 *Test-Time Scaling in the Wild*（2608.18931）——实证 SOTA reward model 与真实质量相关性仅 ρ≈0.12，开放域 TTS 利用崩溃。与 sora 的模型路由评测系统直接相关，但更多是「需关注」而非「马上行动」。