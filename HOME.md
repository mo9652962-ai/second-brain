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

- **[[skills/hermes/hermes-workflow-preferences|用户交互规则 v1.0]]** — 凌晨/深夜构建需求最小确认机制，防止 1 小时全归零
- **[[skills/hermes/hermes-automation-patterns|Cron 自动化模式 v1.1]]** — 网络任务错峰调度 + 自动重试脚本，避免批量失败
- **[[skills/hermes/daily-knowledge-absorption-gate|知识吸收守门人 v1.0]]** — 每日至少 1 个主动吸收底线 + 5 分钟快速吸收选项库
- [[memory/2026/07/2026-07-28-maintenance-3|2026-07-28 维护报告 #3]] — 深度链接修复 + 孤立笔记整合
- [[memory/.archive/maintenance/2026-07-28-maintenance-2|2026-07-28 维护报告 #2]] — 新增孤立笔记链接（已归档）
- [[memory/2026/07/2026-07-28-maintenance|2026-07-28 维护报告]] — 仓库健康检查 + 孤立笔记链接
- [[memory/2026/07/2026-07-31-maintenance|2026-07-31 维护报告]] — 链接修复 + 空文件清理
- [[memory/2026/07/2026-07-30-reflection|🪞 反思日记 07-30]] — 7/30 任务完成与知识吸收回顾
- [[memory/2026/08/2026-08-02-maintenance|2026-08-02 维护报告]] — 空壳清理 + 游离日志归位 + 推送分支修复
- [[memory/2026/08/weekly-2026-08-02|📚 W31 周度整理报告]] — 13 文件归域 + Research MOC 创建 + 47 孤儿补链
- [[knowledge/Research/MOC-Research|🔬 Research MOC 创建]] — 36 篇研究笔记索引化（W31 新建）
- [[docs/WPS数学练习册标准化优化指南|WPS 数学练习册标准化指南]] — 排版规范参考
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
     │ 🔧 Hardware/   │ │ 💻 Dev/        │ │ 🏠 Productivity/│
     │ CAD·PCB·8051    │ │ Python·Web·系统 │ │  效率·工具       │
     └────────────────┘ └────────────────┘ └────────┬────────┘
                                                     │
                                                     ▼
                                             ┌─────────────────┐
                                             │ 🤖 Hermes/      │
                                             │  Agent 自举·进化  │
                                             └─────────────────┘
```

---

## 📁 七大知识域

### 🤖 [[knowledge/AI/AI-Agent|AI]] — Agent 核心
AI 能力架构、Skill 编排、模型供应商策略、Vibe Research
- **包含**: AI-Agent · AI-Workflow · LLM-Providers · vibe-research · reverse-prompting · [[github-projects-note|DeepTutor 学习笔记]]
- **MOC**: [[knowledge/AI/MOC-AI|🗺️ AI MOC]]
- **关联**: → Academic → Design → Hardware

### 📚 [[knowledge/Academic/Academic|Academic]] — 学术论文与变现
论文检索、阅读、写作、去AI化、闲鱼接单定价策略
- **包含**: Academic · ai-monetization-costs · academic-service-research · [[paper-pipeline-data-contract|论文 Pipeline 数据契约]]
- **MOC**: [[knowledge/Academic/MOC-Academic|🗺️ Academic MOC]]
- **关联**: → AI(AI-Agent) → Design(PPT)

### 🎨 [[knowledge/Design/PPT-Design|Design]] — PPT 与视觉设计
2026 设计趋势、工具选型、AI 辅助设计
- **包含**: PPT-Design · desktop-beautify · ai-tools-reference
- **MOC**: [[knowledge/Design/MOC-Design|🗺️ Design MOC]]
- **关联**: → Academic(论文PPT) → AI(AI-Workflow)

### 🔧 [[knowledge/Hardware/CAD-Design|Hardware]] — 硬件设计
CAD 3D建模、PCB 设计、8051 单片机
- **包含**: CAD-Design · pcb-design-notes · 8051-MCU · CAD-Project-Postmortem · opencut
- **MOC**: [[knowledge/Hardware/MOC-Hardware|🗺️ Hardware MOC]]
- **关联**: → Dev(编程) → AI(Agent控制)

### 💻 [[knowledge/Dev/Programming|Dev]] — 开发
Python、Web 开发、系统设计、编程教育
- **包含**: Programming · freeCodeCamp · campus-box-design · web-dev-2026 · system-design-primer · grok-build · mattpocock-*
- **关联**: → Hardware(嵌入式) → AI(Agent开发)

### 🏠 [[knowledge/Productivity/obsidian-tips|Productivity]] — 效率工具
Obsidian 笔记系统、效率插件
- **包含**: obsidian-tips · [[knowledge/Productivity/token-usage-report-20260727|Token 使用报告]] · [[knowledge/Productivity/ai-blogger-10round-research|AI博主10轮研究]] · [[knowledge/Tools/hermes-agent-ecosystem|🔧 工具生态]]
- **MOC**: [[knowledge/Productivity/MOC-Productivity|🗺️ Productivity MOC]]
- **关联**: → [[knowledge/AI/MOC-AI|AI 域]] · [[knowledge/Dev/python-ecosystem|Python 生态]] · 全部域（元知识）

### 🤖 [[skills/hermes/hermes-workflow-preferences|Hermes]] — Agent 自身进化
Hermes 工作流优化、Cron 自动化、交互规则沉淀（自举域）
- **包含**: hermes-workflow-preferences · hermes-automation-patterns · daily-knowledge-absorption-gate
- **关联**: → 全部域（Agent 方法论）· Productivity（效率工具）

### 🔬 [[knowledge/Research/MOC-Research|Research]] — 外部调研
web 研究、GitHub 热榜、深度调研的落地笔记（W31 新建域）
- **包含**: MOC-Research · 36 篇研究笔记（日报热榜/深度研究/文章研究/工具部署）
- **关联**: → AI → Academic → 全部域（learn→research→apply）


---

## 🔥 交叉领域

| 交叉点 | 涉及领域 | 场景 |
|--------|----------|------|
| **AI 变现** | Academic + Design + AI | 闲鱼 PPT/论文/PCB 接单 |
| **学术PPT** | Design + Academic | 论文答辩、学术汇报 |
| **嵌入式开发** | Hardware + Dev | 单片机+PCB+编程 |
| **Skill 编排** | AI + 全部 | Pipeline 化、并行、渐进式加载 |
| **Agent 自举** | Hermes + Productivity | 用 Hermes 改进 Hermes 自身

---

## 📋 项目与日志

- **[[projects/current]]** — 所有进行中项目实时状态
| **[[knowledge/Cross-Domain]]** — 交叉领域自动索引
| **[[knowledge/arxiv-digest|arXiv 周报]]** — 15 篇 AI Agent/LLM 论文速览 (07-28)
- **[[INDEX]]** — 🗺️ vault 全局关联网
- **[[MEMORY]]** — k 的长期记忆
- **[[memory/2026/07/2026-07-26-review|memory/2026/07]]** — 每日原始日志（按年月分层，近期回顾可见）
- **[[memory/2026/07/2026-07-27-daily-cleanup|今日清理报告]]** — 每日清除记录 (07-27)
- **[[memory/2026/07/2026-07-27-todo-cleanup|今日 TODO 清理]]** — TODO 扫描与归档 (07-27)
- **[[memory/2026/07/github-trending-w30|GitHub W30 周报]]** — 07-20 热榜速览
- **[[memory/2026/07/github-trending-w31|GitHub W31 周报]]** — 07-27 热榜速览
|- **[[memory/2026/07/github-trending-w31-v2|GitHub W31 评估]]** — W31 项目研究与应用评估
|- **[[knowledge/arxiv-2026-07-30-core-contributions|arXiv 今日速览]]** — AI Agent 核心贡献 (07-30)
|- **[[knowledge/Daily/hackernews-2026-07-30|HN 今日热点]]** — Hacker News 热门 (07-30)
|- **[[knowledge/Research/10-Top-AI-Agent-Projects-Deep-Research|AI Agent 项目深度研究]]** — Top10 调研
|- **[[knowledge/Research/Memvid-n8n-kaeru-Deep-Research|Memvid/n8n/kaeru 深度研究]]** — 自动化工具调研
|- **[[memory/2026/07/2026-07-30-maintenance|今日维护报告]]** — 仓库健康检查 (07-30)
|- **[[memory/2026/07/2026-07-30-daily-review|今日回顾]]** — 07-30 知识吸收回顾
|- **[[memory/2026/07/2026-07-30-daily-todo-cleanup|今日 TODO 清理]]** — 07-30 待办扫描
|- **[[memory/2026/07/cron-improvement-plan|Cron 改进计划]]** — 自动任务优化方案
|- **[[research/hermes-mcp-architecture|Hermes MCP 架构调研]]** — MCP 代理架构研究
|- **[[system/GitHub-Treasure-Hunt-System|GitHub 宝藏系统]]** — 开源探索方法论
|- **[[research/trackers/charm-graph-transfer|charm-graph 迁移追踪]]** — 代码图谱跟踪
|- **[[research/trackers/kutie-context-injection|kutie 上下文注入追踪]]** — 上下文管理研究
|- **[[research/trackers/long-term-model-systems|长期模型系统追踪]]** — 模型演进跟踪
|- **[[playbooks/browserbase-evaluation|Browserbase 评估]]** — 浏览器自动化评估
|- **[[playbooks/camofox-docker-setup|Camofox Docker 搭建]]** — Docker 部署方案
|- **[[playbooks/web-scraping-cron-template|Web Scraping Cron 模板]]** — 自动化爬虫模板
|- **[[knowledge/Python/Awesome-Lists-Study|Awesome Lists 研究]]** — Python 精品列表学习
|- **[[memory/2026/07/2026-07-31-daily-review|今日回顾]]** — 07-31 知识吸收回顾
|- **[[memory/2026/07/2026-07-31-daily-todo-cleanup|今日 TODO 清理]]** — 07-31 待办扫描
|- **[[memory/2026/07/2026-07-31-xianyu-todo-executor|闲鱼待办执行]]** — 07-31 闲鱼任务执行
|- **[[memory/2026/08/2026-08-01-daily-review|今日回顾]]** — 08-01 知识吸收回顾
|- **[[memory/2026/08/2026-08-01-daily-todo-cleanup|今日 TODO 清理]]** — 08-01 待办扫描
|- **[[memory/2026/08/2026-08-01-todo-cleanup|TODO 清理]]** — 08-01 补充待办扫描
|- **[[memory/2026/08/2026-08-01-reflection|反思日记]]** — 08-01 自我反思
|- **[[memory/2026/08/2026-08-02|今日日志]]** — 08-02 自我完善记录
|- **[[health/HEALTH_REPORT-2026-08-01|系统健康报告]]** — 08-01 健康检查
|- **[[research/arxiv-weekly-2026-08-02|arXiv 周报]]** — 08-02 论文速览
|- **[[memory/2026/08/2026-08-02-maintenance|今日维护报告]]** — 仓库健康检查 (08-02)
|- **[[memory/2026/08/weekly-2026-08-02|W31 周度整理报告]]** — 本周知识库整合
|- **[[knowledge/Research/MOC-Research|🔬 研究域 MOC]]** — 36 篇研究笔记索引
|- **[[knowledge/Daily/hackernews-2026-08-02|HN 今日热点]]** — Hacker News 热门 (08-02)
|- **[[knowledge/cards/2026-08-02-eu-ai-act|EU AI Act 生效卡片]]** — 今日法规生效精选
|- **[[knowledge/Research/GitHub-Weekly-2026-08-02|GitHub 宝藏挖掘]]** — 08-02 周报
|- **[[knowledge/AI/deepseek-v4-flash-0731-upgrade|DeepSeek V4 Flash 升级]]** — 模型能力跃升
|- **[[knowledge/Hardware/jlc-mcp-setup|JLCPCB MCP]]** — 嘉立创 EDA AI 自动化
|- **[[memory/2026/08/2026-08-02-daily-review|今日回顾]]** — 08-02 知识吸收回顾
|- **[[memory/2026/08/2026-08-02-todo-cleanup|今日 TODO 清理]]** — 08-02 待办扫描
|- **[[memory/2026/08/github-trending-w31-v3|GitHub W31 周报 v3]]** — 08-02 weekly 口径
|- **[[memory/2026/08/2026-08-03-research-apply|每日研究应用]]** — 08-03 learn→research→apply
|- **[[memory/2026/08/2026-08-03-todo-cleanup|今日 TODO 清理]]** — 08-03 待办落实
|- **[[memory/2026/08/2026-08-03-maintenance|今日维护报告]]** — 仓库健康检查 (08-03)
|- **[[knowledge/Daily/hackernews-2026-08-03|HN 今日热点]]** — Hacker News 热门 (08-03)
|- **[[memory/2026/08/2026-08-03-daily-review|今日回顾]]** — 08-03 知识吸收回顾
|- **[[memory/2026/08/2026-08-03-xianyu-todo-executor|闲鱼待办执行]]** — 08-03 闲鱼任务执行
|- **[[memory/2026/08/2026-08-04-maintenance|今日维护报告]]** — 仓库健康检查 (08-04)
- **[[memory/2026/08/2026-08-05-maintenance|今日维护报告]]** — 仓库健康检查 (08-05)
- **[[memory/2026/08/2026-08-03-reflection|反思日记]]** — 08-03 自我反思
- **[[memory/2026/08/2026-08-04-daily-review|今日回顾]]** — 08-04 知识吸收回顾
- **[[memory/2026/08/2026-08-04-todo-cleanup|今日 TODO 清理]]** — 08-04 待办扫描
- **[[memory/2026/08/2026-08-04-xianyu-todo-executor|闲鱼待办执行]]** — 08-04 闲鱼任务执行
- **[[memory/2026/08/2026-08-05-daily-review|今日回顾]]** — 08-05 知识吸收回顾
- **[[memory/2026/08/2026-08-05-todo-cleanup|今日 TODO 清理]]** — 08-05 待办扫描
- **[[memory/2026/08/2026-08-05-xianyu-todo-executor|闲鱼待办执行]]** — 08-05 闲鱼任务执行
- **[[knowledge/cards/2026-08-05-agent-reliability-toolmaze|Agent 可靠性卡片]]** — 工具失败恢复研究 (08-05)
- **[[knowledge/cards/2026-08-06-ai-daily|AI 日报 08-05]]** — 模型/融资热点卡片
- **[[knowledge/cards/2026-08-06-deepseek-v4-flash-official|DeepSeek V4-Flash 正式版]]** — 模型能力卡片
- **[[knowledge/cards/2026-08-06-minimax-h3|MiniMax H3]]** — 视频编辑开源模型卡片
- **[[knowledge/Daily/hackernews-2026-08-05|HN 今日热点]]** — Hacker News 热门 (08-05)
- **[[knowledge/writing-material/独立开发陷阱与开源协作|独立开发陷阱]]** — 学生应先学协作写作素材
- **[[memory/2026/08/2026-08-04-reflection|反思日记]]** — 08-04 自我反思
- **[[memory/2026/08/health-2026-08-05|健康巡检报告]]** — 08-05 系统健康检查
- **[[memory/2026/08/2026-08-06-maintenance|今日维护报告]]** — 仓库健康检查 (08-06)
- **[[memory/2026/08/2026-08-06-xianyu-todo-executor|闲鱼待办执行]]** — 08-06 闲鱼任务执行
- **[[memory/2026/08/2026-08-07-xianyu-todo-executor|闲鱼待办执行]]** — 08-07 闲鱼任务执行（8/7 到期日）
- **[[memory/2026/08/2026-08-06-daily-todo-executor|每日待办落实]]** — 08-06 全库待办扫描 + 11 项自动执行
- **[[memory/2026/08/2026-08-06-daily-review|今日回顾]]** — 08-06 知识吸收回顾 + 明日变现行动项
- **[[knowledge/arXiv/arxiv-2026-08-06-agent-llm|arXiv 今日速览]]** — 14 篇 AI Agent/LLM 论文 (08-06)
- **[[memory/2026/08/2026-08-07-maintenance|今日维护报告]]** — 仓库健康检查 (08-07)
- **[[knowledge/Daily/hackernews-2026-08-06|HN 今日热点]]** — Hacker News 热门 (08-06)
- **[[memory/2026/08/2026-08-05-reflection|反思日记]]** — 08-05 自我反思
- **[[memory/2026/08/2026-08-06-reflection|反思日记]]** — 08-06 自我反思（3 改进点当场落地：xianyu 微步骤清单 / bat 检查清单 / web_extract 比例）
- **[[memory/2026/08/health-2026-08-06|健康巡检报告]]** — 08-06 系统健康检查
- **[[knowledge/arXiv/arxiv-2026-08-07-agent-llm|arXiv 今日速览]]** — 15 篇 AI Agent/LLM 论文 (08-07)
- **[[memory/2026/08/2026-08-07-daily-review|今日回顾]]** — 08-07 知识吸收回顾 + 明日变现行动项（P0 上架第 8 天 + 第 4 商品文案）
- **[[memory/2026/08/2026-08-07-daily-todo-executor|每日待办落实]]** — 08-07 全库待办扫描 + 状态推进第 8 天 + 技能孤岛审视落地

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

| 入口            | 位置                                                          | 说明                      |                    |
| :------------ | :---------------------------------------------------------- | :---------------------- | ------------------ |
| 📊 **工作流**    | [[pipelines/pipeline-overview                               | pipelines/]]            | 论文·PPT·Skill 触发工作流 |
| 📈 **项目**     | [[projects/current]]                                        | 当前项目状态与进度               |                    |
| 📝 **模板**     | [[templates/每日笔记模板                                          | templates/]]            | 每日笔记/通用笔记模板        |
| 📓 **通用模板**   | [[通用笔记模板]]                                                  | 通用笔记结构参考                |                    |
| 🧪 **边界测试**   | [[light-skills-boundary-test]]                              | Light Skills 4 情形边界测试报告 |                    |
| 🗂️ **方法论模板** | [[minimal-methodology-guide]] · [[research-cron-templates]] | 方法论 + 科研 cron 模板        |                    |
| 🧠 **学习**     | [[.learnings/LEARNINGS]]                                    | 架构决策 + 最佳实践             |                    |
| ❌ **错误**      | [[.learnings/ERRORS]]                                       | 踩坑记录与修复方案               |                    |
| 🗺️ **知识图谱**  | [[knowledge/knowledge-map]]                                 | vault 全局知识图谱            |                    |
| 🔀 **交叉域**    | [[knowledge/Cross-Domain]]                                  | 跨域自动索引                  |                    |
| 📝 **缓冲**     | [[memory/working-buffer]]                                   | 临时工作笔记                  |                    |

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
| 知识域 | 7 域 + 1 中枢（+ Research 研究域） |
| knowledge 文件 | ~160 篇 |
| Skills 生态 | 93 全活跃 |
| 记忆系统 | MEMORY + 每日日志 |
| Git 备份 | github.com/mo9652962-ai/second-brain |

---

_由 Obsidian + k (Hermes) 共同维护 | 2026-07-25 结构优化完成_
