---
type: maintenance
tags: [maintenance, vault, obsidian]
created: 2026-08-18
---

# 2026-08-18 Vault 维护：断链修复 + 空壳清理 + 孤立补链

> 执行：全量诊断（full-vault-diagnostic）→ 分类 → 修复 → 复跑验证 → 提交

## 📊 总览

| 指标 | 修复前 | 修复后 |
|:---|:---|:---|
| 断链 wikilink | 9 | 0 |
| 断链 markdown 链接（真实） | 2 | 0 |
| 空/近空文件 | 2 | 0 |
| 标签大小写/单复数冲突 | 0 | 0 |
| 孤立笔记补链 | 4 篇 | 已挂 MOC |

## 一、断链修复（9 处 wikilink + 2 处 markdown）

**技能名 wikilink → 纯文本反引号（8 处，Hermes 技能非 vault 笔记）：**
- `agent-infra-weekly-2026-08-17.md`：`engineering-workflow`
- `code-graph-rag-2026-08-16.md`：`code-review-graph`
- `diagram-design-2026-08-16.md`：`ppt-design-2026`、`baoyu-infographic`
- `game-engine-ai-research-2026-08-17.md`：`engineering-workflow`
- `needle-tiny-model-2026-08-16.md`：`local-llm-inference`、`microcontroller-edge-ai`、`8051-embedded-dev`

**MOC 不存在（1 处）：**
- `knowledge/AI漫剧制作全流程.md`：`MOC-AI`（AI 域已合并为空）→ `[[MOC-Dev]]`；文件已 `git mv` 归入 `knowledge/Dev/`，MOC-Dev 补索引行

**markdown 相对路径（2 处）：**
- `arxiv-2026-08-16-agent-llm.md`、`arxiv-2026-08-16-core-contributions.md`：`HOME(../HOME.md)` 从 `knowledge/Research/` 解析到不存在的 `knowledge/HOME.md` → `HOME(../../HOME.md)`（指向 vault 根）

**保留的假阳性（不修）：** `claude-code-opus-5.md:45 [file.md]`（verbatim system prompt 示例）、`skills/hermes/github-repo-optimization.md` 13 处（fenced code block 模板示例）

## 二、空壳清理（2 个）

| 文件 | 大小 | 处理 |
|:---|:---|:---|
| `memory/dreaming/light/2026-08-18.md` | 37B（No notable updates） | 删除 |
| `memory/dreaming/deep/2026-08-18.md` | 103B（Ranked 0 candidate(s)） | 删除 |

`rem/2026-08-18.md`（1397B）有 Reflections 实质内容，保留。删除前已确认无任何引用。

## 三、孤立笔记补链（4 篇 → MOC）

- `knowledge/Dev/link-content-fetch-2026-08-17.md` → `[[MOC-Dev]]`（MOC-Dev 核心笔记区补索引）
- `knowledge/Security/silver-fox-defense-2026-08-17.md` → `[[MOC-Security]]`
- `knowledge/Security/src-bug-hunting-2026-08-17.md` → `[[MOC-Security]]`
- `knowledge/Security/src-hunting-earnings-2026-08-17.md` → `[[MOC-Security]]`

MOC-Security 新建「🌐 Web 安全 / SRC 挖洞」分区，计数 12 → 15。
MOC-Research「其他」区补 `arxiv-2026-08-18-agent-llm`。

## 三点五、验证补漏（ad-hoc 验证发现）

验证脚本（hermes-verify-vault-maintenance-2026-08-18.py）抓出 DIR_MOC 两个真实盲区：

- `knowledge/Finance/` 有 MOC-Finance 但映射缺失（08-15/08-17 两篇每日股票分析从未被补链）→ 新增映射 `knowledge/Finance: MOC-Finance`，补链 2 篇 + MOC-Finance 索引补 08-17
- `knowledge/Creative/` 有文件但无映射无 MOC（novel-worldbuilding 孤立）→ 新增映射 `knowledge/Creative: knowledge-map`，补链 1 篇

另修维护笔记自身：文档旧断链示例的 `[[]]` wikilink 语法已剥离（防自己成为下轮断链来源，技能 Pitfall 已知模式）。

## 三点六、标签归一（最终验证发现，5 组大小写变体）

ad-hoc 验证脚本发现 frontmatter tags 大小写变体（Obsidian 标签大小写敏感），按多数派/惯例统一到小写：

| 变体 | 归一 | 依据 |
|:---|:---|:---|
| GitHub(3) → github(21) | github | 多数派 |
| Agent(2) → agent(3) | agent | 多数派 |
| MCP(1) → mcp(6) | mcp | 多数派 |
| Godot(1) → godot(1) | godot | 平局按 vault 小写惯例 |
| Security(1) → security(8) | security | 多数派 |

涉及 6 个文件（agent-infra-weekly、spacetime-diagram-edge、MOC-GitHub、code-graph-rag、game-engine-ai-research、MOC-Security）。只改 frontmatter `tags:` 行，不碰 inline tag。full-vault-diagnostic 未报这些（其标签检查只查连字符模式），ad-hoc 全量扫描才抓到——后续诊断需覆盖全量 frontmatter tags。

## 四、脚本修复（防复发）

`scripts/daily_vault_optimize.py` DIR_MOC 清理：
- **移除** 8 个已空目录的过期映射（AI→MOC-AI、Academic→MOC-Academic、Design→MOC-Design、Content/arXiv/Python/Tools/writing-material）——避免未来给孤立笔记补链到不存在的 MOC 制造新断链
- **新增** `knowledge/Security → MOC-Security`（此前 Security 域孤立笔记从未被补链，属漏项）

## 五、遗留（非本轮范围）

- `memory/` 下 cron 产出孤儿（daily-review/todo-executor/reflection 等 ~20 篇）——已知模式，需从 cron 脚本源头挂 HOME.md 链接
- `memory/.archive/`、`memory/archive/`、`memory/dreaming/` 历史孤儿——归档区非活跃，可接受
- `knowledge/Daily/hackernews-*.md` 已有 `[[knowledge-map]]` 出链，半连接状态

---
> 🗺️ 属于 [[knowledge-map]] · [[HOME|🏠 首页]]
