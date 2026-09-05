---
tags: [MOC, security, 网络安全, 索引]
aliases: [安全地图, Security MOC, 网络安全 MOC]
domain: Security
type: moc
status: active
created: 2026-08-16
updated: 2026-08-31
---

# 🛡️ 网络安全 MOC — Security Map

> 网络安全主题的总入口：威胁研究 / Web 安全 / Agent 安全 / 本机加固 / 合规。
> [[knowledge-map|🗺️ 知识地图]] · [[MOC-Research|🔬 Research MOC]] · [[MOC-GitHub|🐙 GitHub 研究 MOC]]

**共 23 篇相关笔记** · 最后更新：2026-08-18（本 MOC 随《知识库重构方案(已删)》创建，收拢散落在 Security / Research / cards / Dev 四处的安全主题笔记）

---

## 🔴 威胁与攻击研究（域内正编）

- [[virus-threats-2026-08-17]] — **2026 病毒威胁全景**：Shai-Hulud npm 供应链蠕虫（专偷 AI 工具凭据，本机已扫描确认安全）+ 勒索/僵尸网络态势 + 预防清单三级优先
- [[clickfix-sql-injection-2026-08-17]] — **ClickFix 钓鱼 + SQL 注入**：剪贴板劫持让用户亲手执行恶意命令；参数化查询是注入根本解；含墨题代码审计实证（✅ 无注入面）
- [[silver-fox-defense-2026-08-17]] — **银狐木马防御**：识别特征 + 预防清单 + 应急处置 8 步 + 原理拆解（本机已排查）

## 🌐 Web 安全 / SRC 挖洞

- [[src-bug-hunting-2026-08-17]] — SRC 漏洞挖掘实战方法论：平台选型 + 5 类新手漏洞 + 六步流程 + 报告模板
- [[src-hunting-earnings-2026-08-17]] — SRC 挖洞收益路径：0-1 月入门 → 3 月+ 冲击高危；只挖授权范围

- [[Security/SRC批量初筛最小闭环验证-真洞转化率趋零-2026-09-02]]
## 🤖 Agent / AI 安全线（跨域收拢）

- [[agent-memory-injection-2026-08-05]] — Agent 记忆注入攻击：查询只读注入，记忆是攻击面
- [[kutie-context-injection]] — KuTIE 论文跟踪：运行时拓扑上下文能否改进 LLM 生成的 Kubernetes 安全补丁（arXiv 2607.25995）
- [[2026-08-05-zero-mem|卡片：Zero-Mem]] — 零 token 记忆架构；反向警示 ICLR 2026 Memory Injection Attacks（记忆操作即攻击面）
- [[10-Top-AI-Agent-Projects-Deep-Research]] — Top10 Agent 项目深研：含 ClawHavoc 供应链攻击、审计发现 12% 技能为恶意的生态风险段

- [[Security/hermes-codex-security-policy-2026-09-04]]
## 🏠 本机与运维安全

- [[security-risk-assessment-2026-08-02]] — 落实项目风险评估：网关 18789 / ComfyUI 8188 均仅监听 127.0.0.1（对照 OpenClaw 85% 实例暴露公网的教训），3 个待加固风险点

## ⚖️ 合规

- [[eu-ai-act-2026-08-assessment]] — EU AI Act 2026-08-02 生效的多 Agent 场景合规评估
- [[2026-08-02-eu-ai-act|卡片：EU AI Act]] — 生效要点速记

## 🔗 相关（跨域引用）

- [[claude-max-sepa-incident-2026-07-26]] — Claude Max 20x 扣费支付漏洞事件研究（incident 类）
- [[agent-infra-weekly-2026-08-17]] — Agent 基建化周榜（clickfix 研究的相关来源）
- [[hermes-mcp-architecture]] — MCP 架构对比中的供应链攻击风险 vs 零 CVE 自生成方案

---

## ✅ 本机防护状态速查（由上列笔记汇总裁止 2026-08-16）

