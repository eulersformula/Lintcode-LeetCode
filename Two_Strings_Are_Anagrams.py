#Write a method anagram(s,t) to decide if two strings are anagrams or not.

#Example:
#Given s="abcd", t="dcab", return true.

#Method 1: Sort and compare. Time complexity: O(nlog(n)). Space complexity: O(1).

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if s == None or t == None:
          return False
        
