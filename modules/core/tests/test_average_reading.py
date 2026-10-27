"""Tests for Challenge 1.0.1: Steady the Signal"""

import pytest
from modules.core.tasks.average_reading import average_reading


class TestAverageReading:
    """Test suite for average_reading."""

    def test_simple_integers(self):
        assert average_reading([1, 2, 3, 4]) == 2.5

    def test_floats(self):
        assert average_reading([10.5, 11.3, 9.8]) == pytest.approx(10.53, abs=0.01)

    def test_empty_list(self):
        assert average_reading([]) == 0.0

    def test_single_value(self):
        assert average_reading([7]) == 7.0

    def test_rounds_to_two_decimals(self):
        result = average_reading([1, 2])
        assert result == 1.5

    def test_rounding_behavior(self):
        result = average_reading([1, 1, 1, 1, 1, 2])
        assert result == pytest.approx(1.17, abs=0.01)

    def test_negative_numbers(self):
        assert average_reading([-2, -4, -6]) == -4.0

    def test_mixed_sign(self):
        assert average_reading([-5, 5, 10]) == pytest.approx(3.33, abs=0.01)

    def test_return_type_is_float(self):
        assert isinstance(average_reading([1, 2, 3]), float)

    def test_large_list(self):
        assert average_reading(list(range(1, 101))) == 50.5
