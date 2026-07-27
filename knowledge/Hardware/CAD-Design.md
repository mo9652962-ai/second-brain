---
tags: [CAD, 3d-modeling, engineering, 2026-trends]
domain: cad-design
cross-domain: [ai-agent, vibe-coding]
related: ["knowledge/AI-Agent", "knowledge/Vibe-Coding"]
created: 2026-07-21
updated: 2026-07-21
status: adopted
---

# CAD 设计与 3D 建模知识库

## 现有 Skill 生态

调研发现 ClawHub 上已有 **7 个 CAD 相关 Skills**：

| Skill | 作者 | 方式 | 特点 |
|-------|------|------|------|
| **cad-agent** | @clawd-maf | Docker + build123d + VTK | 容器化渲染，HTTP API，视觉反馈 |
| **agentcad** | @jdilla1277 | CLI + build123d/CadQuery | STEP/STL/GLB 导出，版本追踪 |
| **cad** | @bytesagain-lab | 纯参考文档 | 零依赖，纯文档输出 |
| **build123d CAD** | @rawwerks (MCP) | build123d Python | 齿轮库、螺纹、紧固件 |
| **text-to-cad** | @earthtojake | Agent Skill 集合 | 7.6K GitHub Stars |
| **blender-render** | @lzyling | Blender | STL/OBJ 渲染 |
| **cli-anything** | @ntaffffff | CLI 通用包装 | 可控制 Blender/GIMP 等 |

## 自建 Skill：cad-design-master

已整合以上全部知识，创建了全新的 `cad-design-master` skill，包含：

- 🔧 **build123d 编程式 CAD** — 完整的 Python API 速查 + 4 个实战食谱
- 📐 **传统 CAD 6 步工作流** — Sketch→Feature→Detail→Assembly→Drawing→Export
- 🎯 **软件选型决策树** — 按需求推荐最合适的 CAD 软件
- 🖨️ **3D 打印准备清单** — 壁厚/悬垂/桥接/水密性检查
- 📚 **20 周自学课程大纲** — 从入门到制造的全路径
- 🤝 **与现有 Skills 协同表** — 如何串联 cad-agent/agentcad/图片生成
- 🔮 **2026 前沿趋势** — Text-to-CAD、生成式设计、VR/AR、数字孪生

## 核心技术栈

### AI-Native CAD 管线
```
自然语言描述 → build123d Python 代码 → OpenCASCADE 几何内核
                                         ├→ STEP (制造交换)
                                         ├→ STL (3D 打印)
                                         ├→ GLB (Web 展示)
                                         └→ VTK 渲染 (视觉反馈)
```

### 参数化建模核心概念

- **约束优于尺寸** — 先定义几何关系，再定义具体数值
- **设计意图驱动** — 参数名反映设计逻辑而非几何描述
- **B-Rep 优于 Mesh** — STEP (精确几何) > STL (三角形近似)
- **特征顺序重要** — 圆角/倒角永远放在特征树的最后

## 软件生态矩阵

| 软件 | 范式 | 价格 | 适合 |
|------|------|------|------|
| Fusion 360 | 参数化+直接 | 个人免费 | 3D打印、创客 |
| SolidWorks | 参数化 | $48-2820/年 | 机械工程 |
| FreeCAD | 参数化 | 免费开源 | 预算有限 |
| AutoCAD | 2D/3D | $2030/年 | 建筑施工图 |
| Onshape | 参数化(SaaS) | 免费 | 云协作 |
| Rhino | NURBS | $995 | 工业设计 |
| build123d | 编程式(Python) | 免费开源 | AI 驱动设计 |
| OpenSCAD | 编程式(DSL) | 免费开源 | 程序员友好 |

## 2026 年 CAD 趋势

1. **AI Text-to-CAD** — LLM 直接生成 3D 模型 (build123d/CadQuery 驱动)
2. **MIT VideoCAD** — AI 观看 CAD 操作视频学习建模，41K+ 数据集
3. **生成式设计** — 拓扑优化 + AI 自动迭代
4. **云原生 CAD** — Onshape 多人实时协作
5. **VR/AR 设计** — 在 3D 空间中直接建模
6. **数字孪生** — CAD→仿真→IoT 数据闭环

---

## 🔗 知识关联

- **[[AI-Agent]]** — k 的 CAD Skills 家族（cad-design-master 已加入）
- **[[AI-Workflow]]** — CAD Pipeline 可与图片生成/搜索 Skills 串联
- **[[Vibe-Coding]]** — build123d Python 环境、Docker 容器
- **[[HOME]]** — 返回知识中枢
---
> 关联: [[Programming]] · [[AI-Workflow]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]
