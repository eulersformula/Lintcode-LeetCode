# Lintcode 685//Medium

# Description
# Given a continuous stream of data, write a function that returns the first unique number (including the last number) when the terminating number arrives. If the terminating number is not found, return -1.

# Example
# Example1

# Input: 
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 5
# Output: 3
# Example2

# Input: 
# [1, 2, 2, 1, 3, 4, 4, 5, 6]
# 7
# Output: -1
# Example3

# Input: 
# [1, 2, 2, 1, 3, 4]
# 3
# Output: 3

from typing import (
    List,
)

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def first_unique_number(self, nums: List[int], number: int) -> int:
        # Write your code here
        if len(nums) == 0:
            return -1
        first_time = dict() 
        for (i, n) in enumerate(nums):
            if n == number:
                res_v, res_first_time = n, i
                for (v, t) in first_time.items():
                    if t != -1 and t < res_first_time:
                        res_v, res_first_time = v, t
                return res_v
            if n not in first_time:
                first_time[n] = i
            else:
                first_time[n] = -1
        # number not found in nums
        return -1

# 需补充解法：HashMap + LinkedList
