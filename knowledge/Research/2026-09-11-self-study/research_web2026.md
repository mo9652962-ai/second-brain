# Web 全栈 2026 千轮研究报告：框架格局 · 部署定价 · 无 Docker 后端 · 接单技术栈

> 调研日期：2026-09-12 ｜ 方法：多轮 web_search + web_extract，优先官方文档（nextjs.org / react.dev / vercel.com / developers.cloudflare.com / nuxt.com / astro.build / cloud.tencent.com / aliyun.com）
> 背景：sora 网站接单业务（L1 100-150 元 / L2+ 域名 150-250 元 / L3 500-2000 元，域名客户出），技术栈倾向现代 Web，目标 = 前端 Vercel/CF + 后端轻量云（本机无虚拟化，禁 Docker/VM）。
> 一句话结论：**新单全面切 Next.js 16 + React 19.2 + Tailwind v4 + shadcn/ui；部署海外走 Vercel/CF Pages 免费层、国内走腾讯 EdgeOne Makers 免费层；后端一台 ¥99/年 轻量云跑 Gunicorn/systemd（Python）或 PM2（Node），全程零 Docker。**

---

## 一、2026 主流全栈框架格局（带实证）

### 1.1 Next.js + React：事实上的行业默认，但要注意两条线

| 项 | 实证 |
|:--|:--|
| 版本状态 | **Next.js 16.x = Active LTS（当前 16.2.11 / 16.3.4，2026-09 官方文档验证）；15.x = Maintenance LTS（15.5.21）**。新项目从 16 起，旧项目按 lockfile 锁版，不要把部署当升级 |
| Next 16 亮点 | Turbopack 成为默认打包器；Cache Components（`use cache` + PPR）；Instant Navigations（单页应用级响应）；dev 内存降 ~90%、`next dev` 启动快 ~400%、渲染快 ~50%（官方 blog，2026） |
| Next 15.5 节点 | Turbopack 构建 beta、Node.js Middleware 转稳定、`next lint` 废弃（官方 blog） |
| React 19 | **19.2.1（2025-12-03）为最新稳定；19.2.0（2025-10-01）**。RSC 与 Server Actions 已**稳定**（不再是实验特性）；React Compiler 1.0 稳定（构建期自动 memo，Meta 生产验证）；新增 Activity、useEffectEvent、ViewTransition、cacheSignal、性能轨道。React 19（2024-12）→ 19.1（2025-06）→ 19.2，一年三个 minor 说明特性都在 minor 里迭代 |
| 范式 | App Router + RSC 默认（Server First），只有交互组件标 `use client`；Server Actions 取代"为每个操作写 API 路由"；PPR/流式渲染成为性能基线；Suspense 边界即流式单元 |
| 生态 | 最大社区与岗位池；Vercel 原生优化 + v0、Vercel AI 等工具链；RSC 生态（下一跳）独占 |

**⚠️ 2026 接单必守安全线（RSC 新攻击面，官方确认）**：
- **CVE-2025-55182（React2Shell，CVSS 9.8）**：RSC Flight 协议反序列化 RCE，影响 React 19.0.0-19.2.0，修复版 19.0.1/19.1.2/19.2.1+；
- **CVE-2025-66478（CVSS 10.0）**：Next.js App Router 下游 RCE；修复版 Next 15.0.5 / 15.1.9 / 15.2.6 / 15.3.6 / 15.4.8 / 15.5.7 / 16.0.7（含 16.1/16.2/16.3 后续线）；官方明确"无关闭选项，唯一方案是升级"。
- 配套还有 CVE-2025-55184（DoS）/ CVE-2025-55183（源码泄露）。
- **SOP：任何交付物 lockfile 里 `next ≥ 15.3.6（16 线）`、`react ≥ 19.2.1`；Server Actions 入参一律 Zod 校验 + CSP。** 接单交付后把"依赖升级"写进交接文档。

### 1.2 Vue / Nuxt：国内第一生态，Nuxt 3 已到期

| 项 | 实证 |
|:--|:--|
| Nuxt 版本 | **Nuxt 4 稳定版 2025-07-16 发布；当前 4.4.6（2026-05-18）**；Nitro 2.13（全平台 server 引擎，支持 Vercel/CF/Node/Deno 等 15+ 目标）；Vue 3.5.34+ |
| EOL 红线 | **Nuxt 3 已于 2026-07-31 停维护**（官方从 2026-01-31 延长了 6 个月）；Nuxt 5 + Nitro v3 预告中。→ **新单一律 Nuxt 4；接手 Nuxt 3 老单要提前谈迁移** |
| 生态数据 | npm 周下载 ~1.44M（2026-05 实测）；GitHub 60.3k stars；313+ 社区模块（19 类）；Nuxt UI 120+ 组件；官方 CMS/auth 模块齐全（Better Auth 推荐）；LinkedIn 岗位 8k-12k，是 SvelteKit 的 10-20 倍 |
| 国内地位 | 中文资料/教程/岗位池最大；若墨题接单走 Vue 线，Nuxt 4 是唯一正解 |

