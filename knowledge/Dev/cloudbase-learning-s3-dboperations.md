---
tags: [cloudbase, miniprogram, wechat, learning, crud, transaction]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 3 站：dbOperations 统一 CRUD（核心）

> 对照校园便利盒 dbOperations 云函数 + 微信官方文档
> 学习日期: 2026-07-31

## 核心概念：action 分发模式

一个云函数处理所有集合的 CRUD，用 `event.action` 分发：

```javascript
// cloudfunctions/dbOperations/index.js (架构示意)
const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })
const db = cloud.database()
const _ = db.command

exports.main = async (event) => {
  const { action, collection, data, where } = event
  switch (action) {
    case 'create': return db.collection(collection).add({ data })
    case 'read':   return db.collection(collection).where(where).get()
    case 'update': return db.collection(collection).where(where).update({ data })
    case 'remove': return db.collection(collection).where(where).remove()
    default: return { code: -1, msg: 'unknown action' }
  }
}
```

**优点**：一个云函数管全部集合 → 部署少、调用统一、权限集中。
**缺点**：action 膨胀后 switch 巨大 → 校园便利盒用模块拆分（marketCategories/activityZoneCore/webAdminHandlers 独立文件）。

## 原子操作 vs 事务（并发控制核心）

| 方案 | 适用 | 说明 |
|------|------|------|
| **更新指令** `_.inc/_.mul/_.addToSet` | 单记录内字段 | 原子，无需事务 |
| **确定性 _id 幂等写入** | 点赞/关注/收藏 | doc(id).set() 天然幂等，防并发重复 |
| **事务 runTransaction** | 跨记录/跨集合 | 快照隔离 + 事务锁，自动重试 |

### 幂等写入（校园便利盒精华）

```javascript
// 生成确定性 _id，配合 doc().get/set 实现幂等写入，防止并发重复
const crypto = require('crypto')
function makeDeterministicId(scope, ...parts) {
  const raw = [scope, ...parts.map(p => String(p == null ? '' : p))].join('|')
  return `${scope}_${crypto.createHash('md5').update(raw).digest('hex')}`
}
// 用法: 点赞 → doc(`like_${userId}_${postId}`).set({ liked: true })
// 重复点赞 = 更新同一文档，不会产生重复记录
```

### 事务示例（转账）

```javascript
await db.runTransaction(async transaction => {
  const aaa = await transaction.collection('account').doc('aaa').get()
  const bbb = await transaction.collection('account').doc('bbb').get()
  if (aaa.data && bbb.data) {
    await transaction.collection('account').doc('aaa').update({ data: { amount: _.inc(-10) } })
    await transaction.collection('account').doc('bbb').update({ data: { amount: _.inc(10) } })
  } else {
    await transaction.rollback()
  }
})
```

## 关键认知

1. **云函数默认管理员权限**（官方文档明确）——但注意校园便利盒实测：**执行身份继承调用方 OPENID**，读全表需显式管理员客户端（见第 1 站踩坑）
2. **快照隔离**：避免脏读/不可重复读/幻读；事务中读返回快照，写加事务锁
3. **事务不支持批量**：只支持单记录（collection.doc / collection.add）
4. **批量插入只消耗 1 次调用**：`addDocList`（云函数端）——一万条数据也只算 1 次
5. **批量更新没有直接 API**：用「事务 + remove + addDocList」技巧，3 次调用完成一万条更新

## 数据限制速查

| 操作 | 限制 |
|------|------|
| 小程序端 get | 默认最多 100 条/次 |
| 云函数 get | 单次返回总大小 ≤ 50M |
| add 写入 | 单次 ≤ 5M（云函数端） |
| update 写入 | 单次 ≤ 5M |
| callFunction data | ≤ 5MB |

## 复合查询（校园便利盒模式）

```javascript
// 多校区隔离
function campusWhereClause(campusId) {
  if (!campusId) return null
  if (campusId === DEFAULT_CAMPUS_ID) {
    return _.or([{ campusId: DEFAULT_CAMPUS_ID }, { campusId: _.exists(false) }])
    // 默认校区兼容老数据（无 campusId 字段）
  }
  return { campusId }
}

// 关键词模糊搜索（db.RegExp）
const regex = db.RegExp({ regexp: escapeRegExp(kw), options: 'i' })
parts.push({ nickName: regex }, { college: regex })
return _.or(parts)
```

## 原型仓库对照

校园便利汇 dbOperations 覆盖：帖子、评论、点赞、收藏、关注、私信、举报、用户管理。模块拆分：
- `marketCategories.js` — 集市分类（主分类 + 历史兼容 + 归一化）
- `activityZoneCore.js` — 活动专区期次管理
- `webAdminHandlers.js` — H5 管理后台逻辑（内联执行避免云函数互调失败）
- `analyticsDashboard.js` — 数据看板聚合统计

## 动手练习

- [ ] 实现 posts 增删改查（action 分发）
- [ ] 实现点赞（幂等写入 makeDeterministicId）
- [ ] 实现收藏/关注（幂等）

---

*第 3 站完成 · 下一步: 第 4 站 notifySender 订阅消息*

---
> **CloudBase 学习路径系列**: [[cloudbase-learning-s1-login|① 登录]] · [[cloudbase-learning-s2-contentcheck|② 内容安全]] · [[cloudbase-learning-s3-dboperations|③ 统一CRUD]] · [[cloudbase-learning-s4-notifysender|④ 订阅消息]] · [[cloudbase-learning-s5-marketcategories|⑤ 分类体系]] · [[cloudbase-learning-s6-adminpanel|⑥ 管理后台]] · [[cloudbase-learning-s7-analytics|⑦ 数据看板]] · [[cloudbase-learning-s8-activity|⑧ 活动专区]] | [[HOME|🏠 首页]]
