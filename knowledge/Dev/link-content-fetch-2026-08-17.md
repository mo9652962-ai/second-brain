# 链接内容抓取能力增强 · 千轮研究（2026-08-17）

> 触发：用户问「增强从链接获取内容的能力，比如小黑盒类似的链接」
> 技能沉淀：`link-content-fetch`（Hermes）+ `douyin-video-fetch`（抖音专项）

## 一、实测结论（小黑盒当靶子）

| 方案 | 小黑盒首页 | 小黑盒帖子正文 | 结论 |
|:---|:---:|:---:|:---|
| 直接 curl | 302 | ❌ | JS 渲染 |
| **Jina Reader**（r.jina.ai 免费）| ✅ slogan | ❌ 正文空白 | 只过首页，帖子被反爬挡 |
| 旧 API（hkey 签名）| — | ❌ 「请使用APP查看」| 签名已过时 |
| Playwright 真实浏览器 | ✅ | ✅（需登录）| 小黑盒正文要登录 Cookie |

**核心发现**：小黑盒 = JS 渲染 + hkey 签名 + 登录墙三层防护。Jina 这类免费 API 只过第一层。

## 二、小黑盒专门方案（GitHub 实证）

| 项目 | 技术 | 状态 | 亮点 |
|:---|:---|:---|:---|
| XiaoheiheMcpServer | .NET + Playwright | get_post_detail ✅ | 扫码登录、Cookie 持久化、9 工具 |
| heybox-video | FastAPI + requests/nodriver | 视频直链 ✅ | 两段式解析 + 验证码冷却 |
| better-XiaoHeiHe | 浏览器扩展 | ✅ | 复用页面参数实时生成 hkey |

**精华模式（两段式）**：HTTP fast path → 浏览器回退（无头）→ 验证码升级有头 → 冷却期防撞。

## 三、通用工具基准（2026 横评，30 页实测）

Firecrawl 24/25 > MDisBetter 23 > Jina Reader 21 > Trafilatura 19 > Readability 16 > html2text 10

**选型原则**：谁付渲染成本 + 提取逻辑放哪，决定选哪个 rung：
- 单个 URL 即时读 → Jina Reader（前缀 API，免费 10M tokens）
- 高量 RAG 管道 → Crawl4AI（自托管，边际零成本）
- 全站结构化提取 → Firecrawl（metered API）

## 四、四层抓取决策树（落地）

```
① web_extract（静态页）→ ② Jina Reader（JS 渲染，免费）
→ ③ Playwright 拦截（签名反爬，征用算法）
→ ④ MCP 登录方案（登录墙，XiaoheiheMcpServer）
→ ⑤ Firecrawl/Crawl4AI（全站大规模）
```

## 五、对 Hermes 的接入结论

- Hermes web_extract 支持 tavily/firecrawl/exa/searxng，**无内置 jina**
- Jina 是零配置 curl 前缀，无需改核心——按 footprint ladder 走技能方案
- 已建 `link-content-fetch` 技能含四层方案 + 通用 Playwright 拦截模板
