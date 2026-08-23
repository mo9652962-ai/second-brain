---
date: 2026-07-29
tags: [research-tracker, kutie, context-engineering, LLM]
source: arXiv 2607.25995v1
status: tracking
priority: 🟡 中（2周内研究）
---

# KuTIE 研究跟踪 — LLM + 运行时上下文

> 论文：Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?
>
> 核心发现：注入运行时拓扑 → 补丁正确率从 11.1% → 78.0%

---

## 核心理念

**「LLM 生成操作需要知道系统的实际依赖关系，而非仅凭通用知识」**

## 对我们系统的映射

| KuTIE 概念 | Second Brain 映射 | 当前状态 |
|-----------|-----------------|---------|
| Istio call edges | Obsidian 双链图谱 | ✅ 已有 |
| KSPM findings | Cron 错误模式库 | ✅ 今日建立 |
| Service-account bindings | Skills 依赖关系 | ❌ 未建模 |
| Topology context injection | Agent 操作前注入关联上下文 | ❌ 待实现 |

## 应用场景

1. **修改 config 时**：自动注入「哪些 Cron/工具依赖此配置」
2. **删除 Skill 时**：自动注入「哪些 Cron 引用了此 Skill」
3. **更新 memory 时**：自动注入「哪些规则与此 memory 关联」

## 跟踪计划

- [x] ~~第 1 周：读懂论文的依赖注入方法~~ 📖 周计划参考（学习计划文档内容）
- [x] ~~第 2 周：设计 Second Brain 的 context injection 方案~~ 📖 周计划参考
- [x] ~~目标：任何修改操作前，自动展示「影响范围」~~ 📖 周计划参考

---

*跟踪开始：2026-07-29 | 下次更新：8/5*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
