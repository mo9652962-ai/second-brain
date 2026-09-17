#!/usr/bin/env python3
"""闲鱼主图2-价格表 禁词「最受欢迎」局部修复 v1.0 (2026-09-17)
============================================================
背景：vault-suggestion-executor 6 张主图 vision 禁词复核发现
主图2-价格表.png 与 网站主图2-价格表.png 含「★ 最受欢迎」（禁词「最」，
L2 清单第 120 行）。外部生图 API 全失效，走 PIL 局部重绘兜底：
只替换标签文字像素区域，其余像素 100% 保留（与 gen_xianyu_main_image_safe.py 同思路）。

用法：
    python scripts/fix_xianyu_price_banned_word.py

输出：原位覆盖（已备份到 .temp/），自动 PNG 头 + 尺寸校验。
"""
import os
import shutil
import struct
import sys

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "xianyu-master", "上架素材包")
BACKUP_DIR = os.path.join(os.path.dirname(__file__), "..", ".temp")

FONT_BOLD = r"C:\Windows\Fonts\SourceHanSansSC-Bold.otf"
FONT_EMOJI = r"C:\Windows\Fonts\seguiemj.ttf"

YELLOW_SOFT = (255, 224, 178)   # 高亮卡片底色
ORANGE_DARK = (220, 110, 40)    # 标签文字色（脚本原值）

# (文件名, 标签文字区域, 文字中心 y, 替换文案)
# 区域 = (x0, y0, x1, y1) 覆盖 bbox 略大于文字，含 ★ 与文字
TARGETS = [
    ("主图2-价格表.png",      (290, 405, 440, 450), 427, "★ 人气之选"),
    ("网站主图2-价格表.png",  (285, 495, 445, 540), 517, "★ 人气之选"),
]


def png_header_ok(path):
    try:
        with open(path, "rb") as fh:
            sig = fh.read(8)
            return sig == b"\x89PNG\r\n\x1a\n"
    except Exception:
        return False


def center_text(draw, cx, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2 - bbox[0], y), text, font=font, fill=fill)


def fix(path, region, cy, new_text):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = region
    # 1) 擦除原标签（背景色填充整个 bbox）
    draw.rectangle([x0, y0, x1, y1], fill=YELLOW_SOFT)
    # 2) 重绘「★」+ 新文案：★ 用 emoji 字体，中文用思源黑体，按像素居中
    emoji_font = ImageFont.truetype(FONT_EMOJI, 22)
    cn_font = ImageFont.truetype(FONT_BOLD, 22)
    star_w = draw.textbbox((0, 0), "★", font=emoji_font)[2] - draw.textbbox((0, 0), "★", font=emoji_font)[0]
    cn_w = draw.textbbox((0, 0), new_text.replace("★ ", ""), font=cn_font)[2] - draw.textbbox((0, 0), new_text.replace("★ ", ""), font=cn_font)[0]
    total_w = star_w + 8 + cn_w
    cx = (x0 + x1) / 2
    draw.text((cx - total_w / 2, cy - 16), "★", font=emoji_font, fill=ORANGE_DARK)
    draw.text((cx - total_w / 2 + star_w + 8, cy - 16), new_text.replace("★ ", ""), font=cn_font, fill=ORANGE_DARK)
    # 3) 备份 + 保存
    os.makedirs(BACKUP_DIR, exist_ok=True)
    bak = os.path.join(BACKUP_DIR, os.path.basename(path) + ".bak-20260917")
    if not os.path.exists(bak):
        shutil.copy2(path, bak)
    img.save(path)
    # 4) 校验
    if not png_header_ok(path):
        print(f"❌ {path} PNG 头校验失败")
        return False
    im2 = Image.open(path)
    if im2.size != (w, h):
        print(f"❌ {path} 尺寸变化 {im2.size} != {w}x{h}")
        return False
    print(f"✅ {os.path.basename(path)} 修复完成 ({w}x{h}), 备份: {os.path.basename(bak)}")
    return True


def main():
    ok = True
    for name, region, cy, text in TARGETS:
        path = os.path.join(OUT_DIR, name)
        if not os.path.exists(path):
            print(f"❌ 缺失 {path}")
            ok = False
            continue
        ok = fix(path, region, cy, text) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
