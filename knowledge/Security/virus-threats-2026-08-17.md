---
tags: [网络安全, 病毒, 勒索软件, 供应链攻击, 研究笔记, 2026-08]
domain: Security
---

# 2026 网络病毒威胁研究 + 预防（2026-08-17）

> 方法：web_search 多源实证（CNCERT/奇安信/火绒/Cloudflare/Check Point/Bitdefender/Kodem/Elastic）+ 本地环境实测
> 相关: [[clickfix-sql-injection-2026-08-17]]

## 一、2026 威胁总态势（多源交叉）

### 宏观数据
- 2026 上半年新增漏洞 **35,467 个**（同比 +51.9%），高危占比 52.1%（奇安信）
- **30.2% 高危漏洞发布当天即被利用**，83.7% 在 21 天内遭攻击——「修补窗口期」进入**小时级**
- 勒索软件：Q2 数据泄露站点 2,139 受害者（同比 +33%），活跃团伙 71→93 个创新高（Check Point）
- 被盗凭据同比 +42%；**63% 登录尝试来自机器人**（Cloudflare）
- 攻击者用 AI 编码助手 3 天建好勒索管理面板（The Gentlemen 泄露聊天记录实锤）

### 六大趋势（Cloudflare 2026 报告）
1. AI 自动化攻击（实时网络测绘/漏洞开发/深度伪造）
2. 国家级预部署攻击关键基础设施
3. SaaS 集成权限过高 → 连锁入侵
4. **可信云工具被武器化**（Google Calendar/Dropbox/GitHub 做 C2）
5. 深度伪造身份渗透企业
6. **令牌窃取让 MFA 失效**（LummaC2 窃取会话令牌）

## 二、近期重点病毒/恶意软件（对你最相关）

### 🔴 1. Shai-Hulud npm 供应链蠕虫（2026-08-04 爆发，**最直接威胁**）
**这是什么**：攻击者黑掉 keyv 维护者 GitHub 账号 → 往 11 个核心缓存包（keyv/flat-cache/file-entry-cache/cacheable 系）注入蠕虫 → 月下载量超 20 亿次。

**攻击链**：`preinstall hook` → 下载 Bun 运行时 → 执行 728KB 混淆载荷（Math_Symbol.js）→ 窃取 npm/GitHub/云/AI 工具（Claude/Codex/Cursor/OpenAI/Gemini）凭据 → 用窃取的发布 token **自我复制到几百个包**。

**独特危险**：
- 恶意版本带**有效 npm 签名**（GitHub Actions 签名过的！）——签名只证构建不证来源
- 会往 `.claude/settings.json` / `.vscode/tasks.json` 植入 hook——**AI 编码 agent 打开项目就触发**（Hermes/dsh 也在目标内！）
- **死开关陷阱**：撤销 token 反而触发远程恶意命令——**先清理后轮换**

**恶意版本**（安全版本见括号）：
| 包 | 恶意版 | 安全版 |
|:---|:---|:---|
| keyv | 6.0.0 | 5.6.0 |
| flat-cache | 6.1.24 | 6.1.23 |
| file-entry-cache | 11.1.6 | 11.1.5 |
| cacheable-request | 13.0.20 | 13.0.19 |
| cacheable 系全部 | 2.5.1 | 2.5.0 |

**排查**：setup.mjs / Math_Symbol.js / math_init.js 文件、`preinstall: node setup.mjs` hook、`.claude`/`.vscode` hook、bun 进程（非 bun 项目出现 bun=异常）、`npm-cache[.]com` 流量。

**✅ 本机实测：未感染**（墨题/hermes-agent/Sims4/.openclaw 四处全净 + npm 12.0.2 默认拦截 preinstall + 无 .npmrc token）

### 🟠 2. 勒索软件（Q2 2026）
- **Top 3**：Qilin（279 受害者，连续 4 季第一）、The Gentlemen（+62%）、CRPx0（7 月 46 受害者）
- 支付率降至 23%（六年连降，备份有效），但 2025 链上支付仍超 **$8.2 亿**
- 转向「**先窃数据再加密**」——备份救不了数据泄露
- INC Ransom 利用 SonicWall SMA 1000 漏洞（CVE-2026-15409/15410）建立 root 权限

### 🟡 3. 僵尸网络（IoT 为主）
- **Dysphoria**（CNCERT 2026-07-27）：20 万+ bot，ENS/SNS 区块链域名 C2，受害者主机转中继节点，Telnet/SSH 弱口令传播
- **RCtea**：RC4/ChaCha20/TEA 深度加密，针对 ARM/MIPS IoT 设备，DDoS 能力成熟
- **「独狼」团伙**：非官方下载站捆绑热门软件（搜狗输入法/五笔/QQ音乐）→ 盗抖音/B站/小红书账号 + 刷流量（**下载软件只走官网**）

## 三、预防清单（按优先级）

### 🥇 立即做（本机已做）
| 项 | 状态 |
|:---|:---|
| npm 升级 ≥12（拦 preinstall hook）| ✅ 12.0.2 |
| 关键项目扫描 Shai-Hulud | ✅ 全净 |
| .npmrc 不存 token | ✅ 无 |
| 软件只从官网/可信源下载（防「独狼」）| ⚠️ 需保持 |

### 🥈 日常习惯
1. **不明命令绝不粘贴执行**（ClickFix）——先粘记事本看内容
2. **密码 ≥16 位混合**，不用弱口令（防僵尸网络 Telnet/SSH 爆破）——路由器/摄像头默认密码必改
3. **重要账号开 2FA + 定期查异常登录**
4. **不在 .env 明文存 key**（Shai-Hulud 会扫 .env/.pem/.kdbx/.ovpn）
5. **定期全盘杀毒** + 下载后校验 HASH
6. **npm 装包加 `--ignore-scripts`**（新项目/可疑包）或延迟升级（让社区先发现投毒）

### 🥉 开发环境加固（你的场景）
- npm 包延迟升级策略：**新版本发布后等 2-7 天再升**（让社区先抓投毒）——Elastic 建议
- 检查 GitHub 仓库有无异常 commit（作者 claude、消息 `chore: update config`）
- AI agent（claude/codex/dsh）工作目录的 `.claude/settings.json` / `.vscode/tasks.json` 定期检查
- npm 账号开 2FA，自动化 token 不用 `bypass_2fa`
- 备份：**3-2-1 原则**（3 份副本、2 种介质、1 份异地）——勒索软件最后防线

## 四、AI 博主角度
- 主题：**「AI 时代的供应链攻击」**——Shai-Hulud 是首个大规模利用 AI agent hook（.claude/）传播的病毒，天然有传播度
- 角度：AI 开发者（用 claude/codex/dsh 的人）是 Shai-Hulud 头号目标——你的受众画像完全吻合
- 实测素材：本地扫描演示（本文档的检测脚本思路可做成视频）

## 结论
- **最该警惕**：Shai-Hulud npm 供应链蠕虫（8 月爆发，专偷开发者/AI 工具凭据）——本机已确认安全
- **最该改习惯**：不明命令不粘贴 + 软件只走官网 + 强密码 + 2FA
- **最该保持**：npm 12+、定期扫描、延迟升级、3-2-1 备份
