---
tags: [knowledge, ai-image, prompt-engineering, reverse-prompting]
domain: AI-Workflow
created: 2026-07-23
updated: 2026-07-23
---

# 反推提示词工程（Reverse Prompting）

> 关联 Skill: `ai-image-generation` §九

## 工作流

```
Step 1 → 把图丢给视觉 AI（豆包/Qwen3-VL）
Step 2 → AI 逐维度分析图片，生成结构化描述
Step 3 → 复制完整提示词
Step 4 → 喂给任意生图模型
Step 5 → 得到同风格变体
```

## 7 类图片反推框架

### 📷 摄影类
光线(自然/柔光/逆光)、景深、焦距、画质(8K/胶片)、色调(冷/暖/复古)、构图

### 🎨 插画类
手绘/板绘、平涂/厚涂、赛璐璐/二次元/国风、线条粗细、色彩搭配

### 🏗️ 3D 类
卡通/写实/黏土/磨砂、材质(金属/玻璃/PBR)、三点布光、OC渲染

### 🧸 IP 角色类
Q版/潮玩/盲盒、头身比、材质(哑光/树脂/PVC)、服饰装饰

### 🌄 风景类
季节/时段、云天、植被、水体、色调撞色、镜头感

### ✏️ 字体/Logo
风格(现代/赛博/手写)、字形、立体效果、材质、特效

### 🖼️ 通用
中英双语、风格/光线/材质/镜头/配色全维度

## Qwen3-VL 独有能力
- 32 语种 OCR
- 空间理解（2D/3D 定位）
- 多图推理
- 262K 上下文

## 配置
- 视觉模型: `Qwen/Qwen3-VL-32B-Instruct`（SiliconFlow）
- 替代: `Qwen3-VL-32B-Thinking`（CoT 推理增强）
- 轻量: `Qwen3-VL-8B-Instruct`
