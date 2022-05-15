# Lintcode 891//Medium
# Leetcode 680//Easy

# Description
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.)

# The string will only contain lowercase characters.
# The maximum length of the string is 50000.
# Example
# Example 1:

# Input: s = "aba"
# Output: true
# Explanation: Originally a palindrome.
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: Delete 'b' or 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
# Explanation: Deleting any letter can not make it a palindrome.

class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def real_valid_palindrome(self, s:str) -> bool:
        if len(s) == 0:
            return True
        st, ed = 0, len(s)-1
        while st < ed:
            if s[st] != s[ed]:
                return False
            st += 1
            ed -= 1
        return True

    def valid_palindrome(self, s: str) -> bool:
        # Write your code here
        if len(s) == 0:
            return True
        st, ed = 0, len(s)-1
        while st < ed:
            if s[st] == s[ed]:
                st += 1
                ed -= 1
            # now st != ed
            else:
                return self.real_valid_palindrome(s[st:ed]) or \
                self.real_valid_palindrome(s[(st+1):(ed+1)])
        return True
   
