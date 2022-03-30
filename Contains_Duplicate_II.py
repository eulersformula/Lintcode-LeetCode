# Lintcode 1319//Easy
# Description
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example
# Example 1：
# Input：nums = [1,2,1], k = 0
# Output：False

# Example 2：
# Input：nums = [1,2,1], k = 2
# Output：True
# Explanation：nums[0] = nums[2] and 2 - 0 <= 2

from typing import (
    List,
)

class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        # Write your code here
        # Questions to ask:
        # 1. Can nums be empty? If so, just return False?
        if len(nums) == 0:
            return False
        num_indices = dict() # There is no need to store all indices of a num, since only the last index will be compared
        for (idx, num) in enumerate(nums):
            if num not in num_indices:
                num_indices[num] = idx
            else:
                if idx - num_indices[num] <= k:
                    return True
                num_indices[num] = idx
        return False
