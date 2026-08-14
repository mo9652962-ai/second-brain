---
tags: [Agent-Skills, engineering, skill-format, Claude-Codex-Gemini, 方法论]
aliases: [addyosmani-agent-skills, agent-skills]
date: 2026-08-14
source: https://github.com/addyosmani/agent-skills
status: watch
---

# agent-skills (Addy Osmani) — 生产级工程技能

> **简介**：Google Chrome 团队 Addy Osmani 出品，production-grade engineering skills for AI coding agents。本周 87,148⭐ **+4,562/周**（JavaScript，MIT，421 commits，活跃）。服务多 agent：Claude/Codex/Gemini/OpenCode/Cursor/Copilot/Antigravity。**87k star 需甄别**——但 addyosmani 是真实知名开发者，且仓库有完整的 skill 格式规范 + CI 校验 + 多 agent plugin manifest，真实度高（对比 RuView 那种刷星项目）。

## 核心方法论：好 Skill 的四原则
> Skills 应 **specific**（可执行步骤，非模糊建议）、**verifiable**（明确的退出标准 + 证据要求）、**battle-tested**（基于真实工作流）、**minimal**（只留引导 agent 所需）。

## 多 Agent 单源结构
```
agent-skills/
├── skills/*/SKILL.md       # 统一格式
├── .claude-plugin/  .codex-plugin/   # 各 agent 的 plugin manifest
├── .claude/  .gemini/  .opencode/  .cursor/  # 各 agent 加载配置
├── agents/                 # persona 定义(YAML frontmatter)
├── commands/               # 命令
├── docs/skill-anatomy.md   # 格式规范(单源真相)
└── CI: validate-reference-links.js  # references/ 链接门禁
```

## 精妙工程细节（值得抄）
- **CI 校验 references/ 链接**：`validate-reference-links.js` 逐个解析每个 skill 目录里的 `references/*.md` 链接，裂了就 CI 失败——防止「skill 移动/改名后引用断裂」的静默腐化（这正是 sora 每个 skill 都可能踩的坑）。
- **文档为单源真相**：CLAUDE.md / CONTRIBUTING.md 指引模型走 CONTRIBUTING 预检，不重复复制，避免多份文档不同步。
- **`contents` 规范路径分域**：GitHub Copilot CLI 会扫描 `agents/*.md` 当自定义 agent 定义，需 YAML frontmatter——仓库把帮助文档移到 `docs/`，只留真 agent 定义。
- **诚实对比**：官方提供 vs Superpowers(obra) / Matt Pocock's skills 的对照文档 + 受控 head-to-head 实验。

## 💎 可借鉴点（对 Hermes 技能库最值）
1. **references/ 链接门禁**：sora 100+ skills，迁移/改名极易断引。可给 skills 加一个「校验 references/ scripts/ 内链接」的校验脚本（Hermes skill_manage 已有 write_file 到 references/，缺链接完整性检查）。
2. **四原则当 skill 质量门**：specific / verifiable / battle-tested / minimal——正是 service-quality、skill-vetter、code-quality-bootstrapping 等评估技能的统一标准，可沉淀成 skill 自检清单。
3. **多 agent 单源**：一份 skill 逻辑，多个 agent 各自 manifest——sora 同时用 Hermes/Codex，可用同一套 skill 目录 + 各自加载配置，避免重复维护。
4. **agents/ 与 docs/ 分离**：避免被工具误判为 agent 定义——sora 的 agents 目录若被某 CLI 扫描会出现同类告警，可借鉴命名/存放约定。

## 综合评估
| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★☆（skill 工程化做到位：规范/CI/多端）|
| 与 sora 工作流关联 | ★★★★★（Hermes skills 体系直接对标）|
| 值得安装 | 🟢 参考——不整体安装，但「references 链接门禁 + 四原则」应并入 Hermes skill 管理 |
| 趋势判断 | Agent Skills 成为 2026 标准装配，向「可校验、可版本化」演进 |

> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]] · 平行参考：[[agent-skills-methodology-absorbed]](kepano/obsidian-skills) · [[mattpocock-skills]]