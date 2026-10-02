# -*- coding: utf-8 -*-
"""PPT 结尾页设计库生成器 (Ending Slide Library Generator)

来源方法论：抖音「你的 PPT 结尾不应该只有谢谢观看」+ 全网搜索引擎研究（2026-10-02）
核心结论：结尾页是全场停留时间最长的一页（评委提问 5~15 分钟），
        却是 99% 的人唯一不做设计的一页 —— 这是纯粹的浪费。

产出：一个 .pptx，含 1 页反例 + 8 种可直接复用的结尾页版式（原生可编辑 + 真实动效 + 真二维码）

五层架构：
  1. 配置层  CONFIG          —— 尺寸/配色/文案/字体，全部集中可改
  2. 工具层  tools_*         —— 渐变背景、光晕、暗角、二维码、镂空面板、动效注入
  3. 生成层  build_page_*    —— 每种版式一个纯函数，互不干扰（SRP）
  4. 渲染层  render_preview  —— LibreOffice 渲染回图，供视觉验收
  5. 流程层  main()          —— 编排 + 落盘 + 自检报告
"""
import os
import sys
import math
import datetime

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import qrcode

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml

# ============================================================
# 1. 配置层
# ============================================================
W_IN, H_IN = 13.333, 7.5          # 16:9 画布
PX_W, PX_H = 2560, 1440           # 背景图渲染分辨率

HERE = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(HERE, "ending_assets")
OUT_PPTX = os.path.join(os.path.dirname(HERE), "PPT结尾页设计库-2026-10-02.pptx")

FONT_HEI = "C:/Windows/Fonts/SourceHanSansSC-Bold.otf"
FONT_MSYH = "C:/Windows/Fonts/msyh.ttc"
FONT_MSYHBD = "C:/Windows/Fonts/msyhbd.ttc"
FONT_ARIALBD = "C:/Windows/Fonts/arialbd.ttf"

# 演示用真实感元数据（交付时替换成客户自己的）
META = {
    "name": "sora",
    "role": "硬件研发 / AI 自动化",
    "email": "sora.work@example.com",
    "wechat": "sora_ai",
    "brand": "墨题",
    "brand_slogan": "把每一道错题，变成下一次的得分点。",
    "cta_url": "https://example.com/ppt-ending-pack",
    "deck": "2026 年度项目汇报",
    "date": "2026.10",
}

PAGES = []  # (index, name, scene, note)


# ============================================================
# 2. 工具层
# ============================================================
def hx(c):
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def ensure_dir(p):
    os.makedirs(p, exist_ok=True)
    return p


