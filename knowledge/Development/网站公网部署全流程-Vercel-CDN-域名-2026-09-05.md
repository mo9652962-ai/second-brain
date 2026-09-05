---
tags: [knowledge, deployment, web, vercel, domain]
title: "网站公网部署全流程-Vercel-CDN-域名-2026-09-05"
type: note
created: 2026-09-05
updated: 2026-09-05
---

# 网站公网部署全流程（Vercel + 自定义域名 + Cloudflare）

> 来源：抖音「写代码的码农：如何将做出来的网站实现让别人访问全流程 AI + Codex」（拿到完整章节要点）
> 章节：理解 localhost → 本地开发与公网访问 → Vercel 部署 → 公网链接 → 绑定自定义域名 DNS 解析 → 全球可访问 → 流程复盘
> 数据截止：2026-09-05

## 核心结论（置顶）

1. **部署前端静态站的最短路径 = Vercel**：GitHub 导入 → 自动构建 → `*.vercel.app` 公网链接 → 自动 HTTPS → 全球 CDN。个人项目免费额度（月 100GB 流量）完全够用。
2. **Vercel 免费（Hobby）仅限非商业用途**——域名用于产品/付费客户/产生收入 → 必须 Pro（$20/席/月）。**墨题商业化前必须评估**；替代：Firebase Spark（免费允许商业）或国内平台。
3. **绑定自定义域名最干净的姿势**：apex 用 A 记录 `76.76.21.21`，www 用项目专属 CNAME（**每个项目不一样，复制控制台的值**），证书签发前 Cloudflare 保持 DNS-only（灰云）。
4. **中国访问 Vercel 慢** → Cloudflare 中国优化网关（`vercel-cname.xingpingcn.top`）或国内平台。sora 用户群在国内，这条是刚需。
5. **我们已有路线对比**：墨题 = FastAPI 后端（fastapi-cloud-deploy 云服务器路线）+ Vue 前端 dist（本方案补前端托管面）——**前端走 Vercel/CF Pages，后端走云服务器，两头分开最优**。

## 一、完整流程（视频主线）

```
本地 localhost → 代码推 GitHub → Vercel 导入部署 → *.vercel.app 公网链接
→ 买自定义域名 → Vercel Domains 添加 → DNS 解析（A/CNAME）
→ Cloudflare 托管 DNS → 证书自动签发 → 全球可访问
```

### 1. 理解 localhost
- `localhost`/`127.0.0.1` = 只有自己电脑能访问；手机/别人访问不到
- 局域网 IP（192.168.x.x）= 同一 WiFi 可访问；跨网络不行
- 公网部署 = 让别人在任何网络都能访问

### 2. Vercel 部署（视频 01:31-06:27）
1. GitHub 账号 → vercel.com 注册（Continue with GitHub）
2. Add New Project → Import 仓库 → Deploy（零配置）
3. 得到 `my-project.vercel.app` 公网链接 + 自动 HTTPS

### 3. 绑定自定义域名（视频 06:48-07:29）
1. Vercel → Project → Settings → Domains → 添加 `yourdomain.com`
2. **选 "Connect to an environment" → Production**（别选 Redirect，否则暴露 vercel.app 长链）
3. 复制 Vercel 给的 DNS 记录（2026 起 CNAME 按项目分配）

| 记录 | 类型 | 值 |
|:---|:---|:---|
| apex（@） | A | `76.76.21.21`（Vercel anycast IP）|
| www | CNAME | `d1d4fc...vercel-dns-017.com`（**项目专属**，复制控制台的）|

4. 域名注册商处添加（Namesilo/Cloudflare/阿里云/腾讯云）
5. 等 Vercel 绿勾（Valid Configuration）→ 自动签 Let's Encrypt 证书

### 4. Cloudflare DNS（视频 07:29-08:39）
- 域名 NS 托管到 Cloudflare（免费，成本价卖域名 .com ≈ ¥55/年）
- 加 DNS 记录时 **proxied: false（灰云）**，等 Vercel 签完证书再开橙云
- 开橙云后 SSL/TLS 模式设 **Full (strict)**（Flexible 会造成无限重定向）

## 二、绑定域名的 5 个坑（90% 卡住的原因）

