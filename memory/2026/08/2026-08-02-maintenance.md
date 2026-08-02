---
tags: [maintenance, vault-health, cron]
---

# 🧹 Vault 维护报告 · 2026-08-02

> 定时维护 cron · 检查文件状态 / 断链 / 空文件 / 标签一致性

## 📊 总览

| 检查项 | 结果 |
|--------|------|
| 仓库 md 文件总数 | 488 |
| 断链 wikilink `[[...]]` | ✅ 0 |
| 断链 markdown 链接 | ✅ 0（14 处均为已知假阳性：代码块内示例） |
| 空/近空文件 | ✅ 已清理 |
| 标签大小写不一致 | ✅ 0 |
| 孤儿笔记 | 47 处遗留（详见下文） |
| git 推送 | ✅ 已修复并同步（曾 ahead 14） |

## ✅ 本次修复

1. **删除 dreaming 空壳笔记（3 个）**
   - `memory/dreaming/deep/2026-08-01.md`、`deep/2026-08-02.md`、`rem/2026-08-02.md`
   - 均为 frontmatter + "Ranked 0 candidate(s)" 空壳，无实质内容

2. **移动游离日志（1 个）**
   - `memory/2026-08-02.md` → `memory/2026/08/2026-08-02.md`（符合 memory/YYYY/MM/ 规范，无引用冲突）

3. **修复内联标签泄漏（3 处）→ 幽灵标签消除**
   - `memory/2026/07/2026-07-29-todo-cleanup.md`：`bug #70482` → `` `#70482` ``
   - `knowledge/Research/krea2-comfyui-deploy-notes.md`：`issue #14717` → `` `#14717` ``
   - `knowledge/Research/skyrim-together-reborn-2p-modlist.md`：`（#111）` → ``（`#111`）``

4. **HOME.md 补充 10 条新笔记链接**（07-31 回顾/TODO/闲鱼执行、08-01 回顾/TODO/反思、08-02 日志、健康报告、arXiv 周报）→ 消除 10 个孤儿

5. **修复 auto-sync 脚本推送分支 bug（重要）**
   - 根因：`obsidian-sync.py` 硬编码 `git push origin main`，但仓库工作分支为 `dev` → 本地持续积压（ahead 14）
   - 修复：改为动态检测当前分支推送（`git branch --show-current`）
   - 已同步修复：`AppData/Local/hermes/scripts/obsidian-sync.py`（部署版，含增强逻辑）+ 技能目录 canonical 副本
   - 修复后验证：`dev...origin/dev` 无 ahead/behind，完全同步

## 📌 遗留：47 个孤儿笔记

- 大部分为 `knowledge/*/*-absorbed.md`（吸收标记桩，内容已并入主笔记，属有意保留）
- `knowledge/Research/*` 研究笔记、`knowledge/Dev/cloudbase-learning-s2~s8` 系列笔记
- `knowledge/Archive/20260728-182639-Example Domain.md`（测试归档，407 字节，非空未删）
- `knowledge/Daily/hackernews-2026-07-31.md` 等
- 建议：随每周整合流程（weekly consolidation）从知识域索引补链

## 📝 断链假阳性备忘（无需处理）

- `skills/hermes/github-repo-optimization.md:116-137` — `markdown` 代码块内示例链接
- `knowledge/Dev/system-prompts-reference/claude-code-opus-5.md:45` — 系统提示词参考中的 `[file.md]` 示例
