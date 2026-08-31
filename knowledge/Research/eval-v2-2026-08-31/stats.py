"""Dependency-free statistics used by the matched three-arm evaluation."""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from fractions import Fraction
from numbers import Real
from statistics import NormalDist
from typing import TypeVar


_K = TypeVar("_K")


def _require_integer(value: object, name: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{name} must be an integer")
    return value


def _require_probability(value: object, name: str, *, open_interval: bool) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a real number")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    valid = 0.0 < result < 1.0 if open_interval else 0.0 <= result <= 1.0
    if not valid:
        interval = "(0, 1)" if open_interval else "[0, 1]"
        raise ValueError(f"{name} must be in {interval}")
    return result


def wilson_ci(
    successes: int, total: int, alpha: float = 0.05
) -> dict[str, float] | None:
    """Return a two-sided Wilson score interval for a binomial proportion.

    ``None`` represents the undefined interval for an empty sample.  Inputs are
    strict integers so values such as ``True`` cannot silently become counts.
    """

    successes = _require_integer(successes, "successes")
    total = _require_integer(total, "total")
    alpha = _require_probability(alpha, "alpha", open_interval=True)
    if total < 0:
        raise ValueError("total must be non-negative")
    if successes < 0 or successes > total:
        raise ValueError("successes must be between zero and total")
    if total == 0:
        return None

    rate = successes / total
    z = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    z2 = z * z
    denominator = 1.0 + z2 / total
    center = (rate + z2 / (2.0 * total)) / denominator
    half_width = (
        z
        * math.sqrt(rate * (1.0 - rate) / total + z2 / (4.0 * total * total))
        / denominator
    )
    return {
        "rate": rate,
        "low": max(0.0, center - half_width),
        "high": min(1.0, center + half_width),
    }


def _binary_values(values: Iterable[int], name: str) -> tuple[int, ...]:
    if isinstance(values, (str, bytes, bytearray)):
        raise ValueError(f"{name} must be an iterable of binary integers")
    try:
        result = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be an iterable of binary integers") from exc
    if any(type(value) is not int or value not in (0, 1) for value in result):
        raise ValueError(f"{name} must contain only integer 0 or 1 values")
    return result


def mcnemar_exact(arm_a: Iterable[int], arm_b: Iterable[int]) -> dict[str, float | int]:
    """Compute the two-sided exact McNemar test for aligned binary outcomes."""

    a = _binary_values(arm_a, "arm_a")
    b = _binary_values(arm_b, "arm_b")
    if len(a) != len(b):
        raise ValueError("arm_a and arm_b must have the same length")
    if not a:
        raise ValueError("McNemar's test requires at least one aligned pair")

    ab = sum(x == 1 and y == 0 for x, y in zip(a, b))
    ba = sum(x == 0 and y == 1 for x, y in zip(a, b))
    discordant = ab + ba
    paired_delta = (sum(a) - sum(b)) / len(a)
    if discordant == 0:
        p_value = 1.0
    else:
        lower_tail = min(ab, ba)
        numerator = 2 * sum(
            math.comb(discordant, k) for k in range(lower_tail + 1)
        )
        # Fraction avoids overflow when the discordant count is large while
        # preserving the exact binomial calculation until the final conversion.
        p_value = min(1.0, float(Fraction(numerator, 1 << discordant)))

    return {
        "ab": ab,
        "ba": ba,
        "discordant": discordant,
        "p_value": p_value,
        "paired_delta": paired_delta,
    }


def _validate_p_values(values: Iterable[object]) -> list[float]:
    result: list[float] = []
    for index, value in enumerate(values):
        result.append(
            _require_probability(value, f"p_values[{index}]", open_interval=False)
        )
    return result


def _holm_values(p_values: list[float]) -> list[float]:
    count = len(p_values)
    adjusted = [0.0] * count
    running_max = 0.0
    for rank, index in enumerate(sorted(range(count), key=p_values.__getitem__)):
        candidate = min(1.0, (count - rank) * p_values[index])
        running_max = max(running_max, candidate)
        adjusted[index] = running_max
    return adjusted


def holm_correction(
    p_values: Iterable[float] | Mapping[_K, float],
) -> list[float] | dict[_K, float]:
    """Apply Holm's step-down family-wise-error correction.

    Sequence results preserve positional order.  Mapping results preserve key
    insertion order and make the three preregistered comparisons self-labeling.
    """

    if isinstance(p_values, Mapping):
        keys = list(p_values.keys())
        adjusted = _holm_values(_validate_p_values(p_values.values()))
        return dict(zip(keys, adjusted))
    if isinstance(p_values, (str, bytes, bytearray)):
        raise ValueError("p_values must be an iterable of probabilities")
    try:
        values = _validate_p_values(p_values)
    except TypeError as exc:
        raise ValueError("p_values must be an iterable of probabilities") from exc
    return _holm_values(values)

