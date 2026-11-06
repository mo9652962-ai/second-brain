# -*- coding: utf-8 -*-
"""把 9 页预览图拼成一张 3x3 联系表，便于一次性视觉验收"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(HERE), "preview_ending")
OUT = os.path.join(D, "contact_sheet.png")
files = [os.path.join(D, "page_%02d.png" % i) for i in range(9)]
ims = [Image.open(f).convert("RGB") for f in files]
w, h = ims[0].size
tw, th = w // 2, h // 2
sheet = Image.new("RGB", (tw * 3 + 40, th * 3 + 40), (245, 246, 248))
d = ImageDraw.Draw(sheet)
for i, im in enumerate(ims):
    im = im.resize((tw, th), Image.LANCZOS)
    x = (i % 3) * (tw + 10) + 10
    y = (i // 3) * (th + 10) + 10
    sheet.paste(im, (x, y))
    d.rectangle([x, y, x + tw, y + th], outline=(200, 205, 212), width=2)
    d.text((x + 6, y + 6), "#%d" % i, fill=(255, 60, 60))
sheet.save(OUT)
print(OUT, sheet.size)
