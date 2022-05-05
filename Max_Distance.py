# Lintcode 1624//Hard//Google

# Description
# The distance between the two binary strings is the sum of the lengths of the common prefix removed. For example: the common prefix of 1011000 and 1011110 is 1011, distance is len ("000" + "110") = 3 + 3 = 6. Now give a list of binary strings, find max distance.

# The total length of the binary string does not exceed 50000

# Example
# Example 1:

# Input：["011000","0111010","01101010"]
# Output：9
# Explanation：the the common prefix of "0111010" and "01101010" is "011", distance is len("1010")+len("01010")=9
# Example 2:

# Input：["011000","0111011","01001010"]
# Output：11
# Explanation:the the common prefix of "0111011" and "01001010" is "01", distance is len("11011")+len("001010")=11

# NAIVE SOLUTION: O(n^2) time complexity
from typing import (
    List,
)

class Solution:
    """
    @param s: the list of binary string
    @return: the max distance
    """
    def get_len_common_prefix(self, s1: str, s2: str) -> str:
        if len(s1) == 0 or len(s2) == 0:
            return 0
        l = 0
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                l += 1
            # 第一次写漏掉了该else语句
            else:
                break
        return l

    def get_ans(self, s: List[str]) -> int:
        # Write your code here
        # Questions to ask:
        # 1. Is it possible for s to be empty or have a length of 1? If so, what should be returned?
        if len(s) < 2:
            return 0
        str_len = [len(x) for x in s]
        max_dist = None
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                len_common_prefix = self.get_len_common_prefix(s[i], s[j])
                dist = str_len[i] + str_len[j] - 2 * len_common_prefix
                if max_dist is None:
                    max_dist = dist
                max_dist = dist if dist > max_dist else max_dist
        return max_dist
