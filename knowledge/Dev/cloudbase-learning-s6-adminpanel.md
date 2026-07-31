---
tags: [cloudbase, miniprogram, wechat, learning, admin-panel]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 6 站：adminPanel + webAdminHandlers 管理后台

> 对照校园便利盒 adminPanel 云函数 + 微信官方文档 + 掘金实战
> 学习日期: 2026-07-31

## 核心概念：双鉴权设计

```
管理端访问路径：
├── 小程序管理员 → 云函数 getWXContext().OPENID → users 表 role=admin 校验
└── Web 匿名登录 → ADMIN_WEB_SECRET 环境变量与请求 webSecret 一致
```

```javascript
// 鉴权 ①：小程序管理员（users 表 role 校验）
async function checkAdmin(openid) {
  if (!openid) return false
  const res = await db.collection('users').where({ _openid: openid, role: 'admin', status: 'active' }).get()
  return res.data.length > 0
}

// 鉴权 ②：Web 匿名登录（环境变量密钥）
const webSecret = process.env.ADMIN_WEB_SECRET
if (event.webSecret !== webSecret) return { code: -1, msg: 'unauthorized' }
```

**为什么双鉴权**：
- 小程序端：用微信身份（role=admin），体验好
- Web 端：没有微信登录态（匿名登录），用共享密钥
- 两层都拦 → 管理接口不会裸奔

## 核心概念：云函数内联复用（避免互调失败）

校园便利盒精华设计：

```javascript
// webAdminHandlers.js 在 dbOperations 进程内执行，与 adminPanel 共用逻辑
// 而不是 dbOperations 去 callFunction 调 adminPanel —— 避免云函数互调超时/失败
const webAdminDispatch = createWebAdminDispatch(db, _, cloud, {
  triggerSubscribeNotify: (payload) => triggerSubscribeNotify(payload)  // lazy wrapper 防循环引用
})
```

**为什么内联**：云函数间 `callFunction` 可能超时/失败（冷启动 + 网络开销）。把逻辑抽成共享模块，在调用方进程内执行 → 稳定。

## 管理后台开发要点（掘金实战精华）

| 要点 | 说明 |
|------|------|
| 静态托管 | 云开发自带静态网站托管，直接部署 Vue/Uniapp 后台 |
| 安全来源 | 静态托管域名必须加入安全来源配置 |
| 匿名登录 | Web 端调云函数必须匿名登录（CloudBase JS SDK） |
| CORS | 跨域问题在云开发控制台配置 |
| 管理员表 | admin 表存管理员账号，云函数验证角色 |
| 所有接口鉴权 | 没有例外 |

## 架构原则（微信官方 + 实战共识）

```
小程序只负责展示
云函数负责所有业务逻辑与支付
数据库只给云函数写权限
管理后台用静态托管 + 管理员云函数
```

**绝对不要**：
- ❌ 小程序端直接操作数据库（写）
- ❌ 支付密钥放前端代码
- ❌ 云函数不校验 OPENID（伪造请求）
- ❌ 管理后台无角色鉴权

## 云开发控制台权限体系

| 角色 | 权限 |
|------|------|
| 小程序管理员 | 最高权限（与 mp.weixin.qq.com 管理员一致） |
| 云开发管理员 | 完整权限（最多 3 人） |
| 云开发开发者 | 小程序管理员/云开发管理员指定 |

## 校园便利盒 adminPanel 模块结构

```
adminPanel/
├── index.js               ← 入口 + checkAdmin + 路由分发
├── analyticsDashboard.js  ← 数据看板（聚合统计）
├── marketCategories.js    ← 分类管理
├── activityZoneCore.js    ← 活动专区管理
├── wxacodeHelper.js       ← 小程序码生成（getWxacodeUnlimitedBuffer）
└── config.json            ← 云调用权限声明
```

## 踩坑清单

| 坑 | 现象 | 修复 |
|----|------|------|
| Web 端 401 | 匿名登录没配 | 静态托管域名加安全来源 + CloudBase JS SDK 匿名登录 |
| 云函数互调超时 | 管理操作偶发失败 | 内联复用（webAdminHandlers 模式） |
| 无权限 | api unauthorized | config.json 没配 permissions.openapi |
| 跨域 | Web 端调不通 | 控制台配置 CORS |

## 动手练习

- [ ] 实现「封禁用户」管理接口（checkAdmin + users 表 status 更新）
- [ ] H5 管理页 + 匿名登录 + ADMIN_WEB_SECRET 鉴权
- [ ] 数据看板聚合统计

---

*第 6 站完成 · 下一步: 第 7 站 analyticsDashboard 数据看板*
