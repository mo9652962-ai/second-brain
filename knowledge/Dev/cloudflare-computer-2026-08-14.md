---
tags: [Agent-Infra, Cloudflare, Sandbox, VFS, Computer-Agent, RPC]
aliases: [cloudflare-computer, computer(cloudflare)]
date: 2026-08-14
source: https://github.com/cloudflare/computer
status: watch
---

# Cloudflare computer — 给 agent 一台电脑

> **简介**：Cloudflare 官方开源，让 agent 拥有一台沙箱电脑（网络可访问、带虚拟文件系统）。本周 8,052⭐ **+3,599/周**（TypeScript/JS，MIT，727 commits，活跃，Cloudflare 大厂背书可信）。与 denoland/celld（self-hosted distributed Durable Objects）有直接协作示例。

## 架构
```
Durable Object(sandbox 主控)             computerd(daemon, 沙箱容器内)
    Computer 包 ──────capnweb RPC─────▶  FUSE 挂载
    Workspace(VFS)                        + HTTP/WebSocket RPC 服务器
    (文件系统能力)                         (运行在 sandbox container)
```
- **Workspace VFS**：agent 的文件系统能力，通过虚拟文件系统暴露；有 `@platformatic/vfs` Node provider
- **capnweb RPC**：wire 类型 + 服务器/客户端助手，在 Durable Object 与 computerd 间共享（`@cloudflare/computer-rpc`）
- **Agent idempotency**：支持 short git IDs（isomorphic-git, revParse 短对象 ID 前缀解析）
- **MCP 可部署**：examples/mcp 提供可部署的 Computer MCP
- 与 **celld** 协作：`CelldAgent` Durable Object + `withWorkspace` 共享 SQLite 存储，本地 harness 起 S3 兼容存储

## 设计亮点
- **文件系统工具与执行工具分离**：callable `exec` 后端跑完整 JS 模块（结构化输入/输出），文件系统工作走专用 Workspace 工具——权限边界清晰，防止执行工具越权访问宿主 FS。
- **VFS 元数据性能 > 真实磁盘**（docs/19_performance.md）：FUSE 挂载在元数据密集型操作上胜过真实盘，大顺序 IO 略逊——证明「虚拟文件系统」不只是玩具。

## 💎 可借鉴点（对 browser-automation / computer-use 最值）
1. **沙箱 VFS 的权限分离**：sora 的 browser-automation / computer-use / CDP(9222) 是「操纵真实桌面/浏览器」。Cloudflare 把 agent 的电脑做成**沙箱 + 虚拟文件系统 + 明确工具边界**——对「给 agent 更自主权限」是很稳的隔离模型（可迁移到 headless 自动化环境的封装）。
2. **exec 与 FS 工具解耦**：执行能力（跑代码）与文件访问能力（读写 FS）分开授予，是 agent 工具安全的最小但关键设计——sora 的 terminal/文件工具授权可按此分层配置。
3. **引 celld 对齐 Durable Objects**：同周 denoland/celld（+1,783）也在 trending，二者联动说明「agent 云基础设施 + 分布式持久化」正成为 Cloudflare/Deno 两派的共同赛道。

## 综合评估
| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★☆（VFS + 沙箱 + capnweb RPC 工程扎实）|
| 与 sora 工作流关联 | ★★★☆（browser-automation/computer-use 云端版，参考隔离模型）|
| 值得安装 | 🔵 关注——sora 本地自动化为主，暂不需要云端电脑；借鉴权限边界设计 |
| 趋势判断 | 「agent 拥有可信电脑」成为头部大厂基建方向（Cloudflare/Deno 竞速）|

> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]] · 平行参考：`browser-automation` · `celld`(trending 同周)