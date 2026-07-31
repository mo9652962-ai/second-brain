---
tags: [research, gis, geospatial, geolibre, open-source]
created: 2026-07-31
status: archived-reference
source: "https://geolibre.app/"
---

# GeoLibre — 云原生 GIS 平台（备查）

> 2026-07-31 存档 · 待 GIS/地理数据需求时启用

## 是什么

免费开源的轻量级云原生 GIS 平台，在浏览器/桌面/移动端/Jupyter 中运行，数据本地处理（隐私优先）。

- GitHub: [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre) · 3.4K stars · MIT
- 版本: 2.2 (stable, 2026)

## 技术栈

| 组件 | 作用 |
|------|------|
| Tauri v2 (Rust) | 桌面/Android 原生外壳，比 Electron 小数倍 |
| MapLibre GL JS | GPU 矢量地图渲染 |
| **DuckDB-WASM Spatial** | 浏览器内跑空间 SQL（120 万行 < 20ms） |
| deck.gl | 大规模数据可视化 |
| React + TypeScript | 一套代码跨 web/桌面/移动 |

## 核心能力

- **数据格式**: GeoParquet / FlatGeobuf / PMTiles / COG / Zarr / LiDAR / 3D Tiles
- **SQL 工作区**: 浏览器内 DuckDB 空间查询，无需服务器
- **处理工具**: 矢量 (Turf.js) + 栅格 (rasterio sidecar) + Whitebox 700+ 工具
- **AI 助手**: 自然语言 → 空间 SQL/符号化/地图控制
- **行星制图**: 月球/火星等天体坐标系（罕见特性）
- **嵌入**: Jupyter notebook / Colab 集成，`pip install geolibre`

## 与我们相关的点

| 场景 | 用途 |
|------|------|
| 闲鱼 GIS 数据可视化单 | 浏览器交付，无需部署服务器 |
| 地理数据展示 | PCB 项目选址/物流路径可视化 |
| Jupyter 工作流 | 嵌入现有数据分析流程 |

## 何时启用

- [ ] 接到 GIS/地图/地理数据可视化单
- [ ] 需要快速展示 GeoJSON/GeoParquet 数据
- [ ] 空间数据分析需求

## 限制（研究确认）

- 栅格像素级运算弱于 QGIS（DuckDB 是列式 OLAP）
- 高级地理处理依赖 Python sidecar（纯 Web 模式不可用）
- 插件生态初期，质量参差
- 浏览器内存上限 ~2-4GB，超大数据需降级

---

*存档 2026-07-31 · 备用工具，非立即执行*
