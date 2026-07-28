---
tags: [meta, graph, tags, 指南]
created: 2026-07-28
---

# 🎨 图谱颜色分组指南

> 在 Obsidian 中使用这些设置，让图谱从混乱变清爽

---

## 📊 颜色分组设置

**操作路径：** 图谱视图 → 设置 ⚙️ → 分组 → 新建分组

### 分组 1：知识域标识（按文件夹）

| 分组名 | 筛选规则 | 颜色 |
|--------|---------|------|
| 📚 Academic | `path: knowledge/Academic` | 🟢 `#22C55E` |
| 🤖 AI Agent | `path: knowledge/AI` | 🔵 `#3B82F6` |
| 🎨 Design | `path: knowledge/Design` | 🟣 `#8B5CF6` |
| 💻 Dev | `path: knowledge/Dev` | 🟠 `#F97316` |
| 🔧 Hardware | `path: knowledge/Hardware` | 🔴 `#EF4444` |
| 🏠 Productivity | `path: knowledge/Productivity` | 🟡 `#EAB308` |

### 分组 2：技能域标识

| 分组名 | 筛选规则 | 颜色 |
|--------|---------|------|
| 🛠️ 我的技能 | `path: skills/hardware OR path: skills/hermes OR path: skills/web` | 🟢 `#10B981` |
| 👥 社区技能 | `path: skills/@` | ⚪ `#6B7280` |

### 分组 3：图谱筛选器（减少噪音）

| 筛选器 | 规则 | 目的 |
|--------|------|------|
| 🔇 隐藏社区技能 | `-path: skills/@` | 隐藏 34 个社区技能文件夹 |
| 🔇 隐藏模板 | `-path: templates` | 模板文件不需要在图中 |
| 📅 只看知识 | `path: knowledge` | 纯知识域视图 |

---

## 🏷️ 标签系统标准化

### 当前问题

```
#1a1a1a     ← 颜色代码被当成标签
#include    ← C/C++ 代码片段被当成标签
#2, #3      ← 数字被当成标签
```

### 标准标签列表

| 类别 | 标签 | 用途 |
|------|------|------|
| **知识域** | `#AI` `#Academic` `#Dev` `#Hardware` `#Design` | 知识分类 |
| **文档类型** | `#MOC` `#reflection` `#daily` `#weekly` `#feature` | 文档角色 |
| **状态** | `#completed` `#in-progress` `#backlog` `#abandoned` | 进度追踪 |
| **来源** | `#research/10round` `#cron/arxiv` `#manual` `#absorbed` | 知识来源 |

---

## 📁 清理建议

1. **移除颜色代码标签** — 替换为 Obsidian CSS 主题设置
2. **将 C/C++ 代码标签迁移到独立代码笔记** — 不混入知识标签
3. **为所有未分类笔记添加域标签** — 确保每个笔记至少有一个域标签

---
*此文件为优化指南，不参与图谱可视化*
