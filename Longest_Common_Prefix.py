# Lintcode 78//Medium
# Description
# Given k strings, find the longest common prefix (LCP).

# Example
# Example 1:
# Input:
# K strings = ["ABCD", "ABEF", "ACEF"]
# Output:
# "A"
# Explanation:
# The longest common prefix is "A".

# Example 2:
# Input:
# K strings = ["ABCDEFG", "ABCEFG", "ABCEFA"]
# Output:
# "ABC"
# Explanation:
# The longest common prefix is "ABC".

from typing import (
    List,
)

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def common_prefix_string_pair(self, str1, str2):
        res = ''
        for idx in range(min(len(str1), len(str2))):
            if str1[idx] == str2[idx]:
                res += str1[idx]
            else:
                break
        return res

    def longest_common_prefix(self, strs: List[str]) -> str:
        # write your code here
        # Questions to ask:
        # 1. Is it possible to have an empty string list? If so, what should be returned?
        # 2. If len(strs) == 1, should strs[0] just be returned?
        if len(strs) == 0: # corner case missed
            return ''
        if len(strs) == 1:
            return strs[0]
        res = self.common_prefix_string_pair(strs[0], strs[1])        
        for s in strs[2:]:
            if res != '':
                res = self.common_prefix_string_pair(res, s)
            else:
                break
        return res
