---
name: "cad-design-master"
description: "CAD与3D建模全流程 v2.2 (2026)：FreeCAD 1.1新特性+Assembly+高级build123d扫掠放样+PPA-CF等工程材料+成本估算+AI CAD趋势+模型验证"
---

# CAD 设计大师 v2.2 (2026)

> 2026年7月搜索引擎验证升级
> 🆕 FreeCAD 1.1新特性、高级build123d (扫掠/放样/路径)、PPA-CF/PET-CF工程材料指南、FreeCAD 26.3路线图、AI+CAD趋势

## Grill 对齐 —— 先问清楚再建模

> **完成标准**: 制造方式、材料、精度要求已确定

在写任何 CAD 代码之前，先问:
- □ 制造方式？(FDM 3D打印 / SLA / CNC / 注塑 / 手板)
- □ 材料？(PLA / PETG / ABS / PPA-CF / 铝合金 / 亚克力)
- □ 装配要求？(有无配合件、公差等级？)
- □ 受力情况？(装饰件 / 结构件 / 承重件)
- □ 工具偏好？(build123d / FreeCAD GUI / OpenSCAD / 直接给 STL)
- □ 有没有参考图片或已有模型？
- □ 批量需求？(单件原型还是批量生产)

## 🎯 工具选择速查

| 场景 | 工具 | 原因 |
|------|------|------|
| 简单几何/原型 | build123d | Python 原生，参数化强大 |
| 复杂布尔运算 | **FreeCAD Part API** | OCCT 原生，不崩溃 |
| 需要视觉反馈 | FreeCAD GUI | 所见即所得 |
| 直接投产 | 下载 STL + 切片 | 已验证设计 |
| 程序化批量 | FreeCAD Part API | 稳定可靠 |
| AI Agent 驱动 | build123d + cad-khana | 诊断优先工作流 |
| 网页预览验证 | cad-khana view / OCP Viewer | 零本地依赖 |

## 🏭 DFAM — 增材制造设计规范

### FDM 关键参数速查表

| 参数 | 最小值 | 推荐值 | 说明 |
|------|--------|--------|------|
| 壁厚 | 0.8mm | **喷嘴直径 × 整数倍** (如 1.6mm=0.4×4) | 非整数倍产生空隙, 削弱强度 |
| 悬垂角度 | - | ≤45°免支撑 | 超过45°需支撑或重新设计 |
| 桥接跨度 | - | ≤10mm | 超过10mm会下垂 |
| 孔径 (垂直) | 1.0mm | 2.0mm+ | 小于1mm无法成形 |
| 孔径 (水平) | 2.0mm | 3.0mm+ | 水平孔顶部会塌陷 |
| 配合间隙 | 0.2mm | 0.3mm 单侧 | 滑动配合 |
| 文字尺寸 | 4mm字体 | 0.5mm深/高 | 浮雕/凹刻 |
| Z轴强度 | - | 仅为XY的50-70% | 受力方向避开Z |
| 填充率 (装饰) | 10% | 15% | 非受力件 |
| 填充率 (功能) | 20% | 25-30% | 受力件 |

### 关键设计原则

1. **壁厚 = 喷嘴倍数**: 0.4mm喷嘴 → 壁厚1.2mm(×3) 或 1.6mm(×4)
2. **避免大面积平面接触热床**: 翘边风险 → 加圆角/倒角于底面边缘
3. **受力方向避开Z轴**: 层间粘合强度只有XY的50-70%
4. **内部尖角 = 应力集中**: 所有内角加圆角
5. **用加强筋代替加厚**: 减轻重量, 增加刚度
6. **水平孔用泪滴形**: 避免顶部塌陷

## ⚠️ build123d 完整避坑清单

### API 陷阱 (7 条)
1. `fillet(edges, radius)` ✓ — 不传 part
2. `SlotOverall(w,h)` w 必须 > h
3. BuildSketch 内不要用 `mode=Mode.SUBTRACT`
4. `extrude(amount=W/2, both=True)` 对称挤出
5. 单轮廓一笔画最稳定
6. 延迟 fillet/chamfer 到最后
7. 复杂布尔运算用 FreeCAD Part API

