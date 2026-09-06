---
tags: [Dev, 图表, Agent-Skill, 架构图, 可视化, GitHub-Trending, W37]
aliases: [archify, 可验证架构图, 确定性图表编译]
date: 2026-09-06
source: https://github.com/tt-a1i/archify
domain: Dev
status: active
---

# Archify — 可验证的系统图 Agent Skill

**49.9k★（W37 周榜增长王 +19,480）** · 把代码库或系统描述变成「可在聊天里直接打开」的交互式系统图。Agent Skill 形态，Node.js 渲染 + 校验系统，兼容 Cursor / Claude Code / Codex CLI / OpenCode / DeepSeek Harness。

核心口号：**"Turn a codebase or system description into a polished, interactive system map — directly in chat."**

## 核心特征

- **typed JSON IR → 确定性编译**：Agent 产出类型化 JSON 中间表示，Archify 用确定性算法编译成 HTML/SVG——同一输入必得同一输出，可复现、可校验。
- **5 种图类型 × 4 预设 × 深/浅主题 × 品牌标识 × 有限动效**：架构 / 工作流 / 时序 / 数据流 / 生命周期，信号流 / 蓝图 / 经典等预设。
- **「不发明拓扑」原则**：所有交互（search / trace / compare / guided story）都基于 revision-verified 源，不幻觉连接关系——这是与普通 AI 画图（Mermaid-slop）的本质区别。
- **Before / Delta / After 快照评审**：把两个已校验快照对比，精确列出 added / removed / changed / moved / rerouted 事实——PR 合流前审架构变更。
- **单文件可信交付**：自包含 HTML + PNG / SVG / WebM 导出 + 1200×630 分享卡。
- **Proof Lab（11 个检查场景）**：每个场景带 JSON 源 + validation receipt（校验收据），证明图是「检查过的」而非「生成的」。
- **benchmarks/ordinary-model-floor**：普通模型质量地板基准，防止生成质量滑坡。
- MIT · 223 commits · 20 contributors · v2.16.0（08-30），仍高速迭代。

## 技术架构（文字图）

```
Agent (Cursor/Claude Code/Codex/OpenCode)
        │  产出 typed JSON IR
        ▼
┌─────────────────────────────────┐
│  constraint-driven compiler      │  ← 约束驱动编译 + proof receipt
│  确定性 HTML/SVG 渲染            │
└─────────────────────────────────┘
        │
        ├──► 自包含 HTML（单文件, 可打开可分享）
        ├──► PNG / SVG / WebM / 1200×630 分享卡
        └──► validation receipt（校验收据, 进 Proof Lab）
```

## 💎 可借鉴点（⭐ 核心价值）

1. **「确定性编译 + 校验收据」= 质量门禁的落地方案**。sora 的 service-quality / G5 门禁是「软判断」，Archify 把「校验」做成产物的一部分（validation receipt）——每次生成都附带可验证证据。可搬进 PPT/信息图/论文图的交付流程：产出即带证明。
2. **typed JSON IR 中间表示**。不是让模型直接输出图，而是输出结构化中间件再编译——把「生成」和「渲染」解耦，编译期做校验。sora 的 PPT 管线（outline.json 数据契约 → pptx 生成）已是同思路，可升级为「校验编译期」。
3. **Before / Delta / After 评审**。代码 review 前先 diff 架构图，精确到 added/removed/moved——适合 sora 的 code review / 墨题版本迭代做「可视化 diff」。
4. **Agent Skill 形态 + `npx skills add` 一键装**。验证了 Agent Skills 标准生态的成熟度——sora 自己的 130+ 技能体系与之一致，可考虑把 archify 作为外部技能安装，直接在 PPT/文档交付里调用。

## 安装/验证

```bash
npx skills add tt-a1i/archify -g   # 装到 agent
# 或在任意 agent 聊天里直接描述系统 → 产出可打开的系统图
```

## 总结评价

| 维度 | 评分 | 说明 |
|:--|:--|:--|
| 技术含金量 | ★★★★★ | 确定性编译 + 校验证据链，工程水准高 |
| 关联度 | ★★★★★ | PPT/图表/架构图交付业务 + Agent Skills 体系双契合 |
| 可迁移性 | ★★★★★ | 校验证据 / IR 编译 / Delta 评审三招可直接搬 |
| 热度 | ★★★★★ | 本周增长王 +19,480 |
| 值得安装 | 🟡 可试 | 先试装跑 1 个真实系统图验证；低风险（MIT，Node） |

> 🗺️ 属于 [[MOC-Dev]] · [[MOC-GitHub]] · [[HOME|🏠 Home]]
> 📅 周报见 [[../../memory/2026/09/github-trending-w37|W37 周报]]
