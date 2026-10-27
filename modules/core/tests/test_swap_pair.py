"""Tests for Challenge 1.0.9: Reverse the Channel"""

import pytest
from modules.core.tasks.swap_pair import swap_pair


class TestSwapPair:
    """Test suite for swap_pair."""

    def test_simple_integers(self):
        assert swap_pair((1, 2)) == (2, 1)

    def test_strings(self):
        assert swap_pair(("alpha", "beta")) == ("beta", "alpha")

    def test_identical_values(self):
        assert swap_pair((5, 5)) == (5, 5)

    def test_mixed_types(self):
        assert swap_pair((1, "a")) == ("a", 1)

    def test_negative_numbers(self):
        assert swap_pair((-1, -2)) == (-2, -1)

    def test_return_type_is_tuple(self):
        assert isinstance(swap_pair((1, 2)), tuple)

    def test_does_not_mutate_input(self):
        original = (1, 2)
        swap_pair(original)
        assert original == (1, 2)

    def test_booleans(self):
        assert swap_pair((True, False)) == (False, True)

    def test_floats(self):
        assert swap_pair((1.5, 2.5)) == (2.5, 1.5)

    def test_zero_and_value(self):
        assert swap_pair((0, 10)) == (10, 0)
