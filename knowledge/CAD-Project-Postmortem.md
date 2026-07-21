---
domain: CAD-Design
cross-domain: ["programming", "ai-agent"]
related: [[CAD-Design]], [[Programming]], [[Vibe-Coding]]
tags: [case-study, postmortem, cad, build123d, freecad, 3d-printing, lessons-learned]
created: 2026-07-21
---

# 课题一：AI+CAD 全流程 — 实战复盘

> 一天内从零到投产：v1 → v8 → iStand 上线
> 记录了所有踩坑、技术债务、修正方案

## 📊 项目时间线

```
18:00  安装 6 款 CAD 软件 + 7 个 Python 库
20:16  课题一启动: parts_library.py + cad_agent.py
20:30  5 个测试用例全部通过 (螺栓/螺母/齿轮/法兰/支架)
20:37  手机支架 v1 初版 (AI 实时代码生成)
20:44  v2 Pro (夹臂+蜂窝+磁环)
21:19  v3 Transform (铰链+MagSafe, 2.2MB)
21:26  v4 Production (实用极简, 45g, ¥2.7)
21:35  生产链: 切片 → G-code → 成本分析
21:40  参照碳素钢支架设计 v5-v8
22:36  下载 iStand 参考模型
22:45  最终方案: iStand 13 零件装配体投产
```

## 🔴 问题清单

### 1. build123d API 陷阱 (7 个)

| # | 问题 | 症状 | 修正 |
|---|------|------|------|
| 1 | `fillet(part, edges, radius)` | `TypeError: got multiple values for 'radius'` | 正确: `fillet(edges, radius)`，不传 part |
| 2 | `chamfer(part, edges, length)` | `TypeError: got multiple values for 'length'` | 正确: `chamfer(edges, length)` |
| 3 | `SlotOverall(w, h)` | `ValueError: width > height required` | w 必须 > h |
| 4 | `Circle(6, mode=Mode.SUBTRACT)` in BuildSketch | `RuntimeError: Nothing to subtract from` | BuildSketch 内不加 SUBTRACT，在 extrude 阶段减 |
| 5 | `RegularPolygon(hex_r, 6, mode=Mode.SUBTRACT)` | 同上 | 同上 |
| 6 | 复杂的布尔减法 | `0xC0000005 访问冲突` → 进程崩溃 | 简化几何或换 FreeCAD Part API |
| 7 | `JernArc` | 需要 4 个参数 (start, end, radius, arc_size) | 文档不清晰 |

**根因**: build123d 的 OCCT 内核对复杂布尔运算容忍度低。官方文档也承认: *"not all parts can be successfully constructed by the underlying CAD core"*

### 2. 几何问题 (4 个)

| # | 问题 | 症状 | 修正 |
|---|------|------|------|
| 8 | `extrude(amount=W)` 单向挤出 | 模型不对称，偏向 +X 侧 | 改为 `extrude(amount=W/2, both=True)` |
| 9 | 多平面 sketch 不融合 | 不同 Plane 上的零件彼此悬空 | 用单轮廓一笔画 + 一次性挤出 |
| 10 | 背板顶点飞到基座外 | 三角函数计算错误，坐标偏 21mm | 验证几何：顶点 Y 必须在 `[-D/2, D/2]` 内 |
| 11 | 面选择失败 | `Planes can only be created from planar faces` | 倾斜挤出后面不是平面，用 Z 坐标过滤 |

### 3. FreeCAD API 问题 (3 个)

| # | 问题 | 症状 | 修正 |
|---|------|------|------|
| 12 | `Mesh.export([body])` | `None of the objects can be exported to a mesh file` | 先 `body.Shape.tessellate()` 再写 |
| 13 | freecadcmd 中文路径 | `Application unexpectedly terminated` | 用纯英文文件名 |
| 14 | freecadcmd 多文件参数 | crash on large scripts | 写 .py 文件再传给 freecadcmd |

### 4. 工程流程问题 (4 个)

