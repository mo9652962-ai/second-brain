---
tags: [home, MOC, hub]
domain: home
created: 2026-07-21
updated: 2026-07-28
---

# 🏠 Second Brain — 知识中枢

> Obsidian + Hermes + GitHub 三方联动
> 知识库已按域分类整理（2026-07-26 v2 维护完成 | W30 周学习总结已归档）

## 📊 知识域总览

```dataview
TABLE domain AS "领域", length(filter(file.tags, (t) => !contains(t, "home") AND !contains(t, "moc"))) AS "标签数", updated AS "最后更新"
FROM "knowledge"
WHERE domain
SORT domain ASC
```

## 📝 最近更新的笔记

```dataview
TABLE file.mtime AS "修改时间", domain AS "领域"
FROM "knowledge" OR "projects" OR "memory"
SORT file.mtime DESC
LIMIT 10
```

## 🔧 最近维护

- [[memory/2026/07/2026-07-28-maintenance|2026-07-28 维护报告]] — 仓库健康检查 + 孤立笔记链接
- [[memory/2026/07/2026-07-27-maintenance|2026-07-27 维护报告]] — 仓库健康检查：全部通过
- [[memory/2026/07/2026-07-26-maintenance|2026-07-26 维护报告]] — 结构优化 v2 + 批量链接修复

---

## 🧭 知识图谱

```
                        ┌─────────────────┐
                        │    🏠 HOME.md    │
                        │    知识中枢       │
                        └────────┬────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
     ┌────────────────┐ ┌──────────────┐ ┌─────────────────┐
     │  🤖 AI/        │ │ 🎨 Design/   │ │ 📚 Academic/    │
     │  Agent·工作流   │ │  PPT·美化·工具 │ │  论文·变现       │
     └───────┬────────┘ └──────┬───────┘ └────────┬────────┘
             │                 │                   │
             ▼                 ▼                   ▼
     ┌────────────────┐ ┌────────────────┐ ┌─────────────────┐
     │ 🔧 Hardware/   │ │ 💻 Dev/        │ │ 📋 项目          │
     │ CAD·PCB·8051    │ │ Python·Web·系统 │ │   当前项目状态    │
     └────────────────┘ └────────────────┘ └─────────────────┘
```

---

## 📁 六大知识域

### 🤖 [[knowledge/AI/AI-Agent|AI]] — Agent 核心
AI 能力架构、Skill 编排、模型供应商策略、Vibe Research
- **包含**: AI-Agent · AI-Workflow · LLM-Providers · vibe-research · reverse-prompting · github-projects-note
- **关联**: → Academic → Design → Hardware

### 📚 [[knowledge/Academic/Academic|Academic]] — 学术论文与变现
论文检索、阅读、写作、去AI化、闲鱼接单定价策略
- **包含**: Academic · ai-monetization-costs · academic-service-research · [[paper-pipeline-data-contract|论文 Pipeline 数据契约]]
- **关联**: → AI(AI-Agent) → Design(PPT)

### 🎨 [[knowledge/Design/PPT-Design|Design]] — PPT 与视觉设计
2026 设计趋势、工具选型、AI 辅助设计
- **包含**: PPT-Design · desktop-beautify · ai-tools-reference
- **关联**: → Academic(论文PPT) → AI(AI-Workflow)

### 🔧 [[knowledge/Hardware/CAD-Design|Hardware]] — 硬件设计
CAD 3D建模、PCB 设计、8051 单片机
- **包含**: CAD-Design · pcb-design-notes · 8051-MCU · CAD-Project-Postmortem · opencut
- **关联**: → Dev(编程) → AI(Agent控制)

### 💻 [[knowledge/Dev/Programming|Dev]] — 开发
Python、Web 开发、系统设计、编程教育
- **包含**: Programming · freeCodeCamp · campus-box-design · web-dev-2026 · system-design-primer · grok-build · mattpocock-*
- **关联**: → Hardware(嵌入式) → AI(Agent开发)

### 🏠 [[knowledge/Productivity/obsidian-tips|Productivity]] — 效率工具
Obsidian 笔记系统、效率插件
- **包含**: obsidian-tips · [[knowledge/Productivity/token-usage-report-20260727|Token 使用报告]]
- **关联**: → 全部域（元知识）

---

## 🔥 交叉领域

