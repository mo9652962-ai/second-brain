---
type: current-state
verified_at: 2026-09-20
status: active
tags: [meta, paths, fact-source]
---

# 本地知识库入口

> **事实源**：所有文档引用路径、目录、数量时，一律指向本文，不要各自写死。
> 数量会随文件同步变化 —— 以本文实测值或审计脚本输出为准。

## Obsidian Vault

```
Vault:   %USERPROFILE%\.openclaw\workspace
知识区:  %USERPROFILE%\.openclaw\workspace\knowledge
```

- 669 个 `.md`（知识主体）
- 含 MOC 锚点体系：每个知识域一个 `MOC-<域>.md`，总入口 [[knowledge-map]]
- 路由层：[[index]]（先读 index 定位域 → 进 MOC → read_file 具体页）

## Hermes

```
工作区:  %USERPROFILE%\.openclaw\workspace\.hermes
技能区:  %USERPROFILE%\.openclaw\workspace\skills
```

| 路径 | 内容 | 数量 |
|:---|:---|:---|
| `.hermes/` | Hermes 工作区文档（AGENTS.md / HEARTBEAT.md 等） | 4 个 `.md` |
| `skills/` | OpenClaw 遗产技能区 | 131 个 `.md`，其中 `SKILL.md` **31** |

## 技能目录 —— 两个路径，别搞混

**这是最容易出错的地方**，必须明确区分：

| 路径 | 角色 | `SKILL.md` 数 | 状态 |
|:---|:---|:---|:---|
| `%USERPROFILE%\AppData\Local\hermes\skills` | ✅ **Hermes 实际加载入口** | **503** | 活跃（157MB） |
| `%USERPROFILE%\.openclaw\workspace\skills` | OpenClaw 遗产区 | 31 | 部分重叠 |

**判定依据**：
- 技能快照 `.skills_prompt_snapshot.json` → `skills: list len=499`，与 AppData 的 503 吻合
- 会话中技能加载路径实测为 `AppData\Local\hermes\skills\<category>\<name>`
- `workspace/skills` 仅有 4 个独有条目（`ai`/`dev`/`general`/`platform`），其余为 AppData 子集

**结论：查找技能一律以 `AppData\Local\hermes\skills` 为准。**

> ⚠️ 历史文档中的「AppData 技能区为空」是**过期结论**，已作废。
> ⚠️ 历史文档中的「451 skills」「1550 skills」「488+ knowledge」「490+ knowledge」均为**某个时点的快照**，不再作为当前事实。

## 历史记忆（只读）

```
%USERPROFILE%\.openclaw\workspace\memory
```

- 379 个 `.md`：`memory/2026/08/*`、`memory/2026/09/*`、`memory/dreaming/*`
- **语义**：记录「当时发生了什么」，不是当前配置
- **规则**：原文保留，不删除、不改写、不伪装成当前状态
- **引用时**：必须标注 `> 历史状态：截至 YYYY-MM-DD`

## 相关

- [[knowledge/META/current-environment]] — 环境与 Docker 事实源
- [[knowledge/META/current-model-status]] — 模型与 API 事实源
- [[index]] — 知识库路由层
