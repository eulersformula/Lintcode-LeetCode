# Lintcode 1320//Easy

# Description
# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example
# Example 1：
# Input：nums = [1, 1]
# Output：True

# Example 2：
# Input：nums = [1, 2, 3]
# Output：False

from typing import (
    List,
)

# SOLUTION 1
class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def contains_duplicate(self, nums: List[int]) -> bool:
        # Write your code here
        # Questions to ask:
        # 1. Can nums be empty? If so, what should be returned?
        return len(set(nums)) != len(nums)

# SOLUTION 2
class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def contains_duplicate(self, nums: List[int]) -> bool:
        # Write your code here
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        return False
