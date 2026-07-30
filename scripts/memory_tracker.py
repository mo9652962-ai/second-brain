"""
轻量记忆贡献度追踪 — MemLens P0 实现
记录每条记忆的使用次数、任务成功率和贡献度评分
"""
import json, os
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

TRACKER_FILE = Path.home() / ".openclaw/workspace/.hermes/memory-tracker.json"

def ensure_tracker():
    """确保追踪文件存在"""
    TRACKER_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not TRACKER_FILE.exists():
        TRACKER_FILE.write_text(json.dumps({
            "version": 1,
            "entries": {},
            "created": datetime.now().isoformat()
        }, ensure_ascii=False, indent=2))


def record_hit(memory_key: str, task_type: str = "", success: bool = True):
    """
    记录一次记忆命中

    Args:
        memory_key: 记忆的唯一标识（如 memory 条目内容的前 40 字符）
        task_type: 触发的任务类型（如 "cron-fix", "answer"）
        success: 本次任务是否成功
    """
    ensure_tracker()
    data = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    entries = data["entries"]

    if memory_key not in entries:
        entries[memory_key] = {
            "first_hit": datetime.now().isoformat(),
            "hit_count": 0,
            "success_count": 0,
            "fail_count": 0,
            "task_types": [],
            "score": 0.0
        }

    e = entries[memory_key]
    e["hit_count"] += 1
    if success:
        e["success_count"] += 1
    else:
        e["fail_count"] += 1
    if task_type and task_type not in e["task_types"]:
        e["task_types"].append(task_type)

    # 简化贡献度评分：成功率 × 命中权重
    total = e["success_count"] + e["fail_count"]
    success_rate = e["success_count"] / max(total, 1)
    frequency_bonus = min(1.0, e["hit_count"] / 10)  # 10次及以上算满分
    e["score"] = round(success_rate * 0.6 + frequency_bonus * 0.4, 3)

    data["updated"] = datetime.now().isoformat()
    TRACKER_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def get_low_value_memories(threshold: float = 0.3, min_hits: int = 3) -> list:
    """
    获取低价值记忆列表（候选清理）

    Args:
        threshold: 评分阈值，低于此值视为低价值
        min_hits: 最少命中次数才纳入评估

    Returns:
        [(memory_key, score, hit_count), ...]
    """
    ensure_tracker()
    data = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    low_value = []
    for key, entry in data["entries"].items():
        if entry["hit_count"] >= min_hits and entry["score"] < threshold:
            low_value.append((key, entry["score"], entry["hit_count"]))
    return sorted(low_value, key=lambda x: x[1])


def get_report() -> str:
    """生成记忆贡献度报告"""
    ensure_tracker()
    data = json.loads(TRACKER_FILE.read_text(encoding="utf-8"))
    entries = data["entries"]

    if not entries:
        return "暂无记忆追踪记录"

    lines = ["## 📊 记忆贡献度追踪报告\n"]
    lines.append(f"总追踪条目: {len(entries)}")

    # 按价值排序
    sorted_entries = sorted(entries.items(), key=lambda x: x[1]["score"], reverse=True)

    lines.append("\n### 🔥 高价值 (>0.7)")
    for k, v in sorted_entries:
        if v["score"] >= 0.7:
            lines.append(f"- {k[:50]}...  score={v['score']}  hits={v['hit_count']}")

    lines.append("\n### 🟡 中等 (0.3-0.7)")
    for k, v in sorted_entries:
        if 0.3 <= v["score"] < 0.7:
            lines.append(f"- {k[:50]}...  score={v['score']}  hits={v['hit_count']}")

    lines.append("\n### ⚪ 低价值 (<0.3)")
    for k, v in sorted_entries:
        if v["score"] < 0.3:
            lines.append(f"- {k[:50]}...  score={v['score']}  hits={v['hit_count']}")

    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "report":
        print(get_report())
    else:
        print(f"用法: uv run python {__file__} report")
        print("示例调用:")
        print('  record_hit("cron-2026-07-30-fix", "cron-fix", True)')
