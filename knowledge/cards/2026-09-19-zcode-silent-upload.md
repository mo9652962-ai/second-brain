---
aliases:
  - 2026-09-19-card-zcode-silent-upload
tags: [knowledge-card, security, privacy, ai-coding, zcode, supply-chain]
created: 2026-09-19
source: "[[knowledge/Daily/hackernews-2026-09-19]]"
status: fresh
---

# 🃏 知识卡片 · ZCode 静默上传整个工作区 + Git 历史——本机实锤：墨题仓库已被打包待传

> **来源**：ferstar 逆向文《Inside ZCode: Silently Uploading Your Entire Git History to the Cloud》（09-18）· HN 09-19 #7 · ✅ ferstar 原文 web_extract + tokenstead/runtimewire/frame-press 三源交叉 + **本机 `~/.zcode` 实锤核验**
> **一句话**：**ZCode（智谱官方 AI 编码桌面端）只要登录，就无条件把整个工作区 + 完整 `.git` 历史加密打包上传阿里云 OSS，任何 UI 开关都关不掉**——而 sora 本机已发现墨题仓库 131MB 加密快照 pending 待传。

---

## 核心洞察 / 影响

| 维度 | 内容 |
|------|------|
| 行为 | 登录即静默打包：完整 `.git` 历史 + LFS 缓存 + reflogs + 全局配置 → 加密 → 直传阿里云 OSS（绕过自家服务器直传） |
| 加密 | 信封加密：AES-256-CTR + RSA-OAEP，公钥由服务器下发、私钥只在云端——**本机自己都无法解密自己的快照** |
| 开关 | 「优化体验」只管训练授权、「快照索引」只管服务端索引——**两个开关都关不掉打包上传**；捕获端 sidecar 启动时无条件实例化 |
| 泄露面 | `.git` 占 86.6%：历史 API key、未推送分支名、内网 GitLab 主机名全在包里；删除本地快照半小时内会重新打包（打地鼠无效） |

## 本机实锤（2026-09-19 13:00 核验，✅ 官方源路径）

1. ⚠️ **墨题仓库（D:\english-multiple-choice-practice-machine）已被打包**：`~/.zcode/v2/checkpoints/57bb190b8316/pending/` 有 **131,814,270 字节（126MB）`tar.gz.enc`** + envelope.json，state.json 记录 `workspacePath=墨题路径`、`captureStage: "prompt"`、**失败 18 次未上传成功**（09-12 生成）——manifest 明文列了 `.git/` 全套 + `.agents/skills/` + 全局配置
2. ⚠️ **默认工作区已成功上传**：`287edfac5559/state.json` 有 `lastAcceptedManifestHash`（= 服务器已确认收到）——说明上传通道是通的，墨题快照只是暂时因失败滞留，**网络恢复/重试可能补传**
3. ✅ 结论：sora 本机 ZCode 数据根 584MB，行为与 ferstar 逆向完全一致

## 关键数据 / 对 sora 的影响

1. 🔴 **立即动作**：ZCode 已登录 + 本机有墨题加密快照待传——**先退出 ZCode 登录**（无 JWT 即不捕获），再决定卸载 or 锁目录
2. ⚠️ **墨题仓库假设已泄露**：默认工作区上传成功证明通道可用；墨题 `.git` 若含历史敏感 key/路径，按已泄露处置（轮换 key、清 .git 历史）
3. 💡 **替代方案**：sora 已用 Codex CLI（本地纯执行）+ Hermes 委派——ZCode 冗余且危险，卸载即可闭环

## 行动项

- [x] 本机核验：`~/.zcode` 存在、checkpoints 有 2 个 workspace、墨题 126MB 加密快照 + 默认工作区已上传 ✅ 2026-09-19 13:00
- [x] 知识落库：本卡片 + HN 09-19 源 ✅ 2026-09-19
- [ ] **sora 操作（🔴 P0）**：退出 ZCode 登录 → 卸载 ZCode（已不用，Codex 替代）→ 删除 `~/.zcode` 剩余快照 → 墨题 git 历史轮换敏感信息
- [ ] 防御可选（若暂不卸载）：Windows 锁目录 `icacls "%USERPROFILE%\.zcode\v2\checkpoints" /deny <USER>:(W)` 阻断写入（等价 ferstar 的 chattr/chflags 方案）

## 为什么重要

- **时效性**：09-18 逆向文 + 09-19 HN 热榜（277 分）当日入库
- **业务相关性**：直接命中 sora 生产工具链——墨题仓库 = 商业项目源码 + 技能体系，被静默打包待传是真实泄露风险，不是概念新闻
- **可行动性**：本机证据链完整，处置路径清晰（退出登录→卸载→清残留）

---

*卡片来源：当天知识库精选 · HN 09-19（🥇 本机实锤 + 直接威胁墨题源码，压过同天 arXiv/HN 其余条目）*
