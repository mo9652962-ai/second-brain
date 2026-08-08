---
tags: [research, api-relay, zcode, glm, luna, vision, cost-optimization]
created: 2026-08-08
type: research
---

# zcode/luna 深入研究 · 2026-08-08（真身确认 + Luna 视觉路径）

> 来源：小黑盒帖子（zcode 3亿token 2元 + luna 辅助）+ ZCode 官网 + helpaio 中转站评测。learn→research→apply。

## 核心结论

**zcode 真身 = 智谱 Z.ai 官方 AI 编程编辑器（GLM-5.2 官方适配），不是中转站**——"3 亿 token 2 元 + 99% 缓存"是 ZCode 编辑器的 GLM 模型额度。**Luna = GPT-5.6 Luna（OpenAI），Micu 中转站 0.35x 倍率超便宜（¥0.07/M 输入）且支持视觉——sora 视觉断点的新解路径！**

## 事实（官方/评测页验证）

### ZCode（智谱官方编辑器）
- 官网 zcode.z.ai：GLM-5.2 官方适配开发工具，Windows/macOS/Linux 全平台（v3.6.5）
- 定位：Cursor 竞品，多 Agent 协作，GLM-5.2 深度优化
- 帖子里"3 亿 token 2 元"= ZCode 的 GLM 模型调用（缓存命中 99% 所以便宜）
- **与 sora 相关性低**：sora 用 Hermes/刷题机，不是 Cursor 类编辑器（ZCode 是独立桌面编辑器）

### GPT-5.6 Luna（视觉救星）
- OpenAI 新模型：降价 80%、比 DeepSeek 便宜一半、**支持视觉理解 + 工具调用**
- 评论区"转 luna 了，中转站也太便宜"= 中转站卖 Luna 便宜
- **helpaio 评测实测价**：
  - Micu（#1，86.96 分）：`gpt-5.6-luna` 0.35x → **¥0.07/M 输入 / ¥0.42/M 输出**
  - Duck Code（#20）：0.80x → ¥0.16/M 输入
- Micu 详情：25年12月开业（OCC 秽土转生）、3 天退十几万无槽点、客服高强度在线、**退款无手续费**、无并发限制、缓存一线 85-95%

### 中转站评测体系（helpaio，可复用）
- 站点分 = 运营 65% + 价格 35%，乘 3 日可用率
- 风险铁律：**小额试用、勿囤积、勿贪大额优惠**
- 近 24h 健康度：Claude 89.5% / GPT 96.6%

## Apply 评估

| 项 | 决策 |
|:---|:---|
| ZCode 编辑器 | 🟢 了解即可（sora 工作流不依赖 Cursor 类编辑器）|
| **Luna 视觉路径（首选新解）** | 🟡 **Micu 小额充（¥10-50）→ gpt-5.6-luna 视觉**——解决上轮 4 候选全断点的视觉缺口 |
| 中转站选型 | ✅ 若充：Micu（#1 评分最高 + 退款无手续费）|

## 行动项

| 优先级 | 项 | 说明 |
|:---|:---|:---|
| 🟡 P1 | **Micu 小额试充 Luna** | ¥10-50 起充 → 配置 auxiliary.vision = gpt-5.6-luna → 视觉恢复 |
| 🟡 P1 | 百炼开通 qwen-image-3.0-pro | 待用户控制台点"开通"后重测 |
| 🟢 P2 | ZCode 体验评估 | 可装 Windows exe 试 GLM-5.2 编辑器（非必需）|

_生成: k (Hermes) · 2026-08-08 · learn→research→apply_
