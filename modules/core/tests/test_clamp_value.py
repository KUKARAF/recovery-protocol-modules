"""Tests for Challenge 1.0.2: Hold the Line"""

import pytest
from modules.core.tasks.clamp_value import clamp_value


class TestClampValue:
    """Test suite for clamp_value."""

    def test_within_range(self):
        assert clamp_value(5, 0, 10) == 5

    def test_above_high(self):
        assert clamp_value(15, 0, 10) == 10

    def test_below_low(self):
        assert clamp_value(-5, 0, 10) == 0

    def test_equal_to_low(self):
        assert clamp_value(0, 0, 10) == 0

    def test_equal_to_high(self):
        assert clamp_value(10, 0, 10) == 10

    def test_negative_range(self):
        assert clamp_value(-50, -10, -1) == -10

    def test_float_value(self):
        assert clamp_value(7.5, 0, 10) == 7.5

    def test_float_above_high(self):
        assert clamp_value(10.5, 0, 10) == 10

    def test_zero_width_range(self):
        assert clamp_value(100, 5, 5) == 5

    def test_value_already_matches_bound_exactly(self):
        assert clamp_value(3, 3, 8) == 3