### 1.3 SvelteKit：性能最优但生态小，不适合接单主战线

- **SvelteKit 2.61.1（2026-05-24）+ Svelte 5（5.55.10，runes）**；npm 周下载 2.02M（高于 Nuxt），GitHub 20.5k stars。
- 优势：Svelte 5 运行时仅 2-3KB gzip（Vue ~34KB），30 路由内容站比 Nuxt 少发 **40-60%** KB（toolchew 2026-05 实测）；默认零框架运行时；用户留存率 90%（vs Nuxt 81%）。
- 劣势：**无官方模块注册表**（Nuxt 313+ vs shadcn-svelte 40+ 组件）；CMS/auth 都要手接 SDK；岗位少 10-20 倍。
- 结论：适合自用/实验，不适合以交付速度与维护确定性为 KPI 的接单。

### 1.4 Astro 5：内容站/营销站/落地页的新标准（与 Next 殊途同归）

- **Astro 5.0 已稳定**：Content Layer（内容可来自任意源，Markdown 构建快 5x、MDX 快 2x、内存 -25~50%，SQLite 增量缓存）+ **Server Islands**（页面主体静态缓存进 CDN，动态小块按 `server:defer` 延迟渲染，cdn 命中率可到 95%+）+ Astro Actions（类型安全表单/变更）+ 静态/混合模式合并。
- 定位对照（来自 2026-05 深度测评）：
  - Astro = **static-first**（默认 0 JS，从静态吸收全栈）；Next.js = server-first（静态是缓存的一种）；SvelteKit = router-first。
- 最适合：落地页、官网、博客、文档、营销站 → **默认 JS 负载最小，免费静态托管友好**。

### 1.5 国内生态：Ant Design Pro 全面换代 + Tailwind v4 标准确立

- **Ant Design Pro v6 正式发布**：React 19 + antd 6 + Umi Max 4 + utoopack（基于 Turbopack 的打包器）+ **Tailwind CSS v4** + antd-style（CSS 变量主题）+ Biome + TanStack React Query + 内置 AI 助手页（Ant Design X）+ **示例后端为 Cloudflare Worker + Hono 独立部署**。内置 20+ 中后台页面模板（Dashboard/表单/列表/详情/异常/账号），`npm run simple` 一键精简。
- **Tailwind v4 已稳定**：CSS-first 配置（`@theme`）、OKLCH 颜色、`size-*` 工具；官方 3→4 升级 codemod 成熟。
- **shadcn/ui 已全量适配 Tailwind v4 + React 19**：CLI 默认新项目 Tailwind v4、new-york 风格；toast 废弃换 sonner；`tw-animate-css` 替代 tailwindcss-animate。（注意坑：v4 无 tailwind.config.js，shadcn init 校验 CSS 里 `@import "tailwindcss"` 行即可）
- 中后台结论：**别自造轮子——Ant Design Pro v6 或 Next.js + antd 6 + shadcn 起步**。

---

## 二、前端部署 2026：Vercel / Cloudflare / 国内平台定价实证

### 2.1 Vercel（海外默认首选，免费层够接单）

**Hobby（免费，永不收费，超限暂停不扣费）**——官方 pricing 页（2026 抓取）：
- Fast Data Transfer **100 GB/月**；函数调用 **100 万/月**；Active CPU 4 CPU-h；Provisioned Memory 360 GB-h；Edge Requests 100 万；Web Analytics 5 万事件/月；**200 个项目；100 次部署/天；每项目 50 域名；函数最长 300s**；WAF IP/规则各 3 条。
- 注意：Hobby 不能买超额，超了等 30 天重置。

**Pro $20/月（1 席位，加人 $20/人）**：Fast Data Transfer **1TB 含**，超额 **$0.15/GB**（2024 调价后降 62%）；函数 800s（beta 1800s）；无限项目；Edge Requests 1000 万含。

