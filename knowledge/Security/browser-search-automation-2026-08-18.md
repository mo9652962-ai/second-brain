# 浏览器搜索 + 自动化增强（2026-08-18 千轮研究）

> 技能：`browser-automation`（新增「浏览器搜索增强 / AI 代理工具矩阵 / Hermes 登录 5 方案」章节）

## 一、Dorking 2026 核心
- 骨干算子：site: / filetype: / intitle: / inurl: / intext:
- 高价值：`"精确"` / -排除 / OR 分组 / before: / after:
- 已废弃：cache:(2024) related:(2023) → Wayback Machine 替代
- 全引擎唯一：site:

## 二、挖洞 Dork 组合（严重级排序）
| 级别 | Dork | 目标 |
|:---|:---|:---|
| 严重 | filetype:env intext:"DB_PASSWORD" site:目标 | 数据库凭证 |
| 严重 | site:github.com "目标" token OR secret | 外部泄露 |
| 高危 | intitle:"index of" inurl:backup | 开放目录 |
| 高危 | intitle:"Grafana" OR "Kibana" site:目标 | 未授权监控 |
| 中危 | inurl:admin OR inurl:login -www | 管理界面 |
| 中危 | site:pastebin.com "目标" password | 密码泄露 |

## 三、AI 浏览器代理选型
- browser-use（Python 65K stars）：自主 agent，开放式任务
- Stagehand（TS 15K stars）：控制优先 act/extract/observe，3-4x 便宜
- Skyvern：视觉工作流平台
- **AOM 观察策略 = token 效率关键**（省 10-57x，Hermes browser_snapshot 即 AOM）

## 四、反检测三层
JS 层（playwright-stealth）→ TLS 层（CloakBrowser 49+ patch）→ 行为层（真实 UA/轨迹）

## 五、Hermes 登录 5 方案
表单登录 / Camofox profile 持久化 / browser_console 注入 Token / VNC 人机协作 / CDP 连接已登录浏览器

## 六、增强落地流水线
web_search 基础 → Dork 组合 → browser_navigate+snapshot（需渲染）→ Playwright MCP/CDP（反爬/登录）→ AI 分析报告
