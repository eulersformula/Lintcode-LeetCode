# Lintcode 1905//Easy
# Description
# Given the two strings str and sub, your task is to completely delete the characters in str that exist in sub.

# String contains spaces
# 1\leq len(str),len(sub) \leq 10^5
 

# Example
# Example 1:

# Input:  
# str="They are students"，sub="aeiou"
# Output: 
# "Thy r stdnts"

# SOLUTION 1: 
class Solution:
    """
    @param str: The first string given
    @param sub: The given second string
    @return: Returns the deleted string
    """
    def character_deletion(self, str: str, sub: str) -> str:
        # write your code here
        if len(str) == 0 or len(sub) == 0:
            return str
        sub = set(sub) # 如果没有取set会导致 TIME LIMIT EXCEEDED
        out = ''
        for c in str:
            if c in sub:
                continue
            out += c
        return out
 

