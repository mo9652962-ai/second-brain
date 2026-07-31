---
tags: [research, article-study, learning, github, ai-course]
created: 2026-07-31
status: absorbed
---

# 《用 GitHub 搭一套「AI 自学作战系统」》— 992Zero

> 来源：小黑盒文章 · 2026-07-31 · 已验证 + 吸收

## 文章核心：四层自学架构

| 层级 | 模块 | 解决什么问题 | 核心工具 |
|------|------|-------------|---------|
| 信息层 | 学习路线追踪 | 学什么、从哪学、学到哪 | GitHub Trending + Notion |
| 工具层 | AI 工具矩阵 | 写作、代码、搜索、笔记 | Copilot + DeepSeek/豆包/Kimi + Obsidian |
| 实战层 | 项目驱动学习 | 光学不用等于没学 | GitHub 开源项目实战 |
| 展示层 | 成果沉淀 | 写简历、面试有话 | GitHub Profile + 博客 |

## 5 个推荐项目（全部验证，star 数为 2026-07-31 实测）

| 项目 | Stars（实测） | 类型 | 语言 | 对我们的价值 |
|------|:---:|------|:---:|------|
| Hands-On LLM | 27.6k | O'Reilly 书配套代码，300 图可视化 LLM | EN | 🟡 基础回顾，暂不精读 |
| MS AI Agents for Beginners | **70.5k** | 微软官方 18 课 Agent 课程（文章只说了 11 课） | 多语 | 🔴 **第 11-13 课与体系同构** |
| happy-llm | 32.4k | Datawhale 中文 LLM 原理+训练实战 | 中文 | 🟡 造轮子层，暂用不到 |
| self-llm | 31.4k | Datawhale 开源模型部署+微调指南 | 中文 | 🟡 我们走 API 路线，暂用不到 |
| hello-agents | **68.9k** | Datawhale 16 章智能体构建教程 | 中文 | 🔴 **第 8-12 章与体系同构** |

## 关键发现：体系对照（我们的实践 vs 课程内容）

这两个高星课程讲的内容，**我们的 Second Brain 体系已在实践中**：

| 课程章节 | 我们体系对应物 | 状态 |
|---------|--------------|------|
| MS 第 11 课 Agentic Protocols (MCP/A2A/NLWeb) | 规则 #2 MCP 配置铁律 + jlc-mcp | ✅ 已实践 |
| MS 第 12 课 Context Engineering | 规则 #15 跨天会话 + 规则 #21 干湿分离 | ✅ 已实践 |
| MS 第 13 课 Managing Agentic Memory | 规则 #11 记忆价值量化 + memory_tracker | ✅ 已实践 |
| hello-agents 第 8 章 记忆与检索 | UniMem 情景→参数化路由（规则 #12） | ✅ 已实践 |
| hello-agents 第 9 章 上下文工程 | 规则 #15/#21 上下文治理 | ✅ 已实践 |
| hello-agents 第 10 章 智能体通信协议 | MCP 体系 + 工具集 | ✅ 已实践 |
| hello-agents 第 12 章 智能体性能评估 | 规则 #17 评估器可靠性自检 | ✅ 已实践 |
| MS 第 15 课 Computer Use Agents (CUA) | StateAct 规则 #16（状态优先于渲染） | ✅ 已实践 |

**结论：我们的体系不是"纸上谈兵"，而是覆盖了 2026 年最热 AI 课程的核心知识点，且已落地为可执行规则。**

## 落地行动

1. ✅ 4 个学习项目已存档（本文档即存档）
2. 🟡 可选：精读 MS 第 12 课 Context Engineering + hello-agents 第 9 章，验证我们规则 #15/#21 是否还有遗漏（暂缓，待有专门学习时段）
3. 💡 对 AI 博主身份的价值：这篇"四层架构"文章是现成的选题框架（信息层/工具层/实战层/展示层），可参考做一期 B 站视频《用 GitHub 搭 AI 自学系统》

## 结论

- 文章面向准大一新生，四层架构逻辑清晰，但 star 数据过时（低估 2-4 倍）
- 对我们的增量价值：① 确认体系知识覆盖度 ② 存档 4 个学习项目 ③ 博主选题参考
- 无需安装任何新工具（GitHub Copilot 我们不缺——Hermes 本身就是更强的 Copilot）