**⚠️ 中国大陆访问现状（官方 KB + 多篇 2026 实测）**：
- Vercel **无境内节点**，请求走港/日/新跨境链路，延迟 80-200ms；`*.vercel.app` 被 DNS 策略波及，**约 30% 用户间歇故障**；首屏 5-15s 常见。
- 官方建议：**绑自定义域名**（避开封锁面，约 +10-20%）；再叠 **Cloudflare 橙云代理**（DNS 全托管 CF + CNAME 到 vercel 目标、代理开启）可把首屏从 8-15s 压到 2-4s（+60-80%，2026 实测文章）。大陆为主要客户群时：**境内部署 + ICP 备案**（Vercel 不提供境内托管/合规支持）。
- 接单速记：**海外客户 → Vercel 秒级上线；国内客户 → 默认别用 vercel.app，绑客户域名 + CF 代理，或直接国内平台**。

### 2.2 Cloudflare Pages / Workers（海外性价比之王，免费层最慷慨）

**Pages 免费**（官方 limits 页）：
- **静态资源请求不限量、带宽不限量**；500 构建/月；单站点 2 万文件；100 项目/账号；1 并发构建；单次构建限 20 分钟。
- 动态（Functions）= Workers 计费：**10 万请求/天（所有 Worker 脚本共享，UTC 零点重置）**；CPU 10ms/次。

**Workers Free vs Paid**：Free 10ms CPU/次；**Paid $5/月起**：含 1000 万请求/月、超额 $0.30/百万、CPU 30M ms 含（单次上限默认 30s）。
**Pages Pro $20/月 扁平价（不按席位）**：5 并发构建 + Workers Paid 权益（10M 请求、CPU 50ms/次）。

**关键坑（2026 实测文章）**：
- 免费档 10ms CPU 对 Next.js middleware/SSR 极易 **1101 报错或静默截断**（GROQ 拉取、JWT 校验、next-intl 都能超）→ 加 **Workers Paid（$5）** 即可，不用升 Pages Pro；
- SSR 站每个 HTML/API/revalidate 都算一次调用，日活 150k 页面轻松打爆 10 万/天免费额 → 用 100 万请求/月的口径决策是否上 Paid；
- Next.js 上 CF 走 `@cloudflare/next-on-pages` 适配；**部分 ISR/缓存模式仍需 Vercel 或 workaround**（2026 仍是主要摩擦点，接单前先验证）。

### 2.3 国内平台：腾讯 EdgeOne Makers（原 EdgeOne Pages）免费层已很强

- **EdgeOne Makers 免费版（限时免费，商业化后额度可能收紧，官方明示当前更宽松）**：
  - 不限量的网站加速流量/请求；**40 项目；500 构建/月；Edge Functions 300 万次/月；Cloud Functions 100 万次/月**；Agents/Sandbox 各 10 万 GB-s；内置模型 50 万 token/月；**KV 1GB + Blob 1GB**；**200 自定义域名 + 免费 SSL**；DDoS 防护 + 单访问者 2000 次/5s 速率限制；生产/预览双环境；GitHub 导入自动识别框架（Next.js 零配置集成）。
  - 静态托管纯免费：HTML/CSS/JS/图片直传即上线，全球 CDN（腾讯云含大陆节点）、自动 HTTPS、无需信用卡；未注册临时链接 1 小时有效，注册后永久。
- **合规硬约束**：大陆服务器/大陆 CDN 回源 = 必须 **ICP 备案**（域名 + 主体，周期 2-4 周，接单要提前排队）；EdgeOne Makers 这类境外源不必备，但客户要大陆解析体验仍建议备案。**备案走客户主体（域名客户出）顺理成章。**

### 2.4 四平台横向速查

| 平台 | 免费额（月） | 首个付费档 | 大陆访问 | 适合 |
|:--|:--|:--|:--|:--|
| Vercel Hobby | 100GB 流量 / 100 万函数 / 200 项目 | $20（1TB 含、超额 $0.15/GB） | 无境内节点，需自定义域名+CF 代理 | Next.js 海外站 |
| Cloudflare Pages | 静态不限量 / 500 构建 / 10 万函数请求·天 | Workers Paid $5 或 Pages Pro $20（扁平） | CF 大陆节点有限，主走港/日 | 静态站、Next.js（适配器验证过） |
| EdgeOne Makers | 不限流量 / 500 构建 / 300 万边缘函数 / 200 域名 | 待商业化 | **腾讯全球 CDN 含大陆节点，免备案可用** | 国内客户首选 |
| 轻量云+自托管 | 看套餐 | ¥38-99/年 | 完全自控，备案后最优 | 需要后端+前端同机的项目 |

---

## 三、后端上云无 Docker 方案（sora 本机无虚拟化 → 裸进程 + systemd/PM2）

> 约束：本机无虚拟化 → **不碰 Docker/VM**；后端 = 轻量云服务器（Ubuntu 24.04）+ 裸进程管理。以下两套均已形成可复制 SOP（Python 栈已有 Hermes 技能实证，Node 栈经 2026 官方文档核对）。

