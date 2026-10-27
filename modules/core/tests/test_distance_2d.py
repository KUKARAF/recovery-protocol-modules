"""Tests for Challenge 1.0.10: Triangulate"""

import pytest
from modules.core.tasks.distance_2d import distance_2d


class TestDistance2D:
    """Test suite for distance_2d."""

    def test_classic_3_4_5_triangle(self):
        assert distance_2d((0, 0), (3, 4)) == 5.0

    def test_same_point(self):
        assert distance_2d((1, 1), (1, 1)) == 0.0

    def test_horizontal_distance(self):
        assert distance_2d((0, 0), (5, 0)) == 5.0

    def test_vertical_distance(self):
        assert distance_2d((0, 0), (0, 5)) == 5.0

    def test_negative_coordinates(self):
        assert distance_2d((-3, -4), (0, 0)) == 5.0

    def test_rounds_to_two_decimals(self):
        result = distance_2d((0, 0), (1, 1))
        assert result == pytest.approx(1.41, abs=0.01)

    def test_return_type_is_float(self):
        assert isinstance(distance_2d((0, 0), (1, 1)), float)

    def test_order_independence(self):
        assert distance_2d((0, 0), (3, 4)) == distance_2d((3, 4), (0, 0))

    def test_large_coordinates(self):
        assert distance_2d((0, 0), (300, 400)) == 500.0

    def test_float_coordinates(self):
        assert distance_2d((0.0, 0.0), (3.0, 4.0)) == 5.0
