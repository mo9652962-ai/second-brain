---
tags: [home, moc, hub]
domain: home
created: 2026-07-21
updated: 2026-07-21
---

# 🏠 Second Brain — 知识中枢

> Obsidian + Hermes + GitHub 三方联动
> 我（k）在 Hermes Agent 上读写，你（sora）在这里思考。

## 📊 知识域总览

```dataview
TABLE domain AS "领域", length(filter(file.tags, (t) => !contains(t, "home") AND !contains(t, "moc"))) AS "标签数", updated AS "最后更新"
FROM "knowledge" OR "projects"
WHERE domain
SORT domain ASC
```

### 🆕 新增: [[Programming]] + [[freeCodeCamp]] + [[8051-MCU]] (2026-07-21)
Python 3.14 新特性、AI Agent 架构模式、ReAct/CodeAct 范式、build123d + AI 结合、OpenClaw Skill 开发
**freeCodeCamp**: 451K GitHub Stars 的开源编程教育平台源码研究
**8051-MCU**: 51单片机嵌入式开发全流程 (Keil/SDCC → GPIO/定时器/UART → STC-ISP 烧录) + 新 skill `8051-embedded-dev`

## 📝 最近更新的笔记

```dataview
TABLE file.mtime AS "修改时间", domain AS "领域"
FROM "knowledge" OR "projects" OR "MEMORY"
SORT file.mtime DESC
LIMIT 10
```

---

## 🧭 知识图谱

> 所有 14 个知识域已通过 [[knowledge/Cross-Domain|交叉领域索引 🔀]] 串联
> 每个知识文件底部均有交叉引用链接

```
                        ┌─────────────────┐
                        │    🏠 HOME.MD    │
                        │    知识中枢       │
                        └────────┬────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
     ┌────────────────┐ ┌──────────────┐ ┌─────────────────┐
     │  🤖 AI-Agent   │ │ 🎨 PPT-Design│ │ 📚 Academic     │
     │  k 的能力与架构 │ │  设计与方法论  │ │  检索·阅读·写作  │
     └───────┬────────┘ └──────┬───────┘ └────────┬────────┘
             │                 │                   │
             │         ┌───────┴───────┐           │
             │         │               │           │
             ▼         ▼               ▼           ▼
     ┌────────────┐ ┌────────────────┐ ┌─────────────────┐
     │🔀AI-Workflow│ │ 💻 Vibe-Coding │ │ 📋 projects/    │
     │ Skill编排   │ │  环境·工具·系统 │ │   当前项目状态    │
     └───────┬────┘ └────────────────┘ └─────────────────┘
             │
             ▼
     ┌────────────────┐
     │ 🐍 Programming  │
     │ Python + AI 开发 │
     └────────────────┘
```

---

## 📁 七大知识领域

### 🤖 [[AI-Agent]] — Agent 核心
k 的能力架构、Memory 范式、安全态势、成本优化
- **驱动**: 26 个 skills（9 论文 + 6 PPT + 7 图片 + 3 自改进 + 1 搜索）
- **关联**: → [[AI-Workflow]] · → [[PPT-Design]] · → [[Academic]] · → [[Vibe-Coding]]

### 🔀 [[AI-Workflow]] — Skill 编排与工作流 🆕
Multi-Agent 五大模式、Skill 设计模式、Pipeline 管道、渐进式加载
- **核心**: 让 26 个 Skills 自然精准地联动
- **关联**: → 全部领域（编排层，串联一切）

### 🎨 [[PPT-Design]] — PPT 设计
2026 六大趋势、6 轮制作方法论、行业工具对标
- **驱动**: 6 个 PPT skills 全家桶（v4.0 标准）
- **关联**: → [[AI-Agent]] · → [[AI-Workflow]]（Pipeline 化）· → [[Academic]]

### 📚 [[Academic]] — 学术论文
检索→阅读→写作→SCI 精修全流程、去 AI 化方法论
- **驱动**: 9 个论文 skills 全家桶
- **关联**: → [[AI-Agent]] · → [[AI-Workflow]]（Pipeline 化）· → [[PPT-Design]]

### 🔧 [[CAD-Design]] — CAD 与 3D 建模 🆕
build123d 参数化建模、软件选型、3D打印、学习路径
- **驱动**: cad-design-master skill + 7 个 ClawHub CAD skills
- **关联**: → [[AI-Agent]] · → [[Vibe-Coding]]（Python/Docker 环境）

