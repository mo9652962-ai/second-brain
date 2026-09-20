# -*- coding: utf-8 -*-
"""生产级原生可编辑矢量折扇开场演示文稿生成器（Fan Native Master）

【修复折扇扇骨扇叶匹配与力学结构 · 真正符合物理传统折扇】
1. 彻底解决扇骨偏心漂移 Bug：
   - 传统矩形以自身几何中心为旋转轴，旋转后扇骨端点会脱离扇轴数英寸，导致扇骨漂浮乱飞；
   - 本版本改用以 (cx, cy) 为几何圆心的 MSO_SHAPE.PIE 纤细辐条（弧度 0.8°），
     几何圆心与扇轴完全同心，旋转时 100% 紧锁于扇纽 (cx, cy) 辐射而出，永不漂浮脱节！
2. 扇骨与扇叶严丝合缝匹配（中轴贯穿）：
   - 每根扇骨角度精确锁定在对应扇叶的中轴线（rot = blade_rot + blade_span * 0.5 - 0.4°）；
   - 在内圈 30% 半径空白处清晰露出竹节骨架，自然延伸并牢固贯穿扇面，完美呈现传统折扇真实构造！
3. 增加折扇左右两侧大骨（外护骨）：
   - 起始侧与收尾侧各有一根稍微加宽的竹制大骨（1.2°），给整把折扇提供坚实骨架支撑感；
4. 官方 ISO/IEC 29500 mc:AlternateContent + p159:morph 原生平滑动画：
   - Slide 1: 6 片扇叶 + 6 根小骨 + 2 根大骨完全闭合叠拢于收起角，呈现修长优雅的闭合折扇！
   - Slide 2: 扇叶与扇骨以毫厘不差的角速度同步旋转绽放，标题优雅降落，四列诗词从右向左滑入！
"""
import os, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml import parse_xml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import render_fan_3d as f3

