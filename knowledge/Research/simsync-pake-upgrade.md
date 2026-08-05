---
aliases:
  - simsync-pake-upgrade
tags:
  - simsync
  - research
  - crypto
  - pake
  - network-security
created: 2026-08-05
updated: 2026-08-05
status: proposed
domain: research
---

# SimSync 存档同步 PAKE 加密升级研究

> 2026-08-05 · 基于 croc (39.3k★) 的 PAKE 方案研究
> 结论先行：**PAKE 加密是可选增强，非必需**——LAN 自用威胁模型低，但升级成本可控，值得做

---

## 一、croc 的 PAKE 实现（研究对象）

### 协议：PAKE2（Boneh-Shoup 密码学书 pg 789）

```
双方预共享弱口令（croc 的房间码）
      │
      ├─→ ECDH 点交换（P/Q 互传，Bytes() 序列化防私钥泄露）
      ├─→ 口令绑定到密钥派生（弱口令 → 强会话密钥）
      └─→ 硬编码椭圆曲线点（siec/P-256/P-384/P-521——防用户传自定义点开后门）

库: schollz/pake (MIT)
进阶: InitCurveWithIdentities 绑定参与方身份（角色 A/B）
安全注意: CVE-2021-31603 曾爆 "Full Plaintext Recovery"——PAKE 实现细节极易出错
```

### 与 SimSync 现状对比

| 维度 | SimSync 现状 | croc PAKE |
|:-----|:------------|:----------|
| 房间码用途 | 仅身份验证（join 时比对） | 派生共享密钥 |
| 消息安全 | HMAC-SHA256 认证（防篡改） | 认证 + 加密（防嗅探） |
| 嗅探风险 | 局域网抓包可见消息内容 | 不可见 |
| 中间人 | 无房间码不能加入 | 无房间码不能加入 + 密钥协商失败 |

## 二、SimSync 升级方案

### 目标
把 6 位房间码（弱口令）通过 PAKE 升级为**强会话密钥**，加密所有消息。

### 架构（改动最小方案）

```
房间码（6 位弱口令）
    │
    ├─→ SPAKE2/PAKE2 握手（join 时，启动器层）
    │      ├─ 房主: InitCurve(password) → P → 发给加入者
    │      └─ 加入者: 收到 P → Q → 发给房主 → 双方各自派生密钥 K
    │
    ├─→ HKDF(K, salt=房间码) → 32B AES-GCM 密钥 + 32B HMAC 密钥
    │
    ├─→ 启动器房间层（7660）：save 分块 AES-GCM 加密
    └─→ 游戏网络层（7655）：帧 payload AES-GCM 加密（替代现有明文 pickle）
```

### 关键决策

| 决策 | 选择 | 理由 |
|:-----|:-----|:-----|
| PAKE 协议 | SPAKE2（RFC 9382）| 有 Python 实现（`spake2` 包），比手写 PAKE2 安全 |
| Python 兼容 | 启动器 3.11 + mod 3.7 | `spake2` 纯 Python，3.7 可用（需验证） |
| 曲线 | Ed25519 / P-256 | SPAKE2 库默认曲线，性能足够 |
| 加密 | AES-GCM（pyca/cryptography）| 认证加密一体，Python 3.7 可用 |
| 向后兼容 | 协议版本升级 + 握手失败提示 | v9.18 → v9.19 需双端同版本 |

### 实施步骤（若做）

1. **验证 `spake2` 库**：Python 3.7 兼容性 + 双端握手测试（本地两进程）
2. **room_protocol.py 加 PAKE 握手**：join 消息扩展 P/Q 点交换
3. **密钥派生**：HKDF(房间码 + PAKE 输出) → AES-GCM/HMAC 双密钥
4. **network.py 加密帧**：payload 加密替代明文 pickle
5. **测试**：v919 套件（握手/加密/错误口令拒绝/嗅探不可读）
6. **双端同步升级**：协议版本不兼容自动提示

## 三、成本收益评估

### 收益
1. **防嗅探**：LAN 抓包看不到位置/聊天/存档内容（当前明文！）
2. **防中间人**：没有房间码无法协商密钥
3. **防存档窃取**：存档同步加密传输

### 成本
1. 引入 2 个依赖（spake2 + cryptography）——**mod 的 Python 3.7 兼容性需验证**
2. 协议 breaking change（v9.19）——双端必须同版本
3. 手写 PAKE 有 CVE 风险——用成熟库（spake2）而非手写

### 威胁模型判断

| 场景 | 风险 | PAKE 必要性 |
|:-----|:-----|:-----------|
| 家里 LAN（自己 + 朋友）| 低——同路由器的人基本可信 | 🟡 可选 |
| 咖啡厅/公共 WiFi LAN | 中——同网陌生人可抓包 | 🟢 有价值 |
| 公网（UPnP 穿透后）| 高——暴露公网可被扫描 | 🔴 强烈建议 |

**结论**：SimSync 定位是"自己和朋友家用"——当前威胁模型低，HMAC 防篡改已够；但**升级成本可控**（一次握手 + 加密），且未来若跨公网联机则必需。**建议做**（作为 v9.19 增强），但优先级低于真机验证。

## 四、参考

- croc: https://github.com/schollz/croc（PAKE 房间码→密钥，39.3k★）
- schollz/pake: https://github.com/schollz/pake（PAKE2 实现，MIT）
- SPAKE2 Python: https://pypi.org/project/spake2/（RFC 9382）
- CVE-2021-31603: croc 明文恢复漏洞（PAKE 实现细节教训）

---

*研究完成：2026-08-05 · 状态: proposed（建议 v9.19 实施，优先级低于真机验证）*
