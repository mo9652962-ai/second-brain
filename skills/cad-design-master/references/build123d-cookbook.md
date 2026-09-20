# build123d 实战食谱

## 基础入门

```python
from build123d import *
from ocp_vscode import show

# 创建一个简单的零件并预览
part = Box(50, 30, 20)
show(part)  # 在 VS Code 中预览
```

## 常见零件设计

### 1. 带孔底板
```python
from build123d import *

base = Box(80, 60, 5)
holes = Pos(30, 20) * Cylinder(3, 5)
holes += Pos(-30, 20) * Cylinder(3, 5)
holes += Pos(30, -20) * Cylinder(3, 5)
holes += Pos(-30, -20) * Cylinder(3, 5)
plate = base - holes
```

### 2. L型支架
```python
from build123d import *

with BuildPart() as bracket:
    with BuildSketch(Plane.XY) as profile:
        with BuildLine() as outline:
            Polyline((0,0), (0,40), (40,40), (40,30), (10,30), (10,0))
        make_face()
    extrude(amount=5)
    # 加强筋
    with BuildSketch(Plane.YZ.offset(20)) as rib_sketch:
        Rectangle(40, 3, align=(Align.MIN, Align.CENTER))
    extrude(amount=5, both=True)
```

### 3. 轴
```python
from build123d import *

# 阶梯轴
a = Cylinder(8, 50)
b = Cylinder(12, 10).locate(Pos(0, 0, 50))
c = Cylinder(8, 30).locate(Pos(0, 0, 60))
shaft = a + b + c
# 键槽
keyway = Box(4, 3, 15).locate(Pos(12, 0, 25))
shaft -= keyway
# 倒角
shaft = chamfer(shaft.edges().group_by(Axis.Z)[0], 1)
```

### 4. 外壳/机箱
```python
from build123d import *

outer = Box(120, 80, 40)
inner = Box(116, 76, 39).locate(Pos(0, 0, 1))
enclosure = outer - inner
# 螺丝柱
for x in [-50, 50]:
    for y in [-30, 30]:
        pillar = Cylinder(4, 10).locate(Pos(x, y, 0))
        hole_feat = Cylinder(2.5, 10).locate(Pos(x, y, 5))
        enclosure += pillar - hole_feat
```

## 高级技巧

### 参数化设计
```python
from build123d import *

class Params:
    length = 100
    width = 50
    height = 30
    wall = 2.0
    hole_dia = 4.0

part = Box(Params.length, Params.width, Params.height)
```

### 镜像
```python
from build123d import *

half = Box(40, 30, 20) - Cylinder(5, 20).locate(Pos(15, 0, 0))
full = half + mirror(half, Plane.YZ)
```
