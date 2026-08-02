---
tags: [methodology, multi-agent, orchestration, agentradio, cron]
aliases: [agentradio-five-phase, 五阶段分工协议]
date: 2026-08-02
source: https://arxiv.org/abs/2607.28430 (AgentRadio)
status: adopted
---

# 📻 AgentRadio 五阶段分工 → 多 Agent 编排参考

> 2026-08-02 从 AgentRadio 论文提炼（四 agent 32.3%→62.1%，超过更强单 agent）
> 核心：**架构 > 模型**——分工协议比换更强模型更有效
> 本文映射到我们的 cron 多任务链 + delegate_task 后台子代理

## 一句话

AgentRadio 证明：多个 agent 用"**线程/消息/被动感知**"三个原语 + "**分工/协商**"五阶段协议协作，效果超过单个更强 agent（62.1% vs 57.2%）。我们的 cron 任务链已有分工雏形，本文把它升级为显式协议。

---

## 1️⃣ AgentRadio 核心（论文提炼）

### 三个原语
| 原语 | 作用 |
|------|------|
| **threads（线程）** | 每个 agent 独立工作线 |
| **messages（消息）** | agent 间异步通信 |
| **wait-for-mention（等被提及）** | 后台被动感知：不打断前台工作，被提及才介入 |

### 五阶段协议
1. **分工**（division of labor）：任务按领域拆给各 agent
2. **独立执行**：各 agent 并行工作
3. **结果广播**：发现新信息 → 广播给团队
4. **协商**：冲突/重叠部分讨论解决
5. **整合产出**：合并各 agent 成果

**关键**：wait-for-mention 让 agent **被动感知**队友进展，不浪费 token 轮询，也不错过关键信息。

---

## 2️⃣ 映射到我们的体系

### 现状（cron 多任务链）

```
daily-self-improvement ──→ daily-todo-executor ──→ weekly-todo-cleanup
        ↓                        ↓
arxiv-fetch ──→ arxiv-summarize ──→ weekly-knowledge-consolidation
        ↓
github-treasure-hunt ──→ weekly-trending-review
```

**现状问题**：
- 各 cron 任务**独立运行**，靠"输出文件"间接传递（context_from 链）
- 无"被动感知"——任务不知道其他任务的产出（除非显式 context_from）
- 无"协商"——任务冲突（如两个任务写同一文件）可能互相覆盖

### AgentRadio 增强设计

| AgentRadio 概念 | 我们的实现 | 落地 |
|----------------|-----------|------|
| threads | cron 任务（各自独立） | ✅ 已有 |
| messages | 任务输出文件 + context_from | ✅ 部分（靠 cronjob context_from） |
| **wait-for-mention** | **轮询 output/ 目录 + 心跳状态** | 🆕 增强 |
| 五阶段分工 | cron 调度（错峰） | ✅ 已有 |
| **协商** | **冲突检测（同一文件多写者）** | 🆕 新增 |

---

## 3️⃣ 落地行动（按我们的实际情况）

### 🔴 P0（本周）
1. **显式任务链声明**：把现有的 cron 依赖关系写成"五阶段协议"文档（谁是上游/下游/谁整合）——参考 `cron-output-absorption` 已有雏形
2. **冲突检测**：审计是否有两个 cron 写同一知识文件（如 MOC-Research 被多个任务追加）——用 git log 查冲突历史

### 🟡 P1（2-3 周）
3. **wait-for-mention 落地**：给依赖型任务加"等待上游产出"逻辑（cronjob context_from 已支持，扩展到"产出未生成则跳过"）
4. **结果广播**：weekly-knowledge-consolidation 改为聚合本周所有任务产出（已是此功能，强化）

### 🟢 P2（长期）
5. **delegate_task 被动感知**：后台子代理完成任务后，主会话能感知结果并整合（现状：结果自动回到会话 ✅，增强：多子代理结果交叉验证）
6. **协商机制**：多任务写同一文件时，用"最后写入者 + git 合并"或"写前检查"防覆盖

---

## 4️⃣ 与现有系统衔接

| 现有机制 | AgentRadio 对应 | 增强点 |
|---------|----------------|--------|
| cronjob context_from | messages | 增加"产出未生成则跳过" |
| 错峰调度 | 分工 | ✅ 已有（15 分钟错峰） |
| cron-output-absorption | 结果广播 | 强化为聚合 |
| delegate_task 后台 | threads | 结果自动回主会话 ✅ |
| heartbeat-state.json | wait-for-mention | 可扩展为任务间感知 |

## 5️⃣ 验证方式

1. 本周：审计 cron 输出文件冲突（git log 查多写者）
2. 下周：给 1 个依赖任务加"等待上游产出"逻辑
3. 月度：统计任务链效率（产出物数量/冲突次数）

---
## 关联
- [[arxiv-week32-2026-08-02-study]] — AgentRadio 原始研究
- [[openmle-four-operators-methodology]] — 同批方法论（Crossover 产物）
- [[hermes-automation-patterns]] — cron 可靠性模式

---
*2026-08-02 · 从 AgentRadio 提炼 · 五阶段分工 v1*
