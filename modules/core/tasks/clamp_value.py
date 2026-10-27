"""
Challenge 1.0.2: Hold the Line

MISSION BRIEF:
Raw sensor values can spike past what your systems can safely report.
Before anything downstream sees a number, it needs to be held inside
safe bounds - too low gets raised to the floor, too high gets capped
at the ceiling.

INSTRUCTIONS:
Implement the function to clamp a number into the inclusive range
[low, high]. Values already inside the range pass through unchanged.

EXAMPLE:
    Input:  value=12, low=0, high=10
    Output: 10

    Input:  value=-5, low=0, high=10
    Output: 0

    Input:  value=7, low=0, high=10
    Output: 7
"""


def clamp_value(value, low, high):
    """
    Clamp a number into the inclusive range [low, high].

    Args:
        value: The number to clamp (int or float)
        low: The minimum allowed value
        high: The maximum allowed value

    Returns:
        low if value < low, high if value > high, otherwise value unchanged

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Implement this function
    # Hint: two comparisons, no loop needed.
    pass
