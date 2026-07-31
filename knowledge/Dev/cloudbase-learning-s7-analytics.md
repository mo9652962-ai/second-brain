---
tags: [cloudbase, miniprogram, wechat, learning, analytics]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 7 站：analyticsDashboard 数据看板

> 对照校园便利盒 analyticsDashboard.js + 微信官方聚合文档
> 学习日期: 2026-07-31

## 核心概念：聚合流水线（Aggregate Pipeline）

聚合 = 数据批处理管道，每个阶段接收输入记录 → 转换 → 输出给下一阶段。

```
集合全集 → match（过滤） → group（分组统计） → sort（排序） → end（结果）
```

## 常用聚合操作

```javascript
const db = cloud.database()
const $ = db.command.aggregate

// 按分类分组求平均销量
await db.collection('books').aggregate()
  .group({
    _id: '$category',       // 分组字段
    avgSales: $.avg('$sales')  // 累计器
  })
  .end()

// 多字段分组 + 求和
await db.collection('posts').aggregate()
  .group({
    _id: { campus: '$campusId', day: '$day' },
    total: $.sum(1)          // 计数
  })
  .end()
```

**累计器（accumulator）**：`addToSet` / `avg` / `first` / `last` / `max` / `min` / `push` / `stdDevPop` / `stdDevSamp` / `sum`

## 聚合阶段

| 阶段 | 作用 | 说明 |
|------|------|------|
| `match` | 过滤 | 语法同普通查询（where），可用索引 |
| `group` | 分组统计 | `_id` 必填，其他字段是累计器 |
| `sort` | 排序 | 按统计值排 |
| `project` | 投影 | 只取某些字段 |
| `limit`/`skip` | 分页 | 缩小数据量 |
| `geoNear` | 地理位置 | 必须是第一个阶段 |

## 数据看板典型指标

| 指标 | 聚合实现 |
|------|---------|
| 总用户数 | `users.count()` |
| 每日活跃（DAU） | group by date + sum(1) |
| 帖子总量 | `posts.count()` |
| 分类分布 | group by category + sum(1) |
| 平均互动 | group + avg(comments) |
| 帖子 Top 榜 | sort by likes desc + limit(10) |

## 性能原则（微信官方）

1. **尽早缩小数据集**：`match`/`limit`/`skip` 放前面（match 和 sort 在开头可利用索引）
2. 聚合是输入整个集合的 → 数据量大时必须有过滤
3. `geoNear` 必须在流水线第一个阶段

## 校园便利盒 analyticsDashboard 职责（推断）

- 管理后台数据看板：帖子数/用户数/活跃度/分类分布
- 聚合统计接口供 H5 admin.html 展示
- 与 adminPanel 共用（内联执行）

## 踩坑清单

| 坑 | 现象 | 修复 |
|----|------|------|
| 聚合无索引 | 大数据量慢 | match/sort 用索引字段 |
| group 全集合 | 内存超限 | 先 match 缩小范围 |
| 累计器拼错 | 返回 null | 检查 $.avg('$field') 语法 |

## 动手练习

- [ ] 实现「每日活跃用户」统计接口
- [ ] 分类分布饼图数据（group by category）
- [ ] 帖子 Top 榜（sort + limit）

---

*第 7 站完成 · 下一步: 第 8 站 activityZoneCore 活动专区（最后一站）*
