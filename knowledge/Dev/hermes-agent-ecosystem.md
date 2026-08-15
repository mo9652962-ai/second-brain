---
tags: [tools, ecosystem, hermes, dev, knowledge-map]
domain: Productivity
created: 2026-07-30
updated: 2026-07-30
---

# 🔧 Hermes 工具生态速览

> 本库实际使用的工具链全景。不列"可能有用"的工具，只记**正在用**和**已验证可用**的。

## Agent 框架

| 工具 | 角色 | 状态 |
|------|------|------|
| **Hermes Agent** | 主力 AI 助手 | 🟢 日常使用 |
| **opencode-go** | 主 provider（deepseek-v4-flash/pro） | 🟢 通过火山方舟 |
| **SiliconFlow** | 辅助 provider（Qwen3-VL 视觉） | 🟢 视觉分析用 |
| **Kimi API** | 辅助 provider（k2.7-code/k2.6） | 🟢 已验证可用 |

## 浏览器自动化

| 工具 | 角色 | 状态 |
|------|------|------|
| `browser_navigate/click/type` | Hermes 内置浏览器 | 🟢 日常使用 |
| **Browserbase** | 云浏览器后端 | 🔵 可配未用 |
| **Browser Use** | 第三方集成 | ⏳ 官方集成已存在，内置已够用 |

## MCP 工具（当前 active）

| 工具 | 功能 | 来源 |
|------|------|------|
| Obsidian MCP | 读写 vault 笔记 | 内置 |
| 嘉立创 EDA MCP | PCB 设计自动化（38 工具） | jlcmcp |
| GitHub MCP | PR/Issue/Repo 管理 | 内置 |
| code-review-graph | 代码知识图谱（34 工具） | 已加载 |

## 部署与运行

```yaml
Hermes -> 本地桌面版 (Windows 10)
  ├── 配置文件: AppData/Local/hermes/config.yaml
  ├── 技能目录: AppData/Local/hermes/skills/
  ├── 脚本目录: AppData/Local/hermes/scripts/
  └── Cron 任务: 28 个定时任务
```

## Python 工具

| 工具 | 用途 | 安装方式 |
|------|------|---------|
| uv | 包管理器 | 随 Hermes venv |
| python-docx | 文档生成 | uv pip install |
| markitdown | 文件转换 | uv pip install |

## 跨域引用

- → [[knowledge/Dev/python-ecosystem|Python 生态]]
- → [[knowledge/Dev/MOC-Dev|AI 域]] — Hermes+Agent 配置
- → [[MOC-Productivity|效率域]] — 工具方法论
