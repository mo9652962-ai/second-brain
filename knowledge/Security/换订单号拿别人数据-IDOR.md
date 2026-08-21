---
tags: [后端, idor, 越权, AI生成接口, 登录不等于权限, 攻防一体]
domain: Security
status: fresh
date: 2026-08-21
---

# 换订单号拿别人订单 = IDOR（程序员Orion · 抖音 2026-08-21）

> 来源：抖音 @程序员Orion（创业中）《我只换了一个订单号，AI写的接口竟然返回了别人的订单？》（1:26，页面章节要点）
> 系列：接口安全第三视角（①前端隐藏≠安全 ②接口三件套 ③IDOR）

## 核心认知

> **登录 ≠ 有权限**——AI 写的接口只验证「登录了没」，没验证「资源是不是你的」

- 换 order_id → 返回别人订单 = **IDOR / 水平越权**（OWASP A01）
- AI 生成接口高频坑：只做认证（Authentication）没做授权（Authorization）

## 正确做法（后端授权）

```
① 确定用户身份 (session/token → user_id)
② 按业务权限判断: 该资源属于当前用户吗?
   SELECT * FROM orders WHERE id=? AND user_id=?   ← 关键: 带 user_id 过滤
③ 不属于 → 403 拒绝
④ 权限检查覆盖全接口: 列表/详情/修改/删除/导出 都要
```

## 错误代码 vs 正确代码

```python
# ❌ 只验证登录 (AI 常见)
@app.get("/api/order/{order_id}")
def get_order(order_id):
    if not session.get("user"): return 401
    return db.query(f"SELECT * FROM orders WHERE id={order_id}")  # 谁的都能查

# ✅ 验证归属
@app.get("/api/order/{order_id}")
def get_order(order_id):
    user = session.get("user")
    if not user: return 401
    row = db.query("SELECT * FROM orders WHERE id=? AND user_id=?", order_id, user.id)
    if not row: return 403   # 不是你的 → 拒绝
    return row
```

## SRC 挖法（攻防一体）

```
① 登录自己账号 → 拿一个自己的 order_id/resource_id
② 改成别人的 ID (±1 / UUID 枚举 / 批量 ids=[...])
③ 返回 200 + 别人数据 = IDOR 确认
④ 注意: 请求体/文件路径/GraphQL 参数里的 ID 都要测
完整方法论: src-bug-hunting 技能「IDOR 深度方法论」6 步工作流
```

## 关联

- bizlogic_lab.py 靶场（越权 IDOR 模块）
- src-bug-hunting 技能 IDOR 章节
- `Security/前端隐藏不等于安全-后端鉴权.md` / `Security/接口三件套-攻防一体.md`
