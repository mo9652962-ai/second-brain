---
tags: [research, github, article-study, project-management, kaneo]
created: 2026-08-01
status: absorbed
source: https://github.com/usekaneo/kaneo
---

# Kaneo — 研究笔记（极简项目管理工具）

> 来源：小黑盒推荐 · 2026-08-01 验证 + 评估

## 项目验证

| 项 | 值 |
|----|-----|
| 仓库 | usekaneo/kaneo |
| Stars | 3,894 |
| License | MIT |
| 技术栈 | TypeScript + Hono (API) + React/Tailwind (Web) + PostgreSQL |
| 创建 | 2024-12-31 |
| 安装 | Docker Compose / drim CLI / Helm chart |
| 集成 | GitHub / Gitea 同步，Slack/Discord webhooks |

## 核心理念

> "All you need. Nothing you don't."
> 作者（Andrej）厌倦了臃肿的项目管理平台——问题不是缺功能，是功能太多。
> "最好的工具是隐形的。"

**极简原则**：
- 看板 + 列表同一数据源（Board 和 List 视图同步）
- 无重型流程（分配负责人/截止日期/优先级即可）
- 标签 + 优先级组织
- 原生 GitHub 集成（issue 同步）
- 隐私优先（最小分析）+ 自托管（Docker）

## 我们的评估

| 选项 | 决策 | 理由 |
|------|:---:|------|
| 安装 Kaneo | ❌ | **无 Docker 环境**（需要 Docker + PostgreSQL + 2GB RAM/10GB 磁盘） |
| 作为任务管理工具 | ❌ | 我们已有轻量体系：todo + Obsidian 待办 + User-blocked（规则 #6） |
| **极简理念吸收** | ✅ | "less dashboard theater" 与我们的低调务实风格一致 |

## 理念吸收（有普适价值）

**Kaneo 最值得学的不是功能，是设计哲学**：
1. **极简主义**：每个功能必须解决真实问题，不为演示好看
2. **工具隐形**：好的工具放大自然工作流，不强迫用户适应工具
3. **自托管/数据自有**：隐私优先，不依赖 SaaS

**与我们的映射**：
- 呼应 sora 风格偏好（低调务实，不自称第一）
- 呼应"全都要但能用就行"（工具实用主义）
- 我们的 todo + Obsidian 待办已实现"轻量任务管理"——Kaneo 对单人知识工作者过重

## 何时值得再评估
- 如果未来需要团队协作/客户项目可视化交付（闲鱼接单项目管理）
- 如果 Docker 环境就绪
- 需要 GitHub issue 可视化同步时

## 结论
- 项目真实（3.9K★，MIT，活跃维护）
- 对我们：**不安装**（无 Docker + 已有轻量任务体系）
- 理念（极简/工具隐形/数据自有）已吸收
- 未来团队协作/接单项目管理场景可再评估

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
