---
tags: [research, ai-model, meta, pricing]
created: 2026-08-08
type: research
---

# Meta Muse Spark 1.2 价格战研究 · 2026-08-08

> 来源：TerryTAO 数码硬件文章 + VentureBeat/Artificial Analysis/llm-stats/kingy.ai 交叉验证

## 结论置顶

**"比 DeepSeek 便宜 29%"是真的——但那是 Contributor 档（用你的数据换低价）！标准档 $1.25/$4.25 反而比 DeepSeek V4-Flash 贵 3-9 倍。叠加中国地区被封禁，sora 继续用 DeepSeek V4-Flash 是最优解。**

## 价格真相（VentureBeat 权威对比）

| 模型 | 输入 $/1M | 输出 $/1M | 合计 | 说明 |
|:---|:---|:---|:---|:---|
| **Muse Spark 1.2 Contributor** | $0.10 | $0.20 | **$0.30** | **数据换价**（prompt 被 Meta 训练用）|
| MiMo-V2.5 Flash（小米）| $0.10 | $0.30 | $0.40 | |
| **deepseek-v4-flash** | $0.14 | $0.28 | **$0.42** | sora 当前默认 |
| deepseek-v4-pro | $0.435 | $0.87 | $1.305 | |
| **Muse Spark 1.2 标准档** | **$1.25** | **$4.25** | $5.50 | 不用数据的真实价 |
| GPT-5.6 Luna | $0.20 | $1.20 | $1.40 | |

**"29%"的真相**：$0.30 vs $0.42 = 便宜 28.6% ✅ 但那是 Contributor 档。标准档 $5.50 vs DeepSeek $0.42 = **贵 13 倍**。

## 性能真相（交叉验证）

| 基准 | Muse Spark 1.2 | 对比 |
|:---|:---|:---|
| Terminal-Bench 2.1 | 82.9%（Muse Code）| Claude Opus 5: 86.7%（略逊）|
| MCP Atlas | 90.3%（宣传）| 自家基准，注水嫌疑 |
| DeepSWE | 59.3% | Opus 5: 65.0%（**换了自己的 agent 测**——不公平对比）|
| llm-stats 综合 | 1/6 胜 | DeepSeek V4-Pro-Max 5/6 胜 |
| 上下文 | 1M | 全模态（图/视频/音频/PDF）|

## 可用性（致命伤）

- 评论区实锤：**中国地区严格封禁**（"要美国家宽"），连 VPN 都被检测出真实所在地
- Meta 官方 2026-07 宣布"扩大全球访问"但中国仍不可用
- Contributor 档要求数据授权——**敏感内容不能传**

## 对 sora 的 apply

| 方向 | 判断 |
|:---|:---|
| **切换 Muse Spark？** | ❌ 否——地区封禁 + 标准档贵 13 倍 + Contributor 卖数据 |
| **继续 DeepSeek V4-Flash** | ✅ 正确（0.42 无地区限制无数据交换）|
| **关注 Muse Code 产品形态** | 🟡 多 agent 协同 + 持久上下文是趋势（Hermes 已有 delegation）|
| **关注小米 MiMo-V2.5 Flash** | 🟡 0.40/1M 比 DeepSeek 略便宜——但性能待验证 |

## 结论

价格战进入"白菜价时代"是趋势（MoE + 推理效率提升），但**白送的代价要么是数据要么是地区**。sora 的 DeepSeek V4-Flash 配置（0.14/0.28，免费镜像可用）在当前约束下依然最优。

_生成: k (Hermes) · 2026-08-08_
