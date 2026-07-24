---
tags: [design, wechat-miniprogram, campus, project-plan]
domain: Programming
created: 2026-07-24
---

# 校园便利盒 — 完整设计方案

> 基于微信小程序云开发（CloudBase）的校园生活服务平台

---

## 一、系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    微信小程序端                          │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐          │
│  │ 首页  │ │ 集市  │ │ 发布  │ │ 消息  │ │ 我的  │          │
│  │信息流 │ │分类  │ │选择  │ │会话  │ │个人  │          │
│  │公告   │ │筛选  │ │表单  │ │聊天  │ │管理  │          │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘          │
└──────────────────────┬──────────────────────────────────┘
                       │ 云调用
┌──────────────────────▼──────────────────────────────────┐
│                 腾讯云开发 CloudBase                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  云函数   │  │  云数据库  │  │  云存储   │              │
│  │ Node.js  │  │  JSON    │  │  图片/文件│              │
│  └──────────┘  └──────────┘  └──────────┘              │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                   Web 运营后台                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ 内容审核  │  │ 公告发布  │  │ 数据统计  │              │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
```

---

## 二、数据库详细设计

### 2.1 用户表 `users`

| 字段 | 类型 | 说明 |
|:-----|:-----|:------|
| `_id` | string | 自动 |
| `openId` | string | 微信唯一标识（云函数自动获取） |
| `nickname` | string | 昵称 |
| `avatar` | string | 头像 URL |
| `phone` | string | 手机号（可选） |
| `school` | string | 学校（首次填写） |
| `studentId` | string | 学号（可选认证） |
| `role` | string | `user` / `admin` |
| `createTime` | date | 注册时间 |
| `lastLogin` | date | 最后登录 |

### 2.2 商品表 `goods`

| 字段 | 类型 | 说明 |
|:-----|:-----|:------|
| `_id` | string | 自动 |
| `title` | string | 商品标题 |
| `price` | number | 价格（元） |
| `originalPrice` | number | 原价（可选） |
| `images` | array[string] | 图片 fileID 列表 |
| `description` | string | 商品描述 |
| `category` | string | `数码`/`书籍`/`生活`/`服饰`/`其他` |
| `sellerOpenId` | string | 卖家 openId |
| `sellerInfo` | object | `{nickname, avatar}` |
| `status` | string | `selling`(在售) / `sold`(已售) / `off`(下架) |
| `views` | number | 浏览次数 |
| `createTime` | date | 发布时间 |
| `updateTime` | date | 更新时间 |

### 2.3 帖子表 `posts`

| 字段 | 类型 | 说明 |
|:-----|:-----|:------|
| `_id` | string | 自动 |
| `type` | string | `help`(互助) / `share`(分享) / `activity`(活动) |
| `content` | string | 正文 |
| `images` | array[string] | 图片列表 |
| `authorOpenId` | string | 作者 |
| `authorInfo` | object | `{nickname, avatar}` |
| `comments` | number | 评论数 |
| `likes` | number | 点赞数 |
| `status` | string | `normal` / `hidden` |
| `createTime` | date | 发布时间 |

### 2.4 会话表 `conversations`

| 字段 | 类型 | 说明 |
|:-----|:-----|:------|
| `_id` | string | 自动 |
| `participants` | array[string] | 参与双方 openId |
| `relatedGoodsId` | string | 关联商品 ID（可选） |
| `lastMessage` | object | `{content, sender, time}` |
| `unread` | object | `{ openId_A: 0, openId_B: 1 }` |
| `createTime` | date | 创建时间 |

### 2.5 消息表 `messages`

| 字段 | 类型 | 说明 |
|:-----|:-----|:------|
| `_id` | string | 自动 |
| `conversationId` | string | 所属会话 ID |
| `sender` | string | 发送方 openId |
| `receiver` | string | 接收方 openId |
| `content` | string | 内容 |
| `type` | string | `text` / `image` |
| `imageUrl` | string | 图片 URL（type=image） |
| `createTime` | date | 发送时间 |

### 2.6 公告表 `notices`

| 字段 | 类型 | 说明 |
|:-----|:-----|:------|
| `_id` | string | 自动 |
| `title` | string | 标题 |
| `content` | string | 正文（支持 HTML） |
| `coverImage` | string | 封面图 |
| `type` | string | `notice`(公告) / `activity`(活动) |
| `status` | string | `draft` / `published` |
| `publishTime` | date | 发布时间 |
| `createTime` | date | 创建时间 |

### 2.7 数据库权限规则

```json
// goods 表
{
  "read": true,                          // 所有人可读
  "write": "doc._openid == auth.openid"   // 仅创建者可写
}

