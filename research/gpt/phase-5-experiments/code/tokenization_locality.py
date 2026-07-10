"""Pure, experimental token grouping controls for FKT Phase 5."""

from __future__ import annotations

from dataclasses import dataclass


Grouping = tuple[bytes, ...]


def unit_blocks(data: bytes) -> Grouping:
    """Return the canonical one-octet grouping τ₁."""
    return tuple(data[index : index + 1] for index in range(len(data)))


def fixed_blocks(data: bytes, width: int) -> Grouping:
    """Partition data from the left into non-empty blocks of at most width."""
    if width < 1:
        raise ValueError("width must be at least one")
    return tuple(data[index : index + width] for index in range(0, len(data), width))


def delimiter_groups(data: bytes, delimiter: int, minimum: int, maximum: int) -> Grouping:
    """Group delimiter-terminated segments or fall back to canonical unit blocks."""
    if not 0 <= delimiter <= 255:
        raise ValueError("delimiter must be an octet")
    if not 2 <= minimum <= maximum:
        raise ValueError("expected 2 <= minimum <= maximum")
    if not data:
        return ()

    marker = bytes((delimiter,))
    groups: list[bytes] = []
    start = 0
    for index, value in enumerate(data):
        if value != delimiter:
            continue
        group = data[start : index + 1]
        if not minimum <= len(group) <= maximum:
            return unit_blocks(data)
        groups.append(group)
        start = index + 1

    if start != len(data) or not groups or marker in b"".join(group[:-1] for group in groups):
        return unit_blocks(data)
    return tuple(groups)


def reconstruct(groups: Grouping) -> bytes:
    """Expand any experimental grouping back to its original octets."""
    return b"".join(groups)


@dataclass(frozen=True)
class ChangeMetrics:
    common_prefix_groups: int
    common_suffix_groups: int
    changed_groups: int


def change_metrics(before: Grouping, after: Grouping) -> ChangeMetrics:
    """Measure exact shared prefix/suffix groups between two experiment outputs."""
    prefix = 0
    limit = min(len(before), len(after))
    while prefix < limit and before[prefix] == after[prefix]:
        prefix += 1

    suffix = 0
    while suffix < limit - prefix and before[-(suffix + 1)] == after[-(suffix + 1)]:
        suffix += 1

    changed = (len(before) - prefix - suffix) + (len(after) - prefix - suffix)
    return ChangeMetrics(prefix, suffix, changed)
