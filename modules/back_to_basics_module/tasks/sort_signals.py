"""
Challenge 1.1: Sort the Chaos

MISSION BRIEF:
AIDAN's final transmission came through in fragmented packets. Each packet
has a sequence number, but they arrived scrambled. Your task: restore the
original order by sorting the packets.

This is the foundation of data processing: learning to organize chaos into
meaningful structure.

INSTRUCTIONS:
Implement the function below to sort a list of packet IDs (integers) in
ascending order. The function should handle both positive and negative numbers.

Do NOT use external libraries. Python's built-in sort is allowed.

EXAMPLE:
    Input:  [42, 3, 17, 9, 1]
    Output: [1, 3, 9, 17, 42]

    Input:  [-5, 10, 0, -2, 8]
    Output: [-5, -2, 0, 8, 10]
"""


def sort_signals(packets: list) -> list:
    """
    Sort a list of packet IDs in ascending order.

    Args:
        packets: List of integers (can be positive, negative, or zero)

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n log n) expected
    Space Complexity: O(n)
    """
    return sorted(packets)