### 3.1 Python（FastAPI）→ 已有实证 SOP（fastapi-cloud-deploy 技能）
```
互联网 → Nginx(443 TLS, Certbot) → Gunicorn(UvicornWorker, 127.0.0.1:8000) → FastAPI → SQLite(WAL)
```
- Gunicorn 生产进程管理（勿裸 uvicorn）：`-w 2`（1-2GB 内存）、`--max-requests 1000 + jitter`（内存泄漏保险丝）、`timeout ≥ 最慢端点（AI 120-300s）`；
- systemd 守护（Restart=always、PrivateTmp、ProtectSystem）；Nginx 只绑 127.0.0.1、WS 配 Upgrade/Connection、`proxy_read_timeout` 调大；
- SQLite 生产四件套：WAL + synchronous=NORMAL + busy_timeout=5000 + cache_size=-64000；**换库判据：`database is locked` 每周 >1 次或并发写 >20 才上 PostgreSQL**；
- 零掉线部署：`git pull && pip-sync && systemctl reload`（HUP 优雅重载）。

### 3.2 Node（Next.js 自托管）→ 2026 官方文档核对版
```
互联网 → Nginx(443) → PM2(或 systemd) → next start (127.0.0.1:3000, Node 24 LTS=24.20.0)
```
- **单实例起步**：Next.js 官方自托管指南明确"缓存按实例本地化"，多实例需要额外协调 cache tag 失效/共享缓存/部署版本；PM2 `instances: 1` + `max_memory_restart: 500M`；
- Nginx 要点：`proxy_buffering off`（App Router 流式/PPR 必需，否则丢 TTFB 优势）；`/_next/static` 直接从磁盘 alias + `expires 365d immutable` 直出（官方推荐）；`X-Accel-Buffering: no`；
- 内存：`NODE_OPTIONS=--max-old-space-size=512`（1GB 机器防 OOM）+ Swap；
- 持久化：`pm2 startup && pm2 save` 或直接 systemd unit（省一层依赖）；优雅退出 SIGTERM + 10-30s drain；
- 构建：用 lockfile 锁版（`npm ci`），`output: 'standalone'` 可选（纯 Node 产物，部署目录极小）；
- 纯静态项目直接用 `output: 'export'` → 连 Node 都不需要，Nginx/CF Pages/EdgeOne 直出（性能无敌）。

### 3.3 后端数据库免运维选项（不需要的时候别自建）
- **Neon Free**：100 项目、每项目 0.5GB、**100 CU-h/月**（compute 闲置 5 分钟自动归零、唤醒 ~570ms，不烧额度）、10 分支、6 小时即时恢复、5GB 出口流量。→ "闲置即零成本、分支即预发"最贴合接单后台。
- **Supabase Free**：2 项目、500MB、自带 Auth（5 万 MAU）/Storage 1GB/Edge Functions 50 万次/Realtime；**警告：项目闲置 7 天自动暂停、手动恢复，90 天后只能下载备份**。
- PlanetScale 已无免费层。接单后台若需要"零运维 + 客户迁移不心疼"，轻量云 SQLite 仍是第一选择（单文件备份最简单）。

### 3.4 服务器选型（2026 实价，续费是最大坑）
| 来源 | 配置 | 价格 | 续费 |
|:--|:--|:--|:--|
| 阿里云 ECS 99 计划 | 2核2G/3M 固定带宽/不限流量/40G ESSD | **¥99/年** | **同价续费，锁价至 2029-03-31**（官方活动页） |
| 腾讯云轻量 2核2G | 4M/50G SSD/300GB 月流量 | ¥99/年 | 同价续费限 1 次 |
| 腾讯云秒杀 | 4核4G/3M/40G | ¥38/年 | 首单限 1 个 |
| 华为云 | 2核2G/3M/40G | ¥89/年 | — |
- 选**固定带宽**（ECS）比峰值带宽稳定；别选 Windows 镜像（贵 3x）；国内地域延迟最优。接单后端成本天花板 = ¥99/年。

---

## 四、接单技术栈模板（sora L1-L3 定价）

### 模板 A：落地页 / 单页营销页（L1 100-150 元）→ 毛利率最高
- **栈**：Astro 5（默认 0 JS、Content Layer 管文案）或 Next.js `output: 'export'` 纯静态；Tailwind v4 + shadcn/ui（如需组件）。
- **部署**：CF Pages / EdgeOne Makers / Vercel Hobby 任选免费层；国内客户给 EdgeOne（大陆 CDN 免备案可达）。
- **交付物**：静态产物 zip + 部署指引；成本 **$0**。

