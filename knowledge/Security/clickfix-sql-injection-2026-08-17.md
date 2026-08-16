---
tags: [网络安全, ClickFix, SQL注入, 研究笔记, 2026-08]
domain: Security
---

# ClickFix 钓鱼 + SQL 注入 学习研究（2026-08-17）

> 来源：抖音科普视频（南瓜的网安日记 / 网安视野）
> 方法：web_search 深挖（微软安全博客/阿里云/OWASP/HKCERT 实证）+ 墨题代码安全审计
> 相关: [[agent-infra-weekly-2026-08-17]]

## 一、ClickFix——「复制粘贴一下，电脑就被控制」

### 核心原理（颠覆传统钓鱼）
**传统钓鱼**：诱导你输入账号密码 → 表单提交 → 窃取凭证
**ClickFix**：不偷密码，**让你亲手执行恶意命令**——「用户协同入侵」

### 攻击链（4 阶段）
| 阶段 | 手法 |
|:---|:---|
| 1. 诱饵 | 伪造人机验证/系统报错/流媒体解锁弹窗（高仿 Cloudflare Turnstile、Google reCAPTCHA、Discord）|
| 2. 剪贴板劫持 | 页面 JS **静默**写入恶意 PowerShell 命令到剪贴板（`navigator.clipboard.writeText`，无弹窗）|
| 3. 诱导执行 | 引导你按 Win+R → Ctrl+V 粘贴 → Enter——**你自己执行了攻击代码** |
| 4. 载荷投递 | PowerShell/CMD/mshta 等 LOLBins 下载内存载荷 → 远控/窃密/勒索 |

### 为什么难防
- 无恶意文件落地（LOLBins 系统自带程序）→ 静态杀毒失效
- 剪贴板劫持是 JS 静默操作 → URL 检测/页面扫描失效
- 命令是**用户主动执行** → 自动化检测失效（2025 初微软实测：EDR 开着也挡不住，数千设备/月被攻破）

### 2026 最新变种
- **macOS 版**：假 CAPTCHA → 诱导粘贴 curl 命令 → 装 Infinity Stealer（Python 窃密器）
- **rundll32 + WebDAV**：Windows 版改用 DLL 加载，更隐蔽
- 已占恶意软件加载网络攻击的 **50%+**

### 个人防护（对你最实用）
1. **绝不**在 Win+R / Terminal / PowerShell 里粘贴网页让你复制的命令——除非你逐字看懂它在干什么
2. 看剪贴板内容再贴：先粘贴到**记事本**检查，确认是网址/文本而非 `powershell`/`curl`/`iex` 开头
3. 真正常见的「人机验证」从不需要你打开运行窗口
4. 可疑「验证」页面 → 直接关掉，去官网找官方入口
5. Opera 已内置 Paste Protect（粘贴防护）——其他浏览器可关注类似功能
6. **你常从网上复制命令跑**（教程/脚本）——这是高风险习惯：优先从可信源（官方 README/GitHub 已审）复制，陌生博客的命令先拆解看内容

### 企业/个人终端加固
- 禁用 Win+R（组策略：Start Menu and Taskbar → Remove Run menu）
- PowerShell 脚本块日志（Script Block Logging）+ 执行策略 AllSigned
- 终端行为检测：Win+R 创建 + 剪贴粘贴 + PowerShell 外网请求 = 高危告警

## 二、SQL 注入——不用密码也能登录

### 原理（一句话）
**数据库把用户输入当成了 SQL 代码执行**——因为程序把输入拼接进了查询字符串。

### 经典绕过登录（华为/OWASP 示例）
```sql
-- 原查询（字符串拼接，危险）
SELECT * FROM users WHERE user='admin' AND pass='xxx'

-- 密码输入: 1' or 'a'='a
SELECT * FROM users WHERE user='admin' AND pass='1' or 'a'='a'
-- 先算 AND 再算 OR → 整体为 True → 绕过登录！
```

### 为什么「不用密码也能登录」
`' OR '1'='1` 这类 payload 让 WHERE 条件恒真 → 返回第一行用户（通常是 admin）→ 直接进系统。

### 注入类型
| 类型 | 手法 |
|:---|:---|
| 联合注入 UNION | 拼 SQL 把其他表数据并进来（偷全库）|
| 布尔盲注 | 页面 True/False 差异逐位猜数据 |
| 时间盲注 | 响应延迟判断（SLEEP()）|
| 报错注入 | 数据库错误信息泄露表结构 |
| 二阶注入 | 先存脏数据到库，下次查询触发 |

### 防御（核心 = 参数化查询）
```python
# ❌ 危险：字符串拼接
sql = f"SELECT * FROM users WHERE email='{email}'"

# ✅ 安全：参数化（代码与数据分离）
stmt = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
```
- **参数化查询 / Prepared Statements** = 根本解法（数据库永远区分代码和数据）
- **最小权限**：数据库账号只给所需权限（登录接口只读，不给 DELETE）
- 表名/列名/排序方向不能用值参数 → 用**白名单映射**
- WAF/输入过滤只是辅助（可绕过），不是主要防御
- 关闭生产环境详细报错（防报错注入泄露结构）

## 三、墨题代码审计（实证 apply）

扫描 D:\english-multiple-choice-practice-machine：
| 位置 | 写法 | 结论 |
|:---|:---|:---|
| 后端 database.py PRAGMA | f-string 表名来自硬编码元组 | ✅ 安全 |
| 后端 version.py 哈希 | 表名硬编码 ("questions","options","vocabulary_entries") | ✅ 安全 |
| 后端 vocabulary.py UPDATE | 字段名有 allowed 白名单 + 值全 `?` | ✅ 安全 |
| 前端 api-adapter.ts (sql.js) | 全部 `?` 参数化占位 | ✅ 安全 |

**墨题 SQL 注入防护 ✅ 无注入面**（SQLite 本地库 + 参数化 + 白名单，符合最佳实践）。

## 四、AI 博主角度（可做内容）
这两个主题是**网安科普的经典爆款选题**：
1. ClickFix——「复制粘贴就被控」猎奇感强 + 2025-2026 真实爆发 + 有微软/俄亥俄大学实证案例 → 适合做短视频脚本
2. SQL 注入——「不用密码登录」反常识 + 原理可视化（拼 SQL 的过程动画）→ 入门级网安教学
3. 结合实操：本地搭 DVWA 演示（TrueSight 有 2026 版指南）→ 演示视频更有说服力
4. 差异化角度：从「AI 时代的安全」切入——AI agent 帮你复制命令执行（Hermes/dsh 场景）如何保证安全 → 与你的 AI 自动化博主定位契合

## 结论
- ClickFix = 2026 最需警惕的钓鱼变种，核心是「**不明命令绝不粘贴执行**」——你的高危习惯要改
- SQL 注入 = 最老牌 Web 漏洞，防御核心就一条：**参数化查询**
- 墨题代码安全 ✅（已审计）
