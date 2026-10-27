"""
Challenge 1.0.7: Echoes in the Log

MISSION BRIEF:
Some entries in AIDAN's packet log were transmitted more than once -
echoes from a system that couldn't tell if its first attempt got
through. Find every value that repeats.

INSTRUCTIONS:
Implement the function to return the values that appear more than once
in the list, each listed only once, in the order their first repeat is
detected (i.e. the order in which you discover "I've seen this before").

EXAMPLE:
    Input:  [1, 2, 3, 2, 4, 1]
    Output: [2, 1]
    (2 repeats first when the second 2 is seen, then 1 repeats)

    Input:  [5, 6, 7]
    Output: []

    Input:  [9, 9, 9]
    Output: [9]
    (9 only gets added once, even though it repeats twice)
"""


def find_duplicates(items: list) -> list:
    """
    Return values that appear more than once, each listed once, in the
    order their first repeat is detected.

    Args:
        items: List of hashable values (may contain duplicates)

    Returns:
        List of values that occurred more than once, no repeats in the output

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # TODO: Implement this function
    # Hint: you need to track two things as you scan: which values
    # you've seen before at all, and which ones you've already added to
    # your result (so a value that repeats 3+ times doesn't get added
    # more than once).
    pass
