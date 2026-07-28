# PPT Pipeline 定义 v1.0

> 6 个 Skills 的 Pipeline 编排：触发条件 → 数据流 → Gate 检查
> 基于 AI-Workflow 五大编排模式之 Pipeline/Sequential

## 触发条件

```
用户说「做PPT」「生成幻灯片」「学术汇报」「旅游展示」...
  ↓
自动激活: cn-ppt-outline-writer → pptx-generator → ppt-optimizer
额外可选: openclaw-slides → academic-presentation
```

## Pipeline 流程

```
Phase 1: Outline
  Skill: cn-ppt-outline-writer
  输入: 用户主题/需求
  输出: outline.json
  检查点: 大纲完整性 (标题/分页/数据点)

Phase 2: Generate  
  Skill: pptx-generator
  输入: outline.json (JSON 数据契约)
  输出: presentation.pptx + slides/ 目录
  检查点: 每页是否独立可读 (Async-First 检查)

Phase 3: Optimize
  Skill: ppt-optimizer
  输入: presentation.pptx
  输出: presentation_optimized.pptx + report.json
  检查点: 移动端适配 / 卡片布局评分 / 3D 一致性
  Gate: score >= 60 → 通过; < 60 → 返回 Phase 1

Phase 4: Slides (可选, 用于网页展示)
  Skill: openclaw-slides
  输入: outline.json
  输出: index.html

Phase 5: Academic (可选, 学术场景)
  Skill: academic-presentation
  输入: outline.json + 论文全文
  输出: academic_presentation.pptx
```

## 数据契约: outline.json

```json
{
  "title": "演示标题",
  "meta": {
    "type": "academic|business|creative",
    "slides_count": 10,
    "style": "warm-minimal",
    "audience": "async-first",
    "mobile_ready": true
  },
  "slides": [
    {
      "index": 1,
      "type": "title",
      "title": "封面标题",
      "subtitle": "副标题(可选)",
      "notes": "演讲者备注"
    },
    {
      "index": 2,
      "type": "content|card|comparison|chart|quote|image|ending",
      "title": "页面标题 (<40字)",
      "body": "正文内容...",
      "data": { "type": "chart|table|stat", "source": "数据来源" },
      "image_prompt": "用于AI图片生成的提示词",
      "layout": "single|two-column|grid|full-image",
      "notes": ""
    }
  ]
}
```

## Gate 检查 (Phase 3)

```json
{
  "score": 72,
  "checks": {
    "async_friendly": { "pass": true, "score": 18, "note": "每页独立可读" },
    "mobile_ready": { "pass": true, "score": 15, "note": "字号>=18pt" },
    "card_layout": { "pass": true, "score": 14, "note": "卡片式结构" },
    "warm_color": { "pass": true, "score": 10, "note": "暖色调配色" },
    "visual_density": { "pass": false, "score": 8, "note": "第3页文字过密" },
    "ai_image_detection": { "pass": true, "score": 7, "note": "AI图像风格统一" }
  },
  "threshold": 60,
  "passed": true
}
```

## Schedule

| Phase | Skill | 预计耗时 | 并行 |
|-------|-------|----------|------|
| 1 | outline-writer | 2-5 min | - |
| 2 | pptx-generator | 5-10 min | - |
| 3 | ppt-optimizer | 2-3 min | - |
| 4+5 | slides/academic | 3-5 min | 可并行 |

---
[[HOME|🏠 返回首页]]
