# Lintcode 1283//Easy

# Description
# Write a function that takes a string as input and returns the string reversed.

# Example
# Example 1：

# Input："hello"
# Output："olleh"
# Example 2：

# Input："hello world"
# Output："dlrow olleh"

# SOLUTION 1:内置函数

class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverse_string(self, s: str) -> str:
        # write your code here
        return s[::-1]
  
