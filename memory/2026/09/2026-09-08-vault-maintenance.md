---
tags: [maintenance, vault, lint]
type: maintenance
created: 2026-09-08
updated: 2026-09-08
---

# 2026-09-08 知识库体检与维护

> 例行维护：断链修复 + 空文件清理 + 标签一致性 + 孤立挂载。完整体检脚本：`knowledge/META/scripts/knowledge-lint.py` + `full-vault-diagnostic.py`。

## 📊 体检结果（修复后复跑）

| 检查项 | 修复前 | 修复后 | 说明 |
|:---|:---:|:---:|:---|
| Broken wikilinks（knowledge/） | 0 | 0 | 全仓库严格扫描发现 16 处 → 已修复 |
| Missing frontmatter | 2 | 0 | 今日 2 个新笔记补 frontmatter |
| Orphan pages（knowledge/） | 5 | 1 | 剩 1 为 eval-v2 README 已知 lint 盲区（MOC-Research 有全路径入链，Obsidian 实际有效） |
| Empty/near-empty notes | 3 | 0 | 删除今日 dreaming 空壳 3 个 |
| Tag case inconsistency | 1 组 | 0 | `github trending`/`GitHub Trending` → `github-trending` |
| Stale pages (>90d) | 0 | 0 | — |

## 🔧 本次动作

### 1. 断链修复（16 处，全仓库）
- **dreaming 快照剥括号 ×6**：`memory/dreaming/light-2026-08-06/07.md` 的 `[[health-2026-07-24]]`/`[[weekly-2026-07-26]]`/`[[hermes-session-20260723]]`（目标已归档不存在）→ 纯文本
- **维护笔记文档示例剥括号 ×8**：`log.md`（`[[../knowledge/...]]` 等 3 处）、`2026-08-13-vault-maintenance.md`（`[[knowledge/AI-Workflow]]`、`[[knowledge/arxiv-2026-07-31-core-contributions]]`、`[[projects]]` 3 处）、`2026-09-04-maintenance.md`（`[[MOC-Development]]`、截断 `[[memory/2026/08/sug...` 2 处）——均为文档化示例，按技能规范剥离 `[[` `]]`
- **`[[MEMORY.md]]` → `[[MEMORY]]` ×5**（含 1 处带别名 `[[MEMORY.md|长期记忆]]`）：5 篇维护/回顾笔记规范化，消除扫描噪声

### 2. 空文件清理（3 个）
- 删除今日 dreaming 空壳：`memory/dreaming/{light,deep,rem}/2026-09-08.md`（无 footer 链接 + 计数 0，按 09-03 细化规则判定最干净可删）
- 09-05/06/07 的 deep/light 空壳带 `> 🗺️ 属于 [[knowledge-map]]` footer → 保守保留

### 3. 标签一致性（6 文件）
- `github trending` → `github-trending`（W31~W35 周报 5 个，规范形为连字符）
- `GitHub Trending` → `github-trending`（W37 周报 1 个）
- 依据：log.md 已记载 `github trending`→`github-trending` 为库内规范，`github-trending` 现有 9 文件为多数形

### 4. 孤立挂载（4 个今日 cron 新笔记，不删页）
- `GitHub-Weekly-2026-09-08` → MOC-GitHub 周报系列
- `skill-audit-2026-09-08` → MOC-Research（skill-audit 序列）
- `CAD自动化MCP参考-pascal-2026-09-08` → MOC-Dev 最近新增
- `hackernews-2026-09-08` → knowledge-map Daily 行
- 4 个均已在 HOME.md 📋 项目与日志挂载

### 5. 补 frontmatter（2 个今日新笔记）
- `Development/CAD自动化MCP参考-pascal-2026-09-08`：tags: [cad, mcp, ai-automation, research, 千轮研究]
- `Research/GitHub-Weekly-2026-09-08`：tags: [github, github-trending, weekly, research]

## ⏭️ 遗留与说明
- `Research/eval-v2-2026-08-31/README.md` 报孤立 = lint README 重名检测盲区（MOC-Research 已有 `[[knowledge/Research/eval-v2-2026-08-31/README]]` 全路径入链），Obsidian 实际有效，不处理
- `2026-09-04-maintenance.md` 中「剥离 `[[` `]]` 方括号」为规则说明 prose → 按 09-04 规范保留不剥（knowledge-lint 判定 0 断链）
- 全仓库严格扫描剩 1 处 `[[`。`]]` 残匹配 = 上述 prose，属设计内保留项
- `skills/hermes/github-repo-optimization.md` 的 13 处 markdown 链接在模板代码块内、`claude-code-opus-5.md` 的 `[file.md]` 为 verbatim 系统提示词 → 均文档化误报，跳过

## 🔗 关联
- [[knowledge/log.md|维护时间线]]
- [[HOME|🏠 首页]]
