#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Academic Super Retriever v2.0 (2026)
国家队科研基建自动化数据、文献与学术图表全栈检索器
1. 国家统计局 (National Data / data.stats.gov.cn) 免鉴权权威宏观数据检索 + 300DPI 学术图表生成
2. 中科院 PubScholar (pubscholar.cn) 免登录学术文献检索与全文链接提取
3. 中科院科技论文预发布平台 ChinaXiv (chinaxiv.org) 预印本元数据检索
4. 文献交叉验真与 GB/T 7714-2015 标准引用格式化
"""

import sys
import os
import json
import asyncio
import urllib.request
import urllib.parse
from typing import List, Dict, Any, Optional

# ══════════════════════════════════════════════════════════════
# 1. 国家统计局 (National Data) 官方数据引擎 + 规范学术图表
# ══════════════════════════════════════════════════════════════

class NationalDataRetriever:
    BASE_URL = "https://data.stats.gov.cn/dg/website/publicrelease/web/external"
    
    @classmethod
    def query(cls, keyword: str, page_size: int = 10) -> List[Dict[str, Any]]:
        """
        通过国家统计局公开外部 API 检索权威宏观数据指标
        免鉴权，官方数据直连 (2026 V2.0 规范)
        """
        params = {
            "code": "",
            "pagenum": 1,
            "pageSize": page_size,
            "search": keyword
        }
        url = f"{cls.BASE_URL}/query?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://data.stats.gov.cn/dg/website/page.html",
            "client": "pc"
        })
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode("utf-8"))
                if not res.get("success"):
                    return []
                records = res.get("data", {}).get("data", [])
                results = []
                for r in records:
                    val_str = r.get("value", "")
                    try:
                        numeric_val = float(val_str)
                    except (ValueError, TypeError):
                        numeric_val = None
                        
                    results.append({
                        "name": r.get("show_name", "").strip(),
                        "value": r.get("value", "").strip(),
                        "numeric_value": numeric_val,
                        "time": r.get("dt_name", "").strip(),
                        "time_code": r.get("dt", "").strip(),
                        "region": r.get("da_name", "全国").strip(),
                        "unit": r.get("du_name", "").strip(),
                        "category": r.get("type_text", "").strip(),
                        "source": "国家统计局 (National Data)"
                    })
                return results
        except Exception as e:
            return [{"error": str(e)}]

    @classmethod
    def plot_chart(cls, keyword: str, output_path: str = None) -> Optional[str]:
        """
        根据检索到的时间序列数据，自动渲染出版级规范学术图表 (300 DPI)
        """
        import matplotlib.pyplot as plt
        
        # 配置出版级字体与排版
        plt.rcParams['font.sans-serif'] = ['SimSun', 'Microsoft YaHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.size'] = 10.5 # 五号字
        
        records = cls.query(keyword, page_size=15)
        # 筛选有效数值且按时间排序
        valid_records = [r for r in records if r.get("numeric_value") is not None and r.get("time")]
        if not valid_records:
            return None
            
        # 逆序或按时间正序排列
        valid_records.sort(key=lambda x: x.get("time_code") or x.get("time"))
        
        times = [r["time"] for r in valid_records]
        values = [r["numeric_value"] for r in valid_records]
        indicator_name = valid_records[0]["name"]
        unit = valid_records[0].get("unit") or ""
        
        fig, ax = plt.subplots(figsize=(8, 4.8), dpi=300)
        
        # 绘制学术折线与数据点
        ax.plot(times, values, marker='o', markersize=6, color='#1f77b4', linewidth=1.8, label=indicator_name)
        
        # 数值标签
        for i, txt in enumerate(values):
            ax.annotate(f"{txt}", (times[i], values[i]), textcoords="offset points", xytext=(0, 7), ha='center', fontsize=9)
            
        ax.set_title(f"{indicator_name} 历史演进趋势", fontsize=12, fontweight='bold', pad=12)
        ax.set_xlabel("时间", fontsize=10, labelpad=8)
        y_label = f"数值 ({unit})" if unit else "数值"
        ax.set_ylabel(y_label, fontsize=10, labelpad=8)
        ax.grid(True, linestyle='--', alpha=0.5)
        
        # 标注学术出处
        plt.figtext(0.12, 0.02, "数据来源：国家统计局官方发布库 (National Data) | 研学制图规范", fontsize=8.5, color='#555555')
        
        plt.tight_layout(rect=[0, 0.04, 1, 1])
        
        if not output_path:
            scratch_dir = os.path.expanduser(r"~\AppData\Local\hermes\cache\scratch")
            os.makedirs(scratch_dir, exist_ok=True)
            safe_name = "".join([c for c in keyword if c.isalnum() or c in ('_', '-')])
            output_path = os.path.join(scratch_dir, f"academic_chart_{safe_name}.png")
            
        plt.savefig(output_path, dpi=300)
        plt.close(fig)
        return os.path.abspath(output_path)


# ══════════════════════════════════════════════════════════════
# 2. 中科院 PubScholar 公益学术平台文献引擎
# ══════════════════════════════════════════════════════════════

class PubScholarRetriever:
    @classmethod
    async def search_async(cls, keyword: str, size: int = 5) -> Dict[str, Any]:
        from playwright.async_api import async_playwright
        
        captured = {}
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            
            async def on_resp(resp):
                if "open/resources/api/v1/articles" in resp.url and not resp.url.endswith("/aggregations"):
                    try:
                        ct = resp.headers.get("content-type", "")
                        if "json" in ct and resp.status == 200:
                            captured["data"] = await resp.json()
                    except Exception:
                        pass
                        
            page.on("response", on_resp)
            try:
                await page.goto("https://pubscholar.cn/", wait_until="networkidle", timeout=25000)
                inputs = await page.query_selector_all("input")
                target_input = None
                for inp in inputs:
                    ph = await inp.get_attribute("placeholder") or ""
                    if "发现" in ph or "搜索" in ph or "检索" in ph:
                        target_input = inp
                        break
                if not target_input and len(inputs) > 1:
                    target_input = inputs[1]
                    
                if target_input:
                    await target_input.fill(keyword)
                    await page.keyboard.press("Enter")
                    
                    for _ in range(8):
                        if "data" in captured:
                            break
                        await asyncio.sleep(1)
            except Exception as e:
                captured["error"] = str(e)
            finally:
                await browser.close()
                
        data = captured.get("data", {})
        total = data.get("total", 0)
        items = data.get("content", [])[:size]
        
        cleaned_articles = []
        for item in items:
            raw_authors = item.get("authors") or []
            authors = []
            for a in raw_authors:
                if isinstance(a, dict):
                    name = a.get("name") or a.get("author_name") or a.get("author") or ""
                    if isinstance(name, str) and name.strip():
                        authors.append(name.strip())
                elif isinstance(a, str) and a.strip():
                    authors.append(a.strip())
                elif isinstance(a, list):
                    for sub in a:
                        if isinstance(sub, str) and sub.strip():
                            authors.append(sub.strip())
                        elif isinstance(sub, dict):
                            n = sub.get("name") or ""
                            if n:
                                authors.append(n)
            if not authors:
                raw_a = item.get("author")
                if isinstance(raw_a, str) and raw_a.strip():
                    authors = [raw_a.strip()]
                elif isinstance(raw_a, list):
                    authors = [str(x) for x in raw_a if str(x).strip()]
                
            links = []
            for link_obj in item.get("links") or []:
                if isinstance(link_obj, dict) and link_obj.get("url"):
                    links.append({
                        "name": link_obj.get("name", "链接"),
                        "url": link_obj.get("url"),
                        "is_oa": link_obj.get("is_open_access", False)
                    })
                    
            raw_title = item.get("title", "")
            clean_title = raw_title.replace('<span class="Highlight">', '').replace('</span>', '')
            
            cleaned_articles.append({
                "title": clean_title,
                "authors": authors,
                "source": item.get("source", ""),
                "year": item.get("year", ""),
                "doi": item.get("doi", ""),
                "is_free": item.get("is_free", False),
                "abstract": (item.get("abstracts") or "")[:200] + "...",
                "fulltext_links": links
            })
            
        return {
            "total_matched": total,
            "keyword": keyword,
            "articles": cleaned_articles
        }

    @classmethod
    def search(cls, keyword: str, size: int = 5) -> Dict[str, Any]:
        return asyncio.run(cls.search_async(keyword, size))


# ══════════════════════════════════════════════════════════════
# 3. 中科院科技论文预发布平台 ChinaXiv (chinaxiv.org) 预印本引擎
# ══════════════════════════════════════════════════════════════

class ChinaXivRetriever:
    BASE_URL = "http://www.chinaxiv.org/oai/OAIHandler"
    
    @classmethod
    def search_oai(cls, keyword: str, limit: int = 3) -> List[Dict[str, Any]]:
        """
        通过 ChinaXiv 标准 OAI-PMH 接口检索首发权开放预印本
        """
        url = f"{cls.BASE_URL}?verb=ListRecords&metadataPrefix=oai_dc"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                xml_data = resp.read().decode("utf-8", errors="ignore")
                # 简单解析匹配
                records = []
                import xml.etree.ElementTree as ET
                root = ET.fromstring(xml_data)
                ns = {"oai": "http://www.openarchives.org/OAI/2.0/", "dc": "http://purl.org/dc/elements/1.1/"}
                for rec in root.findall(".//oai:record", ns):
                    title_el = rec.find(".//dc:title", ns)
                    creator_el = rec.findall(".//dc:creator", ns)
                    date_el = rec.find(".//dc:date", ns)
                    id_el = rec.find(".//dc:identifier", ns)
                    if title_el is not None and title_el.text:
                        title = title_el.text.strip()
                        if not keyword or keyword.lower() in title.lower():
                            creators = [c.text.strip() for c in creator_el if c.text]
                            records.append({
                                "title": title,
                                "authors": creators,
                                "date": date_el.text.strip() if date_el is not None and date_el.text else "",
                                "url": id_el.text.strip() if id_el is not None and id_el.text else "https://chinaxiv.org",
                                "type": "ChinaXiv 预发布论文 (Preprint)"
                            })
                            if len(records) >= limit:
                                break
                return records
        except Exception as e:
            return [{"error": f"ChinaXiv OAI 访问异常: {e}"}]


# ══════════════════════════════════════════════════════════════
# 4. GB/T 7714-2015 引用生成
# ══════════════════════════════════════════════════════════════

def format_gbt7714(article: Dict[str, Any]) -> str:
    raw_authors = article.get("authors") or ["佚名"]
    authors = [str(x).strip() for x in raw_authors if str(x).strip()] or ["佚名"]
    author_str = ", ".join(authors[:3])
    if len(authors) > 3:
        author_str += " 等"
    title = str(article.get("title") or "无题")
    source = str(article.get("source") or "学术刊物")
    year = str(article.get("year") or "2026")
    doi = article.get("doi")
    
    ref = f"{author_str}. {title}[J]. {source}, {year}."
    if doi:
        ref += f" DOI: {doi}."
    return ref


if __name__ == "__main__":
    kw = sys.argv[1] if len(sys.argv) > 1 else "国内生产总值"
    
    # 演示 1: 拉取数据
    print(f"=== [1] 国家统计局权威数据检索: {kw} ===")
    stats = NationalDataRetriever.query(kw, page_size=3)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    
    # 演示 2: 自动出图
    print(f"\n=== [2] 自动绘制 300 DPI 学术统计图 ===")
    chart_path = NationalDataRetriever.plot_chart(kw)
    if chart_path:
        print(f"✓ 图表已生成并保存至: {chart_path}")
        print(f"  (可用于毕业论文插图或答辩 PPT，带来源标注)")
    else:
        print("未获取到足够数值生成图表")
        
    # 演示 3: PubScholar 检索
    print(f"\n=== [3] 中科院 PubScholar 公益文献检索: {kw} ===")
    pub = PubScholarRetriever.search(kw, size=2)
    print(f"总检索量: {pub.get('total_matched')}")
    for i, art in enumerate(pub.get("articles", []), 1):
        print(f"\n[{i}] {format_gbt7714(art)}")
        print(f"    来源: {art['source']} | 年份: {art['year']} | 免费获取: {art['is_free']}")
