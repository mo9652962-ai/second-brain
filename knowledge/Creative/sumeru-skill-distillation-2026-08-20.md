# sumeru 技能蒸馏（2026-08-20）

> 来源：xindoo/sumeru（129★，7 个 Claude Code Skill 模块——与抖音「AI 小说工厂 7 条产线」视频吻合）
> 行动：实证 clone + Windows 适配检查 + 方法论蒸馏进 Hermes 技能体系

## Windows 适配结论

- sumeru 全部脚本只有 1 个 Python 文件（chapter-word-counter.py，跨平台 ✅）
- 无 zsh/bash 硬依赖脚本（CLAUDE.md 提 zsh 只是环境声明）
- 可在 Windows + Claude Code/OpenCode 直接加载

## 7 模块对照（sumeru → Hermes）

| sumeru 模块 | 功能 | Hermes 落点 |
|:---|:---|:---|
| sumeru-topic | 选题策划（金手指/卖点/爽点/可行性）| novel-pipeline ① |
| sumeru-worldbuilder | 总控协调（创意→完整作品）| novel-pipeline ② |
| sumeru-outline | 大纲/人设/爽点排布/分章细纲 | novel-pipeline ③ |
| sumeru-write | 章节创作（单章/批量/续写/重写）| novel-pipeline ④ |
| sumeru-review | 8 维度审查+自动修复 | novel-pipeline ⑤ |
| sumeru-polish | 3 级润色/爽点强化 | novel-pipeline ⑥ |
| sumeru-finalize | 校验+多平台导出 | novel-pipeline ⑦ |

## 蒸馏出的核心方法论（写入 novel-pipeline 技能）

1. **细纲驱动**：先出分章细纲（chapter-outlines.json）再批量生成
2. **批量并行**：子 Agent 每批 ≤3 章（delegate_task 对应）
3. **自动备份**：修改前备份到 .novel/write/original/
4. **底线零遗漏**：致命问题必须解决（必要时改大纲重写章节）
5. **网文节奏**：开头钩子/中间冲突/结尾悬念；默认 4000-5000 字/章

## 组合工作流（sora 认可，2026-08-20）

**ainovel-cli 跑长篇 → Hermes novel-pipeline 审查润色**：

```
cd <小说目录> && ainovel-cli.exe   # 全自动跑初稿，产物 {cwd}/output/novel/
→ 初稿丢给 Hermes → 8 维度审查 → 改大纲重写严重问题 → humanizer-zh 去 AI → 平台导出
```

- ainovel-cli：每本小说绑定启动目录（换目录=换一本，cd 回去=断点恢复）
- 已配基元律动（tokenrhythm.studio/v1，17 模型，默认 deepseek-v4-flash）
- 技能：novel-pipeline 已含「组合工作流」章节

## 相关实测

- ainovel-cli v0.7.6（1739★，Go）Windows 二进制验证通过（v0.7.6，初始化向导正常）——全自动长篇引擎
- ai-novelist（92★）样例《洞悉天机三千年一不小心无敌了》正文质量实测：短段落+内心吐槽+章末钩子，有人味

## 文件

- 技能：creative/novel-pipeline（新）
- 关联：novel-worldbuilding + related_skills 补 novel-pipeline
- 临时克隆：已清理（ai-novel-run/）
