"""
Challenge 1.0.3: All Systems Go

MISSION BRIEF:
Before AIDAN commits to any action, every subsystem check must report
True. One False anywhere in the list means the whole launch is a no-go.

INSTRUCTIONS:
Implement the function to return True only if every value in the list
is True. An empty list of checks means nothing failed - return True.

EXAMPLE:
    Input:  [True, True, True]
    Output: True

    Input:  [True, False, True]
    Output: False

    Input:  []
    Output: True
"""


def all_systems_go(checks: list) -> bool:
    """
    Return True only if every value in `checks` is True.

    Args:
        checks: List of booleans (may be empty)

    Returns:
        True if every check passed (or the list is empty), False if any failed

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # TODO: Implement this function
    # Hint: you can loop and bail out the moment you see a False, or
    # think about what built-in function does exactly this already.
    # Hint: think carefully about the empty-list case - is "nothing
    # failed" the same thing as "everything passed"?
    pass
