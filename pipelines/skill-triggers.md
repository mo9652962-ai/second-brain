# Skill 触发词映射表 v1.0

> 用户说什么 → 激活哪些 Skills → Pipeline 路径
> 基于渐进式加载 + 触发精确匹配

## PPT 族触发

| 用户说 | 激活 Skills | Pipeline |
|--------|------------|----------|
| 「做PPT」「生成幻灯片」 | cn-ppt-outline-writer → pptx-generator → ppt-optimizer | ppt-pipeline |
| 「学术汇报PPT」 | + academic-presentation | ppt-pipeline |
| 「优化PPT」「检查PPT」 | ppt-optimizer | 单步 |
| 「网页演示」「HTML幻灯片」 | openclaw-slides | 单步 |
| 「PPT模板」「占位符PPT」 | powerpoint-pptx | 单步 |

## 论文族触发

| 用户说 | 激活 Skills | Pipeline |
|--------|------------|----------|
| 「搜论文」「查文献」 | cnki-scholar + cnki-advanced-search (Fan-Out) | paper-pipeline |
| 「读论文」「分析这篇」 | paper-parse | 单步 |
| 「论文摘要」 | paper-summarize-academic | 单步 |
| 「写论文」 | paper-writing-workflow | paper-pipeline |
| 「润色论文」「SCI精修」 | sci-paper-three-pass | paper-pipeline |
| 「去AI味」「降重」 | chinese-academic-writing | 单步 |
| 「期刊检索 SCI」 | journal-sci-ssci-checker | 单步 |

## 图片族触发

| 用户说 | 激活 Skills | Pipeline |
|--------|------------|----------|
| 「生成图片」「AI绘图」 | ai-image-generation | 单步 |
| 「国内生成图片」 | nano-banana-pro-image-gen | 单步 |
| 「图片优化」「写提示词」 | image-prompt-generator | 单步 |
| 「找最佳图源」 | best-image-generation | 单步 |

## 自改进族触发

| 用户说 | 激活 Skills | Pipeline |
|--------|------------|----------|
| 「我错了」「不对」 | self-improving-agent | 单步 |
| 「提醒我」「定时」 | proactive-agent | 单步 |
| 「审计 skill」 | skill-vetter | 单步 |

## CAD 族触发

| 用户说 | 激活 Skills | Pipeline |
|--------|------------|----------|
| 「3D建模」「CAD设计」 | cad-design-master | 单步 |
| 「51单片机」「嵌入式」 | 8051-embedded-dev | 单步 |

## 跨族触发 (多 Pipeline)

| 用户说 | 激活 Skills | Pipeline |
|--------|------------|----------|
| 「论文+PPT」 | paper-pipeline + ppt-pipeline | 先后执行 |
| 「检索→写作→PPT」 | 论文族全流程 + PPT族 | 串行 |
| 「做一个3D模型并出PPT」 | cad-design-master + ppt-pipeline | 串行 |

## 精准匹配规则

1. **最长匹配优先**: 「学术汇报PPT」→ 匹配 academic-presentation，而非仅 ppt
2. **组合匹配**: 「写论文并做PPT」→ 同时匹配 paper + ppt
3. **语义等价**: 「做个片子」=「做PPT」; 「扒文献」=「搜论文」
4. **负向排除**: 「不要生成图片」→ 不激活图片族
