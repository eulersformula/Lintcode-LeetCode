# You are given a string s consisting only of lowercase English letters.

# In one move, you can select any two adjacent characters of s and swap them.

# Return the minimum number of moves needed to make s a palindrome.

# Note that the input will be generated such that s can always be converted to a palindrome.

# Example 1:

# Input: s = "aabb"
# Output: 2
# Explanation:
# We can obtain two palindromes from s, "abba" and "baab". 
# - We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
# - We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
# Thus, the minimum number of moves needed to make s a palindrome is 2.
# Example 2:

# Input: s = "letelt"
# Output: 2
# Explanation:
# One of the palindromes we can obtain from s in 2 moves is "lettel".
# One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
# Other palindromes such as "tleelt" can also be obtained in 2 moves.
# It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 
# Constraints:
# 1 <= s.length <= 2000
# s consists only of lowercase English letters.
# s can be converted to a palindrome using a finite number of moves.

# 最一开始答案：找最近的和头或尾一样的换到尾或头。TLE
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 2:
            return 0
        if s[0] == s[-1]:
            return self.minMovesToMakePalindrome(s[1:-1])
        # make the first s[0] from the end to the end
        idx = 0
        left_possible = False
        while s[idx] != s[-1]:
            idx += 1
        if idx < len_s - 1:
            left_possible = True
            n_swaps_left = idx
            n_total_left = n_swaps_left + \
                self.minMovesToMakePalindrome(s[:idx]+s[(idx+1):-1])
        idx = len_s - 1
        right_possible = False
        while s[idx] != s[0]:
            idx -= 1
        if idx > 0:
            right_possible = True
            n_swaps_right = len_s - 1 - idx
            n_total_right = n_swaps_right + \
                self.minMovesToMakePalindrome(s[1:idx]+s[(idx+1):])
        if left_possible and right_possible:
            return min(n_total_left, n_total_right)
        if left_possible:
            return n_total_left
        return n_total_right
 
