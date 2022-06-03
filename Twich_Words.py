# Lintcode 1401//Easy//Google

# Description
# A normal word never contains two or more consecutive letters. We call a substring is a twitch if three or more letters in the word are consecutive. Now given a word and output the start points and the end points of all the twitch from left to right.

# The input string length is n, n <= 100000.
# Example
# Example1

# Input: str = "whaaaaatttsup"
# Output: [[2,6],[7,9]]
# Explanation: 
# "aaaa" and "ttt" are twitching letters, and output their starting and ending points.
# Example2

# Input: str = "whooooisssbesssst"
# Output: [[2,5],[7,9],[12,15]]
# Explanation: 
# "ooo" and "sss" and "ssss" are twitchy letters, output their start and end points. ending points.

from typing import (
    List,
)

class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitch_words(self, str: str) -> List[List[int]]:
        # Write your code here
        if len(str) <= 2:
            return []
        res = []
        st, base = 0, str[0]
        for idx in range(1, len(str)):
            if str[idx] == base:
                continue
            else:
                length = idx - st
                if length >= 3:
                    res.append([st, idx-1])
                st, base = idx, str[idx]
        if len(str) - st >= 3:
            res.append([st, len(str)-1])
        return res

# 来自面经：
# You are given a word like hellloooo print all the repeating character index and the number of time it is has been repeated: https://leetcode.com/problems/positions-of-large-groups

# Example 1:

# Input: "hellloooo"
# Output: [[2, 3], [5, 4]]
# Explanation: hellloooo has l and o as repeating characters so return index of l which is at 2
# and the number of times it has been repeated is 3. Same goes for O.
# Example 2:

# Input: "leetcodeee"
# Output: [[1, 2], [7, 3]]
# Follow-up:
# What if you need to print the repeated character as well?

# Example 1:

# Input: "hellloooo"
# Output : [['l', 3], ['o', 4]]
# Example 2:

# Input: "leetcodeee"
# Output: [['e', 5]]
