---
aliases:
  - 2026-08-05-card-protocol-version-negotiation
tags:
  - knowledge-card
  - protocol
  - network
  - s4mp
  - engineering
created: 2026-08-05
source: "[[knowledge/Research/s4mp-protocol-network-100round-2026-08-05]]"
---

# 🃏 知识卡片 · 协议版本协商：让"版本无关可读"排在最前面，旧客户端才不秒断

> **来源**：S4MP 百轮协议研究 §14（MCP spec + Martin Evans 游戏协议经验）· 2026-08-05 · ✅ 真机 bug 触发 + web 交叉验证
> **一句话**：协议帧升级后，旧客户端连新服务器会因帧格式错位直接秒断（连版本号都读不到）；行业解法是——握手最前面放"任何版本都能读"的帧头（magic number + 版本号），不兼容时发结构化错误提示"请更新到 vX"，而不是裸断连。

---

## 核心洞察 / 影响

| 维度 | 内容 |
|------|------|
| 问题根源 | 帧格式升级是 breaking change：v9.16 帧头 12→44 字节，旧客户端按旧偏移解析新帧 → 错位 → 反序列化失败 → 1 秒内主动断开 |
| 行业方案 | MCP `server/discover`：客户端先问服务器支持的版本列表再协商；不兼容返回结构化错误（`UnsupportedProtocolVersionError`）而非静默断连 |
| 关键细节 | magic number 固定偏移、任何版本都能读 → 收端先读 magic 判断协议时代 → 能兼容则降级解析，不能则发"请更新"提示 |
| 配套实践 | 兼容窗口期：先同时支持新旧版本，一段时间后再移除旧（jser.dev / TLS 版本对齐） |

## 关键数据 / 对 sora 的影响

1. ✅ **S4MP 已有 PROTO_VERSION 协商**（hello 带版本，不匹配发 version_mismatch）——但盲点在"握手之前"：旧客户端 hello 帧本身解析不了，版本字段都读不到 → 候选改进：帧头加 magic + 版本
2. ⚠️ **分发规范**：帧升级两端必须同版本；zip 内 mod/说明/bat 四件套版本号要一致；日志出现 `'utf-8' codec can't decode` = 对端还是 JSON 协议时代（v7.2 前），秒级诊断
3. 💡 **通用迁移**：任何协议（游戏/API/IoT）升级前先问"老版本收到新帧会怎样"，而不是只想着新功能——向后兼容要设计进帧格式，不是事后补

## 行动项

- [x] v9.16 跨网安全闭环：HMAC-SHA256 消息签名 + HKDF 握手密钥交换（先验签再反序列化），15 套件 237 断言全过
- [ ] P1：S4MP 帧头加 magic number + 协议版本（固定偏移），收端先读 magic → 结构化 version_mismatch（含"请更新到 vX"）而非裸断连 → ⏳ 项目 backlog（需改协议层+双端同版本发布，等开发窗口）
- [ ] P1：跨网真机验证 UPnP/STUN（代码就绪但从未公网实测——当前最大短板）→ ⏳ 项目 backlog（需 sora 两台真机+公网环境实测）

## 为什么重要

- 由真机 bug「对端加入秒断」触发的深度研究——**虚拟测试全绿 ≠ 真机没问题，真机日志是最终裁判**（当天还挖出模块内 `network.` 前缀 NameError 等 3 个测试没抓到的 bug）
- 结论可迁移：MCP（模型上下文协议）与游戏网络协议的版本协商最佳实践殊途同归，适用于任何需要长期演进的通信协议
- 直接强化 S4MP 项目与 sims4-mod-development 技能

---

*卡片来源：当天知识库精选 · knowledge/Research/s4mp-protocol-network-100round-2026-08-05（🥇 daily-review Top1 + 可迁移性最强 + 有明确后续行动项）*
