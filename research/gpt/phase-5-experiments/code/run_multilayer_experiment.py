"""Run exp-003 history-independence controls."""

from canonical_multilayer import midpoint_view, reconstruct_leaves


def main() -> None:
    final = b"aXbcd"
    routes = {
        "direct": final,
        "insertion": b"a" + b"X" + b"bcd",
        "concatenation": b"aX" + b"bcd",
        "edit": b"abcd"[:1] + b"X" + b"abcd"[1:],
    }
    views = {name: midpoint_view(value) for name, value in routes.items()}
    reference = views["direct"]
    for name, view in views.items():
        assert view == reference
        assert reconstruct_leaves(final, view) == final
        print(f"{name}: layers={view.layers} leaves={view.leaves}")


if __name__ == "__main__":
    main()
