"""
Challenge 1.0.11: Flip the Table

MISSION BRIEF:
AIDAN's lookup table maps operator IDs to callsigns, but the next
system in the recovery chain needs it the other way around - callsign
to ID. Flip it.

INSTRUCTIONS:
Implement the function to return a new dictionary with every key and
value swapped. You can assume no two keys in the input share the same
value, so the result is unambiguous.

EXAMPLE:
    Input:  {"a1": "GHOST", "a2": "ECHO"}
    Output: {"GHOST": "a1", "ECHO": "a2"}

    Input:  {}
    Output: {}
"""


def invert_mapping(mapping: dict) -> dict:
    """
    Return a new dict with keys and values swapped.

    Args:
        mapping: Dict with no duplicate values

    Returns:
        A new dict where every former value is now a key, and vice versa

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # TODO: Implement this function
    # Hint: `.items()` gives you (key, value) pairs to iterate over. A
    # dict comprehension can build the inverted dict in one line.
    pass
