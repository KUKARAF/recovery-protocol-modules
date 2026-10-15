"""
Challenge 1.2: Extract the Signal

MISSION BRIEF:
Embedded in AIDAN's transmission are operator callsigns—identities of the
people who were there at the end. They're buried in corruption—surrounded by
noise characters, special symbols, and debris. Your job: extract only the
valid callsigns.

A valid callsign:
  - Contains ONLY uppercase letters (A-Z)
  - Is between 3 and 15 characters long
  - Cannot have spaces or numbers

Finding the signal in the noise is how we rebuild trust in the data.

INSTRUCTIONS:
Implement the function to find all valid callsigns in a given string.
Return them in the order they appear.

EXAMPLE:
    Input:  "###GHOST###PROTOCOL+++ERROR"
    Output: ["GHOST", "PROTOCOL", "ERROR"]

    Input:  "123invalid ABC VALID xyz 12X"
    Output: ["VALID"]
"""


def extract_callsign(data: str) -> list:
    """
    Extract valid callsigns from a corrupted transmission.

    A valid callsign:
    - Contains only uppercase letters (A-Z)
    - Is 3-15 characters long
    - No spaces, numbers, or special characters

    Args:
        data: String containing mixed text and noise

    Returns:
        List of valid callsigns in order found

    Time Complexity: O(n) where n is length of input string
    Space Complexity: O(m) where m is number of valid callsigns found
    """
    # TODO: Implement this function
    # Hint: Think about what makes a character "valid" for a callsign
    # Then iterate through the string looking for sequences of valid characters
    pass