// messages 表
{
  "read": "doc.sender == auth.openid || doc.receiver == auth.openid",
  "write": "doc.sender == auth.openid"
}
```

---

## 三、页面架构与交互

### 3.1 底部 Tab（5 个）

```
🏠 首页     🛒 集市     ➕ 发布     💬 消息     👤 我的
```

### 3.2 首页

```
┌─────────────────────────┐
│  搜索框 🔍              │
├─────────────────────────┤
│  [轮播公告 Banner]       │
├─────────────────────────┤
│  快捷入口                │
│  📚二手书 🖥️数码 🏠生活   │
├─────────────────────────┤
│  最新动态 (信息流)        │
│  ┌──────────────────┐   │
│  │ 公告: ...         │   │
│  │ 商品: ...         │   │
│  │ 帖子: ...         │   │
│  └──────────────────┘   │
└─────────────────────────┘
```

### 3.3 集市页

```
┌─────────────────────────┐
│  分类: 全部 数码 书籍 ... │
├─────────────────────────┤
│  ┌────┐ ┌────┐ ┌────┐  │
│  │图片│ │图片│ │图片│  │
│  │标题│ │标题│ │标题│  │
│  │¥价格│ │¥价格│ │¥价格│  │
│  └────┘ └────┘ └────┘  │
│  瀑布流布局              │
└─────────────────────────┘
```

### 3.4 发布页

```
┌─────────────────────────┐
│  [选择发布类型]           │
│  📦 卖二手  📝 发帖子     │
├─────────────────────────┤
│  上传图片 (最多9张)       │
│  ┌──┐ ┌──┐ ┌──┐        │
│  │📷│ │📷│ │📷│        │
│  └──┘ └──┘ └──┘        │
│  标题: [____________]    │
│  价格: [____________]    │
│  描述: [____________]    │
│  分类: [选择 ▼]          │
│                         │
│  [📤 发布]              │
└─────────────────────────┘
```

### 3.5 消息页

```
┌─────────────────────────┐
│  消息                    │
├─────────────────────────┤
│  👤 张三    关于iPhone  │
│  你好，还在吗？  10:30   │
├─────────────────────────┤
│  👤 李四    关于教材    │
│  可以便宜点吗？ 昨天     │
├─────────────────────────┤
│  空状态: 暂无消息        │
└─────────────────────────┘
```

### 3.6 聊天页

```
┌─────────────────────────┐
│  ← 张三     商品: iPhone│
├─────────────────────────┤
│  ┌──────────┐           │
│  │ 你好     │ 我 →      │
│  └──────────┘           │
│           ┌──────────┐  │
│  ← 对方   │ 还在的   │  │
│           └──────────┘  │
│  ┌──────────┐           │
│  │ 能便宜吗 │ 我 →      │
│  └──────────┘           │
├─────────────────────────┤
│  [输入框...]  [发送]     │
└─────────────────────────┘
```

---

## 四、云函数 API 清单

| 云函数 | 功能 | 参数 |
|:-------|:-----|:------|
| `login` | 用户登录/注册 | code → openId |
| `getGoods` | 获取商品列表 | category, page, keyword |
| `getGoodsDetail` | 商品详情 | goodsId |
| `addGoods` | 发布商品 | title, price, images, desc |
| `updateGoods` | 更新商品状态 | goodsId, status |
| `addPost` | 发布帖子 | type, content, images |
| `getPosts` | 获取帖子列表 | type, page |
| `getConversations` | 获取会话列表 | — |
| `sendMessage` | 发送消息 | conversationId, content, type |
| `getMessages` | 获取消息列表 | conversationId, page |
| `getNotices` | 获取公告 | — |
| `uploadImage` | 上传图片 | filePath → fileID |

---

## 五、项目目录结构

```
campus-box/
├── miniprogram/              # 小程序前端
│   ├── app.js/css/json       # 全局配置
│   ├── pages/
│   │   ├── index/            # 首页
│   │   ├── market/           # 集市
│   │   ├── publish/          # 发布
│   │   ├── message/          # 消息列表
│   │   ├── chat/             # 聊天
│   │   ├── profile/          # 我的
│   │   ├── goods-detail/     # 商品详情
│   │   └── post-detail/      # 帖子详情
│   ├── components/           # 公共组件
│   │   ├── goods-card/       # 商品卡片
│   │   ├── post-card/        # 帖子卡片
│   │   └── loading/          # 加载状态
│   ├── images/               # 图标资源
│   └── utils/                # 工具函数
│       ├── util.js
│       └── cloud.js          # 云函数封装
├── cloudfunctions/           # 云函数
│   ├── login/
│   ├── getGoods/
│   ├── addGoods/
│   ├── sendMessage/
│   └── ...
└── admin/                    # Web运营后台(可选)
    ├── index.html
    └── ...
```

---

## 六、实施路线图

建议先完成 MVP（最小可行产品），再迭代添加功能。

| 阶段 | 内容 | 预估 |
|:-----|:------|:----:|
| **Phase 1** | 环境搭建 + 底部Tab + 用户登录 | 1 天 |
| **Phase 2** | 商品发布 + 商品列表 + 商品详情 | 2 天 |
| **Phase 3** | 私信聊天 + 消息通知 | 2 天 |
| **Phase 4** | 首页信息流 + 公告 + 帖子 | 2 天 |
| **Phase 5** | 运营后台（CloudBase CMS） | 1 天 |
| **Phase 6** | 测试 + 发布上线 | 1 天 |

**总计：约 7-10 天可以实现完整 MVP**

---

## 七、关键页面路径

```
用户打开小程序
    ↓
[登录/注册] ← 首次自动弹窗
    ↓
[首页] ← 信息流 / 公告 / 快捷入口
    ↓
[集市] ← 分类浏览 / 搜索 / 瀑布流
    ↓
[商品详情] ← 图片 / 描述 / 联系卖家
    ↓
[聊天] ← 私信沟通 / 讨价还价
    ↓
[确认交易] ← 线下 / 线上
    ↓
完成 ✅
```
---
> 关联: [[Programming]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]