def make_bg(path, top_hex, bot_hex, glow=None, vignette=0.55,
            grid=False, rays=False, grain=False, radial=None):
    """生成一张 16:9 渐变背景（可叠加光晕 / 网格 / 光束 / 颗粒 / 暗角）"""
    top, bot = np.array(hx(top_hex), float), np.array(hx(bot_hex), float)
    t = np.linspace(0, 1, PX_H)[:, None, None]
    img = (top * (1 - t) + bot * t)
    img = np.repeat(img, PX_W, axis=1)

    if radial is not None:
        cx, cy, rad, col, amt = radial
        yy, xx = np.mgrid[0:PX_H, 0:PX_W]
        d = np.sqrt(((xx - cx * PX_W) / (rad * PX_W)) ** 2 + ((yy - cy * PX_H) / (rad * PX_W)) ** 2)
        m = np.clip(1 - d, 0, 1)[:, :, None] ** 2 * amt
        img = img * (1 - m) + np.array(col, float) * m

    if glow is not None:
        cx, cy, rad, col, amt = glow
        yy, xx = np.mgrid[0:PX_H, 0:PX_W]
        d = np.sqrt(((xx - cx * PX_W) / (rad * PX_W)) ** 2 + ((yy - cy * PX_H) / (rad * PX_W)) ** 2)
        m = np.clip(1 - d, 0, 1)[:, :, None] ** 2.2 * amt
        img = img * (1 - m) + np.array(col, float) * m

    img = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")

    if rays:
        lay = Image.new("L", (PX_W, PX_H), 0)
        d = ImageDraw.Draw(lay)
        for i in range(14):
            ang = math.radians(-78 + i * 5.4)
            x2 = PX_W * 0.5 + math.cos(ang) * PX_H * 2.1
            y2 = PX_H * 0.02 + math.sin(ang) * PX_H * 2.1
            d.polygon([(PX_W * 0.5, PX_H * 0.02), (x2, y2), (x2 + 90, y2)], fill=26)
        lay = lay.filter(ImageFilter.GaussianBlur(38))
        img = Image.composite(Image.new("RGB", img.size, (210, 225, 255)), img, lay)

    if grid:
        lay = Image.new("L", (PX_W, PX_H), 0)
        d = ImageDraw.Draw(lay)
        for x in range(0, PX_W, 128):
            d.line([(x, 0), (x, PX_H)], fill=22, width=2)
        for y in range(0, PX_H, 128):
            d.line([(0, y), (PX_W, y)], fill=22, width=2)
        img = Image.composite(Image.new("RGB", img.size, (120, 190, 255)), img, lay)

    if vignette > 0:
        yy, xx = np.mgrid[0:PX_H, 0:PX_W]
        r = np.sqrt(((xx - PX_W / 2) / (PX_W / 2)) ** 2 + ((yy - PX_H / 2) / (PX_H / 2)) ** 2)
        v = np.clip((r - 0.55) / 0.75, 0, 1)[:, :, None] ** 1.7 * vignette
        arr = np.asarray(img, float) * (1 - v)
        img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

    if grain:
        n = np.random.default_rng(7).normal(0, 3.2, (PX_H, PX_W, 1))
        arr = np.asarray(img, float) + np.repeat(n, 3, axis=2)
        img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")

    img.save(path, quality=94)
    return path


def make_qr(path, text, box=760):
    q = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M,
                      box_size=12, border=2)
    q.add_data(text)
    q.make(fit=True)
    img = q.make_image(fill_color="#101418", back_color="white").convert("RGB")
    img = img.resize((box, box), Image.NEAREST)
    img.save(path)
    return path


def make_hollow_panel(path, shape="s_curve", fill=(0, 0, 0), alpha=0.32,
                      text="致 谢", font_path=FONT_HEI, font_px=330,
                      text_pos=(0.16, 0.30), shadow=True):
    """半透明有机流线面板 + 文字负空间镂空（文字处 100% 透明，透出底层原图）"""
    base = Image.new("RGBA", (PX_W, PX_H), (0, 0, 0, 0))
    mask = Image.new("L", (PX_W, PX_H), 0)
    d = ImageDraw.Draw(mask)

    if shape == "s_curve":
        pts = [(0, 0), (int(PX_W * 0.60), 0)]
        for i in range(0, 121):
            u = i / 120
            x = PX_W * (0.60 - 0.085 * math.sin(u * math.pi))
            y = PX_H * u
            pts.append((int(x), int(y)))
        pts += [(int(PX_W * 0.60), PX_H), (0, PX_H)]
        d.polygon(pts, fill=255)

    d.text(text_pos and (int(text_pos[0] * PX_W), int(text_pos[1] * PX_H)),
           text, font=ImageFont.truetype(font_path, font_px), fill=0, anchor="la")

    if shadow:
        sh = mask.filter(ImageFilter.GaussianBlur(26)).point(lambda v: int(v * 0.55))
        off = Image.new("L", mask.size, 0)
        off.paste(sh, (14, 18))
        base.paste(Image.new("RGBA", mask.size, (0, 0, 0, 110)), (0, 0), off)

    base.paste(Image.new("RGBA", mask.size, fill + (int(alpha * 255),)), (0, 0), mask)
    base.save(path)
    return path


def set_alpha(shape, pct):
    """设置形状纯色填充的透明度（0-100 表示不透明度百分比 0=全透）"""
    sF = shape.fill._xPr.find(qn("a:solidFill"))
    if sF is not None:
        clr = sF.find(qn("a:srgbClr"))
        if clr is not None:
            for ch in list(clr):
                if ch.tag == qn("a:alpha"):
                    clr.remove(ch)
            clr.append(parse_xml('<a:alpha xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" val="%d"/>' % int(pct * 1000)))


