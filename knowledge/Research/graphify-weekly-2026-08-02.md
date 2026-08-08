---
type: graph-update
date: 2026-08-02
domain: graphify
---

# Graphify 图谱周更新 (2026-08-02, W31)

## 变更摘要

- **范围**: 372 个新/变更文件 + 34 个删除文件（自 07-23 上次构建）
- **新图谱规模**: 1256 节点 / 2045 边 / 127 社区（净化后，已剔除 .obsidian 插件噪声 4654 节点）
- **新增**: 1153 新节点 / 1941 新边（对比旧图）
- **删除**: 34 个旧平铺 knowledge/memory 文件已迁入子目录并剪枝

## 新增知识域关联（本周亮点）

| 社区 | 规模 | 关联说明 |
|---|---|---|
| Second Brain 知识库核心 | 54 | HOME 枢纽，跨 8+ 域桥接 |
| 闲鱼变现与学术服务 | 43 | 论文/PPT/降AI率接单 SOP ↔ 学术域 |
| arXiv 周报与研究域 | 26 | 07-30/07-31/08-02 三份核心贡献 |
| 知识图谱工具 (Graphify) | 17 | CHARM/KuTIE/Desktop-Delta 跨域连接 |
| GitHub 宝藏挖掘与定时任务 | 22 | 周报 → 知识吸收 → Obsidian 输出链路 |
| CloudBase 与可靠性工程 | 40 | 学习路径 8 站 + Cron 容灾 |

## 关键枢纽节点（God Nodes）

1. **HOME — 知识中枢**（介数 0.138，跨社区桥接最强）
2. **知识地图 Knowledge Map**
3. **Cross-Domain 交叉领域索引**
4. **AI Agent 知识库 (Hermes 视角)**
5. **效率域 MOC** / **学术知识域 MOC**

## 健康检查

- 悬空边 0 / 缺失端点 0 / 自环 1（可忽略）
- 289 个孤立节点（多为 HEARTBEAT/模板/身份文件，待后续连边）

## 产物

- `graphify-out/graph.json` — 图谱数据
- `graphify-out/graph.html` — 交互可视化（1.18MB）
- `graphify-out/GRAPH_REPORT.md` — 审计报告

## 备注

- 本次发现并修复：上次图谱包含大量 `.obsidian/plugins/*/main.js` 混淆代码节点（78%），已过滤，避免污染社区检测
- Token 消耗: ~20.2M in / 0.7M out（16 个提取 subagent）

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
