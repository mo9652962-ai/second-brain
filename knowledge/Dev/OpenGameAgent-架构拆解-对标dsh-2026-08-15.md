---
title: "OpenGameAgent 架构拆解 — 对标 DeepSeek Harness"
type: note
domain: Dev
status: active
tags: [knowledge/dev]
source: null
date: 2026-08-15
---
# OpenGameAgent 架构拆解 — 对标 DeepSeek Harness

> 研究日期：2026-08-15 | 来源：GitHub EricSun0218/OpenGameAgent（C#/.NET 8，Apache-2.0，⭐23）
> 状态：0.3.0-alpha.2（2026-07-28 创建 → 08-15 仅 18 天推到 alpha，378 文件 / 23 个 C# 项目）
> 定位：AI 原生游戏 / 自主 NPC / 交互世界的 agent runtime——「游戏代码对所有状态变更保持权威」

## 一句话

**两层架构**：`Kernel`（一个有状态的 model/tool loop，不知道 NPC/世界/引擎是什么）+ `GameLayer`（把 GameInput 变成 bounded kernel run 的游戏坐标层）。一切游戏特有能力都放 extension，kernel 契约优先稳定。

## 两层架构

```
Godot / Unity / .NET 游戏服务
        │ GameInput (bounded JSON + GameMoment)
        ▼
GameAgentRuntime ── 游戏坐标(session/actor/timeline/tick) · 路由 · 乐观持久化 · actor lanes
        │
        ▼
Kernel ── 有状态 model/tool loop（验证消息→bounded 请求→流式事件→验证工具→顺序/并发执行→steering→继续）
        │
        ▼
模型 API（provider 无关：Anthropic/Bedrock/Gemini/OpenAI/本地）
```

- **Kernel** 的规范值：typed content parts（text/json/resource/image_attachment/reasoning/tool_call）
- **GameLayer** 不拥有通用世界模型——上下文是游戏提供的 opaque JSON（回合制战略和实时模拟共用同一 runtime，不强制统一 schema）
- **GameAgentBuilder** 是组合根（一次性，运行配置不可被意外突变）；注册名带作用域 + 校验；extension 状态在 session 内命名空间隔离

## 三大核心机制深拆

### ① 游戏时间：GameMoment（dsh 完全没有的概念）

```csharp
GameMoment = timeline ID + signed 64-bit tick + 可选 calendar JSON
```

- **不是墙钟时间**——tick 的含义由游戏决定（回合/天/月/纪元/战斗帧/自定义日历）
- **Timeline ID 让存档分叉（save forks）显式化**：不同 timeline 的 moment 不能排序
- 记忆/触发器/调度都按游戏时间，但 mailbox 的操作租约用真实时长（保护并发 worker）
- `GameTimeScheduler.CaptureState()` 保存可恢复的循环触发位置——**读档不会重放已发出的触发**

**对标 dsh**：dsh 只有墙钟时间（session 内线性对话）。OGA 把「时间」做成一等坐标，NPC 可以「明天再来找你」而不用 hack。

### ② 多 NPC 并发：actor lanes（dsh 无对应）

- 每 `(session, actor)` 一个逻辑 lane：**同 actor 输入顺序执行，不同 actor 有界并发**（MaxConcurrentActors 上限）
- per-actor 队列有界；session 保存用 **expected revisions 检测冲突 writer**
- turn 内 `SafeParallel`：只读工具可重叠；共享 conflict key 的写串行化；**结果按 model source order 追加**（完成时序不搅乱 transcript）
- 大世界不该每帧调每个 NPC——**让确定性游戏模拟决定哪些 actor 需要推理，再入队**（GameTimeScheduler/GameSignal/IGameMailbox 是准入层积木，不是隐藏全局模拟策略）

**对标 dsh**：dsh 是单会话线性；subagent 是独立进程不做内存共享。OGA 是「一个进程内多角色并行 + 冲突控制」——游戏模拟的天然需求。

### ③ 动作幂等：journal + receipts（dsh 的软肋）

```
model tool call
  → JSON Schema 验证
  → GameActionIntent 记入 journal（Prepared）
  → 游戏处理器验证规则 + 期望 revision
  → 游戏状态事务
  → GameActionReceipt 存储（Dispatched → receipt）
  → receipt 返回模型
```