def set_run_font(run, name, size=None, bold=None, color=None, spc=None):
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:ea", "a:cs"):
        for el in rPr.findall(qn(tag)):
            rPr.remove(el)
    rPr.append(parse_xml('<a:ea xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" typeface="%s"/>' % name))
    rPr.append(parse_xml('<a:cs xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" typeface="%s"/>' % name))
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if color is not None:
        run.font.color.rgb = RGBColor(*color)
    if spc is not None:
        rPr.set("spc", str(int(spc * 100)))


def add_text(slide, l, t, w, h, lines, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
             line_spacing=1.0, space_after=0):
    """lines: [ (text, font_name, size_pt, bold, color_tuple, spc_pt or None), ... ]"""
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, item in enumerate(lines):
        txt, fname, size, bold, col = item[0], item[1], item[2], item[3], item[4]
        spc = item[5] if len(item) > 5 else None
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        p.space_after = Pt(space_after)
        r = p.add_run()
        r.text = txt
        set_run_font(r, fname, size, bold, col, spc)
    return tb


def add_rect(slide, l, t, w, h, fill=None, alpha=None, line=None,
             shape=MSO_SHAPE.RECTANGLE, radius=None):
    sh = slide.shapes.add_shape(shape, Inches(l), Inches(t), Inches(w), Inches(h))
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = radius
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = RGBColor(*fill)
        if alpha is not None:
            set_alpha(sh, alpha)
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = RGBColor(*line)
        sh.line.width = Pt(1)
    sh.shadow.inherit = False
    return sh


def add_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


# ---- 原生动效注入（真实 OpenXML p:timing，非静态图） ----
def _anim_group(ids, effects):
    """effects: list of (spid, kind, delay_ms, dur_ms, pct)"""
    inner = []
    eid = ids[0]
    for spid, kind, delay, dur, pct in effects:
        if kind == "zoom":
            inner.append(f'''<p:par><p:cTn id="{eid}" presetID="23" presetClass="emph" presetSubtype="16" fill="hold" grpId="0" nodeType="withEffect">
<p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>
<p:set><p:cBhvr><p:cTn id="{eid+1}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
<p:to><p:strVal val="visible"/></p:to></p:set>
<p:animScale><p:cBhvr><p:cTn id="{eid+2}" dur="{dur}" fill="hold"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr>
<p:by x="{pct*1000}" y="{pct*1000}"/></p:animScale>
</p:childTnLst></p:cTn></p:par>''')
            eid += 3
        else:  # fade in
            inner.append(f'''<p:par><p:cTn id="{eid}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" grpId="0" nodeType="withEffect">
<p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>
<p:set><p:cBhvr><p:cTn id="{eid+1}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>
<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>
<p:to><p:strVal val="visible"/></p:to></p:set>
<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{eid+2}" dur="{dur}"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>
</p:childTnLst></p:cTn></p:par>''')
            eid += 3
    return "".join(inner), eid


def add_motion(slide, effects, start_id=40):
    """effects: [(shape, 'zoom'|'fade', delay_ms, dur_ms, pct)] —— 进入幻灯片即自动播放"""
    items = []
    for shape, kind, delay, dur, pct in effects:
        spid = shape.shape_id
        items.append((spid, kind, delay, dur, pct))
    body, nxt = _anim_group([start_id], items)
    xml = f'''<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>
<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>
<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>
{body}
</p:childTnLst></p:cTn></p:par>
</p:childTnLst></p:cTn>
<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>
<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>
</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>'''
    slide._element.append(parse_xml(xml))


def new_deck():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W_IN), Inches(H_IN)
    return prs


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def full_bg(slide, img):
    return slide.shapes.add_picture(img, 0, 0, width=Inches(W_IN), height=Inches(H_IN))


# ============================================================
# 3. 生成层 —— 每种版式一个纯函数
# ============================================================
GOLD = (214, 178, 110)
DARK = (24, 27, 33)
WHITE = (255, 255, 255)


