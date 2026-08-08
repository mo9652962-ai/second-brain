---
date: 2026-07-29
tags: [research-tracker, charm, graph, knowledge-graph, multimodal]
source: arXiv 2607.26023v1
status: tracking
priority: 🟡 中（2周内研究）
---

# CHARM 研究跟踪 — 多模态图谱零样本迁移

> 论文：CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer
>
> 核心发现：用层次化图谱上下文替代孤立节点，实现跨域零样本迁移

---

## 核心理念

**「节点在孤立的图中无法泛化 → 用层次化上下文把领域特定模式映射到共享高层概念」**

## 对我们系统的映射

| CHARM 概念 | Second Brain 映射 | 成熟度 |
|-----------|-----------------|-------|
| 多模态节点 | Obsidian 笔记（文本+图片+代码） | ✅ 已有 |
| 层次化图上下文 | MOC 锚点 → 知识域 → 具体笔记 | ✅ 已建7域MOC |
| 跨域零样本迁移 | 不同知识域的概念自动关联 | ❌ 待实现 |
| Graph tokens → LLM | 图谱嵌入注入 prompt | ❌ 待研究 |

## 应用场景

1. **知识发现**：「PCB 设计中的阻抗匹配」↔「MLOps 中的模型 serving 延迟优化」— 都是「匹配问题」，自动关联
2. **跨域搜索**：搜「状态管理」自动关联 React state → Hermes session → Cron job state
3. **自动标签**：新笔记自动匹配到最合适的知识域和 MOC

## 跟踪计划

- [ ] 第 1 周：读懂 CHARM 的层次上下文编码方法
- [ ] 第 2 周：评估 Obsidian 图谱是否可作为 CHARM 的输入
- [ ] 可选：用 graphify 工具做一次知识图谱质量评估

---

*跟踪开始：2026-07-29 | 下次更新：8/5*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
