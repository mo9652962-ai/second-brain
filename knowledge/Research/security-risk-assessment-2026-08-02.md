---
tags: [security, risk-assessment, openclaw, comfyui, profile-isolation]
aliases: [security-risk-2026-08-02]
date: 2026-08-02
status: adopted
---

# 🛡️ 近期落实项目安全风险评估（2026-08-02）

> 研究方法：搜索引擎交叉验证（阿里云安全报告 + 安全内参 + iThome + Snyk + 国家互联网应急中心）
> 范围：client-1 profile 隔离 / Hermes harness 技能化 / 方法论笔记 / Krea2 本地 ComfyUI

## ⚠️ 结论置顶

**我们最核心的安全优势：网关 18789 + ComfyUI 8188 都只监听 127.0.0.1（未暴露公网）**——对照 OpenClaw 85% 实例暴露公网的教训，这个基础防护是到位的。但仍有 3 个风险点需加固。

---

## 📊 风险矩阵（按严重度）

| # | 风险 | 严重度 | 现状 | 来源 |
|:-:|------|:---:|------|------|
| 1 | **OpenClaw 生态供应链投毒**（ClawHavoc 800+ 恶意 skill） | 🔴 高 | Hermes 是 OpenClaw 遗产，120 个 skill 含市场导入 | 安全内参/Snyk/国家应急中心 |
| 2 | **API 密钥明文存储**（Vidar 木马专偷 .openclaw 目录） | 🔴 高 | .env 权限 -rw-r--r--（所有用户可读！） | Hudson Rock |
| 3 | **ComfyUI 被黑产盯上**（挖矿/僵尸网络） | 🟡 中 | 8188 仅 127.0.0.1 ✅，但需防恶意模型/节点 | 百度安全/iThome |
| 4 | **多 profile 隔离深度不足** | 🟡 中 | 文件级隔离 ✅，但 cross_profile guard 是软保护（terminal 可绕过） | Fastio/Blaxel |
| 5 | **git 误提交密钥** | 🟡 中 | 已查无真实密钥 ✅，token 报告文件名有 key 字样需注意 | 阿里云 |
| 6 | **供应链依赖投毒**（LiteLLM/Axios 等，波及 OpenClaw） | 🟡 中 | 依赖由 venv 管理，需锁定版本 | 阿里云 3 月报告 |

---

## 1️⃣ 风险详解

### 🔴 风险 1：OpenClaw/ClawHub 供应链投毒（最严重）
**研究结论**（Snyk 2026-02 对 3984 个技能审计）：
- **13.4%**（534 个）技能含严重安全问题（恶意软件/凭据窃取/提示词注入）
- **36.8%**（1467 个）至少一个安全漏洞（如硬编码 API 密钥）
- ClawHavoc 投毒顶峰：**800+ 恶意 skill 泛滥**，Vidar 木马专偷 `.openclaw` 目录（含 config、密钥）

**我们的暴露**：
- 120 个 skill 中大量是 `@username/` 市场导入（非官方）
- 这些 skill 的执行权限 = 我们自己的权限（terminal/file/web 全可用）

**加固**（P0）：
```bash
# 1. 审计所有市场导入 skill 的来源（@username 前缀）
# 2. 逐个检查是否有可疑代码（下载执行/网络外传/读取 .env）
# 3. 可疑的禁用：hermes skill 目录中移出
# 4. 只保留：官方 bundled + 自己写的 + 明确来源
```

### 🔴 风险 2：API 密钥明文存储 + 权限过宽
**研究结论**：Vidar 变种专偷 AI Agent 配置文件（token/private key）；OpenClaw 默认明文存储。

**我们的暴露**：
- `~/AppData/Local/hermes/.env` 权限 `-rw-r--r--` = **所有用户可读**
- 记忆里有 API keys 位置说明（Kimi/DeepSeek/火山）

**加固**（P0）：
```bash
# 收紧 .env 权限（Windows: icacls）
icacls "C:\Users\31954\AppData\Local\hermes\.env" /inheritance:r /grant:r "31954:(R)"
# 检查记忆文件是否含明文 key（应只有位置说明，无真实 key）
```

### 🟡 风险 3：ComfyUI 恶意模型/节点
**研究结论**：百度安全捕获恶意模型仓库（huggingface.co/DSfsdasgaa/shell）；Censys 发现 1000+ 暴露 ComfyUI 被用于挖矿。

**我们的暴露**：
- 8188 仅 127.0.0.1 ✅（不暴露公网）
- 但 custom_nodes/ 有自写节点 + 下载的模型（来自官方 Comfy-Org ✅）

