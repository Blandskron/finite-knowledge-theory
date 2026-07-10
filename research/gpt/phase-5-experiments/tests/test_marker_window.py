"""Tests for the exp-002 marker-window control."""

from pathlib import Path
import sys
import unittest


CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from marker_window import marker_window_groups, reconstruct
from tokenization_locality import change_metrics


def groups(data: bytes) -> tuple[bytes, ...]:
    return marker_window_groups(data, window=1, minimum=2, maximum=4, marker=ord("Z"))


class MarkerWindowTests(unittest.TestCase):
    def test_groups_reconstruct_and_respect_maximum(self) -> None:
        sample = b"abZcdZefghijkl"
        output = groups(sample)
        self.assertEqual(reconstruct(output), sample)
        self.assertTrue(all(1 <= len(group) <= 4 for group in output))

    def test_natural_marker_preserves_following_group(self) -> None:
        before = groups(b"abZcdZ")
        after = groups(b"abXZcdZ")
        metrics = change_metrics(before, after)
        self.assertEqual(before, (b"abZ", b"cdZ"))
        self.assertEqual(after, (b"abXZ", b"cdZ"))
        self.assertEqual(metrics.common_suffix_groups, 1)

    def test_forced_only_case_loses_exact_shared_suffix(self) -> None:
        before = groups(b"abcdefghijkl")
        after = groups(b"aXbcdefghijkl")
        metrics = change_metrics(before, after)
        self.assertEqual(before, (b"abcd", b"efgh", b"ijkl"))
        self.assertEqual(metrics.common_suffix_groups, 0)
        self.assertGreater(metrics.changed_groups, 1)

    def test_invalid_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            marker_window_groups(b"abc", window=0, minimum=1, maximum=2, marker=0)
        with self.assertRaises(ValueError):
            marker_window_groups(b"abc", window=1, minimum=3, maximum=2, marker=0)