def page_00_bad(prs, A):
    """反例：谢谢观看（对比基准，不推荐交付）"""
    s = blank(prs)
    full_bg(s, A["bg_bad"])
    add_text(s, 0, 3.1, W_IN, 1.4, [("谢谢观看", FONT_MSYHBD, 60, True, (46, 52, 62))],
             align=PP_ALIGN.CENTER)
    add_text(s, 0, 4.35, W_IN, 0.6, [("THANKS FOR WATCHING", FONT_ARIALBD, 16, False, (150, 158, 170), 4)],
             align=PP_ALIGN.CENTER)
    add_notes(s, "反例页：信息量为零、无记忆点、无行动指引。它唯一的作用是提醒观众「终于结束了」。\n"
                 "观众记住的是最后看到的东西（近因效应）——你把最高价值的广告位用来贴了一张白纸。")
    PAGES.append((0, "谢谢观看（反例）", "任何场合都不推荐", "对比基准：为什么必须改"))


def page_01_boomerang(prs, A):
    """方案一：核心信息回旋镖 —— 开场那句话，最后一页再说一遍"""
    s = blank(prs)
    full_bg(s, A["bg_boomerang"])
    add_text(s, 1.1, 1.35, 11, 0.4, [("开场  ·  第 2 页", FONT_MSYH, 14, False, (146, 158, 176), 3)])
    add_text(s, 1.1, 1.85, 11, 0.9, [("“我们今年只做一件事——把交付准时率从 62% 拉到 95%。”",
                                     FONT_MSYH, 26, False, (188, 197, 210))])
    bar = add_rect(s, 1.12, 3.05, 1.5, 0.045, fill=GOLD)
    big = add_text(s, 1.1, 3.45, 11.2, 1.6, [("交付准时率  95%", FONT_HEI, 66, True, WHITE)])
    add_text(s, 1.1, 5.15, 11, 0.5, [("已经做到  ·  下一个 12 个月，我们守住它", FONT_MSYH, 20, False, GOLD)])
    add_text(s, 1.1, 6.55, 11, 0.4, [("2026 年度项目汇报   |   sora   |   2026.10",
                                     FONT_MSYH, 12, False, (120, 132, 150))])
    add_motion(s, [(bar, "fade", 0, 700, 0), (big, "fade", 350, 800, 0)])
    add_notes(s, "回旋镖结构：开场抛出的那句话，在最后一页原封不动弹回来。\n"
                 "心理机制 = 首因效应 + 近因效应叠加，记忆强度翻倍。\n"
                 "适用：年会、年度汇报、复盘会。文案铁律：必须和开场一模一样，一个字都别改。")
    PAGES.append((1, "核心信息回旋镖", "年会 / 年度汇报 / 复盘", "开场金句在结尾原样弹回，首因+近因双杀"))


