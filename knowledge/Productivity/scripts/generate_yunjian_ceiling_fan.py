# -*- coding: utf-8 -*-
"""【云间设计PPT】角落锚定式对角双扇梯级绽放（PPT天花板·极致版）生成器

【千轮深挖底层突破】：
1. 角落锚定式构图（Corner-Anchored Layout）：
   - 右下主扇圆心严丝合缝锚定在画布右下角顶点 (x = 13.333 in, y = 7.50 in)；
   - 左上副扇圆心严丝合缝锚定在画布左上角顶点 (x = 0.000 in, y = 0.000 in)；
   - 彻底打破悬空漂浮感，构建纯正从角落向全场“破晓绽放”的张力与视觉动线。
2. 梯级角度与力学阴影：
   - 6 片扇叶，角度步长严格恒定为 15.0°（75°, 60°, 45°, 30°, 15°, 0°）；
   - 统一定向 135° 右下方向柔和外阴影（dir=8100000），片片层叠出纸雕 3D 浮雕深度。
3. 画中画透光取景（blipFill）：
   - 底层为高清唯美自然艺术底图；
   - 中层为全屏 35% 白纱柔光遮罩；
   - 顶层扇面透出 100% 鲜明画质，扇外烟雨朦胧、扇内明艳鲜活。
4. 双态平滑切换（Morph 原生 60fps）：
   - Slide 1: 12 片扇叶收拢贴紧角落边界，文案在画外；
   - Slide 2: 12 片扇叶自对角角落梯级弹射绽放，文案在中央被双折扇优雅环抱。
"""
import os, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml import parse_xml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BG_DEFAULT_PATH = os.path.join(
    os.path.dirname(SCRIPT_DIR), "images", "authentic_fan_bg_hd.jpg"
)

