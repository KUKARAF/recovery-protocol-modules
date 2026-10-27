"""Tests for Challenge 1.0.3: All Systems Go"""

import pytest
from modules.core.tasks.all_systems_go import all_systems_go


class TestAllSystemsGo:
    """Test suite for all_systems_go."""

    def test_all_true(self):
        assert all_systems_go([True, True, True]) is True

    def test_one_false(self):
        assert all_systems_go([True, False, True]) is False

    def test_all_false(self):
        assert all_systems_go([False, False]) is False

    def test_empty_list_is_true(self):
        """Vacuous truth: nothing failed, so nothing is wrong."""
        assert all_systems_go([]) is True

    def test_single_true(self):
        assert all_systems_go([True]) is True

    def test_single_false(self):
        assert all_systems_go([False]) is False

    def test_false_at_start(self):
        assert all_systems_go([False, True, True]) is False

    def test_false_at_end(self):
        assert all_systems_go([True, True, False]) is False

    def test_return_type_is_bool(self):
        assert isinstance(all_systems_go([True, True]), bool)

    def test_large_all_true(self):
        assert all_systems_go([True] * 50) is True
