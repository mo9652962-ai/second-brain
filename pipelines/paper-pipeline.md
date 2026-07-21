# Paper Pipeline 定义 v1.0

> 9 个 Skills 的 Fan-Out → Pipeline → Gate 编排

## 触发条件

```
「搜论文」「写论文」「查文献」「SCI润色」「论文降重」...
  ↓
自动激活: cnki-scholar (+ cnki-advanced-search 并行)
         → paper-parse (深度研读)
         → paper-writing-workflow (写作)
         → sci-paper-three-pass (润色)
```

## Pipeline 流程

```
Phase 1: Search (Fan-Out 并行)
  ┌─ cnki-scholar ──┐
  │  (OpenAlex API)  │
  └──────────────────┘
         +
  ┌─ cnki-advanced-search ──┐
  │  (知网高级检索 + CSSCI)  │
  └─────────────────────────┘
         ↓ 合并去重
  Phase 1 输出: papers.json

Phase 2: Filter
  Skill: journal-sci-ssci-checker
  输入: papers.json
  输出: filtered_papers.json (SCI/SSCI 标记)

Phase 3: Deep Read (Fan-Out 并行)
  Skill: paper-parse (每篇论文一个实例)
  输入: paper PDF/URL
  输出: paper_analysis_{id}.json

Phase 4: Write
  Skill: paper-writing-workflow
  输入: papers.json + 研究大纲
  输出: draft.md

Phase 5: Polish
  Skill: sci-paper-three-pass (SCI 四刀精修)
  输入: draft.md
  输出: final.md + polish_report.json

Phase 6: De-AI (可选)
  Skill: chinese-academic-writing
  输入: final.md
  输出: de_ai_final.md
```

## 数据契约

### papers.json (Phase 1→2→3)
```json
{
  "query": "检索关键词",
  "source": "cnki|openalex",
  "results": [{
    "id": "unique_id",
    "title": "论文标题",
    "authors": ["作者1", "作者2"],
    "year": 2026,
    "journal": "期刊名",
    "doi": "10.xxx",
    "abstract": "摘要",
    "keywords": ["关键词"],
    "citation_count": 42,
    "sci_indexed": true,
    "ssci_indexed": false,
    "csci_indexed": true
  }]
}
```

### paper_analysis_{id}.json (Phase 3→4)
```json
{
  "paper_id": "unique_id",
  "part_a": {
    "title": "深度专业解析",
    "methodology": { ... },
    "contributions": [...],
    "limitations": [...],
    "technical_depth": 8
  },
  "part_b": {
    "title": "核心逻辑提炼",
    "core_idea": "一句话核心",
    "key_findings": [...],
    "practical_value": "实际价值"
  }
}
```

### polish_report.json (Phase 5)
```json
{
  "passes": {
    "grammar_pass": { "issues": 12, "fixed": 12 },
    "logic_pass": { "issues": 5, "fixed": 4 },
    "format_pass": { "issues": 3, "fixed": 3 },
    "ai_pattern_pass": { "patterns_found": 8, "replaced": 7 }
  },
  "score": 85,
  "ready_for_submission": true
}
```

## Gate 检查

| 阶段 | 检查点 | 阈值 | 阻断行为 |
|------|--------|------|----------|
| Phase 1→2 | 结果数 > 0 | >0 | 无结果→换关键词重试 |
| Phase 2→3 | SCI/SSCI 命中率 | >30% | 低质量期刊→搜索补强 |
| Phase 3→4 | 深度分析完成度 | >80% | 未完成→换模型重读 |
| Phase 5→6 | 润色评分 | >75 | 低于75→回Phase 4 |

## Schedule

| Phase | 并行 | 预计耗时 |
|-------|------|----------|
| 1 Search | ✅ 双引擎并行 | 3-5 min |
| 2 Filter | - | 1 min |
| 3 Read | ✅ 按论文并行 | 3-5 min/篇 |
| 4 Write | - | 10-20 min |
| 5 Polish | - | 5-10 min |
| 6 De-AI | - | 3-5 min |
