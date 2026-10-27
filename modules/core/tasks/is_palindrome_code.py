"""
Challenge 1.0.6: Mirror Code

MISSION BRIEF:
Some access codes in AIDAN's old logs were designed to read identically
forwards and backwards, as a cheap integrity check. Your job: tell
which ones still do.

INSTRUCTIONS:
Implement the function to return whether a string is a palindrome,
ignoring letter case. Compare the exact characters - don't ignore
spaces or punctuation.

EXAMPLE:
    Input:  "GHOST"
    Output: False

    Input:  "RADAR"
    Output: True

    Input:  "Radar"
    Output: True
"""


def is_palindrome_code(code: str) -> bool:
    """
    Return whether `code` reads the same forwards and backwards,
    ignoring case.

    Args:
        code: The string to check

    Returns:
        True if the string is a case-insensitive palindrome, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # TODO: Implement this function
    # Hint: normalize case first (upper() or lower()), then compare the
    # string to its own reverse. Slicing with a step of -1 reverses a
    # string without a loop.
    pass