def build_fan_native_presentation(
    title="雨   霖   铃",
    author_seal="柳永",
    poem_lines=None,
    out_name="Fan_Native_Master.pptx"
):
    if poem_lines is None:
        # 正统从右向左四列《雨霖铃》名句，文化意境完全契合
        poem_lines = [
            ("寒蝉凄切骤雨歇", Inches(3.2)),
            ("多情自古伤离别", Inches(2.6)),
            ("今宵酒醒杨柳岸", Inches(2.0)),
            ("便纵风情更与谁", Inches(1.4)),
        ]

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
    os.makedirs(temp_dir, exist_ok=True)

    # 1. 高清古风庭院底图（竹林 + 雨丝 + 灯笼暖光）
    bg = f3.create_courtyard_bg_v3(1920, 1080)
    bg_path = os.path.join(temp_dir, "courtyard_master_bg.jpg")
    bg.save(bg_path, quality=95)

    s1 = prs.slides.add_slide(blank)
    s2 = prs.slides.add_slide(blank)

    # 双页底图
    s1.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))
    s2.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 2. 全屏半透明白纱柔光遮罩（外朦胧内清晰对比）
    for s in (s1, s2):
        rect = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        rect.name = "!!FrostedVeil"
        rect.line.fill.background()
        spPr = rect._element.spPr
        for child in list(spPr):
            if child.tag.endswith("Fill"):
                spPr.remove(child)
        spPr.append(parse_xml(
            '<a:solidFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            '<a:srgbClr val="FFFFFF"><a:alpha val="28000"/></a:srgbClr>'
            '</a:solidFill>'
        ))

    # 3. 对角线扇轴与几何参数（右下向左上舒展）
    R = Inches(5.4)          # 大扇面半径
    cx = Inches(8.8)         # 扇轴中心偏右下（黄金分割律）
    cy = Inches(5.5)
    blade_span = 25.5        # 单片扇叶弧度
    step_rot = 28.5          # 步长 28.5°，留 3.0° 透气呼吸缝隙
    base_rot = -135.0        # 收拢基准角（斜指左上方）

    blade_rotations = [base_rot + i * step_rot for i in range(6)]

    # 4. 扇骨：使用以 (cx, cy) 为圆心的 PIE 极细辐射条，彻底锁死在扇纽中心！
    # 6 根内部竹质小骨（穿插于扇叶中轴）
    for i in range(6):
        rib_s1_rot = base_rot + blade_span * 0.5 - 0.4
        rib_s2_rot = blade_rotations[i] + blade_span * 0.5 - 0.4

        # Slide 1 (合拢态): 全部叠合在同一收起中轴
        rib1 = s1.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
        rib1.name = f"!!FanRib{i+1}"
        rib1.adjustments[0] = 0.0
        rib1.adjustments[1] = 0.8  # 0.8° 纤细竹骨
        rib1.rotation = rib_s1_rot
        rib1.line.fill.background()
        rib1.fill.solid()
        rib1.fill.fore_color.rgb = RGBColor(160, 125, 75)

        # Slide 2 (展开态): 精准贯穿每片扇叶中轴
        rib2 = s2.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
        rib2.name = f"!!FanRib{i+1}"
        rib2.adjustments[0] = 0.0
        rib2.adjustments[1] = 0.8
        rib2.rotation = rib_s2_rot
        rib2.line.fill.background()
        rib2.fill.solid()
        rib2.fill.fore_color.rgb = RGBColor(160, 125, 75)

    # 2 根折扇外侧大骨（起止两侧保护大骨，沉香木深色）
    # 大骨 1：左外侧大骨
    guard1_s1 = s1.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
    guard1_s1.name = "!!FanGuardLeft"
    guard1_s1.adjustments[0] = 0.0
    guard1_s1.adjustments[1] = 1.2
    guard1_s1.rotation = base_rot - 0.6
    guard1_s1.line.fill.background()
    guard1_s1.fill.solid()
    guard1_s1.fill.fore_color.rgb = RGBColor(120, 90, 55)

    guard1_s2 = s2.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
    guard1_s2.name = "!!FanGuardLeft"
    guard1_s2.adjustments[0] = 0.0
    guard1_s2.adjustments[1] = 1.2
    guard1_s2.rotation = blade_rotations[0] - 0.6
    guard1_s2.line.fill.background()
    guard1_s2.fill.solid()
    guard1_s2.fill.fore_color.rgb = RGBColor(120, 90, 55)

    # 大骨 2：右外侧大骨
    guard2_s1 = s1.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
    guard2_s1.name = "!!FanGuardRight"
    guard2_s1.adjustments[0] = 0.0
    guard2_s1.adjustments[1] = 1.2
    guard2_s1.rotation = base_rot + blade_span - 0.6
    guard2_s1.line.fill.background()
    guard2_s1.fill.solid()
    guard2_s1.fill.fore_color.rgb = RGBColor(120, 90, 55)

    guard2_s2 = s2.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
    guard2_s2.name = "!!FanGuardRight"
    guard2_s2.adjustments[0] = 0.0
    guard2_s2.adjustments[1] = 1.2
    guard2_s2.rotation = blade_rotations[5] + blade_span - 0.6
    guard2_s2.line.fill.background()
    guard2_s2.fill.solid()
    guard2_s2.fill.fore_color.rgb = RGBColor(120, 90, 55)

    # 5. 6 片扇面弧片 (BLOCK_ARC，内径30%留出内圈扇骨与玉纽)
    for i in range(6):
        # Slide 1 (合拢态): 6 片完全叠合，如同一把闭合的修长雅致折扇
        b1 = s1.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx - R, cy - R, 2*R, 2*R)
        b1.name = f"!!FanBlade{i+1}"
        b1.adjustments[0] = 0.0          # 起始角 0°
        b1.adjustments[1] = blade_span   # 结束角 25.5°
        b1.adjustments[2] = 0.30         # 内径 30%
        b1.rotation = base_rot
        b1.line.color.rgb = RGBColor(215, 185, 125)
        b1.line.width = Pt(0.75)
        
        spPr1 = b1._element.spPr
        for c in list(spPr1):
            if c.tag.endswith("Fill"):
                spPr1.remove(c)
        spPr1.append(parse_xml('''
        <a:gradFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" flip="none" rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:srgbClr val="B8D4A4"><a:alpha val="88000"/></a:srgbClr></a:gs>
            <a:gs pos="45000"><a:srgbClr val="78A365"><a:alpha val="82000"/></a:srgbClr></a:gs>
            <a:gs pos="100000"><a:srgbClr val="36522E"><a:alpha val="92000"/></a:srgbClr></a:gs>
          </a:gsLst>
          <a:lin ang="5400000"/>
        </a:gradFill>
        '''))
        spPr1.append(parse_xml('''
        <a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:softEdge rad="25400"/>
          <a:outerShdw blurRad="63500" dist="0" dir="0" algn="ctr" rotWithShape="0">
            <a:srgbClr val="000000"><a:alpha val="15000"/></a:srgbClr>
          </a:outerShdw>
        </a:effectLst>
        '''))

        # Slide 2 (展开态): 逐片逆时针绽放，形成 170° 优美扇面
        b2 = s2.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx - R, cy - R, 2*R, 2*R)
        b2.name = f"!!FanBlade{i+1}"
        b2.adjustments[0] = 0.0          # 起始角 0°
        b2.adjustments[1] = blade_span   # 结束角 25.5°
        b2.adjustments[2] = 0.30         # 内径 30%
        b2.rotation = blade_rotations[i]
        b2.line.color.rgb = RGBColor(215, 185, 125)
        b2.line.width = Pt(0.75)
        
        spPr2 = b2._element.spPr
        for c in list(spPr2):
            if c.tag.endswith("Fill"):
                spPr2.remove(c)
        spPr2.append(parse_xml('''
        <a:gradFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" flip="none" rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:srgbClr val="B8D4A4"><a:alpha val="88000"/></a:srgbClr></a:gs>
            <a:gs pos="45000"><a:srgbClr val="78A365"><a:alpha val="82000"/></a:srgbClr></a:gs>
            <a:gs pos="100000"><a:srgbClr val="36522E"><a:alpha val="92000"/></a:srgbClr></a:gs>
          </a:gsLst>
          <a:lin ang="5400000"/>
        </a:gradFill>
        '''))
        spPr2.append(parse_xml('''
        <a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:softEdge rad="25400"/>
          <a:outerShdw blurRad="63500" dist="0" dir="0" algn="ctr" rotWithShape="0">
            <a:srgbClr val="000000"><a:alpha val="15000"/></a:srgbClr>
          </a:outerShdw>
        </a:effectLst>
        '''))

    # 6. 扇轴三重同心金镶玉纽 (覆盖扇骨根部交汇点，天衣无缝)
    for s in (s1, s2):
        yu = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.42), cy - Inches(0.42), Inches(0.84), Inches(0.84))
        yu.name = "!!JadeRing"
        yu.line.color.rgb = RGBColor(215, 185, 125)
        yu.line.width = Pt(1.5)
        yu.fill.solid()
        yu.fill.fore_color.rgb = RGBColor(242, 248, 242)

        gold = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.24), cy - Inches(0.24), Inches(0.48), Inches(0.48))
        gold.name = "!!GoldRing"
        gold.line.fill.background()
        gold.fill.solid()
        gold.fill.fore_color.rgb = RGBColor(205, 170, 105)

        core = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.13), cy - Inches(0.13), Inches(0.26), Inches(0.26))
        core.name = "!!CoreJade"
        core.line.fill.background()
        core.fill.solid()
        core.fill.fore_color.rgb = RGBColor(34, 50, 28)

    # 7. 主标题「雨 霖 铃」+ 朱砂印章「柳永」
    t1 = s1.shapes.add_textbox(Inches(3.8), Inches(-2.6), Inches(5.8), Inches(1.5))
    t1.name = "!!MainTitle"
    p1 = t1.text_frame.paragraphs[0]
    p1.text = title
    p1.font.size = Pt(56)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(20, 32, 18)

    t2 = s2.shapes.add_textbox(Inches(3.8), Inches(0.65), Inches(5.8), Inches(1.5))
    t2.name = "!!MainTitle"
    p2 = t2.text_frame.paragraphs[0]
    p2.text = title
    p2.font.size = Pt(56)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(20, 32, 18)

    seal1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(-2.3), Inches(0.68), Inches(0.68))
    seal1.name = "!!Seal"
    seal1.fill.solid()
    seal1.fill.fore_color.rgb = RGBColor(168, 40, 36)
    seal1.line.color.rgb = RGBColor(220, 185, 130)
    seal1.line.width = Pt(1.0)
    seal1.text_frame.paragraphs[0].text = author_seal
    seal1.text_frame.paragraphs[0].font.size = Pt(13)
    seal1.text_frame.paragraphs[0].font.bold = True
    seal1.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

    seal2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(0.95), Inches(0.68), Inches(0.68))
    seal2.name = "!!Seal"
    seal2.fill.solid()
    seal2.fill.fore_color.rgb = RGBColor(168, 40, 36)
    seal2.line.color.rgb = RGBColor(220, 185, 130)
    seal2.line.width = Pt(1.0)
    seal2.text_frame.paragraphs[0].text = author_seal
    seal2.text_frame.paragraphs[0].font.size = Pt(13)
    seal2.text_frame.paragraphs[0].font.bold = True
    seal2.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

    # 8. 古典竖排诗词（左侧雅致排布，4列从右向左）
    for idx, (text, x_pos) in enumerate(poem_lines):
        y_pos = Inches(2.2)
        # Slide 1 位于右侧外场 (x > 13.333)
        tb1 = s1.shapes.add_textbox(Inches(14.0 + idx * 0.5), y_pos, Inches(0.38), Inches(3.6))
        tb1.name = f"!!PoemCol{idx}"
        tb1.text_frame.word_wrap = True
        p = tb1.text_frame.paragraphs[0]
        p.text = "\n".join(list(text))
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(56, 78, 50)
        p.alignment = PP_ALIGN.CENTER

        # Slide 2 归位
        tb2 = s2.shapes.add_textbox(x_pos, y_pos, Inches(0.38), Inches(3.6))
        tb2.name = f"!!PoemCol{idx}"
        tb2.text_frame.word_wrap = True
        p = tb2.text_frame.paragraphs[0]
        p.text = "\n".join(list(text))
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(56, 78, 50)
        p.alignment = PP_ALIGN.CENTER

    # 9. 微软官方 ISO/IEC 29500 mc:AlternateContent + p159:morph 引擎
    morph_xml = '''
    <mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
      <mc:Choice xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
                 xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main"
                 Requires="p159">
        <p:transition spd="med" advClick="1">
          <p159:morph option="byObject"/>
        </p:transition>
      </mc:Choice>
      <mc:Fallback xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
        <p:transition spd="med" advClick="1">
          <p:fade/>
        </p:transition>
      </mc:Fallback>
    </mc:AlternateContent>
    '''
    s2._element.append(parse_xml(morph_xml))

    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    out_path = os.path.join(out_dir, out_name)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prs.save(out_path)
    print(f"✅ 生成原生矢量折扇开场 PPT: {out_path}")
    return out_path

if __name__ == "__main__":
    build_fan_native_presentation()
