# -*- coding: utf-8 -*-
"""渲染验收：pptx → pdf → 逐页 PNG，用于视觉自检（白屏/错位一票否决）"""
import os
import subprocess
import sys

import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
PPTX = os.path.join(os.path.dirname(HERE), "PPT结尾页设计库-2026-10-02.pptx")
OUT = os.path.join(os.path.dirname(HERE), "preview_ending")
SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"


def main():
    os.makedirs(OUT, exist_ok=True)
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", OUT, PPTX],
                   capture_output=True, timeout=600)
    pdf = os.path.join(OUT, os.path.splitext(os.path.basename(PPTX))[0] + ".pdf")
    if not os.path.exists(pdf):
        print("PDF FAILED"); return 1
    doc = fitz.open(pdf)
    print("pages:", doc.page_count)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=110)
        p = os.path.join(OUT, "page_%02d.png" % i)
        pix.save(p)
        # 白屏检测：非白像素占比
        import numpy as np
        arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        lum = arr[:, :, :3].mean(axis=2)
        dark = float((lum < 200).mean())
        print("page %02d  %dx%d  ink=%.3f" % (i, pix.width, pix.height, dark))
    doc.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
