# Lintcode 1901//Easy//ByteDance

# Description
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
# Example
# Example 1

# Input: 
# [-4,-1,0,3,10]
# Output: 
# [0,1,9,16,100]
# Example 2

# Input: 
# [-7,-3,2,3,11]
# Output: 
# [4,9,9,49,121]

from typing import (
    List,
)

# T: O(n); S: O(1) 返回数组不算额外空间
class Solution:
    """
    @param a: The array A.
    @return: The array of the squares.
    """
    def square_array(self, a: List[int]) -> List[int]:
        # write your code here
        if len(a) == 0:
            return []
        if len(a) == 1:
            return [a[0]*a[0]]
        res = [-1] * len(a)
        st, ed = 0, len(res) - 1
        idx = len(a) - 1
        while idx >= 0:
            if a[st] * a[st] >= a[ed] * a[ed]:
                res[idx] = a[st] * a[st]
                st += 1
            else:
                res[idx] = a[ed] * a[ed]
                ed -= 1
            idx -= 1
        return res
