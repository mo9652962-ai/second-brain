---
aliases:
  - deepseek-v4-flash-0731
tags:
  - models
  - deepseek
  - agent
  - pricing
  - daily
created: 2026-08-06
source: user + 36kr/DeepSeek官方
status: active
---

# DeepSeek V4-Flash 正式版 — Agent 能力暴增 6 倍

> 2026-07-31 公测，284B/13B MoE，MIT 开源

## 核心数据

| 维度 | 参数 |
|:-----|:-----|
| 参数 | 284B total / **13B active** MoE |
| 上下文 | **100 万 Token** |
| 最大输出 | 384K Token |
| DeepSWE | 7.3 → **54.4**（Agent 代码能力 6x 提升） |
| Terminal Bench | **82.7**（逼近 Claude Opus 4.8） |
| 许可证 | **MIT**（开源权重） |
| 支持 | Tool Calls / JSON Output / FIM / Responses API |

## 定价（峰谷）

| 时段 | 输入(未命中) | 输入(命中) | 输出 |
|:-----|:-----|:-----|:-----|
| 平峰 (71%时间) | **1 元** | 0.02 元 | **2 元** |
| 高峰 (9-12/14-18) | 2 元 | 0.04 元 | 4 元 |

> 对比：Claude Opus 4.8 输出 $25/M token → V4-Flash 是它的 **1/90**

## 实测数据（来自社区）

- 393 次 API 调用，3422 万 token，总花费 **2.85 元**
- Claude Code 连续运行 4 小时，1 亿 token，缓存命中 99%，花费不到 **1 元**
- 一次完成代码编写 + 修复 10+ bug，成本约 **0.1 美元**

## 对你和 Hermes 的意义

- 🟢 **你现在用的就是 deepseek-v4-flash**（通过 opencode-go）
- 🟢 Agent 能力 6x 提升 → Hermes tool calling 质量直接受益
- 🟢 继续走 opencode-go 渠道即可，价格已经极低
- 🟡 opencode-go 可能还没更新到 V4-Flash-0731——留意 provider 版本
- 🟡 峰谷定价已生效：**避开 9-12 和 14-18 点用更便宜**

## 关键洞察

> "未来的大模型竞争，可能不再只比谁更聪明，还要比谁更快、更省、更能真正把事情做完。"

V4-Flash 把 Agent 能力（工具调用、多步骤任务、自主规划）从"高端专属"变成了"人人用得起"的基础设施。
