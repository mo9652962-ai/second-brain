# 817 网安技能库对照（2026-08-20）

> 来源：mukul975/Anthropic-Cybersecurity-Skills（27,747★，Apache 2.0，agentskills.io 标准）
> 用途：对照 src-bug-hunting 技能补强——已整合 IDOR 深度方法论 + API 安全测试框架

## 技能库概况（实证）

- **817 个结构化网安技能 / 29 安全领域 / 6 框架映射**（MITRE ATT&CK 805 + NIST CSF 804 + ATLAS + D3FEND + AI RMF + F3）
- 每技能结构：SKILL.md（标准 frontmatter + 场景/前置/工作流/概念/工具/输出格式）+ references/ + scripts/agent.py + LICENSE
- 兼容：Claude Code / Copilot / Codex / Cursor / Gemini CLI 等 26+ 平台
- 质量：ATT&CK v19.1 官方 mitreattack-python 验证、零撤销 ID、无硬编码凭据

## 与 sora src-bug-hunting 的对照结论

| 维度 | sora 技能（原有）| 817 库 | 整合动作 |
|:---|:---|:---|:---|
| 水平越权 | ✅ 案例级（合同 _id 遍历）| ✅ 6 步工作流 | **补强**（Authorize 自动化/垂直/非明显位置/枚举）|
| API 测试 | ⚠️ Swagger 单点 | ✅ OWASP API Top 10 框架 | **补强**（JWT/OAuth/BOLA/BFLA）|
| SQLi | ✅ DVWA 实战 | ✅ 跨引擎技巧 | 已够，不重复 |
| 报告格式 | ✅ 4 件套规范 | ✅ 结构化 finding 模板 | 互相印证 |
| 合规红线 | ✅ 超详细（30+ 平台）| ⚠️ 通用授权声明 | sora 更细，保留 |
| 框架映射 | ❌ 无 | ✅ nist_csf/mitre_attack frontmatter | 可选加分（SRC 报告可引 ATT&CK ID）|

## 已落地

- `src-bug-hunting` 技能新增 2 章：
  1. **IDOR 深度方法论**（6 步工作流：映射→Authorize 自动化→水平→垂直→非明显位置→枚举升级 + 报告输出格式）
  2. **API 安全测试框架**（4 步：发现→认证→授权→逻辑 + SRC 接口挖洞清单速记）

## 可继续用（未整合）

- 817 库克隆在 Temp 已删——需要时重新浅克隆（4510 文件 ~100MB）
- 高价值候选：exploiting-jwt-algorithm-confusion / exploiting-nosql-injection / detecting-shadow-api-endpoints / escaping-containers-to-host
- 中文版：killvxk/cybersecurity-skills-zh（3★，翻译不全，不推荐优先）

## 教训

- 817 技能库价值 = 结构化方法论，但 sora 的 Hermes 技能体系（中文+实测+合规红线）比它更适合 sora 实际使用——**只补缺口，不整套迁移**

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]
