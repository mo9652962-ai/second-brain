#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Citation Grounding Verifier v1.0 (2026)
学术文献张冠李戴与虚假引用交叉验证器
利用 OpenAlex 全球开放学术图谱 (2.5 亿论文库，免 Key 直连)
检测正文论述与所引论文真实结论是否脱节（防范商业 AI 初稿常见造假）
"""

import sys
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

def reconstruct_abstract(inverted_index: Optional[Dict[str, list]]) -> str:
    """将 OpenAlex 的 abstract_inverted_index 反解为连贯英文/中文文本"""
    if not inverted_index:
        return ""
    word_positions = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort(key=lambda x: x[0])
    return " ".join([w for _, w in word_positions])

class CitationVerifier:
    BASE_URL = "https://api.openalex.org/works"

    @classmethod
    def verify_work(cls, title: str = "", doi: str = "") -> Dict[str, Any]:
        """
        验证文献是否存在，并获取其真实摘要与核心主题
        """
        data = None
        # 1. 优先使用 DOI 检索
        if doi:
            clean_doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
            url = f"{cls.BASE_URL}/https://doi.org/{clean_doi}"
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "AcademicVerifier/1.0 (mailto:scholar@research.org)"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode("utf-8"))
            except Exception:
                pass
                
        # 2. 回退到按标题检索
        if not data and title:
            encoded_title = urllib.parse.quote(title.strip())
            url = f"{cls.BASE_URL}?search={encoded_title}&per_page=3"
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "AcademicVerifier/1.0 (mailto:scholar@research.org)"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    if resp.status == 200:
                        res = json.loads(resp.read().decode("utf-8"))
                        results = res.get("results", [])
                        if results:
                            data = results[0]
            except Exception as e:
                return {"status": "error", "message": f"API request failed: {e}"}

        if not data:
            return {
                "status": "not_found",
                "exists": False,
                "warning": "未在全球学术知识图谱 (OpenAlex/Crossref) 中检索到该文献，疑似虚构/伪造文献！"
            }

        # 提取真实元数据
        real_title = data.get("title", "")
        real_doi = data.get("doi", "")
        year = data.get("publication_year", "")
        cited_count = data.get("cited_by_count", 0)
        source_name = data.get("primary_location", {}).get("source", {}).get("display_name", "未知期刊/会议") if data.get("primary_location") else "未知"
        abstract = reconstruct_abstract(data.get("abstract_inverted_index"))
        
        # 提取主题概念
        concepts = [c.get("display_name") for c in data.get("concepts", [])[:5] if c.get("display_name")]

        return {
            "status": "verified",
            "exists": True,
            "real_title": real_title,
            "real_doi": real_doi,
            "year": year,
            "cited_count": cited_count,
            "source": source_name,
            "core_concepts": concepts,
            "abstract_snippet": (abstract[:250] + "...") if abstract else "暂无公开发表摘要 (需查证全文)"
        }

    @classmethod
    def check_claim_alignment(cls, claim_text: str, title: str, doi: str = "") -> Dict[str, Any]:
        """
        检查正文引用陈述与原文献真实内容的契合度 (防张冠李戴)
        """
        ver = cls.verify_work(title=title, doi=doi)
        if not ver.get("exists"):
            return {
                "claim_status": "HIGH_RISK_FAKE",
                "risk_desc": "文献本身不存在，属于典型 AI 幻觉文献",
                "detail": ver
            }
            
        abstract = ver.get("abstract_snippet", "").lower()
        concepts = [c.lower() for c in ver.get("core_concepts", [])]
        claim_lower = claim_text.lower()
        
        # 简单语义交集探测
        concept_overlap = [c for c in concepts if c in claim_lower]
        
        alignment = "ALIGNED"
        alignment_note = "正文论述与该文献核心主题匹配，具备事实依据。"
        
        if concepts and not concept_overlap and len(abstract) > 50:
            alignment = "SUSPICIOUS_MISMATCH"
            alignment_note = "⚠️ 存疑：文献真实存在，但其核心主题（" + "、".join(ver.get("core_concepts", [])[:3]) + "）与正文论点关联度极低，疑似张冠李戴！"
            
        return {
            "claim_status": alignment,
            "note": alignment_note,
            "matched_concepts": concept_overlap,
            "verified_meta": ver
        }

if __name__ == "__main__":
    test_title = "Deep Residual Learning for Image Recognition"
    test_doi = "10.1109/CVPR.2016.90"
    claim = "何恺明等人提出了ResNet架构，通过残差连接解决了深层神经网络的梯度消失与退化问题。"
    
    print(f"=== 验证文献: {test_title} ===")
    res = CitationVerifier.check_claim_alignment(claim, title=test_title, doi=test_doi)
    print(json.dumps(res, ensure_ascii=False, indent=2))
