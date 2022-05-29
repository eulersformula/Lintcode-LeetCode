# Lintcode 924//Easy

# Description
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# Example
# Example 1:

# Input：["practice", "makes", "perfect", "coding", "makes"],"coding","practice"
# Output：3
# Explanation：index("coding") - index("practice") = 3
# Example 2:

# Input：["practice", "makes", "perfect", "coding", "makes"],"makes","coding"
# Output：1
# Explanation：index("makes") - index("coding") = 1

from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortest_distance(self, words: List[str], word1: str, word2: str) -> int:
        # Write your code here
        word1_pos, word2_pos = None, None
        min_dist = None
        for (idx, word) in enumerate(words):
            if word != word1 and word != word2:
                continue
            if word == word1:
                word1_pos = idx
            if word == word2:
                word2_pos = idx
            if word1_pos is not None and word2_pos is not None:
                # 用is not None 去判定非None。用if word1_pos当word1_pos为0时返回否
                d = abs(word2_pos - word1_pos)
                if min_dist is None or min_dist > d: # 注意大小等于
                    min_dist = d
        return min_dist
