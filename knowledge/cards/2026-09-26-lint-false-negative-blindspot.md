---
aliases:
  - 2026-09-26-card-lint-false-negative-blindspot
tags: [knowledge-card, methodology, tooling, knowledge-lint, frontmatter]
created: 2026-09-26
source: "[[knowledge/cards/2026-09-05-false-positive-tax|假阳性税]]（姊妹篇）+ 本机知识库实测"
status: fresh
---

# 🃏 知识卡片 · 假阴性税：检测器报 0 不代表没问题，判据写错会静默放行 80 个坏文件

> **来源**：2026-09-26 知识库每日维护实战（second-brain vault 全库扫描）· ✅ 本机实证 + 修复前后对照
> **一句话**：**「报 0」比「报错」更危险**——假阳性会让你学会忽略报警，假阴性让你以为已经修完了；同一个检测器可以同时犯这两种错。

---

## 🔍 现象：检测器说「0」，实际有 80 个坏文件

`knowledge-lint.py` 的「粘连 frontmatter 闭合符」检查（如 `status: fresh---` 缺独立 `---` 行）报告 **Glued = 0**。独立复检发现 **80 个文件**真的粘连：

| 目录 | 数量 | 粘连键 |
|:---|:---:|:---|
| `knowledge/Research/` | 49 | `source`(39) / `domain`(14) |
| `knowledge/cards/` | 27 | `status`(23) |
| `knowledge/Archive/` | 3 | `updated` / `tags` |
| `knowledge/Security/` | 1 | `updated` |

## 🐛 根因：判据的**取值范围**写错了

```python
# 旧实现（错）
closed = any(l.strip() == "---" for l in fm_lines[1:20])
if not closed:
    glued_fm.append(f)
```

它问的是「**前 20 行里有没有任意一个独立 `---`**」。但这些笔记的正文第 10 行左右本来就有一条水平分隔线 `---`：

```markdown
---
status: fresh---        ← 真正的粘连点（第 7 行）

# 标题
---
正文水平分隔线            ← 被判据当成了"frontmatter 已正常闭合"
```

→ **正文的装饰性横线冒充了 frontmatter 闭合符**，`closed=True`，检查通过。

```python
# 新实现（对）：frontmatter 区 = 第 2 行 → 首个独立 --- 为止
for i, l in enumerate(fm_lines[1:200], start=1):
    s = l.strip()
    if s == "---":
        closed, close_idx = True, i
        break
    if s.endswith("---"):     # 区间内任何 --- 结尾行 = 粘连
        glued = True
        break
```

**修复后：Glued 0 → 80 → 修复 → 0（真 0）。**

## 💡 可迁移的三条教训

1. **检测器的判据必须锚定「结构边界」，不能扫「窗口内有没有」**
   - 「前 N 行存在 X」这类判据天然可被同形 token 欺骗（水平线 / 代码块 / 引用块里的同款字符）。
   - 正确姿势：先确定结构的**起点与终点**（首个独立分隔符即终点），只在区间内判定。

2. **报 0 的检查项要做「负例测试」（negative test）**
   - 每个检测项都应有一份**故意造坏的样本**，确认它真的会报警。本次就是用 2 个临时坏文件
     （粘连 + 非法 YAML）验证新判据会 fire，确认后再删除样本。
   - 没有负例测试的「0」，只是「没测出来」，不是「没有」。

3. **假阳性税 vs 假阴性税是一对，别只防一边**
   - 姊妹篇《假阳性税》讲：误报太多 → 团队学会忽略报警 → 召回被清零。
   - 本篇讲：漏报 → 以为修完了 → **问题在无人看的地方持续累积**。
   - 两者同源：**都是评估口径问题，不是数据问题**。评估工具先看 TP/FP/**FN** 三个原始计数。

## ✅ 本次落地的工程动作

- `knowledge-lint.py` 修复粘连判据（改为结构边界锚定）
- 新增 **YAML 可解析性**检查：`related: [[A]], [[B]]` 这类未加引号的 wikilink 列表在 YAML 中非法
  （`[` 开启 flow sequence → 解析崩溃），旧版只看「有没有 frontmatter」不验证「能不能解析」→ 漏报 1 个
  （`knowledge/Dev/Programming.md`）。全部属性（MOC 分组 / Dataview 查询 / 代谢分类）都依赖
  frontmatter 可解析，故必须进门禁。
- 新增检查项同步进 `post_change_lint.py` 的 BLOCKING 列表（ERROR 级 → 阻断提交）
- 80 个粘连文件 + 1 个非法 YAML 全量修复（每文件 +1/−1 行，零行尾扰动）

## 🔗 相关

- [[knowledge/cards/2026-09-05-false-positive-tax|🃏 假阳性税：工具误报比不修更危险]]（姊妹篇 · 建议对读）
- [[knowledge/META/MOC-META|🗂️ META MOC]]
- [[MOC-cards|🃏 知识卡片 MOC]] · [[Home|🏠 Home]]
