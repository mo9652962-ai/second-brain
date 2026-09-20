---
title: 知识库例行维护 2026-09-20
type: maintenance
created: 2026-09-20
tags: [knowledge/productivity, vault-maintenance, lint]
---

# 知识库例行维护 2026-09-20

> 例行 cron：体检 → 修断链 → 清空文件 → 统一标签。knowledge-lint 从 8 问题降到 0。

## 修复项（本会话）

| 项 | 文件 | 操作 |
|:---|:---|:---|
| 真断链 | README.md:164 | memory/2026/2026-09-10.md → memory/2026/09/2026-09-10.md（缺一层 09/） |
| 标签大小写 | knowledge/AI/semif-logit-decisions-2026-09-20.md | frontmatter 裸 tag AI → ai（库内规范：knowledge/ai 小写） |
| 标签大小写 | knowledge/Content/竞品对标-AI商业广告接单教程.md | 正文话题 inline tag #AI → #ai |
| 垃圾文件 | temp_extracted_content.md | 删除（UTF-16 残留提取内容，git rm） |
| 空壳清理 | memory/dreaming/deep/2026-09-20.md（103B） | 删除（仅计数器行、无 footer、无入链） |
| 空壳清理 | memory/dreaming/rem/2026-09-20.md（128B） | 删除（No strong patterns、无 footer、无入链） |

## 并发进程已修复（同日其他 cron/会话，验证无需重复处理）

| 项 | 说明 |
|:---|:---|
| award-defense-presentation 断链 ×2 | PPT SOP 关联已改反引号纯文本（技能引用） |
| MOC-Content 断链 | GEO 研究改指 MOC-Inbox（Content 域实际入口） |
| 孤立挂载 ×3 | 即梦Seedance → MOC-Inbox + knowledge-map；React-Bits → MOC-Dev；hackernews-09-20 → Daily |
| frontmatter 补齐 | system-cleanup-report-20260920.md（并发进程已补） |

## 已知遗留（不处理，记录在案）

- 14 个 markdown 链接误报：claude-code-opus-5 verbatim prompt（1）+ skills/hermes/github-repo-optimization.md 代码块模板（13）
- ~100 个 orphan：绝大多数为 .hermes/.venv/skills 基础设施 + memory/.archive 归档区 + 历史 cron 产出（8-9 月 daily-review/todo-executor/reflection/health 等，非活跃）
- 1 组重复文件名：Dev/system-prompts-reference/README.md vs Research/eval-v2-2026-08-31/README.md（低风险）
- 备份：.backup/knowledge-lint-20260920/knowledge-backup.tar.gz（7.5MB）

## 验证结果

- knowledge-lint：Broken wikilinks 0 / Missing frontmatter 0 / Orphan 0 / Short pages 0
- vault-structure：Broken wikilinks 0 / Tag case 0 / Empty（仅 .venv 基础设施 1）

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