| # | 坑 | 解法 |
|:---|:---|:---|
| 1 | **DNS 分裂**：NS 在 registrar 却把记录加在别处 | `dig NS yourdomain.com` 确认哪家在应答，加到那边 |
| 2 | **签发期开 Cloudflare 橙云** → "Failed to Generate Cert" | 证书签好前灰云（DNS-only）|
| 3 | **只加 apex 或只加 www** → 另一半 404 | 两个都加，Vercel 自动 308 跳主域 |
| 4 | **旧记录 TTL 太长** → 切了 DNS 还在缓存 | 切换前 TTL 调 300s 等过期 |
| 5 | **CAA 记录挡 Let's Encrypt** → 无声失败 | `dig +short CAA` 检查；无 CAA 最好；有则必须授权 |

**验证命令**：
```bash
dig +short A yourdomain.com @1.1.1.1          # 期望 76.76.21.21
dig +short CNAME www.yourdomain.com @1.1.1.1  # 期望项目专属 CNAME
curl -vI https://yourdomain.com 2>&1 | grep -E 'subject:|issuer:|HTTP'
# 期望 subject=域名 issuer=Let's Encrypt HTTP/2 200
```

## 三、中国访问加速（sora 刚需）

**问题**：Vercel 服务器海外，国内访问慢/不稳。
**方案**（Cloudflare + Vercel 中国优化，CSDN 2026 实测）：

| 阶段 | Cloudflare CNAME 目标 | 代理状态 | 目的 |
|:---|:---|:---|:---|
| 初始验证 | `cname-china.vercel-dns.com` | 灰云 | 让 Vercel 验证域名所有权 |
| 加速生效 | `vercel-cname.xingpingcn.top` | 橙云 | 流量走 CF 中国友好节点 → 优化网关 → Vercel |

链路：`用户 → Cloudflare 中国节点 → 优化网关 → Vercel 全球网络`
备用：`enhanced-FaaS-in-China` 项目文档有其他可用 CNAME。
**更稳替代**：国内平台（腾讯 Webify/阿里云 OSS+CDN）或后端云服务器方案（我们已有）。

## 四、域名注册商对比（2026）

| 平台 | 特点 | .com 价格 |
|:---|:---|:---|
| Namesilo | 便宜、免费隐私保护 | ≈¥60/年 |
| **Cloudflare** | 成本价、无加价 | ≈¥55/年（最便宜）|
| 阿里云万网 | 中文、支付方便 | ≈¥69/年 |
| 腾讯云 | 同上 | ≈¥65/年 |

选域名：短、跟项目相关（huajiaji.com 优于 hjj.com）、别用拼音缩写。

## 五、与 sora 现有体系的对照（apply）

| 场景 | 走哪条路 |
|:---|:---|
| 墨题后端 API | **fastapi-cloud-deploy**（Gunicorn+systemd+Nginx+SQLite，¥38-99/年）|
| 墨题前端 dist 静态 | Vercel/CF Pages 免费托管（**商业化前确认许可证**）或同服务器 Nginx 托管 |
| 简单静态站/接单交付 | Vercel 免费 + 域名可选 |
| 国内用户为主 | 优先国内 CDN/平台；Vercel 必须配中国优化网关 |
| 接单帮客户部署 | Vercel 演示站（免费）+ 客户域名；商业站点提示 Pro 条款 |

**商业化红线**：Vercel Hobby 非商业用途——墨题 Pro 买断（¥98-128）一旦走 Vercel 域名就要 Pro 套餐，或前端改用 Firebase/CF Pages/国内平台。

## 落地条件与触发器

- 落地条件：墨题前端上线公网时，或接单交付「网站部署」服务时
- 触发器：用户说「网站部署/让别人访问/上线公网/绑定域名」→ 本笔记 + fastapi-cloud-deploy 双参考
- 未满足：墨题商业化定案前，先定前端托管平台（Vercel Pro vs CF Pages vs 国内）

## 关联

- [[Development/墨题上云部署方案-无Docker-2026-09-02]] — 墨题后端云服务器方案
- skill: fastapi-cloud-deploy（后端部署；本笔记补前端面）
- skill: modern-web-development / web-dev-2026（建站方法论）
