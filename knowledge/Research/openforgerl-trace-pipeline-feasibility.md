---
tags: [research, openforgerl, trajectory, rl-training, feasibility]
created: 2026-07-31
status: complete-p1-p2
---

# 自训数据管线可行性备忘 — OpenForgeRL 轨迹记录层

> 2026-07-31 · 基于 arXiv 2607.21557v2 (OpenForgeRL) 的落地调研

## 结论速览

| 维度 | 结果 |
|------|------|
| **Hermes 是否需要额外 proxy？** | ❌ **不需要** — state.db 已原生记录全部轨迹 |
| **数据量是否达标？** | ✅ 7 天 206 会话 / 77k 消息（论文门槛: 几百任务） |
| **缺少什么？** | ① 轨迹标注（成功/失败判定）② RL 训练环境（veRL + K8s） |
| **当前阶段** | P0 完成（导出器可用）；P1/P2 视需求推进 |

## 一、关键发现：Hermes 已有原生轨迹层

OpenForgeRL 的核心是在 harness 与模型之间插 proxy 记录轨迹。**Hermes 的 `state.db` 已内置等价能力**：

| 数据 | 位置 | 内容 |
|------|------|------|
| 会话用量 | `session_model_usage` (225 行) | 每会话每模型: input/output/cache/reasoning tokens + 成本 |
| 完整消息 | `messages` (14,397 行) | 角色、内容、工具调用、推理链、时间戳 |
| 检索索引 | `messages_fts` | 全文搜索支持 |

**意义**：无需 OpenForgeRL 式 proxy —— 只需把 state.db 转成训练格式，即"轨迹记录层"已在 0 成本下运行。

## 二、落地产物

### `scripts/export_traces.py` — 轨迹导出器

```bash
uv run python scripts/export_traces.py --days 7
uv run python scripts/export_traces.py --model deepseek-v4-flash --days 30 --out traces/
```

输出 JSONL，每条含：
```json
{
  "session_id": "...",
  "model": "deepseek-v4-flash",
  "conversation": [{"role": "user", "content": "..."},
                   {"role": "assistant", "content": "...", "tool_calls": [...]},
                   {"role": "tool", "content": "...", "tool": "read_file"}],
  "token_count": 12345
}
```

**首次实测 (7 天)**：206 会话 → 205 轨迹 / 77,263 消息 / 81.7 MB
- 输入 tokens: 37.5M
- 输出 tokens: 3.3M

## 三、OpenForgeRL 可行性评估

### 已满足
- ✅ 数据采集层（export_traces.py）
- ✅ 数据量门槛（论文: 几百到几千任务；当前 7 天 206，月累积 800+）
- ✅ 多种模型轨迹（deepseek-v4-flash/pro、doubao、kimi-k3 等 9 种）

### 待建设状态（2026-08-05 更新）
| 项 | 说明 | 优先级 | 状态 |
|----|------|:------:|:----:|
| **轨迹标注** |  已落地——结构化判定（success/error 字段）优先于关键词 | 🔴 高 | ✅ 完成 |
| **数据清洗** | 同脚本——超长/过多消息/过短过滤；阈值 MAX_TOKENS=200k, MAX_MSGS=2000 | 🟡 中 | ✅ 完成 |
| **RL 训练环境** | veRL/OpenRLHF + GPU 训练（成本考量） | 🟢 低 | ⏳ 待定 |
| **K8s rollout** | 规模化需容器编排（当前单机足够） | 🟢 低 | ⏳ 待定 |

### 标注实测（2026-08-05，7 天 173 轨迹）
- 清洗后 144 条（丢弃 29：长期桌面会话 13100 消息 + 300k+ tokens 超长）
- 分布：success 62% / fail 3% / uncertain 35%
- 关键坑：**关键词误判**——web_search 摘要里的 "Error"、search_files 的 `{"total_count": 0}` 不是失败；改为 JSON 结构化判定（`success:false` / `error` 字段）后 fail 49%→3%
- uncertain 35% 保守保留（OSReward 防宽松偏见原则：不确定不硬标）

### 替代路径（更务实）
```
当前: 用轨迹数据 → 未来训练自有模型 (重投入)
可选: 用轨迹数据 → 改进 prompt/skill 设计 (轻投入, 即时收益)
     └── 分析高频失败会话 → 提炼为 Skill/规则 (与七大自举系统同向)
```

## 四、关联
- 论文: [OpenForgeRL 2607.21557v2](https://arxiv.org/abs/2607.21557v2)
- 知识卡: [[knowledge/cards/2026-07-31-openforgerl|OpenForgeRL 卡片]]
- 规则: `hermes-workflow-preferences` #17 (评估器可靠性，用于轨迹标注防偏见)
- 工具: `scripts/export_traces.py`

---

*备忘完成：2026-07-31 · 状态: P0 落地，P1+ 按需推进*

---
> 关联: [[2026-07-31-openforgerl|知识卡片]] | [[HOME|🏠 首页]]

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]
