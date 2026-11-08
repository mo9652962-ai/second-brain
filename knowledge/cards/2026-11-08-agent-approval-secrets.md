---
aliases:
  - 2026-11-08-card-agent-approval-secrets
tags: [knowledge-card, security, secrets, coding-agent, scanner-blindspot]
created: 2026-11-08
source: "[[knowledge/Daily/hackernews-2026-11-08]]（HN 315 分）+ Apiiro 原始研究经 5 家独立媒体交叉核对 + 本机仓库实测"
status: fresh
---

# 🃏 知识卡片 · 一次「别再问我」，把密码写进了公开仓库

> **一句话**：编码 agent 的「别再问我」按钮会把**整条命令原文**存成权限规则——密码跟着一起存；而 gitleaks / TruffleHog 只认「钥匙的形状」，不认「钥匙在命令里」，1,122 份泄露文件里 **215 份（约 1/5）两个扫描器都没抓到**。

---

## 一、事情本身（观察）

| 项 | 数值 | 口径 |
|:--|:--|:--|
| 公开 `.claude/settings.local.json` 份数 | **104,185** 份 / 103,617 个仓库 | GitHub code search，2026-11-01~03 抓取 |
| 含真实凭据的文件 | **1,122** 份（1.1%），共 **1,379** 个凭据 | Apiiro 分类：匹配已知密钥格式，或密码/令牌挨着公网主机 |
| 计入历史版本 + 共享 settings.json + agent 转录 | **2,539** 个凭据 / **1,994** 个仓库 | 历史部分是下限 |
| 构成 | 379 DB 密码 · 122 Supabase service-role · 149 AI 模型 key · 43 SSH · 42 GitHub/GitLab/npm · 23 AWS · 6 私钥 | 直接开数据库的占 1/3 以上 |
| 滞留时长 | 中位 **217 天**仍在默认分支，118 个仓库超一年 | 删文件不解决问题：734 个凭据只活在历史里，211 个 fork 带着同样的凭据 |
| 谁提交的 | 1,105 个仓库里 **539** 个（49%）有「Claude 共同作者」的提交改过这个文件 | 只说明它在场，不证明是它敲的密码 |
| 扫描器表现 | gitleaks 抓到 564 / TruffleHog 643 / **两个都没抓到 215** | 都不带验证步骤跑 |

**机制**：Claude Code 默认跑 shell 命令前要问一句。选「Yes, and don't ask again」，它就把**这条命令字符串本身**写成 allow 规则存进项目里的 `.claude/settings.local.json`。你让它排查 staging 登录失败，它读配置拼出 `PGPASSWORD=真实密码 psql -h ...`——这条命令被完整存下来，明文。

**为什么扫描器漏**：gitleaks / TruffleHog 找的是 `sk-`、`AKIA` 前缀或高熵长串。而 `PGPASSWORD=xxx`、`sshpass -p xxx`、`mysql -p xxx`、`curl -H "Authorization: Bearer xxx"` 里的密码，在词法上就是「命令行里一个普通单词」。

## 二、最要命的一条设计缺陷（观察，Anthropic 文档自认）

Claude Code 首次创建这个文件时，会把它写进**用户本机的全局 git excludes**（`core.excludesFile` 或 `~/.config/git/ignore`），**从不写进仓库自己的 `.gitignore`**。

于是保护只挂在「这台机器、这个用户」身上，四个缺口全开：

1. 文件先存在、目录后变成 git 仓库 → 不覆盖
2. 别人 clone 你的仓库 → 他那台机器没有这条 exclude
3. 文件已经提交过 → 加多少 exclude 都拦不住
4. 仓库自己的 `.gitignore` 里什么都没有 → 保护不随项目走

## 三、本机核对（观察，2026-11-08 实测）

| 检查项 | 结果 |
|:--|:--|
| 已跟踪的 `.claude/settings.json`、`.codebuddy/settings.json`、`.qoder/settings.json` | **干净**：只有 hooks（code-review-graph 触发），无 `permissions`、无任何凭据 |
| 全库 `settings.local.json` | **0 个**（find 全库无命中） |
| git 历史是否出现过 | **从未**（`git log --all --diff-filter=A -- "*settings.local.json"` 空） |
| `.gitignore` 是否含 agent 配置规则 | **没有**（grep `claude\|settings` 0 命中）——下一次真生成就裸奔 |
| `core.excludesFile` | 未配置，`~/.config/git/ignore` 不存在 → 本机连那层全局保护都还没有 |
| `scripts/check-repo-privacy.py`（83 行） | 只扫学校名/手机号/本机路径/内网 IP/密钥**关键字**；**无** `PGPASSWORD=`/`sshpass -p`/`Bearer`/`sk-`/`AKIA` 规则 → 同类盲区 |

**推断**：我的门禁防的是「我是谁」（身份/路径），不防「我的钥匙」。身份泄露我一直在拦，凭据泄露一次都没扫过——而 agent 配置文件正好是钥匙最爱落地的地方。

## 四、行动项

