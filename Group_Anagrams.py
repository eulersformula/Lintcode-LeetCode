# Leetcode 49

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 
# Constraints:

# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# 方法一
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Questions to ask:
        # 1. Is it possible to have duplicated strs in str? If so, should I return one copy or all copies?
        # 2. Should I care about upper/lower cases?
        if len(strs) == 0:
            return []
        all_chars = set()
        for s in strs:
            for ss in s:
                all_chars.add(ss)
        n_unique_chars = len(all_chars)
        char_to_idx = {v: idx for (idx, v) in enumerate(list(all_chars))}
        anagrams_dict = dict()
        for s in strs:
            tmp = [0] * n_unique_chars
            for ss in s:
                tmp[char_to_idx[ss]] += 1
            tmp = tuple(tmp)
            if tmp not in anagrams_dict:
                anagrams_dict[tmp] = []
            anagrams_dict[tmp].append(s)
        return list(anagrams_dict.values())

# 方法二

# 也可以用union find但没必要
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        anagrams_dict = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s)) # string sort之后返回值为list type
            if sorted_s not in anagrams_dict:
                anagrams_dict[sorted_s] = []
            anagrams_dict[sorted_s].append(s)
        return list(anagrams_dict.values())


