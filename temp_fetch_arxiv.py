import sys, xml.etree.ElementTree as ET
import urllib.request
from datetime import datetime

# Fetch from arXiv
url = "https://export.arxiv.org/api/query?search_query=all:AI+agent+OR+all:large+language+model+OR+all:LLM+agent&sortBy=submittedDate&sortOrder=descending&max_results=10"
response = urllib.request.urlopen(url)
xml_content = response.read()

# Parse XML
ns = {'a': 'http://www.w3.org/2005/Atom'}
root = ET.fromstring(xml_content)
papers = []

for entry in root.findall('a:entry', ns):
    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
    arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    published = entry.find('a:published', ns).text[:10]
    authors_list = [a.find('a:name', ns).text for a in entry.findall('a:author', ns)]
    authors = ', '.join(authors_list[:3])
    if len(authors_list) > 3:
        authors += ' et al.'
    summary = entry.find('a:summary', ns).text.strip()
    cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
    papers.append({
        'id': arxiv_id,
        'title': title,
        'authors': authors,
        'published': published,
        'abstract': summary,
        'categories': cats,
        'pdf': f'https://arxiv.org/pdf/{arxiv_id}',
        'abs': f'https://arxiv.org/abs/{arxiv_id}'
    })

# Generate markdown
today = datetime.now().strftime('%Y-%m-%d')

md_content = f'''---
tags: [arxiv, ai-agent, llm, research, papers]
date: {today}
source: arXiv
---

# arXiv AI Agent & LLM 最新论文 - {today}

> 自动检索于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

'''

for i, p in enumerate(papers, 1):
    md_content += f'''## {i}. {p['title']}

- **ID**: `{p['id']}`
- **作者**: {p['authors']}
- **发表日期**: {p['published']}
- **分类**: {p['categories']}
- **链接**: [摘要]({p['abs']}) | [PDF]({p['pdf']})

### 摘要
{p['abstract']}

---

'''

print(md_content)
