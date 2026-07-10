"""Minimal marker-window grouping control for FKT exp-002."""

from __future__ import annotations

Grouping = tuple[bytes, ...]


def marker_window_groups(
    data: bytes,
    *,
    window: int,
    minimum: int,
    maximum: int,
    marker: int,
) -> Grouping:
    """Split on a visible window marker, forcing a cut at maximum length."""
    if window < 1:
        raise ValueError("window must be at least one")
    if not 1 <= minimum <= maximum:
        raise ValueError("expected 1 <= minimum <= maximum")
    if not 0 <= marker <= 255:
        raise ValueError("marker must be an octet")

    groups: list[bytes] = []
    start = 0
    for end in range(1, len(data) + 1):
        length = end - start
        window_sum = sum(data[max(0, end - window) : end]) % 256
        natural_cut = length >= minimum and end >= window and window_sum == marker
        forced_cut = length == maximum
        if natural_cut or forced_cut:
            groups.append(data[start:end])
            start = end

    if start < len(data):
        groups.append(data[start:])
    return tuple(groups)


def reconstruct(groups: Grouping) -> bytes:
    """Return the exact original byte sequence represented by groups."""
    return b"".join(groups)
