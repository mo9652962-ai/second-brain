#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AIGC Paper Auditor v1.0 (2026)
知网 5.0 / 维普 AIGC 检测算法对抗门禁与学术去 AI 味诊断器
"""

import re
import sys
import os
import math
import json
from typing import Dict, List, Any

HIGH_RISK_ROADSIGNS = [
    "具有重要意义", "具有重要的理论意义和现实意义", "具有深远的现实意义",
    "具有广阔的应用前景", "为...提供了新的思路", "为...提供了重要参考",
    "随着社会的发展", "随着经济的发展", "随着科技的发展", "随着...的快速发展",
    "随着...的深入推进", "随着...的不断深化", "随着时代的进步",
    "众所周知", "毋庸置疑", "不可否认的是", "不难看出", "不言而喻",
    "综上所述", "总而言之", "由上可知", "显而易见", "由此可见",
    "在一定程度上", "在某种意义上", "不可或缺的", "具有里程碑意义"
]

LINEAR_CONNECTORS = ["首先", "其次", "再次", "最后", "第一", "第二", "第三", "第四", "一方面", "另一方面"]

class AIGCPaperAuditor:
    def __init__(self, text: str):
        self.raw_text = text.strip()
        self.paragraphs = [p.strip() for p in self.raw_text.splitlines() if p.strip()]
        self.sentences = self._split_sentences(self.raw_text)
        self.char_count = len(re.sub(r"\s+", "", self.raw_text))

    def _split_sentences(self, text: str) -> List[str]:
        raw = re.split(r"[。！？!?；;\n]+", text)
        return [s.strip() for s in raw if len(s.strip()) > 3]

    def audit_burstiness(self) -> Dict[str, Any]:
        """突发度分析：计算句长均值与标准差"""
        if not self.sentences:
            return {"mean_len": 0, "std_len": 0, "risk": "unknown"}
        lengths = [len(s) for s in self.sentences]
        mean = sum(lengths) / len(lengths)
        variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
        std = math.sqrt(variance)
        
        if std < 2.5:
            risk = "极高 (AI 机械均匀特征，知网高敏)"
        elif std < 8.0:
            risk = "中偏高 (缺乏呼吸感，偏向机器生成)"
        elif std < 10.0:
            risk = "合格 (人类写作中位区间)"
        else:
            risk = "优良 (典型人类忽长忽短特征，AIGC 免疫)"
            
        return {
            "sentence_count": len(self.sentences),
            "mean_length": round(mean, 1),
            "std_length": round(std, 2),
            "risk": risk
        }

    def audit_roadsigns(self) -> Dict[str, Any]:
        """高危套话与路标词密度分析"""
        matched = []
        for word in HIGH_RISK_ROADSIGNS:
            pattern = re.escape(word).replace(r"\.\.\.", r"[\u4e00-\u9fa5A-Za-z0-9_]{1,15}")
            matches = list(re.finditer(pattern, self.raw_text))
            for m in matches:
                matched.append({
                    "word": m.group(0),
                    "pos": m.start()
                })
        
        density_per_kilo = (len(matched) / (self.char_count or 1)) * 1000
        return {
            "total_roadsigns": len(matched),
            "density_per_thousand": round(density_per_kilo, 2),
            "matched_words": [m["word"] for m in matched],
            "benchmark": "人类平均 3.2 个/千字，AI 常见 > 5.8 个/千字"
        }

    def audit_linearity(self) -> Dict[str, Any]:
        """检测段落中线性罗列 (首先/其次/再次/最后)"""
        linear_hits = []
        for i, p in enumerate(self.paragraphs, 1):
            hits = [w for w in LINEAR_CONNECTORS if p.startswith(w) or f"，{w}" in p or f"；{w}" in p]
            if len(hits) >= 2 or any(p.startswith(w) for w in ["首先", "第一"]):
                linear_hits.append({
                    "para_idx": i,
                    "para_sample": p[:50] + "...",
                    "connectors": hits
                })
        return {
            "linear_segments": len(linear_hits),
            "details": linear_hits
        }

    def audit_particle_and_style(self) -> Dict[str, Any]:
        """的字密度与进行+动词机械搭配"""
        de_count = self.raw_text.count("的")
        de_rate = (de_count / (self.char_count or 1)) * 100
        jinxing_matches = re.findall(r"进行(分析|研究|探讨|阐述|总结|归纳|调查|实验|验证|设计)", self.raw_text)
        
        return {
            "de_count": de_count,
            "de_ratio_percent": round(de_rate, 2),
            "de_benchmark": "人类 3-5%，AI 常见 > 6%",
            "jinxing_count": len(jinxing_matches),
            "jinxing_samples": list(set(jinxing_matches))
        }

    def evaluate_score(self) -> Dict[str, Any]:
        """综合加权计算知网 5.0 AIGC 疑似度概率"""
        burst = self.audit_burstiness()
        road = self.audit_roadsigns()
        linear = self.audit_linearity()
        particle = self.audit_particle_and_style()
        
        score = 15.0
        std = burst.get("std_length", 10)
        if std < 2.5:
            score += 35.0
        elif std < 5.0:
            score += 25.0
        elif std < 8.0:
            score += 15.0
        elif std > 12.0:
            score -= 10.0
            
        dens = road.get("density_per_thousand", 0)
        if dens > 6.0:
            score += 30.0
        elif dens > 4.0:
            score += 20.0
        elif dens > 2.0:
            score += 10.0
        elif dens == 0:
            score -= 5.0
            
        score += min(linear.get("linear_segments", 0) * 8.0, 20.0)
        
        if particle.get("de_ratio_percent", 0) > 6.0:
            score += 10.0
        score += min(particle.get("jinxing_count", 0) * 2.0, 10.0)
        
        final_score = max(5.0, min(95.0, round(score, 1)))
        
        if final_score >= 60.0:
            level = "高危 (知网 5.0 / 维普大概率预警或标红)"
        elif final_score >= 35.0:
            level = "疑似 (存在较重机械句式，需重点重构)"
        else:
            level = "安全 (具备清晰的人类写作与非线性论证特征)"
            
        prescriptions = []
        if burst.get("std_length", 10) < 8.0:
            prescriptions.append("【句长重塑】：故意插入 5-10 字短句收尾，将长复合句拆解，拉大句长标准差至 10 以上。")
        if road.get("matched_words"):
            prescriptions.append(f"【路标词清除】：将发现的套话（如 {', '.join(road['matched_words'][:4])}）全部剔除，直接切入核心结论。")
        if linear.get("linear_segments", 0) > 0:
            prescriptions.append("【非线性改写】：消除'首先/其次/最后'递进，改用让步/假设式嵌套论证（如'尽管...但更深层的制约在于...'）。")
        if particle.get("jinxing_count", 0) > 2:
            prescriptions.append("【动词降虚】：将'进行分析'改为直接动词'分析'，'进行探讨'改为'探讨'。")
            
        return {
            "char_count": self.char_count,
            "estimated_aigc_rate": f"{final_score}%",
            "risk_level": level,
            "burstiness": burst,
            "roadsigns": road,
            "linearity": linear,
            "particle_style": particle,
            "prescriptions": prescriptions
        }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.exists(arg):
            with open(arg, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            content = arg
    else:
        content = """
        随着人工智能技术的快速发展，深度学习在各个领域都取得了显著的成果。首先，卷积神经网络在图像处理方面具有重要意义，能够自动提取图像的多层次特征。其次，循环神经网络在自然语言处理中得到了广泛应用，为机器翻译提供了新的思路。最后，强化学习在智能决策中扮演了不可或缺的角色。不可否认的是，人工智能不仅推动了科技的进步，而且为人类社会的生产方式带来了深刻变革。综上所述，加强对人工智能核心算法的研究具有重要的理论意义和现实意义。我们将对相关算法进行深入的分析与探讨。
        """
        print("=== 正在运行内置典型 AI 样本检测 ===")
        
    auditor = AIGCPaperAuditor(content)
    result = auditor.evaluate_score()
    print(json.dumps(result, ensure_ascii=False, indent=2))
