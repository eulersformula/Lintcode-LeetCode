# Lintcode 761//Medium
# Description
# Given an array of non-negative integers. Our task is to find minimum number of elements such that their sum should be greater than the sum of rest of the elements of the array. At least one positive integer is in the array.

# Example
# Example 1:

# Input: nums = [3, 1, 7, 1], 
# Output: 1
# Example 2:

# Input: nums = [2, 1, 2], 
# Output: 2

from typing import (
    List,
)

# SOLUTION: T: O(nlogn) + O(n); S: O(1), in-place sort.

class Solution:
    """
    @param arr: an array of non-negative integers
    @return: minimum number of elements
    """
    def min_elements(self, arr: List[int]) -> int:
        # write your code here
        if len(arr) == 0:
            return 0
        arr.sort(reverse=True) # 一开始此处忘了写reverse=True
        s = sum(arr)
        cur_sum, cur_remaining_sum, cnt = 0, s, 0
        for v in arr:
            cur_sum += v
            cnt += 1
            cur_remaining_sum -= v
            if cur_sum > cur_remaining_sum:
                return cnt
        return -1 # should never reach
