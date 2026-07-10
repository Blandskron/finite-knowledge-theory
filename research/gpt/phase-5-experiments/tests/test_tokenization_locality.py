"""Invariant tests for the exp-001 experimental controls."""

from pathlib import Path
import sys
import unittest
from itertools import product


CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from tokenization_locality import change_metrics, delimiter_groups, fixed_blocks, reconstruct, unit_blocks


class TokenizationLocalityTests(unittest.TestCase):
    def test_all_controls_reconstruct_exactly(self) -> None:
        samples = (b"", b"aaaaaa", b"ab|cd|", bytes(range(16)))
        for sample in samples:
            controls = (
                unit_blocks(sample),
                fixed_blocks(sample, 4),
                delimiter_groups(sample, ord("|"), 3, 4),
            )
            for groups in controls:
                self.assertEqual(reconstruct(groups), sample)

    def test_controls_are_deterministic(self) -> None:
        sample = b"ab|cd|"
        self.assertEqual(unit_blocks(sample), unit_blocks(sample))
        self.assertEqual(fixed_blocks(sample, 3), fixed_blocks(sample, 3))
        self.assertEqual(
            delimiter_groups(sample, ord("|"), 3, 4),
            delimiter_groups(sample, ord("|"), 3, 4),
        )

    def test_delimiter_groups_fall_back_when_domain_is_invalid(self) -> None:
        self.assertEqual(
            delimiter_groups(b"abcdef", ord("|"), 3, 4),
            unit_blocks(b"abcdef"),
        )

    def test_unit_groups_preserve_the_unmodified_suffix_after_insertion(self) -> None:
        before = unit_blocks(b"abcdefgh")
        after = unit_blocks(b"aXbcdefgh")
        metrics = change_metrics(before, after)
        self.assertEqual(metrics.common_prefix_groups, 1)
        self.assertEqual(metrics.common_suffix_groups, 7)
        self.assertEqual(metrics.changed_groups, 1)

    def test_fixed_groups_can_lose_the_shared_suffix_after_insertion(self) -> None:
        before = fixed_blocks(b"abcdefgh", 4)
        after = fixed_blocks(b"aXbcdefgh", 4)
        metrics = change_metrics(before, after)
        self.assertEqual(metrics.common_suffix_groups, 0)
        self.assertGreater(metrics.changed_groups, 1)

    def test_fixed_groups_preserve_completed_prefix_under_append_only_extension(self) -> None:
        before = fixed_blocks(b"abcdef", 4)
        after = fixed_blocks(b"abcdefXY", 4)
        metrics = change_metrics(before, after)
        self.assertEqual(before, (b"abcd", b"ef"))
        self.assertEqual(after, (b"abcd", b"efXY"))
        self.assertEqual(metrics.common_prefix_groups, 1)
        self.assertEqual(metrics.changed_groups, 2)

    def test_unit_groups_preserve_suffix_after_substitution_and_deletion(self) -> None:
        substituted = change_metrics(unit_blocks(b"abcdefgh"), unit_blocks(b"abcXefgh"))
        deleted = change_metrics(unit_blocks(b"abcdefgh"), unit_blocks(b"abdefgh"))
        self.assertEqual(substituted.common_suffix_groups, 4)
        self.assertEqual(deleted.common_suffix_groups, 5)

    def test_valid_delimiter_domain_preserves_the_following_group(self) -> None:
        before = delimiter_groups(b"ab|cd|", ord("|"), 3, 4)
        after = delimiter_groups(b"abZ|cd|", ord("|"), 3, 4)
        metrics = change_metrics(before, after)
        self.assertEqual(before, (b"ab|", b"cd|"))
        self.assertEqual(after, (b"abZ|", b"cd|"))
        self.assertEqual(metrics.common_suffix_groups, 1)

    def test_invalid_grouping_parameters_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            fixed_blocks(b"abc", 0)
        with self.assertRaises(ValueError):
            delimiter_groups(b"ab|", ord("|"), 4, 3)

    def test_unit_locality_for_all_short_binary_insertions(self) -> None:
        alphabet = (0, 1)
        checked_cases = 0
        for length in range(7):
            for values in product(alphabet, repeat=length):
                original = bytes(values)
                before = unit_blocks(original)
                for position in range(length + 1):
                    changed = original[:position] + b"\xff" + original[position:]
                    after = unit_blocks(changed)
                    metrics = change_metrics(before, after)
                    self.assertEqual(reconstruct(after), changed)
                    self.assertEqual(metrics.common_prefix_groups, position)
                    self.assertEqual(metrics.common_suffix_groups, length - position)
                    self.assertEqual(metrics.changed_groups, 1)
                    checked_cases += 1
        self.assertEqual(checked_cases, 769)

    def test_fixed_blocks_preserve_all_completed_groups_for_short_binary_appends(self) -> None:
        alphabet = (0, 1)
        checked_cases = 0
        for width in range(1, 5):
            for length in range(7):
                for values in product(alphabet, repeat=length):
                    original = bytes(values)
                    before = fixed_blocks(original, width)
                    for suffix_length in range(1, 4):
                        for suffix_values in product(alphabet, repeat=suffix_length):
                            suffix = bytes(suffix_values)
                            after = fixed_blocks(original + suffix, width)
                            metrics = change_metrics(before, after)
                            self.assertEqual(reconstruct(after), original + suffix)
                            self.assertEqual(
                                metrics.common_prefix_groups,
                                len(original) // width,
                            )
                            checked_cases += 1
        self.assertEqual(checked_cases, 7112)


if __name__ == "__main__":
    unittest.main()
