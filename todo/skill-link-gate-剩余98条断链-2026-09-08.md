# 待办：skill-link-gate 剩余断链

> 2026-09-08 记录，2026-09-13 suggestion-implementation 复查

## 2026-09-13 复查结论

- 复跑 `python AppData/Local/hermes/scripts/skill_link_check.py`：断链 **100 条**（9/8 的 98 → 100）
- ✅ 确认 **references/research/ 引用为检测器误报**：nuwa-skill / steve-jobs-perspective 的 `references/research/` 目录实际存在（检测器只按文件校验）→ 2 条可忽略
- ⏳ light-orchestrator 引用 9 条（run_checkpoint.py ×6 + reroute.py ×3）保持待 sora 确认：装 light-orchestrator 或删引用
- 占位符类（file.md/.md/path.md/assets/.../[^"']+ 正则）为模板残留/正则误报，低价值，不单独修
- JSON 模板示例生成（light-venue-matching 等 11 条 templates/）仍为最高价值项，留待专项会话处理

## 背景
- skill-link-gate（cron 周一 08:15，脚本 `~/AppData/Local/hermes/scripts/skill_link_check.py`）检测技能库断链
- 2026-09-08 保守修复：49 个 references/templates 占位 + 过滤 checkpoint= 误报 → 断链从 166 → 98
- 检测器已备份 `.bak-20260908`

## 剩余分类（9/8 口径，2026-09-13 复查微调）
| 类型 | 数量 | 处理建议 |
|:---|:---|:---|
| `..` 跨 skill 引用（light-orchestrator） | 31（含 9 条 light-orchestrator 脚本） | 需确认是否安装或删引用 |
| scripts/ 缺失 | 16 | 引用的脚本从未创建 → 需确认/删引用 |
| assets/ 缺失 | 14 | 同上 |
| templates/ JSON | 11 | JSON 模板需真实内容 → 生成示例（最高价值） |
| examples/ | 5 | 示例文件缺失 → 生成示例 |
| references.md / strategy.md | 6 | 顶层文档缺失 |
| references/ 目录（含误报） | 2（实际目录存在 → 检测器误报） | 修检测器按目录校验 |

## 处理原则（保守）
- 不盲创建 scripts/assets 占位（agent 读到空脚本比读不到更糟）
- 不批量删 SKILL.md 引用（误删风险）
- 优先：JSON 模板生成示例（价值高）、确认 light-orchestrator 是否该装
- 可回滚：检测器有备份、占位文件可删

## 复现
```bash
python ~/AppData/Local/hermes/scripts/skill_link_check.py
```
