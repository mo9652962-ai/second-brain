# Negative Results Registry — 阴性结果登记册（Hermes 适配版）

> 来源：redamancy231-create/negative-results-registry (CC BY 4.0)
> 用途：对抗"文件抽屉问题"——记录"试了没效果"，与 ERRORS.md（记录修复成功）互补
> 适配：2026-07-31 落地到 .learnings 体系

## 为什么需要

我们的 ERRORS.md 记录了"错误 → 修复"（56 条），但**漏掉了"尝试 → 无效"**的阴性结果：
- 试了某个 prompt 方案，效果没提升 → 没记录
- 换了某个工具，反而更差 → 没记录
- 某个方法在特定任务上不 work → 没记录

这些"知道死胡同在哪"的信息，价值不低于"知道路在哪"。

## 记录模板（字段对齐 NRR Schema，简化适配）

```markdown
## [NRR-YYYYMMDD-NNN] 一句话标题（阴性）

**Logged**: YYYY-MM-DDTHH:MM:SS+08:00
**Status**: recorded
**Domain**: 领域（prompt-engineering/code-review/tool-eval/workflow/other）
**Category**: null-result | ceiling-effect | worse-than-baseline | failed-to-replicate | methodology-failure | abandoned-dead-end | hypothesis-falsified | tool-unfit-for-purpose

### Hypothesis（假设，可证伪）
我认为 X 比 Y 在 Z 指标上提高 N%。

### Method（方法，可复核）
- 实验设计/对比基线
- 模型/工具及版本
- 样本描述

### Expected vs Actual
- **预期**: 假设成立时应观察到什么
- **实际**: 实际观察到什么

### Interpretation（解读）
- 证据支持的解释 vs 替代解释/混杂因素

### Lessons Learned（教训，1-3 条）
1. ...

### Source
- 来源项目/任务:
- 证据链接（数据/代码/日志）:
```

## 三条证据门槛

1. **假设可证伪**：不能是"我想试试 X"，必须是"我认为 X 比 Y 在 Z 上提高 N%"
2. **方法可复核**：有模型/工具版本、样本描述、评价指标
3. **证据可追溯**：至少一个链接指向原始数据/代码/日志

## 分类速查

| 类型 | 含义 | 示例 |
|------|------|------|
| null-result | 零结果：无显著差异 | prompt 三段式 vs 单段 d≈0.03 |
| ceiling-effect | 天花板效应：基线已很好 | C++ 加速单步 53x 但端到端被 Amdahl 限制 2.2x |
| worse-than-baseline | 劣于基线 | 换方案后反而更差 |
| failed-to-replicate | 复现失败 | 换模型后结果不一致 |
| methodology-failure | 方法失败：设计本身有问题 | 无法产生可信结论 |
| abandoned-dead-end | 死胡同：成本/数据导致放弃 | 不是方法错，是外部因素 |
| hypothesis-falsified | 假设被证伪 | 数据否定了假设 |
| tool-unfit-for-purpose | 工具不适用 | 某工具在特定任务上失败 |

## 记录时机（触发条件）

- [ ] 实验/尝试完成但效果未达预期（无论大小）
- [ ] 换工具/方案后没有改善或更差
- [ ] 发现某方法在特定场景不适用
- [ ] 复盘时发现"当时试过 X 不行"但没记录

---

# 已登记条目

## [NRR-20260731-001] jcode — Rust Agent harness 因 SAC 封杀被评估为不适用

**Logged**: 2026-07-31T22:00:00+08:00
**Status**: recorded
**Domain**: tool-eval
**Category**: abandoned-dead-end

### Hypothesis
jcode（Rust 内存高效 Agent harness）能替代 opencode-go 作为 Hermes 的执行后端，降低内存占用。

### Method
- 评估：GitHub 项目研究（star 14.5k）+ 社区讨论
- 发现：该项目被 SAC（某安全组织）封杀
- 上下文：2026-07 工具评估期间

### Expected vs Actual
- **预期**: 内存占用更低，可作为轻量 harness 使用
- **实际**: 项目被 SAC 封杀，存在合规/安全风险，评估终止

### Interpretation
封杀原因与项目性质相关，继续使用有未知风险。这不是方法失败，而是外部因素（安全组织裁定）导致的方向放弃——典型死胡同。

### Lessons Learned
1. 工具评估不只看 star 和技术，还要查安全/合规状态
2. abandoned 结论要记录完整评估过程（三态更新：adopted→abandoned + 原因）

### Source
- 来源任务: 2026-07 GitHub Trending 工具评估
- 证据链接: https://github.com/1jehuang/jcode（已存档至 knowledge/Research/）

---
*第一条登记 · 2026-07-31 回填*

## 与现有体系的关系

| 现有 | 互补关系 |
|------|---------|
| ERRORS.md | ERRORS 记"错误+修复"（阳性），NRR 记"尝试+无效"（阴性） |
| LEARNINGS.md | LEARNINGS 记经验教训，NRR 记原始实验证据 |
| 规则 #23 踩坑速查 | 规则 #23 是抽象后的通用规则，NRR 是原始个案记录 |
| 知识吸收流程 | 工具评估三态（adopted/trialed/abandoned）→ abandoned 时写 NRR |

---
*2026-07-31 · negative-results-registry 适配版模板*
