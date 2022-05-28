# Lintcode 587//Medium

# Description
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

# Example
# Example 1:

# Input: nums = [1,1,2,45,46,46], target = 47 
# Output: 2
# Explanation:

# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:

# Input: nums = [1,1], target = 2 
# Output: 1
# Explanation:
# 1 + 1 = 2

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        # Questions to ask:
        # 1. Is nums sorted?
        if len(nums) < 2:
            return 0
        nums.sort()
        unique_pairs = set()
        res = 0
        st, ed = 0, len(nums) - 1
        while st < ed:
            a, b = nums[st], nums[ed]
            if a + b == target:
                a, b = min(a, b), max(a, b)
                if (a, b) not in unique_pairs:
                    unique_pairs.add((a, b))
                    res += 1
                st += 1
                ed -= 1
            elif a + b < target:
                st += 1
            else:
                ed -= 1
        return res
