# Lintcode 297 // Naive
# Description
# Find the maximum of n numbers.

# We promise that all numbers in the list are in the range of int.

# Example
# Example 1:

# Input：[1, 2, 3, 4, 5]
# Output：5

from typing import (
    List,
)

# SOLUTION 1
class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def max_num(self, nums: List[int]) -> int:
        # write your code here
        # Questions to ask:
        # 1. Can nums be empty?
        res = nums[0]
        for v in nums[1:]:
            if v > res:
                res = v
        return res 

# SOLUTION 2
class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def max_num(self, nums: List[int]) -> int:
        # write your code here
        # Questions to ask:
        # 1. Can nums be empty?
        return max(nums)
      
