---
type: graph-update
date: 2026-08-09
domain: graphify
---

# Graphify 图谱周更新 (2026-08-09, W32)

## 变更摘要

- **范围**: 599 个新/变更文件（86 code + 470 doc + 7 paper + 36 image），0 删除（上次 manifest 缺失导致全量重列）
- **新图谱规模**: 1925 节点 / 3487 边 / 139 社区（净化后，已剔除 .obsidian 插件噪声 4660 节点）
- **语义提取**: 30 个 chunk 全部成功 → 1593 语义节点 / 2796 边 / 55 hyperedge
- **对比上周**: 节点 1256→1925（+53%），边 2045→3487（+70%），社区 127→139

## 新增知识域关联（本周亮点）

| 社区 | 规模 | 关联说明 |
|---|---|---|
| arXiv Agent/LLM 研究周报 | 49 | 08-07 速览 + Argus/HiGram/PIMiner 等论文链 |
| 知识卡片与自进化 Agent | 47 | 零感AI/SESA/ToolMaze 卡片 → 闲鱼降AI率服务 |
| AI 图片生成与 ComfyUI 诊断 | 44 | Krea2 双缩放 root cause + outputs/diag 图片节点 |
| 8051 嵌入式开发 | 35 | STC89C52/Keil/SDCC 与 CAD 技能库同簇 |
| AI-CAD 装配自动化 Pipeline | 29 | Assembly Slicer 全链路 |
| PlanExecute 与容灾研究 | 22 | 逆练 PlanExecute + 火山容灾 |
| 浏览器自动化工具 | 22 | Browser-use/反检测最佳实践 |
| 降AI工具对比与闲鱼素材 | 34 | 笔灵/零感/森克兰特 → 上架素材包 |

## 关键枢纽节点（God Nodes）

1. **HOME 首页** — 230 边（介数 0.292，跨 20+ 社区最强桥）
2. **知识地图** — 219 边（介数 0.172）
3. **知识图谱 (MOC)** — 86 边
4. **闲鱼变现/上架体系** — 73 边
5. **MOC-Research 研究笔记** — 71 边

## 健康检查

- 构建后 graph.json: 0 悬空边 / 0 缺失端点 / 0 重复 id（verify 13/14 通过）
- 提取层诊断 252 个 dangling 边 = AST 跨文件引用指向被过滤的 .obsidian 节点，build 时自动丢弃
- 孤立节点 ~289（HEARTBEAT/模板/身份文件，符合预期）

## 产物

- `graphify-out/graph.json` — 图谱数据（2.2MB）
- `graphify-out/graph.html` — 交互可视化（1.88MB）
- `graphify-out/GRAPH_REPORT.md` — 审计报告（48KB）
- `graphify-out/manifest.json` — 增量清单（599 条目，下周增量更新可命中缓存）

## 备注

- 本次因上周 manifest.json 缺失，全部 513 个语义文件重新提取（缓存仅命中 34）；已修复 manifest 持久化，下周 --update 应只处理增量
- Token 消耗: 44.3M in / 0.9M out（30 subagent）；累计 64.5M in / 1.6M out（2 次运行）
- 30 个 chunk 全部成功（subagent 自带 ad-hoc schema 验证），无失败重试

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
