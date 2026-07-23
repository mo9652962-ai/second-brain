# HEARTBEAT.md - 心跳自检清单

## 静默规则 (Silent-by-Default)

**如果在 23:00-08:00 且无紧急事项** → 回复 `HEARTBEAT_OK`，不做任何事。

**如果距上次用户交互 > 2h 且无新内容** → 回复 `HEARTBEAT_OK`，仅当有值得汇报的内容时才主动联系。

80-95% 的心跳应该静默通过，只为真正重要的事打扰 sora。

## 轮换检查项

每次心跳从以下项目中选 2-3 项轮换执行：

### 日常
- [ ] 📧 邮件：检查是否有紧急未读邮件需要 sora 关注
- [ ] 📅 日历：未来 24-48h 是否有事件需要提醒
- [ ] 🌤️ 天气：sora 是否会出门？需要带伞/添衣？

### 维护
- [ ] 🧠 记忆维护：检查上周 daily notes，提炼值得保留的到 MEMORY.md
- [ ] 🗑️ Memory Pruning：清理超过 30 天的日常日志中的冗余内容
- [ ] 📊 自我审查：review .learnings/ 中的 pending 项，解决或晋升
- [ ] 🔍 健康检查：Gateway 状态、模型可用性、token 用量
- [ ] 🧹 Session Cleanup：`openclaw sessions cleanup --enforce --fix-missing`（每月一次）
- [ ] 🔒 安全审计：确认 commands.ownerAllowFrom 配置，检查 skills 是否有 SkillSpector 标记

### 主动
- [ ] 💡 反思：有什么可以做得更好？有什么模式可以自动化？
- [ ] 🎁 惊喜：可以为 sora 主动做点什么？
- [ ] 📈 技能审计：安装的 skills 是否都必要？是否有更好的替代？

## 紧急联系条件

以下情况**必须**主动联系 sora（即使在夜间）：
- 发现了 sora 关心的领域重大新闻/事件
- Gateway 或关键服务故障
- 预定的事件即将发生（< 2h）
- sora 有未读的重要消息超过 8h

## 状态追踪

使用 `memory/heartbeat-state.json` 追踪上次各检查的时间，避免重复。

---

_基于 Hermes Agent + Obsidian 最佳实践 | 最后更新: 2026-07-23_
