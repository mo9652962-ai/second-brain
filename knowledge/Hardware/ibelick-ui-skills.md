---
tags: [agent-skills, 设计工程, ui/UX, 学习笔记]
aliases: [UI Skills, Design Engineer Skills, ibelick]
date: 2026-07-27
source: https://github.com/ibelick/ui-skills
status: watch
---

# UI Skills — 设计工程师的 Agent Skills

> 来源: [ibelick/ui-skills](https://github.com/ibelick/ui-skills)
> ⭐ 6.3K | ⬆ 1,647 stars/week (本周 trending)
> 作者: ibelick (知名前端动画/设计工程师)
> 学习时间: 2026-07-27 | 所属知识网络: [[knowledge-map]] | 相关: [[hallmark]] | [[mattpocock-skills]] | [[PPT-Design]]

## 简介

**UI Skills** 是一个面向「设计工程师」（Design Engineer）的 Agent Skills 集合——帮助 AI 编码工具生成**更精致、更专业、更有设计感**的用户界面。运行 `npx ui-skills start` 即可将 Agent 路由到合适的 UI Skill 集。

> **一句话**: 把你的 AI 编码助手变成设计工程师。

## 安装与使用

```bash
npx ui-skills start                # 进入 UI skill 路由模式
npx ui-skills categories           # 查看所有分类
npx ui-skills list --category motion  # 列出某类 skill
npx ui-skills get baseline-ui      # 获取基础 UI skill
```

## Skill 分类

| 分类 | 用途 | 示例 Skill |
|:---:|:----|:----------|
| **Baseline UI** | 基础 UI 构建规范 | 组件结构、命名约定、无障碍 |
| **Motion / 动画** | 动效设计模式 | 入场/出场动画、过渡曲线、手势反馈 |
| **Color / 色彩** | 配色系统 | 调色板生成、对比度、暗色模式 |
| **Typography / 排版** | 字体与排印 | 字体配对、字号层级、行高规则 |
| **Layout / 布局** | 页面结构 | 响应式网格、间距系统、断点 |
| **Accessibility** | 无障碍 | ARIA 标注、键盘导航、屏幕阅读器 |
| **Design Tokens** | 设计令牌 | CSS 变量、主题系统、属性命名 |

## 核心理念

### 1. Skill 路由模式

`npx ui-skills start` 不是加载单个 skill，而是根据任务自动路由到最合适的 UI skill 子集。类似 [[mattpocock-skills]] 的 `ask-matt` 路由器。

### 2. Design Engineer 定位

「设计工程师」是 2024-2026 年兴起的新角色——既有设计师的审美能力，又会写代码。UI Skills 瞄准的就是这个群体（或者说 Agent 替代这个群体时所需的能力）。

### 3. 渐进式专业度

```
Baseline UI（基础规范）
    ↓
色彩/排版/布局（单项专精）
    ↓
Motion/动画（高阶交互）
    ↓
Design Tokens（系统化设计）
```

每层 skill 独立加载，不扰民。

## 💎 可借鉴点

### 1. 分类驱动的 Skill 架构

UI Skills 按设计维度（色彩/排版/动效/布局）拆分为独立 skill，而非一个大而全的「前端开发 skill」。这种 **垂直领域切分** 比我们的工程类 skill 更细粒度，也更容易维护。

### 2. CLI 入口 + 自动路由

`npx ui-skills start` 作为单一入口，背后自动选择正确的 skill 集。用户不需要知道具体用哪个——Agent 代劳判断。类似的思路可以用在：`hermes run design` 统一路由到 PPT / UI / Design 等。

### 3. 与 Hallmark 的互补关系

| 维度 | Hallmark | UI Skills |
|:---:|:--------:|:---------:|
| 侧重点 | **反 AI 味**（别丑） | **正设计能力**（做好看） |
| 哲学 | 57 道门「排除坏答案」 | 300+ 条规则「引导好答案」 |
| 输出保障 | 拒绝 + 回退 | 正向指导 |
| 维护方式 | 单一 SKILL.md | 多分类独立 Skill |

> **组合使用效果最佳**: Hallmark 负责「不谈 AI」，UI Skills 负责「谈好设计」。

### 4. 设计系统的 Agent 化

Design Tokens skill 将设计系统（颜色/间距/字体 Token）编码为 Agent 可读的格式——Agent 不再需要翻 Figma 文件，直接从 Token 生成一致 UI。这和我之前学习的 [[vibe-research]] 中的 design-to-code 思路一致。

## 总结

| 维度 | 评价 |
|:---:|:------|
| 对我当前工作流 | ⭐⭐⭐⭐ — 我们做 PPT/前端项目时会很有用，特别是动效和色彩系统 |
| 技术含金量 | ⭐⭐⭐⭐ — 分类设计优雅，CLI 工具链完整 |
| 值得安装 | ✅ `npx ui-skills start` 即可，零成本 |
| 特别启发 | **垂直分类 skill** 的组织方式值得在 Hermes skill 体系中试验 |
