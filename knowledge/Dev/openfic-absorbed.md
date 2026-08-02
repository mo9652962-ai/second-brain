---
tags: [absorbed, vibe-writing, ai-native-tool, agent-design]
source: OpenFic (syrizelink) · v0.7.6 · 343⭐
status: absorbed
date: 2026-07-27
---

# OpenFic · Vibe Writing 工具 · 吸收笔记

> AI Native 小说写作工具，343⭐，Apache 2.0
> 设计理念：让 Agent 适应你的写作流程，而非反之

---

## 最值得借鉴的设计理念

### 1. "人机协同"而非"一键生成"
OpenFic 明确区分自己与 SillyTavern（抽卡生成）、Claude Code（编码优化）：
- Agent 是**协作伙伴**，不是替代你写
- 发散思维、构建情节、协同编辑
- **首先是一个好用的写作工具，其次才是 AI Agent**

**→ 应用到我们**：闲鱼服务的定位也应该是"人机协同"——先对齐需求再动手

### 2. Agent 适应人，而非人适应 Agent
> "让 Agent 适应你的写作流程，而非反之"
- 高度可配置的 Agent 系统
- 可以自由修改任何 Prompt
- 用 Skill 构建自己的工作流

**→ 应用到我们**：Skill 系统就是这么设计的，方法论提取项目的 G5 审计也是这个方向

### 3. 迭代路径：固定流程 → 父子节点 → Agent
```
① 固定工作流（像酒馆的一键生成）
② 父子节点的主管模式
③ 现在的 Agent 形式（类似 Codex）
```

**→ 应用到我们**：Agent 系统设计也应该允许从简单到复杂的渐进使用

### 4. 成本优先架构
- 多层上下文管理
- 智能压缩、动态截断
- 稳定缓存

**→ 应用到我们**：我们的 8 级 fallback 链 + reasoning_effort: high 也是成本优先

### 5. 基于向量的 Agentic RAG
百万字级别项目中高效检索过往信息

**→ 应用到我们**：Obsidian MCP 的语义搜索类似，但还有差距

---

## 技术栈参考

| 组件 | OpenFic | 我们的对标 |
|:-----|:--------|:----------|
| 后端 | Python (FastAPI) | Hermes Gateway |
| 前端 | React/TypeScript | Hermes Desktop |
| 桌面端 | Electron/Tauri | Electron |
| RAG | 向量检索 | Obsidian MCP |
| Agent | 定制工作流 + Skill | Hermes Skill 系统 |
| 成本控制 | 多层上下文管理 | 8 级 fallback 链 |

## 可实操行动

- 如果要写小说，OpenFic + DeepSeek（他说几乎没有限制）可以试试
- show-me-the-story 标记为 backlog，OpenFic 可能是更好的选择

---
> 关联: [[openfic-study]]（完整研究笔记） | [[HOME|🏠 首页]]
