---
tags: [reference, context-management, compaction, cost]
created: 2026-07-31
source: syrizelink/OpenFic (Apache-2.0)
---

# 生产级上下文压缩参数参考（OpenFic 吸收）

> 来源：OpenFic v0.8.1 后端 `agent_runtime/context/compaction/` 实现
> 价值：把"上下文管理"从经验规则升级为可量化参数

## 核心参数（OpenFic 实测生产值）

| 参数 | 值 | 含义 |
|------|-----|------|
| AUTO_TRIGGER_RATIO | 0.8 | 上下文使用率达 80% 自动触发压缩 |
| TAIL_TOKEN_BUDGET | 20,000 | 压缩后保留尾部预算 20K tokens |
| TAIL_WINDOW_RATIO | 0.5 | 尾部窗口 = 总窗口的 50% |
| MIN_COMPACTABLE_TOKENS | 2,000 | 少于 2K tokens 不压缩（避免无意义压缩） |

## 设计要点（值得借鉴）

1. **触发机制**：比例触发（0.8）而非主观感觉 → 与 ECC headroom_compress"机械闸门"一致
2. **压缩保留策略**：保尾部 20K + 50% 窗口 → 最近对话优先
3. **最小压缩门槛**：2K 以下不压缩 → 避免小会话频繁压缩的开销
4. **事件驱动**：`agent:compaction_start` 事件 + usage_sink → 压缩可观测、可审计
5. **持久化**：compaction_repo 记录每次压缩 → 历史可回溯（对比我们的规则 #13 因果验证）

## 对我们体系的映射

| OpenFic 实现 | 我们的对应 | 差距 |
|-------------|-----------|------|
| AUTO_TRIGGER_RATIO=0.8 | 规则 #15 跨天拆会话（时间触发） | 🟡 我们无比例触发 |
| TAIL_TOKEN_BUDGET=20K | 规则 #21 干湿分离（内容隔离） | 🟡 无量化预算 |
| MIN_COMPACTABLE=2K | 无 | 🟡 |
| compaction 持久化 | 规则 #13 记忆因果验证 | 🟢 一致 |

## 可落地建议

- [ ] 会话 >80% 上下文占用时 → 主动触发压缩/归档（比例触发）
- [ ] 归档保留尾部 20K tokens（最近对话优先）
- [ ] 小会话（<2K tokens）不做压缩开销
- [ ] 压缩动作记录到日志（可审计）

---
*2026-07-31 · OpenFic 上下文压缩模块吸收*
