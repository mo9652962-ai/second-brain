"""Timeline-based failure attribution for agent evaluation transcripts."""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from numbers import Real
from typing import Any


class FailureCode(str, Enum):
    INFRA = "INFRA"
    TIMEOUT = "TIMEOUT"
    TOOL = "TOOL"
    ORCH = "ORCH"
    BUDGET = "BUDGET"
    GATE = "GATE"
    PARSE = "PARSE"
    TASK = "TASK"
    DATA = "DATA"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class AttributedEvent:
    timestamp: int | float | str
    event_type: str
    code: FailureCode | None
    recovered: bool
    blocking: bool
    evidence: str | None


@dataclass(frozen=True)
class FailureAttribution:
    primary: FailureCode | None
    contributing: tuple[FailureCode, ...]
    observed_events: tuple[FailureCode, ...]
    timeline: tuple[AttributedEvent, ...]


_EVENT_CODES: dict[str, FailureCode] = {
    "infra": FailureCode.INFRA,
    "infra_error": FailureCode.INFRA,
    "infrastructure_error": FailureCode.INFRA,
    "http_error": FailureCode.INFRA,
    "provider_error": FailureCode.INFRA,
    "network_error": FailureCode.INFRA,
    "authentication_error": FailureCode.INFRA,
    "rate_limit": FailureCode.INFRA,
    "timeout": FailureCode.TIMEOUT,
    "call_timeout": FailureCode.TIMEOUT,
    "wall_clock_timeout": FailureCode.TIMEOUT,
    "tool_error": FailureCode.TOOL,
    "tool_failure": FailureCode.TOOL,
    "tool_unavailable": FailureCode.TOOL,
    "tool_parameter_error": FailureCode.TOOL,
    "orchestration_error": FailureCode.ORCH,
    "orchestrator_error": FailureCode.ORCH,
    "orch_error": FailureCode.ORCH,
    "deadlock": FailureCode.ORCH,
    "worker_lost": FailureCode.ORCH,
    "message_routing_error": FailureCode.ORCH,
    "lease_conflict": FailureCode.ORCH,
    "budget_exhausted": FailureCode.BUDGET,
    "budget_error": FailureCode.BUDGET,
    "token_budget_exhausted": FailureCode.BUDGET,
    "step_budget_exhausted": FailureCode.BUDGET,
    "gate_error": FailureCode.GATE,
    "gate_failure": FailureCode.GATE,
    "gate_missed": FailureCode.GATE,
    "gate_repair_loop": FailureCode.GATE,
    "gate_wrong_rejection": FailureCode.GATE,
    "parse_error": FailureCode.PARSE,
    "parsing_error": FailureCode.PARSE,
    "judge_parse_error": FailureCode.PARSE,
    "parser_error": FailureCode.PARSE,
    "grader_error": FailureCode.PARSE,
    "schema_error": FailureCode.PARSE,
    "invalid_judge_json": FailureCode.PARSE,
    "incorrect_answer": FailureCode.TASK,
    "incorrect_result": FailureCode.TASK,
    "task_error": FailureCode.TASK,
    "wrong_answer": FailureCode.TASK,
    "reasoning_error": FailureCode.TASK,
    "task_failure": FailureCode.TASK,
    "rubric_failure": FailureCode.TASK,
    "ambiguous_task": FailureCode.DATA,
    "data_ambiguity": FailureCode.DATA,
    "task_ambiguity": FailureCode.DATA,
    "data_error": FailureCode.DATA,
    "fixture_error": FailureCode.DATA,
    "reference_error": FailureCode.DATA,
    "input_corrupt": FailureCode.DATA,
    "unknown": FailureCode.UNKNOWN,
    "unknown_failure": FailureCode.UNKNOWN,
}
_NON_FAILURE_EVENTS = frozenset(
    {"output_completed", "checkpoint", "run_started", "retry_succeeded"}
)
_SUCCESS_OUTCOMES = frozenset({"pass", "passed", "success", "succeeded", "scored"})


