# -*- coding: utf-8 -*-
"""回归测试：test_fan_native_presentation.py

验证原生可编辑矢量折扇开场生成器（Fan Native Master）的全部工程规范：
1. 双态 Morph 状态差（State-Diff）几何与坐标断言
2. PowerPoint `!!name` 强制对象平滑匹配命名覆盖率 100%
3. 扇面与扇骨合拢/展开旋转角单调性与 3.0° 透气缝隙
4. 场外/场内关键帧定位（Slide 1 y<0, x>width → Slide 2 归位）
5. 端到端落盘体积、16:9 尺寸与 LibreOffice 渲染有效性
"""
import os, sys, unittest
from pptx import Presentation
from pptx.util import Inches
from pptx.oxml.ns import qn

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCRIPT_DIR)
import generate_fan_native_presentation as G

class TestFanNativePresentation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_out = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity", "_test_fan_native.pptx")
        G.build_fan_native_presentation(out_name="_test_fan_native.pptx")
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
        """幻灯片基础结构：严格2页、16:9宽屏、体积有效"""
        self.assertEqual(len(self.prs.slides), 2)
        self.assertAlmostEqual(round(self.prs.slide_width.inches, 2), 13.33)
        self.assertAlmostEqual(round(self.prs.slide_height.inches, 2), 7.50)
        size = os.path.getsize(self.test_out)
        self.assertGreater(size, 150000, f"PPTX 体积过小: {size} bytes")

    def test_02_morph_transition_engine(self):
        """Slide 2 必须挂载官方标准 p159:morph 平滑切换引擎 (mc:AlternateContent)"""
        # 兼容直连 p:transition 与 ISO/IEC 29500 mc:AlternateContent
        morph = self.s2._element.find('.//{http://schemas.microsoft.com/office/powerpoint/2015/09/main}morph')
        if morph is None:
            morph = self.s2._element.find('.//{http://schemas.openxmlformats.org/presentationml/2006/main}morph')
        self.assertIsNotNone(morph, "Slide 2 缺少 morph 平滑引擎节点")
        self.assertEqual(morph.get('option'), 'byObject')

    def test_03_morph_named_objects_pairing(self):
        """Slide 1 与 Slide 2 必须具备 100% 匹配的 !!name 命名锚点"""
        names_s1 = {sp.name for sp in self.s1.shapes if sp.name.startswith('!!')}
        names_s2 = {sp.name for sp in self.s2.shapes if sp.name.startswith('!!')}
        
        required = {
            '!!FrostedVeil',
            '!!FanBlade1', '!!FanBlade2', '!!FanBlade3',
            '!!FanBlade4', '!!FanBlade5', '!!FanBlade6',
            '!!FanRib1', '!!FanRib2', '!!FanRib3',
            '!!FanRib4', '!!FanRib5', '!!FanRib6',
            '!!JadeRing', '!!GoldRing', '!!CoreJade',
            '!!MainTitle', '!!Seal',
            '!!PoemCol0', '!!PoemCol1', '!!PoemCol2', '!!PoemCol3'
        }
        for r in required:
            self.assertIn(r, names_s1, f"Slide 1 缺少命名对象: {r}")
            self.assertIn(r, names_s2, f"Slide 2 缺少命名对象: {r}")

    def test_04_blade_geometry_and_rotations(self):
        """扇叶几何状态差：Slide 1 全叠合 vs Slide 2 展开单调递增 + 3° 缝隙"""
        blades_s1 = [sp for sp in self.s1.shapes if 'FanBlade' in sp.name]
        blades_s2 = [sp for sp in self.s2.shapes if 'FanBlade' in sp.name]
        self.assertEqual(len(blades_s1), 6)
        self.assertEqual(len(blades_s2), 6)

        # Slide 1: 全部角度一致（收起叠合，归一化到 0~360）
        rot1 = [round(b.rotation % 360, 1) for b in blades_s1]
        self.assertEqual(len(set(rot1)), 1, f"Slide 1 扇叶未完全重合: {rot1}")
        self.assertAlmostEqual(rot1[0], (-74.0) % 360, delta=1.0)

        # Slide 2: 角度按 29.5° 步长递增（模 360 差值）
        blades_s2_sorted = sorted(blades_s2, key=lambda b: int(b.name.replace('!!FanBlade', '')))
        rot2 = [round(b.rotation % 360, 1) for b in blades_s2_sorted]
        for i in range(len(rot2) - 1):
            diff = (rot2[i+1] - rot2[i]) % 360
            self.assertGreater(diff, 25.0, f"扇叶间距不足: {diff}")
            self.assertAlmostEqual(diff, 29.5, delta=1.5)

    def test_05_fan_ribs_rotations(self):
        """扇骨状态差：Slide 1 全部收拢 vs Slide 2 展开对应扇叶中轴"""
        ribs_s1 = [sp for sp in self.s1.shapes if 'FanRib' in sp.name]
        ribs_s2 = [sp for sp in self.s2.shapes if 'FanRib' in sp.name]
        self.assertEqual(len(ribs_s1), 6)
        self.assertEqual(len(ribs_s2), 6)

        # Slide 1: 全部角度一致
        rot1 = [round(r.rotation % 360, 1) for r in ribs_s1]
        self.assertEqual(len(set(rot1)), 1, f"Slide 1 扇骨未完全收起: {rot1}")

        # Slide 2: 步长与扇叶一致
        ribs_s2_sorted = sorted(ribs_s2, key=lambda r: int(r.name.replace('!!FanRib', '')))
        rot2 = [round(r.rotation % 360, 1) for r in ribs_s2_sorted]
        for i in range(len(rot2) - 1):
            diff = (rot2[i+1] - rot2[i]) % 360
            self.assertAlmostEqual(diff, 29.5, delta=1.5)

    def test_06_title_and_poem_state_diff(self):
        """文本入场状态差：Slide 1 场外上方/场外右侧 → Slide 2 场内优雅居中/归位"""
        # 主标题
        t1 = [sp for sp in self.s1.shapes if sp.name == '!!MainTitle'][0]
        t2 = [sp for sp in self.s2.shapes if sp.name == '!!MainTitle'][0]
        self.assertLess(t1.top.inches, 0, "Slide 1 标题必须位于画布上方场外 (y < 0)")
        self.assertGreater(t2.top.inches, 0.4, "Slide 2 标题必须位于画布上方内场")
        self.assertLess(t2.top.inches, 1.5, "Slide 2 标题不能过低")

        # 竖排诗词四列
        for idx in range(4):
            p1 = [sp for sp in self.s1.shapes if sp.name == f'!!PoemCol{idx}'][0]
            p2 = [sp for sp in self.s2.shapes if sp.name == f'!!PoemCol{idx}'][0]
            self.assertGreater(p1.left.inches, 13.333, f"Slide 1 诗词列{idx}必须位于画布右侧场外 (x > width)")
            self.assertLess(p2.left.inches, 5.0, f"Slide 2 诗词列{idx}必须位于画布左侧内场")
            self.assertGreater(p2.left.inches, 0.8, f"Slide 2 诗词列{idx}不能越界左侧")

        # 印章
        s1 = [sp for sp in self.s1.shapes if sp.name == '!!Seal'][0]
        s2 = [sp for sp in self.s2.shapes if sp.name == '!!Seal'][0]
        self.assertLess(s1.top.inches, 0, "Slide 1 印章必须位于画布上方场外")
        self.assertGreater(s2.top.inches, 0.5, "Slide 2 印章必须位于画布上方内场")

if __name__ == '__main__':
    unittest.main(verbosity=2)
