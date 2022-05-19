# Lintcode 50//Easy

# Description
# Given an integers array A.

# Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]B[i]=A[0]∗...∗A[i−1]∗A[i+1]∗...∗A[n−1], calculate B WITHOUT divide operation.Out put B

# Example
# Example 1:

# Input:

# A = [1,2,3]
# Output:

# [6,3,2]
# Explanation:

# B[0] = A[1] * A[2] = 6; B[1] = A[0] * A[2] = 3; B[2] = A[0] * A[1] = 2

# Example 2:

# Input:

# A = [2,4,6]
# Output:

# [24,12,8]
# Explanation:

# B[0] = A[1] * A[2] = 24; B[1] = A[0] * A[2] = 12; B[2] = A[0] * A[1] = 8

from typing import (
    List,
)

class Solution:
    """
    @param nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def product_exclude_itself(self, nums: List[int]) -> List[int]:
        # write your code here
        res = [1] * len(nums)
        for i in range(len(nums)-1):
            res[i+1] *= res[i] * nums[i] 
        tmp = 1
        for i in range(len(nums)-1, 0, -1):
            tmp *= nums[i]
            res[i-1] *= tmp
        return res