| 交叉点 | 涉及领域 | 场景 |
|--------|----------|------|
| **AI 变现** | Academic + Design + AI | 闲鱼 PPT/论文/PCB 接单 |
| **学术PPT** | Design + Academic | 论文答辩、学术汇报 |
| **嵌入式开发** | Hardware + Dev | 单片机+PCB+编程 |
| **Skill 编排** | AI + 全部 | Pipeline 化、并行、渐进式加载 |

---

## 📋 项目与日志

- **[[projects/current]]** — 所有进行中项目实时状态
- **[[knowledge/Cross-Domain]]** — 交叉领域自动索引
- **[[INDEX]]** — 🗺️ vault 全局关联网
- **[[MEMORY]]** — k 的长期记忆
- **[[memory/2026/07/2026-07-26-review|memory/2026/07]]** — 每日原始日志（按年月分层，近期回顾可见）
- **[[memory/2026/07/2026-07-27-daily-cleanup|今日清理报告]]** — 每日清除记录 (07-27)
- **[[memory/2026/07/2026-07-27-todo-cleanup|今日 TODO 清理]]** — TODO 扫描与归档 (07-27)

### 🧩 散落知识点关联网

```
HOME.md ──→ 每个知识域（6域）
     │
     ├──→ pipelines/          工作流Pipeline（论文·PPT·Skill触发）
     ├──→ projects/           项目进度追踪
     ├──→ templates/          笔记模板（每日·通用）
     ├──→ .learnings/         错误与经验记录
     ├──→ knowledge/Cross-Domain  交叉域索引
     ├──→ knowledge/knowledge-map 知识图谱
     ├──→ working-buffer      工作暂存区
     └──→ hermes-session      会话记录
```

| 入口 | 位置 | 说明 |
|:-----|:-----|:------|
| 📊 **工作流** | [[pipelines/pipeline-overview|pipelines/]] | 论文·PPT·Skill 触发工作流 |
| 📈 **项目** | [[projects/current]] | 当前项目状态与进度 |
| 📝 **模板** | [[templates/每日笔记模板|templates/]] | 每日笔记/通用笔记模板 |
| 🧠 **学习** | [[.learnings/LEARNINGS]] | 架构决策 + 最佳实践 |
| ❌ **错误** | [[.learnings/ERRORS]] | 踩坑记录与修复方案 |
| 🗺️ **知识图谱** | [[knowledge/knowledge-map]] | vault 全局知识图谱 |
| 🔀 **交叉域** | [[knowledge/Cross-Domain]] | 跨域自动索引 |
| 📝 **缓冲** | [[memory/working-buffer]] | 临时工作笔记 |

---

## 🛠 快速入口

| 你想做什么？ | 从这里开始 → |
|-------------|-------------|
| 做 PPT | [[knowledge/Design/PPT-Design|Design]] → 看趋势 + 方法论 |
| 写论文 | [[knowledge/Academic/Academic|Academic]] → 选对应 skills |
| 画 PCB | [[knowledge/Hardware/pcb-design-notes|pcb-design]] → 加载 skill |
| 配置 Agent | [[knowledge/AI/AI-Agent|AI]] → 配置要点 |
| 看进度 | [[projects/current]] |
| 查经验 | [[MEMORY]] |

---

## 📊 自动索引

### 所有笔记

```dataview
TABLE file.folder AS "位置", updated AS "更新"
FROM "knowledge"
SORT file.folder ASC
```

### 最近修改

```dataview
TABLE file.mtime AS "修改时间", file.folder AS "位置"
FROM "knowledge" OR "projects" OR "memory"
SORT file.mtime DESC
LIMIT 10
```

### 孤立笔记（无反向链接）

```dataview
TABLE file.folder AS "位置"
FROM -"templates"
WHERE length(file.inlinks) = 0 AND file.name != "HOME"
SORT file.folder ASC
```

### vault 统计

| 指标 | 数值 |
|------|------|
| 知识域 | 6 域 + 1 中枢 |
| knowledge 文件 | ~25 篇 |
| Skills 生态 | 93 全活跃 |
| 记忆系统 | MEMORY + 每日日志 |
| Git 备份 | github.com/mo9652962-ai/second-brain |

---

_由 Obsidian + k (Hermes) 共同维护 | 2026-07-25 结构优化完成_
