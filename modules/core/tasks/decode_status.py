"""
Challenge 1.3: Decode System Status

MISSION BRIEF:
Each satellite in the Grid reports its status in a single character:
  S = Standby (waiting for activation)
  O = Online (operational)
  F = Failed (beyond recovery)
  U = Unknown (communication lost)

You have a string of status codes from all satellites. Your task: count
how many systems are in each state.

Understanding the aggregate health of your systems is critical for
prioritizing recovery efforts.

INSTRUCTIONS:
Parse the status string and return a dictionary with counts for each status.

EXAMPLE:
    Input:  "SOFUSOFF"
    Output: {"S": 2, "O": 2, "F": 2, "U": 1}

IMPORTANT:
- Ignore any characters that are not S, O, F, or U
- Return counts only for statuses that exist in the input
- This must run in O(n) time complexity
"""


def decode_status(status_string: str) -> dict:
    """
    Count the frequency of each satellite status.

    Args:
        status_string: String containing status codes (S/O/F/U)

    Returns:
        Dictionary with counts: {"S": int, "O": int, "F": int, "U": int}
        Only includes statuses that appear in the input.

    Time Complexity: O(n) where n is length of input string
    Space Complexity: O(1) since dictionary has max 4 keys
    """
    # TODO: Implement this function
    # Hint: Use a dictionary to accumulate counts
    # Remember to only count valid status codes
    pass
