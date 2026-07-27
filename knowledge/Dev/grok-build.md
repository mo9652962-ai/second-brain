---
tags: [AI编码工具, 开源工具, 学习笔记, xAI]
aliases: [Grok Build, xAI Coding Agent]
date: 2026-07-22
source: https://github.com/xai-org/grok-build
---

# Grok Build — xAI 开源 AI 编码 Agent

> 来源: [xai-org/grok-build](https://github.com/xai-org/grok-build)
> 学习时间: 2026-07-22 (更新: 2026-07-27) | ⭐ 22.6K (⬆ 13K/周)
> 所属知识网络: [[knowledge-map]] | 相关: [[airi]] | [[opencut]] | [[codebase-memory-mcp]]

## 简介

Grok Build 是 **SpaceXAI (xAI) 的终端 AI 编码 Agent** — 开源的 Rust 实现，全屏 TUI 界面，类似 Claude Code / OpenCode。

## 核心特征

- **全屏 TUI**: 终端中的全屏交互式界面，鼠标可操作
- **Rust 实现**: 性能优先，跨平台（macOS / Linux / Windows）
- **ACP 支持**: Agent Client Protocol — 可嵌入编辑器
- **MCP**: 支持 Model Context Protocol 服务器
- **Headless 模式**: 可脚本化、CI/CD 集成
- **Sandbox**: 沙箱隔离

## 技术架构

```
xai-grok-pager-bin (入口)
    ↓
xai-grok-pager (TUI: 滚动、提示、模态框、渲染)
    ↓
xai-grok-shell (Agent 运行时: leader/stdio/headless)
    ↓
xai-grok-tools (工具实现: 终端、文件编辑、搜索...)
    ↓
xai-grok-workspace (文件系统、VCS、执行、检查点)
    ↓
配置 / MCP / Markdown / 沙箱...
```

## 安装

```bash
curl -fsSL https://x.ai/cli/install.sh | bash   # macOS/Linux
irm https://x.ai/cli/install.ps1 | iex            # Windows
grok --version
```

## 从源码构建

```bash
cargo install dotslash
cargo run -p xai-grok-pager-bin    # 开发模式启动 TUI
cargo build -p xai-grok-pager-bin --release  # 编译发布版
```

## 技术细节

- **语言**: Rust
- **许可证**: Apache 2.0
- **文档**: [docs.x.ai/build/overview](https://docs.x.ai/build/overview)
- **仓库**: 从 xAI 内部 monorepo 定期同步到 GitHub

## 竞品对比

| 维度 | Grok Build | OpenCode | Claude Code |
|:---:|:---:|:---:|:---:|
| 开发商 | xAI | Anomaly (SST) | Anthropic |
| 语言 | Rust | TypeScript | TypeScript |
| TUI | ✅ 全屏 | ✅ | ✅ |
| 开源 | ✅ Apache 2.0 | ✅ MIT | ❌ |
| MCP 支持 | ✅ | ✅ | ✅ |
| ACP 支持 | ✅ | ❌ | ❌ |
| 模型 | Grok 系列 | 75+ 供应商 | Claude |
| 平台 | Mac/Linux/Win | Mac/Linux/Win | Mac/Linux |

## 综合评估

| 维度 | 评价 |
|:---:|:------|
| 适合做 skill | ❌ 是一个独立产品（AI 编码 Agent），不是 Agent skill |
| 当前状态 | ✅ Apache 2.0 开源，可构建运行 |
| 值得关注 | ✅ xAI 的开源编码 Agent，Rust 实现有性能优势 |
