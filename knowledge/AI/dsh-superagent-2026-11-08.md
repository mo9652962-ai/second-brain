---
tags: [github, W45, ai, agent-architecture, deepseek, dsh, super-agent, 方法论]
aliases: [dsh-superagent, Super-agent, DeepSeek 超级 Agent]
date: 2026-11-08
source: https://github.com/deepseek-ai/dsh-superagent-prototype
status: watching
---

# dsh-superagent — DeepSeek 的「超级 Agent」两层架构原型

> W45 精选。DeepSeek Harness 团队 2026-11-01 发文章《Exploring Super-agent Design: Towards a More Autonomous Agent System》并开源参考实现。**核心主张：编码 agent 的瓶颈已经从模型能力转移到人的注意力**——一个人通常只能同时盯 3~5 个活跃会话。
> 甄别结论：**20,933★ / 1 commit / 1 contributor / 37KB / MIT**。star 来自 DeepSeek 品牌 + 文章，代码是「研究原型，非官方产品」——**价值在 docs/ 的架构与授权模型，不在代码可直接复用**。

## 一句话定位

把一个 coding agent 从「单会话、人盯着跑」改成「常驻实体」：常驻 Router 层接所有人机交互与派发，Worker 层在隔离上下文里并发干活，事件驱动（Trigger）让它主动、Watchdog 让它持久。

## 四特性 × 五模块

| 四特性 | 含义 |
|:--|:--|
| Continuous 连续 | 用户在 IM / GitHub 评论里直接说话，感觉只有一个 agent，不用管「信息在哪个 session」 |
| Productive 高产出 | 不等上一条命令跑完就接下一条，多任务并行 |
| Proactive 主动 | 持续观察环境事件，该动的动，不需要干预时保持安静 |
| Persistent 持久 | 常在线，直连真实工作环境，长跑异常自动恢复 |

| 五模块 | 作用 |
|:--|:--|
| ① 两层架构 | Router 层只做交互与全局协调（**不执行具体任务，甚至可能没有 Bash 工具**，避免成瓶颈）；Worker 层上下文隔离、工具齐全、用最强模型 |
| ② 事件驱动 | 输入从「人打的 prompt」换成环境里的半结构化 Trigger（群消息/邮件/日历/PR 评论/CI 结果） |
| ③ 全双工人机交互 | 多通道路由 + 回复归口到 Router，避免多个 session 各自回话造成混乱 |
| ④ 计算/状态/环境分离 | 会话状态外置，换设备/重启能接上 |
| ⑤ Watchdog | 主系统之外的独立控制回路，负责长跑自愈（内部逻辑救不了自己） |

## 值得抄的四个机制细节

1. **两层分工的本质是「全局序列点」**：Router 是跨任务的记忆与协调点，所以它必须便宜、常驻、不被任务拖住。Worker 是吞吐来源，所以它必须隔离、并发、用强模型。
2. **两阶段过滤（代码 + 模型）**：先用确定性规则砍掉大量噪声事件，再让模型判断剩下的事件值不值得动手——成本与误报的折中。
3. **Inline & Spill + Chain of Recall**：信息密度高的上下文内联，长的落盘（spill），需要时按链条召回——与 claude-mem 的「索引→时间线→详情」是同一个思路的两种实现（见 [[knowledge/AI/claude-mem-2026-11-08]]）。
4. **投机执行（speculative execution）**：根据环境信号在后台提前做，等确认后再交付——省的是人的等待时间。

## 授权模型（这篇最被低估的部分）

`docs/002-authorization.md` 把「谁能让它干活、干到什么程度」拆成了可执行的表：

