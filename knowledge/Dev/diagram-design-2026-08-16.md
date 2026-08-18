---
tags: [diagram, HTML-SVG, skill, Claude-Code, 设计, 方法论, W34]
aliases: [diagram-design, cathrynlavery-diagram]
date: 2026-08-16
source: https://github.com/cathrynlavery/diagram-design
status: watch
---

# diagram-design — 29 种编辑级图表模板（Claude Code Skill）

> **简介**：Cathryn Lavery（BestSelf.co 创始人）出品，29 种编辑级图表类型的 Claude Code skill。**本周增长王：18,864⭐ +14,735/周**（HTML/SVG，MIT，100 commits，活跃）。自包含 HTML + SVG，**无阴影、无 Mermaid-slop**——专治 AI 生成图表千篇一律的「Mermaid 味」。

## 核心思路

1. **29 种编辑级图表类型**：Radar/Spider、Loop、IT current-state、High-Level 架构、Bar/Line/Gantt/Scatter、Process、Medallion、Data flow、DP integration、DP security matrix 等——每种都是设计过的模板，直接产出可截图的成品图。
2. **自包含 HTML + SVG**：不依赖 Mermaid/外部渲染器，单个 HTML 内联 SVG，可嵌入任意文档/网页/PPT。
3. **品牌自动提取（onboarding）**：`onboard diagram-design to https://yoursite.com` → 抓首页 → 提取主色板 + 字体栈 → 映射到语义 token（paper/ink/muted/accent/link）→ 写入 style-guide.md → 之后所有图都用你的品牌色。
4. **WCAG AA 对比度自动校验**：写 token 前先验证 ink over paper 在 9-12px 下的对比度，不合格自动提出调整值——无障碍默认开启。
5. **多客户端插件分发**：Claude Code / Codex / Pi / Claude Cowork 四种安装路径，`.claude-plugin/` + `.codex-plugin/` + `.agents/plugins/marketplace.json` 三套 manifest 同步维护（CI 版本门禁 `bump-plugin-version.py` 强制 Claude 和 Codex 版本同步递增）。

## 精妙工程细节（值得抄）

- **Sketchy filter**：SVG turbulence + displacement map 生成手绘风变体——用滤镜而非重画实现风格切换。
- **图标集**：55 个单色 IT/云图标（Tabler Icons MIT + Simple Icons CC0），全部用 `currentColor` 继承品牌色。
- **「何时不用」门禁**：README 明说——纯列表用表格、前后对比用表格、单框图直接写句子；画图前先问「读者从图中学到的比一个好段落更多吗？」。**不为了画图而画图**。
- **可编辑安装**：托管安装会被更新覆盖 style-guide.md，`~/.diagram-design/profiles/` 保存用户 profile 可幸存——配置与代码分离。

## 💎 可借鉴点（对 sora 工作流最值）

1. **「无 Mermaid-slop」理念 → 直接应用到 PPT/图表生成**：sora 的 academic-presentation / ppt-design / baoyu-infographic 技能生成的图，若自动检测到「Mermaid 默认蓝紫配色 + 圆角矩形 + 标准箭头」就重做——图表同质化是 AI 代做被认出的重灾区，diagram-design 的「设计过的模板」思路可沉淀成图表样式库。
2. **品牌 token 化设计系统**：不写死颜色，用语义角色（paper/ink/muted/accent/link）映射品牌。sora 的水墨风 UI / PPT 模板可借鉴——一套 token 换肤，PPT 代做可快速出「客户品牌色」版本。
3. **WCAG 对比度门禁**：生成图表/PPT 时自动检查文字 vs 背景对比度——现在很多 AI 生成 PPT 的浅灰字根本看不清，这是可落地的质量门。
4. **多客户端 manifest 同步 = agent-skills-addyosmani 的落地案例**：上篇笔记（[[agent-skills-addyosmani-2026-08-14]]）讲的多 agent 单源 + CI 校验，diagram-design 用 `bump-plugin-version.py` 落地了版本同步门禁——sora 若做跨 Hermes/Codex 技能，可抄这个脚本。

## 综合评估

| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★☆（图表 skill 工程化标杆：模板/品牌/无障碍/多端分发全做了）|
| 与 sora 工作流关联 | ★★★★★（PPT/图表代做、信息图、UI 品牌化直接对口）|
| 值得安装 | 🟢 参考——不整体装 Claude Code 插件，但「图表样式库 + 品牌 token + 对比度门禁」三个方法论应落地到 ppt-design / baoyu-infographic |
| 趋势判断 | AI 生成图表的「去模板化」成为新战场，编辑级设计成为卖点 |

> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]] · 平行参考：[[agent-skills-addyosmani-2026-08-14]]（多 agent skill 工程化）· `ppt-design-2026` · `baoyu-infographic`