### 🐍 [[Programming]] — Python 与 AI 开发 🆕
Python 3.14 新特性、AI Agent 架构、ReAct/CodeAct 模式、build123d + AI
- **驱动**: Python 生态 + 7 个 CAD Python 库
- **关联**: → [[AI-Agent]]（Agent 实现）· → [[AI-Workflow]]（代码编排）· → [[CAD-Design]]（build123d）· → [[Vibe-Coding]]（开发环境）· → [[freeCodeCamp]]（编程教育）· → [[8051-MCU]]（嵌入式 C 语言）

### 🏫 [[freeCodeCamp]] — 全球最大开源编程教育平台 🆕
451K Stars · 10 年 · 100K 就业 · Monorepo 架构 · CFSD 认证体系
- **核心**: 开源教育模式、Monorepo 工程实践、课程设计方法论
- **关联**: → [[Programming]]（编程技术栈）· → [[AI-Agent]]（开源协作模式）· → [[AI-Workflow]]（课程流水线设计）· → [[Vibe-Coding]]（开发环境技术栈）

### 💻 [[Vibe-Coding]] — 编程与系统
Windows 环境、PowerShell、搜索工具链、系统维护
- **关联**: → [[AI-Agent]]（运行环境）· → [[PPT-Design]]（生成工具）· → [[Academic]]（写作工具链）· → [[Programming]]（开发环境）

---

## 🔥 交叉领域

| 交叉点 | 涉及领域 | 场景 |
|--------|----------|------|
| **Skill 编排** | [[AI-Workflow]] + 全部 | Pipeline 化、Fan-Out 并行、渐进式加载 |
| **学术 PPT** | [[PPT-Design]] + [[Academic]] | 论文答辩、学术汇报 |
| **AI 变现** | [[AI-Agent]] + 全部 | PPT代做、论文润色、Agent定制 |
| **知识管理** | [[AI-Agent]] + [[Vibe-Coding]] | Obsidian + Git 联动 |

---

## 📋 项目与日志

- **[[projects/current]]** — 所有进行中项目实时状态
- **[[knowledge/Cross-Domain]]** — 交叉领域自动索引（Dataview 驱动）
- **[[Second Brain]]** — Canvas 视觉知识图谱
- **[[MEMORY]]** — k 的长期记忆（curated）
- **[[memory/]]** — 每日原始日志

---

## 🛠 快速入口

| 你想做什么？ | 从这里开始 → |
|-------------|-------------|
| 做 PPT | [[PPT-Design]] → 看趋势 + 方法论 |
| 写论文 | [[Academic]] → 选对应 skills |
| 联动多个 Skills | [[AI-Workflow]] → Pipeline 编排指南 |
| 配置 Agent | [[AI-Agent]] → 配置要点 |
| 修系统问题 | [[Vibe-Coding]] → 系统维护 |
| 看进度 | [[projects/current]] |
| 查经验 | [[MEMORY]] |

---

## 📊 自动索引

### 知识域概览

```dataview
TABLE domain AS "领域", tags AS "标签", updated AS "最后更新"
FROM "knowledge"
WHERE domain
SORT domain ASC
```

### 最近修改

```dataview
TABLE file.mtime AS "修改时间", domain AS "领域"
FROM "knowledge" OR "projects" OR "memory"
SORT file.mtime DESC
LIMIT 10
```

### 所有标签

```dataview
TABLE rows.file.link AS "笔记"
FROM -"templates"
FLATTEN tags AS tag
GROUP BY tag
SORT tag ASC
```

### 孤立笔记（无反向链接）

```dataview
TABLE file.folder AS "位置"
FROM -"templates"
WHERE length(file.inlinks) = 0 AND file.name != "HOME"
SORT file.folder ASC
```

### 项目状态

```dataview
TABLE status AS "状态", updated AS "最后更新"
FROM "projects"
WHERE domain = "project"
SORT status ASC, updated DESC
```

| 指标 | 数值 |
|------|------|
| Skills 总量 | 26 |
| 知识库文件 | 6 领域 + 1 中枢 |
| 编排模式 | 5 大 Multi-Agent + 5 大 Skill 设计 |
| 记忆文件 | MEMORY + SESSION-STATE + 每日日志 |
| 学习记录 | 8 错误 + 22 经验 (learnings/) |
| Git 备份 | github.com/mo9652962-ai/second-brain |

---

_由 Obsidian + k (Hermes) 共同维护 | 最后更新: 2026-07-23_
