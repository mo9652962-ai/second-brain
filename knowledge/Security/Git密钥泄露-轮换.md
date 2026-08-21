---
tags: [安全, git, 密钥泄露, .env, 轮换, 爬虫]
domain: Security
status: fresh
date: 2026-08-21
---

# Git 历史泄密：密钥不是配置（程序员Orion · 抖音 2026-08-21）

> 来源：抖音 @程序员Orion（创业中）《你以为代码删了就安全？Git 历史早就把你的数据库...》（1:XX）
> 转写 485 字（SenseVoice）

## 事故

```
.env 写数据库密码/短信密钥/支付回调密钥 → git add 全提交
→ 黑客爬虫 24h 盯着 GitHub → 全站命脉挂互联网
→ 删文件重新提交 = 没用! Git 历史里清清楚楚躺着旧代码
```

## 保命三连

```
① .gitignore 永远立刻马上加 .env/*.env（提交前）
② 仓库只放变量名, 绝不写真密钥（配置模板 .env.example）
③ 一旦泄露 → 去云厂商后台轮换重置密钥（不是删文件完事）
```

> 金句：密钥不是配置，是系统的命脉。代码泄了能修，密钥泄了别人能直接替你花钱、删库、跑路。

## 落地检查

```
□ .gitignore 含 .env / *.env / config.local.*
□ git log --all --diff-filter=D 查历史有无密钥文件
□ git filter-repo / BFG 清理已泄露历史（或直接轮换密钥）
□ 密钥放环境变量/密钥管理服务（Vault/云 KMS）
```

## 关联

- `Development/写码前扫坑清单.md`（第 21 项）
- Hermes redact_secrets 已开（8-20）— 输出侧防泄
- `ai-agent-security-audit` 技能（供应链/凭据审计）
