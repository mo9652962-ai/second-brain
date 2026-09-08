# 待办：skill-link-gate 剩余 98 条真断链

> 2026-09-08 记录，待后续处理

## 背景
- skill-link-gate（cron 周一 08:15，脚本 `~/AppData/Local/hermes/scripts/skill_link_check.py`）检测技能库断链
- 2026-09-08 保守修复：49 个 references/templates 占位 + 过滤 checkpoint= 误报 → 断链从 166 → 98
- 检测器已备份 `.bak-20260908`

## 剩余 98 条分类
| 类型 | 数量 | 处理建议 |
|:---|:---|:---|
| `..` 跨 skill 引用 | 31 | light-* 系列引用 light-orchestrator（未安装）→ 需确认是否安装或删引用 |
| scripts/ 缺失 | 16 | 引用的脚本从未创建 → 需确认/删引用 |
| assets/ 缺失 | 14 | 同上 |
| templates/ JSON | 11 | JSON 模板需真实内容 → 生成示例 |
| examples/ | 5 | 示例文件缺失 → 生成示例 |
| references.md / strategy.md | 6 | 顶层文档缺失 |
| references/ 目录 | 2 | 目录引用（references/research/）|

## 处理原则（保守）
- 不盲创建 scripts/assets 占位（agent 读到空脚本比读不到更糟）
- 不批量删 SKILL.md 引用（误删风险）
- 优先：JSON 模板生成示例（价值高）、确认 light-orchestrator 是否该装
- 可回滚：检测器有备份、占位文件可删

## 复现
```bash
python ~/AppData/Local/hermes/scripts/skill_link_check.py
```
