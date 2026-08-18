# 防御能力研究（2026-08-18 八轮千轮研究完整版）

> 攻击端→防御端视角：知道防御方怎么想，才能知道怎么突破 & 怎么保护自己

## 一、WAF 绕过技术（理解防御盲区）
| 层 | 技术 | 说明 |
|:---|:---|:---|
| 协议层 | HTTP/2 帧分片、chunked 扩展参数、双重 Content-Length | 70% WAF 未完整解析 HTTP/2 重组 |
| 语法层 | `/*!11440UNION*/` 版本注释、SQL 碎片化、参数污染(HPP) | 各厂商特有缺陷 |
| 语义层 | 上下文逃逸、时间盲注混淆（BENCHMARK vs SLEEP）| 现代 WAF 检测核心 |
| 编码 | 多层嵌套（URL+HTML+Base64）、UTF-7/UCS-2、双重 URL 编码 | 编码深度差异 |

WAF 指纹：Cloudflare=403+cf-error-code / Akamai=ak_bm cookie / Imperva=Incapsula incident
工具：waf-bypass-tester（557 变体/13 编码/三厂商对比）、wafw00f

## 二、纵深防御体系（企业标准）
- 国家标准：T/ZTCIA 010-2026 可信纵深防御架构（蚂蚁/华为/公安部）
- 华为云「一个中心+七层防线」：物理→身份→网络→应用→主机→数据→运维
- 关键实践：边界高危端口封禁(445/135-139/3389) → 数据中心防火墙精细化 ACL → 主机级 iptables 微隔离
- 零信任：东西向流量控制、业务系统分组、最小权限、堡垒机审计

## 三、蓝队检测响应（攻防演练全流程）
- 四阶段：备战(收敛资产/加固) → 对抗(实时监测/处置) → 溯源(还原攻击链) → 复盘(整改闭环)
- 告警分级：P0(5min处置) P1(15min隔离) P2(1h封禁) P3(4h汇总)
- 关键指标：MTTD<5min、MTTC<30min、检出率>90%、误报率<10%
- 溯源画像：TTPs 三维（战术/技术/程序）+ C2 分析 + 蜜罐诱捕(HFish/Cowrie/T-Pot)
- 开源栈：Wazuh(检测) + DFIR-IRIS(案件管理) + MISP/OpenCTI(情报) + VirusTotal/微步(查询)

## 四、端点加固（Windows 10 大实践 + 个人清单）
### 企业级（Intune/Defender for Endpoint）
```
① Intune 安全基线  ② ASR 规则(攻击面缩减)  ③ BitLocker 全盘加密
④ MFA + 条件访问   ⑤ LAPS(本地管理员密码)  ⑥ 自动化补丁(3-7天质量/30-60天功能)
⑦ 防火墙高级规则(封 445/3389/5985)  ⑧ EDR 部署
⑨ 禁用 SMBv1/LLMNR/NetBIOS/Print Spooler  ⑩ WDAC/AppLocker 应用控制
```
### 个人电脑（立即执行）
```
Bitwarden 密码管理器 + 唯一密码 / 邮箱银行云开 2FA(passkey优先)
BitLocker 全盘加密 / Defender: 实时+云+篡改保护+受控文件夹(防勒索)
防火墙三档全开 / DoH (1.1.1.1) / VPN 陌生网络
工具: Windows Client Security Baseline Toolkit (PowerShell 检查+修复)
```

## 五、数据备份防勒索（最关键认知）
```
3-2-1 原则: 3 份数据 + 2 种介质 + 1 份异地
⚠️ 90% 勒索攻击会先打备份!
备份 4 大失效漏洞: ①完整性不足 ②3-2-1只做一半 ③未隔离 ④从未还原演练
救命机制: 不可变备份(WORM, 连管理员都删不掉) + 离线副本(拔掉硬盘)
工具: 个人→外接硬盘+云(版本保留) / 企业→群晖 ABB+Snapshot+WORM
SaaS 同步 ≠ 备份 (误删/加密会同步扩散)
```

## 六、身份安全 + API 密钥管理
### 零信任三原则
明确验证 / 最小权限 / 假设违规
### API 密钥 7 大最佳实践
```
① 密钥=机密(不硬编码)  ② 最小权限(每密钥只干一件事)  ③ 90天轮换
④ HTTPS传输+日志脱敏  ⑤ 监控审计(异常IP/高请求量)  ⑥ IP白名单
⑦ 避免客户端使用(服务端调用)
```
腾讯云 AK 实践: 避免主账号 AK / 子账号+最小权限 / 定期轮换 / 云安全中心监测
IAM 十大威胁: 凭证填充/钓鱼/BOLA/权限提升/会话劫持/影子IT/内部威胁/弱默认凭证/令牌泄漏/DoS

## 七、AI 安全（OWASP GenAI LLM Top 10 2026）
```
LLM01 Prompt Injection 居首 — LLM 无法架构性区分指令和数据
致命三要素 (lethal trifecta): [私有数据+不可信内容+对外通信] 同时具备=高危
防御铁律:
  ① 最小权限(Agent 工具按需最小)
  ② 人工审批(破坏性/外部可见操作)
  ③ 双 LLM 隔离(持工具的不读不可信内容)
  ④ 记忆写入当特权操作(防投毒跨会话)
  ⑤ MCP/工具 pin 版本 + 审计工具描述
Guardrail: Llama Guard / ShieldGemma / Prompt Guard / NeMo Guardrails
```

## 八、供应链安全（npm/PyPI）
```
2026年3月: axios 维护者账号被盗发布含 RAT 版本 / TeamPCP 跨5生态级联
五大模式: 安装钩子窃密 / 钱包窃取 / Webhook外传 / 反弹shell / 依赖混淆
⚠️ 恶意包会污染 .cursorrules/CLAUDE.md → 污染 AI 助手!

npm 加固 (~/.npmrc):
  ignore-scripts=true        # 禁 postinstall
  min-release-age=3          # 不装 3 天内新包
  allow-git=none             # 禁 git 来源
  allow-remote=none          # 禁 direct URL
PyPI: pip install --require-hashes --only-binary :all:
工具: npm audit / pip-audit / Socket Firewall / syft(SBOM) / Sigstore / SLSA
pnpm v10+ 默认阻止依赖生命周期脚本 (推荐)
```

## 九、攻击链卡位（防守视角）
```
钓鱼(邮件网关) → 终端恶意代码(EDR) → 横向移动(内网流量监控) → 域控异常(审计日志) → 数据外泄(DLP/加密)
```

## 十、AI 在防御中
- DeepHunting：AI 威胁狩猎 30 分钟全链溯源（人工需 6-8 小时）
- 行为检测：EDR 12 种监督学习模型（SentinelOne）
- 规则+语义+行为三层 WAF：libinjection 语义检测、AST 解析、基线建模

## 十一、对自己挖洞的启示
1. 知道 WAF 怎么检测 → 绕过更高效（但仅限授权测试）
2. 知道蓝队怎么溯源 → 测试时注意行为规范（不暴力扫描、用代理池）
3. 防御知识 = 报告价值（修复建议写得专业，审核通过率更高）
4. 知道自己怎么被黑 → 保护自己的资产（密钥管理/备份/供应链）

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
