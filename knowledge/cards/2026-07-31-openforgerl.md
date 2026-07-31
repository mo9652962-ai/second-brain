---
aliases:
  - 2026-07-31-card-openforgerl
tags:
  - knowledge-card
  - arxiv
  - ai-agent
  - rl
  - harness
created: 2026-07-31
source: "[[knowledge/arxiv-2026-07-31-core-contributions]]"
---

# 🃏 知识卡片 · OpenForgeRL：用你每天都在用的 Agent Harness 直接训练模型

> **来源**：arXiv 2607.21557v2 · 2026-07-23 · ICLR 2027 投稿 · ✅ 已验证
> **一句话**：给现代 Agent Harness（Claude Code / Codex / **OpenClaw**）插一个轻量 proxy，就能把日常使用轨迹变成 RL 训练数据——训练-部署错配问题有了开源解法。

---

## 核心洞察

| 问题 | 传统局限 | 它的解法 |
|------|---------|---------|
| **训练-部署错配** | 开源 RL 栈表达不了 harness 的状态化推理 | proxy 插在 harness 与 RL codebase 之间，解耦训练与推理 |
| **训练数据难获取** | 需人工构造干净环境 | proxy 顺手把模型调用记录为训练数据 |
| **环境难扩展** | 单机 rollout 慢、状态易串 | K8s orchestrator 每个 rollout 独立远程容器 |

## 机制示意

```
Agent Harness (OpenClaw/Codex/Claude Code)
        │ 模型调用
        ▼
  Lightweight Proxy ──→ 记录轨迹 = 训练数据
        │
        ├──→ 标准 RL codebase (veRL)  ← 直接训练
        └──→ Kubernetes Orchestrator  ← 任意环境任意规模
```

## 关键数据

- OpenForgeClaw：ClawEval **31.7 pass^3** / QwenClawBench **33.7**
- OpenForgeGUI：OSWorld-Verified **37.7** / WebVoyager **72.3**
- 只需 **几百到几千个任务** 即可训练出可用 agent（数据效率高）
- 诚实结论：**错误恢复仍是短板** —— 与我们的教训一致

## 为什么对 sora 重要

1. **论文点名 OpenClaw** —— Hermes 正是 OpenClaw 系，这是离我们最近的一条「自训模型」路径
2. **轨迹记录层** —— 给 Hermes 模型调用链加记录层，积累真实使用数据，为未来训练自有模型备料
3. **数据效率门槛低** —— 几百个任务即可起步，不是遥不可及的算力工程

**可借鉴到**：`hermes-automation-patterns` 可靠性模式 + 未来自训数据管线设计

---

*卡片来源：当天知识库精选 · arxiv-2026-07-31-core-contributions（🥇 精选）*
