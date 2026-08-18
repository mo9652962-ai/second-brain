# 抖音视频抓取能力增强 · 千轮研究（2026-08-17）

> 触发：用户问「抓取信息的能力能增强吗」——此前抖音链接（浮石·SolidWorks仿生机器人）curl/web_extract 都拿不到空壳
> 技能沉淀：`douyin-video-fetch`（Hermes，已实测）

## 一、问题本质

抖音 Web 端 API 防护 = 多层体系：
- **a_bogus / X-Bogus 签名**：前端 JS 动态生成，与 query 参数/UA/时间戳绑定
- **msToken / s_v_web_id cookies**：会话身份关键
- **TLS/浏览器指纹**：Canvas/WebGL/字体检测

简单 HTTP 客户端（requests/curl）缺这些 → 返回空壳或风控页。

## 二、方案对比（千轮研究结论）

| 方案 | 状态 | 说明 |
|:---|:---|:---|
| curl / web_extract | ❌ 空壳 | JS 渲染页面 |
| yt-dlp | ❌ 已坏 | Douyin extractor 2024 起失效（GitHub #9667/#10409），需 a_bogus + fresh cookies + 验证码 |
| 逆向签名算法 | ⚠️ 维护地狱 | SM3/RC4+指纹（DLWangSan/douyin_parse 等），算法频繁更新易封 |
| **Playwright 拦截** | ✅ 实测成功 | 「不破解算法，征用算法」——抖音 JS 在真实浏览器生成合法签名，拦截 aweme/detail 响应 |

## 三、实测结果（2026-08-17）

对 `v.douyin.com/Ka9mnVlIsnY/`（浮石·SolidWorks仿生机器人）：
- ✅ 标题：solidworks建模仿生机器人 #solidworks #仿生机器人...
- ✅ 作者：浮石 (uid: 3952118821031104)
- ✅ 视频ID：7674569049985182702
- ✅ 无水印直链：douyinvod.com mp4
- ✅ 点赞数：217

之前 curl 空壳、yt-dlp 报「Fresh cookies are needed」，Playwright 一次成功。

## 四、核心代码模式

```python
async def fetch_douyin(url):
    from playwright.async_api import async_playwright
    captured = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="...Chrome...", locale="zh-CN")
        page = await context.new_page()
        async def on_response(resp):
            if "aweme/v1/web/aweme/detail" in resp.url and resp.status == 200:
                try: captured["detail"] = await resp.json()
                except Exception: pass
        page.on("response", on_response)
        await page.goto(url, timeout=30000, wait_until="domcontentloaded")
        for _ in range(15):
            if "detail" in captured: break
            await asyncio.sleep(1)
        await browser.close()
    return captured.get("detail")
# 提取：desc标题 / author.nickname / play_addr.url_list[0] / statistics.digg_count
```

## 五、备选方案

1. RENDER_DATA script 标签：页面 document 中 script#RENDER_DATA，URL 解码后是 JSON
2. video 标签直读 src（有头模式防验证码）
3. 搜索引擎兜底：抓不到视频本体 → 搜标题关键词给替代资料

## 六、通用启示（不止抖音）

- 抓取能力增强路径：**轻量 HTTP → Playwright 真实浏览器 → 网络拦截**（递进）
- 「征用算法」>「逆向算法」：维护成本低一个量级
- 任何 JS 渲染 + 签名反爬的站点（抖音/小红书/快手）都适用同一模式

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
