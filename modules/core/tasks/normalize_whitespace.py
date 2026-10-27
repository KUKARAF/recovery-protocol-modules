"""
Challenge 1.0.5: Clean Transmission

MISSION BRIEF:
Corrupted transmissions arrive with ragged spacing - double spaces,
tabs, leading and trailing junk. Before any text can be parsed, it
needs to be cleaned down to single spaces between words, nothing more.

INSTRUCTIONS:
Implement the function to collapse any run of whitespace (spaces,
tabs, newlines) into a single space, and strip leading/trailing
whitespace entirely.

EXAMPLE:
    Input:  "  GHOST    PROTOCOL  "
    Output: "GHOST PROTOCOL"

    Input:  "ALPHA\\t\\tBETA\\nGAMMA"
    Output: "ALPHA BETA GAMMA"
"""


def normalize_whitespace(text: str) -> str:
    """
    Collapse runs of whitespace into single spaces and strip the ends.

    Args:
        text: String with irregular whitespace

    Returns:
        String with single spaces between words, no leading/trailing whitespace

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # TODO: Implement this function
    # Hint: str.split() with no arguments already treats any run of
    # whitespace as one separator and drops empty pieces. What do you
    # do with the pieces once you have them?
    pass