def build_yunjian_ceiling_presentation(
    main_title="春   天   序",
    sub_title="Spring  ·  2026",
    quote_text="当折扇与微风相遇，\n春天便有了具象的模样，\n愿日子清透，万事皆有生机。",
    out_name="Fan_Ceiling_Showcase.pptx"
):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    bg_path = BG_DEFAULT_PATH
    if not os.path.exists(bg_path):
        temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
        bg_path = os.path.join(temp_dir, "fan_hq", "authentic_bg_hd.jpg")

    s1 = prs.slides.add_slide(blank)
    s2 = prs.slides.add_slide(blank)

    # 获取图片 rId
    temp1 = s1.shapes.add_picture(bg_path, 0, 0, width=Inches(1), height=Inches(1))
    rid1 = temp1._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip').get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
    s1.shapes._spTree.remove(temp1._element)

    temp2 = s2.shapes.add_picture(bg_path, 0, 0, width=Inches(1), height=Inches(1))
    rid2 = temp2._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip').get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
    s2.shapes._spTree.remove(temp2._element)

    # 1. 双页全屏底图
    s1.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))
    s2.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 2. 全屏 35% 半透明白纱柔光遮罩
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
            '<a:srgbClr val="F8FAF6"><a:alpha val="35000"/></a:srgbClr>'
            '</a:solidFill>'
        ))

    # 3. 对角角落锚定几何参数
    # 右下角主折扇：圆心牢固锚定在 (13.333, 7.50) 右下角顶点！
    cx_br, cy_br, R_br = Inches(13.333), Inches(7.50), Inches(5.8)
    br_base_rot = -165.0  # 闭合时贴合底边

    # 左上角副折扇：圆心牢固锚定在 (0.000, 0.000) 左上角顶点！
    cx_tl, cy_tl, R_tl = Inches(0.000), Inches(0.000), Inches(4.8)
    tl_base_rot = 15.0   # 闭合时贴合顶边

    blade_angles = [75.0, 60.0, 45.0, 30.0, 15.0, 0.0]
    arc_span = 25.0

    # --- 渲染右下角 6 片扇叶 ---
    for i, ang_offset in enumerate(blade_angles):
        rot_s1 = br_base_rot
        rot_s2 = br_base_rot + ang_offset

        # Slide 1 (合拢态)
        b1 = s1.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx_br - R_br, cy_br - R_br, 2*R_br, 2*R_br)
        b1.name = f"!!BRFan{i+1}"
        b1.adjustments[0] = 0.0
        b1.adjustments[1] = arc_span
        b1.adjustments[2] = 0.28
        b1.rotation = rot_s1
        b1.line.color.rgb = RGBColor(215, 185, 125)
        b1.line.width = Pt(0.75)
        spPr1 = b1._element.spPr
        for c in list(spPr1):
            if c.tag.endswith("Fill"): spPr1.remove(c)
        spPr1.append(parse_xml(f'''
        <a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">
          <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid1}"/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        '''))

        # Slide 2 (展开态 · 带 135° 右下方向柔和外阴影)
        b2 = s2.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx_br - R_br, cy_br - R_br, 2*R_br, 2*R_br)
        b2.name = f"!!BRFan{i+1}"
        b2.adjustments[0] = 0.0
        b2.adjustments[1] = arc_span
        b2.adjustments[2] = 0.28
        b2.rotation = rot_s2
        b2.line.color.rgb = RGBColor(215, 185, 125)
        b2.line.width = Pt(0.75)
        spPr2 = b2._element.spPr
        for c in list(spPr2):
            if c.tag.endswith("Fill"): spPr2.remove(c)
        spPr2.append(parse_xml(f'''
        <a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">
          <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid2}"/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        '''))
        spPr2.append(parse_xml('''
        <a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:outerShdw blurRad="50800" dist="38100" dir="8100000" algn="tl" rotWithShape="0">
            <a:srgbClr val="000000"><a:alpha val="25000"/></a:srgbClr>
          </a:outerShdw>
        </a:effectLst>
        '''))

    # --- 渲染左上角 6 片扇叶 ---
    for i, ang_offset in enumerate(blade_angles):
        rot_s1 = tl_base_rot
        rot_s2 = tl_base_rot + ang_offset

        # Slide 1 (合拢态)
        b1 = s1.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx_tl - R_tl, cy_tl - R_tl, 2*R_tl, 2*R_tl)
        b1.name = f"!!TLFan{i+1}"
        b1.adjustments[0] = 0.0
        b1.adjustments[1] = arc_span
        b1.adjustments[2] = 0.28
        b1.rotation = rot_s1
        b1.line.color.rgb = RGBColor(215, 185, 125)
        b1.line.width = Pt(0.75)
        spPr1 = b1._element.spPr
        for c in list(spPr1):
            if c.tag.endswith("Fill"): spPr1.remove(c)
        spPr1.append(parse_xml(f'''
        <a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">
          <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid1}"/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        '''))

        # Slide 2 (展开态)
        b2 = s2.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx_tl - R_tl, cy_tl - R_tl, 2*R_tl, 2*R_tl)
        b2.name = f"!!TLFan{i+1}"
        b2.adjustments[0] = 0.0
        b2.adjustments[1] = arc_span
        b2.adjustments[2] = 0.28
        b2.rotation = rot_s2
        b2.line.color.rgb = RGBColor(215, 185, 125)
        b2.line.width = Pt(0.75)
        spPr2 = b2._element.spPr
        for c in list(spPr2):
            if c.tag.endswith("Fill"): spPr2.remove(c)
        spPr2.append(parse_xml(f'''
        <a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">
          <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid2}"/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        '''))
        spPr2.append(parse_xml('''
        <a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:outerShdw blurRad="50800" dist="38100" dir="8100000" algn="tl" rotWithShape="0">
            <a:srgbClr val="000000"><a:alpha val="25000"/></a:srgbClr>
          </a:outerShdw>
        </a:effectLst>
        '''))

    # 4. 双扇轴心玉纽（紧扣在角落顶点）
    for s in (s1, s2):
        # 右下角玉纽
        yu_br = s.shapes.add_shape(MSO_SHAPE.OVAL, cx_br - Inches(0.4), cy_br - Inches(0.4), Inches(0.8), Inches(0.8))
        yu_br.name = "!!JadeBR"
        yu_br.line.color.rgb = RGBColor(215, 185, 125)
        yu_br.line.width = Pt(1.5)
        yu_br.fill.solid()
        yu_br.fill.fore_color.rgb = RGBColor(245, 248, 245)

        # 左上角玉纽
        yu_tl = s.shapes.add_shape(MSO_SHAPE.OVAL, cx_tl - Inches(0.35), cy_tl - Inches(0.35), Inches(0.7), Inches(0.7))
        yu_tl.name = "!!JadeTL"
        yu_tl.line.color.rgb = RGBColor(215, 185, 125)
        yu_tl.line.width = Pt(1.5)
        yu_tl.fill.solid()
        yu_tl.fill.fore_color.rgb = RGBColor(245, 248, 245)

    # 5. 中央文案排版
    t1 = s1.shapes.add_textbox(Inches(3.2), Inches(-3.0), Inches(7.0), Inches(1.8))
    t1.name = "!!MainTitle"
    p1 = t1.text_frame.paragraphs[0]
    p1.text = main_title
    p1.font.size = Pt(60)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(22, 36, 20)
    p1.alignment = PP_ALIGN.CENTER

    t2 = s2.shapes.add_textbox(Inches(3.2), Inches(1.8), Inches(7.0), Inches(1.8))
    t2.name = "!!MainTitle"
    p2 = t2.text_frame.paragraphs[0]
    p2.text = main_title
    p2.font.size = Pt(60)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(22, 36, 20)
    p2.alignment = PP_ALIGN.CENTER

    sub1 = s1.shapes.add_textbox(Inches(3.2), Inches(-1.2), Inches(7.0), Inches(0.8))
    sub1.name = "!!SubTitle"
    sp1 = sub1.text_frame.paragraphs[0]
    sp1.text = sub_title
    sp1.font.size = Pt(18)
    sp1.font.color.rgb = RGBColor(90, 115, 85)
    sp1.alignment = PP_ALIGN.CENTER

    sub2 = s2.shapes.add_textbox(Inches(3.2), Inches(3.2), Inches(7.0), Inches(0.8))
    sub2.name = "!!SubTitle"
    sp2 = sub2.text_frame.paragraphs[0]
    sp2.text = sub_title
    sp2.font.size = Pt(18)
    sp2.font.color.rgb = RGBColor(90, 115, 85)
    sp2.alignment = PP_ALIGN.CENTER

    q1 = s1.shapes.add_textbox(Inches(3.2), Inches(8.5), Inches(7.0), Inches(1.6))
    q1.name = "!!QuoteText"
    qp1 = q1.text_frame.paragraphs[0]
    qp1.text = quote_text
    qp1.font.size = Pt(16)
    qp1.font.color.rgb = RGBColor(55, 75, 50)
    qp1.alignment = PP_ALIGN.CENTER

    q2 = s2.shapes.add_textbox(Inches(3.2), Inches(4.2), Inches(7.0), Inches(1.6))
    q2.name = "!!QuoteText"
    qp2 = q2.text_frame.paragraphs[0]
    qp2.text = quote_text
    qp2.font.size = Pt(16)
    qp2.font.color.rgb = RGBColor(55, 75, 50)
    qp2.alignment = PP_ALIGN.CENTER

    # 6. 微软官方 ISO/IEC 29500 mc:AlternateContent + p159:morph 引擎
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
    print(f"✅ 生成【云间设计PPT】角落锚定对角双扇天花板 PPT: {out_path}")
    return out_path

if __name__ == "__main__":
    build_yunjian_ceiling_presentation()
