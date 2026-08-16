---
tags:
  - hermes
  - reliability
  - model-fallback
  - audit
created: 2026-08-16
status: applied
---

# Hermes 模型容灾链审计 · 2026-08-16

> 来源：Behavioral Contracts II（arXiv 2608.12895）实证结论「同模型冗余 = 没有冗余」→ 对 Hermes 容灾链做专项审计。
> 结论先行：**生效配置无「同供应商多模型」组合，符合论文正解；发现 1 处旧配置风险 + 1 个已知权衡。**

## 审计对象与结论

| 配置 | 链 | 审计结论 |
|:---|:---|:---|
| **生效配置** `AppData/Local/hermes/config.yaml` | default: `doubao-seed-2-0-pro` (fangzhou-1) → fallback: `jiyuanlvdong/deepseek-v4-flash` → `keylink/deepseek-v4-flash` | ✅ **三家独立供应商**，无同供应商多模型组合。跨 relay 真兜底设计正确 |
| **旧配置** `~/.hermes/config.yaml`（非当前生效，8-15 修改） | default: `kimi-k2.7-code` (moonshot) + failover chain: `kimi-k2.7-code → kimi-k2.6`（**同供应商 moonshot**） | ⚠️ **违反论文结论**：同模型/同供应商 failover = 90% 会同败。若未来启用此文件需改造 |

## 生效链的已知权衡（跨 relay 兜底理由，文档化）

`jiyuanlvdong flash → keylink flash` 是**同模型跨 relay**：

- ✅ **防 relay 故障有效**：基元律动 tokenrhythm.studio 服务挂/限流/封 key → keylinkclub 独立通道接管，模型能力不变。这是日常高频风险（relay 稳定性），sora 的「跨 relay 真兜底」意图正确（记忆 2026-08-14 已记录，glm-5.2 弃用后保持双 relay flash）
- ⚠️ **防模型级故障无效**：若 DeepSeek 官方 API 整体故障/模型下架，两个 relay 转发同一模型会**同时失败**——论文 15/15 null result 印证「只换厂商不换模型也不降关联」
- 结论：当前链覆盖「relay 故障」场景，未覆盖「模型级故障」场景。**可接受的权衡**（模型级故障概率远低于 relay 故障，且主模型 doubao 本身就是异模型首层兜底）

## 建议（可选项，不强制）

| 优先级 | 动作 | 理由 |
|:---|:---|:---|
| P2 | 若未来要覆盖模型级故障：fallback 加一个**异模型** relay（如 keylink 的 claude / fangzhou 的 doubao 备用） | 论文核心结论：换模型 + 换厂商才是有效去冗余 |
| P3 | 清理/改造 `~/.hermes/config.yaml` 旧配置的 moonshot failover 链（同供应商） | 防止未来误启用 |
| P3 | 健康检查可加「同源失败」信号监控（φ 系数） | 论文建议：监控同模型多通道是否同败 |

## 验证记录

- `hermes config get default_model` → `doubao-seed-2-0-pro`（生效文件确认）
- Python yaml 解析生效配置 fallback_model：jiyuanlvdong + keylink 两条，base_url 独立
- 生效配置无 failover 段（failover: None）；旧配置有 failover chain

## 关联

- [[knowledge/cards/2026-08-16-behavioral-contracts-reliability]]（行动项 1 ✅ 已执行）
- [[knowledge/Research/arxiv-2026-08-16-core-contributions]]（待办 2 ✅ 已执行）
- 论文：Agent Behavioral Contracts II arXiv 2608.12895

---
*生成: k (Hermes) · 2026-08-16 · 建议落实 cron 自动执行*
