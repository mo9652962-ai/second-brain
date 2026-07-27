---
tags: [Agent Skills, 工程方法论, TDD, 学习笔记]
aliases: [Matt Pocock Skills, 编程工作流]
date: 2026-07-22
source: https://github.com/mattpocock/skills
---

# Matt Pocock Skills

> 来源: [mattpocock/skills](https://github.com/mattpocock/skills)
> ⭐ 183K | 🚀 本周新增 2.4K (trendshift.io 月榜 Top 10)
> 作者: Matt Pocock（知名 TypeScript 教育家）
> 学习时间: 2026-07-22 (更新: 2026-07-27)
> 所属知识网络: [[knowledge-map]] | 相关: [[mattpocock-methodology]] | engineering-workflow | [[system-design-primer]] | [[ibelick-ui-skills]]

## 项目定位

Matt Pocock 的 **个人 Agent Skills 集合**，是他每天用来做真实工程开发的 skill 集——不是 vibe coding。

## 核心理念

"Developing real applications is hard. Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control."

→ **这些 skill 小而精、易修改、可组合。**

## Skill 列表

### 工程类 (User-invoked)

| Skill | 功能 |
|:----|------|
| **ask-matt** | 路由 skill，告诉你该用哪个 skill |
| **grill-with-docs** ⭐ | 面试式需求分析 + 创建文档（术语表 + ADR） |
| **triage** | Issue 状态机流转 |
| **improve-codebase-architecture** | 扫描代码库 → HTML 报告 → 改进 |
| **to-spec** | 将对话转为 spec 并发布到 issue tracker |
| **to-tickets** | 将 plan/spec 拆成 ticket |
| **implement** | 完整实现流程，驱动 /tdd |
| **wayfinder** | 超大任务规划，分步探索 |

### 工程类 (Model-invoked)

| Skill | 功能 |
|:----|------|
| **tdd** | 红-绿-重构 TDD 循环 |
| **diagnosing-bugs** | Bug 诊断循环 |
| **research** | 对高信任度一手资料做调研 |
| **domain-modeling** ⭐ | 构建并打磨项目的领域模型 |
| **codebase-design** | 深度模块设计（大量行为通过小接口暴露） |
| **code-review** | 双轴代码审查（标准 + Spec 一致性） |
| **prototype** | 快速原型验证 |
| **resolving-merge-conflicts** | Git 合并冲突解决 |

### 生产力类 (User-invoked)

| Skill | 功能 |
|:----|------|
| **grill-me** ⭐ | 面试式需求澄清 |
| **handoff** | Agent 之间的交接文档 |
| **teach** | 跨会话教学 |
| **writing-great-skills** ⭐ | **如何写好 skill 的元知识** |

### 生产力类 (Model-invoked)

| Skill | 功能 |
|:----|------|
| **grilling** | grill-me / grill-with-docs 背后的可复用循环 |

---

## 💎 最宝贵的收获：写作 Skill 的艺术

Matt 的 `writing-great-skills` 是我见过最好的 skill 设计指南。以下是核心法则：

### 1. 可预测性 > 一切

Skill 的根目标是：**Agent 每次跑同样的流程**，而不是产生同样输出。

### 2. 两种调用方式

| 方式 | 描述 | 上下文消耗 | 场景 |
|:---:|:---:|:---:|:---:|
| **Model-invoked** | Agent 可自主调用 | ❌ description 常驻 | Agent 必须能自己触发 |
| **User-invoked** | 只能用户手动调用 | ✅ 零上下文 | 仅用户手动触发，用 router 索引 |

> 用 `disable-model-invocation: true` 标记 user-invoked

### 3. 信息层级

```
1️⃣ 步骤 (Step) — SKILL.md 中的有序操作，明确完成条件
       ↓
2️⃣ 内联参考 (In-skill Reference) — SKILL.md 中的定义/规则/事实
       ↓
3️⃣ 外部参考 (External Reference) — 分离文件，上下文指针加载
```

**渐进式披露**：将不常用的内容推进下层文件，保持顶层简洁。

### 4. 何时拆分 Skill

- **按调用拆分** — 当有一个独立的触发器词时
- **按步骤序列拆分** — 当后续步骤让 Agent 想跳过当前步骤时

### 5. 修剪原则

- **SSOT**（单一事实来源）：每个概念只在一个地方定义
- **相关性检查**：每一行是否仍然相关？
- **无操作检查**：去掉不改变默认行为的文本
- **删除整个句子**，而不是修剪词

### 6. 引导词 (Leading Words)

用模型预训练中已有的紧凑概念（如 _lesson_、_fog of war_、_tracer bullets_），一句话改成一个词：

- "fast, deterministic, low-overhead" → **tight**
- "a loop you believe in" → **red**

### 7. 失败模式

| 模式 | 说明 | 解决 |
|:----|------|------|
| **Premature completion** | 提前结束步骤 | 明确完成条件 |
| **Duplication** | 同一含义多处出现 | 合并到 SSOT |
| **Sediment** | 陈旧内容堆积 | 定期修剪 |
| **Sprawl** | skill 过长 | 用层级推进披露 |
| **No-op** | 不改变默认行为的文本 | 删除 |
| **Negation** | 通过禁止来引导（适得其反） | 用正面引导代替 |

---

## 对我最有启发的内容

1. **`grill-with-docs` — 面试式需求分析**
   在写代码之前先和用户深度对齐，创建领域术语表和 ADR。这解决了我作为助手时的「理解偏差」问题——以后接到复杂任务我应该先问你几个问题再动手。

2. **`writing-great-skills` — Skill 方法论**
   Matt 的 skill 设计哲学比我们现有的更成熟。可以直接用来改进我们的现有 skill。

3. **`domain-modeling` — 领域模型**
   建立共享语言（Ubiquitous Language），让 Agent 和用户说同样的术语。

4. **双轴 Code Review**
   一个轴检查编码标准，另一个轴检查是否忠实实现了 spec。两个子 Agent 并行执行互不干扰。

## 对我们的 skill 改进建议

基于 Matt 的方法论，我们现有 skill 可以改进：

| 当前 skill | 问题 | 状态 | 改进方向 |
|:---------|:---:|:----:|---------|
| 8051-embedded-dev | 偏知识清单 | ✅ **已有 Gril 步骤**（openclaw-imports） | 已完成 |
| cad-design-master | 模板偏多 | ✅ **已有 Gril + 完成标准**（openclaw-imports） | 已完成 |
| 所有 PPT skills | 无完成条件 | ✅ **已修复 (2026-07-26)** | 每个阶段加了明确完成标准 |

笔记已更新到 `memory/mattpocock-skills.md`
