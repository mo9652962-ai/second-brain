# -*- coding: utf-8 -*-
"""PPT 国奖级扇叶开场平滑动画生成器 (Fan Blade Opening Presentation Generator)

基于抖音 @小文爱做ppt 教程逆向工程拆解：
1. 几何原理：6 片 52° 缺角圆形（留 8° 间隙），中心辐射排列
2. 状态差设计：
   - 奇数页（起始态）：扇叶全部合拢回 0° 闭合位，主标题与内容置于屏幕上方外场
   - 偶数页（终态）：扇叶顺时针 360° 绽放展开（0°, 60°, 120°, 180°, 240°, 300°），主标题优雅落位
3. 切换引擎：注入 OpenXML 原生 <p:transition><p:morph/></p:transition>，在 PowerPoint / WPS 中一键播放即享机械光圈绽放动效
"""
import os, sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import qn


def set_alpha(shape, pct):
    """设置形状填充不透明度 (0-100)"""
    sF = shape.fill._xPr.find(qn('a:solidFill'))
    if sF is not None:
        clr = sF.find(qn('a:srgbClr'))
        if clr is not None:
            a = clr.makeelement(qn('a:alpha'), {'val': str(int(pct * 1000))})
            clr.append(a)


def add_morph_transition(slide):
    """向幻灯片注入 OpenXML 原生平滑 (Morph) 切换配置"""
    trans_xml = (
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'spd="med" advClick="1">'
        '<p:morph option="byObject"/>'
        '</p:transition>'
    )
    slide._element.append(parse_xml(trans_xml))


