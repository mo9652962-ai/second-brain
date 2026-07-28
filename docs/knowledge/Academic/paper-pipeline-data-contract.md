# 论文处理 Pipeline 数据契约

## 输入

```json
{
  "paper": {
    "title": "string",
    "authors": ["string"],
    "abstract": "text",
    "source": "pdf_url | text | docx",
    "target_platform": "知网 | 维普 | 格子达 | Turnitin",
    "deadline": "ISO datetime",
    "requirements": {
      "target_ai_rate": "number (default: <10%)",
      "preserve_terms": ["专业术语保护列表"],
      "format": "GB/T 7714 | 学校模板"
    }
  }
}
```

## 处理流程

1. **Grill 对齐** (5min) → 术语表 + ADR
2. **AI率检测** (2min) → 目标平台初始检测
3. **分段降AI** (15min) → 零感AI + 人工复核
4. **二次检测** (2min) → 确认达标
5. **格式排版** (5min) → Pandoc + 人工微调
6. **交付** → 源文件 + 检测报告

## 输出

```json
{
  "order_id": "string",
  "status": "pending | processing | done",
  "ai_rate_before": "number",
  "ai_rate_after": "number",
  "cost": {
    "tool": "number (零感AI费用)",
    "detection": "number (检测费用)",
    "labor": "number (工时费)"
  },
  "delivery_files": ["file_paths"]
}
```
