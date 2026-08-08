---
tags: [research, image-gen, qwen-image, seedream, evaluation]
created: 2026-08-08
type: research
---

# Qwen-Image-3.0-Pro 实测研究 · 2026-08-08

> 来源：阿梨Aria 实测对比（8.6）+ 官方榜/Seedream 实测交叉验证。learn→research→apply。

## 核心结论

**Qwen-Image-3.0-Pro 单张可用、批量不可用**（限流 RPM=1 + 生成 3-8 分钟 + 参考图 3 张 = 电商批量判死刑）。开源前不建议作为批量生图主力；玩一玩/单张需求值得试。**批量场景首选 Seedream 5.0 Pro**（0.3 元/张 + 编辑工作流）。

## 事实（验证后）

### Qwen-Image-3.0-Pro
| 维度 | 结论 | 证据 |
|:---|:---|:---|
| 画面质量 | 完成度高，复杂场景/文字/版面可做实际任务 | 实测对比（vs GPT Image 2）|
| 文字能力 | 4.5k token 提示词、10px 小字、12 语言、20+ 字体 | 官方 + 实测 |
| 价格 | 1K 图 0.25 元 / 2K 0.5 元（比 Seedream 5.0 Pro 低 ~0.05-0.1 元）| 百炼 + bimant 交叉 |
| 统一模型 | T2I + I2I 共用 qwen-image-3.0-pro 单 ID | 官方 |
| 参考图 | **最多 3 张**（多角度需求不够）| 实测 |
| 限流 | **RPM=1（华北二邀测），单张 3-8 分钟** | 实测 |
| 输出 | 最高 2048²、PNG 固定、结果链接 24h 有效 | 实测 |
| 短板 | 无遮罩编辑、无 Function Calling/批量/上下文缓存、单轮 | 官方模型页 |

### 交叉验证
- **Qwen-Image-Bench 官方榜**：Top4 = GPT Image 2 / Nano Banana 2.0 / GPT Image 1.5 / Nano Banana Pro；Qwen Image 2.0 Pro 排第 5——**注意**：帖子称"3.0 排在 Banana 2 前面"，官方榜是 2.0 Pro 数据，3.0 可能已更新
- **Seedream 5.0 Pro**（腾讯云 17 案例实测）：国产当前最强形态，中文文字不乱码，0.3 元/张，"价格+编辑工作流组合拳"是杀手锏；复杂中文信息图错误率仍偏高
- 评论反馈：人物形体/皮肤质感仍粗糙（食山君）；3.0 频繁"服务器有问题"（Kizunaai）——算力不足实锤

## 关键配置（已记）

- 生图 URL 用 `https://dashscope.aliyuncs.com/api/v1`（**不要用百炼业务空间专属域名——不支持跨域，生图报错**）
- 支持 negative_prompt / 固定 seed / prompt_extend / 水印开关 / 一次最多 6 张变体 / 512²-2048²

## Apply 评估（更新昨天 P1 行动项）

| 场景 | 决策 | 理由 |
|:---|:---|:---|
| 刷题机背景图/单张需求 | 🟡 可试玩 | 低频单张，RPM=1 无影响；文字渲染强（可做试卷/海报）|
| 闲鱼电商批量出图 | ❌ 不选 | RPM=1 + 3-8 分钟 + 3 张参考图 → 批量不可用 |
| 闲鱼批量素材 | ✅ **选 Seedream 5.0 Pro** | 0.3 元/张 + 编辑能力 + 稳定 |

## 行动项更新

- P1 调整为：**百炼试玩 Qwen-Image-3.0-Pro 单张**（验证文字渲染 + 0.25 元成本）→ 若好用于单张需求
- P1 新增：**Seedream 5.0 Pro 接入评估**（批量场景主力候选）
- 关键配置已记：dashscope.aliyuncs.com/api/v1

_生成: k (Hermes) · 2026-08-08 · learn→research→apply_

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
