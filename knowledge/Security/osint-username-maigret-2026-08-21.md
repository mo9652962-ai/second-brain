---
tags: [osint, maigret, 用户名搜索, 信息收集, 网安]
domain: Security
status: fresh
date: 2026-08-21
---

# OSINT 用户名搜索笔记（我是王青青 · 抖音 2026-08-21）

> 来源：抖音 @我是王青青《互联网侦探：只输入一个用户名，就能扫描 840 多...》（36 秒，07/10）——SenseVoice 转写 333 字
> 工具实证：**Maigret**（soxoj/maigret，Sherlock ML 改进 fork，3000+ 站点，无 API key）
> 技能：`security/osint-username-search`（已建）

## 视频要点

1. 输入用户名 → 自动扫描（视频说 840+ 平台，现 Maigret 已支持 **3000+**）
2. **不是简单同名判断**——ML + 30 维度特征（网页结构/关键词/跳转记录/头像/简介/共享链接交叉比对）
3. 判断「真实存在 vs 同名误判」——哪怕网站改版藏得深也能识别
4. 支持多用户名同时查、指定平台、自己添加平台规则
5. 查自己 → 发现随手注册的用户名留下多少公开痕迹
6. 合规提醒：公开信息 ≠ 可以随便用

## Maigret 关键能力（README 实证）

| 能力 | 说明 |
|:---|:---|
| 站点数 | 3000+（默认扫 500 热门，`-a` 全扫）|
| ML 判断 | 特征交叉比对，降低同名误判 |
| 递归搜索 | 从主页提取关联账号/用户名 → 自动继续搜 |
| 标签过滤 | `--tags photo,dating,us` 等 |
| AI 报告 | `--ai` 用 OpenAI 兼容 API 生成调查摘要（本地 DeepSeek 可配）|
| 输出 | HTML/PDF/JSON 报告 |
| 其他 | Tor/I2P、反爬处理、站点库每日自动更新 |

## 用法速查

```bash
pip install maigret
maigret 用户名                    # 默认 500 站
maigret user1 user2 -a           # 多用户全站
maigret user --tags photo        # 分类过滤
maigret --parse <主页URL> --recursive  # 递归搜索
maigret user --ai                # AI 调查摘要
```

## 对 SRC 侦察链的价值

```
子域枚举 → Nmap 端口 → 【Maigret 人员画像】→ 平台账号 → 社工/泄露 → 漏洞
```

## 关联

- [[src-recon-scanning]]（资产层）· [[nmap-scanning]]（端口层）· [[src-bug-hunting]]
- 技能：`security/osint-username-search`

---
*k (Hermes) 2026-08-21 · SenseVoice 转写 + 工具实证*
