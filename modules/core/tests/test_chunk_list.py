"""Tests for Challenge 1.0.8: Packet Framing"""

import pytest
from modules.core.tasks.chunk_list import chunk_list


class TestChunkList:
    """Test suite for chunk_list."""

    def test_even_division(self):
        assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

    def test_uneven_division(self):
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

    def test_empty_list(self):
        assert chunk_list([], 3) == []

    def test_chunk_size_larger_than_list(self):
        assert chunk_list([1, 2], 5) == [[1, 2]]

    def test_chunk_size_one(self):
        assert chunk_list([1, 2, 3], 1) == [[1], [2], [3]]

    def test_chunk_size_equal_to_length(self):
        assert chunk_list([1, 2, 3], 3) == [[1, 2, 3]]

    def test_strings(self):
        assert chunk_list(["a", "b", "c"], 2) == [["a", "b"], ["c"]]

    def test_preserves_order(self):
        result = chunk_list(list(range(10)), 3)
        assert result == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

    def test_return_type_is_list_of_lists(self):
        result = chunk_list([1, 2, 3], 2)
        assert isinstance(result, list)
        assert all(isinstance(c, list) for c in result)

    def test_single_element_list(self):
        assert chunk_list([1], 2) == [[1]]
