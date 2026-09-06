---
tags: [AI, Agent-Skills, 科研, 技能库, 学术, GitHub-Trending, W37]
aliases: [scientific-agent-skills, K-Dense, 科研技能库]
date: 2026-09-06
source: https://github.com/K-Dense-AI/scientific-agent-skills
domain: AI
status: active
---

# Scientific Agent Skills — 科研 Agent 技能库（#1）

**43.0k★（本周 +5,491）** · "Turn any AI agent into an AI Scientist"——把任意 agent 变成 AI 科学家。165 个 ready-to-use **validated** skills + 100+ 科研数据库（生物/化学/医学/药物发现），号称 19 万+ 科学家使用。有 arXiv 论文（2609.00065）、v2.65.0、MIT。

## 核心特征

- **open Agent Skills 标准**：兼容 Cursor / Claude Code / Codex / Pi / Antigravity 及任意支持标准 agent。同名 SKILL.md 单文件格式，与 sora 的技能体系同构。
- **工程化基础设施**（大规模技能库治理样板）：
  - `plugin.json` + `pyproject.toml`（标准化打包）
  - `scan_skills.py` / `scan_pr_skills.py`（批量扫描 + PR 扫描）
  - CI：`skill-tests.yml`（技能测试门禁）+ `security-scan.yml`（安全扫描门禁）
  - **每个 skill 在 SKILL.md metadata 里有独立 license 字段**——仓库 MIT，但单技能各有条款，使用者自担审查责任
- **K-Dense BYOK**：免费开源桌面 AI co-scientist，自带 API key、40+ 模型可选、web search + 文件处理 + 100+ 数据库，数据留本地，可 Modal 上云扩算力。
- 705 commits · 4 branches · 103 tags，活跃维护。

## 技术架构（文字图）

```
skills/ 目录（165+ 个 SKILL.md，各自带 license/tests）
    │
    ├── scan_skills.py / scan_pr_skills.py   ← 批量扫描与 PR 门禁
    ├── skill-tests.yml  CI                  ← 技能测试
    ├── security-scan.yml CI                 ← 安全扫描
    └── plugin.json + pyproject.toml         ← 标准化分发
          │
          ▼
   任意 agent（Cursor/Claude Code/Codex/Pi/Antigravity）
```

## 💎 可借鉴点（⭐ 核心价值）

1. **大规模技能库治理 = sora 技能体系的工程模板**。sora 现有 130+ 技能，靠 skill-library-audit / skill-vetter 手工治理。该仓库把「扫描 + 测试 + 安全 + 单技能 license」做成 CI 门禁——可以直接照抄成 sora 的「技能入库门禁」（skill-tests + security-scan + scan_pr）。
2. **"validated skills" 概念**：不只是"可用"而是"验证过"——对应 sora 的 service-quality / 交付质量门，可升级为「每技能带验证证据」。
3. **单文件 SKILL.md 标准兼容**：sora 的 skill_manage 已用同格式，科研类技能可批量 import 复用（文献检索、数据可视化、论文写作等），与 light-* 科研主线互补。
4. **BYOK 桌面 co-scientist 形态**：本地 + 自带 key + 40 模型 + 数据不出本机——与 sora 的 EasyCLIProxyAPI / 本地推理偏好一致，是可参考的交付产品形态（也提示论文代做业务的「科研工作台」产品化方向）。

## 安装/验证

```bash
# 按 Agent Skills 标准安装（示例）
npx skills add K-Dense-AI/scientific-agent-skills
# 或只取需要的 skill 目录复制到 ~/AppData/Local/hermes/skills/
```

## 总结评价

| 维度 | 评分 | 说明 |
|:--|:--|:--|
| 技术含金量 | ★★★★ | 技能库治理工程化到位，科研技能深度待逐个验证 |
| 关联度 | ★★★★★ | 与 sora 技能体系同构 + 学术主线直接互补 |
| 可迁移性 | ★★★★★ | CI 门禁 / validated 概念 / SKILL.md 标准均可搬 |
| 热度 | ★★★★ | +5,491，科研 agent 赛道头部 |
| 值得安装 | 🟢 值得 | 至少抄治理模式；挑 3-5 个科研技能实测 |

> 🗺️ 属于 [[MOC-Inbox]] · [[MOC-GitHub]] · [[Home|🏠 Home]]
> 📅 周报见 [[../../memory/2026/09/github-trending-w37|W37 周报]]
