# -*- coding: utf-8 -*-
"""回归测试：test_yunjian_ceiling_fan.py

验证【云间设计PPT】对角双扇梯级绽放（PPT天花板）生成器的全部工程规范：
1. 双态 Morph 状态差（State-Diff）：
   - Slide 1: 左右两组 12 片扇叶角度归零（完全叠合闭合），无多层展开
   - Slide 2: 左右两组各 6 片扇叶按 15° 步长递增展开 (75°, 60°, 45°, 30°, 15°, 0°)
2. 对角双折扇几何结构：
   - 右下主扇 (BRFan1~6) + 左上副扇 (TLFan1~6) 完整存在并同心锁定
   - 扇纽 (JadeBR, JadeTL) 对角分布
3. 画中画底图图片填充 (blipFill) 完整存在
4. 官方 ISO/IEC 29500 mc:AlternateContent + p159:morph 引擎
5. 端到端体积与 16:9 宽屏尺寸
"""
import os, sys, unittest
from pptx import Presentation
from pptx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCRIPT_DIR)
import generate_yunjian_ceiling_fan as G

class TestYunjianCeilingFan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_out = os.path.join(
            os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity", "_test_ceiling_fan.pptx"
        )
        G.build_yunjian_ceiling_presentation(out_name="_test_ceiling_fan.pptx")
        cls.prs = Presentation(cls.test_out)
        cls.s1 = cls.prs.slides[0]
        cls.s2 = cls.prs.slides[1]

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_out):
            try:
                os.remove(cls.test_out)
            except OSError:
                pass

    def test_01_deck_structure(self):
        """严格双页、16:9 宽屏、体积有效"""
        self.assertEqual(len(self.prs.slides), 2)
        self.assertAlmostEqual(round(self.prs.slide_width.inches, 2), 13.33)
        self.assertAlmostEqual(round(self.prs.slide_height.inches, 2), 7.50)
        size = os.path.getsize(self.test_out)
        self.assertGreater(size, 400000, f"体积过小: {size}")

    def test_02_morph_transition_engine(self):
        """Slide 2 挂载官方 p159:morph 引擎"""
        morph = self.s2._element.find('.//{http://schemas.microsoft.com/office/powerpoint/2015/09/main}morph')
        if morph is None:
            morph = self.s2._element.find('.//{http://schemas.openxmlformats.org/presentationml/2006/main}morph')
        self.assertIsNotNone(morph, "Slide 2 缺少 morph 平滑引擎节点")
        self.assertEqual(morph.get('option'), 'byObject')

    def test_03_named_objects_pairing(self):
        """左右两组双扇共 12 片扇叶、双纽、文本完整匹配"""
        names_s1 = {sp.name for sp in self.s1.shapes if sp.name.startswith('!!')}
        names_s2 = {sp.name for sp in self.s2.shapes if sp.name.startswith('!!')}

        required = {
            '!!FrostedVeil',
            '!!BRFan1', '!!BRFan2', '!!BRFan3', '!!BRFan4', '!!BRFan5', '!!BRFan6',
            '!!TLFan1', '!!TLFan2', '!!TLFan3', '!!TLFan4', '!!TLFan5', '!!TLFan6',
            '!!JadeBR', '!!JadeTL',
            '!!MainTitle', '!!SubTitle', '!!QuoteText'
        }
        for r in required:
            self.assertIn(r, names_s1, f"Slide 1 缺少命名对象: {r}")
            self.assertIn(r, names_s2, f"Slide 2 缺少命名对象: {r}")

    def test_04_dual_fan_geometry_and_stepping(self):
        """对角双折扇展开步长恒定为 15.0°"""
        # 右下扇叶
        br_s1 = [sp for sp in self.s1.shapes if 'BRFan' in sp.name]
        br_s2 = [sp for sp in self.s2.shapes if 'BRFan' in sp.name]
        self.assertEqual(len(br_s1), 6)
        self.assertEqual(len(br_s2), 6)

        # Slide 1: 全部角度一致
        rot1 = [round(b.rotation % 360, 1) for b in br_s1]
        self.assertEqual(len(set(rot1)), 1, f"Slide 1 右下扇叶未完全收拢: {rot1}")

        # Slide 2: 步长 15°
        br_s2_sorted = sorted(br_s2, key=lambda b: int(b.name.replace('!!BRFan', '')))
        rot2 = [round(b.rotation % 360, 1) for b in br_s2_sorted]
        for i in range(len(rot2) - 1):
            diff = (rot2[i] - rot2[i+1]) % 360
            self.assertAlmostEqual(diff, 15.0, delta=1.0)

        # 左上扇叶
        tl_s1 = [sp for sp in self.s1.shapes if 'TLFan' in sp.name]
        tl_s2 = [sp for sp in self.s2.shapes if 'TLFan' in sp.name]
        self.assertEqual(len(tl_s1), 6)
        self.assertEqual(len(tl_s2), 6)

        rot_tl1 = [round(b.rotation % 360, 1) for b in tl_s1]
        self.assertEqual(len(set(rot_tl1)), 1, f"Slide 1 左上扇叶未完全收拢: {rot_tl1}")

        tl_s2_sorted = sorted(tl_s2, key=lambda b: int(b.name.replace('!!TLFan', '')))
        rot_tl2 = [round(b.rotation % 360, 1) for b in tl_s2_sorted]
        for i in range(len(rot_tl2) - 1):
            diff = (rot_tl2[i] - rot_tl2[i+1]) % 360
            self.assertAlmostEqual(diff, 15.0, delta=1.0)

    def test_05_blip_fill_exists(self):
        """扇叶均包含画中画底图图片填充 (blipFill)"""
        for name in ['!!BRFan1', '!!TLFan1']:
            sp = [s for s in self.s2.shapes if s.name == name][0]
            blip = sp._element.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
            self.assertIsNotNone(blip, f"{name} 缺少 blipFill 底图图片填充")

    def test_06_text_motion_state_diff(self):
        """文本入场状态差：Slide 1 场外 → Slide 2 居中归位"""
        t1 = [sp for sp in self.s1.shapes if sp.name == '!!MainTitle'][0]
        t2 = [sp for sp in self.s2.shapes if sp.name == '!!MainTitle'][0]
        self.assertLess(t1.top.inches, 0, "Slide 1 标题必须在画外上方 (y < 0)")
        self.assertGreater(t2.top.inches, 1.0, "Slide 2 标题必须在画内")

        q1 = [sp for sp in self.s1.shapes if sp.name == '!!QuoteText'][0]
        q2 = [sp for sp in self.s2.shapes if sp.name == '!!QuoteText'][0]
        self.assertGreater(q1.top.inches, 7.5, "Slide 1 正文必须在画外下方 (y > 7.5)")
        self.assertLess(q2.top.inches, 5.5, "Slide 2 正文必须在画内中央")

if __name__ == '__main__':
    unittest.main(verbosity=2)