- [x] `.gitignore` 补 `**/.claude/settings.local.json`（2026-11-08 已加，防下一次裸奔）
- [ ] 门禁加「命令内嵌凭据」规则（`PGPASSWORD=`、`sshpass -p`、`mysql -p`、`Bearer <20+ 字符>`、`sk-`、`AKIA`）——**暂未自动改**：本库 skill 文档里有大量命令示例，直接加会大面积误报，需先加白名单再上
- [ ] 批准时给**模式**不给整条命令（`Bash(npm run:*)`），密码走变量（`$DB_URL`），让存下来的规则里只有变量名
- [ ] 真进过仓库的凭据：**先轮换，再清理**——历史版本和 fork 都留着，删文件是假的

## 五、证据分级

| 档位 | 内容 |
|:--|:--|
| **观察** | 数字均来自 Apiiro 2026-11-05 原始研究，经 The Hacker News / cybersecuritynews / aiweekly / devlery / ctxsec 五家独立转述一致；「只写全局 excludes 不写仓库 .gitignore」有 Anthropic 官方 settings 文档背书。本机六项核对为上表实测输出 |
| **推断** | 「1,122 份只是冰山」——Apiiro 明说没统计留在本机、没上 GitHub 的文件，而它认为那才是大头；「我的门禁会漏这类泄露」按脚本 83 行实读推断，未构造样本实测 |
| **未知** | 1,379 个凭据里有多少**还有效**（Apiiro 未使用任何凭据，仅 1 家企业确认自己的 key 仍然活着）；本机其他项目目录里是否已生成过 `settings.local.json`（只扫了本仓库） |

## 六、为什么值得记

这不是「谁的 bug」，是**权限系统的通病**：把「你批准过什么」记成明文，就等于把当时的上下文（含密码）一起归档。同类落点还有：agent 转录、memory 文件、handoff 笔记——凡是「记录我干过什么」的地方，都会顺手记录「我用的凭据」。

判据一句话：**看一个安全扫描器好不好，不看它抓了多少，看它认不认「人类手打的那半句」**。格式化的密钥好抓，命令行中间的密码才是常态。

---

## 📱 微信推送版（可直接复制）

今天 HN 上有一条 315 分的安全研究，我顺着查到原始报告，然后回头扫了自己的仓库。

事情是这样的：用 Claude Code 跑命令时，它每次都会问「要不要执行」。有个选项叫「是，别再问我了」。你点了它，它就把这条命令的**原文**存成一个权限规则，下次自动跑。

问题是，你让它排查数据库连不上的时候，它拼出来的命令长这样：`PGPASSWORD=真实密码 psql -h ...`。因为不带密码这条命令根本跑不起来。于是你点一下「别再问我」，这串密码就明文躺进了项目里的一个 JSON 文件。

Apiiro 在 GitHub 上搜了这个文件，找到 10 万份公开的。其中 1,122 份里含真实凭据，一共 1,379 个：379 个数据库密码、122 个 Supabase 服务密钥、149 个 AI 模型 key、43 个 SSH、23 个 AWS。一半的仓库里，这东西已经挂了 217 天以上。

最扎心的是扫描器。他们拿 gitleaks 和 TruffleHog 去扫这 1,122 份：gitleaks 抓到 564，TruffleHog 抓到 643，**两个都没抓到的有 215 份，大约五分之一**。原因是扫描器认的是钥匙的形状——sk- 开头、AKIA 开头、一长串乱码。可 `PGPASSWORD=` 后面那串密码，在语法上就是命令行里一个普通单词。

还有个设计细节：Claude Code 会把这个文件加进你**本机**的 git 忽略列表，但从不会写进仓库自己的 .gitignore。所以保护只在你这一台机器上，别人 clone 你的仓库、或者文件已经提交过一次，这层保护就等于没有。

我查了自己的仓库：已跟踪的三个 agent 配置文件里只有 hooks，没有权限规则、没有凭据；历史上也从没提交过这个文件。但 .gitignore 里一条相关规则都没有——也就是说下一次真生成，它就是裸的。我把这条忽略规则加上了。

顺带发现一件更值得说的事：我自己的隐私门禁，扫的是学校名、手机号、本机路径、内网 IP。它防的是「我是谁」，从来没防过「我的钥匙」。身份泄露我拦了几个月，凭据泄露一次都没扫过。

所以今天记住两句话：批准命令时给模式不给整条命令，密码走变量；万一真进过仓库，先轮换再清理——删文件没用，历史版本和 fork 里都还在。

（数据：Apiiro 2026-11-05 研究，GitHub 2026-11-01~03 抓取，10.4 万份文件样本。）

---

*卡片来源：今日 `knowledge/Daily/hackernews-2026-11-08.md` 第 6 条 → 回查 Apiiro 原始研究（页面为 JS 渲染，正文取不到，改用 5 家独立转述交叉核对数字）+ 本机仓库六项实测。次选候选：MaxxBench（改写 89 个 DeepSWE 任务后，模型为了迎合「想象中的评分器」删掉自己正确的代码）。*
