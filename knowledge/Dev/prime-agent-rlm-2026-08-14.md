---
tags: [ai-agent, RLM, self-improving, long-running, 记忆工程, skills]
aliases: [prime-agent, RLM, Recursive Language Model, Continual Harness]
date: 2026-08-14
source: https://github.com/PrimeIntellect-ai/prime-agent
status: watch
---

# Prime Agent — 自改进 RLM 编码/研究 Agent

> **简介**：PrimeIntellect 开源的编码与研究 agent，本周 GitHub Trending 增长第一（15,753⭐ **+12,476/周**，TypeScript，MIT，4509 commits，非常活跃）。核心定位：*self-improving RLM agent for coding workflows and long-running autonomous tasks*。与 Hermes 的 memory/skills/cron/subagent 理念几乎一一对应，是最值得拆解的架构。

## 两个核心抽象

### 1. Recursive Language Model (RLM)
把「上下文」和「工具调用」当程序构造：
- **`prompt-as-a-variable`**：上下文（prompt）是变量，不是一次性贴进窗口的文本
- **`programmatic tool/sub-agent calling`**：工具如递归子代理（`rlm(...)`）是**函数调用**，返回结果可编程接收，不是文本拼接
- 一切运行在**持久 IPython REPL** 中——持久 Python 是模型的唯一内置工具，文件/命令/工具/子代理/上下文管理都通过代码完成

### 2. Continual Harness（持续框架）
- 把补充 prompt、**记忆**、技能描述、可复用子代理规格存为**持久状态**
- `/refine` 审查当前轨迹，应用**小规模、有证据支持的更新**到 harness 状态
- **绝不重写不可变的基础系统 prompt**；记录快照支持回滚
- 论文：arxiv.org/abs/2605.09998

## 关键特性（→ 对应 Hermes 概念）

| Prime Agent | Hermes 对应 | 说明 |
|:---|:---|:---|
| `/refine` 自改进 harness | memory / skills 自举 | 小步、证据驱动、可回滚 |
| Skills = 可导入 Python 包 | 本地 skills 库 | 技能是代码，可被模型创建 |
| `rlm(...)` 真实子代理 | delegate_task | 并行/后台，结果程序化返回 |
| daemon 后台会话可重附 | 后台进程/cron | 检测到独立会话 |
| `/goal` 持久目标 | todo | 跨 turn 保持进度 |
| `/heartbeat` 心跳 + `schedule` | cron 调度 | 定时重回会话 |
| agent 间直接通信 | a2a | 绕过用户编排 |
| `/autonomous` 有界自主模式 | 自主 agent | turn/token/时间预算 + 质量门 |

## 架构
```
daemon(常驻) → worker → kernel(持久 IPython)
                    └── rlm() 递归子代理
                    └── skills(可导入包) / goals / memory(harness 状态)
                    └── /refine 自我精炼(回滚快照)
```

## 💎 可借鉴点（对 Hermes/vault 最值）
1. **「一切皆程序化」的工具抽象**：模型唯一内置工具是持久 IPython——这比 30+ 工具列表更简洁，模型通过代码表达意图。Hermes 可借鉴「把常用文件操作/命令封装成可编程 kernel」的思路，reduce tool 数量。
2. **`/refine` 的自改进纪律**：小步、证据驱动、可回滚、**不动基础系统 prompt**。与「skills 自举」完美同源（参见 openmle-four-operators / self-improving-agent 技能）——可落地为：Hermes 每次迭代改进 skill 时只 patch 局部，绝不重写 SOUL，保留回滚快照。
3. **SKILLS 是「可导入包」而非文档**：技能 = 代码 = 可被模型创建/调用。sora 的 100+ skills 目前是 markdown 为主，可考虑把验证过的流程沉淀成可执行脚本（已有 scripts/ 目录，方向一致）。
4. **持久目标 + 心跳 + 调度** 组合即「长寿 agent」配方，Hermes 的 cron + todo 已覆盖，缺的是「目标跨 turn 持久化」的显式机制。

## 综合评估
| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★★（RLM 抽象 + Continual Harness 论文支撑）|
| 与 sora 工作流关联 | ★★★★★（memory/skills/cron/subagent 全对应）|
| 值得安装 | 🟡 观察——不急着装（Hermes 已覆盖大部分能力），但 RLM 抽象值得长期跟踪 |
| 趋势判断 | 自改进 + 长寿 agent 是 2026 下半主战场，prime-agent/pi 生态值得关注 |

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]] · 平行参考：[[mattpocock-skills]] · [[codebase-memory-mcp]]