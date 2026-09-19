# PPT 固定模板库 · Template 01 国风红金大师模板

> 定位：**首个固定标准模板（Fixed Template）**——国家奖学金 / 优秀毕业生 / 硕士论文等高规格答辩的一键初版即优秀方案。
> 设计核心：**超框大折扇开场（Morph 机械光圈）+ 红金设计系统 + S型流线毛玻璃负空间镂空致谢（Q&A 长驻页）**

---

## 一、模板资产清单

| 资产 | 路径 | 用途 |
|:---|:---|:---|
| 固定模板成品 | `templates/PPT-Template-01-Masterpiece.pptx` | 直接套用 / 交付客户初版 |
| 中文名成品 | `knowledge/Productivity/templates/PPT-Template-01-国风红金大折扇与镂空致谢.pptx` | 中文归档副本 |
| 生成器源码 | `knowledge/Productivity/scripts/build_template_01_masterpiece.py` | 参数化重生成（换人/换数据） |
| 9页渲染预览图 | `knowledge/Productivity/images/template_01_slide_{1..9}.png` | 快速预览 / 发客户看稿 |

---

## 二、9 页结构（固定骨架）

| 页码 | 章节 | 视觉工程 | 实测评分 |
|:---:|:---|:---|:---:|
| 1 | 开场·折扇合拢态 | 超框大折扇起始态（右下起轴，扇叶全合拢） | 9.8（合拢→展开联动） |
| 2 | 开场·折扇绽放终态 | 6 扇叶 25° 超框展开 + Morph 平滑补间 + 汇报人信息卡 | 9.8 |
| 3 | 目录·五篇章 | 5 张圆角卡片 + 金色编号 + 高亮当前章节 | 8.5 |
| 4 | 思想引领 | 3 卡结构（顶金条 + 金标题 + 深红正文） | 9.0 |
| 5 | 学业成绩 | 左侧 3 张深红金大数字指标卡 + 右侧原生无网格柱状图 | 9.5 |
| 6 | 科研探索 | STAR 项目总览 + 5 步技术路线流程图（箭头连接） | 9.0 |
| 7 | 获奖荣誉 | 3 卡勋章版式（★ 圆形徽章 + 荣誉层级） | 9.0 |
| 8 | 实践影像 | 3×2 金边虚线照片墙栅格 + 图注规范 | 8.5 |
| 9 | 致谢·Q&A 长驻 | S 型贝塞尔毛玻璃 + 负空间 Q&A 透光镂空 + 红金光晕 | 9.5 |

---

## 三、核心设计 Token（换色/换字体改这里）

```python
DEEP_RED   = RGBColor(0x7A, 0x10, 0x22)  # 深酒红（主色）
BRIGHT_RED = RGBColor(0xB7, 0x1C, 0x2C)  # 亮红（渐变端点）
GOLD       = RGBColor(0xD4, 0xAF, 0x37)  # 金（强调色）
PALE_GOLD  = RGBColor(0xF0, 0xDF, 0xA8)  # 浅金（辅助文字）
CREAM      = RGBColor(0xFB, 0xF4, 0xEA)  # 米白（内容页底）
DARK_TEXT  = RGBColor(0x2A, 0x24, 0x1E)  # 深墨（正文）
LIGHT_BOX  = RGBColor(0xF7, 0xEF, 0xE2)  # 浅米（卡片底）
```

---

## 四、两大视觉工程复用清单

### 1. 超框大折扇开场（Slide 1→2）
- 函数：`create_scenic_background()` + `render_masterpiece_state(is_opened=)`
- 关键参数：
  - 扇轴：右下 `(0.72W, 0.82H)`（超框构图，扇叶远超画布）
  - 半径：`0.88H`（大画幅压场）
  - 扇叶：6 片 × 25° 扇弧，展开角 `[150,180,210,240,270,300]`
  - 透光视差：扇叶外 170/255 白色薄纱雾层 + 扇叶内透出原画 + 104% 柔和阴影 + 2px 白边高光
- Morph 注入：`add_morph_transition(slide)` → `<p:morph option="byObject"/>`

### 2. S 型流线毛玻璃镂空致谢（Slide 9）
- 函数：`generate_curved_cutout_mask()`（3840×2160 高分辨率渲染）
- 关键参数：
  - 贝塞尔曲线：`p0=(1620,0) p1=(1320,680) p2=(1950,1420) p3=(1740,2160)`
  - 面板：米白 55/255 透明度（真实毛玻璃半透感）
  - 镂空文字：Q & A（Arial 粗体 400pt），文字区域 alpha 归零 → 透出底层红金光晕
  - 阴影：25px 偏移 + 36px 高斯模糊（面板立体悬浮感）

---

## 五、使用方式（SOP）

1. **接单 / 自用**：复制 `templates/PPT-Template-01-Masterpiece.pptx` 作为初版底稿
2. **换人换数据**：运行 `python scripts/build_template_01_masterpiece.py`，直接改源码中的：
   - 汇报人卡片字符串、GPA 数据、图表系列、获奖名称、照片墙图注
3. **交付前验证**：LibreOffice 渲染 PDF → PyMuPDF 出图 → 视觉评审 ≥9.0 分才交付
4. **动画验收**：在 PowerPoint 2019+ / WPS 中打开，检查 Slide 1→2 平滑过渡是否流畅

---

## 六、版本记录

| 日期 | 版本 | 变更 | 验证 |
|:---|:---|:---|:---|
| 2026-09-20 | v1.0 | 首个固定模板：超框折扇开场 + 红金系统 + 镂空致谢 9 页全流程 | 12/12 ad-hoc 测试通过；LibreOffice 渲染 9/9 页；视觉评审 8.5-9.8 分 |
