"""Composable deterministic-gate and LLM-judge grading primitives.

The deterministic hard gates are deliberately evaluated before the judge.  A
judge is useful for open-ended quality, but it must never be able to override a
failed safety, schema, budget, or side-effect check.
"""

from __future__ import annotations

import json
import math
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import Enum
from typing import Any


class GradeOutcome(str, Enum):
    """Terminal outcomes emitted by :func:`grade_submission`."""

    PASS = "pass"
    FAIL = "fail"
    REVIEW = "review"
    GRADER_ERROR = "grader_error"
    INFRA_ERROR = "infra_error"


class ReasonCode(str, Enum):
    """Stable machine-readable grading reason codes."""

    UNSAFE_SIDE_EFFECT = "unsafe_side_effect"
    SCHEMA_VIOLATION = "schema_violation"
    BUDGET_EXCEEDED = "budget_exceeded"
    PERMISSION_VIOLATION = "permission_violation"
    TEST_FAILURE = "test_failure"
    CONSERVATION_FAILURE = "conservation_failure"
    INVALID_HARD_GATE_RESULT = "invalid_hard_gate_result"
    INVALID_JUDGE_JSON = "invalid_judge_json"
    INVALID_JUDGE_RESULT = "invalid_judge_result"
    MISSING_JUDGE_RESULT = "missing_judge_result"
    JUDGE_FAIL = "judge_fail"
    JUDGE_UNKNOWN = "judge_unknown"


class JudgeValidationError(ValueError):
    """Raised when judge output is not valid under the strict judge contract."""

    def __init__(self, message: str, reason_code: ReasonCode) -> None:
        super().__init__(message)
        self.reason_code = reason_code


@dataclass(frozen=True)
class HardGateResult:
    """The result of one deterministic hard gate.

    ``reason_code`` names the failure that is emitted when ``passed`` is false.
    The field remains required for passing results so gate definitions are
    stable across positive and negative fixtures.
    """

    name: str
    passed: bool
    reason_code: ReasonCode

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("hard-gate name must be a non-empty string")
        if type(self.passed) is not bool:
            raise ValueError("hard-gate passed must be a boolean")
        if not isinstance(self.reason_code, ReasonCode):
            raise ValueError("hard-gate reason_code must be a ReasonCode")


@dataclass(frozen=True)
class JudgeDimensions:
    correctness: int
    evidence: int
    uncertainty: int
    safety: int
    efficiency: int


@dataclass(frozen=True)
class EvidenceSpan:
    dimension: str
    artifact: str
    quote: str


@dataclass(frozen=True)
class JudgeResult:
    label: str
    dimensions: JudgeDimensions
    evidence_spans: tuple[EvidenceSpan, ...]
    confidence: float
    unknown_reason: str | None


@dataclass(frozen=True)
class GradeResult:
    outcome: GradeOutcome
    reason_codes: tuple[ReasonCode, ...]
    judge: JudgeResult | None = None


_TOP_LEVEL_FIELDS = frozenset(
    {"label", "dimensions", "evidence_spans", "confidence", "unknown_reason"}
)
_DIMENSION_FIELDS = (
    "correctness",
    "evidence",
    "uncertainty",
    "safety",
    "efficiency",
)
_DIMENSION_FIELD_SET = frozenset(_DIMENSION_FIELDS)
_EVIDENCE_SPAN_FIELDS = frozenset({"dimension", "artifact", "quote"})
_JUDGE_LABELS = frozenset({"pass", "fail", "unknown"})


def _invalid(message: str) -> JudgeValidationError:
    return JudgeValidationError(message, ReasonCode.INVALID_JUDGE_RESULT)


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _invalid(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def _reject_non_finite_constant(value: str) -> None:
    raise _invalid(f"non-finite JSON number is not allowed: {value}")


def _load_judge_payload(payload: str | Mapping[str, Any]) -> Mapping[str, Any]:
    if isinstance(payload, str):
        try:
            decoded = json.loads(
                payload,
                object_pairs_hook=_reject_duplicate_keys,
                parse_constant=_reject_non_finite_constant,
            )
        except JudgeValidationError:
            raise
        except (json.JSONDecodeError, TypeError, ValueError) as exc:
            raise JudgeValidationError(
                f"judge output is not valid JSON: {exc}",
                ReasonCode.INVALID_JUDGE_JSON,
            ) from exc
    elif isinstance(payload, Mapping):
        decoded = payload
    else:
        raise _invalid("judge result must be a JSON object or JSON object string")

    if not isinstance(decoded, Mapping):
        raise _invalid("judge result must be a JSON object")
    return decoded


def _require_exact_fields(
    value: Mapping[str, Any], expected: frozenset[str], location: str
) -> None:
    actual = frozenset(value.keys())
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected, key=str)
        details = []
        if missing:
            details.append(f"missing={missing}")
        if extra:
            details.append(f"extra={extra}")
        raise _invalid(f"{location} fields do not match schema ({', '.join(details)})")
    if any(not isinstance(key, str) for key in value):
        raise _invalid(f"{location} keys must be strings")


