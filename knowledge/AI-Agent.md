---
tags: [ai-agent, openclaw]
created: 2026-07-21
---

# AI Agent 知识库

## 我的 Agent 架构

- **Agent**: k（基于 OpenClaw 2026.7.1）
- **模型**: deepseek-v4-pro → kimi-k2.6 → qwen3.7-plus → glm-5.2
- **Skills**: 26 个（9 论文 + 6 PPT + 7 图片 + 3 自我改进 + 1 搜索）
- **搜索**: Tavily + Firecrawl + Exa 三引擎冗余

## 核心能力

### PPT 制作
- 6 个 skills 全家桶协同
- 2026 趋势：Async-First、移动端、卡片式、AI 图像
- 支持学术/商业/故事三种叙事框架

### 学术论文
- 9 个 skills 覆盖检索→翻译→润色→SCI 精修
- 知网高级检索 + SCI/SSCI 期刊索引检查

### 图片生成
- 7 个 skills 覆盖文生图、图生图、风格迁移
- 支持中英文提示词

## 配置要点

- 受保护路径 → 直接编辑 `openclaw.json` → `gateway restart`
- 搜索超时 → 120s
- npm 安装 → 先切 npmmirror 镜像

## 变现路径

- 🥇 AI PPT 代做（最强）
- 🥈 学术论文服务
- 🥉 AI Agent 定制
