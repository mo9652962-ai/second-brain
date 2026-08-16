---
aliases:
  - 2026-08-14-card-prime-agent-rlm
tags:
  - knowledge-card
  - ai-agent
  - RLM
  - self-improving
  - Hermes
created: 2026-08-14
source: "[[knowledge/Dev/prime-agent-rlm-2026-08-14]]"
status: fresh
---

# 🃏 知识卡片 · Prime Agent：自改进 RLM Agent 登顶本周 GitHub 热榜

> **来源**：PrimeIntellect-ai/prime-agent（本周 GitHub Trending 增长第一 15,753⭐ +12,476）· 2026-08-14 · ✅ 已读源笔记
> **一句话**：一个「把上下文当变量、把工具当函数、靠 /refine 小步自改进」的常驻 Agent——架构理念与 Hermes 一一对应，是 2026 下半年「自改进 + 长寿 Agent」主战场的代表性开源实现。

---

## 核心洞察

| 维度 | 内容 |
|------|------|
| RLM 抽象 | 上下文是变量、工具/子代理是函数调用（`rlm(...)`），一切跑在持久 IPython REPL 里 |
| Continual Harness | 记忆/技能/子代理规格存为持久状态；`/refine` 做**小步、证据驱动、可回滚**的自我改进，绝不重写基础系统 prompt |
| Skills = 代码 | 技能是可导入的 Python 包，可被模型创建/调用，而非纯文档 |
| 长寿配方 | 持久目标 + 心跳 + 调度 = 跨 turn 保持进度（对应 Hermes 的 cron + todo + 后台进程） |
| 论文支撑 | arXiv 2605.09998，非纯营销项目 |

## 与 sora 体系的对照

| Prime Agent | Hermes 对应 | 结论 |
|:---|:---|:---|
| /refine 自改进 | memory / skills 自举 | ✅ 同源，方向被验证 |
| rlm() 子代理 | delegate_task | ✅ 已有 |
| 心跳 + schedule | cron 调度 | ✅ 已有 |
| SKILLS 可导入包 | 本地 skills 库 | ⚠️ sora 以 markdown 为主，可把验证过的流程沉淀成 scripts/ |

## 行动项

- [x] **借鉴 /refine 纪律**：改 skill 时只 patch 局部、保留回滚快照、不动 SOUL 基础 prompt → ✅ **2026-08-14 已采纳**：suggestion-implementation skill 新增「技能编辑纪律」章节（备份 `/tmp/suggestion-implementation-SKILL.md.bak-20260814`）
- [x] **持久目标机制**：评估给 Hermes 加「目标跨 turn 持久化」的显式机制（如 todo 升级为 /goal）→ ✅ **2026-08-16 已评估结案**：**Hermes 已原生支持 `/goal`**（Ralph loop，参考 [Persistent Goals 文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)）——跨 turn 持久化 + judge 自动判断 + completion contract + `/subgoal` + quality gates + `goals.max_turns` 配置，状态存 SessionDB.state_meta 可跨 /resume。**无需自建，直接用即可**（todo 用于会话内任务列表，/goal 用于跨 turn 持续目标，二者互补）
- [x] **技能代码化方向**：把高频验证过的流程从 markdown 沉淀为可执行 scripts/ → ✅ 持续进行（验证过的流程继续 scripts/ 化）
- [ ] 跟踪 prime-agent 生态（pi），验证「RAG 检索 + 思考」模式对长任务的实际收益 → ⏳ 周期跟踪项（github-weekly 顺带看）

## 为什么重要

- **时效性**：本周 GitHub Trending 增长第一（+12,476/周），「自改进 + 长寿 Agent」被验证为 2026 下半主战场
- **强相关**：与 sora 正在用的 Hermes 架构几乎一一对应——不是陌生新东西，而是「自家体系的开源镜像」，拿来对照就能找到改进点
- **可行动**：/refine 的「小步、证据驱动、可回滚、不动基础 prompt」纪律可以直接应用于日常 skill 维护，零成本落地

---

*卡片来源：当天知识库精选 · [[knowledge/Dev/prime-agent-rlm-2026-08-14]]（🥇 GitHub 热榜增长第一 + 与 Hermes 体系直接对标 + 4 条可落地行动项）*