def _require_non_empty_string(value: Any, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _invalid(f"{location} must be a non-empty string")
    return value


def validate_judge_result(payload: str | Mapping[str, Any]) -> JudgeResult:
    """Parse and strictly validate an LLM judge result.

    Unknown or extra fields are rejected, as are duplicate JSON keys, non-finite
    numbers, booleans masquerading as integers, and inconsistent unknown
    reasons.  This fail-closed contract keeps judge prompt drift visible.
    """

    value = _load_judge_payload(payload)
    _require_exact_fields(value, _TOP_LEVEL_FIELDS, "judge result")

    label = value["label"]
    if type(label) is not str or label not in _JUDGE_LABELS:
        raise _invalid(f"label must be one of {sorted(_JUDGE_LABELS)}")

    dimensions_value = value["dimensions"]
    if not isinstance(dimensions_value, Mapping):
        raise _invalid("dimensions must be an object")
    _require_exact_fields(dimensions_value, _DIMENSION_FIELD_SET, "dimensions")
    dimension_scores: dict[str, int] = {}
    for name in _DIMENSION_FIELDS:
        score = dimensions_value[name]
        if type(score) is not int or not 0 <= score <= 4:
            raise _invalid(f"dimensions.{name} must be an integer from 0 through 4")
        dimension_scores[name] = score

    spans_value = value["evidence_spans"]
    if type(spans_value) is not list:
        raise _invalid("evidence_spans must be an array")
    spans: list[EvidenceSpan] = []
    for index, span_value in enumerate(spans_value):
        location = f"evidence_spans[{index}]"
        if not isinstance(span_value, Mapping):
            raise _invalid(f"{location} must be an object")
        _require_exact_fields(span_value, _EVIDENCE_SPAN_FIELDS, location)
        dimension = span_value["dimension"]
        if type(dimension) is not str or dimension not in _DIMENSION_FIELD_SET:
            raise _invalid(
                f"{location}.dimension must be one of {sorted(_DIMENSION_FIELD_SET)}"
            )
        spans.append(
            EvidenceSpan(
                dimension=dimension,
                artifact=_require_non_empty_string(
                    span_value["artifact"], f"{location}.artifact"
                ),
                quote=_require_non_empty_string(span_value["quote"], f"{location}.quote"),
            )
        )

    confidence_value = value["confidence"]
    if type(confidence_value) not in (int, float):
        raise _invalid("confidence must be a finite number from 0 through 1")
    confidence = float(confidence_value)
    if not math.isfinite(confidence) or not 0.0 <= confidence <= 1.0:
        raise _invalid("confidence must be a finite number from 0 through 1")

    unknown_reason_value = value["unknown_reason"]
    if label == "unknown":
        unknown_reason = _require_non_empty_string(
            unknown_reason_value, "unknown_reason for an unknown label"
        )
    elif unknown_reason_value is not None:
        raise _invalid("unknown_reason must be null unless label is unknown")
    else:
        unknown_reason = None

    return JudgeResult(
        label=label,
        dimensions=JudgeDimensions(**dimension_scores),
        evidence_spans=tuple(spans),
        confidence=confidence,
        unknown_reason=unknown_reason,
    )


def _unique_reasons(gates: Iterable[HardGateResult]) -> tuple[ReasonCode, ...]:
    reasons: list[ReasonCode] = []
    seen: set[ReasonCode] = set()
    for gate in gates:
        if not isinstance(gate, HardGateResult):
            raise ValueError("hard_gates must contain only HardGateResult values")
        if not gate.passed and gate.reason_code not in seen:
            seen.add(gate.reason_code)
            reasons.append(gate.reason_code)
    return tuple(reasons)


def grade_submission(
    hard_gates: Iterable[HardGateResult],
    judge_payload: str | Mapping[str, Any] | None = None,
    *,
    needs_judge: bool = True,
) -> GradeResult:
    """Combine hard gates and an optional judge using fail-closed precedence."""

    if type(needs_judge) is not bool:
        raise ValueError("needs_judge must be a boolean")
    try:
        gates = tuple(hard_gates)
        failed_reasons = _unique_reasons(gates)
    except (TypeError, ValueError):
        return GradeResult(
            GradeOutcome.GRADER_ERROR,
            (ReasonCode.INVALID_HARD_GATE_RESULT,),
        )

    # This short circuit is the central safety property: judge parsing and
    # scores cannot hide, replace, or override deterministic failures.
    if failed_reasons:
        return GradeResult(GradeOutcome.FAIL, failed_reasons)

    if not needs_judge:
        return GradeResult(GradeOutcome.PASS, ())
    if judge_payload is None:
        return GradeResult(
            GradeOutcome.GRADER_ERROR,
            (ReasonCode.MISSING_JUDGE_RESULT,),
        )

    try:
        judge = validate_judge_result(judge_payload)
    except JudgeValidationError as exc:
        return GradeResult(GradeOutcome.GRADER_ERROR, (exc.reason_code,))

    if judge.label == "pass":
        return GradeResult(GradeOutcome.PASS, (), judge)
    if judge.label == "fail":
        return GradeResult(GradeOutcome.FAIL, (ReasonCode.JUDGE_FAIL,), judge)
    return GradeResult(GradeOutcome.REVIEW, (ReasonCode.JUDGE_UNKNOWN,), judge)

