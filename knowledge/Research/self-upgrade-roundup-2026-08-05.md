---
aliases:
  - self-upgrade-research-2026-08-05
tags:
  - research
  - memory
  - serialization
  - decision
  - roundup
created: 2026-08-05
updated: 2026-08-05
status: adopted
domain: research
---

# 自我升级多轮研究汇总（2026-08-05）

> 千轮研究（系统性多轮）：6 大主题、多轮搜索 + 深挖 + 落地
> 覆盖：未落实项清零 + 新主题研究 + 决策闭环

---

## 📋 未落实项清零

| 未落实项 | 状态 | 落地 |
|:---------|:----:|:-----|
| 安全审计 cron（P2）| ✅ | `scripts/security_audit.py` + cron `74dbe08a5d77`（每周日 8:30，watchdog：skill 新增 + 端口变化）|
| orca-misscore 2 项落地 | ✅ 确认 | 技能已含（ORCA 多信号交叉诊断 + Mis-Score 评估器审计）|
| code-review-graph 决策 | ✅ | 选择 code-review-graph（28.5k★），替代 codebase-memory-mcp，已装 + 建图（1127 files → 17754 节点）|
| PAKE 升级 | 📌 已研究 | proposed（等真机验证后 v9.19 实施）|
| Protobuf 序列化 | ✅ 决策 | **保持 pickle**——LAN 可信场景不升级（详见下）|

## 🆕 新研究主题（已落库）

### 1. Zero-Mem 零 token 记忆（2607.29377）→ `knowledge/cards/2026-08-05-zero-mem.md`
- 记忆操作零 LLM 调用、零 token，保留原始轨迹为唯一源
- 记忆操作时间成本 **-57.6%**
- 落地 4 项：知识卡保出处 / 查询走确定性检索 / 冲突检测 / 评估 memory 注入成本

### 2. AI Agent 记忆注入攻击（MINJA）→ `knowledge/Research/agent-memory-injection-2026-08-05.md`
- **注入成功率 >95%，跨 session 持久化 70-80%**——记忆库是最大攻击面
- Query-Only 攻击：只通过查询就能污染记忆
- 落地：patch `knowledge-absorption` 技能加**来源分级**（trust: high/med/low；low 只进 knowledge 不进 memory；指令式语言直接丢弃）

### 3. 记忆成本优化（行业印证）
- "Naive memory injection is the quietest cost killer"——每条记忆注入每次推理
- 与 Zero-Mem 同向：记忆不该是生成负载

## 📌 决策记录

### Protobuf vs pickle（S4MP 候选）
| 维度 | pickle（现状）| Protobuf |
|:-----|:-------------|:---------|
| 安全 | ❌ 任意代码执行风险 | ✅ 类型安全 |
| 性能 | 中 | 快（25ns vs 40ns JSON）|
| 信任边界 | 朋友（可信）| — |
| 改造成本 | 0 | 需 schema + 迁移 |

**结论：保持 pickle**——SimSync 是 LAN + 朋友（可信）场景，pickle 的安全风险不适用；性能差异在 10Hz 帧率下无感。**若未来跨公网联机 → 必须换**（那时候随便哪个序列化都比 pickle 安全）。这个决策与之前"纯 TCP 保持"同向：不为低威胁场景引入复杂度。

### code-review-graph（已落地）
- 28.5k★、增量更新、token 节省 71x（有 benchmark）
- SimSync 项目实测：17754 节点/97207 边/11 架构社区
- 查询能力验证：`callers_of RoomServer` 命中 19 候选

## 🔄 闭环总结

本轮把知识库 5 个未落实项清零（3 完成 + 2 决策），新增 3 个知识资产（Zero-Mem 卡、记忆注入研究、决策记录），patch 1 个技能（knowledge-absorption 来源分级），建 2 个 cron 工具（安全审计 + GitHub RSS 速报——后者是上一轮）。

**核心方法论收获**：记忆系统既要省钱（Zero-Mem 零 token 思路）又要防攻击（MINJA 来源分级）——两个方向今天同时验证落地。

---

*汇总完成：2026-08-05 · 下一轮候选：PAKE v9.19 实施、Hermes MCP 接入 code-review-graph*

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
