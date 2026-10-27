"""Tests for Challenge 1.0.6: Mirror Code"""

import pytest
from modules.core.tasks.is_palindrome_code import is_palindrome_code


class TestIsPalindromeCode:
    """Test suite for is_palindrome_code."""

    def test_simple_palindrome(self):
        assert is_palindrome_code("RADAR") is True

    def test_not_palindrome(self):
        assert is_palindrome_code("GHOST") is False

    def test_mixed_case_palindrome(self):
        assert is_palindrome_code("Radar") is True

    def test_single_character(self):
        assert is_palindrome_code("A") is True

    def test_two_same_characters(self):
        assert is_palindrome_code("AA") is True

    def test_two_different_characters(self):
        assert is_palindrome_code("AB") is False

    def test_empty_string(self):
        assert is_palindrome_code("") is True

    def test_all_uppercase_palindrome(self):
        assert is_palindrome_code("LEVEL") is True

    def test_longer_non_palindrome(self):
        assert is_palindrome_code("PROTOCOL") is False

    def test_return_type_is_bool(self):
        assert isinstance(is_palindrome_code("RADAR"), bool)
