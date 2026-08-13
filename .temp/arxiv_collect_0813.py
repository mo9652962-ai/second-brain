#!/usr/bin/env python
"""Collect arXiv AI Agent/LLM papers 2026-08-08..2026-08-13 (daily quick-scan).
URL built MANUALLY (no urlencode!) — verified 2026-08-13: full urlencode (%28/%29/%2B/%3A)
returns 0 entries in this arXiv env; literal parens + literal '+' + pre-encoded %5B%5D works.
"""
import sys, time, json, urllib.request
import xml.etree.ElementTree as ET

NS = {'a': 'http://www.w3.org/2005/Atom'}
CATS = 'cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.LG+OR+cat:cs.MA+OR+cat:cs.SE+OR+cat:cs.RO+OR+cat:cs.HC+OR+cat:cs.CV+OR+cat:cs.CR+OR+cat:cs.DB'
WINDOW = 'submittedDate:%5B202608090000+TO+202608092359%5D'

QUERIES = [
    ('Agent Framework', 'all:AI+agent+framework+OR+all:autonomous+agent+OR+all:agentic+workflow'),
    ('LLM Agent', 'all:LLM+agent+system+OR+all:language+model+agent+OR+all:large+language+model+agent'),
    ('Multi-Agent', 'all:multi-agent+reinforcement+OR+all:multi-agent+system+OR+all:multiagent'),
    ('Tool Use/MCP', 'all:tool+use+LLM+OR+all:function+calling+OR+all:tool+calling+OR+all:MCP+protocol+OR+all:model+context+protocol'),
    ('Code Agent', 'all:code+generation+agent+OR+all:software+engineering+agent+OR+all:coding+agent'),
    ('Agent Memory', 'all:agent+memory+OR+all:memory+augmented+agent+OR+all:retrieval+agent'),
    ('Agent Safety', 'all:agent+safety+OR+all:prompt+injection+OR+all:agent+security+OR+all:jailbreak'),
]

def fetch(query, max_results=15):
    url = ('https://export.arxiv.org/api/query?search_query='
           f'({query})+AND+({CATS})+AND+{WINDOW}'
           f'&max_results={max_results}&sortBy=submittedDate&sortOrder=descending')
    req = urllib.request.Request(url, headers={'User-Agent': 'HermesCron/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return ET.parse(r).getroot()

def main():
    out = sys.argv[1] if len(sys.argv) > 1 else '.temp/arxiv_20260813.json'
    seen = {}
    for topic, q in QUERIES:
        try:
            root = fetch(q)
            entries = root.findall('a:entry', NS)
            print(f'[ok] {topic}: {len(entries)} entries', flush=True)
            for entry in entries:
                arxiv_id = entry.find('a:id', NS).text.strip().split('/abs/')[-1]
                base = arxiv_id.split('v')[0]
                published = entry.find('a:published', NS).text
                summary = ' '.join(entry.find('a:summary', NS).text.strip().split())
                if 'withdrawn' in summary[:200].lower():
                    continue
                if base not in seen:
                    seen[base] = {
                        'id': arxiv_id,
                        'base': base,
                        'title': ' '.join(entry.find('a:title', NS).text.strip().split()),
                        'published': published[:10],
                        'submitted': published[:16],
                        'authors': ', '.join(a.find('a:name', NS).text for a in entry.findall('a:author', NS)),
                        'abstract': summary,
                        'cats': ', '.join(c.get('term') for c in entry.findall('a:category', NS)),
                        'topics': [],
                    }
                if topic not in seen[base]['topics']:
                    seen[base]['topics'].append(topic)
        except Exception as e:
            print(f'[error] {topic}: {e}', file=sys.stderr)
        time.sleep(3.5)

    items = sorted(seen.values(), key=lambda x: x['submitted'], reverse=True)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
    print(f'TOTAL_UNIQUE={len(items)} -> {out}')
    for i, p in enumerate(items, 1):
        print(f'{i}. [{p["id"]}] {p["submitted"]} | {p["title"][:90]} | {p["cats"][:40]}')

if __name__ == '__main__':
    main()