def build_fan_blade_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    os.makedirs(out_dir, exist_ok=True)

    # 配色 Tokens
    DEEP_RED   = RGBColor(0x7A, 0x10, 0x22)
    BRIGHT_RED = RGBColor(0xB7, 0x1C, 0x2C)
    GOLD       = RGBColor(0xD4, 0xAF, 0x37)
    PALE_GOLD  = RGBColor(0xF0, 0xDF, 0xA8)
    WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
    DARK_TEXT  = RGBColor(0x2A, 0x24, 0x1E)

    TECH_NAVY  = RGBColor(0x0A, 0x11, 0x28)
    TECH_BLUE  = RGBColor(0x00, 0x1F, 0x54)
    CYAN       = RGBColor(0x00, 0xF5, 0xD4)
    TEAL       = RGBColor(0x00, 0xB4, 0xD8)

    # 扇叶几何参数
    blade_diameter = Inches(6.8)
    center_x = (prs.slide_width - blade_diameter) / 2
    center_y = (prs.slide_height - blade_diameter) / 2
    blade_angles = [0, 60, 120, 180, 240, 300]
    sweep_angle = 52.0  # 留 8 度呼吸空隙

    # =========================================================================
    # PART 1: 国奖 / 荣誉答辩红金扇叶开场
    # =========================================================================

    # ── 1.1 Slide 1: 合拢起始态 (Closed Initial State) ──
    s1 = prs.slides.add_slide(blank_layout)

    # 背景
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill1 = bg1.fill; fill1.gradient()
    s_stop = fill1.gradient_stops
    s_stop[0].color.rgb = DEEP_RED; s_stop[0].position = 0.0
    s_stop[1].color.rgb = BRIGHT_RED; s_stop[1].position = 1.0
    fill1.gradient_angle = 45; bg1.line.fill.background()

    # 全屏磨砂白遮罩
    mask1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    mask1.fill.solid(); mask1.fill.fore_color.rgb = WHITE
    set_alpha(mask1, 20); mask1.line.fill.background()

    # 6 片扇叶（起始态：全部重叠归于 0° 闭合位置）
    for i in range(6):
        blade = s1.shapes.add_shape(MSO_SHAPE.PIE, center_x, center_y, blade_diameter, blade_diameter)
        blade.name = f"blade_{i+1}"
        blade.adjustments[0] = 0.0
        blade.adjustments[1] = sweep_angle
        blade.rotation = 0.0  # 完全闭合
        blade.fill.solid()
        blade.fill.fore_color.rgb = GOLD if i % 2 == 0 else PALE_GOLD
        set_alpha(blade, 80 if i % 2 == 0 else 60)
        blade.line.color.rgb = GOLD
        blade.line.width = Pt(1.5)

    # 中心装饰同心圆（起始态）
    core1 = s1.shapes.add_shape(MSO_SHAPE.OVAL, center_x + Inches(2.2), center_y + Inches(2.2), Inches(2.4), Inches(2.4))
    core1.name = "core_medallion"
    core1.fill.solid(); core1.fill.fore_color.rgb = DEEP_RED
    core1.line.color.rgb = GOLD; core1.line.width = Pt(2.0)

    # 标题文字（起始态：在屏幕上方场外 y = -3.0 英寸，等待平滑降落）
    tb1 = s1.shapes.add_textbox(Inches(1.5), Inches(-3.0), Inches(10.333), Inches(2.5))
    tb1.name = "main_title_box"
    tf1 = tb1.text_frame; tf1.word_wrap = True
    p1 = tf1.paragraphs[0]; p1.text = "让青春在奋斗中绽放绚丽之花"
    p1.font.size = Pt(36); p1.font.bold = True; p1.font.color.rgb = GOLD; p1.alignment = PP_ALIGN.CENTER
    p1_sub = tf1.add_paragraph(); p1_sub.text = "2026 年度国家奖学金评审答辩 · 汇报展示"
    p1_sub.font.size = Pt(18); p1_sub.font.color.rgb = PALE_GOLD; p1_sub.alignment = PP_ALIGN.CENTER

    # ── 1.2 Slide 2: 绽放展开终态 (Opened Final State with Morph) ──
    s2 = prs.slides.add_slide(blank_layout)
    add_morph_transition(s2)  # 注入平滑切换

    # 背景
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill2 = bg2.fill; fill2.gradient()
    s_stop2 = fill2.gradient_stops
    s_stop2[0].color.rgb = DEEP_RED; s_stop2[0].position = 0.0
    s_stop2[1].color.rgb = BRIGHT_RED; s_stop2[1].position = 1.0
    fill2.gradient_angle = 45; bg2.line.fill.background()

    # 全屏磨砂白遮罩
    mask2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    mask2.fill.solid(); mask2.fill.fore_color.rgb = WHITE
    set_alpha(mask2, 20); mask2.line.fill.background()

    # 6 片扇叶（终态：平滑旋转展开至 360 度圆周）
    for i, angle in enumerate(blade_angles):
        blade2 = s2.shapes.add_shape(MSO_SHAPE.PIE, center_x, center_y, blade_diameter, blade_diameter)
        blade2.name = f"blade_{i+1}"  # 相同名称触发 Morph 平滑补间
        blade2.adjustments[0] = 0.0
        blade2.adjustments[1] = sweep_angle
        blade2.rotation = float(angle)  # 各自展开旋转
        blade2.fill.solid()
        blade2.fill.fore_color.rgb = GOLD if i % 2 == 0 else PALE_GOLD
        set_alpha(blade2, 80 if i % 2 == 0 else 60)
        blade2.line.color.rgb = GOLD
        blade2.line.width = Pt(1.5)

    # 中心装饰同心圆（终态）
    core2 = s2.shapes.add_shape(MSO_SHAPE.OVAL, center_x + Inches(2.2), center_y + Inches(2.2), Inches(2.4), Inches(2.4))
    core2.name = "core_medallion"
    core2.fill.solid(); core2.fill.fore_color.rgb = DEEP_RED
    core2.line.color.rgb = GOLD; core2.line.width = Pt(2.0)
    tf_c = core2.text_frame
    pc = tf_c.paragraphs[0]; pc.text = "❖"
    pc.font.size = Pt(28); pc.font.color.rgb = GOLD; pc.alignment = PP_ALIGN.CENTER

    # 标题文字（终态：平滑降落至居中偏上方显眼位置）
    tb2 = s2.shapes.add_textbox(Inches(1.5), Inches(0.8), Inches(10.333), Inches(2.2))
    tb2.name = "main_title_box"
    tf2 = tb2.text_frame; tf2.word_wrap = True
    p2 = tf2.paragraphs[0]; p2.text = "让青春在奋斗中绽放绚丽之花"
    p2.font.size = Pt(36); p2.font.bold = True; p2.font.color.rgb = GOLD; p2.alignment = PP_ALIGN.CENTER
    p2_sub = tf2.add_paragraph(); p2_sub.text = "2026 年度国家奖学金评审答辩 · 汇报展示"
    p2_sub.font.size = Pt(18); p2_sub.font.color.rgb = PALE_GOLD; p2_sub.alignment = PP_ALIGN.CENTER

    # 底部个人元数据卡片
    card_meta = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(3.8), Inches(6.1), Inches(5.733), Inches(0.9))
    card_meta.adjustments[0] = 0.2
    card_meta.fill.solid(); card_meta.fill.fore_color.rgb = WHITE
    card_meta.line.color.rgb = GOLD; card_meta.line.width = Pt(1.2)
    tf_cm = card_meta.text_frame
    pcm = tf_cm.paragraphs[0]
    pcm.text = "汇报人：sora  |  专业：目标专业  |  2026.09"
    pcm.font.size = Pt(13); pcm.font.bold = True; pcm.font.color.rgb = DARK_TEXT; pcm.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # PART 2: 科技蓝 / 墨题产品发布开场
    # =========================================================================

    # ── 2.1 Slide 3: 科技扇叶合拢起始态 ──
    s3 = prs.slides.add_slide(blank_layout)

    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill3 = bg3.fill; fill3.gradient()
    s_stop3 = fill3.gradient_stops
    s_stop3[0].color.rgb = TECH_NAVY; s_stop3[0].position = 0.0
    s_stop3[1].color.rgb = TECH_BLUE; s_stop3[1].position = 1.0
    fill3.gradient_angle = 135; bg3.line.fill.background()

    for i in range(6):
        b3 = s3.shapes.add_shape(MSO_SHAPE.PIE, center_x, center_y, blade_diameter, blade_diameter)
        b3.name = f"tech_blade_{i+1}"
        b3.adjustments[0] = 0.0; b3.adjustments[1] = sweep_angle
        b3.rotation = 0.0
        b3.fill.solid(); b3.fill.fore_color.rgb = CYAN if i % 2 == 0 else TEAL
        set_alpha(b3, 75 if i % 2 == 0 else 55)
        b3.line.color.rgb = CYAN; b3.line.width = Pt(1.5)

    tb3 = s3.shapes.add_textbox(Inches(1.5), Inches(-3.0), Inches(10.333), Inches(2.2))
    tb3.name = "tech_title_box"
    tf3 = tb3.text_frame
    p3 = tf3.paragraphs[0]; p3.text = "MOTIX · 墨题"
    p3.font.size = Pt(40); p3.font.bold = True; p3.font.color.rgb = CYAN; p3.alignment = PP_ALIGN.CENTER

    # ── 2.2 Slide 4: 科技扇叶展开终态 ──
    s4 = prs.slides.add_slide(blank_layout)
    add_morph_transition(s4)

    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill4 = bg4.fill; fill4.gradient()
    s_stop4 = fill4.gradient_stops
    s_stop4[0].color.rgb = TECH_NAVY; s_stop4[0].position = 0.0
    s_stop4[1].color.rgb = TECH_BLUE; s_stop4[1].position = 1.0
    fill4.gradient_angle = 135; bg4.line.fill.background()

    for i, angle in enumerate(blade_angles):
        b4 = s4.shapes.add_shape(MSO_SHAPE.PIE, center_x, center_y, blade_diameter, blade_diameter)
        b4.name = f"tech_blade_{i+1}"
        b4.adjustments[0] = 0.0; b4.adjustments[1] = sweep_angle
        b4.rotation = float(angle)
        b4.fill.solid(); b4.fill.fore_color.rgb = CYAN if i % 2 == 0 else TEAL
        set_alpha(b4, 75 if i % 2 == 0 else 55)
        b4.line.color.rgb = CYAN; b4.line.width = Pt(1.5)

    core_tech = s4.shapes.add_shape(MSO_SHAPE.OVAL, center_x + Inches(2.2), center_y + Inches(2.2), Inches(2.4), Inches(2.4))
    core_tech.name = "core_tech"
    core_tech.fill.solid(); core_tech.fill.fore_color.rgb = TECH_NAVY
    core_tech.line.color.rgb = CYAN; core_tech.line.width = Pt(2.0)
    p_ct = core_tech.text_frame.paragraphs[0]; p_ct.text = "AI"
    p_ct.font.size = Pt(24); p_ct.font.bold = True; p_ct.font.color.rgb = CYAN; p_ct.alignment = PP_ALIGN.CENTER

    tb4 = s4.shapes.add_textbox(Inches(1.5), Inches(0.8), Inches(10.333), Inches(2.2))
    tb4.name = "tech_title_box"
    tf4 = tb4.text_frame
    p4 = tf4.paragraphs[0]; p4.text = "MOTIX · 墨题智能刷题机"
    p4.font.size = Pt(36); p4.font.bold = True; p4.font.color.rgb = CYAN; p4.alignment = PP_ALIGN.CENTER
    p4_sub = tf4.add_paragraph(); p4_sub.text = "离线优先 · 真题切片 · 沉浸式水墨交互"
    p4_sub.font.size = Pt(18); p4_sub.font.color.rgb = WHITE; p4_sub.alignment = PP_ALIGN.CENTER

    out_file = os.path.join(out_dir, "Fan_Blade_Opening_Showcase.pptx")
    prs.save(out_file)
    print(f"✅ 成功生成扇叶开场平滑动画 PPT: {out_file}")
    return out_file


if __name__ == "__main__":
    build_fan_blade_presentation()
