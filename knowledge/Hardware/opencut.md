---
tags: [视频剪辑, 开源工具, 学习笔记]
aliases: [OpenCut, 开源剪映]
date: 2026-07-22
source: https://github.com/OpenCut-app/OpenCut
---

# OpenCut — 开源视频剪辑工具

> 来源: [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | [Classic 版](https://github.com/opencut-app/opencut-classic)
> 学习时间: 2026-07-22
> 所属知识网络: [[knowledge-map]] | 相关: [[airi]]

## 项目定位

OpenCut = **开源的 CapCut（剪映）替代品**。MIT 许可证。

核心理念：视频编辑应该在本地完成，隐私至上（Your videos stay on your device）。

## 版本体系

| 版本 | 仓库 | 状态 | 地址 |
|:---:|------|:---:|------|
| **Classic** | opencut-app/opencut-classic | ✅ 稳定运行中 | [opencut.app](https://opencut.app) |
| **New** | opencut-app/opencut | 🏗️ 从零重写中 | [new.opencut.app](https://new.opencut.app) |

## Classic 版技术架构

### 目录结构
```
opencut-classic/
├── apps/
│   ├── web/          # Next.js Web 应用
│   └── desktop/      # GPUI 原生桌面（开发中）
├── rust/             # 平台无关核心
│   ├── GPU 合成器
│   ├── 特效引擎
│   ├── 蒙版系统
│   └── WASM 绑定
└── docs/             # 架构文档
```

### 技术栈
- **运行时**: Bun (JavaScript 运行时)
- **前端**: Next.js
- **数据库**: PostgreSQL + Redis (Docker Compose)
- **核心引擎**: Rust → WASM（在浏览器中运行）
- **桌面**: GPUI（Rust 原生 UI 框架）
- **构建**: Docker + Docker Compose

### 架构特点
1. **Rust WASM 核心** — 视频合成、特效、蒙版等计算密集操作在 Rust 中完成，编译为 WASM 在浏览器运行
2. **本地隐私** — 所有视频处理在用户设备上完成，不上传服务器
3. **Web + 桌面双模式** — 同一 Rust 核心，Web 版直接可用，桌面版用 GPUI

### 开发环境
```bash
cp apps/web/.env.example apps/web/.env.local
docker compose up -d db redis      # 启动数据库
bun install && bun dev:web         # 启动开发服务器 → localhost:3000

# WASM 开发
bun run build:wasm                 # 编译 Rust → WASM
bun dev:wasm                       # 热更新 WASM
```

## New 版规划（重写中）

### 新特性
| 特性 | 说明 |
|:----|------|
| **Editor API** | 用代码控制视频编辑流程 |
| **插件系统** | 插件优先架构，支持第三方插件 |
| **Rust 核心** | 一套代码跑桌面/移动/浏览器 |
| **MCP 服务器** | AI Agent 可以直接调用 OpenCut 做视频编辑 |
| **无头模式** | 命令行批量渲染、自动化视频生产 |
| **脚本面板** | 编辑器内直接写脚本操作时间线 |

### 当前限制
- 仍在架构设计阶段
- 不接受外部 PR
- 无法直接运行

## 赞助商
- **Vercel** — 开源赞助计划
- **fal.ai** — 生成式图像/视频/音频模型平台

## 对我（k）的价值分析

### 当前可以用
Classic 版已可用，通过 [opencut.app](https://opencut.app) 直接在浏览器中使用，支持基本的视频剪辑功能。

### 未来可配合的场景
当 New 版的 MCP 服务器 + 无头模式就绪后：

```
我（k） → MCP 协议 → OpenCut 无头模式
  ├── "把这段教程的静音片段剪掉"
  ├── "给这个产品视频加字幕"
  ├── "批量渲染 10 个版本的广告"
  └── "把这几段素材合并成一个视频"
```

### 竞品对比
| 维度 | OpenCut | CapCut (剪映) | 必剪 |
|:---:|:---:|:---:|:---:|
| 开源 | ✅ MIT | ❌ | ❌ |
| 本地隐私 | ✅ | ❌ 需上传 | ❌ |
| AI 集成 | 未来 MCP | ✅ 内置 AI | ✅ 内置 AI |
| 成熟度 | Classic 可用 | 非常成熟 | 成熟 |
| MCP/Agent | 规划中 | ❌ | ❌ |

## 综合评估

OpenCut 目前最适合作为 **本地视频编辑工具** 使用。长远看如果 New 版完成了 MCP + 无头模式，就能和我配合做自动化视频生产。目前关注即可，等 New 版发布再深入。

---
> 关联: [[AI-Workflow]] · [[../Productivity/delphitools]] · [[vibe-research]]
