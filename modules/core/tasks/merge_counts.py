"""
Challenge 1.0.12: Combine the Tallies

MISSION BRIEF:
Two separate monitoring stations each kept their own tally of status
codes seen. Before AIDAN can report a single number, those two tallies
need to be combined into one - matching keys add together, keys that
only exist in one side carry over unchanged.

INSTRUCTIONS:
Implement the function to merge two dictionaries of counts. For a key
that appears in both, sum the values. For a key that appears in only
one, keep its value as-is.

EXAMPLE:
    Input:  counts_a={"S": 3, "O": 1}, counts_b={"S": 2, "F": 5}
    Output: {"S": 5, "O": 1, "F": 5}

    Input:  counts_a={}, counts_b={"S": 1}
    Output: {"S": 1}
"""


def merge_counts(counts_a: dict, counts_b: dict) -> dict:
    """
    Merge two count dictionaries, summing values for shared keys.

    Args:
        counts_a: First dict of counts
        counts_b: Second dict of counts

    Returns:
        A new dict with every key from both inputs, summed where they overlap

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    # TODO: Implement this function
    # Hint: start from a copy of one dict, then walk the other one's
    # items and add each value in - dict.get(key, 0) gives you a safe
    # default when the key isn't there yet.
    pass