def page_02_cta(prs, A):
    """方案二：行动号召 —— 只给一个动作"""
    s = blank(prs)
    full_bg(s, A["bg_cta"])
    add_text(s, 1.0, 1.5, 7.6, 1.0, [("下一步", FONT_MSYH, 15, False, (120, 200, 190), 5)])
    add_text(s, 1.0, 2.0, 7.6, 1.9,
             [("扫码申请", FONT_HEI, 54, True, WHITE), ("7 天试用", FONT_HEI, 54, True, (94, 226, 208))],
             line_spacing=1.05)
    btn = add_rect(s, 1.02, 4.18, 5.3, 0.9, fill=(28, 32, 40), alpha=90,
                   shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.35)
    add_text(s, 1.35, 4.44, 5.0, 0.5, [("example.com/apply", FONT_ARIALBD, 22, True, (94, 226, 208), 1)])
    add_text(s, 1.0, 5.45, 7.0, 0.9,
             [("名额：本期 20 个  ·  截止：10 月 20 日", FONT_MSYH, 15, False, (176, 186, 200)),
              ("申请后 48 小时内回复", FONT_MSYH, 15, False, (176, 186, 200))], line_spacing=1.5)
    add_rect(s, 9.72, 1.87, 2.72, 2.72, fill=WHITE, alpha=100,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
    s.shapes.add_picture(A["qr"], Inches(10.00), Inches(2.15), height=Inches(2.16))
    add_text(s, 9.72, 4.72, 2.72, 0.4, [("微信扫码", FONT_MSYH, 14, False, (206, 216, 228))], align=PP_ALIGN.CENTER)
    add_motion(s, [(btn, "fade", 0, 600, 0)])
    add_notes(s, "CTA 铁律：一页只有一个动作。给两个选项 = 让观众做选择 = 大多数人不选。\n"
                 "必须写清三件事：做什么、门槛多低（扫码）、什么时候截止（稀缺感）。\n"
                 "适用：销售提案、招商、内测招募、活动报名。")
    PAGES.append((2, "行动号召 CTA", "销售 / 招商 / 招募", "一个动作 + 二维码 + 截止时间"))


def page_03_contact(prs, A):
    """方案三：联系方式卡片 —— 分栏，左情绪右信息"""
    s = blank(prs)
    full_bg(s, A["bg_contact"])
    add_text(s, 0.95, 2.55, 6.0, 1.4, [("有技术问题，", FONT_HEI, 40, True, WHITE),
                                       ("随时找我。", FONT_HEI, 40, True, GOLD)], line_spacing=1.15)
    add_text(s, 0.95, 4.5, 6.0, 0.5, [("硬件研发 / AI 自动化 / 工业软件", FONT_MSYH, 16, False, (186, 196, 210))])
    card = add_rect(s, 7.15, 1.55, 5.2, 4.4, fill=WHITE, alpha=7,
                    shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    rows = [("姓　名", META["name"]), ("领　域", META["role"]),
            ("邮　箱", META["email"]), ("微　信", META["wechat"])]
    for i, (k, v) in enumerate(rows):
        y = 2.15 + i * 0.92
        add_text(s, 7.75, y, 1.4, 0.4, [(k, FONT_MSYH, 13, False, (150, 160, 176))])
        add_text(s, 9.15, y - 0.04, 3.1, 0.45, [(v, FONT_MSYHBD, 19, True, (38, 44, 54))])
    for i in range(3):
        add_rect(s, 7.75, 3.05 + i * 0.92, 4.0, 0.012, fill=(220, 226, 234))
    add_text(s, 7.75, 5.15, 4.2, 0.4, [("微信扫码   ·   直接加我", FONT_MSYH, 13, False, (170, 180, 196))])
    s.shapes.add_picture(A["qr"], Inches(10.72), Inches(4.86), height=Inches(0.95))
    add_motion(s, [(card, "fade", 0, 700, 0)])
    add_notes(s, "分栏法：左边给情绪（一句人话），右边给信息（可抄走的数据）。\n"
                 "把联系方式放在结尾页而不是单独一页 —— 观众想起来要联系你的时候，不用往回翻。\n"
                 "适用：求职、商务合作、项目汇报、讲师介绍。")
    PAGES.append((3, "联系方式卡片", "求职 / 合作 / 讲师", "左情绪右信息，联系方式永不丢"))


def page_04_golden(prs, A):
    """方案四：金句页 —— 一句顶一页"""
    s = blank(prs)
    full_bg(s, A["bg_golden"])
    add_text(s, 1.5, 2.15, 10.3, 2.6,
             [("先把问题定义对，", FONT_HEI, 54, True, WHITE),
              ("再谈用什么模型。", FONT_HEI, 54, True, GOLD)], line_spacing=1.12)
    add_rect(s, 1.52, 5.05, 1.35, 0.05, fill=GOLD)
    add_text(s, 1.5, 5.35, 10.3, 0.5, [("sora   ·   2026 年度技术复盘", FONT_MSYH, 15, False, (156, 168, 186), 2)])
    add_motion(s, [(s.shapes[-1], "fade", 0, 900, 0)])
    add_notes(s, "金句页的成功率只有一条判据：这句话能不能被观众原样复述出来。\n"
                 "不能复述的就不是金句，是标语。写作方法：前半句制造反差，后半句给答案。\n"
                 "字体必须够大（>=44pt）且占满版面 —— 金句页排版越简单越高级，不要加装饰。\n"
                 "适用：发布会、竞聘、年终演讲、个人品牌。")
    PAGES.append((4, "金句升华", "发布会 / 竞聘 / 演讲", "一句可被复述的话，撑满整页"))


def page_05_summary(prs, A):
    """方案五：核心要点总结 —— 3 张卡 + 图例"""
    s = blank(prs)
    full_bg(s, A["bg_summary"])
    add_text(s, 0.95, 0.72, 8.0, 0.6, [("今天只讲了三件事", FONT_HEI, 34, True, (32, 40, 52))])
    add_text(s, 0.95, 1.42, 8.0, 0.4, [("带走这三条，比记住整份 PPT 有用", FONT_MSYH, 15, False, (128, 140, 158))])
    cards = [("01", "问题定义先于模型选型", "80% 的失败发生在第一步", GOLD),
             ("02", "数据闭环决定上限", "没有反馈的 Agent 只是脚本", (74, 128, 226)),
             ("03", "交付确定性，不是代码", "客户买的是不出事的承诺", (54, 160, 132))]
    for i, (num, title, sub, col) in enumerate(cards):
        x = 0.95 + i * 3.94
        c = add_rect(s, x, 2.35, 3.62, 3.5, fill=WHITE, alpha=100,
                     shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.07)
        add_rect(s, x, 2.35, 3.62, 0.085, fill=col)
        add_text(s, x + 0.42, 2.85, 2.9, 0.9, [(num, FONT_ARIALBD, 40, True, col)])
        add_text(s, x + 0.42, 3.95, 2.9, 1.2, [(title, FONT_MSYHBD, 20, True, (30, 36, 46))], line_spacing=1.25)
        add_text(s, x + 0.42, 5.05, 2.9, 0.6, [(sub, FONT_MSYH, 13, False, (132, 144, 160))])
        add_motion(s, [(c, "fade", i * 220, 620, 0)])
    add_text(s, 0.95, 6.35, 11.4, 0.4, [("完整材料与数据附录：example.com/2026-report      |      sora",
                                         FONT_MSYH, 13, False, (128, 140, 158))])
    add_notes(s, "总结页不是目录复读。判断标准：如果只截这一页发出去，别人能不能看懂你的核心结论？\n"
                 "三张卡上限。超过三张，观众一张都记不住。\n"
                 "适用：培训、行业分析、项目复盘、异步交付（别人只看最后一页也能拿走东西）。")
    PAGES.append((5, "核心要点总结", "培训 / 分析 / 复盘", "三张卡，截屏即摘要"))


def page_06_image(prs, A):
    """方案六：全屏影像 + 一个字"""
    s = blank(prs)
    full_bg(s, A["bg_image"])
    add_rect(s, 0, 0, W_IN, H_IN, fill=(8, 10, 16), alpha=38)
    word = add_text(s, 0, 2.55, W_IN, 1.6, [("继续", FONT_HEI, 96, True, WHITE)], align=PP_ALIGN.CENTER)
    add_rect(s, W_IN / 2 - 0.65, 4.45, 1.3, 0.05, fill=GOLD)
    add_text(s, 0, 4.78, W_IN, 0.5, [("技术这件事，值得一直做下去", FONT_MSYH, 18, False, (222, 228, 238), 3)],
             align=PP_ALIGN.CENTER)
    add_motion(s, [(word, "fade", 0, 800, 0)])
    add_notes(s, "沉默的力量：放完全屏图后停 3~5 秒不说话，台下会先安静，然后掌声。\n"
                 "底层图动画建议手动再加一个「强调-放大/缩小 110%」，9 秒缓动 —— 大屏上有极轻微的呼吸感，"
                 "肉眼几乎察觉不到，但质感完全不同。\n"
                 "适用：主题演讲、公益、品牌片尾、答辩致谢。")
    PAGES.append((6, "全屏影像 + 单字", "演讲 / 品牌 / 致谢", "图替你说最后一句，留白即力量"))


def page_07_hollow(prs, A):
    """方案七：负空间流线镂空（红金学术答辩版）"""
    s = blank(prs)
    bg = full_bg(s, A["bg_hollow_red"])
    s.shapes.add_picture(A["panel_red"], 0, 0, width=Inches(W_IN), height=Inches(H_IN))
    add_rect(s, 0.88, 4.18, 6.05, 2.62, fill=(10, 4, 6), alpha=32,
             shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
    add_text(s, 1.05, 4.35, 6.6, 1.1,
             [("恳请各位专家评委批评指正", FONT_MSYHBD, 24, True, (252, 248, 240))])
    add_rect(s, 1.07, 5.42, 1.1, 0.04, fill=GOLD)
    add_text(s, 1.05, 5.65, 6.6, 1.0,
             [("汇报人：sora      指导教师：×××", FONT_MSYH, 16, False, (242, 234, 220)),
              ("2026 年度课题汇报   ·   2026.10", FONT_MSYH, 16, False, (242, 234, 220))], line_spacing=1.6)
    add_text(s, 8.3, 6.5, 4.2, 0.4, [("Q & A", FONT_ARIALBD, 15, False, (230, 202, 148), 6)], align=PP_ALIGN.RIGHT)
    add_motion(s, [(bg, "zoom", 0, 9000, 10)])
    add_notes(s, "致谢页是全场停留时间最长的一页（评委提问 5~15 分钟），绝不能白底黑字。\n"
                 "三层结构：底层暗红鎏金缓动缩放 + 中层 S 型流线毛玻璃 + 顶层文字布尔运算镂空。\n"
                 "镂空文字处 100% 透明，直接透出底层流动金光 —— 文字是「窗」，不是「字」。\n"
                 "适用：学位答辩、国奖/优毕评奖、学术会议。")
    PAGES.append((7, "负空间镂空（红金）", "答辩 / 评奖 / 学术", "镂空透光，评委盯着看也高级"))


def page_08_hollow_tech(prs, A):
    """方案八：负空间镂空（科技商务版）"""
    s = blank(prs)
    bg = full_bg(s, A["bg_hollow_tech"])
    s.shapes.add_picture(A["panel_tech"], 0, 0, width=Inches(W_IN), height=Inches(H_IN))
    add_text(s, 6.15, 4.05, 6.2, 0.9, [("CLOSING", FONT_ARIALBD, 17, True, (150, 176, 208), 6)])
    add_text(s, 6.15, 4.62, 6.2, 1.2,
             [("项目已进入交付期", FONT_HEI, 32, True, WHITE),
              ("欢迎随时找我聊下一步", FONT_HEI, 32, True, (126, 214, 255))], line_spacing=1.18)
    add_rect(s, 6.17, 6.05, 1.1, 0.04, fill=(126, 214, 255))
    add_text(s, 6.15, 6.28, 6.2, 0.5, [("sora   ·   " + META["email"], FONT_MSYH, 14, False, (168, 186, 208))])
    add_motion(s, [(bg, "zoom", 0, 9000, 10)])
    add_notes(s, "同一套镂空结构换成冷色调 + 白色磨砂面板，立刻从学术切换成商业科技风。\n"
                 "面板放右侧，镂空大字压在面板上 —— 大面积留白在左，视觉重心稳定不飘。\n"
                 "适用：企业年终汇报、商业方案交付、客户路演、高客单接单收尾。")
    PAGES.append((8, "负空间镂空（科技）", "商务 / 路演 / 客户交付", "同结构换色，学术秒变商务"))


BUILDERS = [page_00_bad, page_01_boomerang, page_02_cta, page_03_contact,
            page_04_golden, page_05_summary, page_06_image,
            page_07_hollow, page_08_hollow_tech]


# ============================================================
# 5. 流程层
# ============================================================
def build_assets():
    ensure_dir(ASSET_DIR)
    A = {}
    A["bg_bad"] = make_bg(os.path.join(ASSET_DIR, "bg_bad.jpg"), "E9EDF2", "CBD3DD", vignette=0.2)
    A["bg_boomerang"] = make_bg(os.path.join(ASSET_DIR, "bg_boomerang.jpg"), "141821", "080A0E",
                                glow=(0.72, 0.28, 0.62, (120, 62, 30), 0.75), vignette=0.5, grain=True)
    A["bg_cta"] = make_bg(os.path.join(ASSET_DIR, "bg_cta.jpg"), "0B1B22", "050C11",
                          glow=(0.78, 0.30, 0.55, (12, 90, 92), 0.72), vignette=0.45, grain=True)
    A["bg_contact"] = make_bg(os.path.join(ASSET_DIR, "bg_contact.jpg"), "191410", "0B0908",
                              glow=(0.18, 0.72, 0.55, (96, 66, 24), 0.65), vignette=0.5, grain=True)
    A["bg_golden"] = make_bg(os.path.join(ASSET_DIR, "bg_golden.jpg"), "1A1208", "070503",
                             glow=(0.30, 0.42, 0.66, (128, 88, 22), 0.8), vignette=0.55, grain=True)
    A["bg_summary"] = make_bg(os.path.join(ASSET_DIR, "bg_summary.jpg"), "F3F5F8", "E2E7EE",
                              glow=(0.86, 0.12, 0.5, (255, 246, 228), 0.7), vignette=0.15)
    A["bg_image"] = make_bg(os.path.join(ASSET_DIR, "bg_image.jpg"), "101B2B", "04070D",
                            radial=(0.5, 0.42, 0.72, (44, 84, 140), 0.72),
                            rays=True, vignette=0.62, grain=True)
    A["bg_hollow_red"] = make_bg(os.path.join(ASSET_DIR, "bg_hollow_red.jpg"), "4A0C12", "150205",
                                 radial=(0.22, 0.30, 0.55, (176, 108, 40), 0.62),
                                 vignette=0.5, grain=True)
    A["bg_hollow_tech"] = make_bg(os.path.join(ASSET_DIR, "bg_hollow_tech.jpg"), "0C1826", "04080E",
                                  radial=(0.78, 0.34, 0.55, (26, 96, 156), 0.62),
                                  grid=True, vignette=0.5, grain=True)
    A["qr"] = make_qr(os.path.join(ASSET_DIR, "qr.png"), META["cta_url"])
    A["panel_red"] = make_hollow_panel(
        os.path.join(ASSET_DIR, "panel_red.png"), shape="s_curve", fill=(0, 0, 0), alpha=0.30,
        text="致　谢", font_path=FONT_HEI, font_px=300, text_pos=(0.135, 0.175))
    A["panel_tech"] = make_hollow_panel(
        os.path.join(ASSET_DIR, "panel_tech.png"), shape="s_curve", fill=(255, 255, 255), alpha=0.20,
        text="THANK", font_path=FONT_ARIALBD, font_px=250, text_pos=(0.115, 0.20))
    return A


def render_preview(pptx_path, out_dir):
    """LibreOffice 渲染 PDF，供视觉验收（白屏/错位一票否决）"""
    import subprocess
    ensure_dir(out_dir)
    soffice = r"C:\Program Files\LibreOffice\program\soffice.exe"
    if not os.path.exists(soffice):
        return None
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", out_dir, pptx_path],
                   capture_output=True, timeout=420)
    pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(pptx_path))[0] + ".pdf")
    return pdf if os.path.exists(pdf) else None


