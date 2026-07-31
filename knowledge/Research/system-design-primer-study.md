---
tags: [research, github, system-design, article-study]
created: 2026-07-31
status: absorbed
---

# 《AI 时代程序员最硬核的能力》— system-design-primer 研究

> 来源：小黑盒文章（前沿情报站 07-19）· 2026-07-31 验证 + 吸收

## 项目验证

- **donnemartin/system-design-primer** — GitHub 实测 **359,759★**（文章说 358K ✅ 准确）
- 2017 年创建，130+ contributors，Python 为主（98%）
- GitHub 全站前 20，有中文版（README-zh-Hans.md）
- 358K★ 不是刷的：持续增长（+437/天，+4.5k/周）

## 文章核心：四步面试法（可迁移为架构设计方法论）

| 步骤 | 内容 | 关键 |
|------|------|------|
| ① 对齐假设 | 容量/读写比例/延迟/一致性 | 需求没聊清楚就画图 = 全错 |
| ② 高层架构 | 请求→经过什么→存到哪 | 只画大组件框 |
| ③ 核心组件 | 数据库/缓存/API/队列选型 | 每个选择说出 why + trade-off |
| ④ 十万倍流量 | 一万涨到一千万哪里先崩 | 扩容方案说清才过关 |

## 已落地

1. ✅ **创建技能 `system-design-primer-essence`**（software-development 类）
   - 四步法 + trade-off 表 + 反模式表 + 使用时机
   - 与 engineering-workflow（实现流程）互补：一个管"怎么建"，一个管"建什么"

2. 📄 本笔记存档

## 与现有体系的关系

- **engineering-workflow** = 实现流程（Grill→建模→TDD→Review）
- **system-design-primer-essence**（新）= 架构设计（假设→架构→组件→扩展）
- 两者组合 = 完整软件工程链路（设计→实现）

## 对博主身份的价值

- 文章"缺的不是知识，是把知识串起来的能力"是共鸣点
- 可做一期内容：《系统设计四步法，AI 时代依然硬核》

## 结论

- 文章数据准确（358K star 实测 359.8K）
- 核心方法论已吸收为技能，非收藏即止
- 不克隆整个仓库（README 足够提炼方法论），需要真题时再按需拉取
