---
tags: [research, wemux, multi-agent, tool]
type: research
created: 2026-09-18
title: Wemux — 自托管 AI Agent 协作平台
---
# Wemux — 自托管 AI Agent 协作平台（千轮研究 2026-09-18）

> 来源：抖音【子杰Kyro】→ wemux-ai/wemux。一句话定位：**AI 原生组织 OS，Worker-first 执行 —— agent 在你的机器上用你的凭据做真实编码，代码不出机器。**

## 结论置顶

**方向对 sora 的 multi-agent 兴趣有参考价值，但当前太早期（3 周新 repo / 136 star），且主打「组织/团队协作」场景，对个人接单的 sora 有点超前，不建议立即采用。** 最实际的价值是：① AI 博主选题素材（solo 44 万行代码的故事性）② worker-first + worktree 隔离 + 人机审查流的架构参考。

## 实证数据（2026-09-18 抓取）

| 项 | 值 |
|---|---|
| 仓库 | `wemux-ai/wemux` |
| 发布 | 2026-09-02（作者子杰Kyro，一个人+AI，166天/2666 提交/44 万行） |
| Star / Fork | **136** / 39（刚开源，小量级） |
| 协议 | Apache-2.0（社区版全自托管；model gateway/cloud node/billing 是商业化服务，不在 repo） |
| 技术栈 | TS：React web + Hono control plane + worker daemon；Postgres + S3 |
| 定位 | self-hostable AI agent collaboration platform |

## 核心机制（Worker-first）

```
web console → server control plane（Hono，规划/路由/审查）→ worker daemon（隔离 Git worktree 里跑 OpenCode/Claude Code/Codex）
```

流程：自然语言建任务 → main agent 规划选 worker → worker 在隔离 worktree 用你的凭据执行 → diff 上报 → **人工审查批准** → 交付。control plane 永不执行你的代码。

## 关键能力

- **Worker-first**：代码在你自己 worker 上跑，隔离 worktree，BYOK 模型 key 不出 worker。
- **多节点 mesh**：多 worker 用 easytier 组网，按能力路由。
- **IM 渠道接入**：飞书/Slack/钉钉/企微/微信/WhatsApp 入站建任务。
- **Kanban/工作区/群聊**：任务看板、workspace 会话、agent 群聊、Drive 文件共享。
- **原生客户端**：Electron 桌面 + React Native/Expo 移动端。
- BYOK：跑 OpenCode/Claude Code/Codex，任意模型。

## 与 sora 现状的关系

sora 已有 Hermes + Codex 委派 + multi-agent（WorkBuddy/dsh/Codex/Antigravity/K3/Gemini）+ 记忆引擎。Wemux 的「agent 编排 + 隔离执行 + 审查」与现有方案方向重叠，且是团队协作定位，个人场景暂用不上。**唯一可借鉴的是 worker-first 的「隔离 worktree + 人工合并门」设计**，未来 sora 若接 agent 相关单或做 agent 产品可参考。

## 决策建议

- **不急于采用**（太早期 + 场景不符），保持关注即可。
- 若要做 AI 博主选题，「solo 44 万行 AI 原生 OS」有故事性，可对比测评。
- 架构参考留档：worker-first / worktree 隔离 / 人机审查门。