"""
Challenge 1.0.8: Packet Framing

MISSION BRIEF:
The transmission channel can only carry so much at once. Before
anything goes out, a long list of values has to be broken into fixed-
size packets - and the last one, if it doesn't divide evenly, just
carries whatever's left.

INSTRUCTIONS:
Implement the function to split a list into chunks of `size` elements
each. If the list doesn't divide evenly, the last chunk is shorter.
Assume size is a positive integer.

EXAMPLE:
    Input:  items=[1, 2, 3, 4, 5], size=2
    Output: [[1, 2], [3, 4], [5]]

    Input:  items=[1, 2, 3, 4], size=2
    Output: [[1, 2], [3, 4]]

    Input:  items=[], size=3
    Output: []
"""


def chunk_list(items: list, size: int) -> list:
    """
    Split a list into chunks of `size` elements, last chunk possibly shorter.

    Args:
        items: The list to split
        size: Chunk size (positive integer)

    Returns:
        List of chunks (each a list), covering all of `items` in order

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # TODO: Implement this function
    # Hint: slicing a list out of bounds doesn't raise an error - it
    # just returns however much is actually there. range(start, stop, step)
    # can walk the start index of each chunk for you.
    pass
