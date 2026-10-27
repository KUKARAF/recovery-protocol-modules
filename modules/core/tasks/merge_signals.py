"""
Challenge 1.5: Merge Data Streams

MISSION BRIEF:
Two satellite arrays transmitted simultaneously for redundancy. Their
data got interleaved in transit—we need to separate and re-merge them
correctly.

You have two data streams (lists), and they need to be combined by
alternating: first element from Stream A, first from Stream B, second
from Stream A, second from Stream B... and so on.

Understanding data merging is crucial for handling distributed systems
and parallel data processing.

INSTRUCTIONS:
Take two lists of equal length and merge them by alternating elements.
Start with the first list.

EXAMPLE:
    Stream A: [1, 2, 3]
    Stream B: [10, 20, 30]
    Output:   [1, 10, 2, 20, 3, 30]

    Stream A: ['a', 'b']
    Stream B: ['x', 'y']
    Output:   ['a', 'x', 'b', 'y']

IMPORTANT:
- Both lists have equal length
- Preserve order within each stream
- Return a single merged list
"""


def merge_signals(stream_a: list, stream_b: list) -> list:
    """
    Merge two data streams by alternating elements.

    Args:
        stream_a: First data stream (list)
        stream_b: Second data stream (list of equal length)

    Returns:
        Merged list with alternating elements: A[0], B[0], A[1], B[1], ...

    Time Complexity: O(n) where n is length of each stream
    Space Complexity: O(n) for the output list
    """
    # TODO: Implement this function
    # Hint: Think about how to iterate through both lists simultaneously
    # Can you use zip() to help? Or manual indexing?
    pass
