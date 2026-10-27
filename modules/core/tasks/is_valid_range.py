"""
Challenge 1.0.4: Within Tolerance

MISSION BRIEF:
A reading is only trustworthy if it falls within the tolerance band
AIDAN was calibrated for. Anything outside it, even by a hair, is noise.

INSTRUCTIONS:
Implement the function to return whether a value falls within the
inclusive range [low, high].

EXAMPLE:
    Input:  value=5, low=0, high=10
    Output: True

    Input:  value=10, low=0, high=10
    Output: True

    Input:  value=11, low=0, high=10
    Output: False
"""


def is_valid_range(value, low, high) -> bool:
    """
    Return whether value falls within the inclusive range [low, high].

    Args:
        value: The number to check
        low: The minimum allowed value
        high: The maximum allowed value

    Returns:
        True if low <= value <= high, False otherwise

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Implement this function
    # Hint: this is a single boolean expression. Return it directly -
    # don't wrap it in an if/else that just returns True or False.
    pass
