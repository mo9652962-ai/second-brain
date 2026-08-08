---
tags: [research, awesome-list, golang, go, reference]
created: 2026-07-31
status: archived-reference
source: "https://awesome-go.com/"
---

# Awesome Go — Go 生态资源精选（备查）

> 2026-07-31 存档 · 待 Go 相关需求时启用

## 是什么

Go 语言框架/库/软件精选清单（awesome-python 风格），社区维护，MIT 协议。

## 核心价值

| 类别 | 亮点 |
|------|------|
| **AI/Agent** | goai (20+ providers)、langchaingo、mcp-go、LocalAI、Ollama 生态 |
| **CLI** | 高级控制台 UI、标准 CLI 工具 |
| **Web 框架** | 中间件、路由、WebAssembly |
| **数据库** | 嵌入式、ORM、SQL 构建器、迁移工具 |
| **测试** | 框架、Mock、模糊测试、浏览器控制 |
| **学习资源** | Go By Example、Learn Go with TDD、Go Developer Roadmap |

## 与我们相关的项目（Go 生态 → Hermes 对照）

| Go 项目 | 用途 | 关联 |
|---------|------|------|
| `mcp-go` | MCP 服务器/客户端 Go 实现 | Hermes MCP 工具链 |
| `goai` | 20+ LLM provider SDK | opencode-go 类似定位 |
| `web-researcher-mcp` | 多源搜索 MCP 服务器（5 provider + 熔断） | 我们的 5 路搜索冗余同思路 |
| `AegisFlow` | AI 网关（路由/安全/监控 LLM 流量） | Hermes fallback 链 |
| `otellix` | LLM 可观测性 + 预算护栏 | cron_health 监控 |

## 何时启用

- [ ] 接到 Go 后端/CLI 开发单
- [ ] 需要 Go 实现的 MCP server
- [ ] 研究 Go 生态 AI 工具时

## 链接
- 官网: https://awesome-go.com/
- GitHub: https://github.com/avelino/awesome-go

---

*存档 2026-07-31 · 备用索引，非立即执行*

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
