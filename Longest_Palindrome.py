# Lintcode 627//Easy//Google//Amazon

# Description
# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Assume the length of given string will not exceed 100000.

# Example
# Example 1:

# Input : s = "abccccdd"
# Output : 7
# Explanation :
# One longest palindrome that can be built is "dccaccd", whose length is `7`.

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        if len(s) == 0: # FORGOT THIS SPECIAL CASE
            return 0
        letter_counts = dict()
        for l in s:
            if l not in letter_counts:
                letter_counts[l] = 0
            letter_counts[l] += 1
        res = 0
        n_odd = 0
        for (l, c) in letter_counts.items():
            res += c
            if c % 2 != 0:
                n_odd += 1
        if n_odd > 0: # 这一行初次提交未考虑
            res -= (n_odd - 1)
        return res
 
# 补充其他两个solution
