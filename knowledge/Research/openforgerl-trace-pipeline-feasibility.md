---
tags: [research, openforgerl, trajectory, rl-training, feasibility]
created: 2026-07-31
status: complete
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

### 待建设（P1+）
| 项 | 说明 | 优先级 |
|----|------|:------:|
| **轨迹标注** | 给每条轨迹标成功/失败（可用 OSReward 思路，但先防宽松偏见） | 🔴 高 |
| **数据清洗** | 过滤超长/截断/异常会话，统一格式 | 🟡 中 |
| **RL 训练环境** | veRL/OpenRLHF + GPU 训练（成本考量） | 🟢 低 |
| **K8s rollout** | 规模化需容器编排（当前单机足够） | 🟢 低 |

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
