# URL 短链系统设计

> **技能**: system-design-primer | **复杂度**: ⭐⭐⭐
> **方法**: 四步设计法（约束→高层→核心→扩展）
> **关键词**: 分布式、哈希、Base62、缓存、分片

---

## Step 1: 约束与假设

### 使用场景
- 用户输入长 URL → 生成短链
- 用户访问短链 → 302 重定向到长 URL
- 可选过期时间
- 访问统计

### 数据估算
```
月写入: 1 亿条
月读取: 10 亿次
读写比: 10:1
短链长度: 7 字符
每条存储: ~500 bytes (URL + 元数据)
年增长: ~600 GB
```

## Step 2: 高层设计

```
Client ─→ DNS ─→ LB ─→ Web Server ─→ Write API
                                      → Read API
                                      → Cache (Redis)
                                      → DB (SQL)
                                      → CDN (静态)
```

### 核心组件
| 组件 | 技术选型 | 理由 |
|:----|:--------|:----|
| 负载均衡 | Nginx/HAPoxy | L7 路由，SSL 终结 |
| Web 服务器 | Nginx | 反向代理，静态资源 |
| API 服务 | Go/Rust | 高性能，低延迟 |
| 数据库 | PostgreSQL | 强一致，支持事务 |
| 缓存 | Redis Cluster | 高吞吐读请求 |
| 对象存储 | S3/MinIO | 存储完整 URL (可选) |

## Step 3: 核心组件设计

### 短链生成算法

```
输入: 长 URL + 时间戳
  ↓
MD5 hash (128 bit)
  ↓
Base62 编码 ([a-zA-Z0-9])
  ↓
取前 7 字符 → 62^7 ≈ 3.5 万亿种组合
  ↓
查重 ← 碰撞？→ 拼接盐值重新哈希
  ↓
存入数据库
```

**Python 实现**
```python
import hashlib
import base64

def generate_short_url(original_url: str, salt: str = "") -> str:
    """生成 7 字符短链"""
    content = original_url + salt
    md5_hash = hashlib.md5(content.encode()).digest()
    # 取前 7 bytes → Base62
    num = int.from_bytes(md5_hash[:7], 'big')
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    result = ""
    for _ in range(7):
        result = chars[num % 62] + result
        num //= 62
    return result
```

### 数据库 Schema
```sql
CREATE TABLE url_mappings (
    short_key   CHAR(7) PRIMARY KEY,
    original_url TEXT NOT NULL,
    created_at  TIMESTAMP DEFAULT NOW(),
    expires_at  TIMESTAMP,
    visit_count BIGINT DEFAULT 0
);

CREATE INDEX idx_expires ON url_mappings(expires_at);
```

### API 设计
```http
# 创建短链
POST /api/shorten
Content-Type: application/json

{
    "url": "https://example.com/very/long/url/that/needs/shortening",
    "expires_in_days": 30
}

→ 201 Created
{
    "short_key": "aB3xK9m",
    "short_url": "https://s.lu/aB3xK9m"
}

# 访问短链
GET /{short_key}
→ 302 Found
Location: https://example.com/very/long/url/...
```

## Step 4: 扩展设计

### 读优化 (读多写少 10:1)

```
用户访问短链
  ↓
DNS → LB → Web Server
  ↓
Redis Cache (TTL: 24h)
  ├── Hit → 直接返回
  └── Miss → 查 PostgreSQL
              ↓
             回填 Redis
              ↓
             返回结果
```

### 缓存策略

| 策略 | 实现 | 效果 |
|:----|:----|:----|
| Cache-Aside | 读时先查缓存 | 减少 90% DB 读 |
| 预刷新 | 热点数据 TTL 前自动刷新 | 减少缓存穿透 |
| LRU 淘汰 | Redis 内置 | 内存可控 |

### 写扩展

```
写入量 1 亿/月 ≈ 40/s
  ↓
单 PostgreSQL 可承受
  ↓
未来扩展：
├── 分片: short_key 前 1 字符 (62 分片)
├── 读写分离: 主写从读
└── 异步: 写队列 + 批量写入
```

### 可用性设计

```
SLA 目标: 99.99% (年停机 52 分钟)
  ↓
高可用方案:
├── 多 LB 热备 (Active-Active)
├── PostgreSQL 主从复制
├── Redis Sentinel/Sentinel
├── CDN 边缘缓存
└── 多可用区部署
```

## 成本估算

| 组件 | 规格 | 月成本 |
|:----|:----|:-----:|
| Web Server (×2) | 2C4G | $40 |
| Redis (×3) | 4G 集群 | $60 |
| PostgreSQL (主+从) | 4C8G ×2 | $120 |
| 负载均衡 | 托管的 | $20 |
| CDN | 按流量 | $50-100 |
| **总计** | | **$290-340/月** |

## 技术选型对比

| 方案 | 优点 | 缺点 | 适用 |
|:----|:----|:----|:----|
| **Base62** | 短链短，无特殊字符 | 需要处理碰撞 | ✅ 推荐 |
| **UUID** | 无需碰撞处理 | 长度 36 字符 | ❌ 太长 |
| **自增 ID** | 简单 | 可预测、需发号器 | ❌ 不安全 |
| **布隆过滤器** | 快速判断是否存在 | 有误判率 | ✅ 可辅助 |

## 面试回答要点

### 瓶颈与优化
1. **读 QPS**: Redis 缓存可承受 10 万+ QPS
2. **写 QPS**: PostgreSQL 单机可承受 1000+ TPS
3. **存储**: 年增长 600GB，3 年约 2TB，可扩展
4. **热点**: 热门短链 CDN 边缘缓存
5. **防爬**: 限流 + 验证码 + IP 黑白名单

### 追问答案
- **Q: 如何生成更好记的短链？** → 自定义别名 + 字典词组合
- **Q: 用户可删除短链吗？** → 软删除 + 标记过期
- **Q: 如何防恶意生成？** → 用户限流 + 验证码 + 黑名单

## 生成日期

2026-07-22 | 由 system-design-primer 知识 + engineering-workflow skill 生成
