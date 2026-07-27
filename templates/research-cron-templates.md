# 科研 cron 模板集

> 灵感来自 攻玉"自动化模板" · 适配 Hermes cron 系统

---

## 📋 模板 1：组会报告（每周日 20:00）

```yaml
schedule: "0 20 * * 0"    # 每周日 20:00
prompt: >
  请完成以下组会报告准备工作：
  1. 文献速递：检索我研究方向本周最新论文，总结3-5篇亮点
  2. 项目进展：回顾本周 vault 中 knowledge/ 和 memory/ 的新增内容，总结项目进度
  3. 下周计划：基于当前进展，给出下周3个优先级最高的任务
skills:
  - light-literature-search
  - light-research-plan
```

## 📋 模板 2：文献周报（每周一 07:00）

```yaml
schedule: "0 7 * * 1"     # 每周一 07:00
prompt: >
  检索上周最新学术论文并生成周报：
  1. 使用文献库检索与我研究方向相关的最新论文
  2. 每篇给出：标题、作者、核心发现、创新点
  3. 推荐2-3篇值得精读的论文并说明理由
skills:
  - light-literature-search
  - arxiv
```

## 📋 模板 3：项目进度追踪（每日 21:00）

```yaml
schedule: "0 21 * * *"    # 每天 21:00
prompt: >
  回顾今日 vault 更新，生成项目进度简报：
  1. 今日新增/修改的知识笔记
  2. 技术决策记录（ADR）
  3. 遇到的障碍和解决方案
  4. 明日优先级任务
```

## 📋 模板 4：闲鱼服务提醒（自定义）

```yaml
schedule: "0 9 * * 1-5"   # 工作日 09:00
prompt: >
  基于当前 vault 中的服务记录，提醒今日待办：
  1. 检查是否有未完成的闲鱼订单
  2. 检查技能更新状态
  3. 生成今日工作计划
skills:
  - vault-suggestion-executor
```

---

## 使用方法

```bash
# 创建组会报告 cron
cronjob create \
  --name "组会报告" \
  --schedule "0 20 * * 0" \
  --prompt "请完成组会报告准备工作：..." \
  --skills light-literature-search,light-research-plan

# 创建文献周报 cron
cronjob create \
  --name "文献周报" \
  --schedule "0 7 * * 1" \
  --prompt "检索上周最新论文..." \
  --skills light-literature-search,arxiv
```
