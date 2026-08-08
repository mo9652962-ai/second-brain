---
tags: [research, ai-model, xiaomi, pricing]
created: 2026-08-08
type: research
---

# 小米 MiMo-V2.5 研究 · 2026-08-08

> 来源：小米开放平台官方（mimo.mi.com）+ Artificial Analysis + llm-stats + BenchLM + Reddit 实测

## 结论置顶

**MiMo-V2.5 与 DeepSeek V4-Flash 完全同价（$0.14/$0.28），不是更便宜——VentureBeat 表格里的 $0.10/$0.30 是旧 Flash 版。性能上 DeepSeek 综合更强（智能指数 52 vs 38、速度快 14%、TTFT 快一半）。结论：维持 DeepSeek V4-Flash，不切换。**

## 价格真相（小米官方 2026-08-06 更新）

| 模型 | 国内输入 | 国内输出 | 海外输入 | 海外输出 |
|:---|:---|:---|:---|:---|
| **mimo-v2.5** | ¥1.00 | ¥2.00 | **$0.14** | **$0.28** |
| mimo-v2.5-pro | ¥3.00 | ¥6.00 | $0.435 | $0.87 |
| deepseek-v4-flash | — | — | $0.14 | $0.28 |
| 缓存命中 | ¥0.02/1M（近免费）| | $0.0028/1M | |

**关键**：mimo-v2.5 海外价 = **deepseek-v4-flash 完全同价**（不是更便宜！）。VentureBeat 表格的 $0.10/$0.30 对应旧 mimo-v2-flash（2025-12 版，已下线——MiMo-V2 系列 2026-06-30 全部下线）。

## 性能对比（DeepSeek V4 Flash 0731 vs MiMo-V2.5）

| 维度 | DeepSeek V4 Flash | MiMo-V2.5 | 胜者 |
|:---|:---|:---|:---|
| AA 智能指数 | **52** | 38 | DeepSeek |
| 速度 | **105.9 tok/s** | 93.1 tok/s | DeepSeek |
| TTFT | **1.30s** | 2.99s | DeepSeek |
| 混合价(7:2:1) | $0.06 | $0.06 | 平 |
| 上下文 | 1M | 1M | 平 |
| Agentic (BenchLM) | 49.1 | **65.8** | MiMo |
| Coding (BenchLM) | **64.2** | 56.1 | DeepSeek |
| Reddit 实测 | **5-0 胜** | | DeepSeek |

## 可用性

- ✅ **中国直接可用**（小米开放平台，人民币计价）
- ✅ OpenAI 兼容 API
- ✅ TTS 限时免费（可当语音方案）
- ⚠️ MiMo-V2 旧系列 2026-06-30 已下线（模型名失效）

## 对 sora 的 apply

| 方向 | 判断 |
|:---|:---|
| **替换 DeepSeek V4-Flash？** | ❌ 否——同价但性能弱（智能指数 38 vs 52）|
| **作为备用/容灾第 2 源** | 🟡 可考虑（国内直连 + 同价 + 缓存便宜）|
| **TTS 免费** | 🟢 留意（mimo-v2.5-tts 限时免费——可做语音方案备用）|
| **ASR** | 🟢 ¥0.5/小时（极便宜）|

## 结论

MiMo-V2.5 是国内可用的 DeepSeek 平价替代，但**性能弱于 DeepSeek V4-Flash**。sora 的当前配置（DeepSeek V4-Flash 主 + 火山/硅流容灾）无需变更。唯一值得留意的：**MiMo TTS/ASR 免费期**——做语音功能时可白嫖。

_生成: k (Hermes) · 2026-08-08_

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
