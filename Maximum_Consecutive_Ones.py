# Lintcode 1212//Easy//Google
# Description
# Given a binary array, find the maximum number of consecutive 1s in this array.

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# Example
# Example 1:

# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Example 2:

# Input: [1]
# Output: 1

from typing import (
    List,
)

class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # Write your code here
        if len(nums) == 0:
            return 0
        res = 0
        n_ones = 0
        for n in nums:
            if n == 1:
                n_ones += 1
            elif n_ones > 0:
                res = max(res, n_ones)
                n_ones = 0
        res = max(res, n_ones)
        return res
