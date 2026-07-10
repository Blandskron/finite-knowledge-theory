"""Pure canonical multilayer interval control for FKT exp-003."""

from __future__ import annotations

from dataclasses import dataclass


Interval = tuple[int, int]


@dataclass(frozen=True)
class CanonicalView:
    layers: tuple[tuple[Interval, ...], ...]
    leaves: tuple[Interval, ...]


def midpoint_view(data: bytes) -> CanonicalView:
    """Build a canonical binary interval hierarchy from final input bytes only."""
    if not data:
        return CanonicalView((), ())

    by_depth: dict[int, list[Interval]] = {}
    leaves: list[Interval] = []

    def split(start: int, end: int, depth: int) -> None:
        by_depth.setdefault(depth, []).append((start, end))
        if end - start == 1:
            leaves.append((start, end))
            return
        middle = start + (end - start) // 2
        split(start, middle, depth + 1)
        split(middle, end, depth + 1)

    split(0, len(data), 0)
    layers = tuple(tuple(by_depth[depth]) for depth in sorted(by_depth))
    return CanonicalView(layers, tuple(leaves))


def reconstruct_leaves(data: bytes, view: CanonicalView) -> bytes:
    """Expand the observable leaf intervals back to the supplied byte sequence."""
    return b"".join(data[start:end] for start, end in view.leaves)
