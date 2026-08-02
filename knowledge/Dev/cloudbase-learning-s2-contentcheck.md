---
tags: [cloudbase, miniprogram, wechat, learning, content-check]
created: 2026-07-31
status: learning
---

# CloudBase 学习路径 · 第 2 站：contentCheck 内容安全

> 对照校园便利盒 contentCheck 云函数 + 微信官方文档
> 学习日期: 2026-07-31

## 核心概念：云调用（免鉴权调微信开放接口）

**云调用** = 在云函数中直接调用微信开放服务接口，**免 access_token 管理、免密钥、全程不暴露信息**。

```javascript
// cloudfunctions/contentCheck/index.js
const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })

exports.main = async (event) => {
  try {
    const res = await cloud.openapi.security.msgSecCheck({
      content: event.content  // 文本内容，≤ 500KB
    })
    return res  // errCode 0 = 通过
  } catch (err) {
    return err
  }
}
```

**前置配置**：云函数目录 `config.json` 里声明接口权限：
```json
{
  "permissions": {
    "openapi": ["security.msgSecCheck"]
  }
}
```

## 接口能力

| 接口 | 场景 | 频率限制 |
|------|------|---------|
| `msgSecCheck` (v2) | 文本内容检测（昵称/文章/评论） | 4000 次/分钟，200 万次/天 |
| `mediaCheckAsync` | 图片/音频异步检测 | 异步回调 |

检测能力：色情、时政违规、暴恐等违法有害内容（10 万级敏感词库 + 深度学习）。

## 关键认知

1. **不能完全依赖内容安全服务**（微信官方原文）
   - REVIEW 结果 → 需要人工确认
   - PASS 结果 → 可能漏掉违规内容，按比例抽查
2. **UGC 必须接入** — 含用户发布内容的小程序不接内容安全，微信审核过不了
3. **v1 vs v2**：新版用 `msgSecCheck`（v2 版，含 scene 参数更准），旧版 `msgSecCheck-v1` 已标记过时

## 客户端配合

```javascript
wx.cloud.callFunction({ name: 'contentCheck', data: { content: text } })
  .then(res => {
    if (res.result.errCode == 0) {
      // 审核通过 → 继续发布流程
    } else {
      wx.showModal({ title: '提醒', content: '内容不合规，请修改' })
    }
  })
```

## 踩坑清单

| 坑 | 现象 | 修复 |
|----|------|------|
| **api unauthorized** | 云函数调用报无权限 | config.json 没配 permissions.openapi |
| **云托管走不通** | 云托管非 Node 环境 | 云托管用开放接口服务（控制台配白名单 + cloudbase_access_token） |
| **公众号接口限制** | 部分接口调用失败 | 公众号类型不满足权限要求，云调用无法改变 |

## 原型仓库对照

校园便利盒 contentCheck 职责（推断）：
- 发布帖子/商品前调 msgSecCheck 检测文本
- 违规内容拦截（不落库或标记待审）
- 配合 adminPanel 人工审核兜底（对应"不能完全依赖 AI"）

## 动手练习

- [ ] 创建 contentCheck 云函数（config.json + index.js）
- [ ] 发布流程接入：先检测 → 通过才落库

---

*第 2 站完成 · 下一步: 第 3 站 dbOperations 统一 CRUD（核心）*

---
> **CloudBase 学习路径系列**: [[cloudbase-learning-s1-login|① 登录]] · [[cloudbase-learning-s2-contentcheck|② 内容安全]] · [[cloudbase-learning-s3-dboperations|③ 统一CRUD]] · [[cloudbase-learning-s4-notifysender|④ 订阅消息]] · [[cloudbase-learning-s5-marketcategories|⑤ 分类体系]] · [[cloudbase-learning-s6-adminpanel|⑥ 管理后台]] · [[cloudbase-learning-s7-analytics|⑦ 数据看板]] · [[cloudbase-learning-s8-activity|⑧ 活动专区]] | [[HOME|🏠 首页]]
