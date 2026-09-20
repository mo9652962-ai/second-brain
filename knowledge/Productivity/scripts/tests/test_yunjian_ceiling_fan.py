# -*- coding: utf-8 -*-
"""回归测试：test_yunjian_ceiling_fan.py（PIE 实心楔形 + 同位窗口 版）

验证【云间设计PPT】对角双扇梯级绽放生成器的全部工程规范：

1. 双态 Morph 状态差（State-Diff）
2. 角落顶点绝对锚定（BR → (13.333,7.5)，TL → (0,0)）
3. 15° 严格等距旋转步长
4. 形状类型必须是 PIE（不完整圆/实心楔形），而非 BLOCK_ARC（空心弧）
   —— 依据标定实验：PIE 内边界 rmin/rmax=0.014，ARC=0.441，原片=0.11
5. 填充必须是「同位窗口」：fillRect 带非零偏移，而非 <a:fillRect/> 全拉伸
   —— 依据对照实验：fillRect 对齐 MAE=27.04 vs 拉伸 55.83
6. 白纱必须位于扇叶之下（z-order），形成「扇内鲜活、扇外朦胧」的正确视差
7. 官方 p159:morph 引擎节点存在
"""
import os, sys, unittest
from pptx import Presentation
from pptx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(SCRIPT_DIR))
import generate_yunjian_ceiling_fan as G

NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
NS_P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
NS_P159 = "{http://schemas.microsoft.com/office/powerpoint/2015/09/main}"

OUT = r"%USERPROFILE%\AppData\Local\Temp\_test_yunjian_pie.pptx"


def build():
    return G.build_yunjian_ceiling_presentation(out_name=os.path.basename(OUT))


