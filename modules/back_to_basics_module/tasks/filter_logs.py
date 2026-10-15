"""
Challenge 1.4: Filter the Noise

MISSION BRIEF:
AIDAN's logs are mixed—system messages ([SYS]) and error traces ([ERR]).
System messages are routine. Errors tell us what went wrong.

Your task: extract ONLY the error messages, remove the [ERR] prefix,
and return the cleaned error text.

This teaches you data filtering and cleaning—essential when working
with real-world logs and telemetry.

INSTRUCTIONS:
Filter a list of log lines, keeping only those that start with [ERR],
and remove the [ERR] prefix from each.

EXAMPLE:
    Input:  ["[SYS] Boot", "[ERR] NullRef", "[SYS] Init", "[ERR] Overflow"]
    Output: ["NullRef", "Overflow"]

IMPORTANT:
- Case sensitive: only [ERR], not [err]
- Preserve the order of messages
- Return a list of cleaned error messages
"""


def filter_logs(logs: list) -> list:
    """
    Extract and clean error messages from a mixed log list.

    Args:
        logs: List of log line strings, with [SYS] or [ERR] prefixes

    Returns:
        List of error messages with [ERR] prefix removed

    Time Complexity: O(n) where n is number of log lines
    Space Complexity: O(m) where m is number of error lines
    """
    # TODO: Implement this function
    # Hint: Use list filtering/comprehension
    # Remember to remove the [ERR] prefix from each line
    pass
