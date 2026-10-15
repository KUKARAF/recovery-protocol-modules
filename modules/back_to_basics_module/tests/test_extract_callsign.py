"""Tests for Challenge 1.2: Extract the Signal"""

import pytest
from modules.back_to_basics_module.tasks.extract_callsign import extract_callsign


class TestExtractCallsign:
    """Test suite for callsign extraction."""

    def test_simple_extraction(self):
        """Test basic callsign extraction."""
        assert extract_callsign("###GHOST###") == ["GHOST"]

    def test_multiple_callsigns(self):
        """Test extracting multiple callsigns."""
        assert extract_callsign("###GHOST###PROTOCOL+++ERROR") == ["GHOST", "PROTOCOL", "ERROR"]

    def test_ignores_lowercase(self):
        """Test that lowercase letters are treated as noise."""
        assert extract_callsign("GHOSTprotocol") == ["GHOST"]

    def test_ignores_numbers(self):
        """Test that numbers break callsigns."""
        assert extract_callsign("GHOST123PROTOCOL") == ["GHOST", "PROTOCOL"]

    def test_ignores_spaces(self):
        """Test that spaces break callsigns."""
        assert extract_callsign("GHOST PROTOCOL") == ["GHOST", "PROTOCOL"]

    def test_minimum_length_3(self):
        """Test minimum length requirement (3 chars)."""
        assert extract_callsign("AB ABC ABCD") == ["ABC", "ABCD"]

    def test_maximum_length_15(self):
        """Test maximum length requirement (15 chars)."""
        result = extract_callsign("TOOLONGCALLSIGN123 TOOLONGCALLSI")
        assert result == ["TOOLONGCALLSI"]

    def test_too_short(self):
        """Test that callsigns shorter than 3 chars are ignored."""
        assert extract_callsign("A AB ABC") == ["ABC"]

    def test_too_long(self):
        """Test that callsigns longer than 15 chars are ignored."""
        result = extract_callsign("THISISAREALLYLONGCALLSIGN VALID")
        assert result == ["VALID"]

    def test_special_characters_as_noise(self):
        """Test special characters are noise."""
        result = extract_callsign("GHOST!@#$%PROTOCOL^&*()")
        assert result == ["GHOST", "PROTOCOL"]

    def test_empty_string(self):
        """Test empty string."""
        assert extract_callsign("") == []

    def test_no_valid_callsigns(self):
        """Test string with no valid callsigns."""
        assert extract_callsign("123 456 !@# abc def") == []

    def test_mixed_valid_invalid(self):
        """Test mixture of valid and invalid."""
        result = extract_callsign("123GHOST456PROTOCOL789ECHO")
        assert result == ["GHOST", "PROTOCOL", "ECHO"]

    def test_preserves_order(self):
        """Test that callsigns are returned in order found."""
        result = extract_callsign("ZEBRA ALPHA GAMMA")
        assert result == ["ZEBRA", "ALPHA", "GAMMA"]

    def test_repeated_callsigns(self):
        """Test repeated callsigns are returned separately."""
        result = extract_callsign("GHOST xxx GHOST")
        assert result == ["GHOST", "GHOST"]

    def test_boundary_15_chars(self):
        """Test exactly 15 character callsign (should be valid)."""
        callsign_15 = "A" * 15
        result = extract_callsign(callsign_15)
        assert result == [callsign_15]

    def test_boundary_16_chars(self):
        """Test 16 character callsign (should be invalid)."""
        callsign_16 = "A" * 16
        result = extract_callsign(callsign_16)
        assert result == []
