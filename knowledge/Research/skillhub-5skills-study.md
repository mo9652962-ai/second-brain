---
tags: [research, skillhub, skills, persona, ui]
created: 2026-07-31
status: absorbed
---

# SkillHub 本周 5 个 Skill 研究笔记

> 来源：小黑盒 SkillHub 精选 · 2026-07-31 验证 + 落地

## 📊 总览

| # | Skill | 热度 | 决策 | 理由 |
|:-:|-------|:---:|:---:|------|
| 1 | create-ex（前任蒸馏） | 71.5 | ❌ 不导入 | 隐私/伦理边界（微信记录+照片） |
| 2 | **nuwa-skill（女娲）** | 70.3 | ✅ **已导入** | **显式支持 Hermes** + 13 个人物视角现成 |
| 3 | systematic-debugging | 48.8 | ⚪ 已有 | 同名技能已存在 |
| 4 | mcp-builder | 46.5 | ⚪ 已有 | 规则 #2 MCP 铁律覆盖 |
| 5 | ui-ux-pro-max | 46.3 | 🟡 存档 | 与 claude-design/sketch 部分重叠 |

## 🔴 重点落地：nuwa-skill 女娲（4 技能导入）

### 发现
- **badge 显式列出 Hermes 运行时**：Claude Code · Codex · Cursor · OpenClaw · Hermes
- 原理：输入人名 → 6 路并行调研（著作/对话/社交/批评/决策/时间线）→ 三重验证提炼心智模型 → 生成可运行视角 Skill
- 自带 15 个现成人物视角（含完整调研数据）
- 关键原则："女娲不复制人，提取认知操作系统"

### 已导入 Hermes 的 4 个技能
| 技能 | 内容 | 文件数 |
|------|------|:---:|
| nuwa-skill | 女娲本体（造人引擎） | 8 |
| munger-perspective | 芒格（心智模型/决策启发式/25 偏误） | 6 |
| feynman-perspective | 费曼（第一性原理/学习方法） | 8 |
| steve-jobs-perspective | 乔布斯（产品决策/极简） | 9 |

### 芒格视角亮点（质量极高）
- 5 个核心心智模型：多元思维 / 逆向思考 / Lollapalooza / 能力圈 / 激励机制
- 8 条决策启发式（三筐分类法/激励诊断/达尔文协议等）
- 反例黑名单（7 种错误模仿模式）+ 诚实边界（6 条局限）
- 甚至承认芒格的盲区（科技/AI/加密、阿里巴巴失误）——比大多数角色扮演真实

### 踩坑记录（导入过程中的教训）
- ⚠️ 多行 YAML description（`|` 块）被简单正则替换会**吃掉整个正文**（文件从 475 行变 3 行）→ 必须从原仓库恢复 + 精确替换
- ✅ 修复：只在 frontmatter 前 30 行内处理，替换后验证行数 >50 才写入

## ⚪ 评估不导入

### create-ex（前任蒸馏，4K★）
- 功能：微信/QQ 聊天记录 → Relationship Memory + Persona 5 层 → 持续进化
- **不导入理由**：涉及极度隐私数据（聊天记录+照片+EXIF）；作者有伦理声明但风险仍高
- 技术参考价值：Persona 5 层结构（硬规则→身份→说话风格→情感→关系行为）与 nuwa-skill 同源

### ui-ux-pro-max
- 50 种设计风格 + 21 配色 + 20 字体 + shadcn/ui 组件
- 与我们的 claude-design / sketch / baoyu-infographic 部分重叠
- 🟡 待有 UI 设计需求时再评估

## 结论
- **1 个高价值落地**：nuwa-skill 女娲（显式支持 Hermes，4 技能导入）
- 2 个已有覆盖（systematic-debugging / mcp-builder）
- 1 个伦理不碰（create-ex）
- 1 个待定（ui-ux-pro-max）

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
