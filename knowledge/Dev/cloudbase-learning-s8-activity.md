---
tags: [cloudbase, miniprogram, wechat, learning, activity]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 8 站：activityZoneCore 活动专区（完结）

> 对照校园便利盒 activityZoneCore.js + 京东科技活动平台 + CRMEB 活动设计
> 学习日期: 2026-07-31

## 核心概念：活动生命周期（状态流转）

京东科技活动平台的 6 状态生命周期，可简化为校园场景 4 态：

```
草稿态 → 准备中 → 已上线/进行中 → 已结束/已下线
```

校园便利盒的实现（活动专区期次）：

```javascript
// 进行中帖子带 inActivityZone + activityRoundId；
// 结束本期后转为普通帖（默认「校园生活」），并清空横幅配置
```

**设计要点**：
1. **期次管理（activityRoundId）**：每期活动一个 ID，帖子挂期次
2. **结束转普通帖**：活动结束 → 帖子状态回退（不删除数据，只改状态）
3. **横幅配置清空**：活动结束 → 清理相关运营配置

## 活动时间管理（CRMEB 精华）

**问题**：活动开始/结束时间精确控制
**方案**：
1. 定时器任务定期检查活动状态
2. **关键操作时再次验证活动时间**（用户参与时检查是否在活动期）
3. Redis 过期时间自动更新状态（云开发可用定时触发器替代）

## 活动专区数据结构

```javascript
// 活动配置
activityZone: {
  _id, roundId, title, status: 'active'|'ended',
  startAt, endAt, bannerConfig, targetCampuses
}

// 参与活动的帖子
posts: {
  _id, content, campusId,
  inActivityZone: true,
  activityRoundId: 'round_2026_07',
  status: 'normal'  // 活动结束后转回
}
```

## 活动运营工作台（京东科技模式，简化为校园版）

| 阶段 | 功能 |
|------|------|
| 活动前 | 模板选择、报备、配置（草稿态→准备中→已上线） |
| 活动中 | 资源位上/下架、参与数据监控 |
| 活动后 | 数据分析、复盘（已结束→已下线） |

## 关键认知

1. **活动模块本质**：用户需求与商业目标的连接器（拉新/留存/转化）
2. **状态机要完整**：每个状态都要有进入/退出条件，不能有死状态
3. **数据不删除只流转**：活动结束转普通帖（保留数据，降级展示）
4. **防并发超卖**（秒杀/拼团类）：数据库事务 + 乐观锁 + 库存预扣（校园场景一般用不到，但要知道）

## 校园便利盒 activityZoneCore 职责

- 活动专区期次管理（开期/关期）
- 进行中帖子标记（inActivityZone + activityRoundId）
- 活动结束转普通帖 + 清空横幅配置
- 与 adminPanel 共用（内联执行）

## 踩坑清单

| 坑 | 现象 | 修复 |
|----|------|------|
| 活动结束后帖子还在专区 | 数据不清理 | 定时任务/关期时批量转状态 |
| 活动时间判断失误 | 未开始/已结束仍可参与 | 关键操作时二次验证时间 |
| 期次 ID 混乱 | 活动串期 | 每期唯一 roundId，帖子显式挂载 |

## 动手练习

- [ ] 实现「每周主题」轮换功能（开期/关期）
- [ ] 活动帖子转普通帖（状态流转）
- [ ] 管理端配置活动（banner + 时间 + 期次）

---

# ✅ 8 站学习完成！总结

| 站 | 主题 | 核心学到 |
|:--:|------|---------|
| 1 | login | 免鉴权身份注入、OPENID、用户体系 |
| 2 | contentCheck | 云调用、msgSecCheck、不能全依赖 AI |
| 3 | dbOperations | action 分发、幂等写入、事务、原子操作 |
| 4 | notifySender | 订阅消息、内部鉴权、优雅降级 |
| 5 | marketCategories | 归一化、向后兼容、分类设计模式 |
| 6 | adminPanel | 双鉴权、云函数内联复用、管理后台架构 |
| 7 | analyticsDashboard | 聚合流水线、运营指标、性能原则 |
| 8 | activityZoneCore | 活动生命周期、期次管理、状态流转 |

**8 篇笔记已存入 `knowledge/Dev/cloudbase-learning-s*.md`**

## 下一步建议

- [ ] 动手实践：创建自己的 CloudBase 环境，从 login 开始部署
- [ ] 对照 `scripts/deploy-cloud-functions.ps1` 部署脚本
- [ ] 有客户需求时用 `references/miniprogram-order-scaffold.md` 报价接单
