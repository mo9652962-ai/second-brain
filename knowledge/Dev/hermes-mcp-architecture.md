---
title: Hermes + MCP 分层架构
date: 2026-07-29
tags: [architecture, hermes, mcp, agent-design]
domain: research
status: adopted
source: VetClaw paper + OpenClaw vs Hermes comparison + 2026 行业最佳实践
---

# Hermes + MCP 分层架构

> 我们的架构 = **Hermes（OpenClaw 交互层）+ MCP（LangGraph 工作流层）**
>
> 这是 2026 行业最佳实践，与 VetClaw 边缘-云端架构完全对齐。

---

## 🏛 三层架构

```
┌─────────────────────────────────────────────────────────────┐
│                    用户交互层 (User)                         │
│         桌面客户端 / Telegram / Web / API                    │
└─────────────────────────┬───────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────┐
│              🔵 Hermes = OpenClaw 等效层                     │
│              （边缘端 — 交互 + 调度 + 治理）                   │
│                                                             │
│  • 对话管理（session + memory + context engineering）        │
│  • 工具调度（browser_* / terminal / read / write / search）  │
│  • 技能系统（Skill loading + routing + execution）           │
│  • 定时任务（Cron scheduling + health monitoring）           │
│  • 用户交互（streaming output / file delivery / TTS）        │
│  • 治理层（SOUL.md + AGENTS.md + CODE_OF_CONDUCT）           │
│  • 自举系统（7 大自举模块：记忆/输出/工具/代码/上下文/知识/自动化） │
└─────────────────────────┬───────────────────────────────────┘
                          │ 工具调用/MCP协议
┌─────────────────────────▼───────────────────────────────────┐
│              🟢 MCP = LangGraph 等效层                       │
│              （工作流层 — 有状态编排 + 专业工具）              │
│                                                             │
│  🔧 Obsidian MCP (27124)                                    │
│     └─ 知识库读写/搜索/图谱管理                                │
│  🔧 嘉立创 EDA MCP (38 tools)                                │
│     └─ PCB 设计/布线/DRC/阻抗计算                             │
│  🔧 code-review-graph MCP                                    │
│     └─ 代码知识图谱增量分析                                   │
│  🔧 Memvid MCP                                               │
│     └─ 记忆层持久化/检索                                      │
│  🔧 GitHub MCP                                               │
│     └─ 仓库管理/PR/Issues                                    │
│  🔧 Filesystem MCP                                           │
│     └─ 文件系统安全访问                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 架构对照：VetClaw → Hermes

| VetClaw 组件 | 职责 | Hermes 等效 | 状态 |
|-------------|------|------------|------|
| **OpenClaw** | 调度、工具访问、用户交互、通知 | **Hermes Agent Core** | ✅ 运行中 |
| **LangGraph** | 有状态筛查工作流 | **6 个 MCP 工具链** | ✅ 运行中 |
| 输入验证 | 多模态输入校验 | SOUL.md + AGENTS.md 约束 | ✅ |
| 模型调用 | VLM 零样本分类 | 方舟一→方舟二→opencode-go 容灾链 | ✅ |
| 安全检查 | 确定性安全规则 | CODE_OF_CONDUCT.md 全球首创 | ✅ |
| 条件路由 | 不确定案例升级 | Cron 错误模式库 + 经验式修复 | ✅ 今日固化 |
| 故障处理 | 结构化日志 + 重试 | .learnings/ERRORS.md + 自动重试 | ✅ |
| 边缘设备 | 摄像头采集 | Desktop 客户端 + browser_* | ✅ |

---

## 📐 架构优势

### 1. 关注点分离
- **Hermes 层**：只管"用户想做什么"（意图理解 → 工具调度）
- **MCP 层**：只管"怎么做"（专业工具执行 + 状态管理）
- 互不侵入，独立演进

### 2. 可靠性
- Hermes 挂了 → MCP 工具依然可用（独立进程）
- MCP 工具挂了 → Hermes 降级到内置工具
- 参考：VetClaw 的边缘端 + 云端分工模式

### 3. 可扩展性
- 新 MCP 工具接入：无需修改 Hermes 核心
- 新交互渠道：无需修改 MCP 工作流
- 参考：NVIDIA NemoClaw 企业架构

---

## 🔄 与 2026 行业对标

| 对比维度 | OpenClaw | Hermes Agent | 我们 |
|---------|----------|-------------|------|
| 工具市场 | ClawHub 13k+ skills | Curator 自生成 | ✅ 自举 7 大系统 |
| 多 Agent | Agent-to-Agent 通信 | 单 Agent 深度 | ✅ leaf subagent |
| 安全性 | 供应链攻击风险（市场） | 零 CVE（自生成） | ✅ 6 MCP 独立审计 |
| 记忆系统 | 大量上下文 | 搜索优先 | ✅ UniMem 双通路 |

---

## 🚀 演进路线

| 阶段 | 行动 | 状态 |
|-----|------|------|
| ✅ 已实现 | Hermes 单 Agent + 6 MCP 工具链 | done |
| 🔜 近期 | Cron 错误模式库 + 经验式修复 | 今日固化 |
| 🔜 近期 | 浏览器异步验证（参考 DDB） | 今日固化 |
| 📋 中期 | Cognicore 桌面插件（系统状态监控） | 计划中 |
| 📋 中期 | MCP 工作流编排（LangGraph 等效） | 计划中 |
| 🌅 远期 | 多 Agent 协作（leaf subagent 深化） | 架构预留 |

---

## 💡 核心洞察

> **"Hermes = 大脑皮层，MCP = 小脑 + 脊髓"**
>
> Hermes 做决策、理解意图、调度工具（大脑皮层），
> MCP 做执行、管理状态、处理专业领域（小脑 + 脊髓）。
>
> 这个分工在 VetClaw 和 NemoClaw 中都得到了验证，
> 也是 2026 年 Agent 架构的行业共识。

---

*架构确认：2026-07-29 | 参考：VetClaw (2607.26042) + OpenClaw vs Hermes 对比 + NemoClaw*

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
