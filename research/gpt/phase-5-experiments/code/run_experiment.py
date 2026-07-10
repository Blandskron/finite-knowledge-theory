"""Run deterministic control measurements for exp-001-tokenization-locality."""

from tokenization_locality import change_metrics, delimiter_groups, fixed_blocks, reconstruct, unit_blocks


def report(name: str, before: tuple[bytes, ...], after: tuple[bytes, ...]) -> None:
    metrics = change_metrics(before, after)
    print(
        f"{name}: before={len(before)} after={len(after)} "
        f"prefix={metrics.common_prefix_groups} suffix={metrics.common_suffix_groups} "
        f"changed={metrics.changed_groups}"
    )


def main() -> None:
    controls = {
        "unit": unit_blocks,
        "fixed-4": lambda value: fixed_blocks(value, 4),
        "delimiter": lambda value: delimiter_groups(value, ord("|"), 3, 4),
    }
    edits = {
        "insert": (b"abcdefgh", b"aXbcdefgh"),
        "substitute": (b"abcdefgh", b"abcXefgh"),
        "delete": (b"abcdefgh", b"abdefgh"),
    }
    for edit, (original, changed) in edits.items():
        for name, grouping in controls.items():
            before = grouping(original)
            after = grouping(changed)
            assert reconstruct(before) == original
            assert reconstruct(after) == changed
            report(f"{edit}/{name}", before, after)

    delimiter_before = delimiter_groups(b"ab|cd|", ord("|"), 3, 4)
    delimiter_after = delimiter_groups(b"abZ|cd|", ord("|"), 3, 4)
    assert reconstruct(delimiter_before) == b"ab|cd|"
    assert reconstruct(delimiter_after) == b"abZ|cd|"
    report("valid-delimiter/insert", delimiter_before, delimiter_after)


if __name__ == "__main__":
    main()
