# Lintcode 608//Medium//Amazon

# Description
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Example
# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9 
# Output: [1, 2]
# Example 2:

# Input: nums = [2,3], target = 5
# Output: [1, 2]

# 双指针典型题 One pass, T: O(n), S: O(1)

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        # 题目给出必有一解，因此不必考虑特殊情况
        st, ed = 0, len(nums) - 1
        while st < ed:
            s = nums[st] + nums[ed]
            if s == target:
                break
            elif s < target:
                st += 1
            else:
                ed -= 1
        return st + 1, ed + 1
 
