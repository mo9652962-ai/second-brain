---
tags: [knowledge]
title: "Multi-Agent Eval v2 implementation"
type: note
created: 2026-09-05
updated: 2026-09-05
---

# Multi-Agent Eval v2 implementation

This repository turns the design in `EVAL_PLAN.md` into dependency-free grading,
statistics, and failure-attribution primitives plus a draft manifest for the
matched 180-run experiment. It does not execute providers or perform network
calls.

## Repository contents

| File | Purpose |
|---|---|
| `task_cards.jsonl` | Ten open-task cards (`T01`–`T10`) with budgets, artifacts, hard gates, and judge dimensions. |
| `graders.py` | Hard-gate-first aggregation and strict LLM judge JSON validation. |
| `stats.py` | Wilson intervals, exact paired McNemar tests, and Holm correction. |
| `failure_attribution.py` | Timeline reconstruction and the ten-code failure taxonomy. |
| `run_manifest.yaml` | Three-arm matched design, scheduling, grading, metrics, and provenance requirements. |
| `tests/` | Unit tests for precedence, validation, statistics, and attribution behavior. |

## Local validation

No package installation is required by the implementation. If `pytest` is
already available in a local Python interpreter, run:

```powershell
python -m pytest -q
```

The modules themselves use only the Python standard library and support Python
3.11 or newer.

Useful data checks without PyYAML are:

```powershell
python -c "import json; rows=[json.loads(x) for x in open('task_cards.jsonl', encoding='utf-8') if x.strip()]; assert len(rows)==10; assert len({x['task_id'] for x in rows})==10"
python -m py_compile graders.py stats.py failure_attribution.py
```

## Grading contract

Call `grade_submission(hard_gates, judge_payload, needs_judge=True)`. Failed
deterministic gates are collected in stable input order, deduplicated by reason
code, and returned before the judge payload is parsed. Thus malformed or passing
judge output cannot override a deterministic failure.

When a judge is needed, its output must be one strict JSON object containing
exactly:

```json
{
  "label": "pass",
  "dimensions": {
    "correctness": 4,
    "evidence": 3,
    "uncertainty": 3,
    "safety": 4,
    "efficiency": 3
  },
  "evidence_spans": [
    {"dimension": "correctness", "artifact": "answer.md", "quote": "Result"}
  ],
  "confidence": 0.9,
  "unknown_reason": null
}
```

Scores are integer values from 0 through 4, confidence is finite and lies in
`[0, 1]`, and extra/missing/duplicate fields are rejected. `unknown_reason` must
be a non-empty string only when `label` is `unknown`. Malformed judge output is
a `grader_error`, not an agent-quality failure; `unknown` routes to review.

## Statistical contract

- `wilson_ci(successes, total, alpha=0.05)` returns `rate`, `low`, and `high`, or
  `None` for `0/0`.
- `mcnemar_exact(arm_a, arm_b)` requires non-empty aligned integer `0/1` pairs
  and reports `ab`, `ba`, discordance, the exact two-sided p-value, and paired
  success-rate delta.
- `holm_correction(...)` accepts either an iterable of p-values or a mapping of
  named comparisons and preserves original order.

For the preregistered analysis, apply McNemar only to matched binary outcomes
for `M vs S`, `NG vs M`, and `NG vs S`, then apply Holm to those three p-values.
Do not use McNemar for score, token, latency, or cost outcomes.

## Failure-attribution contract

`attribute_failure(events, final_outcome=...)` sorts events by timestamp and
uses the earliest unrecovered blocker as primary. Later distinct blockers become
contributors. Recovered events remain in `observed_events` for reliability
reporting but cannot become primary or contributing causes. The taxonomy is:
`INFRA`, `TIMEOUT`, `TOOL`, `ORCH`, `BUDGET`, `GATE`, `PARSE`, `TASK`, `DATA`,
and `UNKNOWN`.

## Before a formal run

`run_manifest.yaml` intentionally leaves model, prompt, fixture, tool, and
configuration hashes as `null`. Populate them from the final frozen bytes before
execution; do not substitute descriptive labels or provisional digests. The
formal design is 20 task templates × 3 instances × 3 arms = 180 matched runs.
Dry runs, retries, and the separate Regression-20 suite do not increase that
sample count. External side effects must remain simulated or dry-run only.

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]
