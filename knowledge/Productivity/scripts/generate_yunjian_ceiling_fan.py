# -*- coding: utf-8 -*-
"""【云间设计PPT】角落锚定式对角双扇梯级绽放（PPT天花板 · 9.8 精修版）

═══════════════════════════════════════════════════════════════════════
【千轮深挖 · 三项决定性修正】（均由像素级对照实验实证，非推测）
═══════════════════════════════════════════════════════════════════════
修正 1 ── 形状：BLOCK_ARC（空心弧）→ PIE（不完整圆 / 实心楔形）
  证据：标定实验 calib_adj.py
        PIE adj=(0,9.0) → 跨度 14.81°，内边界 rmin/rmax = 0.014  ← 匹配原片(11%)
        ARC adj=(0,9.0) → 跨度 14.81°，内边界 rmin/rmax = 0.441  ← 差 4 倍（空心洞）
  教程口播 Whisper 转写的"不规则远"实为「不完整圆」（= PIE，非 BLOCK_ARC）。

修正 2 ── 填充对齐：stretch 拉伸 → fillRect 同位窗口
  证据：verify_window_alignment.py + build_true_window.py
        拉伸铺满：扇内 vs 背景同位 MAE=55.83  相关=+0.4402
        fillRect：扇内 vs 背景同位 MAE=27.04  相关=+0.8160   ← MAE 腰斩、相关翻倍
  教程口播「填充改为幻灯片背景」= 真·同位窗口语义；stretch 会把 16:9 背景
  挤压进 11.6×11.6 方框，导致扇内内容错位。

修正 3 ── 白纱层级：置于扇叶之上 → 置于扇叶之下（背景之上）
  证据：教程口播「插入矩形…右击置于底层」，且透明度「给到 80%」
        置于底层 → 扇内透出 100% 原图（清晰），扇外被 20% 白纱柔化
        → 形成"扇内鲜活、扇外朦胧"的正确视差方向。

═══════════════════════════════════════════════════════════════════════
【几何规格】
  · 右下主扇：圆心锚定画布右下顶点 (13.333, 7.500) in，R = 5.8 in
  · 左上副扇：圆心锚定画布左上顶点 (0.000, 0.000) in，R = 4.8 in
  · 每扇 6 片扇叶，旋转步长恒定 15.0°（75/60/45/30/15/0）
  · 单叶跨度 15.0°（PIE adj2 = 9.0 归一化值），整扇跨度 90.0°
  · 阴影 135° 右下方向（dir=8100000），片片层叠出纸雕纵深
  · 双态 Morph：Slide 1 全部归零收拢 → Slide 2 梯级绽放
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml import parse_xml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BG_DEFAULT_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), "images", "authentic_fan_bg_hd.jpg")

W_IN, H_IN = 13.333, 7.5
STEP_DEG = 15.0
PIE_ADJ2 = STEP_DEG * 0.6          # 15° → 9.0 归一化值
BLADE_OFFSETS = [75.0, 60.0, 45.0, 30.0, 15.0, 0.0]

BR_CX, BR_CY, BR_R = W_IN, H_IN, 5.8
TL_CX, TL_CY, TL_R = 0.0, 0.0, 4.8
BR_BASE_ROT = 180.0                # PIE 默认 [0°,90°]，+180 → [180°,270°] 朝左上
TL_BASE_ROT = 0.0                  # 左上扇朝右下

# fillRect 同位窗口偏移（%），使图像与幻灯片坐标 1:1 对齐
#   l = (0 - box_left) / box_size * 100
#   t = (0 - box_top ) / box_size * 100
#   r = (slide_w - box_right) / box_size * 100
#   b = (slide_h - box_bottom) / box_size * 100
BR_FILLRECT = (-14940, 35345, 0, 0)
TL_FILLRECT = (50000, 50000, -88885, -28125)

VEIL_ALPHA = 20000                 # 教程原话「透明度给到 80%」→ alpha = 20%


def _blip_fill(rid, fr):
    l, t, r, b = fr
    return (f'<a:blipFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" rotWithShape="0">'
            f'<a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid}"/>'
            f'<a:stretch><a:fillRect l="{l}" t="{t}" r="{r}" b="{b}"/></a:stretch></a:blipFill>')


SHADOW_XML = ('<a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
              '<a:outerShdw blurRad="50800" dist="38100" dir="8100000" algn="tl" rotWithShape="0">'
              '<a:srgbClr val="000000"><a:alpha val="25000"/></a:srgbClr></a:outerShdw></a:effectLst>')

MORPH_XML = '''
<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">
  <mc:Choice xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
             xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main" Requires="p159">
    <p:transition spd="med" advClick="1"><p159:morph option="byObject"/></p:transition>
  </mc:Choice>
  <mc:Fallback xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
    <p:transition spd="med" advClick="1"><p:fade/></p:transition>
  </mc:Fallback>
</mc:AlternateContent>
'''


def _add_background(slide, bg_path):
    """铺满底图，返回图片 rId"""
    slide.shapes.add_picture(bg_path, 0, 0, width=Inches(W_IN), height=Inches(H_IN))
    tmp = slide.shapes.add_picture(bg_path, 0, 0, width=Inches(0.4), height=Inches(0.4))
    rid = tmp._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip').get(
        '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
    slide.shapes._spTree.remove(tmp._element)
    return rid


def _add_veil(slide, alpha=VEIL_ALPHA):
    """半透明白纱遮罩（教程步骤：插入矩形 → 背景相似色 → 透明度 80% → 置于底层）"""
    v = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(W_IN), Inches(H_IN))
    v.name = "!!FrostedVeil"
    v.line.fill.background()
    p = v._element.spPr
    for c in list(p):
        if c.tag.endswith("Fill"):
            p.remove(c)
    p.append(parse_xml(f'<a:solidFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
                       f'<a:srgbClr val="F8FAF6"><a:alpha val="{alpha}"/></a:srgbClr></a:solidFill>'))
    return v


def _add_blade(slide, name, cx, cy, R, rot, rid, fr, shadow=True):
    """单片刻面：PIE 实心楔形 + 同位窗口图片填充 + 可选 135° 外阴影"""
    sp = slide.shapes.add_shape(MSO_SHAPE.PIE,
                                Inches(cx - R), Inches(cy - R), Inches(2 * R), Inches(2 * R))
    sp.name = name
    sp.adjustments[0] = 0.0
    sp.adjustments[1] = PIE_ADJ2
    sp.rotation = rot
    sp.line.color.rgb = RGBColor(215, 185, 125)
    sp.line.width = Pt(0.75)
    p = sp._element.spPr
    for c in list(p):
        if c.tag.endswith("Fill"):
            p.remove(c)
    p.append(parse_xml(_blip_fill(rid, fr)))
    if shadow:
        p.append(parse_xml(SHADOW_XML))
    return sp


def _add_text(slide, name, txt, size, color, y, bold=False):
    tb = slide.shapes.add_textbox(Inches(3.2), Inches(y), Inches(7.0), Inches(1.6))
    tb.name = name
    para = tb.text_frame.paragraphs[0]
    para.text = txt
    para.font.size = Pt(size)
    para.font.bold = bold
    para.font.color.rgb = RGBColor(*color)
    para.alignment = PP_ALIGN.CENTER
    return tb


def build_yunjian_ceiling_presentation(
    main_title="春   天   序",
    sub_title="Spring  ·  2026",
    quote_text="当折扇与微风相遇，\n春天便有了具象的模样，\n愿日子清透，万事皆有生机。",
    out_name="Fan_Ceiling_Showcase.pptx",
    bg_path=None,
):
    bg_path = bg_path or BG_DEFAULT_PATH
    if not os.path.exists(bg_path):
        raise FileNotFoundError(f"背景图缺失: {bg_path}")

    prs = Presentation()
    prs.slide_width = Inches(W_IN)
    prs.slide_height = Inches(H_IN)
    blank = prs.slide_layouts[6]
    s1 = prs.slides.add_slide(blank)
    s2 = prs.slides.add_slide(blank)

    rid1 = _add_background(s1, bg_path)
    rid2 = _add_background(s2, bg_path)

    # ── Slide 1：全部扇叶归零收拢（教程步骤 8：角度全改 0、取消阴影、填充改背景）
    for i in range(6):
        _add_blade(s1, f"!!BRFan{i+1}", BR_CX, BR_CY, BR_R, BR_BASE_ROT, rid1, BR_FILLRECT, shadow=False)
        _add_blade(s1, f"!!TLFan{i+1}", TL_CX, TL_CY, TL_R, TL_BASE_ROT, rid1, TL_FILLRECT, shadow=False)

    # ── Slide 2：白纱先入（置于底层），扇叶后入（位于白纱之上 → 透出 100% 原图）
    _add_veil(s2, VEIL_ALPHA)
    for i, off in enumerate(BLADE_OFFSETS):
        _add_blade(s2, f"!!BRFan{i+1}", BR_CX, BR_CY, BR_R, BR_BASE_ROT + off, rid2, BR_FILLRECT, shadow=True)
    for i, off in enumerate(BLADE_OFFSETS):
        _add_blade(s2, f"!!TLFan{i+1}", TL_CX, TL_CY, TL_R, TL_BASE_ROT + off, rid2, TL_FILLRECT, shadow=True)

    _add_text(s2, "!!MainTitle", main_title, 54, (22, 36, 20), 1.9, bold=True)
    _add_text(s2, "!!SubTitle", sub_title, 18, (90, 115, 85), 3.15)
    _add_text(s2, "!!QuoteText", quote_text, 16, (55, 75, 50), 4.05)

    s2._element.append(parse_xml(MORPH_XML))

    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    out_path = os.path.join(out_dir, out_name)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    prs.save(out_path)
    print(f"✅ 生成【云间设计PPT】角落锚定对角双扇天花板 PPT（PIE 实心楔形 + 同位窗口）: {out_path}")
    return out_path


if __name__ == "__main__":
    build_yunjian_ceiling_presentation()