| 项 | 状态 | 来源 |
|:---|:---|:---|
| npm ≥ 12（拦 preinstall hook） | ✅ 12.0.2 | [[virus-threats-2026-08-17]] |
| Shai-Hulud 四项目扫描 | ✅ 全净 | 同上 |
| .npmrc 不存 token | ✅ | 同上 |
| 本地服务不出公网（127.0.0.1） | ✅ | [[security-risk-assessment-2026-08-02]] |
| 不明命令不粘贴（ClickFix） | ⚠️ 习惯项 | [[clickfix-sql-injection-2026-08-17]] |
| 密码 ≥16 位 + 2FA + 3-2-1 备份 | ⚠️ 持续保持 | [[virus-threats-2026-08-17]] |

## 📌 待办（引用重构方案）

1. ~~5 篇安全笔记从 Research/ 迁入 Security/（方案·迁移清单(原为知识库重构方案章节) #3~#7）~~ → ✅ **2026-08-23 已执行**：Research/ 已无安全笔记（grep 实证），Security/ 现有 40+ 篇（含 8-17~8-22 全部新增），迁移完成
2. 新安全笔记落盘时挂本 MOC；威胁类命名统一 `威胁名-YYYY-MM-DD` → ✅ **持续生效**：8-17 起新增 8 篇均按此约定命名并挂 MOC（见下方 🆕 列表）

## 🆕 2026-08-17/18 新增（8 篇）

- [[knowledge/Security/dvwa-practice-2026-08-17|DVWA 靶场实战]] — 七漏洞全通关
- [[knowledge/Security/src-bounty-and-boundaries-2026-08-17|挖洞平台收益机制 + 安全边界]] — 千轮研究沉淀
- [[knowledge/Security/logic-vulns-first-order-2026-08-18|逻辑漏洞 + 首单流程]] — 千轮研究
- [[knowledge/Security/privesc-lateral-movement-2026-08-18|提权 + 内网渗透]] — 系统性知识
- [[knowledge/Security/ai-enhanced-pipeline-2026-08-18|AI 增强挖洞流水线]] — 落地
- [[knowledge/Security/browser-search-automation-2026-08-18|浏览器搜索 + 自动化增强]] — 千轮研究
- [[knowledge/Security/local-hardening-report-2026-08-18|本机安全加固检查报告]]
- [[knowledge/Security/defense-capabilities-2026-08-18|防御能力研究]] — 八轮千轮研究

## 🆕 2026-08-21 新增（接口安全系列 + 部署安全 — 攻防一体）

> 程序员Orion + 千轮研究（OWASP Top10 2025 验证）——每篇都是双杀：接单交付对照 + SRC 武器库。

- [[knowledge/Security/文件上传四层检查-攻防一体|文件上传四层检查]] — webshell 伪装后缀 → 白名单/随机名/物理分离
- [[knowledge/Security/验证码接口防护-限流熔断|验证码限流熔断]] — 短信轰炸防御（后端 4 层保护）
- [[knowledge/Security/数据库公网裸奔-找死|数据库公网裸奔]] — 3306 暴露 → VPC 私有子网
- [[knowledge/Security/SQL注入-参数化查询|SQL 注入参数化]] — 手动拼接=扔炸弹，ORM 非免死金牌
- [[knowledge/Security/Git密钥泄露-轮换|Git 历史泄密]] — .env 提交 → 密钥轮换
- [[knowledge/Security/OSS公共读-隐私泄露|OSS 公共读]] — 公私分桶 + 签名 URL
- [[knowledge/Security/日志泄露-脱敏|日志脱敏]] — 统一 Logger + 敏感字段脱敏

## 🆕 2026-08-18 补遗 + 08-19/20 新增（SRC 进阶 + 逆向 + 学习路线）

> 联想 SRC 实战 + 报告规范 + 网安学习路线 + 逆向（VMP/SO）——SRC 从入门到报告的链路补全。

