---
tags: [project, pipeline, paper, freelancing]
created: 2026-07-30
status: draft
---

# 论文 Pipeline 数据契约

> 精简版（原始 JSON 输入契约）见 [[paper-pipeline-data-contract]]

## 一、接稿阶段

### 输入数据契约
```yaml
order:
  customer_name: string       # 客户昵称
  paper_type: enum            # 毕业论文 | 期刊论文 | 课程论文
  word_count: int             # 正文字数
  current_ai_rate: float      # 当前AI率（客户提供或检测）
  target_ai_rate: float       # 目标AI率（默认<10%）
  target_platform: enum       # 知网 | 维普 | 万方 | 其他
  deadline: datetime          # 截止时间
  budget: float               # 客户预算
  source_file: path           # 原始文件路径
```

### 报价计算公式
```
报价 = 基础费 + 字数费 × 难度系数
基础费 = 10元
字数费 = 字数/1000 × 工具成本 × 3
难度系数 = 1.0（AI率<50%）| 1.5（50-80%）| 2.0（>80%）
```

## 二、处理阶段

### 处理流水线
```
原始文件 → 检测AI率 → 零感AI初降 → 人工复核 → 笔灵AI精修 → 最终检测 → 交付
```

### 状态机
```
PENDING → DETECTING → PROCESSING → REVIEWING → FINAL_CHECK → DELIVERED
                                                      ↓
                                                  REJECTED（需重做）
```

### 质量门禁
- [ ] AI率 < 目标值
- [ ] 语义保留度 > 90%
- [ ] 格式无损坏
- [ ] 参考文献真实可查
- [ ] 字数偏差 < ±5%

## 三、交付阶段

### 输出数据契约
```yaml
delivery:
  final_file: path            # 处理后文件
  before_ai_rate: float       # 处理前AI率
  after_ai_rate: float        # 处理后AI率
  tool_used: list             # 使用的工具
  processing_time: float      # 处理耗时（分钟）
  manual_review: bool         # 是否人工复核
```

### 交付清单
- [ ] 发送处理后文件
- [ ] 附检测截图（前后对比）
- [ ] 确认客户收到
- [ ] 收款
- [ ] 记录到 Obsidian

## 四、工具链

| 阶段 | 工具 | 成本 | 用途 |
|------|------|------|------|
| 检测 | 客户提供/免费检测 | 0 | 确定初始AI率 |
| 初降 | 零感AI | 1元/千字 | 快速降低 |
| 复核 | 人工 | 时间 | 语义修正 |
| 精修 | 笔灵AI | 3元/千字 | 深度降AI |
| 终检 | 目标平台 | 0-30元 | 最终验证 |

## 五、异常处理

| 异常 | 处理 |
|------|------|
| AI率降不下来 | 分段重新处理 + 人工改写 |
| 客户不满意 | 免费修改1次，之后半价 |
| 逾期 | 提前沟通，协商延期 |
| 跑单 | 定金不退，记录黑名单 |