# Leetcode 214//Hard
# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"
 

# Constraints:

# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.

# Solution 1: T: O(n^2); S: O(1). TLE

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def shortestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s <= 1:
            return s
        target = 0
        for idx in range(len_s, 0, -1):
            if self.isPalindrome(s[:idx]):
                target = idx
                break
        return s[target:][::-1] + s[:target] + s[target:]
