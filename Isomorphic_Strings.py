# Lintcode 638//Easy//LinkedIn

# Description
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# You may assume both s and t have the same length.

# Example
# Example 1:

# Input : s = "egg", t = "add"
# Output : true 
# Explanation : 
# e -> a, g -> d.
# Example 2:

# Input : s = "foo", t = "bar"
# Output : false
# Explanation : 
# No solution.
# Example 3:

# Input : s = "paper", t = "title"
# Output : true 
# Explanation : 
# p -> t, a -> i, e -> l, r -> e.

class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    # 注意审题：No two characters may map to the same character but a character may map to itself.
    def is_isomorphic(self, s: str, t: str) -> bool:
        # write your code here
        # Questions to ask:
        # 1. Does s and t have the same length?
        if len(s) == 0:
            return True
        mapped_chars = set()
        s_to_t = dict()
        for idx in range(len(s)):
            if s[idx] not in s_to_t:
                if t[idx] in mapped_chars:
                    return False
                s_to_t[s[idx]] = t[idx]
                mapped_chars.add(t[idx])
            elif s_to_t[s[idx]] != t[idx]:
                return False
        return True
