# Lintcode 883//Medium//Google

# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000.
# Example
# Example 1:
# 	Input:  nums = [1,0,1,1,0]
# 	Output:  4
	
# 	Explanation:
# 	Flip the first zero will get the the maximum number of consecutive 1s.
# 	After flipping, the maximum number of consecutive 1s is 4.

# Example 2:
# 	Input: nums = [1,0,1,0,1]
# 	Output:  3
	
# 	Explanation:
# 	Flip each zero will get the the maximum number of consecutive 1s.
# 	After flipping, the maximum number of consecutive 1s is 3.

from typing import (
    List,
)

# T: O(n); S: O(n)

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # write your code here
        if len(nums) <= 1:
            return len(nums)
        # records how many consecutive ones till this pos (including this pos)
        # forward and backward
        prev_ones = [[0, 0] for _ in range(len(nums))]
        n_ones = 0
        res = 0
        for (i, n) in enumerate(nums):
            if n == 1:
                n_ones += 1
                if n_ones > res:
                    res = n_ones
            else:
                n_ones = 0
            prev_ones[i][0] = n_ones
        n_ones = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 1:
                n_ones += 1
            else:
                n_ones = 0
            prev_ones[i][1] = n_ones
        for (i, n) in enumerate(nums):
            if n == 0:
                cur_cnt = 1
                if i > 0:
                    cur_cnt += prev_ones[i-1][0]
                if i < len(nums) - 1:
                    cur_cnt += prev_ones[i+1][1]
                if cur_cnt > res:
                    res = cur_cnt
        return res
	
