---
aliases:
  - 2026-09-08-card-heihe-top5-empirical
tags:
  - knowledge-card
  - github
  - 实证研究
  - cad
  - ai-agent
created: 2026-09-08
source: "[[knowledge/Research/黑盒热榜5项目实证研究-2026-09-08]]"
status: fresh
---

# 🃏 知识卡片 · 黑盒热榜别全信：5 个 GitHub 项目实测后，3 个值得抄

> **来源**：小黑盒 GitHub 热榜日报 → 全量实证研究 · 2026-09-08 · ✅ GitHub API 验 star + clone 读代码 + 子代理深研 + 质疑式核验
> **一句话**：黑盒声称的 star 数与实测差 0.4k~2.4k，5 个项目里 3 个值得借鉴（marketing-skills / DeerFlow / pascal-editor），LunaTV 只借技术不碰本体，camofox 不引入。

---

## 核心洞察 / 影响

| 维度 | 内容 |
|------|------|
| 实证方法 | 每个项目用 GitHub API 验真实 star（黑盒 47.8k → 实测 48.2k，不是同一数字）+ clone 读代码，License 看 LICENSE 文件不信 README 徽章 |
| 最值得抄 | **marketing-skills（48.2k★ MIT）**：55 个营销 skill + 51 个零依赖 CLI 工具，每个 skill 配 **evals.json**（prompt+20+断言验证输出）→ 可测试技能库；另有 **product-marketing 上下文前置** 原语（所有 skill 先读产品定位）|
| CAD 方向 | **pascal/editor（22.4k★ MIT）**：R3F+WebGPU 纯浏览器参数化 3D 建筑编辑，原生内置 **31 个 MCP 语义工具** + CLI（create_room/add_door/check-collisions/validate_scene/export-glb），Core 不 import Three.js（headless 零 GPU）|
| 多步 Agent | **DeerFlow 2.0（81.9k★ MIT）**：字节 LangGraph 重写的 long-horizon SuperAgent 运行时，「真实沙盒执行 + checkpoint 可恢复」vs 日常助手；本机无 Docker 只能用 Local Execution（须 Git Bash、牺牲沙盒）|
| 避坑 | **LunaTV**：README 徽章标 MIT、LICENSE 实为 **CC BY-NC-SA 4.0**（影视聚合+禁商用，别碰本体）；**camofox**：不支持 CDP → 不能做 Hermes CDP 无缝替换 |

## 对 sora 的影响

1. 💡 **AI 营销技能库升级**：不必照搬 55 个 skill，但补两个差异化原语——①evals.json 质量断言 ②product-marketing 上下文前置。这是它 48k★ 的核心原因，sora 的博主/闲鱼技能库直接对口
2. 💡 **CAD 自动化 MCP**：pascal/editor 的 31 个 MCP 语义工具 + headless Core 设计，是 sora 的 CAD/PCB 自动化 MCP 方向「直接参考实现」——implicit-cad（隐式有机）与 FreeCAD（B-rep 制造级）两极之间，它是「空间规划 + AI 建造」的中间路线
3. ⚠️ **多步 Agent 任务**：DeerFlow 的 checkpoint 恢复 + sandbox 分级值得借鉴设计；本机无 Docker → 只轻量评估，部署等有 Linux 环境再说
4. ⚠️ **License 陷阱**：选型先看 LICENSE 文件、不信 README 徽章；黑盒 star 数要回官方源复核（评项目实证原则再次验证）
5. ⚠️ **camofox 不引入**：反检测在 Gecko C++ 编译期、无 CDP → 不能替换 Hermes 的 CDP 链路，仅借鉴其 accessibility snapshot 省 ~90% token 的架构思路

## 行动项

- [x] 给 k 的 AI 营销技能库补「质量断言」原语：关键技能配 evals.json（prompt + 断言），沉淀进 skill 结构 → ✅ 2026-09-08 已落地：ai-cmo SKILL.md「核心原语 2：evals 质量断言」（evals.json 结构 + 通用营销方案质量断言 ≥80%）+「核心原语 1：product-marketing 上下文前置」，09-09 复核确认
- [ ] 深读 pascal/editor 的 31 个 MCP 语义工具，对照 implicit-cad/FreeCAD 取「浏览器原生 + MCP 语义化」设计 CAD MCP（draft 设计稿）→ ⏳ 需专项研究会话（09-12 复核仍 open）
- [x] 选型规则固化：新项目评估 = GitHub API 验 star + 看 LICENSE 文件 + clone 读代码，数字 claim 标官方源 → ✅ 规则已固化为 k 常驻基线（memory「评项目须实证(真实star/README/定价)」+ 09-08 研究文档方法论章节），09-09 复核确认无需再落地

## 为什么重要

- **时效性**：09-08 当天实证研究，结论新鲜
- **业务相关性**：CAD/PCB 自动化 MCP（核心兴趣）+ AI 营销技能库（博主/闲鱼）+ 多步 Agent（墨题/编码委派）三线全命中
- **可行动**：5 个借鉴动作全部可执行、带明确落点
- **强化自身**：研究方法正是 sora 偏好的「评项目须实证」——黑盒数字不轻信，官方源复核，同一次研究同时沉淀「结论 + 方法论」

---

*卡片来源：当天知识库精选 · [[knowledge/Research/黑盒热榜5项目实证研究-2026-09-08|黑盒热榜 5 项目实证 09-08]]（🥇 深度实证研究，5 项目验 star+读码，CAD MCP/AI 技能库双落点，胜同天补全性质 arXiv 速览）*

**亚军候选**：arXiv 09-08 速览（2609.04681「写码增益在交付阶段衰减」→ 编码委派交付预估基线；2609.04373「越强越趋同」→ 模型容灾链多样性审计）。