- **默认版本化操作身份**：session + actor + stable game input ID + action + timeline/tick + save generation + model turn + tool-call source index
  - 同一逻辑调用重放 → 身份稳定 → 返回已存 receipt
  - 跨 actor/session/action/save generation → 不可能碰撞
- **不确定就不重复**：进程在 dispatch 后 receipt 前失败 → `RecoverAsync` 让游戏调和 → 框架报 `Uncertain`——**绝不把取消/超时变成「允许重试写」**
- 只读/幂等工具可直接走 kernel；非幂等状态变更必须走 DurableGameActionDispatcher + 持久 journal
- workflow checkpoint 绑定 workflow/session/actor/canonical input——**同一中断输入可恢复；不同输入被拒**直到未完成调用 settle

**对标 dsh**：dsh 工具调用（尤其 terminal 写文件/外部副作用）如果进程挂掉，重试可能重复执行。OGA 的 journal+receipt 是生产级解法——「无法证明结果 = Uncertain，绝不 silent retry」。

## 上下文工程（值得抄的设计）

| 设计 | OGA | 借鉴价值 |
|:---|:---|:---|
| 上下文准入时机 | 首个请求前 + 工具轮后 + 最终请求 hook 后——**hook 不可能绕过配置的上下文窗口** | Hermes 的 hook 系统可以参考（现在 hooks 注入点较少）|
| system prompt 排序 | 最可复用字节在前：base → skills → mutable game context——**保持最长 provider-cache 前缀** | 与 Hermes「prompt caching 神圣」原则同源 |
| 大结果物化 | 大 text/JSON 工具结果移到 artifact store，替换成 bounded handle + preview | Hermes 的三层截断已有类似思路 |
| 压缩 | 保留完整对话后缀、**绝不拆工具交换** | 同 Hermes 压缩原则 |
| 记忆与上下文分离 | IGameMemoryStore 存储/过滤，**游戏代码决定哪些记忆变成 context slice**——不静默插入陈旧/私有记忆 | 与 Mnemon 共享记忆防污染完全同构！ |

## 对标 dsh 总结表

| 维度 | DeepSeek Harness（dsh）| OpenGameAgent |
|:---|:---|:---|
| 语言/框架 | TypeScript / Cordis 插件 | C# / .NET 8 |
| 核心 | agent loop + 事件溯源会话 + 工具注册表 | kernel loop + 游戏坐标层 |
| 时间 | 墙钟时间 | **timeline + tick 一等公民** |
| 并发 | 单会话线性 / subagent 独立进程 | **per-actor lane + 有界并发 + conflict key 串行** |
| 幂等 | 无内建（重试可能重复副作用）| **journal + receipts + Uncertain 语义** |
| 权威边界 | 审批/沙箱门控 | 游戏业务代码是唯一 mutation 裁决者 |
| 记忆 | 会话日志 + Mnemon 插件 | IGameMemoryStore + 可选向量索引 |
| 缓存优化 | 有（前缀稳定）| 显式 system prompt 字节排序 |
| 部署 | CLI/桌面/headless | Godot/Unity/.NET server/独立服务 |
| 版本 | 稳定 | 0.3.0-alpha.2（API 会变）|

## 19 天推到 alpha 的节奏拆解

1. **范围克制**：不建世界模型/角色卡/战斗系统——那些归游戏；kernel 契约最小化、优先稳定
2. **文档先行**：README/ARCHITECTURE/DESIGN/features 一应俱全，决策有据可查
3. **分层隔离**：核心（kernel）vs 扩展（extensions）物理分开——新能力进扩展，不动 kernel
4. **诚实标注**：README 明示 alpha、API 会变、引擎适配只在 Windows editor 验证——不吹生产可用
5. **工具链完整**：CI 绿 + 测试存在（kernel/persistence/models tests）+ NuGet 发布

**可借鉴**：Hermes 项目如果要接游戏/多角色场景，OGA 的「action journal + Uncertain」和「actor lane」是两个可直接吸收的模式；「kernel 稳定优先，功能进扩展」与 Hermes 的「core 窄腰」哲学同构。

## 结论

OGA 不是 dsh 的替代，是**同一架构族在游戏领域的分支**。它解决的三件事（游戏时间/多 NPC 并发/动作幂等）恰好是通用 agent runtime 缺的生产级坐标。作为架构学习素材价值高；生产使用等 1.0。

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
