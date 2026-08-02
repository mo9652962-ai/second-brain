---
tags: [周报, GitHub Trending, W31]
date: 2026-08-02
---

# 🗞️ GitHub 周报 — W31 v3（2026-08-02 · weekly 口径）

> 来源：https://github.com/trending?since=weekly 快照（07-27 ~ 08-02）
> 流程：github-trending-digest 技能 Phase 1-6 · 与今日 13:09 自动脚本（新建仓库口径）互补

## 项目详情

| # | 项目 | ★ | 本周增长 | 核心价值 | 入库笔记 |
|:-:|------|:--:|:-------:|---------|---------|
| 1 | **alibaba/open-code-review** | 17.4K | +4,746 | 确定性工程 × Agent 混合代码评审（F1 更高、token 1/9、行级意见） | [[github-trending-2026-08-02-weekly-5projects]] |
| 2 | **virgiliojr94/book-to-skill** | 14.5K | +4,603 | 技术书 PDF → 按需加载的 Agent Skill（~$1/本，24-51× token 节省） | 同上 |
| 3 | **different-ai/openwork** | 20.0K | +2,213 | opencode 驱动的开源 Claude Cowork：MCP 共享 skills/连接服务 | 同上 |
| 4 | **earthtojake/text-to-cad** | 12.3K | +1,901 | CAD/CAE/CAM agent skills 库 + 10 项 benchmark（已装 text2cad-cad 同源） | 同上 + CAD-Design.md 更新 |
| 5 | **ayghri/i-have-adhd** | 15.0K | +5,133 | 10 条规则约束 agent 输出风格：行动开头、列表≤5、无客套 | 同上 |
| ↳ | diegosouzapw/OmniRoute | 36.7K | +7,701 | 本周热度第一，但已两次评估（watch→不装，ToS 灰色地带） | 仅跟踪不建笔记 |

## 可借鉴点归纳

**技术层面**
- open-code-review 的混合架构：「必须不出错」的步骤交给确定性工程（文件选择/捆绑/规则匹配），LLM 只管动态决策——专用工具集比通用 agent 少 9 倍 token
- book-to-skill 的 skill 结构：SKILL.md 只放索引+心智模型，章节按需加载；5 条设计原则（密度优先/实践者语气/前置加载/按需章节/绝不原文）
- text-to-cad 用 10 个从易到难的 benchmark 定义「什么算 CAD 生成成功」

**方法论层面**
- 本周趋势：Agent 工具链进入「资产复用」阶段（openwork 跨 agent 共享、book-to-skill 书→skill、text-to-cad skill 库分发）
- 输出风格被产品化：i-have-adhd 证明「agent 怎么说」可以是爆款 skill——与 sora 结论置顶偏好一致，是社区共识
- CAD/硬件自动化持续升温：text-to-cad 两周 7.6K→12.3K，验证蓝海工程自动化定位

**可实操行动**
- P1: book-to-skill → trial 安装，拿一本自有技术书转 skill，评估进 Second Brain 工作流
- P2: open-code-review → backlog 安装，与现有 ai-code-review 技能对比试用
- P3: i-have-adhd 10 条规则 → 已内化（sora 偏好已含结论置顶/列表精简），无需安装

## 文件操作清单
- ✅ 新建 `knowledge/Research/github-trending-2026-08-02-weekly-5projects.md`（5 项目深度分析）
- ✅ 更新 `knowledge/Hardware/CAD-Design.md`（text-to-cad 7.6K→12.3K）
- ✅ 更新 `knowledge/Research/MOC-Research.md`（+1 索引）
- ✅ 更新 `knowledge/knowledge-map.md`（关联表 +1）
- 📄 本报告 `memory/2026/08/github-trending-w31-v3.md`

---
*2026-08-02 · github-trending-digest 技能流程 Phase 6 · weekly 口径（与 13:09 新建仓库口径 w31 日报互补）*
