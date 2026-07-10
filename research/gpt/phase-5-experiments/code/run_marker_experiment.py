"""Run the two deterministic controls for exp-002."""

from marker_window import marker_window_groups, reconstruct
from tokenization_locality import change_metrics


def report(name: str, before: tuple[bytes, ...], after: tuple[bytes, ...]) -> None:
    metrics = change_metrics(before, after)
    print(
        f"{name}: before={before} after={after} "
        f"prefix={metrics.common_prefix_groups} suffix={metrics.common_suffix_groups} "
        f"changed={metrics.changed_groups}"
    )


def groups(data: bytes) -> tuple[bytes, ...]:
    return marker_window_groups(data, window=1, minimum=2, maximum=4, marker=ord("Z"))


def main() -> None:
    cases = {
        "natural-marker": (b"abZcdZ", b"abXZcdZ"),
        "forced-only": (b"abcdefghijkl", b"aXbcdefghijkl"),
    }
    for name, (original, changed) in cases.items():
        before = groups(original)
        after = groups(changed)
        assert reconstruct(before) == original
        assert reconstruct(after) == changed
        report(name, before, after)


if __name__ == "__main__":
    main()
