---
aliases:
  - agent-self-strengthen
tags:
  - research
  - ai-agent
  - memory
  - self-improvement
created: 2026-08-06
source: web_search × 6 queries
status: applied
---

# AI Agent 自强化研究 — 记忆分层 + 能力固化

> 2026-08-06，借鉴 Vellum/Reddit AI_Agents/MachineLearningMastery/Redis 等

## 关键发现

### 1. Hermes Agent 获得业界认可
- Vellum《2026 最佳个人 AI 助手》排名 #7: "open-source, self-improving AI agent that builds knowledge about its environment and your workflows over time through active learning"

### 2. 记忆分层原则（Reddit AI_Agents 高赞 + Redis 文章）
- **操作性记忆**（今天做了什么/项目状态）→ 不入 memory，会过时
- **习得性记忆**（偏好/环境事实/教训）→ memory，长期价值
- **程序性记忆**（做法/流程/技能）→ skills
- **语义记忆**（通用知识）→ knowledge base
- 关键洞察: "Agents without memory feel intelligent but inconsistent"

### 3. 自强化循环（Vellum Agentic Workflows）
- Refinement: 用评估器检查自己输出
- Error handling: 快速检测/分类/修复，从失败沉淀 skill
- 工具自造: 无工具时写代码创建自己的工具（LATM）

## 已应用（2026-08-06）

| 动作 | 内容 |
|:-----|:-----|
| ✅ Memory 整理 | 移除 SimSync 操作性细节（已在 skill），压缩项目状态条目 |
| ✅ 技能固化 | sims4-mp-protocol-engineering 完整（12 项协议增强+坑） |
| ✅ 技能新建 | web-ui-beautification（三轮 UI 美化方法论） |
| ✅ 技能新建 | english-practice-machine（刷题机开发指南） |
| ✅ 技能更新 | 路由陷阱/UI 美化记录进技能 |

## 下一步可做
- 定期 memory 健康检查（操作性→skill，腾空间）
- 技能去重（工具库庞大，curator 可跑）
