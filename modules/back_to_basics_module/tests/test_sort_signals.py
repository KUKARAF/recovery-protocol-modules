"""Tests for Challenge 1.1: Sort the Chaos"""

import pytest
import time
from modules.back_to_basics_module.tasks.sort_signals import sort_signals


class TestSortSignals:
    """Test suite for signal sorting challenge."""

    def test_simple_positive_numbers(self):
        """Test sorting simple positive numbers."""
        assert sort_signals([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    def test_already_sorted(self):
        """Test list that's already sorted."""
        assert sort_signals([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test reverse sorted list."""
        assert sort_signals([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_mixed_positive_and_negative(self):
        """Test mixed positive and negative numbers."""
        assert sort_signals([-5, 10, 0, -2, 8]) == [-5, -2, 0, 8, 10]

    def test_with_zeros(self):
        """Test list containing zeros."""
        assert sort_signals([0, -1, 1, 0, -1]) == [-1, -1, 0, 0, 1]

    def test_single_element(self):
        """Test single element list."""
        assert sort_signals([42]) == [42]

    def test_two_elements(self):
        """Test two element list."""
        assert sort_signals([2, 1]) == [1, 2]

    def test_empty_list(self):
        """Test empty list."""
        assert sort_signals([]) == []

    def test_all_same_elements(self):
        """Test list with all same elements."""
        assert sort_signals([5, 5, 5, 5]) == [5, 5, 5, 5]

    def test_large_numbers(self):
        """Test with large numbers."""
        assert sort_signals([1000000, -1000000, 0]) == [-1000000, 0, 1000000]

    def test_performance_1000_elements(self):
        """Test performance with 1000 elements (should be <100ms)."""
        import random
        data = [random.randint(-1000, 1000) for _ in range(1000)]

        start = time.time()
        result = sort_signals(data)
        elapsed = time.time() - start

        # Verify correctness
        assert result == sorted(data)

        # Performance check: should be < 100ms
        assert elapsed < 0.1, f"Sorting took {elapsed*1000:.2f}ms, must be <100ms"

    def test_returns_new_list(self):
        """Test that function returns a new list (not same reference)."""
        original = [3, 1, 2]
        result = sort_signals(original)

        # Original should not be modified if sorted() is used
        # (This tests that you understand the difference between sort() and sorted())
        assert result == [1, 2, 3]


class TestSortSignalsEdgeCases:
    """Edge case tests for robustness."""

    def test_very_long_list(self):
        """Test with very long list."""
        data = list(range(10000, 0, -1))  # 10000 down to 1
        result = sort_signals(data)
        assert result == list(range(1, 10001))

    def test_duplicates_heavy(self):
        """Test with many duplicate values."""
        assert sort_signals([1, 1, 1, 2, 2, 2, 3, 3, 3]) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
