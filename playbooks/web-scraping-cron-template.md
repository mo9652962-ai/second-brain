---
date: 2026-07-29
tags: [cron, web-scraping, knowledge-automation]
status: ready
trigger: 确定具体信息源后启用
---

# 网页定时抓取 — 预备方案

> 状态：🟢 就绪（信息源清单 + Cron 模板已备，选好源即可启动）

---

## 候选信息源

| 优先级 | 源 | URL | 更新频率 | 抓取方式 | 价值 |
|--------|-----|-----|---------|---------|------|
| ⭐⭐⭐ | Hacker News | news.ycombinator.com | 实时 | web_extract | AI/Coding 前沿 |
| ⭐⭐⭐ | Reddit ML | reddit.com/r/MachineLearning | 每日 | web_extract | 论文讨论 |
| ⭐⭐ | GitHub Trending | github.com/trending | 每日 | API/web | 项目发现 |
| ⭐⭐ | 知乎 AI 热榜 | zhihu.com/hot | 每小时 | browser | 中文社区 |
| ⭐ | 机器之心 | jiqizhixin.com | 每日 | web_extract | AI 新闻 |
| ⭐ | 量子位 | qbitai.com | 每日 | web_extract | AI 新闻 |

---

## Cron 任务模板

确定信息源后，用以下模板创建：

```
名称：{source}-daily-fetch
调度：0 7 * * *（每天 7:00）
Skills：browser-automation
提示：

打开 {URL}，抓取前 10 条内容。每条内容：
1. 提取标题 + 链接 + 摘要
2. 去重（与上周内容对比）
3. 选出 3-5 条最有价值的
4. 保存到 knowledge/Daily/{date}.md
```

---

## 首次启用建议

1. **先试 Hacker News** — 纯文本，`web_extract` 即可，最快最简单
2. 稳定运行 1 周后，再添加第二个源
3. 每增加一个源，观察 Cron 成功率（目标 >95%）

---

*预案创建：2026-07-29*