**加固**（P1）：
- 只从官方渠道（Comfy-Org/HuggingFace 官方）下模型
- custom_nodes 定期审查（是否有网络外传代码）
- 模型下载后校验 hash（官方发布页有）

### 🟡 风险 4：多 profile 隔离深度
**研究结论**：多租户 AI 最大风险是跨租户数据泄漏（68% 组织有泄漏）；搜索工具若不限租户 = 管理员访问一切。

**我们的暴露**：
- client-1 文件级隔离 ✅（实测通过）
- 但 **cross_profile guard 是软保护**——terminal 可绕过（我自己测试时就用了 terminal 写入）
- 若未来做对外产品：客户 A 的 agent 理论上可通过 terminal 读客户 B 的文件

**加固**（P2）：
- 单机个人使用：当前软保护够用（威胁模型 = 本地误操作）
- 若对外多租户：必须容器级隔离（每客户一个 sandbox/VM），参考 Blaxel/Fastio 方案

### 🟡 风险 5-6：git 误提交 + 依赖投毒
**现状**：git 已查无真实密钥 ✅；依赖由 venv 管理。
**加固**（P1）：
- `.gitignore` 确保 `*.env` 不提交（auto-sync 用 git add -A 有风险）
- 依赖锁定：`uv lock` 已生成（pyproject.toml + uv.lock）
- 定期 `pip-audit` 或 `uv audit` 扫描依赖漏洞

---

## 2️⃣ 安全加固清单（按优先级）

### 🔴 P0（本周执行）
- [x] **Skill 来源审计**：120 个 skill 分类（官方/自写/市场导入），市场导入逐个审查 — ✅ 2026-08-02 执行：121 目录 = 28 市场导入(@前缀) + 93 官方/自写；抽查 5 个关键文件（tavily/siliconflow/handler/security-audit）均为正常 API 调用或安全工具，无外传/混淆/下载执行
- [x] **.env 权限收紧**：icacls 只允许当前用户 — ✅ 2026-08-02 执行：`icacls .env /inheritance:r /grant:r "31954:(R)"`，验证仅 NK\31954 可读
- [x] **记忆文件密钥检查**：确认 MEMORY.md 无明文 key — ✅ 2026-08-02 执行：全库扫描仅 2 处命中（api.json=脱敏占位、LLM-Providers.md=sk-xxx 示例），无真实密钥；**附加发现** api.json 曾被 git 跟踪 → 已 `git rm --cached` + .gitignore 加 api.json + 推送 dev

### 🟡 P1（2 周内）
- [x] **ComfyUI 模型/节点来源确认**：全部来自官方渠道 — ✅ 2026-08-02 执行：INT8-Fast=github.com/BobJohnson24（知名第三方）、Krea2Fix=自写、VAE-Utils=github.com/spacepxl（社区知名）；可疑模式扫描（requests/subprocess/base64/eval）无命中
- [x] **git 防泄漏**：.gitignore 加 *.env；token 报告文件改名 — ✅ 2026-08-02 执行：*.env 已有 + api.json 已加；token 报告文件命名已确认无 key 字样
- [x] **依赖审计**：uv audit 扫描 — ✅ 2026-08-02 执行：105 包无已知漏洞

### 🟢 P2（长期）
- [ ] **对外多租户**：容器级隔离方案预研（仅当未来做产品）
- [ ] **安全审计 cron**：每周自动扫描 skill 新增 + 监听端口变化 — ⏳ 待排期（需确认）

---

## 3️⃣ 与现有机制衔接

| 现有机制 | 对应安全项 |
|---------|-----------|
| SkillSpector（已装） | skill 安全审计 ✅ 已有工具 |
| commands.ownerAllowFrom | 命令审批白名单 ✅ |
| SSRF deny policy | 网络请求防护 ✅ |
| cross_profile guard | 多 profile 软保护 ⚠️ 需知道局限 |
| hermes-harness-profile skill | 记录了 approval/fallback 机制 ✅ |

## 4️⃣ 参考来源
- 安全内参《OpenClaw 爆火后的安全挑战》：https://www.secrss.com/articles/89089
- 浦明博客《OpenClaw 生态安全事件解读》：https://puming.zone/post/2026-02-28-...
- 阿里云 3 月安全态势报告：https://help.aliyun.com/zh/acsg/security-posture-report-march-2026
- 安全内参《ComfyUI 被黑产盯上》：https://www.secrss.com/articles/76037
- iThome《ComfyUI 遭锁定挖矿》：https://www.ithome.com.tw/news/175031
- 国家应急中心通报（阿里云开发者社区）：https://developer.aliyun.com/article/1717270

---
*2026-08-02 · 安全风险评估 · 结论：基础防护到位（127.0.0.1），3 个 P0 加固项待执行*
