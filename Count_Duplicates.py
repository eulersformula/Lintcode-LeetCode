# Lintcode 1794//Easy//Salesforce

# Description
# Given an array of integers, your task is to find the duplicate numbers in the array.
# Your program should return all duplicate numbers and order them in order of where they started repeating.
# For example, the array [5,1,2,2,1,1] has two duplicate digits,1 and 2.
# The number 1 repeats at index 4, and the number 2 repeats at index 3, so your program should return [2, 1], because the 2 repeats before the 1 repeats.

# Example
# Example 1:

# Input: nums = [1, 2, 2, 3, 3, 3]
# Output: [2, 3]
# Example 2:

# Input: nums = [1, 2, 3]
# Output: []

from typing import (
    List,
)

class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def countduplicates(self, nums: List[int]) -> List[int]:
        # write your code here
        if len(nums) == 0:
            return []
        num_pos = dict()
        res = []
        for n in nums:
            if n not in num_pos:
                num_pos[n] = 1
            elif num_pos[n] != -1:
                res.append(n)
                num_pos[n] = -1
        return res
