# Lintcode 1887//Easy

# Description
# Given a string, you can get a new string by manipulating the same consecutive characters in the string.
# You are only allowed to do the following:
# Keep 1 or 2 characters of the same character whose continuous times are greater than or equal to 2, and delete the rest.

# You have to make sure that there are no more than two consecutive identical characters in the new string.
# If the input string meets the requirements, you don't need to do anything with it.

# The length of the world is between [1,35].

# Example
# Example 1:

# Input: 
# S = "helllllooo"
# Output: 
# 4
# Explanation: 
# The answers are "hello", "helo","heloo","helloo"
# Example 2:

# Input: 
# S = "bbaa"
# Output: 
# 4
# Explanation: 
# The answers are "bbaa", "bba","baa","ba"

class Solution:
    """
    @param s: the string
    @return: The numbers of strings
    """
    def stretch_word(self, s: str) -> int:
        # write your code here
        # Question to ask: can s be empty?
        cur_s, cur_n = s[0], 1
        idx = 1
        chars_multi = 0
        while idx < len(s):
            if s[idx] == cur_s:
                cur_n += 1
            else:
                if cur_n > 1:
                    chars_multi += 1
                cur_s = s[idx]
                cur_n = 1
            idx += 1
        # 易错点：while loop often requires a after-loop check
        if cur_n > 1:
            chars_multi += 1
        return 2 ** chars_multi

# Time complexity: O(n); Space complexity: O(1)
