---
title: 知识库索引
type: 索引
created: 2026-09-05
updated: 2026-09-20
tags: [meta, vault-maintenance]
---

# 📇 知识库索引 — Knowledge Index

> **AI 翻库第一入口。** 这里是路由层，不是内容层——先在此定位域，再进 MOC，最后 read_file 具体页面。
> 全量页面清单在 [[knowledge-map]]（唯一真相源）。本页只做**域级路由**，不重复登记页面。

## 🧭 三层定位法

```
index.md（本页）     ← 你在哪一层：域路由，10 行
   ↓
MOC-<域>.md          ← 该域全部页面索引
   ↓
具体页面 .md          ← read_file 深入
```

## 🗂 域路由表

| 域 | MOC 入口 | 规模 | 典型内容 |
|:---|:---|:---|:---|
| 全量总图 | [[knowledge-map]] | 600+ | **所有页面的完整索引（唯一真相源）** |
| Research | [[MOC-Research]] | 221 | 千轮研究、多 Agent、AI 论文深研 |
| Dev | [[MOC-Dev]] | 137 | 软件工程、前端/后端、部署、系统设计 |
| Security | [[MOC-Security]] | 53 | SRC、逆向、防御加固、合规 |
| Productivity | [[MOC-Productivity]] | 52 | PPT、写作、文档、效率工具 |
| Hardware | [[MOC-Hardware]] | 21 | PCB/KiCad/FreeCAD/单片机 |
| Finance | [[MOC-Finance]] | 16 | A股、量化、自选股分析 |
| GitHub | [[MOC-GitHub]] | 58 | GitHub 项目实证研究 |
| Inbox | [[MOC-Inbox]] | 53 | 待接入笔记（未挂载入口） |

> 无独立 MOC 的域（AI/Content/Daily/cards/SOP/Education/Creative/Product/gaming）→ 统一登记在 [[knowledge-map]] 与 [[MOC-Inbox]]。

## 🛠 治理资产（META）

| 资产 | 位置 | 用途 |
|:---|:---|:---|
| 查询纪律 | [[knowledge/META/KNOWLEDGE-QUERY-RULES]] | 回答必须标来源页面 |
| 体检脚本 | `META/scripts/knowledge-lint.py` | 只读扫描断链/孤立/frontmatter/重复 |
| 知识库方法论 | [[knowledge/AI/知识库-AI不翻知识库根因-2026-09-04]] | 「差的不是资料，是最上面那层规则」 |
| 工具精度方法论 | [[knowledge/AI/工具精度方法论-假阳性税与知识库Lint-2026-09-05]] | 假阳性税 + Precision/Recall 4 问 |
| 操作时间线 | [[log]] | append-only 的 ingest/lint/query 记录 |

## 📐 使用规则（AI 必读）

1. **回答前先读本页**定位域 → 进对应 MOC → read_file 具体页面；不要凭记忆作答
2. **回答必须标注依据**：说明结论来自哪些具体页面，不写泛泛的「根据知识库」
3. **新页面必须挂载**：创建后 24h 内进对应 MOC（`scripts/daily_vault_optimize.py` 已自动兜底）
4. **有价值的回答写回**：实质分析存回 `knowledge/`，不收藏即止
5. **维护动作进 log**：每次 ingest/lint/query 追加到 [[log]]

---

*本页为路由层，页面清单以 [[knowledge-map]] 为准。更新于 2026-09-20（双轨合并：删除重复的页面级登记）。*
