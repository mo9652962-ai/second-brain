---
aliases:
  - 2026-11-07-ppt-layered-material
tags: [knowledge-card, ppt, design, deliverable, layering]
created: 2026-11-07
updated: 2026-11-08
source: "11-07 22:22–23:14 答辩/申报 PPT 两版成品（luxe / navy），2026-11-08 逐页读 slide XML 统计"
status: fresh
---

# 🃏 知识卡片 · 答辩 PPT 的「分层材质」：三层就够，别加第四层

> **一句话**：让 PPT 看起来「有材质」的不是图片，是**每页固定三层**——底色渐变层、卡片层（带外阴影）、内容层。同一套版式换材质，页数与形状几乎不变，观感差一个档次。

---

## 一、实测对比（观察）

同一份内容做了两版，逐页解析 `ppt/slides/slideN.xml` 的形状与填充节点：

| 指标 | luxe（分层材质） | navy（平涂） |
|:--|--:|--:|
| 页数 | 15 | 15 |
| 形状总数 | 567 | 554 |
| `gradFill`（渐变填充） | **50** | **0** |
| `outerShdw`（外阴影） | **145** | **0** |
| `effectLst`（效果容器） | 174 | 0 |
| `p:pic`（位图） | 0 | 0 |
| `a:tbl`（表格） | 0 | 0 |

两条硬事实：

1. **两版都零位图零表格**——观感差异全部来自矢量层（渐变 + 阴影），不是「找了张好看的背景图」。
2. luxe 每页 `gradFill` 恒定 = 3（封面 6 个），`outerShdw` 每页 4–22 个——**渐变是固定层数，阴影跟卡片数量走**。

## 二、三层结构（可复用的做法）

```
第 1 层  底色层：2–3 段线性/径向渐变（深底 → 略亮的同色系），铺满整页
         · 不透明度差异 3%–8%，够看出「有光」但不抢内容
         · 每页层数固定，换页不换结构
第 2 层  卡片层：圆角矩形 + 外阴影（outerShdw：模糊 10–20pt、距离 2–4pt、
         方向 90°、透明度 60%–75%）
         · 阴影只给「承载信息」的卡片，不给装饰线
         · 一页卡片数控制在 3–6 个；超过就拆页
第 3 层  内容层：文字 / 图标 / 数据标签
         · 字号阶梯 3 档（标题 / 小标题 / 正文），正文不小于 14pt（投屏可读）
```

判据：**如果一页的 `outerShdw` 数量 > 卡片数**，说明阴影漏到了装饰元素上，观感会「脏」。

## 三、为什么答辩场景选分层材质（推断）

- 评审现场是投影/大屏，纯平涂在同色系背景上会「糊成一块」，渐变提供边界感；
- 阴影是廉价的深度线索：不需要 3D、不需要图片，一眼就有「卡片浮在底上」的层次；
- 但分层材质有上限：三层以上（再加纹理、再加发光）在低亮度投影仪上会变成噪点——本机两版都没有 `glow` 节点，是刻意不加。

## 四、判据命令（复核用，不依赖 python-pptx）

```bash
# 用法: python - <某个.pptx> <<'PY'
python - proposal_luxe.pptx <<'PY'
import re, sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
for n in sorted([x for x in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', x)],
                key=lambda s: int(re.search(r'(\d+)', s.split('/')[-1]).group(1))):
    x = z.read(n).decode('utf-8', 'ignore')
    print(n, 'grad=', x.count('<a:gradFill'), 'shadow=', x.count('<a:outerShdw'),
          'pic=', x.count('<p:pic>'), 'tbl=', x.count('<a:tbl>'))
PY
```

## 五、未知

- 生成脚本（约 40KB）未找到，无法确认渐变的具体色标与角度参数——只有成品可反推；
- 两版在真实投影仪上的差异未实测（只在 PNG 预览上比对）。

---

> 🔗 相关：[[2026-11-07-cron-monitoring-three-fakes|监控的三张假脸]]（同一套「别拿表面信号当结论」的判据思路）· [[knowledge-map]]
