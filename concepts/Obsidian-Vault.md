---
tags: [concepts, obsidian, vault, knowledge-management]
aliases: [Vault 使用指南]
created: 2026-07-26
---

# Obsidian Vault — 使用指南与双轨记忆策略

> 本仓库是 OpenClaw 遗产 + Obsidian 二合一的长期知识库。

## 双轨记忆策略

| 机制 | 用途 | 特点 |
|------|------|------|
| Hermes Memory 内置 | 跨会话上下文保持 | 自动 recall，无需手动管理 |
| Obsidian Vault | 长期/结构化知识 | 手工 curated，面向知识图谱 |

## 仓库结构

- `knowledge/` — 按领域组织的知识笔记（AI/Academic/Design/Dev/Hardware/Productivity）
- `memory/` — 每日日志与周报（`YYYY/MM/` 分层）
- `projects/` — 项目状态追踪
- `pipelines/` — 工作流 Pipeline
- `concepts/` — 跨领域概念笔记
- `templates/` — 笔记模板
- `.learnings/` — 架构决策 + 错误记录

## 使用规范

1. 知识笔记写入 `knowledge/` 对应目录
2. 每日日志写入 `memory/YYYY/MM/`
3. 交叉引用使用 `[[wikilink]]` 语法
4. 标签使用小写连字符格式（如 `#ai-Agent`）
5. 新知识吸收后更新 `knowledge/knowledge-map.md`