def _time_key(timestamp: int | float | str) -> float:
    if isinstance(timestamp, bool):
        raise ValueError("event timestamp must not be a boolean")
    if isinstance(timestamp, Real):
        value = float(timestamp)
        if not math.isfinite(value):
            raise ValueError("event timestamp must be finite")
        return value
    if isinstance(timestamp, str) and timestamp.strip():
        normalized = timestamp.strip()
        if normalized.endswith("Z"):
            normalized = normalized[:-1] + "+00:00"
        try:
            return datetime.fromisoformat(normalized).timestamp()
        except ValueError as exc:
            raise ValueError(f"invalid ISO-8601 event timestamp: {timestamp!r}") from exc
    raise ValueError("event timestamp must be a number or ISO-8601 string")


def _event_code(event: Mapping[str, Any], event_type: str) -> FailureCode | None:
    explicit = event.get("failure_code")
    if explicit is not None:
        if isinstance(explicit, FailureCode):
            return explicit
        if isinstance(explicit, str):
            try:
                return FailureCode(explicit.upper())
            except ValueError as exc:
                raise ValueError(f"unknown explicit failure_code: {explicit!r}") from exc
        raise ValueError("failure_code must be a string or FailureCode")
    if event_type in _NON_FAILURE_EVENTS:
        return None
    return _EVENT_CODES.get(event_type, FailureCode.UNKNOWN)


def _ordered_unique(values: Iterable[FailureCode]) -> tuple[FailureCode, ...]:
    result: list[FailureCode] = []
    seen: set[FailureCode] = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return tuple(result)


def attribute_failure(
    events: Iterable[Mapping[str, Any]], *, final_outcome: str
) -> FailureAttribution:
    """Attribute a run using the earliest unrecovered blocker in its timeline.

    Recovered failures remain in ``observed_events`` for reliability reporting,
    but they are neither primary nor contributing causes.  Later unrecovered
    categories are retained as contributors instead of replacing the primary.
    """

    if not isinstance(final_outcome, str) or not final_outcome.strip():
        raise ValueError("final_outcome must be a non-empty string")
    try:
        raw_events = list(events)
    except TypeError as exc:
        raise ValueError("events must be an iterable of event objects") from exc

    indexed_events: list[tuple[float, int, Mapping[str, Any]]] = []
    for index, event in enumerate(raw_events):
        if not isinstance(event, Mapping):
            raise ValueError(f"events[{index}] must be an object")
        if "timestamp" not in event:
            raise ValueError(f"events[{index}] is missing timestamp")
        indexed_events.append((_time_key(event["timestamp"]), index, event))
    indexed_events.sort(key=lambda item: (item[0], item[1]))

    timeline: list[AttributedEvent] = []
    for _, _, event in indexed_events:
        event_type_value = event.get("event_type")
        if not isinstance(event_type_value, str) or not event_type_value.strip():
            raise ValueError("event_type must be a non-empty string")
        event_type = event_type_value.strip().lower()
        code = _event_code(event, event_type)
        recovered_value = event.get("recovered", False)
        if type(recovered_value) is not bool:
            raise ValueError("event recovered must be a boolean when supplied")
        blocker_flags = []
        for flag_name in ("terminal", "unrecoverable", "retries_exhausted"):
            flag_value = event.get(flag_name, False)
            if type(flag_value) is not bool:
                raise ValueError(f"event {flag_name} must be a boolean when supplied")
            blocker_flags.append(flag_value)
        blocking = any(blocker_flags)
        evidence_value = event.get("evidence")
        if evidence_value is not None and not isinstance(evidence_value, str):
            raise ValueError("event evidence must be a string or null")
        timeline.append(
            AttributedEvent(
                timestamp=event["timestamp"],
                event_type=event_type,
                code=code,
                recovered=recovered_value,
                blocking=blocking,
                evidence=evidence_value,
            )
        )

    observed = _ordered_unique(
        item.code for item in timeline if item.code is not None
    )
    if final_outcome.strip().lower() in _SUCCESS_OUTCOMES:
        return FailureAttribution(None, (), observed, tuple(timeline))

    # ``recovered`` is the causal boundary. A non-terminal error can still be
    # the earliest unrecoverable cause of a later terminal artifact, so the
    # terminal flag must not make a later transcript line steal attribution.
    causal = [
        item for item in timeline if item.code is not None and not item.recovered
    ]
    if not causal:
        return FailureAttribution(FailureCode.UNKNOWN, (), observed, tuple(timeline))

    primary = causal[0].code
    assert primary is not None
    contributing = _ordered_unique(
        item.code
        for item in causal[1:]
        if item.code is not None and item.code != primary
    )
    return FailureAttribution(primary, contributing, observed, tuple(timeline))
