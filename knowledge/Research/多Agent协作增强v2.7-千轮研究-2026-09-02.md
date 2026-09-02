---
created: 2026-09-02
tags: [multi-agent, 千轮研究, 交接结构化, 上下文工程, 编排]
valid_from: 2026-09-02
type: research-note
---

# 多Agent协作增强 v2.7：交接结构化 + 上下文工程补全

> 千轮研究第二轮落地。核心命题：**多 agent 交接的「表示形式」比压缩率更决定下游成败；上下文工程是比提示工程更根本的杠杆。** 与 v2.6（GPT+Codex eval v2）、v1.5（payload-by-reference + Task Ledger）、v1.4（协作税）形成体系闭环。

## 一、核心发现：结构化交接 > 叙述压缩（硬数据）

两 agent 中继场景（Researcher 审计固定库存 → Booker 仅凭交接 payload 做精确约束决策，50 实例穷举真值）：

| 交接表示 | 可行性准确率 | 压缩比 |
|:---|:---:|:---:|
| 结构化 JSON 提取 | **0.96** | 0.738 |
| 嵌入剪枝 | 0.88 | - |
| 无压缩（全轨迹）| 0.88 | - |
| 叙述摘要（250 词）| **0.48** | 0.333 |

**教训**：叙述摘要压缩最狠但可行性崩一半——压缩丢掉了约束关键证据（淘汰理由、禁令）。**派活时 prior findings 必须结构化（结论/约束/已排除/待验证四字段），不用自然语言段落。**

## 二、落地规则（已进 multi-agent-research 技能 v2.7）

### 规则 1：prior findings 结构化四字段
```
- 结论: <3-5 条已证实事实，每条可独立验证>
- 约束: <必须满足的硬条件，如「>=3 独立源」「不得触碰 X」>
- 已排除: <试过不成立的路径 + 一句原因，防下游重踩>
- 待验证: <拿不准需下游查证的点>
```

### 规则 2：Typed Handoff（机器可校验交接契约）
交接不传自由文本，传类型化 payload，校验失败立即抛错而非静默传坏数据。必含字段：
`task_summary(≤500字) / provenance / constraints / acceptance_criteria / history_strategy(默认summary+pointer) / idempotency(非幂等max_retries=0) / loop_guard(防A↔B死循环)`。

适用：多字段交接（>2 字段）必须结构化；单字段小交接保持轻量。

### 规则 3：Routed Handoff（按任务类型选交接格式）
155-token 轻量 router（0.15% 开销）在两种格式间选择：
- 依赖链任务（数据管道/多步计算）→ **结构化 DAG**（depends_on 显式，+8.7~12.7pp）
- 开放/创意任务 → **自然语言**（回归为 0）
- 关键坑：结构化 DAG 必须带 graph-aware executor prompt，否则接收方当死数据看（+12.7pp 全靠这个）

### 规则 4：上下文工程三件套补全
已有预算槽+子代理隔离，补两块：
- **Narrative Casting**：子代理接棒时前序 agent 消息重述为叙事上下文（`[For context]: Agent B said...`），工具调用标记归属——防角色混淆
- **存储-视图分离**：知识库/memory = Session（持久），任务包 = Working Context（每调用重建）——任务包只带当前决策最小视图
- **include_contents 粒度**：handoff 默认 none+selected，下游只见新 prompt + 必要 artifact，不见祖先全史

## 三、编排新证据：工作流结构 > agent 数

- 对齐协议评测（10 基准，GPT-4.1）：6 个多 agent 系统最多 1 个略超单 agent（+1.44pp 且在误差内），其余落后 2.56-11.29pp
- **agent 数不解释性能，任务-协议匹配才解释**：可验证输出→Debate；独立并行子域→Parallel；长链结构化→Pipeline
- 等 token 预算下单 agent ≥ 多 agent，**除非单 agent 上下文利用退化**（掩码/替换/干扰时 MAS 才翻盘）——这正是外部 agent 独立配额/独立上下文的价值

## 四、成本-精度混合配置

1 万份金融文档实测：reflexive 最高精度但 2.3× 成本；**层级编排 + 语义缓存 + 模型路由 + 自适应重试 = 恢复 89% 精度差 @ 仅 1.15× 成本**。
- 层级编排（supervisor-worker）在成本-精度 Pareto 前沿最优——与我们 v1.3 已有架构一致，有第三方实证
- 语义缓存可推广：多 agent 同参数同源查询 → 缓存（TTL 短防陈旧），我们 web-search 语义缓存已验证此机制

## 五、落地状态

- [x] multi-agent-research 技能 v2.7 已更新（完整章节）
- [x] 结构化密任务包模板 `templates/handoff-packet-v2.7.md`（含 Typed Handoff 契约元数据 + Narrative Casting 块）
- [x] 校验脚本 `scripts/check_handoff_packet.py`（好包 0 警告通过 / 坏包禁止派发，双测通过）
- [x] 实测派活：用 v2.7 模板写真实任务包（web-search 缓存 quota 验证）派 delegate_task 子代理，验证结构化交接有效性
- [ ] 观察：长链任务（Codex 多步）是否用 structured 交接减少返工

## 关联

- [[多Agent协作增强-千轮研究-2026-08-30]]
- [[多Agent协作建议书v3.0-学习落实-2026-08-31]]
- skill: multi-agent-research v2.7
