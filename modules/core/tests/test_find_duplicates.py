"""Tests for Challenge 1.0.7: Echoes in the Log"""

import pytest
from modules.core.tasks.find_duplicates import find_duplicates


class TestFindDuplicates:
    """Test suite for find_duplicates."""

    def test_simple_duplicates(self):
        assert find_duplicates([1, 2, 3, 2, 4, 1]) == [2, 1]

    def test_no_duplicates(self):
        assert find_duplicates([5, 6, 7]) == []

    def test_value_repeated_three_times(self):
        """Only added once, even though it repeats more than once."""
        assert find_duplicates([9, 9, 9]) == [9]

    def test_empty_list(self):
        assert find_duplicates([]) == []

    def test_all_same_value(self):
        assert find_duplicates([1, 1, 1, 1]) == [1]

    def test_strings(self):
        assert find_duplicates(["a", "b", "a", "c"]) == ["a"]

    def test_duplicate_order_matches_detection_order(self):
        assert find_duplicates([3, 1, 3, 1]) == [3, 1]

    def test_single_element(self):
        assert find_duplicates([1]) == []

    def test_adjacent_duplicates(self):
        assert find_duplicates([1, 1, 2, 2]) == [1, 2]

    def test_return_type_is_list(self):
        assert isinstance(find_duplicates([1, 1]), list)
