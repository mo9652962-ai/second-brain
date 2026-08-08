---
tags: [research, vision, deepseek, mcp, ocr, evaluation]
created: 2026-08-08
type: research
---

# DeepSeek Vision 插件研究 · 2026-08-08

> 来源：小黑盒帖子（deepseek-vision for Codex）+ mcp-vision 底层仓库原文验证。learn→research→apply。

## 核心结论

**插件本体用不上（Codex 专用），但底层 mcp-vision 是通用 MCP Server（支持 OpenCode）；sora 的 Hermes 已有等价能力（vision_analyze），无需安装**。可借鉴的功能点：图片表格→Word 表格、PDF 批量 OCR→DOCX（闲鱼接单场景）。

## 事实（验证后）

### 机制
- deepseek-vision = Codex 插件包装 mcp-vision（MIT）
- 原理：截图/剪贴板 → 插件保存图片 → **交给配置的多模态视觉 API** → 返回文本 → 文本模型（DeepSeek）基于文本推理
- **本质**（帖子作者点破）：所有后期视觉方案都是"视觉任务交给子模型处理成文本再发主模型"——**效果打不过原生多模态**

### mcp-vision 底层（可独立使用）
| 工具 | 用途 | 底层 |
|:---|:---|:---|
| analyze_image | 图片内容分析/问答/图表解读 | 多模态 LLM |
| ocr_extract | 图片/PDF 提取文字 | 多模态 LLM |
| ocr_precise | 精准 OCR（坐标+置信度）| 百度/腾讯传统 OCR |

- Provider：SiliconFlow 默认、OpenAI 兼容协议自定义、百度/腾讯 OCR
- **支持 Claude Code / Codex CLI / Cursor / OpenCode**
- 图片格式：PNG/JPG/GIF/BMP/WebP/PDF；本地路径 + URL

## Apply 评估

| 方案 | 决策 | 理由 |
|:---|:---|:---|
| deepseek-vision 插件 | ❌ 不装 | Codex 专用；sora 用 Hermes |
| mcp-vision 接入 Hermes | 🟡 可选 | Hermes 已支持 MCP；但 vision_analyze 已有等价能力；视觉 key 现缺（SiliconFlow 余额不足）|
| 功能借鉴：表格→Word / PDF批量OCR | 🟢 记入技能评估 | ocr-and-documents 技能已有 pymupdf/marker-pdf；图片表格→Word 表格可增强 |

## 验证的既有判断

- sora 记忆「vision 失败→tesseract OCR 兜底」与插件机制同构——**方案正确性被独立验证**
- 帖子核心洞察「后期视觉方案打不过原生多模态」→ 长期解法是**给主链配原生视觉模型**（如火山 doubao 视觉/开源 Qwen-VL），而不是继续堆 wrapper

## 行动项

| 优先级 | 项 | 说明 |
|:---|:---|:---|
| 🟢 P2 | 图片表格→Word 表格增强 | ocr-and-documents 技能补表格提取步骤（闲鱼文档单）|
| 🟢 P2 | 原生视觉模型评估 | 找 sora 主链可用的视觉 key（替代 wrapper 路线）|

_生成: k (Hermes) · 2026-08-08 · learn→research→apply_

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
