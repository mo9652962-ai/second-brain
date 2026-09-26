---
tags: [MOC, index, vault-guide]
domain: home
created: 2026-07-25
updated: 2026-09-25
---

# 🗺️ vault 全局关联网

> 这里是 Obsidian 仓库的完整结构图，从 HOME 出发，串联所有知识。  
> 2026-09-23 全面贯彻执行**【资产三级隔离原则】**，确立 18 域全景拓扑与纯净开源模式。

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
      │ 18 个领域  │   │ projects/    │   │ 配置/脚本  │
      │ 700+ 笔记  │   │ 知识点       │   │ 文档/模板  │
      └─────┬──────┘   └──────────────┘   └─────┬─────┘
            │                                   │
            ▼                                   ▼
  knowledge/ 18 域                    system/ docs/ scripts/
  (含 knowledge-map.md MOC)           templates/ playbooks/
```

## 核心入口

| 节点 | 作用 |
|:---|:---|
| [[HOME]] | 知识中枢 · MOC 索引 · 最近更新 |
| [[INDEX]] | 本文件 · vault 全局关联网 |
| [[knowledge/knowledge-map]] | 知识域 → 笔记的完整映射（最新维护） |
| [[knowledge/METABOLISM]] | 知识新陈代谢 (OKM) 代谢看板 |
| [[knowledge/DASHBOARD]] | 知识库健康度与更新频率总览 |
| [[CHANGELOG]] | 变更记录 |

## 18 大知识域清单（全景拓扑）

| 领域 | 核心 MOC 锚点 | 领域核心内容与实战方向 |
|:---|:---|:---|
| 🤖 **AI / Agent** | [[knowledge/Dev/MOC-Dev\|MOC-Dev]] · [[knowledge/AI/MOC-AI\|MOC-AI]] | Agent 自举系统、Harness 框架、推理路由与多智能体协同 |
| 💻 **现代 Web 开发** | [[knowledge/Dev/MOC-Dev\|MOC-Dev]] | Next.js 15、TypeScript、Three.js、高感官微交互工程 |
| 🔬 **深度前沿研究** | [[knowledge/Research/MOC-Research\|MOC-Research]] | arXiv 前沿论文深研、开源技术评测、算法解析与学术基线 |
| 🐙 **GitHub 开源生态** | [[knowledge/Research/MOC-GitHub\|MOC-GitHub]] | 每周 Trending 增速榜精选、全球前沿开源项目解剖 |
| ⚡ **硬件与自动化** | [[knowledge/Hardware/MOC-Hardware\|MOC-Hardware]] | KiCad 10 自动化脚本、嘉立创 EDA、单片机 8051、工业 CAD |
| 📈 **生产力与工程** | [[knowledge/Productivity/MOC-Productivity\|MOC-Productivity]] | 自动化流水线、工作流编排、高质量工程交付体系 |
| 🛡️ **安全与攻防** | [[knowledge/Security/MOC-Security\|MOC-Security]] | API 安全审计、防木马供应链加固、隐私门禁检测技术 |
| 🎬 **创意与自媒体** | [[knowledge/Content/MOC-Content\|MOC-Content]] · [[knowledge/Creative/MOC-Creative\|MOC-Creative]] | 商业短视频生产管线、四维摄影机控制、去 AI 味与文字润色 |
| 📋 **标准化 SOP** | [[knowledge/SOP/MOC-SOP\|MOC-SOP]] | 深度排障 SOP、模型评估 SOP、知识吸收四算子标准化工程 |
| 🃏 **精选知识卡片** | [[knowledge/cards/MOC-cards\|MOC-cards]] | 每日重磅事件、技术洞察、大模型架构创新极简卡片池 |
| 📦 **项目管理** | [[projects/current\|当前项目]] · [[knowledge/Projects/MOC-Projects\|MOC-Projects]] | 墨题 (EPM) 考研机、万悟产业赛道等重点项目生命周期 |
| 🎓 **教育科研** | [[knowledge/Education/MOC-Education\|MOC-Education]] | 课题申报书设计论证、数模竞赛分析、教学设计规范 |

## 项目与系统

| 目录 | 内容 |
|:---|:---|
| projects/ | 进行中项目与里程碑 |
| system/ | 系统配置与状态 |
| docs/ | 知识库文档与架构指南 |
| scripts/ | 自动化自检与同步脚本 |
| templates/ | 笔记与复盘标准模板 |
| pipelines/ | 自动化知识流水线 |
| traces/ | 任务执行与评测轨迹 |
| health/ | 定时健康巡检报告 |
| site/ | 静态站点与文档站点 |
| concepts/ | 概念原子笔记 |
| research/ | 长期研究追踪器（trackers/，arXiv 追踪） |
| outputs/ | 公开输出产物与示例 |
| mcp/ | MCP 协议服务与配置 |
| skills/ | 可执行 Agent 技能库 |
| portfolio/ | 作品集与实战案例 |

## 🔗 目录内文件挂载

> 以下为公开层实体文档的入链锚点（防图谱孤立）。

| 文件 | 内容 |
|:---|:---|
| [[pipelines/pipeline-overview\|Pipeline 工作流总览]] | cron 任务链与调度全景 |
| [[playbooks/browserbase-evaluation\|Browserbase 评估]] | 浏览器自动化托管方案评估 |
| [[playbooks/camofox-docker-setup\|Camofox Docker 部署]] | 反检测浏览器本地部署 |
| [[playbooks/web-scraping-cron-template\|网页抓取 Cron 模板]] | 抓取任务标准模板 |
| [[system/GitHub-Treasure-Hunt-System\|GitHub 寻宝系统]] | 开源项目发现与评估体系 |
| [[todo/skill-link-gate-剩余98条断链-2026-09-08\|技能断链待办]] | 技能库断链剩余项跟踪 |
| [[concepts/MOC-Concepts\|概念原子笔记索引]] | 概念级常青卡片 |
| [[health/MOC-Health\|健康自举索引]] | Hermes 运行状态与健康报告 |
| [[portfolio/MOC-Portfolio\|作品集索引]] | 实战案例与交付作品 |
| [[docs/知识库重构方案-2026-08-16\|知识库重构方案]] | 18 域拓扑重构设计文档 |
| [[templates/research-cron-templates\|研究 Cron 模板]] | 定时研究任务标准模板 |
| [[templates/light-skills-boundary-test\|轻量技能边界测试]] | 技能边界与降级验证 |
| [[skills/8051-embedded-dev/references/8051-cheatsheet\|8051 速查表]] | STC89C52 寄存器与指令速查 |
| [[skills/8051-embedded-dev/references/hardware-checklist\|8051 硬件清单]] | 最小系统与外围电路核对 |
| [[skills/cad-design-master/references/cad-learning-curriculum\|CAD 学习路线]] | 从 2D 到 3D 打印的课程表 |
| [[skills/cad-design-master/references/cad-software-comparison\|CAD 软件对比]] | 主流建模软件选型矩阵 |

## 维护说明

1. 新研究笔记写入 `knowledge/Research/`（文件名含日期）
2. 每批次研究后更新 `knowledge/knowledge-map.md` 挂载 MOC（防孤立节点）
3. 严格遵循**资产三级隔离原则**，商业核心算法、接单成本与隐私日记物理隔离于 `private_knowledge/`
4. 自动同步：git push → GitHub (mo9652962-ai/second-brain)，gh-pages MkDocs 自动部署
