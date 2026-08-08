---
tags: [周报, github trending, 2026-08-02]
date: 2026-08-02
---

# 🗞️ GitHub 今日热门研究周报 — 2026-08-02

## 项目详情

| # | 项目 | ★ | 核心价值 | 入库笔记 |
|:-:|------|:--:|---------|---------|
| 1 | MoonshotAI/Kimi-K3 | 7,834 | 开源前沿模型 + 技术报告 | [[github-trending-2026-08-02-study]] |
| 2 | yc-software/qm | 5,325 | 多人 Agent 框架（scope 隔离/shared skills） | 同上 |
| 3 | sqliteai/waste | 719 | NVMe 流式权重推理 K3 | 同上 |
| 4 | wassgha/rescript | 507 | 转录式浏览器视频编辑器 | 同上 |

## 可借鉴点归纳

**技术层面**
- K3 开源 4 天 7.5k⭐ = 前沿模型开源是流量密码；技术报告先行是发布标准姿势
- qm 的 deployment directory 模式：核心通用 + 公司特定配置分离
- waste 的流式权重加载：NVMe→显存按需流式，突破内存限制

**方法论层面**
- qm 的 scope 隔离（每人/每房间独立 memory/files/权限）+ shared skills 按 grant 分享 = 与我们的 Hermes/vault 体系同构
- qm 的 Security 三档（Strict/Auto/Dangerous）= 与 Hermes approval 机制对应
- rescript 转录式编辑 = 视频剪辑变"删文字"，内容创作者提效范式

**可实操行动**
- P1: 借鉴 qm scope/skill/安全概念 → 写方法论笔记（Hermes 多人协作扩展）
- P2: 试装 rescript → 评估 B站剪辑提效
- P3: 收藏 waste/deltafin → 硬件升级后再评估

## 文件操作清单
- ✅ 新建 `knowledge/Research/github-trending-2026-08-02-study.md`
- ✅ 更新 `knowledge/Research/MOC-Research.md`（+1 索引）
- 📄 本报告 `memory/2026/08/github-trending-2026-08-02.md`

---
*2026-08-02 · github-trending-digest 技能流程 Phase 6*
