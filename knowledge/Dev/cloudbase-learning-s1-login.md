---
tags: [cloudbase, miniprogram, wechat, learning, login]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 1 站：login 登录与用户体系

> 对照 `Joho6666/xiaoyuanbianlihe` login 云函数 + 微信官方文档 + CloudBase 文档
> 学习日期: 2026-07-31

## 核心概念

### 免鉴权身份注入（CloudBase 最大优势）

```
小程序端 wx.cloud.callFunction('login')
        │  微信自动注入身份（无需 code2session）
        ▼
云函数内 cloud.getWXContext() → { OPENID, APPID, UNIONID }
        │
        ▼
users 表: { _openid, nickName, avatarUrl, role, status }
```

**关键认知**：`getWXContext()` 返回的 OPENID 是**微信从基础库到云函数全链路透传**的，不是请求体里的字段，业务代码改不了也伪造不了 → 可直接当身份用。

### 云函数最小模板

```javascript
// cloudfunctions/login/index.js
const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })  // 标准写法：自动用当前环境

exports.main = async (event) => {
  const { OPENID, APPID, UNIONID } = cloud.getWXContext()
  // 查 users 表，新用户自动注册
  const db = cloud.database()
  const users = db.collection('users')
  const existing = await users.where({ _openid: OPENID }).get()
  if (!existing.data.length) {
    await users.add({ data: { _openid: OPENID, role: 'user', status: 'active', createTime: db.serverDate() } })
  }
  return { openid: OPENID }
}
```

## 踩坑清单（重要！）

| 坑 | 现象 | 修复 |
|----|------|------|
| **未 init** | `wxContext.OPENID` 是 undefined | 云函数顶部必须 `cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })` |
| **UNIONID 空值** | 未登录访客调用时 UNIONID 可能为空字符串 | 业务里做空值兜底 |
| **非法的 env** | `errCode: -404011` | 控制台 → 环境配置 → 安全配置 → **小程序关联**，填 AppID |
| **DATABASE_PERMISSION_DENIED** | `-502005` | 云函数执行身份**继承调用方 OPENID**，不是 admin！读全表需显式管理员客户端 |
| **callFunction vs request** | 返回值在 `res.result` 不在 `res.data` | 这是跟 wx.request 最容易记混的地方 |

## 安全要点（微信官方 Skill 文档精华）

1. **AI/用户参数不可信任** — 云函数内校验类型/范围/长度
2. **所有权/越权校验** — where 条件必须带 `_openid`，避免误改他人数据
3. **写操作一律走云函数** — 增删改由云函数落库，禁止客户端直连数据库写入
4. **只读直连需安全规则** — `auth.openid == doc._openid`
5. **密钥只放环境变量** — 绝不写入小程序端代码或接口返回值

## 原型仓库对照

校园便利盒 login 云函数职责（对照理解）：
- `getWXContext()` 拿 OPENID
- users 表: `{ _openid, nickName, avatarUrl, role: 'user'|'admin', status, campusId }`
- role 字段是管理端双鉴权的基础（后续第 6 站展开）

## 动手练习（可选）

- [ ] 写一个只存 openid + 首次注册时间的 login 云函数
- [ ] 部署到自己的 CloudBase 环境（免费额度）
- [ ] 小程序端 wx.cloud.callFunction 调通

---

*第 1 站完成 · 下一步: 第 2 站 contentCheck 内容安全*
