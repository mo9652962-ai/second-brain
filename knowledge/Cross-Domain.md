---
tags: [cross-domain, index]
domain: cross-reference
created: 2026-07-21
---

# 🔀 交叉领域索引

> 自动收集所有跨域关联的内容。由 Dataview 动态生成，无需手动维护。

## 按交叉域分组

### 🤖 AI-Agent 相关

```dataview
TABLE file.mtime AS "更新时间", tags
FROM "knowledge" OR "projects"
WHERE contains(cross-domain, "ai-agent") AND file.name != "AI-Agent"
SORT file.mtime DESC
```

### 🔀 AI-Workflow 相关

```dataview
TABLE file.mtime AS "更新时间", tags
FROM "knowledge" OR "projects"
WHERE contains(cross-domain, "workflow") AND file.name != "AI-Workflow"
SORT file.mtime DESC
```

### 🎨 PPT-Design 相关

```dataview
TABLE file.mtime AS "更新时间", tags
FROM "knowledge" OR "projects"
WHERE contains(cross-domain, "ppt-design") AND file.name != "PPT-Design"
SORT file.mtime DESC
```

### 📚 Academic 相关

```dataview
TABLE file.mtime AS "更新时间", tags
FROM "knowledge" OR "projects"
WHERE contains(cross-domain, "academic") AND file.name != "Academic"
SORT file.mtime DESC
```

### 💻 Vibe-Coding 相关

```dataview
TABLE file.mtime AS "更新时间", tags
FROM "knowledge" OR "projects"
WHERE contains(cross-domain, "vibe-coding") AND file.name != "Vibe-Coding"
SORT file.mtime DESC
```

---

## 全部跨域关联矩阵

```dataview
TABLE domain AS "领域", cross-domain AS "交叉域", file.mtime AS "最后更新"
FROM "knowledge"
WHERE cross-domain
SORT domain ASC
```

---

## 🔗 知识关联

- **[[HOME]]** — 返回知识中枢
- **[[Second Brain]]** — Canvas 视觉图谱