### 模板 B：企业官网 / 品牌站 / 内容站（L2 150-250 元 + 域名）
- **栈**：Next.js 16 App Router + TypeScript + Tailwind v4 + shadcn/ui；RSC 默认服务端取数、ISR/`use cache` 管更新频率；SEO 元数据 + sitemap；可选 Astro 做纯展示页。
- **部署**：Vercel（海外/演示）或 EdgeOne（国内），客户域名一年期含 SSL 自动签发。
- 组件原型用 v0/Claude 生成 → 复制进项目，交付速度是 L2 定价的生命线。

### 模板 C：后台管理 / 中后台系统（L3 500-2000 元）→ 利润中心
- **前端**：Ant Design Pro v6（React 19 + antd 6 + Umi Max，20+ 现成页面模板，`npm run simple` 精简）或 Next.js + antd/shadcn（要 SSR/SEO 时）。
- **后端**：FastAPI（Gunicorn+systemd 已有 SOP）或 Next.js Route Handlers；认证用 Better Auth/JWT；入参 Zod。
- **数据**：SQLite WAL（单机后台够用）→ Neon/Supabase 免费层（客户要"云数据库"时）。
- **部署**：前端 EdgeOne/CF 免费 + 后端 ¥99/年 轻量云同机 Nginx 路由 `/api`；同一台机器 2 核 2G 即可。

### 通用工程基线（所有模板）
- TypeScript 必选；**Biome** 替代 ESLint+Prettier（快 10x，Ant Pro v6 已内置）；pnpm；Zod 校验所有入参；表单/服务端状态用 TanStack Query；移动优先响应式（Tailwind 断点）；交付盘含 `README + 备份 + 依赖安全版本声明`（React ≥19.2.1 / Next ≥15.3.6 或 ≥16.0.7）。
- 已有 Vue 资产（墨题）：Vue 生态新单一律 **Nuxt 4**（Nuxt 3 已停维护）；中后台直接 Ant Design Pro 而非自造。

---

## 五、立即行动建议（Top 5）

1. **升级主栈并建 2 个模板仓库**：Next.js 16 + React 19.2.x + Tailwind v4 + shadcn/ui；分别沉淀"官网模板"（RSC/ISR + SEO）与"后台模板"（antd 6 + 登录 + 权限 + CRUD），接单直接 `degit` 复制，交付速度翻倍。
2. **部署双轨制落地**：海外/演示 → Vercel Hobby 或 CF Pages 免费（Next.js 上 CF 先跑一遍 next-on-pages 验证 ISR 场景）；国内客户 → EdgeOne Makers 免费层 + 客户域名（免备案优先，需要时引导走 ICP）。永久放弃 `*.vercel.app` 直连国内。
3. **安全基线写进 SOP 第一条**：任何交付 lockfile 满足 React ≥ 19.2.1、Next ≥ 16.0.7（15 线 ≥ 15.3.6）——RSC 两条 RCE（CVSS 9.8/10.0）官方无关闭选项；Server Actions 入参一律 Zod。这条不满足不验收。
4. **L1 落地页用 Astro 5 而非大框架**：零 JS 默认、静态免费托管、L1 毛利拉满；只有需要动态/后台才升级 Next.js。同时把存量 Vue 项目标注"Nuxt 3 EOL(2026-07-31)"，新计一律 Nuxt 4。
5. **后端标准化为一条命令可部署**：把 fastapi-cloud-deploy 与 PM2+Node 两套 SOP 各自做成"部署脚本 + 清单"（服务器 ¥99/年 阿里云 ECS 99 计划，锁价 2029），接 L3 时后端成本恒定为 8 元/月，报价不被服务器费用绑架。

---

## 附：主要来源
- nextjs.org/blog（Next 15/15.5/16 发布与安全公告）、nextjs.org/docs（自托管）
- react.dev/blog（React 19.2）、facebook/react CHANGELOG
- vercel.com/pricing、vercel.com/docs/plans/hobby、vercel.com/kb（大陆访问）
- developers.cloudflare.com（Workers/Pages pricing & limits）
- cloud.tencent.com（EdgeOne Makers 配额/FAQ）、pages.edgeone.ai（限制与配额）
- aliyun.com ECS 99 计划、cloud.tencent.com 轻量价格总览
- nuxt.com / github.com/nuxt（EOL）、toolchew.com & solodevstack.com（Nuxt/SvelteKit 2026 对比实证）
- astro.build/blog/astro-5、ant.design Pro v6、ui.shadcn.com（Tailwind v4）、neon.com & supabase.com 免费层对比

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