- **两条路径**：Eval（判断要不要开工）与 Subscription（已开工的线程继续收上下文，**只给上下文、不给新权限**）
- **强度三档**：`explicit`（白名单的人直接点名）/ `inferred`（非白名单的人在已有工单线程里追问）/ `not admitted`（其他 bot、被忽略的、以及 accept mode 关闭时的所有推断）
- **准入表（admission table）**：按接收范围（每个飞书群、其他群、私聊）逐格配置
- **Mandate**：每张工单自带授权边界，Executor 越界只能「交回」，不能自己扩权
- **恢复前重校验**：长时间挂起后恢复，要重新过一遍权限
- **消息是输入不是命令**：文档明确写「消息、评论、引用的文档都是决策输入，不能改权限」——**这就是 prompt injection 的架构级防线**

## docs/000-philosophy.md 的五条行为约束（直接可搬到 k 身上）

> 核心原则：**Take as little human attention as possible, and give as much value as possible.** 每条消息、通知、提问、设置、面板元素、文档段落都在花别人的注意力，花得比给的多就删掉。

1. 只在被要求时动手，或有团队写下的规则允许时动手；没人要的活先跑「只记录不执行」模式
2. 只在「人必须行动」或「结果可用」时说话；确认一次、干活时闭嘴、出结果再说话
3. 一次只问一个具体问题，用结构化形式，别把问题埋在长报告里
4. 按影响停，不按努力停：局部改动做到可评审；需要设计决策就停下来问
5. 诚实报告：草稿标未完成，失败就说失败，**绝不为了不问而绕过限制**

设计侧同理：少概念（只有 Source 这类领域概念）、少设置（一个默认值能覆盖就别做成开关）、面板只显示「需要人」的事、文档按编号顺序读。

## 原型形态（能跑的那部分）

- 一个仓库一个 agent，打包成 DeepSeek Harness bundle
- 监听 GitHub（可选飞书）→ 有人请求就开 work item → **在自己的 agent session 和自己的目录里干** → 回到原会话回话（通常是 PR）
- Web 面板只列「等人处理」的项
- `pnpm check` = typecheck + test + build

## 💎 可借鉴点

| 借鉴 | 映射到 sora 的现状 | 落地动作 |
|:--|:--|:--|
| Router / Worker 分工 | Hermes cron 目前是「调度 + 执行」混在一起；`delegate_task` 已是 Worker 雏形 | 给 cron 任务定规矩：**调度型任务不干重活**，重活一律 delegate；cron 只负责「谁、在哪、干什么」 |
| 注意力预算 | 当前 12+ 个 cron 每天推消息，sora 的注意力是稀缺资源 | 每个 cron 输出加「是否值得打断」判定：无新增 → `[SILENT]`；有新增 → 结论置顶 3 行 |
| 授权表 + 强度三档 | Hermes 已有 L0-L4 验证等级（见本机 skill `hermes-codex-security-gate`，未入库） | 把「谁说的」写进任务上下文：sora 本人 / 外部内容 / 工具输出，强度不同，外部内容一律不当指令 |
| 消息是输入不是命令 | SOUL.md 已有「只信 OUT-OF-BAND 标记」 | 继续强化：网页/README/Issue 里的文字只当资料，不触发动作 |
| 一次一个问题 | 与 SOUL.md「一次最多问一个问题」一致 | 已在执行，无需改 |
| 按影响停 | 与「3 连败即停 / 长任务设检查点」同源 | 保持 |

## 评价

| 维度 | 判断 |
|:--|:--|
| 技术含金量 | ★★★★★（架构与授权模型是系统设计级的，不是 prompt 技巧） |
| 代码可复用 | ★☆☆☆☆（1 commit，研究原型，作者自己写「may still contain bugs」） |
| 文档价值 | ★★★★★（docs/000-008 按序读，等于一份 agent 系统设计教材） |
| 建议 | **读文档不装代码**。把 philosophy + authorization 两篇的规则吸收进 Hermes cron 设计与 k 的行为准则 |

---
*W45 · 2026-11-08 · 观察：star/commit/README/docs 均已实读；推断：Hermes 可映射部分；未知：未跑通原型（需 dsh bundle 环境）*
