---
tags: [cloudbase, miniprogram, wechat, learning, category]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 5 站：marketCategories 分类体系

> 对照校园便利盒 marketCategories.js + 微信/电商分类设计实践
> 学习日期: 2026-07-31

## 核心概念：分类归一化 + 向后兼容

校园便利盒的集市分类设计（精华）：

```javascript
const MARKET_PRIMARY_CATEGORIES = ['书籍', '手机数码', '生活用品']
const MARKET_LEGACY_CATEGORIES = ['电器', '美妆', '男装', '女装', '医药', '玩乐', '车品', '技能服务', '虚拟产品', '餐饮']

// 归一化：未知分类 → '其他'，旧分类兼容
function normalizePublishCategory(category) {
  const name = String(category || '').trim()
  if (!name) return '其他'
  if (MARKET_PRIMARY_CATEGORIES.includes(name) || name === '其他') return name
  return '其他'  // 历史分类/未知分类都归入其他
}

// 查询 where：按分类筛选（「其他」含历史分类）
function buildMarketCategoryWhere(_, category) {
  const name = String(category || '').trim()
  if (!name) return null
  if (name === '其他') {
    return _.or([...MARKET_LEGACY_CATEGORIES.map(c => ({ category: c })), { category: '其他' }])
  }
  return { category: name }
}
```

**设计要点**：
1. **主分类精简**：只有 3 个常用分类（书籍/手机数码/生活用品）→ 前端展示不臃肿
2. **历史分类兼容**：老数据（电器/美妆等 10 个旧分类）查询时归入"其他"
3. **归一化兜底**：未知/非法分类 → '其他'，永不报错

## 分类设计模式对比

| 模式 | 适用 | 说明 |
|------|------|------|
| **扁平 + 归一化**（校园便利盒） | 轻量 UGC 集市 | 简单，向后兼容 |
| **父子层级**（parentId + level） | 电商复杂分类 | 树形，支持递归查询 |
| **矩阵交叉**（Type + Brand） | 电商多维度筛选 | 一对多关系，O(1) 查询 |
| **枚举 + 叶子类目**（微信小店） | 平台级审核类目 | cat_id + leaf 标识 |

## 关键认知

1. **分类是易变业务**：平台会调整类目树（合并/拆分/下线）→ 设计时就要考虑向后兼容
2. **反规范化权衡**：冗余字段（分类名直接存商品上）省查询，但要接受一致性风险
3. **缓存策略**：分类信息不常变 → 小程序端 `wx.setStorageSync` 缓存，减少请求
4. **多级 vs 扁平**：校园场景扁平足够；电商复杂场景用多级树

## 校园便利盒其他模块的相似模式

- **多校区隔离**（campusWhereClause）：默认校区兼容无 campusId 字段的老数据 —— 与分类兼容同一思路
- **活动专区**（activityRoundId）：活动结束转普通帖 —— 状态流转设计

## 踩坑清单

| 坑 | 现象 | 修复 |
|----|------|------|
| 分类名含空格/大小写 | 筛选不到 | 统一 trim + toLowerCase 归一化 |
| 老分类数据丢失 | 历史商品不可见 | where 里用 _.or 兼容历史分类 |
| 分类枚举膨胀 | 前端展示混乱 | 主分类精简 + 其他兜底 |

## 动手练习

- [ ] 设计一套可扩展的集市分类（主分类 + 历史兼容）
- [ ] 实现 normalizePublishCategory + buildMarketCategoryWhere
- [ ] 分类数据小程序端缓存

---

*第 5 站完成 · 下一步: 第 6 站 adminPanel + webAdminHandlers 管理后台*

---
> **CloudBase 学习路径系列**: [[cloudbase-learning-s1-login|① 登录]] · [[cloudbase-learning-s2-contentcheck|② 内容安全]] · [[cloudbase-learning-s3-dboperations|③ 统一CRUD]] · [[cloudbase-learning-s4-notifysender|④ 订阅消息]] · [[cloudbase-learning-s5-marketcategories|⑤ 分类体系]] · [[cloudbase-learning-s6-adminpanel|⑥ 管理后台]] · [[cloudbase-learning-s7-analytics|⑦ 数据看板]] · [[cloudbase-learning-s8-activity|⑧ 活动专区]] | [[HOME|🏠 首页]]
