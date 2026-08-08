---
tags: [absorbed, superpowers, grounded-copy, quality]
source: obra/superpowers (260k⭐) + 用户自定义技能
date: 2026-07-27
---

# Superpowers + Grounded-Copy · 吸收与评估

> 截图来自：Superpowers（obra, 260k⭐）的 Opus 5 适配工作流

---

## 发现的三个核心方法

### ① grounded-copy：变模糊为具体

核心原则：**不要说"好"，要说"好在哪"**

| 模糊的原文 | 改写后 |
|:-----------|:--------|
| "这不是一个任务追踪器——是你团队的第二大脑" | "追踪器把每个任务链接到它的 PR，每天早上在 Slack 发状态摘要" |
| "告别隐藏费用" | "标价即全价，发票不附加任何额外费用" |
| "专家一致认为 Acme 领先市场" | "Acme 占据 34% 市场份额，Gartner 2025市场报告" |

**对我们**：闲鱼文案、论文广告语、服务描述 — 全部可以应用此方法

### ② copy_lint：给文案上 lint

- 检查"模糊对比"（"不是慢"→ 不如直接说时间）
- 检查空洞的形容词
- 基于规则而非感觉

**对我们**：我们可以创建一个"闲鱼文案检查清单"做同样的事

### ③ Skill Overrides：模型适配

截图中的配置：
```json
"verification-before-completion": "off",   // Opus 5 自己会验证
"requesting-code-review": "off",           // 同理
"dispatching-parallel-agents": "off",     // Opus 5 已擅长并行
```

**核心思想**：不同的模型能力不同——**强模型不需要弱模型的辅助技能**
**对我们**：opencode-go/deepseek-v4-flash 足够强，可以去掉一些不必要的约束性 skill

## 评估：是否安装 Superpowers？

**结论：不装。** Superpowers 是为 Claude Code/Codex 设计的框架，我们的 Hermes 技能系统已经覆盖了类似功能（planning, TDD, debugging skills）。

但 **grounded-copy 方法** 可以直接应用：
- 闲鱼服务文案改写
- 论文摘要的"接地气"改写
- PPT 文案的精准化

---
> 🗺️ 属于 [[MOC-AI]] · [[Home|🏠 Home]]
