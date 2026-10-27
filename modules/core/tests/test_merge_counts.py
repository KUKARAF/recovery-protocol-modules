"""Tests for Challenge 1.0.12: Combine the Tallies"""

import pytest
from modules.core.tasks.merge_counts import merge_counts


class TestMergeCounts:
    """Test suite for merge_counts."""

    def test_overlapping_keys_sum(self):
        assert merge_counts({"S": 3, "O": 1}, {"S": 2, "F": 5}) == {"S": 5, "O": 1, "F": 5}

    def test_no_overlap(self):
        assert merge_counts({"A": 1}, {"B": 2}) == {"A": 1, "B": 2}

    def test_first_empty(self):
        assert merge_counts({}, {"S": 1}) == {"S": 1}

    def test_second_empty(self):
        assert merge_counts({"S": 1}, {}) == {"S": 1}

    def test_both_empty(self):
        assert merge_counts({}, {}) == {}

    def test_identical_keys(self):
        assert merge_counts({"A": 5}, {"A": 5}) == {"A": 10}

    def test_does_not_mutate_inputs(self):
        a, b = {"A": 1}, {"A": 2}
        merge_counts(a, b)
        assert a == {"A": 1}
        assert b == {"A": 2}

    def test_return_type_is_dict(self):
        assert isinstance(merge_counts({"A": 1}, {"B": 2}), dict)

    def test_multiple_overlaps(self):
        assert merge_counts({"A": 1, "B": 2}, {"A": 10, "B": 20}) == {"A": 11, "B": 22}

    def test_zero_values(self):
        assert merge_counts({"A": 0}, {"A": 0}) == {"A": 0}
