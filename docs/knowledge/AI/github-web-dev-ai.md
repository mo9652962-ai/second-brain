---
tags: [GitHub, 学习笔记, AI开发, 全栈]
aliases: [GitHub Web Dev AI]
date: 2026-07-22
status: watch
---

# GitHub 网站开发 + AI 应用 — 学习笔记

## 值得关注的项目

### AI 全栈应用构建
| 项目 | 说明 | Stars |
|:----|:----|:----:|
| [stackblitz/bolt.new](https://github.com/stackblitz/bolt.new) | AI 全栈 Web 开发，浏览器中 prompt→run→deploy | ⭐ 高 |
| [pingcap/full-stack-app-builder-ai-agent](https://github.com/pingcap/full-stack-app-builder-ai-agent) | AI Agent 描述→搭建→部署全流程（TiDB+Vercel+Codex+Claude） | ⭐ 高 |
| [giselles-ai/giselle](https://github.com/giselles-ai/giselle) | 开源 AI 工作流构建器，no-code 拖拽 | ⭐ |

### Awesome List 精选
| 项目 | 内容 | 链接 |
|:----|:----|:----|
| **awesome-ai-agents-2026** | 340+ 资源，20 类，月更新 | [caramaschiHG/awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026) |
| awesome-ai-devtools | AI 开发者工具精选 | [jamesmurdza/awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools) |
| awesome-AI-driven-development | AI 驱动开发工具 | [eltociear/awesome-AI-driven-development](https://github.com/eltociear/awesome-AI-driven-development) |
| awesome-web-agents | Web 浏览 AI Agent | [steel-dev/awesome-web-agents](https://github.com/steel-dev/awesome-web-agents) |

### AI Agent 建设
| 项目 | 亮点 |
|:----|:----|
| [firecrawl/open-agent-builder](https://github.com/firecrawl/open-agent-builder) | 可视化 AI Agent 工作流构建器，Firecrawl 支持 |
| [potpie-ai/AI-COSS](https://github.com/potpie-ai/AI-COSS) | Agentic 开源公司列表 |

## AI 与 Web 开发结合的 4 个层次

### L1: AI 辅助编码 (Copilot)
```
开发者写代码 → AI 补全/建议 → 人工审查 → 合入
```
- 工具: GitHub Copilot, Cursor, Tabnine
- 适用: 日常开发，所有阶段

### L2: Prompt → 应用 (Bolt.new 模式)
```
用户描述需求 → AI 生成完整应用 → 预览 → 修改 → 部署
```
- 工具: Bolt.new, v0 (Vercel)
- 适用: 快速原型、MVP

### L3: AI Agent 全流程 (PingCAP 模式)
```
用户一句话 → Agent 规划 → 配基础设施(GitHub+DB+Vercel)
                       → 生成代码(Codex+Claude)
                       → 数据库迁移
                       → 测试 → 部署
```
- 工具: PingCAP agent, Claude Code, Codex
- 适用: 复杂全栈应用

### L4: Agentic Web 浏览
```
AI Agent → 打开浏览器 → 操作网页 → 提取数据 → 完成任务
```
- 工具: OpenAI Operator, Browser-Use, Skyvern-AI
- 适用: 自动化测试、数据采集、表单填写

## 对我们 web-dev-2026 skill 的补充

新增 AI 集成建议到 skill:

| 环节 | AI 应用 | 建议工具 |
|:----|:--------|:--------|
| 代码生成 | 组件骨架/CRUD | Copilot Chat |
| 设计 | UI → 代码 | v0.dev |
| 测试 | 自动生成测试用例 | Copilot + Vitest |
| 部署 | CI/CD 配置 | Vercel AI |
| 调试 | 错误诊断 | Claude Dev |

## 学习总结

1. **2026 年Web开发的核心趋势**：AI不再是附加品，而是工具链的一等公民
2. **Prompt→App 模式成熟**：Bolt.new 验证了"描述即应用"的可行性
3. **Agent 全流程仍复杂**：PingCAP 方案需要多工具编排，但方向明确
4. **Awesome List 是金矿**：awesome-ai-agents-2026 有 340+ 资源可深入
