---
tags: [游戏开发, Godot, AI编程, 研究笔记, 2026-08]
domain: AI
---

# 开源游戏引擎 + AI 辅助开发研究（2026-08-17）

> 来源：小红书周榜「做游戏听起来很高门槛？2026 开源生态已砍到很低」
> 方法：GitHub API 实证 + AI 游戏开发生态调研
> 相关: [[agent-infra-weekly-2026-08-17]] | [[engineering-workflow]]

## 5 引擎实证数据（GitHub API 实时）

| 引擎 | ⭐ 实际 | 语言 | License | 定位 | AI 辅助 |
|:---|:---|:---|:---|:---|:---|
| Godot | 115,729 | C++/GDScript | MIT 无分成 | 2D/3D 全能 | ⭐ 最成熟 |
| Bevy | 47,649 | Rust/ECS | Apache-2.0 | 高性能严肃项目 | 中等 |
| GDevelop | 25,686 | 无代码事件表 | — | 零代码原型 | 低 |
| melonJS | 6,359 | JS/TS | MIT | H5 小游戏 150KB | 高 |
| boardgame.io | 12,399 | TS | MIT | 回合制桌游 | 高 |

## 核心研究结论：AI + Godot 已经走通

### 实证案例（最强证据）
**OpenCode + 推理路由做完整点球游戏**（DigitalOcean 2026-07）：
- 功能：瞄准/力度条/门将AI/骤死赛/结算/重启/README
- 83 agent turns / 596 路由任务 / 410万 token
- **成本 $8.25**（路由到 MiMo/GLM 为主，2 次回退）
- 对比：全前沿模型 $123，GLM 全用 $18 —— **路由省 15 倍**

### AI 写 GDScript 三大陷阱
1. **版本漂移**：Godot 4 时代模型爱写 Godot 3 API（yield→await、KinematicBody2D→CharacterBody2D）→ headless 编译兜底
2. **节点路径猜测**：AI 写 `$Player/Sprite` 全靠猜 → godot-mcp 读真实场景树
3. **运行时盲区**：空节点/信号漏接/缺碰撞体只有运行才崩 → headless 跑场景

### 工具链（2026 成熟）
- **godot-mcp**（Coding-Solo）：AI 读场景树/节点/ClassDB + 运行/停止/截图
- **godot-ai-builder**（hubdev-ai）：14 技能 + 28 MCP 工具 + 6 阶段构建 + 质量门禁
- **headless 验证**：`godot --headless --editor --quit-after 1` 编译检查

### 模型选型
Claude Opus（质量最高，GDScript 漂移最少）> GPT > **DeepSeek/GLM/MiMo（性价比主选）**

## 对我们的落地

1. 新建技能 `godot-ai-game-dev`（工具链 + 6 阶段流程 + headless 验证 + 成本数据）
2. Hermes 路径：写 .gd/.tscn → headless 编译验证 → 修正（零额外安装）
3. dsh 路径：复杂游戏委派，AGENTS.md 写 Godot 版本/结构，关键接 godot-mcp
4. 成本控制：复用现有路由（delegation.model=flash / dsh 官方 DS）
5. 素材策略：procedural（shader/粒子）优先，避免美术依赖

## 后续可做
- sora 想试时：装 Godot 4.7 + godot-mcp → 用 godot-ai-game-dev 技能从 PRD 到可玩
- 可接闲鱼 H5 小游戏单（melonJS 轻量）或 Godot 独立游戏单
