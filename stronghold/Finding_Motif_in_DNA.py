def find_substring_locations(s: str, t: str) -> list[int]:
    """
    Finds all locations of string t as a substring of string s.

    Args:
        s: The main DNA string.
        t: The substring to find.

    Returns:
        A list of 1-indexed starting positions of t in s.
    """
    locations = []
    len_s = len(s)
    len_t = len(t)

    # Iterate through s up to the point where t can still fit
    for i in range(len_s - len_t + 1):
        # Extract a substring of s with the same length as t
        current_substring = s[i : i + len_t]

        # Compare the extracted substring with t
        if current_substring == t:
            # If they match, record the 1-indexed starting position
            locations.append(i + 1)

    return locations

# highlighting t in s
def highlight_substring(s: str, t: str) -> str:
    """
    Highlights the substring t in the string s by surrounding it with square brackets.

    Args:
        s: The main DNA string.
        t: The substring to highlight.

    Returns:
        The string with t highlighted.
    """
    highlighted = s.replace(t, f"[{t}]")
    return highlighted

# Sample Dataset
s = "GGAGTCGGATGAGTCGGAGCTAGTCGGAGTTAGTCGGAAGCAGTCGGACACTTAGTCGGAAGTCGGAAGTCGGATTCCGAGTCGGATAGCACAGTCGGAAGTCGGAAAAGTCGGATTTGCTTTGTAGTCGGACCTCGAGTCGGACAGTCGGAAAGTCGGACCCATAGTCGGAAGTCGGAAAGTCGGAAGTCGGAATCAGTCGGACAGTCGGAGATCCACAGTCGGACAAGTCGGATAATGATGAAAGTCGGAGAAAGTCGGATAAGTCGGATAGTCGGAAAGCCGAAGTCGGACAGTCGGAAGTCGGAAGAGTCGGATCGCAGTCGGAAGTCGGAGACAGTCGGACCGAGTCGGATAGTCGGACCTAGTCGGAAGTCTTAGTCGGACAAGTCGGATTGCAGTCGGAAGTCGGATTAGTCGGAGAAAGAGTCGGAAAGTCGGATTAGTCGGACAGTCGGAGAGTCGGACTAGTCGGACATGTAGTCGGAAGTCGGATAAAGTCGGAGCAGTCGGATGCATAGTCGGAAGTCGGAAGTCGGATCAAGTCGGAGAGTCGGATCCGTCAAGTCGGAAAGTCGGACAGTCGGAACCAGTCGGAAGTCGGACATTACAAGGTAGTCGGATGCAAGTCGGACAGTCGGAGTGAGTCGGAAGTCGGAGTCAGCGTACATGAAGTCGGAATTGCCATAAGTCGGAATCTAGTCGGAAGTCGGAAGTCGGAACTCTTAGTCGGATGGTAAAGTCGGACGGAGTCGGAAATAGTCGGATCTGAGTCGGACCTAGTCGGATACAGCCCCCCGAGTAGTCGGATTAAGTCGGAGCCAGTCGGAGAAACAGTCGGAAGTCGGATGCAAGTCGGAGAGACGAGTCGGATGGGAGAGTCGGATGGCCAAGTCGGAAAGTCGGATAAGTCGGATAGTCGGACACAACGACTTAGAGTCGGA"

t = "AGTCGGAAG"

# Find and print the locations
output_locations = find_substring_locations(s, t)
print(*output_locations)

# Highlight and print the substring
highlighted_string = highlight_substring(s, t)
print(highlighted_string)