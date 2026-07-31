---
tags: [research, project-study, miniprogram, cloudbase, wechat, campus]
created: 2026-07-31
status: absorbed
---

# 校园便利盒 (xiaoyuanbianlihe) 项目研究 — 全部落地

> 2026-07-31 · 对 `Joho6666/xiaoyuanbianlihe`（微信小程序校园生活服务平台）的完整研究
> 结论：**完全可利用** — 正是 wechat-miniprogram-cloudbase skill 的原型，三项落地完成

## 项目概况

| 项 | 内容 |
|----|------|
| 仓库 | [Joho6666/xiaoyuanbianlihe](https://github.com/Joho6666/xiaoyuanbianlihe) |
| 描述 | 校园生活服务微信小程序（校园动态/二手集市/互助发布/私信/活动公告/运营后台） |
| 技术栈 | 微信小程序 + CloudBase 云开发 + JavaScript |
| 规模 | 386 文件 / 8 云函数 / 25+ 页面 / Web 管理后台 |
| 活跃度 | 2026-04 创建，2026-07-23 最后推送（活跃中） |
| 目标学校 | 桂林航天工业学院（guit-hangtian） |

## 三项落地成果

### 1. Skill 升级 — wechat-miniprogram-cloudbase v1.0.0 → v2.0.0
- 补充真实原型仓库地址
- 版本升级

### 2. 接单脚手架 — `references/miniprogram-order-scaffold.md`
- 需求匹配矩阵（二手/信息流/私信/后台/审核/活动/裂变 → 复用模块）
- 可直接抄的技术结构（8 云函数职责）
- 6 个必须保留的工程模式（幂等写入/双鉴权/多校区隔离/内联复用/订阅鉴权/部署脚本）
- **接单报价参考**（完整平台 3000-8000 / 单项 400-2000）
- 风险提醒（无 license 需重写、UGC 必须过审、主体限制、CloudBase 计费）

### 3. 学习路径 — `references/cloudbase-learning-path.md`
- 8 站从易到难：login → contentCheck → dbOperations → notifySender → marketCategories → adminPanel → analyticsDashboard → activityZoneCore
- 每站：核心概念 + 学到什么 + 动手练习
- 学习产出建议（写笔记/部署/沉淀）

## 工程模式精华（抄录）

```javascript
// 幂等写入（防并发重复）— 点赞/关注/收藏场景
function makeDeterministicId(scope, ...parts) {
  const raw = [scope, ...parts.map(p => String(p == null ? '' : p))].join('|')
  return `${scope}_${crypto.createHash('md5').update(raw).digest('hex')}`
}

// 双鉴权 — 小程序 role=admin + Web ADMIN_WEB_SECRET
// 多校区隔离 — campusWhereClause() 默认校区兼容老数据
// 云函数内联复用 — webAdminHandlers 在 dbOperations 进程内执行（避免互调失败）
// 订阅消息内部鉴权 — INTERNAL_NOTIFY_SECRET，未配置静默跳过
```

## 风险提醒

- 原型仓库**无 license** → 接单交付基于架构思路重写关键文件，不原样提交
- UGC 功能必须接 contentCheck，否则微信审核不通过
- 客户需有合规小程序主体（个人主体类目受限）

---

*研究完成 2026-07-31 · learn→research→apply 全流程 · 三项全部落地*
