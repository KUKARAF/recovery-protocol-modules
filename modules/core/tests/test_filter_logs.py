"""Tests for Challenge 1.4: Filter the Noise"""

import pytest
from modules.core.tasks.filter_logs import filter_logs


class TestFilterLogs:
    """Test suite for log filtering."""

    def test_simple_error_extraction(self):
        """Test basic error extraction."""
        logs = ["[SYS] Boot", "[ERR] NullRef"]
        assert filter_logs(logs) == ["NullRef"]

    def test_multiple_errors(self):
        """Test extracting multiple errors."""
        logs = ["[SYS] Boot", "[ERR] NullRef", "[SYS] Init", "[ERR] Overflow"]
        assert filter_logs(logs) == ["NullRef", "Overflow"]

    def test_ignores_sys_messages(self):
        """Test that SYS messages are ignored."""
        logs = ["[SYS] Started", "[SYS] Running", "[SYS] Stopped"]
        assert filter_logs(logs) == []

    def test_empty_list(self):
        """Test empty log list."""
        assert filter_logs([]) == []

    def test_only_errors(self):
        """Test list with only error messages."""
        logs = ["[ERR] Error1", "[ERR] Error2", "[ERR] Error3"]
        assert filter_logs(logs) == ["Error1", "Error2", "Error3"]

    def test_preserves_order(self):
        """Test that order is preserved."""
        logs = ["[ERR] First", "[SYS] Mid", "[ERR] Second"]
        assert filter_logs(logs) == ["First", "Second"]

    def test_case_sensitive(self):
        """Test that matching is case-sensitive."""
        logs = ["[ERR] Valid", "[err] Invalid", "[Err] Invalid"]
        assert filter_logs(logs) == ["Valid"]

    def test_lowercase_ignored(self):
        """Test lowercase error prefix is ignored."""
        logs = ["[err] should be ignored"]
        assert filter_logs(logs) == []

    def test_mixed_case_ignored(self):
        """Test mixed case error prefix is ignored."""
        logs = ["[Err] should be ignored", "[eRr] should be ignored"]
        assert filter_logs(logs) == []

    def test_removes_prefix_correctly(self):
        """Test that [ERR] prefix is removed correctly."""
        logs = ["[ERR] This is an error message"]
        result = filter_logs(logs)
        assert result == ["This is an error message"]
        assert "[ERR]" not in result[0]

    def test_error_message_with_spaces(self):
        """Test error message that contains spaces."""
        logs = ["[ERR] Multiple word error message"]
        assert filter_logs(logs) == ["Multiple word error message"]

    def test_error_message_empty_after_prefix(self):
        """Test error message with nothing after prefix."""
        logs = ["[ERR] "]
        assert filter_logs(logs) == [" "]

    def test_error_message_with_brackets(self):
        """Test error message containing brackets."""
        logs = ["[ERR] Error [CODE: 42]"]
        assert filter_logs(logs) == ["Error [CODE: 42]"]

    def test_no_prefix_at_all(self):
        """Test message without any prefix."""
        logs = ["This is an error", "[ERR] This is too"]
        assert filter_logs(logs) == ["This is too"]

    def test_partial_prefix_match(self):
        """Test that partial prefix doesn't match."""
        logs = ["[ER] incomplete", "[ERRO] too long", "[ERR] exact"]
        assert filter_logs(logs) == ["exact"]

    def test_whitespace_in_prefix(self):
        """Test that spaces in prefix break the match."""
        logs = ["[ ERR] spaced", "[ERR ] spaced", "[ERR] correct"]
        assert filter_logs(logs) == ["correct"]

    def test_alternating_logs(self):
        """Test alternating SYS and ERR messages."""
        logs = ["[SYS] 1", "[ERR] 2", "[SYS] 3", "[ERR] 4", "[SYS] 5"]
        assert filter_logs(logs) == ["2", "4"]

    def test_large_log_list(self):
        """Test performance with large list."""
        logs = ["[SYS] msg"] * 500 + ["[ERR] error"] * 500
        result = filter_logs(logs)
        assert len(result) == 500
        assert all(msg == "error" for msg in result)
