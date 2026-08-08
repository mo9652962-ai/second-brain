---
tags: [research, 3d, microsoft, trellis, archive]
created: 2026-07-31
status: archived-reference
source: "https://microsoft.github.io/TRELLIS.2/"
---

# TRELLIS / TRELLIS.2 — 微软 3D 生成模型（备查）

> 2026-07-31 存档 · 需 GPU，暂不部署

## 是什么

微软开源 40 亿参数 3D 生成模型，**3 秒**将单张图片转为高质量 3D 资产（完整 PBR 纹理）。

- 仓库: [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS) + [TRELLIS.2](https://microsoft.github.io/TRELLIS.2/)
- Stars: 3.1k+（TRELLIS.2 开源后）
- 协议: MIT（可商用）
- arXiv: 2512.14692

## 核心能力

| 能力 | 说明 |
|------|------|
| 图转 3D | 单张图片 → 高质量 3D 资产（3 秒 512³，17 秒 1024³，60 秒 1536³） |
| PBR 材质 | 金属/塑料/玻璃/木材/水纹等完整物理材质 |
| 复杂结构 | 头发、布料、玻璃、透明物体（瓶内物品清晰可见） |
| 导出 | GLB 格式 → 无缝对接 Unity/Unreal |
| 开放 | 本地部署 + 训练代码，可按需微调 |
| 新架构 | O-Voxel 稀疏体素 + SC-VAE 16 倍空间压缩 |

## 与我们相关的点

| 场景 | 用途 | 状态 |
|------|------|:---:|
| 3D 打印模型生成 | 图片 → 3D 打印资产（连接 OpenDuckMini 想象） | 🟢 长期 |
| 游戏/虚拟资产 | 快速生成 3D 素材 | 🟢 长期 |
| 闲鱼 3D 建模接单 | 潜在新方向 | 🟢 长期 |

## 何时启用

- [ ] 有 GPU 环境（需要 NVIDIA H100 级别才快，低端卡很慢）
- [ ] 接到 3D 建模/打印相关需求
- [ ] 结合 OpenDuckMini 项目做 3D 打印部件

## 限制

- 需要 GPU（H100 上 3 秒/张，消费级显卡慢 10-100 倍）
- 4B 参数模型，内存需求高
- 当前主要为图像输入，文生 3D 支持有限（官方建议先文生图再图生 3D）

---

*存档 2026-07-31 · 备用工具，非立即执行*

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
