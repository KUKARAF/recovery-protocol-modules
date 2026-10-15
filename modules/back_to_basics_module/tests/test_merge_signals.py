"""Tests for Challenge 1.5: Merge Data Streams"""

import pytest
from modules.back_to_basics_module.tasks.merge_signals import merge_signals


class TestMergeSignals:
    """Test suite for signal merging."""

    def test_simple_merge(self):
        """Test basic merge of two equal-length lists."""
        a = [1, 2, 3]
        b = [10, 20, 30]
        assert merge_signals(a, b) == [1, 10, 2, 20, 3, 30]

    def test_string_merge(self):
        """Test merging string lists."""
        a = ['a', 'b', 'c']
        b = ['x', 'y', 'z']
        assert merge_signals(a, b) == ['a', 'x', 'b', 'y', 'c', 'z']

    def test_single_element_each(self):
        """Test with single element in each list."""
        a = [1]
        b = [10]
        assert merge_signals(a, b) == [1, 10]

    def test_two_elements_each(self):
        """Test with two elements in each list."""
        a = [1, 2]
        b = [10, 20]
        assert merge_signals(a, b) == [1, 10, 2, 20]

    def test_empty_lists(self):
        """Test with empty lists."""
        assert merge_signals([], []) == []

    def test_mixed_types(self):
        """Test with mixed data types."""
        a = [1, "two", 3.0]
        b = ['a', 2, 3]
        assert merge_signals(a, b) == [1, 'a', "two", 2, 3.0, 3]

    def test_with_negative_numbers(self):
        """Test with negative numbers."""
        a = [-1, -2, -3]
        b = [1, 2, 3]
        assert merge_signals(a, b) == [-1, 1, -2, 2, -3, 3]

    def test_with_zero(self):
        """Test with zeros."""
        a = [0, 0, 0]
        b = [1, 1, 1]
        assert merge_signals(a, b) == [0, 1, 0, 1, 0, 1]

    def test_with_none_values(self):
        """Test with None values."""
        a = [1, None, 3]
        b = [10, 20, None]
        assert merge_signals(a, b) == [1, 10, None, 20, 3, None]

    def test_large_lists(self):
        """Test with large lists."""
        a = list(range(1000))
        b = list(range(1000, 2000))
        result = merge_signals(a, b)

        # Check alternating pattern
        for i in range(1000):
            assert result[2 * i] == i
            assert result[2 * i + 1] == 1000 + i

    def test_preserves_stream_a_order(self):
        """Verify elements from stream A maintain their order."""
        a = [1, 2, 3, 4, 5]
        b = ['a', 'b', 'c', 'd', 'e']
        result = merge_signals(a, b)

        # Extract A elements (even indices)
        a_from_result = [result[i] for i in range(0, len(result), 2)]
        assert a_from_result == a

    def test_preserves_stream_b_order(self):
        """Verify elements from stream B maintain their order."""
        a = [1, 2, 3, 4, 5]
        b = ['a', 'b', 'c', 'd', 'e']
        result = merge_signals(a, b)

        # Extract B elements (odd indices)
        b_from_result = [result[i] for i in range(1, len(result), 2)]
        assert b_from_result == b

    def test_output_length(self):
        """Verify output length is sum of both lists."""
        a = [1, 2, 3]
        b = [10, 20, 30]
        result = merge_signals(a, b)
        assert len(result) == len(a) + len(b)

    def test_alternating_pattern(self):
        """Verify strict alternating A, B, A, B pattern."""
        a = ['A', 'A', 'A']
        b = ['B', 'B', 'B']
        result = merge_signals(a, b)
        assert result == ['A', 'B', 'A', 'B', 'A', 'B']

    def test_with_boolean_values(self):
        """Test with boolean values."""
        a = [True, False, True]
        b = [False, True, False]
        result = merge_signals(a, b)
        assert result == [True, False, False, True, True, False]

    def test_longer_lists(self):
        """Test with reasonably longer lists (100 elements each)."""
        a = list(range(100))
        b = list(range(100, 200))
        result = merge_signals(a, b)

        assert len(result) == 200
        assert result[0] == 0
        assert result[1] == 100
        assert result[-2] == 99
        assert result[-1] == 199

    def test_doesnt_modify_originals(self):
        """Verify original lists are not modified."""
        a = [1, 2, 3]
        b = [10, 20, 30]
        a_copy = a.copy()
        b_copy = b.copy()

        merge_signals(a, b)

        assert a == a_copy
        assert b == b_copy