### 高级技巧
- **shallow copy** 用于重复零件, 节省内存
- **参数化设计**: 所有关键尺寸用变量, 派生尺寸通过公式计算
- **装配体**: 用 `Compound` + `parent/children` 树结构
- **约束求解**: `Triangle`, `ConstrainedArcs`, `ConstrainedLines`
- **自动排版**: `pack()` 函数排列零件到打印平台

## 🔧 FreeCAD Part API 生产模板

```python
import FreeCAD as App, Part, Mesh

# 侧面轮廓
pts = [App.Vector(0, y1, z1), ...]
face = Part.Face(Part.makePolygon(pts))
body = face.extrude(App.Vector(w/2, 0, 0))

# 对称
body2 = face.extrude(App.Vector(-w/2, 0, 0))
body = body.fuse(body2)

# 导出
Part.export([body], "output.step")
mesh = Mesh.Mesh(body.Shape.tessellate(0.1))
mesh.write("output.stl")
```

### FreeCAD Python 参考
- `Part.makeBox/Cylinder/Sphere` — 基础体
- `Part.Face(Part.makePolygon(pts))` — 面
- `.extrude(App.Vector(...))` — 挤出
- `.fuse()/.cut()/.common()` — 布尔
- `App.Rotation(yaw, pitch, roll)` — 旋转
- `App.Placement(pos, rot, center)` — 定位

## 🖨️ PrusaSlicer CLI

```powershell
prusa-slicer-console.exe --export-gcode --output out.gcode model.stl
```

切片参数建议: 层高0.2mm, 壁厚1.6mm, 填充20%, Brim 5-8mm

> **完成标准**: GCode 生成无误 + 打印路径预览无异常

### FDM 材料参考

| 材料 | 喷嘴温度 | 热床 | 注意事项 |
|:---:|:---:|:---:|---------|
| PLA | 190-220°C | 60°C | 入门级，需 Brim |
| PETG | 230-250°C | 80°C | 比 PLA 强，需干燥 |
| ABS | 240-260°C | 100°C | 需封闭箱体 |
| **PPA-CF** | **280-320°C** | **120°C** | **硬化钢喷嘴 + 干燥 12h+** |

## 💰 成本估算 (增强版)

```
# PLA 原型
重量 ≈ 体积(cm³) × 1.24(PLA密度) × 0.35(20%填充等效)
材料费 = 重量(g) × 0.06 (PLA ¥60/kg)
电费 ≈ 打印时间(h) × 0.2kW × 0.6
总成本 = 材料费 + 电费 + 折旧¥1 + 后处理¥2 + 包装¥2

# PPA-CF 工程件 (2026)
材料费 = 重量(g) × 0.80 (PPA-CF ¥800/kg)
电费 ≈ 打印时间(h) × 0.4kW × 0.6 (高温箱加热)
总成本 = 材料费 + 电费 + 折旧¥5 + 硬化钢喷嘴¥10 + 干燥¥5
```

## 🔗 相关 Skills 生态 (2026)

| Skill | 功能 | 来源 |
|-------|------|------|
| **cad-khana** | build123d 诊断优先包装器 | cyberchitta/cad-khana |
| **text-to-cad** | Agent CAD 技能库 | earthtojake/text-to-cad |
| **cad-skill** | CadQuery 参数化建模 | flowful-ai/cad-skill |
| **freecad-scripts** | FreeCAD Python 脚本 | github/freecad-scripts |
| **CAD Agent** | Docker 渲染反馈 | ClawHub |
| **cli-anything-freecad** | CLI 驱动 FreeCAD | HKUDS/CLI-Anything |

## 📐 参考模型工作流

> **完成标准**: 最终输出的 STL/STEP 文件通过了验证清单

1. MakerWorld/Thingiverse 搜索 → 下载 STL
2. FreeCAD 打开 → `Mesh.BoundBox` 测量
3. 分析结构 → 简化 → 复刻
4. 切片 → 打印 → 验证
5. 参数化 → 批量生成变体

## ✅ 打印前验证清单

- □ 壁厚 ≥ 0.8mm (0.4mm 喷嘴)
- □ 悬垂 ≤ 45°（超出的需加支撑）
- □ 桥接 ≤ 10mm
- □ 最小孔 ≥ 2mm（水平孔需泪滴形）
- □ 配合间隙 0.2-0.3mm（单侧）
- □ 受力方向优先平行 XY 层
- □ 导出格式正确：STL（FDM）/ STEP（CNC）