- [[knowledge/Security/ai-redteam-tools-compare-2026-08-18|AI 红队工作台全景对比]] — 红队工具横向
- [[knowledge/Security/src-info-leak-first-order-sop-2026-08-18|SRC 信息泄露首单 SOP]] — 双视频学习沉淀
- [[knowledge/Security/src-newbie-guide-2026-08-19|SRC 新手从 0 到第一个洞]] — 入门链路
- [[knowledge/Security/src-report-format-2026-08-19|漏洞报告格式规范]] — 补天 2026-07 公告
- [[knowledge/Security/lenovo-src-assets-2026-08-19|联想 SRC 子域名资产清单]] — 资产测绘实战
- [[knowledge/Security/lenovo-src-recon-2026-08-19|联想 SRC 侦察报告]] — 侦察流程
- [[knowledge/Security/nmap-tutorial-2026-08-20|Nmap 保姆级教程]] — 端口扫描（安全小子）
- [[knowledge/Security/网安自学避坑-2026-08-20|网安自学 7 坑]] — 避坑（网络安全黑卡）
- [[knowledge/Security/cybersec-entry-path-2026-08-18|双非本科入局网安]] — 视频学习笔记
- [[knowledge/Security/cybersecurity-offer-path-2026-08-18|网安 Offer 路径研究]] — 就业路径
- [[knowledge/Security/cyber-skills-817-compare-2026-08-20|817 网安技能库对照]] — 技能对照
- [[knowledge/Security/vmp-reversing-2026-08-20|VMP 脱壳学习]] — 逆向（洛洛-软件开发）
- [[knowledge/Security/android-so-vmp-reversing-2026-08-20|安卓 SO 层 VMP 逆向]] — 千轮研究

## 🆕 2026-08-21/22 新增（SRC 自动化 + 攻防实战 + 墨题自查）

> 程序员Orion 接口安全系列（攻防一体）+ SRC 自动化三工具 + 校园便利盒挖洞实战 + 墨题安全自审/防破解。

- [[knowledge/Security/osint-username-maigret-2026-08-21|OSINT 用户名搜索]] — Maigret 3000+ 平台（我是王青青）
- [[knowledge/Security/src-3month-roadmap-2026-08-21|SRC 3 个月路线 + 业务逻辑靶场]] — 路线图（周小粥）
- [[knowledge/Security/src-ai-automation-3tools-2026-08-21|SRC 自动化挖洞三工具]] — VulnClaw/SRC-Hunter/AutoSRC 落地
- [[knowledge/Security/接口三件套-攻防一体|接口三件套]] — 鉴权/限流/幂等攻防（程序员Orion）
- [[knowledge/Security/前端隐藏不等于安全-后端鉴权|前端隐藏 ≠ 安全]] — 后端鉴权才是真（程序员Orion）
- [[knowledge/Security/换订单号拿别人数据-IDOR|IDOR 越权]] — 换订单号拿别人数据（程序员Orion）
- [[knowledge/Security/小程序-2026-开发与挖洞增强|微信小程序开发与挖洞增强]] — 2026 千轮研究
- [[knowledge/Security/挖洞实战-校园便利盒-2026-08-22|校园便利盒挖洞实战]] — 首个授权挖洞实战报告
- [[knowledge/Security/校园便利盒攻防-2026-08-22|校园便利盒攻防分析]] — 完整攻防复盘
- [[knowledge/Security/卡密系统攻防-AI辅助逆向-2026-08-22|卡密系统攻防 + AI 逆向]] — 卡密体系分析
- [[knowledge/Security/手机木马RAT攻防-2026-08-22|手机木马 RAT 攻防全景]] — 防御视角
- [[knowledge/Security/墨题安全自审-2026-08-22|墨题安全自审报告]] — 4 洞修复
- [[knowledge/Security/墨题防破解自查-2026-08-22|墨题防破解自查]] — 加固清单

---

[[HOME|🏠 返回首页]]

## 🧭 入口治理

- [[../MOC-Inbox|待接入/孤立笔记审阅入口]]