class TestYunjianPieCeilingFan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 生成到临时目录
        import shutil
        cls.path = G.build_yunjian_ceiling_presentation(out_name="__tmp_test_pie.pptx")
        cls.prs = Presentation(cls.path)
        cls.s1, cls.s2 = cls.prs.slides[0], cls.prs.slides[1]

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(cls.path)
        except OSError:
            pass

    # ---------- 1. 双态状态差 ----------
    def test_two_slides_exist(self):
        self.assertEqual(len(self.prs.slides), 2)

    def test_state_diff_rotations(self):
        """Slide 1 全部归零收拢；Slide 2 按 15° 梯级展开"""
        def rots(slide, key):
            out = []
            for sp in slide.shapes:
                if key in (sp.name or ""):
                    idx = int(sp.name.replace(f"!!{key}", ""))
                    out.append((idx, round(sp.rotation, 1)))
            return [r for _, r in sorted(out)]
        for key, base in (("BRFan", G.BR_BASE_ROT), ("TLFan", G.TL_BASE_ROT)):
            r1 = rots(self.s1, key)
            r2 = rots(self.s2, key)
            self.assertEqual(len(r1), 6, f"{key} Slide1 应有 6 片")
            self.assertEqual(len(r2), 6, f"{key} Slide2 应有 6 片")
            # Slide 1：全部归零收拢（= base）
            self.assertTrue(all(abs(r - base) < 0.05 for r in r1), f"{key} Slide1 应全部归零: {r1}")
            # Slide 2：按 BLADE_OFFSETS 梯级展开（Fan1 = base+75 → Fan6 = base+0）
            expect = [(base + o) % 360 for o in G.BLADE_OFFSETS]
            for got, exp in zip(r2, expect):
                self.assertAlmostEqual(got % 360, exp % 360, delta=0.05,
                                       msg=f"{key} Slide2 期望 {expect}，实得 {r2}")

    # ---------- 2. 角落顶点绝对锚定 ----------
    def test_corner_anchor_br(self):
        b = [sp for sp in self.s2.shapes if sp.name == "!!BRFan1"][0]
        cx = b.left.inches + b.width.inches / 2
        cy = b.top.inches + b.height.inches / 2
        self.assertAlmostEqual(cx, 13.333, delta=0.05)
        self.assertAlmostEqual(cy, 7.500, delta=0.05)

    def test_corner_anchor_tl(self):
        b = [sp for sp in self.s2.shapes if sp.name == "!!TLFan1"][0]
        cx = b.left.inches + b.width.inches / 2
        cy = b.top.inches + b.height.inches / 2
        self.assertAlmostEqual(cx, 0.0, delta=0.05)
        self.assertAlmostEqual(cy, 0.0, delta=0.05)

    # ---------- 3. 15° 等距步长 ----------
    def test_rotation_step_15deg(self):
        for key in ("BRFan", "TLFan"):
            blades = sorted([sp for sp in self.s2.shapes if key in (sp.name or "")],
                            key=lambda s: int(s.name.replace(f"!!{key}", "")))
            rots = [b.rotation % 360 for b in blades]
            steps = [(rots[i] - rots[i + 1]) % 360 for i in range(len(rots) - 1)]
            for s in steps:
                self.assertAlmostEqual(s, 15.0, delta=0.5, msg=f"{key} 步长异常: {steps}")

    # ---------- 4. 形状必须是 PIE（实心楔形）----------
    def test_shape_is_pie_not_block_arc(self):
        """核心修正：必须是 PIE，不得是 BLOCK_ARC"""
        names = {sp.name for sp in self.s2.shapes if sp.name and "Fan" in sp.name}
        self.assertEqual(len(names), 12, f"应有 12 片扇叶，实得 {len(names)}")
        for sp in self.s2.shapes:
            if sp.name and "Fan" in sp.name:
                prst = sp._element.spPr.find(f"{NS_A}prstGeom")
                self.assertIsNotNone(prst, f"{sp.name} 缺少 prstGeom")
                self.assertEqual(prst.get("prst"), "pie",
                                 f"{sp.name} 应为 pie（实心楔形），实得 {prst.get('prst')}")
                # 不得存在 adj3（BLOCK_ARC 的内径调节点）
                gds = [g.get("name") for g in prst.findall(f"{NS_A}avLst/{NS_A}gd")]
                self.assertNotIn("adj3", gds, f"{sp.name} 不应有 adj3（空心弧参数）")

    def test_pie_span_15deg(self):
        """单叶跨度必须为 15°（PIE adj2 = 9.0 归一化值）"""
        for sp in self.s2.shapes:
            if sp.name and "Fan" in sp.name:
                adj2 = sp.adjustments[1]
                self.assertAlmostEqual(adj2, 9.0, delta=0.1,
                                       msg=f"{sp.name} adj2={adj2} 应为 9.0（=15°）")

    # ---------- 5. 填充必须是同位窗口 ----------
    def test_fill_is_positional_window(self):
        """核心修正：fillRect 必须带非零偏移（同位窗口），而非全拉伸"""
        checked = 0
        for sp in self.s2.shapes:
            if not (sp.name and "Fan" in sp.name):
                continue
            blip = sp._element.spPr.find(f"{NS_A}blipFill")
            self.assertIsNotNone(blip, f"{sp.name} 缺少 blipFill")
            fr = blip.find(f"{NS_A}stretch/{NS_A}fillRect")
            self.assertIsNotNone(fr, f"{sp.name} 缺少 fillRect")
            offsets = [fr.get(k) for k in ("l", "t", "r", "b")]
            nonzero = [o for o in offsets if o is not None and int(o) != 0]
            self.assertTrue(nonzero, f"{sp.name} fillRect 全零 = 拉伸错位，非同位窗口")
            checked += 1
        self.assertEqual(checked, 12)

    # ---------- 6. 白纱层级 ----------
    def test_veil_below_blades(self):
        """白纱必须位于扇叶之下（z-order 更早）"""
        tree = self.s2.shapes._spTree
        order = [e for e in tree if e.tag.endswith("}sp") or e.tag.endswith("}pic")]
        veil_idx = None
        blade_idxs = []
        for i, e in enumerate(order):
            nv = e.find(f"{NS_P}nvSpPr/{NS_P}cNvPr")
            nm = nv.get("name") if nv is not None else ""
            if nm == "!!FrostedVeil":
                veil_idx = i
            elif nm and "Fan" in nm:
                blade_idxs.append(i)
        self.assertIsNotNone(veil_idx, "未找到 !!FrostedVeil 白纱")
        self.assertTrue(blade_idxs, "未找到扇叶")
        self.assertLess(veil_idx, min(blade_idxs),
                        f"白纱(z={veil_idx}) 必须位于所有扇叶之下 (min z={min(blade_idxs)})")

    def test_veil_alpha_80_percent_transparency(self):
        """教程原话「透明度给到 80%」→ alpha = 20%"""
        veil = [sp for sp in self.s2.shapes if sp.name == "!!FrostedVeil"][0]
        alpha = veil._element.spPr.find(f"{NS_A}solidFill/{NS_A}srgbClr/{NS_A}alpha")
        self.assertIsNotNone(alpha, "白纱缺少 alpha")
        self.assertAlmostEqual(int(alpha.get("val")) / 1000.0, 20.0, delta=1.0,
                               msg=f"白纱 alpha={alpha.get('val')} 应为 20000 (20%)")

    # ---------- 7. Morph 引擎 ----------
    def test_morph_engine(self):
        m = self.s2._element.find(f".//{NS_P159}morph")
        self.assertIsNotNone(m, "Slide 2 缺少 p159:morph")
        self.assertEqual(m.get("option"), "byObject")

    # ---------- 8. 阴影方向 ----------
    def test_shadow_dir_135(self):
        """扇叶阴影必须为右下 135°（dir=8100000）"""
        n = 0
        for sp in self.s2.shapes:
            if not (sp.name and "Fan" in sp.name):
                continue
            sh = sp._element.spPr.find(f"{NS_A}effectLst/{NS_A}outerShdw")
            self.assertIsNotNone(sh, f"{sp.name} 缺少外阴影")
            self.assertEqual(sh.get("dir"), "8100000", f"{sp.name} 阴影方向应为 135°")
            n += 1
        self.assertEqual(n, 12)

    # ---------- 9. 扇骨描边标定（v18/v19） ----------
    def test_blade_stroke_width_calibrated(self):
        """扇骨描边必须为 0.15pt（1905 EMU）

        定标依据：v18/v19 变体扫描，视频原片接缝振幅 27.8、宽 1.4px；
        0.15pt 实测振幅 28.86（偏差 3.8%），而原 0.75pt 为 70.54（超标 2.5x）。
        此测试防止参数回退。
        """
        widths = set()
        for sp in self.s2.shapes:
            if not (sp.name and "Fan" in sp.name):
                continue
            ln = sp._element.spPr.find(f"{NS_A}ln")
            self.assertIsNotNone(ln, f"{sp.name} 缺少描边元素")
            widths.add(int(ln.get("w")))
        self.assertEqual(widths, {1905},
                         f"扇骨描边应为 0.15pt (1905 EMU)，实测 {widths}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
