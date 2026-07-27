# 🧠 Second Brain

> AI 驱动的个人知识库 · OpenClaw/Hermes Agent 自动维护

一个由 **AI Agent 自动维护**的第二大脑知识库，涵盖 AI Agent 架构、学术写作、PPT 设计、PCB 开发、变现策略等领域的知识沉淀。

## 🗺️ 结构

```
.
├── knowledge/          # 知识笔记（按域分类）
│   ├── AI/            # AI Agent / LLM 生态
│   ├── Academic/      # 学术服务 / 论文写作
│   ├── Design/        # PPT 设计 / 视觉
│   ├── Dev/           # 软件开发 / 极简编程
│   ├── Hardware/      # PCB / CAD / 嵌入式
│   └── Productivity/  # 效率工具 / 方法论
├── skills/             # Hermes Agent Skills
├── memory/             # 每日日志 / 反思 / 周回顾
│   └── YYYY/MM/       # 时间线存档
├── .learnings/         # LEARNINGS 记录
├── projects/           # 项目文档
├── pipelines/          # 工作流 Pipeline 文档
├── scripts/            # 辅助脚本
├── templates/          # 模板
├── concepts/           # 核心概念
├── portfolio/          # 作品集
├── .hermes/            # Hermes Agent 配置
├── knowledge-map.md   # 🌐 知识地图（核心索引）
├── SOUL.md            # AI 行为准则
├── README.md          # 本文
└── MEMORY.md          # 持久记忆
```

## 🤖 自动化体系

| 频率 | 任务 | 说明 |
|:----|:-----|:------|
| 每天 7:00 | arXiv 论文抓取 | 最新 AI Agent / LLM 论文入库 |
| 每天 8:00 | 论文精读 | 精选 2-3 篇深度解读 |
| 每天 9:00 | 自我反思 | 每日三改进点 |
| 每天 18:00 | 变现回顾 | 闲鱼/接单复盘 |
| 每天 20:00 | 待办执行 | 全库扫描并执行待办 |
| 每 30min | GitHub 同步 | 自动推送变更 |
| 每周日 | 知识整合/图谱/清理/成本报告 | 周末维护 |

## 🔧 技术栈

- **平台**: OpenClaw / Hermes Agent
- **模型**: opencode-go / DeepSeek-v4-flash
- **知识库**: Obsidian + GitHub
- **MCP 服务**: GitHub · Filesystem · JLCPCB · Obsidian
- **自动化**: Hermes Cron（22 个定时任务）

## 📊 统计

- 244+ 文件，117+ 提交
- 12+ 知识域，持续吸收中
- 全自动维护，零手动操作

## 📄 许可

MIT License — 详见 [LICENSE](./LICENSE)
