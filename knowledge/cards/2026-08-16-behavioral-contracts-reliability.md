---
aliases:
  - 2026-08-16-card-behavioral-contracts-reliability
tags:
  - knowledge-card
  - ai-agent
  - reliability
  - model-fallback
  - Hermes
created: 2026-08-16
source: "[[knowledge/Research/arxiv-2026-08-16-core-contributions]]"
status: fresh
---

# 🃏 知识卡片 · 同模型双 Agent 90% 会同败——「换模型才算冗余」的实证依据

> **来源**：arXiv 2608.12895 Agent Behavioral Contracts II（08-13 提交池）· 2026-08-16 入库 · ✅ 已读源笔记 + 全文 HTML 验证
> **一句话**：预注册 18,000 个双 Agent 交接任务实测——同一个模型的两个实例在 90% 的失败任务上会同败；组合可靠性「各组件可靠性相乘」的独立假设被实证拒绝，**同模型冗余 = 没有冗余，只换厂商不换模型也不降关联**。

---

## 核心洞察

| 维度 | 内容 |
|------|------|
| 实测数字 | 同模型对同败率 **90.0%**（log OR 6.66，φ=0.916）——正依赖使联合失败远高于独立乘积 |
| 换模型 | 6/6 对比关联显著降低 → 模型级差异是有效的去冗余手段 |
| 只换厂商 | 注册 null 结果（15/15 空对照）→ 厂商多样性 ≠ 可靠性，需同时换模型 |
| 方法论 | 预注册 + 确定性代码评分 + 无 LLM 判官 = 评估黄金标准 |
| 证书替代 | 假设自由的可靠界常为 0；拟合依赖模型理论证明更糟（数据越多覆盖越差）；正解是有限样本 LP 证书 |

## 对 sora 的影响

1. ✅ **现有配置已被实证背书**：Hermes 模型 fallback 链 = jiyuanlvdong flash → keylink flash，是**跨 relay 独立供应商**组合（换模型 + 换厂商）——正是论文结论的工程正解
2. ⚠️ **同模型冗余被过度信任**：若将来用「同一模型的两个实例」做冗余/重试/双保险，等于没有冗余；健康检查可借鉴 φ 系数监控「同源失败」信号
3. 💡 **方法论可复用**：预注册 + 确定性评分（无 LLM 判官）可直接用于 Hermes 自评/技能评测，比 LLM 自评更硬

## 行动项

- [x] **结论已落地**：现有跨 relay 独立供应商 fallback 链符合「换模型才有效」结论（配置先于论文做对了）
- [x] **审计 + 文档化**：审计 Hermes 模型容灾链，确认无「同供应商多模型」组合，并把「跨 relay 兜底理由」写进配置文档（待办）→ ✅ **2026-08-16 已执行**：审计结论=生效链三家独立供应商 ✓，跨 relay 兜底理由已文档化于 `knowledge/Dev/hermes-model-fallback-audit-2026-08-16.md`；发现旧配置 `~/.hermes/config.yaml` 有 moonshot 同供应商 failover（P3 待清理）
- [x] **方法论沉淀**：预注册 + 确定性评分方法论 → 补进 agent-self-evaluation 技能参考（待办）→ ✅ **2026-08-16 已执行**：ecc-agent-self-evaluation 新增「预注册 + 确定性评分方法论」章节（三要素 + 评估用法 + 自检问题），备份 `.temp/skill-bak/agent-self-evaluation-SKILL.md.bak-20260816`

## 为什么重要

- **生产资产独立验证**：正在每天使用的模型容灾链设计，获论文级实证背书——「配置做对了」从经验判断升级为有量化依据（同类入选：08-09 DeepSeek V4 Flash ARC Prize 卡）
- **硬数字可作内容素材**：90% 同败、φ=0.916 这类反直觉数字适合 AI 博主选题（「为什么你的双保险不是保险」）
- **PawBench 教训呼应**：「工具/harness > 模型」之外，模型共享本身也是可靠性变量

---

*卡片来源：当天知识库精选 · [[knowledge/Research/arxiv-2026-08-16-core-contributions]]（🥈 Behavioral Contracts II——生产资产独立验证 + 硬数字 + 可行动；🥇 Reconcile Once 知识管护防漂移为亚军）*
