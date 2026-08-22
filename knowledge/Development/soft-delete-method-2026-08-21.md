---
tags: [后端, mysql, 软删除, 商业交付, sqlite]
domain: Development
status: fresh
date: 2026-08-21
---

# 软删除（Soft Delete）方法论（程序员Orion · 抖音 2026-08-21）

> 来源：抖音 @程序员Orion（创业中）《拒绝物理超度！独立开发者必会的 MySQL 软删除》（1:14）
> 转写 359 字（SenseVoice）

## 核心

- **学校教**：删除接口 = 一句 DELETE 物理删除（"物理超度"）
- **商业现实**：数据是核心资产——用户误删想找回？查历史流水？物理删除 = 挽救机会都没有，客户直接拉黑
- **商业交付标准：软删除**——给表加字段，删除时 UPDATE 标记，查询永远过滤

## 打法

```sql
-- 1. 表加字段
ALTER TABLE users ADD COLUMN is_deleted TINYINT DEFAULT 0;
-- 或时间戳版（更优）:
ALTER TABLE users ADD COLUMN deleted_at TEXT NULL;

-- 2. 删除 = UPDATE 标记（不 DELETE）
UPDATE users SET is_deleted = 1 WHERE id = ?;
-- 时间戳版:
UPDATE users SET deleted_at = CURRENT_TIMESTAMP WHERE id = ?;

-- 3. 查询永远过滤
SELECT * FROM users WHERE is_deleted = 0;
SELECT * FROM users WHERE deleted_at IS NULL;
```

## 时间戳版 vs 布尔版

| 维度 | is_deleted (0/1) | deleted_at (时间戳) |
|:---|:---|:---|
| 是否删除 | ✅ | ✅ |
| 何时删除 | ❌ 不知道 | ✅ |
| 恢复/审计 | 手动 | ✅ 有删除时间 |
| 报表（删除趋势）| ❌ | ✅ |

## 墨题对照（2026-08-21 实测）

墨题后端 `backend/app/database.py` 已用**时间戳版**（`deleted_at TEXT` + `WHERE deleted_at IS NULL`）——已达标 ✅

## SRC 视角（攻防一体）

- 软删除数据 = 隐藏攻击面：接口没过滤 `deleted_at IS NULL` → IDOR 查「已删除」数据 / 数据残留泄露
- 测试删除接口时：观察是物理删（DELETE）还是软删（UPDATE）→ 软删后可尝试数据恢复漏洞

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]