def main():
    A = build_assets()
    prs = new_deck()
    for fn in BUILDERS:
        fn(prs, A)
    cp = prs.core_properties
    cp.title = "PPT 结尾页设计库"
    cp.author = "sora"
    cp.comments = "8 种结尾页版式 + 1 页反例；原生可编辑 + 真实动效"
    prs.save(OUT_PPTX)
    print("PPTX:", OUT_PPTX, os.path.getsize(OUT_PPTX) // 1024, "KB")

    print("\n%-4s %-20s %-24s %s" % ("#", "版式", "适用场景", "核心机制"))
    for i, name, scene, note in PAGES:
        print("%-4d %-20s %-24s %s" % (i, name, scene, note))

    md = os.path.join(os.path.dirname(HERE), "PPT结尾页设计库-文案对照.md")
    with open(md, "w", encoding="utf-8") as f:
        f.write("# PPT 结尾页设计库 · 版式对照\n\n")
        f.write("> 生成时间：%s ｜ 画布 16:9 ｜ 全部原生可编辑\n\n" % datetime.date.today())
        f.write("| # | 版式 | 适用场景 | 核心机制 |\n|:--|:--|:--|:--|\n")
        for i, name, scene, note in PAGES:
            f.write("| %d | %s | %s | %s |\n" % (i, name, scene, note))
    return OUT_PPTX


if __name__ == "__main__":
    main()
