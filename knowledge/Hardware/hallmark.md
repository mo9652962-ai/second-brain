---
tags: [agent-skills, 设计工程, ui/UX, 反AI味]
aliases: [Hallmark, Anti-AI-Slop]
date: 2026-07-27
source: https://github.com/Nutlope/hallmark
status: adopted
---

# Hallmark — Anti-AI-Slop 设计 Skill

> 来源: [Nutlope/hallmark](https://github.com/Nutlope/hallmark)
> ⭐ 18.2K | 作者: Nutlope (Together AI)
> 学习时间: 2026-07-27 | 所属知识网络: [[knowledge-map]] | 相关: [[ibelick-ui-skills]] | [[mattpocock-skills]] | PPT-Design

## 简介

**Hallmark** 是一个给 Claude Code / Cursor / Codex 用的设计 skill，核心目标：**拒绝看起来像 AI 生成的 UI**。它有 20 个主题、4 个动词命令、57 道「AI 味」检测门，在输出前自我审查。

> **一句话**: 让 AI 编码工具写出来的 UI 不再千篇一律。

## 核心理念

> "Two pages by Hallmark for two different briefs feel like different sites, not colour-swaps of the same template."

AI 模型天然趋向于「分布内」输出——所有 Prompt 都倾向返回中庸、同质化的 UI。Hallmark 做的事情就是**故意偏离分布**：为每个需求选择不同的宏观结构、配色、排版指纹，确保输出独特性。

## 四动词命令系统

| 命令 | 功能 | 对应场景 |
|:---:|:------|---------|
| *(默认)* | 从零创建 UI。选宏观结构 → 套规则集 → 过 slop 测试 | 新建页面/组件 |
| `hallmark audit` | 对现有代码打分，列出违反的反模式清单（不改代码） | Code Review 设计 |
| `hallmark redesign` | 保留内容 + IA + 品牌，抛弃结构，换不同指纹重建 | 改版/焕新 |
| `hallmark study` ⭐ | 提取设计 DNA：宏观结构、字体配对、色彩锚点。**拒绝像素克隆**。可选输出 `design.md` | 学习最佳实践 |

## 57 道 Slop 检测门

Hallmark 输出前自动执行 57 道质量门，涵盖：

| 类别 | 检测点举例 |
|:---:|----------|
| **布局** | 是否标准 12 列网格？卡片间距是否均匀？有无"居中-大标题-三卡片"模板感？ |
| **色彩** | 是否用了 AI 默认蓝/紫渐变？饱和度是否超阈值？色相对比度？ |
| **排版** | 字体选择是否落入 AI 默认集？字号比例是否太数学？ |
| **内容** | 是否有 lorem ipsum？按钮文案是否 AI 套话（Learn More/Get Started）？ |
| **交互** | 悬停态是否自然？过渡动画是否机械？ |
| **代码** | CSS class 命名是否有 AI 特征（container-box-wrapper 类命名）？ |

## 20 个主题示例

| 主题名 | 气质 | 适用 |
|:-----:|:----:|:----:|
| Hum | 温暖手工感 | 食品/生活方式 |
| Cobalt | 冷静专业 | B2B SaaS |
| Carnival | 大胆活力 | 娱乐/音乐 |
| Lumen | 明亮极简 | AI 工具 |
| Riso | 印刷质感 | 文化/艺术 |
| Garden | 自然有机 | 农业/环保 |
| atmospheric | 氛围感 | 旅行 |
| modern-minimal | 现代极简 | SaaS |
| Custom | 完全定制 | 高创意需求 |

## 定制主题模式

当需求创意太强，没有 catalog 主题能匹配时，Hallmark 自动切换到 **Custom** 模式：

1. 分析需求中的创意意图
2. 从零设计调色板、字体、布局
3. 同样经过 57 道 slop 门
4. 没有模板在底下

## 💎 可借鉴点

### 1. 「偏离分布」设计哲学

AI 模型天然倾向输出统计平均，Hallmark 的态度是：**故意打破统计规律**。为我们降 AI 味工作流提供了技术验证——不是靠「加规则」，而是靠 **系统性地偏离默认路径**。

### 2. Pre-emit 自审查

不是输出后再让人评价，而是在生成阶段内嵌 57 道质量门。类似 TDD 的「红-绿-重构」，这里变成了「写-审-拒/改」。

> 对我们的启发：**输出前自检**可以内嵌到我们的 skill 设计里，特别是 PPT/论文场景。

### 3. study 命令的设计

`hallmark study` 不是让你直接抄（像素克隆被明确拒绝），而是提取设计系统的 DNA：宏观结构、字体配对、色彩锚点。这种 **DNA 提取 → 再应用** 的循环，比模板复用高级得多。

### 4. 四动词系统

四个命令覆盖了 **创建 → 审计 → 重构 → 学习** 的完整设计生命周期。每个动词做一件事且只做一件事。

### 5. 与我们的关联

我们已有 [[PPT-Design]] 和降 AI 味工作流，Hallmark 的方法论可以直接复用：

| 我们的场景 | Hallmark 对应 | 可借鉴 |
|:---------:|:------------:|:------:|
| 论文降 AI 味 | Slop 检测门 | 定义我们的 57 道学术 AI 味检测标准 |
| PPT 设计 | 主题选择 + Custom | 多个宏观结构避免同质化 |
| 前端开发 | audit + redesign | 建一个「AI 味 CSS 模式」检测清单 |

## 安装

```bash
npx skills add nutlope/hallmark
```

或手动复制到：
- **Claude Code**: `~/.claude/skills/hallmark/`
- **Cursor**: `.cursor/rules/hallmark.mdc`
- **Codex**: `~/.codex/skills/hallmark/`

## 总结

| 维度 | 评价 |
|:---:|:------|
| 对我当前工作流 | ⭐⭐⭐⭐⭐ — 降 AI 味是我们核心需求之一，方法论可直接迁移 |
| 技术含金量 | ⭐⭐⭐⭐ — 57 道检测门设计精巧，但本质是规则系统而非 AI 驱动 |
| 值得安装 | ✅ 已有 skill 版（memory 中已装） |
| 趋势判断 | AI 生成内容的「反同质化」将成为下一波工具的核心竞争力 |
