# Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills

| 元数据 |  |
|:-------|:--|
| **ID** | [`2607.22529`](https://arxiv.org/abs/2607.22529) |
| **日期** | 2026-07-24 |
| **分类** | cs.CL |
| **作者** | Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen 等 |

---

## 核心贡献

LLM 训练正从人工设计转向交互驱动的自我进化。但现有自进化方法面临 **任务多样性 vs 验证可靠性** 的根本矛盾：

- **环境绑定法** → 反馈精准，但局限在狭窄领域
- **开放自生成法** → 任务空间广，但缺乏可靠验证，误导性奖励会污染训练

**Skill-SP 的突破：** 把 **Agent Skill** 作为中间地带——每个 skill 在特定场景下**可深度执行、可验证**，动态路由跨 skill 保持**任务多样性**。

## 框架架构

```
┌──────────────────────────────────────────┐
│           Skill Self-Play 循环             │
│                                          │
│   Proposer ──生成挑战性任务──→ Solver     │
│     ↑                            │       │
│     │                    探索候选解决方案   │
│     │                            ↓       │
│   Skill Controller ←──收集执行反馈───┘     │
│     ↑                                    │
│     └────── 更新 & 扩展 Skill 库 ────────┘│
└──────────────────────────────────────────┘
```

三个组件通过 **RL 循环** 协同进化：

| 组件 | 职责 |
|:-----|:------|
| **Proposer** | 基于动态采样的 skill 生成有挑战性的任务 |
| **Solver** | 探索候选解决方案，推动能力边界 |
| **Skill Controller** | 收集执行反馈，更新和扩展 skill 库 |

## 关键结果

- 在 tool-use 和 reasoning 基准上持续推高强基线的天花板
- 对初始对齐不佳的模型能实现"逆转翻盘"
- 有效弥合了**结构化验证**与**开放探索**之间的鸿沟

## 与 sora 的关联 🔗

这是 **Regression Tax (2607.22520)** 的「解药」级论文：

| Regression Tax | Skill Self-Play |
|:---------------|:----------------|
| 指出 Skill 会引入倒退 | 给出如何构建 good Skill 的方法 |
| 只分析问题 | 给出 Proposer-Solver-Controller 框架 |
| 建议审计 Skill | 实现 Skill 自动进化 |

**可借鉴到 Hermes Skill 体系：**
1. **动态 Skill 路由** — 不是所有 skill 都要加载，根据上下文动态选择
2. **Skill 执行反馈闭环** — 收集 skill 的使用效果，自动淘汰低效 skill
3. **Skill 生成** — 可以尝试让 proposer 模式自动生成新 skill

---

*吸收状态: adopted — 与 Hermes Skill 体系直接相关，已纳入 skill 设计方法论*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
