---
tags: [research, skills, authoring, best-practices, optimization]
created: 2026-08-12
type: research
---

# Skill 编写最佳实践 · 2026 千轮研究

> 研究于 2026-08-12：Agent Skills 规范 / Anthropic / Red Hat ACE / Microsoft / 社区实践

## 结论置顶

**Skill 的 description 是唯一触发入口，必须写触发词而非摘要；SKILL.md 需渐进披露（<500行），确定性工作给脚本而非模型推理。**

## 核心原则

### 1. Description 的唯一职责是触发
- 30-55 词，包含**具体触发词**（用户会说的短语）
- 加"Do not use this for X"负向约束
- 不是摘要——不要总结技能内容，模型会跳过 SKILL.md
- **触发词测试**：写5个 should/shouldn't 触发用例

### 2. 渐进披露三层
- **L1（metadata）**：~100 tokens，仅 description 在系统提示
- **L2（SKILL.md）**：<5000 tokens 推荐，完整指导
- **L3（reference 文件）**：按需加载，告诉模型何时读

### 3. 脚本 > 推理
- 确定性工作（格式化/验证/数据抓取）用脚本
- 推理工作（主观评估/策略/异常处理）留在 SKILL.md
- 脚本用 Python stdlib + PEP-723

### 4. 聚焦 1-3 技能/任务
- 超过产生认知过载和冲突指令
- 宁用 1 个技能 + 3 个 reference 文件，不用 3 个相似技能

### 5. 关键模式
- **Gotchas 节**——最高价值内容（环境特定修正）
- **模板（Templates）**——比 prose 描述更可靠
- **验证循环**——做完→验证→修→重复
- **计划-验证-执行**——批处理/破坏性操作先出计划

## 升级清单（已执行）

| 技能 | 升级 |
|:---|:---|
| ai-api-provider-evaluation | 描述优化（触发词+负向约束）|
| knowledge-absorption | 描述优化（触发词+动作）|
| service-quality | 描述优化 |
| xianyu-monetization | 描述优化 |
| hermes-harness-profile | 描述优化 |
| english-practice-machine-dev | 描述优化 |
| vocabulary-data-pipeline | 描述优化 |
| self-improving-agent | 5 节 ACL 2026 研究（前序轮次）|

## 来源

- Agent Skills 规范: agentskills.io/skill-creation/best-practices
- Red Hat ACE: building-skills-for-ai-agents
- Anthropic: Complete Guide to Building Skills for Claude
- smcleod: Writing and Reviewing Agent Skills
- Microsoft: Agent Skills