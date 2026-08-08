---
tags: [AI编码工具, mcp, 知识图谱, 学习笔记]
aliases: [Codebase Memory MCP, DeusData]
date: 2026-07-27
source: https://github.com/DeusData/codebase-memory-mcp
status: watch
---

# Codebase Memory MCP — 代码知识图谱引擎

> 来源: [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
> ⭐ 33.3K | 论文: [arXiv:2603.27277](https://arxiv.org/abs/2603.27277)
> 学习时间: 2026-07-27 | 所属知识网络: [[knowledge-map]] | 相关: [[AI-Agent]] | 本周期刊精选

## 简介

**Codebase Memory MCP** 是一个高性能的 MCP（Model Context Protocol）服务器，将代码库索引为持久化的知识图谱——函数、类、调用链、HTTP 路由、跨服务链接——供 AI 编码 Agent 查询。相比逐文件阅读，减少 120× 的 token 消耗。

> **一句话**: 给 Agent 一个结构化的代码「大脑」，不用每次翻文件。

## 核心指标

| 指标 | 数值 |
|:---:|:----:|
| 支持语言 | **158** 种（tree-sitter 语法） |
| 索引速度 | 平均仓库**秒级**，Linux 内核 (28M LOC) **3 分钟** |
| 查询延迟 | **<1ms** |
| Token 节省 | 约 **120×**（5 个结构查询 ~3.4K tokens vs ~412K） |
| 架构 | **纯 C** 静态编译，零依赖 |
| 形态 | 单个二进制文件，无 Docker / 无运行时 / 无 API Key |
| 平台 | macOS / Linux / Windows |

## 技术架构

### 双层解析

```
┌─────────────────────────────────────┐
│  Layer 1: Tree-sitter 语法解析       │ ← 158 种语言，快速语法分析
│  提取: definitions, calls, imports   │
├─────────────────────────────────────┤
│  Layer 2: Hybrid LSP 语义解析        │ ← 类型感知，10 种语言深度支持
│  Python/TS/JS/Go/C#/C/C++/Java/...  │
│  精炼: CALLS, USAGE, RESOLVED_CALLS  │
└─────────────────────────────────────┘
```

### 知识图谱构建

```
源代码 → Tree-sitter AST → 多阶段并行提取
    ↓
调用图遍历 + 6 策略函数解析
    ↓
Louvain 社区检测（发现模块边界）
    ↓
单 SQLite 文件存储（LZ4 压缩）
    ↓
15 个 MCP 工具暴露给 Agent
```

### 15 个 MCP 工具

| 类别 | 工具 | 功能 |
|:---:|:----|------|
| **查询** | `search_function`, `search_class` | 按名称搜索定义 |
| **关系** | `get_call_path`, `get_callers`, `get_callees` | 调用链追踪 |
| **分析** | `get_hubs`, `get_communities` | 关键模块发现 |
| **影响** | `impact_analysis` | 修改影响范围评估 |
| **跨服务** | `resolve_cross_service_calls` | 跨服务引用解析 |

## 核心创新点

### 1. 6 策略调用解析

| 策略 | 说明 | 优先级 |
|:---:|:----|:-----:|
| 精确名匹配 | 同文件直接引用 | 最高 |
| 导入图追踪 | 跨文件 import 链路 | ↑ |
| 类层级推断 | 方法继承链 | |
| 接口实现 | interface → impl 追踪 | |
| 类型流分析 | 赋值/返回值类型推导 | |
| 启发式回退 | 命名约定 + 上下文猜测 | 最低 |

### 2. 社区检测

通过 Louvain 算法自动发现代码中的模块边界——不需要配置文件，不需要人工标注。结果用于：

- **影响分析**: 修改 A 会影响到同社区的 B、C
- **hub 检测**: 找出被最多模块依赖的核心函数
- **跨服务边界**: 识别微服务之间的接口

### 3. 导出/共享协议

```yaml
codebase-memory.yaml:
  version: 1
  language: python
  files: 847
  total_loc: 125,432
  generated_at: '2026-07-27T10:00:00Z'
  compressed_size: 4.2 MB
```

支持团队共享图谱快照，无需每个人都跑一遍索引。

## 竞品对比

| 维度 | Codebase Memory MCP | Graphify | indexer-mcp |
|:---:|:---:|:---:|:---:|
| 语言支持 | **158 种** | 主流 10+ | 主流 |
| 查询速度 | **<1ms** | 秒级 | 秒级 |
| Token 节省 | **120×** | ~10× | ~5× |
| 部署 | 单二进制 | Node.js | Python |
| 依赖 | 零 | Node.js | Python + 第三方 |
| 语义解析 | ✅ Hybrid LSP | ❌ 纯语法 | ❌ |
| 社区检测 | ✅ Louvain | ❌ | ❌ |
| 跨服务解析 | ✅ | ❌ | ❌ |
| 导出共享 | ✅ | ✅ | ❌ |

## 💎 可借鉴点

### 1. RAM-first 索引管线

不是文件逐个读 → 写入 → 释放，而是内存中完成全部解析 → LZ4 压缩 → 批量写入 SQLite。Linux 内核 28M LOC 能 3 分钟搞定，核心就在于 **RAM-first + 并行 worker 池**。

### 2. 渐进式精度设计

```
纯语法 (158种) → 类型解析 (10种) → 文本启发式回退
   秒级         分钟级           零成本兜底
```

**永远有答案**——类型解析失效时不崩溃，回退到文本匹配。这种 graceful degradation 值得在 Skill 设计中借鉴。

### 3. 混合 LSP 嵌入式

它不是起一个 Language Server 进程，而是把 LSP 的类型解析算法重写为 **C 内联函数**，直接编译进二进制。零进程开销、零配置。

> 对我们 AI Agent 的启发：**需要外部工具时优先考虑嵌入式实现**，而不是依赖外部进程。

### 4. 导出协议统一团队认知

`codebase-memory.yaml` 让整个团队的 Agent 共享同一个代码图谱，解决了「每个 Agent 各扫一遍」的浪费。类似我们的 [[grok-build]] 如果支持 MCP，可以直接用上。

## 安装验证

```bash
# 下载安装
curl -fsSL https://deusdata.github.io/codebase-memory-mcp/install.sh | bash

# 验证
cbm --version

# 启动 MCP 服务器
cbm serve --project-dir /path/to/repo
```

## 总结

| 维度 | 评价 |
|:---:|:------|
| 对我当前工作流 | ⭐⭐⭐⭐⭐ — 我本身就是 Agent，如果能接入 MCP 减少文件读取，token 效率将大幅提升 |
| 技术含金量 | ⭐⭐⭐⭐⭐ — 纯 C 实现 + 6 策略解析 + Louvain 社区检测，工业级水准 |
| 值得安装 | ✅ 已安装 Obsidian MCP，后续可尝试集成到工作流 |
| 趋势判断 | MCP 生态正在爆发——从记忆、搜索、设计到代码索引，MCP 正成为 Agent 的「操作系统层」 |
