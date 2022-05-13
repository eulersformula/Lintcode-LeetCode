# Lintcode 1821//Easy//Microsoft

# Description
# We are given a string SS of length NN consisting only of letters A and/or B. Our goal is to obtain a string in the format A...AB...B. (all letters A occur before all letters B) by deleting some letters from SS. In particular, strings consisting only of letters A or only of letters B fit this format.

# Write a function that, given a string SS, return the minimum number of letters that need to be deleted from SS in order to obtain a string in the above format.

# N is an integer within the range [1,100000];
# string SS consists only of the characters A and/or B.
# Example
# Example 1

# Input: "BAAABAB"
# Output: 2
# Explanation: We can obtain "AAABB" by deleting the first occurrence of 'B' and the last occurrence of 'A'.
# Example 2

# Input: "BBABAA"
# Output: 3
# Explanation: We can delete all occurrences of 'A' or 'B'.
# Example 3

# Input: "AABBBB"
# Output: 0
# Explanation: We do not have to delete any letters, because the given string is already in the expected format.

# T: O(n); S: O(1)

class Solution:
    """
    @param s: the string
    @return: Min Deletions To Obtain String in Right Format
    """
    def min_deletions_to_obtain_string_in_right_format(self, s: str) -> int:
        # write your code here
        # Questions to ask:
        # 1. Can s be empty? If so, what should be returned?
        if len(s) <= 1:
            return 0
        num_A, num_B = 0, 0
        for v in s:
            if v == 'A':
                num_A += 1
            else:
                num_B += 1
        if num_A == 0 or num_B == 0:
            return 0
        idx = 0 # either last A or first B
        num_A_r, num_B_l = num_A, 0
        res = None
        while idx < len(s):
            if s[idx] == 'A':
                num_A_r -= 1
            cur_res = num_A_r + num_B_l
            if res is None or cur_res < res:
                res = cur_res
            if s[idx] == 'B':
                num_B_l += 1
            idx += 1
        return res
 
  # 需要添加解：One Pass; DP
