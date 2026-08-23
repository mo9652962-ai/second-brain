---
aliases:
  - code-review-graph-vs-codebase-memory
tags:
  - research
  - mcp
  - code-intelligence
  - decision
created: 2026-08-05
status: adopted
domain: dev
---

# code-review-graph vs codebase-memory-mcp 决策（2026-08-05）

## 结论

**选择 code-review-graph（28.5k★）**，替代 codebase-memory-mcp 定位。

## 对比

| 维度 | code-review-graph | codebase-memory-mcp |
|:-----|:-----------------|:-------------------|
| Stars | 28.5k | 小量级 |
| 核心 | tree-sitter 结构图 + 增量更新 | 代码知识图谱查询 |
| Token 节省 | **71x**（flask 143,594 → 2,196 tokens）| 无基准数据 |
| 增量更新 | ✅ 增量跟踪变更 | 需重建 |
| 语言 | Python 3.10+ | — |
| 维护活跃度 | v2.3.7 活跃 | 已停更（pip show 无输出）|
| 查询 | callers_of/callees_of/imports_of/impact 等 27 命令 | 图谱查询 |
| 额外能力 | dead-code 检测、architecture 社区发现、impact 分析、wiki | — |

## 落地验证（Sims4-Multiplayer-Dev 实测）

```
code-review-graph build:
  1127 files → 17754 nodes / 97207 edges / FTS 17510 rows
  architecture: 11 社区（rich-parse 等）— 与 SimSync 12 模块设计吻合
  query callers_of RoomServer: 19 候选命中，可消歧
```

## 使用方式

```bash
code-review-graph build            # 建图（增量更新用 update）
code-review-graph query callers_of <class>  # 查调用者
code-review-graph impact <file>    # 变更影响分析
code-review-graph architecture     # 架构社区发现
code-review-graph dead-code        # 死代码检测
code-review-graph mcp serve        # MCP 服务（Hermes 可接）
```

## 落地后续

- [x] pip install code-review-graph
- [x] init --repo（已注册 Claude/OpenCode/Gemini hooks）
- [x] build 建图（1127 files 全量）
- [x] Hermes 接入 MCP（`code-review-graph mcp serve` → config.yaml mcp_servers）✅ 2026-08-05 已配置（config.yaml mcp_servers.code-review-graph: uvx code-review-graph serve）
- [x] ~~与 SimSync 开发流程集成（review 前跑 impact 分析）~~ 📖 条件触发参考（SimSync 开发窗口时）

---

*决策完成：2026-08-05 · 已替代 codebase-memory-mcp 定位*

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
