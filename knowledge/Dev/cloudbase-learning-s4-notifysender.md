---
tags: [cloudbase, miniprogram, wechat, learning, subscribe-message]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 4 站：notifySender 订阅消息

> 对照校园便利盒 notifySender 云函数 + 微信官方文档
> 学习日期: 2026-07-31

## 核心概念：订阅消息的两大特性

1. **必须用户授权**：只能给"同意接收"的用户发固定模板通知
2. **一次性**：一次授权只能发一次消息 → 每次发送前都要重新申请权限

## 发送流程（三步）

```
① 后端返回模板 ID（提供接口）
        ↓
② 前端 requestSubscribeMessage 向用户申请权限（获得一次下发额度）
        ↓
③ 后端 subscribeMessage.send 使用额度发消息
```

## 云调用实现（免 access_token）

```javascript
// cloudfunctions/notifySender/index.js
const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

exports.main = async (event) => {
  const { OPENID } = cloud.getWXContext()
  try {
    const result = await cloud.openapi.subscribeMessage.send({
      touser: event.openid || OPENID,
      page: 'index',
      data: {
        thing1: { value: '有人回复了你的帖子' },
        time2: { value: '2026年7月31日 14:00' }
      },
      templateId: 'TEMPLATE_ID',   // 公众平台申请
      miniprogramState: 'developer' // developer/trial/formal
    })
    return result
  } catch (err) {
    return err
  }
}
```

**config.json 声明权限**：
```json
{
  "permissions": { "openapi": ["subscribeMessage.send"] },
  "triggers": [{ "name": "timer", "type": "timer", "config": "*/5 * * * * * *" }]
}
```
（triggers 字段 = 定时触发器，可让云函数定时运行）

## 前端申请权限

```javascript
// 获取模板 ID → 申请权限
const { result } = await wx.cloud.callFunction({ name: 'getTemplateId' })
wx.requestSubscribeMessage({
  tmplIds: [result.templateId],
  success(res) {
    // res['TEMPLATE_ID'] === 'accept' 表示用户同意
  }
})
```

## 校园便利盒精华：内部鉴权（INTERNAL_NOTIFY_SECRET）

```javascript
// notifySender 只接受带内部密钥的调用 —— 防止被任意用户直接调用刷消息
const internalSecret = String(process.env.INTERNAL_NOTIFY_SECRET || '').trim()
if (!internalSecret) return  // 未配置则静默跳过（开发环境不阻塞）

// 调用方（adminPanel/dbOperations）携带密钥：
await cloud.callFunction({
  name: 'notifySender',
  data: { action: 'send', internalSecret, data: payload }
})
```

**设计要点**：
- 密钥放**环境变量**（不是代码里）
- 未配置密钥 → 静默跳过（优雅降级，不阻塞主流程）
- 用 lazy wrapper 避免循环引用（adminPanel ↔ notifySender 互相调用）

## 踩坑清单

| 坑 | 现象 | 修复 |
|----|------|------|
| **用户没授权** | 发送返回 code 43101 | 用户未同意或额度用完 → 引导重新授权 |
| **模板字段不符** | 发送失败 | data 的 key 必须与模板字段类型完全一致（thing/time/number/date） |
| **无权限调用** | api unauthorized | config.json 没配 permissions.openapi |
| **字段值超长** | 发送失败 | thing 类型限 20 字符，注意截断 |

## 原型仓库对照

校园便利盒 notifySender 职责：
- 被 adminPanel / dbOperations 调用（事件触发：有人回复/订单状态变化）
- INTERNAL_NOTIFY_SECRET 内部鉴权防滥用
- 消息失败 console.warn 降级，不阻塞主流程

## 动手练习

- [ ] 公众平台申请一个订阅消息模板
- [ ] 前端 requestSubscribeMessage 授权
- [ ] 云函数发送 + INTERNAL_NOTIFY_SECRET 鉴权

---

*第 4 站完成 · 下一步: 第 5 站 marketCategories 分类体系*

---
> **CloudBase 学习路径系列**: [[cloudbase-learning-s1-login|① 登录]] · [[cloudbase-learning-s2-contentcheck|② 内容安全]] · [[cloudbase-learning-s3-dboperations|③ 统一CRUD]] · [[cloudbase-learning-s4-notifysender|④ 订阅消息]] · [[cloudbase-learning-s5-marketcategories|⑤ 分类体系]] · [[cloudbase-learning-s6-adminpanel|⑥ 管理后台]] · [[cloudbase-learning-s7-analytics|⑦ 数据看板]] · [[cloudbase-learning-s8-activity|⑧ 活动专区]] | [[HOME|🏠 首页]]
