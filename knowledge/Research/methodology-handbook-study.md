---
tags: [research, methodology, ai-collaboration, lessons-learned]
created: 2026-07-31
status: absorbed
source: https://github.com/redamancy231-create/methodology-handbook
license: CC BY 4.0
---

# AI 协作实战 50 条踩坑速查手册 — 研究笔记

> 来源：redamancy231-create/methodology-handbook（CC BY 4.0，3★ 个人项目）
> 2026-07-31 验证 + 吸收

## 项目概况

| 项 | 值 |
|----|-----|
| Stars | 3（个人项目，价值在方法论本身） |
| 内容 | 50 条踩坑实证，4 章：工程纪律(9) / AI协作方法论(32) / 文件陷阱(6) / 量化研究(3) |
| 格式 | Markdown + JSON 双件，CC BY 4.0 |
| 实证范围 | 作者 2026 年 5-7 月个人项目记录（单次观测，案例参考非统计结论） |

## 50 条对照评估（我们的覆盖 vs 缺口）

### ✅ 已有覆盖（无需吸收）
- 多模型独立审查收敛 → 规则 #17 评估器自检
- 配置修改前确认系统读取文件 → 规则 #2 MCP 铁律
- UTF-8 中文编码 → 规则 #14 Windows 编码铁律
- 分类器失败重试上限 → 规则 #5 重试机制
- Skill 设计协议（路由器模式）→ 规则 #20 60 字符预算
- Spec 覆盖 Vibe 执行 → 规则 #8 落实优先
- md/json 双件 → 我们的 .learnings 体系

### 🔴 新吸收（规则 #23，8 条）
1. 下断言前先核实（数字/日期/程度）
2. 配置修改两阶段验证（飞行前+重启）
3. 措辞/版本号修正后 grep 全项目零残留
4. 禁止自扫自夸零残留（异后端独立确认）
5. 多模型审查角度选择（防共享上游偏差）
6. 自评估偏乐观偏差（~11%）
7. docx 矢量图只能走 EMF（工具陷阱）
8. replace_all 短模式全局替换风险（工具陷阱）

### 🟡 存档关注（暂不吸收）
- 量化研究 3 条（特征泄漏/LambdaRank/Regime 滞后）— 我们不做量化交易
- headroom_compress 触发绑定机械闸门 — Claude Code 特有工具
- 任务分派：实现走 Codex/分析走 Workflow — 我们已有 delegate_task

## 研究验证结果

| 验证点 | 结果 |
|--------|------|
| python-docx EMF 限制 | ✅ 属实（官方 issue #24 确认不支持；Word 矢量图只能 EMF/WMF；SVG→Inkscape→EMF 链路） |
| LLM 审查结构性盲区 | ✅ 充分（Wiz GhostApproval：6 大 AI 编码助手确认 UI 不显示真实目标；ANSI 注入研究：终端显示≠实际命令） |
| 多模型审查收敛 | ✅ 合理（不同后端独立审查 = 自然互补盲点） |

## 落地行动

1. ✅ 规则 #23「AI 协作踩坑速查」已加入 hermes-workflow-preferences v1.17.0（8 条吸收）
2. 📄 本笔记存档（含验证证据）

## 与知识吸收流程的关系

- Learn：通读 50 条（601 行手册全文）
- Research：web_search ×2 验证 EMF 限制 + LLM 审查盲区
- Apply：8 条并入规则 #23，量化研究 3 条存档待需要时启用
- 符合 CC BY 4.0：吸收的是原则（非逐字复制），引用已标注来源
