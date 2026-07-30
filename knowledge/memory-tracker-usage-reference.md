# 记忆贡献度追踪系统 — 使用参考

## 架构

```
[工作流] → record_hit() → [memory-tracker.json] → memory_dashboard.py → [HTML仪表盘]
   (any script)        (持久化)                      (可视化前端)        (桌面查看)
```

## 记录记忆命中

在任何 Hermes 会话中，加载后可直接调用：

```python
from scripts.memory_tracker import record_hit

# 成功后记录
record_hit("cron-fix-6-tasks", "cron-fix", True)

# 失败也记录
record_hit("experiment-xyz", "experiment", False)

# 多次命中自动累计，贡献度评分基于成功率+频率
```

## 查看仪表盘

**方式 1：双击桌面快捷方式**
- `生成记忆仪表盘.bat` — 一键生成并打开
- 保存到桌面 `memory-dashboard.html`

**方式 2：命令行生成**
```bash
cd C:\Users\31954\.openclaw\workspace
uv run python scripts/memory_dashboard.py
```

**方式 3：Web 服务模式（实时刷新）**
```bash
uv run python scripts/memory_dashboard.py --serve 8080
# 浏览器访问 http://localhost:8080
```

## 仪表盘内容

| 区域 | 功能 |
|------|------|
| 统计卡片 | 总条目、高/中/低价值数量、平均贡献度 |
| 饼图 | 价值分布可视化 |
| 柱状图 | Top10 记忆贡献度排名 |
| 表格 | 所有记忆条目详情（评级/贡献度/命中数/成功率/任务类型） |

## 评分计算

```
贡献度 = 成功率 × 0.6 + 频率系数 × 0.4

成功率 = 成功次数 / (成功 + 失败)
频率系数 = min(1.0, 命中次数 / 10)

评级：
  ≥0.7 → 🔥 高价值（优先保留）
  0.3-0.7 → 🟡 中等
  <0.3 → ⚪ 低价值（候选清理）
```

## 数据文件

- `~\.openclaw\workspace\.hermes\memory-tracker.json`
- 自动创建，无需手动管理
- 使用 `get_report()` 获取文本版报告
- 使用 `get_low_value_memories(threshold=0.3, min_hits=3)` 获取候选清理条目

## 关联规则

- 规则 #11 轻量记忆价值量化（3因子评分模型）
- 规则 #13 记忆因果验证（State→Evidence→Recovery 三环）
