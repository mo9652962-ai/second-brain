---
tags: [ai, 多Agent, 教育, 编排, 时间轴, github-trending, W37]
aliases: [OpenMAIC, 多智能体课堂, MAIC]
date: 2026-09-06
source: https://github.com/THU-MAIC/OpenMAIC
domain: AI
status: active
---

# OpenMAIC — 清华多 Agent 交互课堂

**32.1k★（本周 +10,109）** · Open Multi-Agent Interactive Classroom——一键获得沉浸式多 agent 学习体验（清华 MAIC）。TypeScript 94.9%，MIT（部分子包 LGPL/pptxgenjs MIT），517 commits · 102 contributors · v1.0.0（08-27），极活跃（提交以分钟计）。

## 核心特征

- **DSL 驱动场景引擎**：课程内容用 DSL 描述场景/动作，引擎确定性回放——多 agent 对话、白板绘制、聚光灯/激光笔动画全部可编排。
- **choreography 编排规范（lib/choreography）**：单一事实源定义编排语义（timing、cursor、timeline、spotlight/laser 动画描述符），eslint 边界强制「纯 Node 可解释」——App 运行时与「课堂视频导出器」共享同一 spec，防漂移。
- **确定性时间轴解析**：`resolveActionTimeline` 把 index-domain 展开成 time-domain，含真实语音时长估计 / no-op 动作 0ms / 场景边界清理等精细语义。
- **动画描述符版本化 + zod 校验**：spotlight.v1 / laser.v1 声明式（property/from/to/duration/easing），可被非 React 消费者（导出器）字面还原。
- **课堂视频导出器**：从同一 choreography spec 导出 faithful 课堂视频。
- 支持多模型（最新 commit 注册 deepseek-v4-flash-vision-exp）。

## 技术架构（文字图）

```
课程 DSL（场景/动作/讨论/白板）
        ▼
┌──────────────────────────────────────┐
│ lib/choreography（单一事实源）          │
│  ├─ timing.ts   （时间常量+语音时长估计）│
│  ├─ cursor.ts   （播放游标解析）        │
│  ├─ timeline.ts（index→time 展开）     │
│  └─ descriptors/（spotlight.v1 等,     │
│     zod 校验、版本化、纯声明式）         │
└──────────────────────────────────────┘
        ├──► App 运行时（React 播放引擎）
        └──► 课堂视频导出器（纯 Node 解释同一 spec）
```

## 💎 可借鉴点（⭐ 核心价值）

1. **「编排规范单一事实源 + 纯解释器」= 多 agent 编排防漂移方案**。sora 的多 agent 协作（WorkBuddy/dsh/Codex/Gemini 联合研究）目前靠 prompt 约定；OpenMAIC 的做法是抽一个共享 spec + eslint 边界保证「谁都能解释」——可迁移到 multi-agent-research 流水线：定义任务契约（输入/输出/时序），各 agent 不再各自实现。
2. **确定性时间轴 → 抖音 AI 视频流水线可借鉴**。douyin-ai-practical-video 的脚本→素材→配音→剪辑可升级为「确定性时间轴 + 导出器」，同一脚本产出视频与分镜导出，消除人工剪辑不确定性。
3. **教育场景产品化**：多 agent 课堂是「AI 家教」的产品形态——墨题/家教的 AI 讲解可借鉴「多角色对话课堂 + 白板 + 确定性回放」的交互设计。
4. **深度工程 commit 文化**：每个 PR 带多轮交叉 review 记录（round 1-7，codex/claude 双审）——本身就是教科书级的「AI 辅助工程 workflow」，对 sora 的 code review 流程有参考价值。

## 安装/验证

```bash
# 官方一键体验（按 README）
# 本地跑需要 Node 18+；可先用在线 demo 看效果再决定部署
```

## 总结评价

| 维度 | 评分 | 说明 |
|:--|:--|:--|
| 技术含金量 | ★★★★★ | choreography spec + 确定性时间轴设计扎实 |
| 关联度 | ★★★★ | 教育 + 多 agent 双契合（墨题/联合研究） |
| 可迁移性 | ★★★★ | 编排 spec 与时间轴思路可搬；整套部署较重 |
| 热度 | ★★★★ | +10,109，本周第三 |
| 值得安装 | 🟡 选学 | 不整套装，抄编排架构；demo 值得一看 |

> 🗺️ 属于 [[MOC-Inbox]] · [[MOC-GitHub]] · [[Home|🏠 Home]]
> 📅 周报见 [[../../memory/2026/09/github-trending-w37|W37 周报]]
