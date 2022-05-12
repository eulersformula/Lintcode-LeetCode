# Lintcode 1368//Easy//Google

# Description
# Given an array, If the same number exists in the array, and the minimum distance the same number is less than the given value k, output YES, otherwise output NO.

# The length of the given array is n，and n <= 100000.
# The element is x，0 <= x <= 1e9.
# 1 <= k < n。
# Example
# Example1

# Input:  array = [1,2,3,1,5,9,3] and k = 4
# Output: "YES"
# Explanation:
# The distance of 1 whose indexes are  3 and 0 is 3, which meets the requirement and output YES.
# Example2

# Input:  array = [1,2,3,5,7,1,5,1,3] and k = 4
# Output: "YES"
# Explanation:
# The distance of 1 whose indexes are 5 and 7 is 2, which meets the requirement， and output YES.

from typing import (
    List,
)

class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def same_number(self, nums: List[int], k: int) -> str:
        # Write your code here
        if len(nums) <= 1:
            return 'NO'
        num_pos = dict()
        for (i, v) in enumerate(nums):
            if v not in num_pos:
                num_pos[v] = []
            num_pos[v].append(i)
        for v in num_pos:
            if len(num_pos[v]) >= 2:
                for i in range(len(num_pos[v])-1):
                    if num_pos[v][i+1] - num_pos[v][i] < k:
                        return 'YES'
        return 'NO'

