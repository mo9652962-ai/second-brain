---
tags: [absorbed, skills, methodology]
source: flyai · 技能详解 + kepano/obsidian-skills (43.4k⭐)
date: 2026-07-27
---

# Agent Skills · 认知升级 + obsidian-skills 安装

> Prompt = 这一次的要求 · Skill = 这一类任务的标准化做法 · MCP = 外部系统连接

---

## 🧠 Prompt vs Skill vs MCP

| 层次 | 范围 | 示例 |
|:-----|:------|:------|
| **Prompt** | 单次指令 | "写一篇短视频推荐算法的论文，3000字" |
| **Skill** | 一类任务的标准流程 | 论文写作 Skill：先确认格式→检索→核验→大纲→起草→检查引用 |
| **MCP** | 外部系统接口 | 连接 Zotero、学校资料库 |

## 📁 Skill 结构

```
skill-name/
├── SKILL.md        # 入口：name + description + 具体步骤
├── references/     # 规范、领域资料、操作文档
├── scripts/        # 格式校验、数据处理脚本
└── assets/         # 模板、样式
```

## ⚡ 渐进式加载

1. 仅加载 `name` + `description`（像目录）
2. 命中 Skill 后，才读取完整 SKILL.md
3. 执行到具体步骤时，再按需打开 references/ 或 scripts/

✅ 我们已经在用这个模式

## 🎯 Skill 优化方法（最值）

测试一个 Skill 至少要覆盖 **4 种情况**：
1. 要求完整（正常）
2. **要求模糊**（缺信息）
3. **资料不足**（找不到来源）
4. **用户要求编造**（测试反谄媚边界）

好的 Skill 应该知道什么时候停下来问，而不是无论如何都输出。

## 🔧 obsidian-skills 已安装（5 个）

| Skill | 用途 |
|:------|:------|
| **obsidian-markdown** | 创建/编辑 Obsidian 格式 markdown（wikilink/callout/properties） |
| **obsidian-bases** | 创建/编辑 .base 文件 |
| **json-canvas** | 创建/编辑 .canvas 文件（Obsidian Canvas） |
| **obsidian-cli** | 通过 CLI 交互 Obsidian |
| **defuddle** | 从网页提取干净 markdown |
