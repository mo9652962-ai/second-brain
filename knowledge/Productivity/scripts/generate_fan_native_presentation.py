# -*- coding: utf-8 -*-
"""生产级原生可编辑矢量折扇开场演示文稿生成器（Fan Native Master · 9.8 顶级美学版）

【核心突破：画中画裁剪式透光折扇 + 官方 Morph 原生 60fps 平滑展开】
1. 解决突兀色块（彻底融入背景世界）：
   - 扇面不使用脱节生硬的纯绿渐变色块，而是使用【底图图片填充 (blipFill)】直接形成透光取景窗口；
   - 底层为高清唯美原图（青翠垂柳、晶莹玻璃风铃、彩纸流苏、晨曦暖阳散景）；
   - 中层为全屏 35% 半透明白纱柔光遮罩；
   - 顶层扇面透出 100% 鲜明未遮罩的高清原图景深，形成“扇外烟雨朦胧，扇内明丽鲜活”的绝美画中画视差。
2. 空间构图与黄金分割（对角线张力）：
   - 扇轴置于右下方黄金分割区（x ≈ Inches(9.2), y ≈ Inches(5.8)）；
   - 6 片扇叶与 8 根扇骨朝左上方与正上方舒展绽放，打破呆板居中，具备强烈的动态视觉冲击力。
3. 文人书画留白与文字版式：
   - 标题移至左上方黄金留白区，行楷风格大字「雨   霖   铃」（54pt，深墨玉色 #142214）；
   - 配套朱砂篆刻方印「柳永」+ 词牌名篇小注副标题；
   - 正统四列从右向左古典竖排《雨霖铃》名句；
4. 扇骨扇叶同心一体：
   - 扇骨采用以扇轴为圆心的 PIE 0.8° 辐条，100% 锁死在玉纽轴心辐射而出；
   - 左右两侧增设深色沉香木大骨（1.2°），力学骨架稳固真实；
5. 官方 ISO/IEC 29500 mc:AlternateContent + p159:morph 原生平滑动画：
   - Slide 1: 扇子完全收拢成修长闭合折扇（斜指左上），标题/副标题/诗词均在画外；
   - Slide 2: 扇面如机械快门般平滑旋转绽放，标题降落，诗词自右向左有序滑入；
   - 100% 原生矢量可编辑，按 F5 即可在 WPS 或 PowerPoint 中体验真实 60fps 动画。
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

def build_fan_native_presentation(
    title="雨   霖   铃",
    author_seal="柳永",
    subtitle="北宋 · 柳永  ｜  秋蝉凄清 · 骤雨初歇 · 晓风残月",
    poem_lines=None,
    out_name="Fan_Native_Master.pptx"
):
    if poem_lines is None:
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

    bg_path = BG_DEFAULT_PATH
    if not os.path.exists(bg_path):
        temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
        bg_path = os.path.join(temp_dir, "fan_hq", "authentic_bg_hd.jpg")

    s1 = prs.slides.add_slide(blank)
    s2 = prs.slides.add_slide(blank)

    # 1. 获取图片 rId 引用
    temp1 = s1.shapes.add_picture(bg_path, 0, 0, width=Inches(1), height=Inches(1))
    rid1 = temp1._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip').get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
    s1.shapes._spTree.remove(temp1._element)

    temp2 = s2.shapes.add_picture(bg_path, 0, 0, width=Inches(1), height=Inches(1))
    rid2 = temp2._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip').get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
    s2.shapes._spTree.remove(temp2._element)

    # 2. 双页底图
    s1.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))
    s2.shapes.add_picture(bg_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 3. 全屏半透明白纱柔光遮罩（透明度 35%）
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
            '<a:srgbClr val="FFFFFF"><a:alpha val="35000"/></a:srgbClr>'
            '</a:solidFill>'
        ))

    # 4. 对角线折扇参数
    R = Inches(5.6)
    cx = Inches(9.2)
    cy = Inches(5.8)
    blade_span = 25.5
    step_rot = 28.5
    base_rot = -135.0
    blade_rotations = [base_rot + i * step_rot for i in range(6)]

    # 5. 扇骨系统（同心锁定在扇轴 cx, cy，100% 无偏心漂浮）
    for i in range(6):
        rib_s1_rot = base_rot + blade_span * 0.5 - 0.4
        rib_s2_rot = blade_rotations[i] + blade_span * 0.5 - 0.4

        rib1 = s1.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
        rib1.name = f"!!FanRib{i+1}"
        rib1.adjustments[0] = 0.0
        rib1.adjustments[1] = 0.8
        rib1.rotation = rib_s1_rot
        rib1.line.fill.background()
        rib1.fill.solid()
        rib1.fill.fore_color.rgb = RGBColor(165, 130, 85)

        rib2 = s2.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
        rib2.name = f"!!FanRib{i+1}"
        rib2.adjustments[0] = 0.0
        rib2.adjustments[1] = 0.8
        rib2.rotation = rib_s2_rot
        rib2.line.fill.background()
        rib2.fill.solid()
        rib2.fill.fore_color.rgb = RGBColor(165, 130, 85)

    # 2 根折扇外侧大骨
    for s, s_rot_l, s_rot_r in [
        (s1, base_rot - 0.6, base_rot + blade_span - 0.6),
        (s2, blade_rotations[0] - 0.6, blade_rotations[5] + blade_span - 0.6)
    ]:
        gl = s.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
        gl.name = "!!FanGuardLeft"
        gl.adjustments[0] = 0.0
        gl.adjustments[1] = 1.2
        gl.rotation = s_rot_l
        gl.line.fill.background()
        gl.fill.solid()
        gl.fill.fore_color.rgb = RGBColor(125, 95, 60)

        gr = s.shapes.add_shape(MSO_SHAPE.PIE, cx - R, cy - R, 2*R, 2*R)
        gr.name = "!!FanGuardRight"
        gr.adjustments[0] = 0.0
        gr.adjustments[1] = 1.2
        gr.rotation = s_rot_r
        gr.line.fill.background()
        gr.fill.solid()
        gr.fill.fore_color.rgb = RGBColor(125, 95, 60)

    # 6. 6 片扇面弧片（核心画中画底图透光填充，消除色块突兀感）
    for i in range(6):
        # Slide 1 (合拢态)
        b1 = s1.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx - R, cy - R, 2*R, 2*R)
        b1.name = f"!!FanBlade{i+1}"
        b1.adjustments[0] = 0.0
        b1.adjustments[1] = blade_span
        b1.adjustments[2] = 0.30
        b1.rotation = base_rot
        b1.line.color.rgb = RGBColor(215, 185, 125)
        b1.line.width = Pt(0.75)
        spPr1 = b1._element.spPr
        for c in list(spPr1):
            if c.tag.endswith("Fill"):
                spPr1.remove(c)
        spPr1.append(parse_xml(f'''
        <a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">
          <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid1}"/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        '''))
        spPr1.append(parse_xml('''
        <a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:softEdge rad="15000"/>
          <a:outerShdw blurRad="63500" dist="0" dir="0" algn="ctr" rotWithShape="0">
            <a:srgbClr val="000000"><a:alpha val="20000"/></a:srgbClr>
          </a:outerShdw>
        </a:effectLst>
        '''))

        # Slide 2 (展开态)
        b2 = s2.shapes.add_shape(MSO_SHAPE.BLOCK_ARC, cx - R, cy - R, 2*R, 2*R)
        b2.name = f"!!FanBlade{i+1}"
        b2.adjustments[0] = 0.0
        b2.adjustments[1] = blade_span
        b2.adjustments[2] = 0.30
        b2.rotation = blade_rotations[i]
        b2.line.color.rgb = RGBColor(215, 185, 125)
        b2.line.width = Pt(0.75)
        spPr2 = b2._element.spPr
        for c in list(spPr2):
            if c.tag.endswith("Fill"):
                spPr2.remove(c)
        spPr2.append(parse_xml(f'''
        <a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">
          <a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid2}"/>
          <a:stretch><a:fillRect/></a:stretch>
        </a:blipFill>
        '''))
        spPr2.append(parse_xml('''
        <a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
          <a:softEdge rad="15000"/>
          <a:outerShdw blurRad="63500" dist="0" dir="0" algn="ctr" rotWithShape="0">
            <a:srgbClr val="000000"><a:alpha val="20000"/></a:srgbClr>
          </a:outerShdw>
        </a:effectLst>
        '''))

    # 7. 扇轴三重同心金镶玉纽
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

    # 8. 左上方留白区：文人书画版式
    t1 = s1.shapes.add_textbox(Inches(1.2), Inches(-2.6), Inches(5.0), Inches(1.5))
    t1.name = "!!MainTitle"
    p1 = t1.text_frame.paragraphs[0]
    p1.text = title
    p1.font.size = Pt(54)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(20, 32, 18)

    t2 = s2.shapes.add_textbox(Inches(1.2), Inches(0.85), Inches(5.0), Inches(1.5))
    t2.name = "!!MainTitle"
    p2 = t2.text_frame.paragraphs[0]
    p2.text = title
    p2.font.size = Pt(54)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(20, 32, 18)

    seal1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(-2.4), Inches(0.68), Inches(0.68))
    seal1.name = "!!Seal"
    seal1.fill.solid()
    seal1.fill.fore_color.rgb = RGBColor(168, 40, 36)
    seal1.line.color.rgb = RGBColor(220, 185, 130)
    seal1.line.width = Pt(1.0)
    seal1.text_frame.paragraphs[0].text = author_seal
    seal1.text_frame.paragraphs[0].font.size = Pt(13)
    seal1.text_frame.paragraphs[0].font.bold = True
    seal1.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

    seal2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.5), Inches(1.05), Inches(0.68), Inches(0.68))
    seal2.name = "!!Seal"
    seal2.fill.solid()
    seal2.fill.fore_color.rgb = RGBColor(168, 40, 36)
    seal2.line.color.rgb = RGBColor(220, 185, 130)
    seal2.line.width = Pt(1.0)
    seal2.text_frame.paragraphs[0].text = author_seal
    seal2.text_frame.paragraphs[0].font.size = Pt(13)
    seal2.text_frame.paragraphs[0].font.bold = True
    seal2.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

    sub1 = s1.shapes.add_textbox(Inches(1.2), Inches(-1.5), Inches(5.5), Inches(0.8))
    sub1.name = "!!SubTitle"
    sub1.text_frame.paragraphs[0].text = subtitle
    sub1.text_frame.paragraphs[0].font.size = Pt(14)
    sub1.text_frame.paragraphs[0].font.color.rgb = RGBColor(70, 95, 65)

    sub2 = s2.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(5.5), Inches(0.8))
    sub2.name = "!!SubTitle"
    sub2.text_frame.paragraphs[0].text = subtitle
    sub2.text_frame.paragraphs[0].font.size = Pt(14)
    sub2.text_frame.paragraphs[0].font.color.rgb = RGBColor(70, 95, 65)

    # 9. 左侧四列正统从右向左宋词名句（竖排）
    for idx, (text, x_pos) in enumerate(poem_lines):
        y_pos = Inches(3.0)
        tb1 = s1.shapes.add_textbox(Inches(14.0 + idx * 0.5), y_pos, Inches(0.38), Inches(3.6))
        tb1.name = f"!!PoemCol{idx}"
        tb1.text_frame.word_wrap = True
        p = tb1.text_frame.paragraphs[0]
        p.text = "\n".join(list(text))
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(48, 68, 44)
        p.alignment = PP_ALIGN.CENTER

        tb2 = s2.shapes.add_textbox(x_pos, y_pos, Inches(0.38), Inches(3.6))
        tb2.name = f"!!PoemCol{idx}"
        tb2.text_frame.word_wrap = True
        p = tb2.text_frame.paragraphs[0]
        p.text = "\n".join(list(text))
        p.font.size = Pt(15)
        p.font.color.rgb = RGBColor(48, 68, 44)
        p.alignment = PP_ALIGN.CENTER

    # 10. 微软官方 ISO/IEC 29500 mc:AlternateContent + p159:morph 引擎
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
