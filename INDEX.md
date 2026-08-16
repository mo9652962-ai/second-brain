---
tags: [MOC, index, vault-guide]
domain: home
created: 2026-07-25
updated: 2026-08-16
---

# 🗺️ vault 全局关联网

> 这里是 Obsidian 仓库的完整结构图，从 HOME 出发，串联所有知识。
> 2026-08-15 更新：知识域收敛至 7 个子域（10→7 合并：Research/Academic、Dev/AI、Hardware/Design）。

## 入口 → 所有节点

```
                ┌───────────────────────────────┐
                │          🏠 HOME.md           │
                │      知识中枢 · MOC 索引       │
                └──────────────┬────────────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
      ┌────────────┐   ┌──────────────┐   ┌───────────┐
      │ 📚 知识域  │   │ 📋 项目      │   │ 🧩 系统    │
      │ 7 个子域   │   │ projects/    │   │ 配置/脚本  │
      │ 690+ 笔记  │   │ 知识点       │   │ 文档/模板  │
      └─────┬──────┘   └──────────────┘   └─────┬─────┘
            │                                   │
            ▼                                   ▼
  knowledge/ 7 域                 system/ docs/ scripts/
  (含 knowledge-map.md MOC)       templates/ playbooks/
```

## 核心入口

| 节点 | 作用 |
|:---|:---|
| [[HOME]] | 知识中枢 · MOC 索引 · 最近更新 |
| [[INDEX]] | 本文件 · vault 全局关联网 |
| [[knowledge/knowledge-map]] | 知识域 → 笔记的完整映射（最新维护） |
| [[MEMORY]] | 持久记忆（用户偏好/环境/教训） |
| [[CHANGELOG]] | 变更记录 |

## 知识域清单（knowledge/ 7 个子域，2026-08-15 收敛：10→7）

| 子域 | 内容 |
|:---|:---|
| Research | 研究+学术（原 Research/Academic 合并） |
| Dev | 开发+AI（原 Dev/AI 合并） |
| Hardware | 硬件+设计（原 Hardware/Design 合并） |
| Productivity | 效率 |
| Daily | 每日记录 |
| cards | 知识卡片 |
| Archive | 归档 |
| Cross-Domain.md | 跨域链接 |

## 项目与系统

| 目录 | 内容 |
|:---|:---|
| projects/ | 进行中项目 |
| memory/ | 记忆体系 |
| system/ | 系统配置 |
| docs/ | 文档 |
| scripts/ | 自动化脚本 |
| templates/ | 模板 |
| pipelines/ | 流水线 |
| traces/ | 轨迹记录 |
| health/ | 健康检查 |
| site/ | 站点相关 |
| concepts/ | 概念笔记 |
| research/ | 研究追踪器（trackers/，arXiv 长期追踪） |
| outputs/ | 输出产物 |
| mcp/ | MCP 配置 |
| skills/ | 技能 |
| portfolio/ | 作品集 |

## 维护说明

1. 新研究笔记写入 `knowledge/Research/`（文件名含日期）
2. 每批次研究后更新 `knowledge/knowledge-map.md` 挂载 MOC（防孤立节点）
3. 标签规范：`research / github / article-study / methodology / digest` 等
4. 自动同步：git push → GitHub (mo9652962-ai/second-brain)，gh-pages MkDocs 部署
