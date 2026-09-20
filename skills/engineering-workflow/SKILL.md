---
name: "engineering-workflow"
description: "软件工程全流程 v1.0：需求对齐(Grill)→领域建模→TDD红绿重构→双轴Code Review→Bug诊断→交接文档。源自 Matt Pocock 方法论，适配 OpenClaw Agent。触发词：开发流程/工程方法/代码审查/TDD/重构"
---

# 软件工程工作流 (Engineering Workflow)

> 基于 Matt Pocock (mattpocock/skills) 工程方法论适配 OpenClaw
> 版本: v1.0 | 2026-07-22

## 🎯 工作流概览

```
用户需求
   ↓
① Grill 对齐 ─── 深度追问，消除理解偏差 → 输出需求文档
   ↓
② 领域建模 ─── 建立共享术语表 + ADR → 统一语言
   ↓
③ 拆解 Ticket ─── 将需求拆成可执行的小块
   ↓
④ TDD 实现 ─── 红-绿-重构循环
   ↓
⑤ Code Review ─── 双轴审查（标准 + Spec）
   ↓
⑥ 交付/交接
```

---

## ① Grill 对齐（需求研磨）

**完成标准**: 所有开放问题已解决，决策树的每个分支已被探索

### 步骤

1. **问核心问题**: 谁用？做什么？输入输出？约束？
2. **追问边界**: 异常情况？极端场景？性能要求？
3. **确认假设**: 列出自己认为「理所当然」的前提，让用户确认
4. **输出**: 一个清晰的、无歧义的需求描述

> 引导词: **grill** — 不是被动听需求，而是主动研磨直到清晰

---

## ② 领域建模（共享语言）

**完成标准**: CONTEXT.md 已创建/更新，术语表中每个关键概念有精确定义

### 步骤

1. 找出项目中**模棱两可的术语**
2. 为每个术语定义**精确含义**
3. 更新 `CONTEXT.md`（或 `TERMS.md`）
4. 对复杂决策写 **ADR**（架构决策记录）

### 为什么重要

```diff
- ❌ "课程中某个章节的一节课被标记为真实"
+ ✅ "物化级联"
```

一个词代替一句话 → Agent 少想 + 少 token + 更一致

> 引导词: **ubiquitous language** — Eric Evans DDD 概念

---

## ③ 拆解 Ticket

**完成标准**: 每个 ticket 有明确的范围、依赖关系、验收标准

### 原则

- **Tracer bullet**: 每个 ticket 是端到端的「曳光弹」——从用户输入到输出走通，而不是分层切割
- **边界声明**: 每个 ticket 标注它阻塞了谁、被谁阻塞
- **大小**: 一个 agent session 能完成的粒度

---

## ④ TDD 实现（红-绿-重构）

**完成标准**: 测试全部通过 + 代码已重构 + 无回归

### 循环

```
🔴 RED   — 写一个失败的测试（定义期望）
🟢 GREEN — 写最少代码让测试通过
🔵 REFACTOR — 重构代码，保持测试绿色
```

### 指南

| 阶段 | 做什么 | 不做什么 |
|:---:|:------|:--------|
| RED | 写业务行为的测试 | 不要测试框架/库/配置 |
| GREEN | 只写能通过的代码 | 不要提前优化 |
| REFACTOR | 改善设计、消除重复 | 不要改行为 |

### 测试类型优先序
1. **行为测试** — 用户可见的功能
2. **边界测试** — 异常输入、极限值
3. **集成测试** — 组件间交互

> 引导词: **red-green-refactor** — TDD 的完整心跳

---

## ⑤ Code Review（双轴审查）

**完成标准**: 两个轴都通过 + 无未解决评论

### 轴 A: 编码标准

- 代码是否符合项目的编码规范？
- 有无 Martin Fowler 代码坏味道？
- 命名是否和领域术语一致？

### 轴 B: Spec 一致性

- 是否忠实实现了需求/spec？
- 有无遗漏的边界情况？
- 有无引入未要求的副作用？

> 两个轴由**子 Agent 并行执行**，互不干扰

---

## ⑥ Bug 诊断

**完成标准**: Bug 已复现 + 根因已定位 + 已修复 + 回归测试通过

### 诊断循环

```
① 复现 ─── 写最小复现步骤
② 最小化 ─── 缩小到最小输入范围
③ 假设 ─── 提出根因假设
④ 验证 ─── 添加日志/断言验证假设
⑤ 修复 ─── 修改代码
⑥ 回归 ─── 确保修复没有引入新问题
```

---

## ⑦ 交接文档

**完成标准**: 另一个 Agent 读完后能无缝继续工作

### 内容

```markdown
# Handoff: [任务名称]

## 已完成
- [x] ...

## 进行中
- [ ] ... (当前状态)

## 决策记录
- ADR: ...

## 上下文加载
- 关键文件: ...
- 下一步: ...
```

---

## 💡 引导词速查

| 引导词 | 含义 | 出处 |
|:---:|:----|:----|
| **grill** | 主动研磨需求直到清晰 | Matt Pocock |
| **red-green-refactor** | TDD 完整循环 | Kent Beck |
| **tracer bullet** | 端到端曳光弹式开发 | 《The Pragmatic Programmer》 |
| **ubiquitous language** | 统一领域语言 | Eric Evans DDD |
| **deep module** | 少接口多行为的模块设计 | John Ousterhout |

## 📚 参考

- [mattpocock/skills](https://github.com/mattpocock/skills) — 原始仓库
- [writing-great-skills](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md) — 元知识
- [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)
- [Domain-Driven Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)
- [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)