| # | 问题 | 影响 |
|---|------|------|
| 15 | **无视觉反馈** | 每次改完跑 2 分钟才能看结果，无法迭代调比例 |
| 16 | **build123d 不稳定** | 同样代码有时成功有时崩溃 |
| 17 | **设计漂移** | v1→v8 越改越不像原设计，失去参照物 |
| 18 | **MakerWorld/Thingiverse 禁止程序下载** | 403 Forbidden，无法自动获取参考模型 |

## 🟢 解决方案与最佳实践

### build123d 安全模式

1. **单轮廓 + 一次性挤出** (最稳定)
```python
with BuildSketch(Plane.XZ) as sk:
    with BuildLine() as ln:
        Polyline(p1, p2, ..., p1)  # 闭合
    make_face()
extrude(amount=W/2, both=True)  # 对称挤出
```

2. **2D 先于 3D** (官方推荐)
   先完成 2D sketch 的所有操作(fillet/chamfer)，再 extrude

3. **延迟 Fillet/Chamfer**
   在最后一步做，避免中间步骤几何变复杂

4. **减法在 extrude 阶段做**
```python
# ✓ 正确
with BuildSketch(face) as sk:
    Circle(5)  # 普通 ADD
extrude(amount=-3, mode=Mode.SUBTRACT)  # 在这儿减

# ✗ 错误
Circle(5, mode=Mode.SUBTRACT)  # BuildSketch 内不能减
```

### FreeCAD Part API 生产模式

```python
# 比 build123d 更稳定，适合复杂布尔运算
import FreeCAD as App, Part, Mesh

# 创建几何
face = Part.Face(Part.makePolygon(pts))
body = face.extrude(App.Vector(w/2, 0, 0))

# 布尔运算 (不会崩溃)
body = body.fuse(other_part)
body = body.cut(hole)

# 导出 STL (需要转换)
mesh = Mesh.Mesh(body.Shape.tessellate(0.1))
mesh.write("output.stl")
```

### 最佳工作流

```
1. 下载参考模型 (MakerWorld/Thingiverse)
   ↓
2. FreeCAD 打开 → 测量尺寸 → 分析结构
   ↓
3. FreeCAD Part API 脚本建模 (不依赖 build123d)
   ↓
4. freecadcmd 运行 → STEP + STL 导出
   ↓
5. PrusaSlicer CLI 切片 → G-code
   ↓
6. 打印验证
```

## 🔧 Skill 升级

### cad-design-master → v2.0

基于今日实战升级内容:
1. 新增 FreeCAD Part API 代码模板 (替代不稳定的 build123d)
2. 新增 build123d 避坑指南 (7 个已知陷阱)
3. 新增 PrusaSlicer CLI 切片模板
4. 新增参考模型分析方法
5. 新增生产链成本估算公式

## 💡 核心经验

1. **build123d 适合简单几何**，复杂形状用 FreeCAD Part API 或直接下载 STL
2. **AI 生成 CAD 的致命缺陷**: 无法视觉迭代 → 必须有人工参考模型
3. **"先有后优"**: v4 的极简实用路线比 v3 的复杂路线更靠谱
4. **社区验证 > 自己瞎造**: iStand 13 零件设计经过数百人下载验证
5. **成本控制**: PLA ¥60/kg, 20%填充, 1.6mm壁厚 → 打印成本 ¥3-5

## 📁 最终交付物

```
📁 CAD-手机支架/iStand/     ← 13 个零件, 卡扣装配
📁 CAD-手机支架/             ← v4/v7/v8 源码 + STEP/STL
📁 CAD-可打印Gcode/         ← 即打 G-code
📁 CAD-零件库/               ← 齿轮/法兰/螺栓/螺母/支架
📁 CAD-装配体/               ← M8 螺栓+螺母+垫圈
📁 CAD-存档/                 ← v1-v3 归档
```

---

_最后更新: 2026-07-21 | 累计迭代: v1-v8 + iStand | 工期: ~5 小时_