# Lintcode 683//Medium

# Description
# Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.

# Ignore case

# Example
# Example1

# Input:
# "CatMat"
# ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
# Output: 3
# Explanation:
# we can form 3 sentences, as follows:
# "CatMat" = "Cat" + "Mat"
# "CatMat" = "Ca" + "tM" + "at"
# "CatMat" = "C" + "at" + "Mat"
# Example1

# Input:
# "a"
# []
# Output: 
# 0

# SOLUTION: RECURSION, 不符合时间要求

from typing import (
    Set,
)

class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def word_break3(self, s: str, dict: Set[str]) -> int:
        # Write your code here
        # 1. 审题未看清ignore case
        # 2. 初次写未加边界条件: 整个s在dict中为结束情况
        if len(s) == 0 or len(dict) == 0:
            return 0 
        s = s.lower()
        new_dict = set()
        for d in dict:
            new_dict.add(d.lower())
        res = 0
        for i in range(len(s)-1):
            if s[:(i+1)] in new_dict:
                res += self.word_break3(s[(i+1):], new_dict)
        if s in new_dict:
            res += 1
        return res
