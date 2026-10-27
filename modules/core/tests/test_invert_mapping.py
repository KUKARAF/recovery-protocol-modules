"""Tests for Challenge 1.0.11: Flip the Table"""

import pytest
from modules.core.tasks.invert_mapping import invert_mapping


class TestInvertMapping:
    """Test suite for invert_mapping."""

    def test_simple_mapping(self):
        assert invert_mapping({"a1": "GHOST", "a2": "ECHO"}) == {"GHOST": "a1", "ECHO": "a2"}

    def test_empty_dict(self):
        assert invert_mapping({}) == {}

    def test_single_entry(self):
        assert invert_mapping({"x": "y"}) == {"y": "x"}

    def test_integer_values(self):
        assert invert_mapping({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    def test_integer_keys(self):
        assert invert_mapping({1: "a", 2: "b"}) == {"a": 1, "b": 2}

    def test_return_type_is_dict(self):
        assert isinstance(invert_mapping({"a": "b"}), dict)

    def test_does_not_mutate_input(self):
        original = {"a": "b"}
        invert_mapping(original)
        assert original == {"a": "b"}

    def test_preserves_count(self):
        mapping = {"a": 1, "b": 2, "c": 3}
        assert len(invert_mapping(mapping)) == 3

    def test_double_inversion_restores_original(self):
        mapping = {"a": "x", "b": "y"}
        assert invert_mapping(invert_mapping(mapping)) == mapping

    def test_boolean_values(self):
        assert invert_mapping({"a": True, "b": False}) == {True: "a", False: "b"}
