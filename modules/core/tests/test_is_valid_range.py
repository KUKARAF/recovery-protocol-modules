"""Tests for Challenge 1.0.4: Within Tolerance"""

import pytest
from modules.core.tasks.is_valid_range import is_valid_range


class TestIsValidRange:
    """Test suite for is_valid_range."""

    def test_within_range(self):
        assert is_valid_range(5, 0, 10) is True

    def test_equal_to_low(self):
        assert is_valid_range(0, 0, 10) is True

    def test_equal_to_high(self):
        assert is_valid_range(10, 0, 10) is True

    def test_below_low(self):
        assert is_valid_range(-1, 0, 10) is False

    def test_above_high(self):
        assert is_valid_range(11, 0, 10) is False

    def test_negative_range(self):
        assert is_valid_range(-5, -10, -1) is True

    def test_float_value(self):
        assert is_valid_range(5.5, 0, 10) is True

    def test_float_just_outside(self):
        assert is_valid_range(10.01, 0, 10) is False

    def test_return_type_is_bool(self):
        assert isinstance(is_valid_range(5, 0, 10), bool)

    def test_zero_width_range_match(self):
        assert is_valid_range(5, 5, 5) is True
