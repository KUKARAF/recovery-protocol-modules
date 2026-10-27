"""
Challenge 1.0.10: Triangulate

MISSION BRIEF:
Two signal sources reported their positions as (x, y) coordinates.
Before AIDAN can triangulate anything, it needs to know how far apart
they actually are.

INSTRUCTIONS:
Implement the function to compute the straight-line (Euclidean)
distance between two (x, y) points, rounded to 2 decimal places.

EXAMPLE:
    Input:  point_a=(0, 0), point_b=(3, 4)
    Output: 5.0

    Input:  point_a=(1, 1), point_b=(1, 1)
    Output: 0.0
"""


def distance_2d(point_a: tuple, point_b: tuple) -> float:
    """
    Compute the Euclidean distance between two (x, y) points.

    Args:
        point_a: A 2-element tuple (x, y)
        point_b: A 2-element tuple (x, y)

    Returns:
        The distance between the two points, rounded to 2 decimal places

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # TODO: Implement this function
    # Hint: unpack both tuples into x/y names. The distance formula is
    # sqrt((x2-x1)**2 + (y2-y1)**2) - the math module has a sqrt function,
    # or you can raise to the power of 0.5 instead.
    pass
