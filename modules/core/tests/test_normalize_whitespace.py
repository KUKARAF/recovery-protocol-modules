"""Tests for Challenge 1.0.5: Clean Transmission"""

import pytest
from modules.core.tasks.normalize_whitespace import normalize_whitespace


class TestNormalizeWhitespace:
    """Test suite for normalize_whitespace."""

    def test_double_spaces(self):
        assert normalize_whitespace("GHOST    PROTOCOL") == "GHOST PROTOCOL"

    def test_leading_trailing_spaces(self):
        assert normalize_whitespace("  GHOST PROTOCOL  ") == "GHOST PROTOCOL"

    def test_tabs(self):
        assert normalize_whitespace("ALPHA\t\tBETA") == "ALPHA BETA"

    def test_newlines(self):
        assert normalize_whitespace("ALPHA\nBETA\nGAMMA") == "ALPHA BETA GAMMA"

    def test_mixed_whitespace(self):
        assert normalize_whitespace("  ALPHA\t BETA\n GAMMA  ") == "ALPHA BETA GAMMA"

    def test_already_clean(self):
        assert normalize_whitespace("ALPHA BETA") == "ALPHA BETA"

    def test_empty_string(self):
        assert normalize_whitespace("") == ""

    def test_only_whitespace(self):
        assert normalize_whitespace("   \t\n  ") == ""

    def test_single_word(self):
        assert normalize_whitespace("  GHOST  ") == "GHOST"

    def test_return_type_is_str(self):
        assert isinstance(normalize_whitespace("A B"), str)
