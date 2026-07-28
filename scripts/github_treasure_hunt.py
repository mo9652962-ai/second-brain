#!/usr/bin/env python3
"""GitHub 宝藏挖掘脚本 - 每周自动挖掘高价值项目"""
import os, sys, json, csv, requests
from datetime import datetime
from pathlib import Path

WORKSPACE = Path("/c/Users/31954/.openclaw/workspace")
RESEARCH_DIR = WORKSPACE / "knowledge" / "Research"
TRACKING_FILE = RESEARCH_DIR / "github-projects-tracking.csv"
GITHUB_API = "https://api.github.com"

SEARCH_TOPICS = ["mcp-server","ai-agent","knowledge-graph","obsidian-md","self-hosted","rag","vector-database","browser-automation","memory-layer","model-context-protocol","llm-inference","workflow-automation"]

WATCH_REPOS = ["memvid/memvid","browser-use/browser-use","n8n-io/n8n","ollama/ollama","langgenius/dify","tirth8205/code-review-graph","open-webui/open-webui"]

def fetch_trending():
    repos = []
    for topic in SEARCH_TOPICS[:5]:
        try:
            url = f"{GITHUB_API}/search/repositories"
            params = {"q": f"topic:{topic} sort:stars", "per_page": 10, "sort": "stars", "order": "desc"}
            resp = requests.get(url, params=params, timeout=30)
            if resp.ok: repos.extend(resp.json().get("items", []))
        except Exception as e: print(f"  search {topic}: {e}")
    seen = set(); unique = []
    for r in repos:
        if r["full_name"] not in seen: seen.add(r["full_name"]); unique.append(r)
    return unique[:20]

def get_repo(full_name):
    try:
        resp = requests.get(f"{GITHUB_API}/repos/{full_name}", timeout=30)
        return resp.json() if resp.ok else None
    except: return None

def assess(repo):
    name = repo.get("full_name","unknown")
    stars = repo.get("stargazers_count",0)
    lang = repo.get("language","N/A")
    lic = repo.get("license",{}).get("spdx_id","?") if repo.get("license") else "?"
    pushed = repo.get("pushed_at","N/A")
    desc = (repo.get("description") or "").lower()
    name_lower = name.lower()
    text = name_lower + " " + desc
    
    # 评分
    try:
        days = (datetime.now()-datetime.fromisoformat(pushed.replace("Z",""))).days if pushed!="N/A" else 999
    except: days = 999
    activity = max(0,100-days)
    star_s = min(100,stars/5000)
    fit_words = ["mcp","memory","knowledge","graph","obsidian","agent","self-host","local-first","rag"]
    fit = sum(1 for w in fit_words if w in text) * 25
    has_mcp = "mcp" in text
    integration = 100 if has_mcp else (60 if ("api" in text or "rest" in text) else 30)
    risk = 0 if repo.get("fork") else 100
    
    total = int(star_s*0.20 + activity*0.15 + fit*0.25 + integration*0.25 + risk*0.15)
    
    if total>=70 and stars>=1000: prio = "red"
    elif total>=50 and stars>=500: prio = "yellow"
    else: prio = "green"
    
    return {"name":name,"stars":stars,"url":repo.get("html_url",""),"description":repo.get("description",""),"lang":lang,"license":lic,"pushed":pushed,"score":total,"prio":prio,"has_mcp":has_mcp}

def gen_report(projects, date):
    top5 = sorted(projects, key=lambda x:x["score"], reverse=True)[:5]
    md = f"# GitHub 宝藏挖掘 - {date}\n\n## Top 5\n\n"
    for i,p in enumerate(top5,1):
        pemoji = {"red":"🔴","yellow":"🟡","green":"🟢"}
        md += f"### {i}. {p['name']} ({p['stars']:,}⭐) [{pemoji.get(p['prio'],'')}]\n- Score: {p['score']}/100 | Lang: {p['lang']} | License: {p['license']}\n- {p['description'][:200]}\n- URL: {p['url']}\n\n"
    
    mcp = [p for p in projects if p["has_mcp"]]
    if mcp:
        md += "## MCP 生态发现\n\n"
        for p in mcp[:3]: md += f"- **{p['name']}** ({p['score']}/100): {p['description'][:150]}\n"
    
    md += f"\n## 洞察\n\n1. MCP 持续成为 Agent 标准接口\n2. 本地优先是主流趋势\n3. 记忆系统是核心突破点\n\n---\n*自动生成 {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
    return md

def save_csv(projects, date):
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    exists = TRACKING_FILE.exists()
    with open(TRACKING_FILE, 'a' if exists else 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        if not exists: w.writerow(["name","stars","lang","url","discovered","checked","score","prio","notes"])
        for p in projects: w.writerow([p["name"],p["stars"],p["lang"],p["url"],date,date,p["score"],p["prio"],p["description"][:100]])

def main():
    date = datetime.now().strftime("%Y-%m-%d")
    print(f"🚀 GitHub 宝藏挖掘 {date}")
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    
    print("🔍 搜索...")
    trending = fetch_trending()
    print(f"   发现 {len(trending)} 个项目")
    
    print("📋 关注列表...")
    watched = [get_repo(r) for r in WATCH_REPOS]
    watched = [w for w in watched if w]
    print(f"   获取 {len(watched)} 个")
    
    all_r = watched + trending
    seen = set(); unique = []
    for r in all_r:
        if r.get("full_name") and r["full_name"] not in seen:
            seen.add(r["full_name"]); unique.append(r)
    
    print("🧠 评估中...")
    assessed = [assess(r) for r in unique]
    assessed.sort(key=lambda x:x["score"], reverse=True)
    
    print("📝 生成报告...")
    report = gen_report(assessed, date)
    fpath = RESEARCH_DIR / f"GitHub-Weekly-{date}.md"
    with open(fpath, 'w', encoding='utf-8') as f: f.write(report)
    print(f"   {fpath}")
    
    save_csv(assessed, date)
    print(f"   {TRACKING_FILE}")
    
    print("\n"+"="*50)
    for p in assessed[:3]:
        e = {"red":"🔴","yellow":"🟡","green":"🟢"}
        print(f"{e.get(p['prio'],'')} {p['name']} ⭐{p['stars']:,} 📊{p['score']}/100")
    
    red_n = sum(1 for p in assessed if p['prio']=='red')
    print(f"\n✅ {len(assessed)} 个项目 | 🔴{red_n} 🟡{sum(1 for p in assessed if p['prio']=='yellow')} 🟢{sum(1 for p in assessed if p['prio']=='green')}")

if __name__ == "__main__":
    main()
