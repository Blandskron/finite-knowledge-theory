"""Tests for the exp-003 canonical multilayer control."""

from pathlib import Path
import sys
import unittest


CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from canonical_multilayer import midpoint_view, reconstruct_leaves


class CanonicalMultilayerTests(unittest.TestCase):
    def test_empty_input_has_no_intervals(self) -> None:
        self.assertEqual(midpoint_view(b"").layers, ())
        self.assertEqual(midpoint_view(b"").leaves, ())

    def test_leaves_reconstruct_multiple_lengths(self) -> None:
        for length in range(1, 17):
            data = bytes(range(length))
            view = midpoint_view(data)
            self.assertEqual(reconstruct_leaves(data, view), data)
            self.assertTrue(all(end - start == 1 for start, end in view.leaves))

    def test_all_history_routes_have_identical_observable_layers(self) -> None:
        final = b"aXbcd"
        routes = (
            final,
            b"a" + b"X" + b"bcd",
            b"aX" + b"bcd",
            b"abcd"[:1] + b"X" + b"abcd"[1:],
        )
        views = tuple(midpoint_view(route) for route in routes)
        self.assertTrue(all(view == views[0] for view in views))

    def test_root_interval_changes_when_length_changes(self) -> None:
        before = midpoint_view(b"abcdefgh")
        after = midpoint_view(b"aXbcdefgh")
        self.assertEqual(before.layers[0], ((0, 8),))
        self.assertEqual(after.layers[0], ((0, 9),))
        self.assertNotEqual(before.layers, after.layers)
