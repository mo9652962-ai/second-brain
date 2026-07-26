---
tags: [hermes, daily, session]
domain: hermes-migration
created: 2026-07-23
updated: 2026-07-23
---

# 2026-07-23 Hermes 会话记录

> 从 OpenClaw 迁移到 Hermes 后的首次深度配置会话

## 完成事项

### 🔍 搜索能力增强（4后端冗余）
| 后端 | 方式 | 状态 |
|------|------|------|
| **Tavily** | API Key `tvly-dev...` | ✅ 最高优先级 |
| **Exa** | API Key `9ae0e...` | ✅ |
| **Firecrawl** | API Key `fc-7cb...` | ✅ |
| **DDGS (DuckDuckGo)** | pip 包 `ddgs v9.14.4` | ✅ 通过 VPN 可用 |
| **SearXNG** | 本地实例 `localhost:8888` | ✅ 自托管，30引擎已启用 |

### 📝 学术论文写作 Skill 创建
- 整合全网搜索，创建了 `academic-paper-writing` skill
- 10 大章节覆盖：写作全流程、学术语言规范、降AI味核心技术、分层策略、指令模板、AI替换表、中文要点、常见误区、自查清单、推荐工具

### ⚙️ 模型 Fallback 链重构
```
deepseek-v4-flash (主力)
  → deepseek-v4-pro (同供应商升配)
  → moonshotai/kimi-k2.6 (OpenRouter)
  → qwen/qwen3.7-plus (OpenRouter, 1M ctx)
  → z-ai/glm-5.2 (OpenRouter, 1M ctx)
```

### 🔗 Obsidian 仓库连接
- 仓库路径: `C:\Users\31954\.openclaw\workspace\`
- 已学习 35+ 个文件，12 个知识域
- 配置了每 30 分钟自动同步到 GitHub

## 相关笔记
- [[AI-Agent]] — 模型架构更新
- [[Academic]] — 论文写作 skill 新增
- [[AI-Workflow]] — 搜索工具链增强
- [[projects/current]] — 项目状态更新

---

_笔记由 k 自动写入_
