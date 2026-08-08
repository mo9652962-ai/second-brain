---
date: 2026-07-29
tags: [browser, cloud, browserbase, evaluation]
status: ready
trigger: 需要高反检测能力（如批量抓取被封、需要住宅代理、CAPTCHA 自动解）
---

# Browserbase 云服务 — 评估对比

> 状态：🟢 就绪（对比已做，需要时直接选方案）
>
> 不预装，触发时按需启用

---

## 云浏览器方案对比

| 维度 | Browserbase | Browser Use Cloud | Camofox Docker |
|-----|------------|-------------------|----------------|
| 反检测率 | 81% | 81% | 高（Firefox指纹） |
| 部署方式 | 云（无需本地） | 云（无需本地） | 本地Docker |
| 费用 | 💰 按 session | 💰 按分钟 | 🆓 免费 |
| 代理 | ✅ 住宅代理内置 | ✅ 住宅代理内置 | ❌ 需自建 |
| CAPTCHA | ✅ 自动解 | ✅ 自动解 | ❌ 需人工 |
| 数据隐私 | ⚠️ 云端 | ⚠️ 云端 | ✅ 本地 |
| 启用耗时 | 注册→5分钟 | 注册→5分钟 | 安装→20分钟 |

---

## 决策矩阵

| 场景 | 推荐方案 | 理由 |
|-----|---------|------|
| 日常网页阅读/归档 | Hermes 内置 browser_* | 免费，够用 |
| 有 Cloudflare 的站点 | **Camofox** | 免费，反检测强 |
| 需要验证码绕过 | **Browserbase** | 唯一能自动解 CAPTCHA |
| 需要住宅IP（地区限制站点） | **Browserbase** | 内置住宅代理 |
| 敏感数据（不想上云） | **Camofox** | 数据在本地 |
| 批量大规模抓取（100+页） | **Browserbase** | 弹性伸缩，不占本地资源 |

---

## Browserbase 启用步骤（需要时执行）

```bash
# 1. 注册 https://browserbase.com → 获取 API Key
# 2. 添加到 .env
# BROWSERBASE_API_KEY=your_key
# BROWSERBASE_PROJECT_ID=your_project

# 3. Hermes config.yaml
# browser:
#   cloud_provider: browserbase
#   auto_local_for_private_urls: true
```

---

## 费用预估

| 用量 | 预估月费 |
|-----|---------|
| 轻量（<100页/月） | $0-5 |
| 中等（100-500页/月） | $10-25 |
| 重度（>1000页/月） | $50+ |

---

*预案创建：2026-07-29*

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]
