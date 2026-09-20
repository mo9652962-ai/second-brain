# -*- coding: utf-8 -*-
"""生产级原生可编辑矢量折扇开场演示文稿生成器（Fan Native Master）

【核心突破】真正解决 PPT 模板"可编辑 + 原生 60fps 平滑展开"问题：
1. 100% PowerPoint 原生可编辑矢量形状：
   - 扇面：BLOCK_ARC（空心折扇弧面，预留 3.0° 透气呼吸缝隙）
   - 扇骨：6 根纤细竹骨（从扇轴向外辐射贯穿）
   - 扇纽：三重同心金镶玉扣（外羊脂白玉璧 + 中鎏金环 + 内翡翠墨玉心）
2. 严格对齐抖音 @小文爱做ppt 教程实录操作：
   - 6 片扇叶，黄金比例分割
   - Slide 1 全扇合拢收起，主标题藏于画布上方场外（y < 0），诗词藏于画布右侧场外（x > 13.333）
   - Slide 2 扇面优雅绽放，主标题徐徐降落归位，竖排诗词从右向左经典四列滑入
   - 采用 PowerPoint 官方 `!!name` 强制对象匹配与 `p:morph` 原生平滑转场引擎
3. 绿色系三阶自然渐变（#B8D4A4 -> #78A365 -> #36522E），0.75pt 哑光金细描边
4. 高清古风庭院背景 + 白纱柔光半透明遮罩
5. 用户可自由双击修改标题文字（如改为答辩/汇报标题），直接按 F5 即可获得震撼原生动效！
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
        poem_lines = [
            ("昨夜疏风骤雨", Inches(2.6)),
            ("浓睡不消残酒", Inches(2.1)),
            ("试问卷帘之人", Inches(1.6)),
            ("却道海棠依旧", Inches(1.1)),
        ]

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
    os.makedirs(temp_dir, exist_ok=True)

    # 1. 高清底图
    bg = f3.create_courtyard_bg_v3(1920, 1080)
    bg_path = os.path.join(temp_dir, "courtyard_native_master_bg.jpg")
    bg.save(bg_path, quality=95)

    s1 = prs.slides.add_slide(blank)
    s2 = prs.slides.add_slide(blank)

    # 2. 双页底图
    s1.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))
    s2.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 3. 半透明白纱遮罩（全屏矩形）
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

    # 4. 原生扇叶参数（预留 3.0° 透气呼吸缝隙）
    R = Inches(4.6)
    cx = Inches(7.6)
    cy = Inches(3.7)
    blade_span = 26.5  # 单片扇叶弧度
    step_rot = 29.5    # 步长 29.5°，缝隙 = 3.0°
    base_rot = -74.0

    blade_rotations = [base_rot + i * step_rot for i in range(6)]

    # 扇骨 (6根纤细竹骨，位于扇面底层)
    for i in range(6):
        # Slide 1 (合拢态): 扇骨全部叠在 base_rot 角度
        rib1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, cy - Inches(0.02), R, Inches(0.04))
        rib1.name = f"!!FanRib{i+1}"
        rib1.rotation = base_rot
        rib1.line.fill.background()
        rib1.fill.solid()
        rib1.fill.fore_color.rgb = RGBColor(160, 130, 80)
        
        # Slide 2 (展开态): 扇骨对应每片扇叶中轴
        rib2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, cy - Inches(0.02), R, Inches(0.04))
        rib2.name = f"!!FanRib{i+1}"
        rib2.rotation = blade_rotations[i] + blade_span * 0.5
        rib2.line.fill.background()
        rib2.fill.solid()
        rib2.fill.fore_color.rgb = RGBColor(160, 130, 80)

    # 扇叶弧片 (BLOCK_ARC，空心折扇面)
    for i in range(6):
        # Slide 1 (合拢态)
        b1 = s1.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx - R, cy - R, 2*R, 2*R)
        b1.name = f"!!FanBlade{i+1}"
        b1.adjustments[1] = 0.0
        b1.adjustments[0] = blade_span
        b1.adjustments[2] = 0.32  # 内径32%，留出内圈扇骨
        b1.rotation = base_rot
        b1.line.color.rgb = RGBColor(210, 180, 120)
        b1.line.width = Pt(0.75)
        
        spPr1 = b1._element.spPr
        for c in list(spPr1):
            if c.tag.endswith("Fill"):
                spPr1.remove(c)
        spPr1.append(parse_xml('''
        <a:gradFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" flip="none" rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:srgbClr val="B8D4A4"><a:alpha val="88000"/></a:srgbClr></a:gs>
            <a:gs pos="40000"><a:srgbClr val="78A365"><a:alpha val="82000"/></a:srgbClr></a:gs>
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

        # Slide 2 (展开态)
        b2 = s2.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx - R, cy - R, 2*R, 2*R)
        b2.name = f"!!FanBlade{i+1}"
        b2.adjustments[1] = 0.0
        b2.adjustments[0] = blade_span
        b2.adjustments[2] = 0.32
        b2.rotation = blade_rotations[i]
        b2.line.color.rgb = RGBColor(210, 180, 120)
        b2.line.width = Pt(0.75)
        
        spPr2 = b2._element.spPr
        for c in list(spPr2):
            if c.tag.endswith("Fill"):
                spPr2.remove(c)
        spPr2.append(parse_xml('''
        <a:gradFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" flip="none" rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:srgbClr val="B8D4A4"><a:alpha val="88000"/></a:srgbClr></a:gs>
            <a:gs pos="40000"><a:srgbClr val="78A365"><a:alpha val="82000"/></a:srgbClr></a:gs>
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

    # 5. 扇轴三重同心玉纽 (外白玉璧 + 中鎏金环 + 内翡翠心)
    for s in (s1, s2):
        yu = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.42), cy - Inches(0.42), Inches(0.84), Inches(0.84))
        yu.name = "!!JadeRing"
        yu.line.color.rgb = RGBColor(210, 180, 120)
        yu.line.width = Pt(1.5)
        yu.fill.solid()
        yu.fill.fore_color.rgb = RGBColor(240, 248, 240)
        
        gold = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.24), cy - Inches(0.24), Inches(0.48), Inches(0.48))
        gold.name = "!!GoldRing"
        gold.line.fill.background()
        gold.fill.solid()
        gold.fill.fore_color.rgb = RGBColor(200, 165, 100)
        
        core = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.14), cy - Inches(0.14), Inches(0.28), Inches(0.28))
        core.name = "!!CoreJade"
        core.line.fill.background()
        core.fill.solid()
        core.fill.fore_color.rgb = RGBColor(35, 52, 30)

    # 6. 主标题 + 朱砂印章
    t1 = s1.shapes.add_textbox(Inches(3.6), Inches(-2.6), Inches(6.0), Inches(1.5))
    t1.name = "!!MainTitle"
    p1 = t1.text_frame.paragraphs[0]
    p1.text = title
    p1.font.size = Pt(56)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(22, 35, 20)

    t2 = s2.shapes.add_textbox(Inches(3.6), Inches(0.55), Inches(6.0), Inches(1.5))
    t2.name = "!!MainTitle"
    p2 = t2.text_frame.paragraphs[0]
    p2.text = title
    p2.font.size = Pt(56)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(22, 35, 20)

    # 印章
    seal1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(-2.3), Inches(0.68), Inches(0.68))
    seal1.name = "!!Seal"
    seal1.fill.solid()
    seal1.fill.fore_color.rgb = RGBColor(165, 42, 38)
    seal1.line.color.rgb = RGBColor(220, 180, 130)
    seal1.line.width = Pt(1.0)
    sp1 = seal1.text_frame.paragraphs[0]
    sp1.text = author_seal
    sp1.font.size = Pt(13)
    sp1.font.bold = True
    sp1.font.color.rgb = RGBColor(255, 255, 255)

    seal2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(0.85), Inches(0.68), Inches(0.68))
    seal2.name = "!!Seal"
    seal2.fill.solid()
    seal2.fill.fore_color.rgb = RGBColor(165, 42, 38)
    seal2.line.color.rgb = RGBColor(220, 180, 130)
    seal2.line.width = Pt(1.0)
    sp2 = seal2.text_frame.paragraphs[0]
    sp2.text = author_seal
    sp2.font.size = Pt(13)
    sp2.font.bold = True
    sp2.font.color.rgb = RGBColor(255, 255, 255)

    # 7. 古典竖排诗词（传统从右向左四列）
    for idx, (text, x_pos) in enumerate(poem_lines):
        y_pos = Inches(2.1)
        # Slide 1: 位于右侧外场
        tb1 = s1.shapes.add_textbox(Inches(14.0 + idx * 0.5), y_pos, Inches(0.38), Inches(3.6))
        tb1.name = f"!!PoemCol{idx}"
        tf1 = tb1.text_frame
        tf1.word_wrap = True
        p = tf1.paragraphs[0]
        p.text = "\n".join(list(text))
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(58, 80, 52)
        p.alignment = PP_ALIGN.CENTER
        
        # Slide 2: 归位
        tb2 = s2.shapes.add_textbox(x_pos, y_pos, Inches(0.38), Inches(3.6))
        tb2.name = f"!!PoemCol{idx}"
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        p = tf2.paragraphs[0]
        p.text = "\n".join(list(text))
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(58, 80, 52)
        p.alignment = PP_ALIGN.CENTER

    # 8. Slide 2 挂载 Morph 平滑切换
    trans_xml = (
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'spd="med" advClick="1"><p:morph option="byObject"/></p:transition>'
    )
    s2._element.append(parse_xml(trans_xml))

    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    out_path = os.path.join(out_dir, out_name)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prs.save(out_path)
    print(f"✅ 生成原生矢量折扇开场 PPT: {out_path}")
    return out_path

if __name__ == "__main__":
    build_fan_native_presentation()
