#!/usr/bin/env python3
"""闲鱼 PPT 代做主图生成器 — 3 张主图
图1: 前后对比（5分钟出稿，学术风极简设计）
图2: 价格表（30元起，不满意免费修改）
图3: 服务承诺（当日交付，字体全嵌入）

尺寸: 闲鱼主图 750x750（正方形，3:4 也支持）
字体: 微软雅黑（标题加粗 + 正文常规）
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"C:\Users\31954\.openclaw\workspace\outputs\xianyu-master"
SIZE = 750

FONT_BOLD = r"C:\Windows\Fonts\msyhbd.ttc"   # 微软雅黑粗体
FONT_REG  = r"C:\Windows\Fonts\msyh.ttc"     # 微软雅黑常规

def font_bold(size): return ImageFont.truetype(FONT_BOLD, size)
def font_reg(size):  return ImageFont.truetype(FONT_REG, size)

def new_canvas(bg=(255, 255, 255)):
    img = Image.new("RGB", (SIZE, SIZE), bg)
    return img, ImageDraw.Draw(img)

def rounded_rect(draw, box, radius, fill, outline=None, width=0):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def center_text(draw, cx, y, text, font, fill=(60, 60, 60)):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2, y), text, font=font, fill=fill)

# ============ 图 1：前后对比 ============
def make_before_after():
    img, d = new_canvas((247, 250, 253))
    # 顶部品牌条
    d.rectangle([0, 0, SIZE, 90], fill=(31, 78, 121))
    center_text(d, SIZE/2, 22, "PPT 代做 · 专业设计", font_bold(38), (255, 255, 255))
    center_text(d, SIZE/2, 64, "5 分钟出稿 · 学术风极简设计", font_reg(20), (200, 218, 235))

    # 左右两栏对比
    col_w = 300
    gap = 30
    left_x = 60
    right_x = left_x + col_w + gap
    top_y = 140

    # 左栏（改造前 - 灰）
    rounded_rect(d, [left_x, top_y, left_x + col_w, top_y + 400], 16, (222, 226, 230))
    center_text(d, left_x + col_w/2, top_y + 30, "改造前", font_bold(28), (120, 130, 140))
    center_text(d, left_x + col_w/2, top_y + 90, "✗ 排版混乱", font_reg(24), (160, 160, 160))
    center_text(d, left_x + col_w/2, top_y + 140, "✗ 无设计感", font_reg(24), (160, 160, 160))
    center_text(d, left_x + col_w/2, top_y + 190, "✗ 内容堆砌", font_reg(24), (160, 160, 160))
    center_text(d, left_x + col_w/2, top_y + 240, "✗ 配色杂乱", font_reg(24), (160, 160, 160))

    # 右栏（改造后 - 蓝）
    rounded_rect(d, [right_x, top_y, right_x + col_w, top_y + 400], 16, (214, 232, 250))
    center_text(d, right_x + col_w/2, top_y + 30, "改造后", font_bold(28), (31, 78, 121))
    center_text(d, right_x + col_w/2, top_y + 90, "✓ 极简设计", font_reg(24), (31, 78, 121))
    center_text(d, right_x + col_w/2, top_y + 140, "✓ 逻辑清晰", font_reg(24), (31, 78, 121))
    center_text(d, right_x + col_w/2, top_y + 190, "✓ 图表专业", font_reg(24), (31, 78, 121))
    center_text(d, right_x + col_w/2, top_y + 240, "✓ 配色统一", font_reg(24), (31, 78, 121))

    # 中间箭头
    d.text((SIZE/2 - 20, top_y + 180), "→", font=font_bold(40), fill=(240, 140, 60))

    # 底部 CTA
    rounded_rect(d, [200, 590, 550, 680], 45, (240, 140, 60))
    center_text(d, SIZE/2, 610, "立即咨询 · 免费评估", font_bold(30), (255, 255, 255))
    center_text(d, SIZE/2, 662, "答辩 / 汇报 / 课题申报 全搞定", font_reg(20), (90, 90, 90))
    img.save(os.path.join(OUT_DIR, "主图1-前后对比.png"))
    print("✅ 主图1-前后对比.png")

# ============ 图 2：价格表 ============
def make_price():
    img, d = new_canvas((247, 250, 253))
    # 顶部标题
    d.rectangle([0, 0, SIZE, 100], fill=(31, 78, 121))
    center_text(d, SIZE/2, 22, "透明价格 · 无隐形消费", font_bold(40), (255, 255, 255))
    center_text(d, SIZE/2, 68, "按需报价，不满意免费修改", font_reg(20), (200, 218, 235))

    # 三个价格档
    cards = [
        ("基础美化", "30 元起", "5-8 页 · 当日交付"),
        ("全套制作", "50 元起", "10-15 页 · 次日交付"),
        ("学术答辩", "80 元起", "20 页+ · 协商交付"),
    ]
    card_w = 200
    gap = 22
    start_x = 40
    top_y = 150
    card_h = 330

    for i, (name, price, desc) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        highlight = (i == 1)
        fill = (255, 224, 178) if highlight else (255, 255, 255)
        rounded_rect(d, [x, top_y, x + card_w, top_y + card_h], 16, fill)
        # 名称
        center_text(d, x + card_w/2, top_y + 30, name, font_bold(26), (31, 78, 121) if highlight else (80, 80, 80))
        # 价格
        center_text(d, x + card_w/2, top_y + 110, price, font_bold(36), (230, 100, 50) if highlight else (60, 60, 60))
        # 描述
        center_text(d, x + card_w/2, top_y + 180, desc, font_reg(19), (120, 120, 120))
        if highlight:
            center_text(d, x + card_w/2, top_y + 260, "★ 最受欢迎", font_bold(20), (230, 100, 50))

    # 底部 CTA
    rounded_rect(d, [150, 550, 600, 640], 45, (240, 140, 60))
    center_text(d, SIZE/2, 570, "30 元起 · 不满意免费修改", font_bold(28), (255, 255, 255))
    center_text(d, SIZE/2, 615, "点「我想要」立即估价", font_reg(20), (90, 90, 90))
    img.save(os.path.join(OUT_DIR, "主图2-价格表.png"))
    print("✅ 主图2-价格表.png")

# ============ 图 3：服务承诺 ============
def make_service():
    img, d = new_canvas((247, 250, 253))
    # 顶部标题
    d.rectangle([0, 0, SIZE, 100], fill=(31, 78, 121))
    center_text(d, SIZE/2, 22, "服务承诺 · 放心下单", font_bold(40), (255, 255, 255))
    center_text(d, SIZE/2, 68, "专业 · 高效 · 售后无忧", font_reg(20), (200, 218, 235))

    # 4 个承诺块
    items = [
        ("⚡", "当日交付", "基础版 5-8 页当天完成"),
        ("🔒", "字体全嵌入", "WPS/PPTX 双格式兼容"),
        ("🎨", "高清图片", "商用授权，无水印"),
        ("🔄", "免费修改", "修改至您满意为止"),
    ]
    box_w = 310
    box_h = 170
    gap_x = 24
    gap_y = 24
    start_x = 50
    start_y = 150

    for i, (icon, title, desc) in enumerate(items):
        col = i % 2
        row = i // 2
        x = start_x + col * (box_w + gap_x)
        y = start_y + row * (box_h + gap_y)
        rounded_rect(d, [x, y, x + box_w, y + box_h], 16, (255, 255, 255))
        d.text((x + 25, y + 20), icon, font=font_bold(36))
        d.text((x + 90, y + 28), title, font=font_bold(28), fill=(31, 78, 121))
        center_text(d, x + box_w/2 + 10, y + 100, desc, font_reg(20), (110, 110, 110))

    # 底部 CTA
    rounded_rect(d, [150, 590, 600, 680], 45, (240, 140, 60))
    center_text(d, SIZE/2, 612, "免费评估需求 · 不满意全额退", font_bold(26), (255, 255, 255))
    center_text(d, SIZE/2, 660, "点「我想要」开始定制", font_reg(18), (90, 90, 90))
    img.save(os.path.join(OUT_DIR, "主图3-服务承诺.png"))
    print("✅ 主图3-服务承诺.png")

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    make_before_after()
    make_price()
    make_service()
    print("🎉 全部完成！输出目录:", OUT_DIR)
