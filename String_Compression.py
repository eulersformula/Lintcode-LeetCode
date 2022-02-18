# Lintcode 213//Easy
# Description
# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.

# If the "compressed" string would not become smaller than the original string, your method should return the original string.

# You can assume the string has only upper and lower case letters (a-z).

# Example
# Example 1:

# Input: str = "aabcccccaaa"
# Output: "a2b1c5a3"
# Example 2:

# Input: str = "aabbcc"
# Output: "aabbcc"

class Solution:
    """
    @param original_string: a string
    @return: a compressed string
    """
    def compress(self, original_string: str) -> str:
        # write your code here
        if len(original_string) == 0:
            return original_string
        comp_str, last, cnt = original_string[0], original_string[0], 1
        for c in original_string[1:]:
            if c != last:
                comp_str += str(cnt) + c
                last = c
                cnt = 1
            else:
                cnt += 1
        comp_str += str(cnt) # THIS LINE IS EASY TO FORGET!!
        if len(comp_str) >= len(original_string):
            return original_string
        return comp_str
