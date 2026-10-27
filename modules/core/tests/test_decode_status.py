"""Tests for Challenge 1.3: Decode System Status"""

import pytest
from modules.core.tasks.decode_status import decode_status


class TestDecodeStatus:
    """Test suite for status decoding."""

    def test_simple_single_status(self):
        """Test single status type."""
        assert decode_status("SSSS") == {"S": 4}

    def test_mixed_statuses(self):
        """Test mixed status codes."""
        result = decode_status("SOFUSOFF")
        assert result == {"S": 2, "O": 2, "F": 2, "U": 1}

    def test_all_status_types(self):
        """Test all four status types present."""
        result = decode_status("SOFU")
        assert result == {"S": 1, "O": 1, "F": 1, "U": 1}

    def test_empty_string(self):
        """Test empty string."""
        assert decode_status("") == {}

    def test_ignores_invalid_characters(self):
        """Test that invalid characters are ignored."""
        result = decode_status("S1O2F3U")
        assert result == {"S": 1, "O": 1, "F": 1, "U": 1}

    def test_ignores_lowercase(self):
        """Test that lowercase versions are ignored."""
        result = decode_status("SsoOfFuU")
        assert result == {"S": 1, "O": 1, "F": 1, "U": 1}

    def test_lowercase_not_counted(self):
        """Verify lowercase is truly not counted."""
        result = decode_status("sofu")
        assert result == {}

    def test_ignores_special_chars(self):
        """Test special characters are ignored."""
        result = decode_status("S!O@F#U$")
        assert result == {"S": 1, "O": 1, "F": 1, "U": 1}

    def test_large_count(self):
        """Test with large number of same status."""
        result = decode_status("O" * 1000)
        assert result == {"O": 1000}

    def test_mixed_with_noise(self):
        """Test real-world corrupted data."""
        result = decode_status("S0O1F2U3S4O5")
        assert result == {"S": 2, "O": 2, "F": 1, "U": 1}

    def test_only_one_status_type_with_noise(self):
        """Test only one valid status amid noise."""
        result = decode_status("123XXXYYYOOO456")
        assert result == {"O": 3}

    def test_return_type_is_dict(self):
        """Verify return type is dictionary."""
        result = decode_status("SOFU")
        assert isinstance(result, dict)

    def test_values_are_integers(self):
        """Verify all counts are integers."""
        result = decode_status("SOFUSOFF")
        for count in result.values():
            assert isinstance(count, int)

    def test_no_extra_keys(self):
        """Verify only valid statuses are in result."""
        result = decode_status("SOF")
        assert set(result.keys()).issubset({"S", "O", "F", "U"})
        assert "U" not in result  # U doesn't appear, so shouldn't be in dict

    def test_whitespace_handling(self):
        """Test whitespace is ignored."""
        result = decode_status("S O F U")
        assert result == {"S": 1, "O": 1, "F": 1, "U": 1}

    def test_order_independence(self):
        """Verify order of input doesn't matter for counts."""
        result1 = decode_status("SOFUSOFF")
        result2 = decode_status("FFOUSUSOF")
        assert result1 == result2
