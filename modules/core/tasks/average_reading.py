"""
Challenge 1.0.1: Steady the Signal

MISSION BRIEF:
Your sensor array is back online, but barely. Before you can trust any
single reading, you need to be able to average a batch of them - the
most basic act of turning noisy numbers into one steady value.

INSTRUCTIONS:
Implement the function to return the average of a list of numbers,
rounded to 2 decimal places. An empty list has no readings to average -
return 0.0 for that case.

EXAMPLE:
    Input:  [1, 2, 3, 4]
    Output: 2.5

    Input:  [10.5, 11.3, 9.8]
    Output: 10.53

    Input:  []
    Output: 0.0
"""


def average_reading(readings: list) -> float:
    """
    Average a list of numeric readings.

    Args:
        readings: List of ints and/or floats (may be empty)

    Returns:
        The average, rounded to 2 decimal places. 0.0 for an empty list.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # TODO: Implement this function
    # Hint: sum() and len() get you most of the way there - but len()
    # can be 0, and dividing by 0 crashes. Handle that case first.
    # Hint: round(x, 2) rounds to 2 decimal places.
    pass
