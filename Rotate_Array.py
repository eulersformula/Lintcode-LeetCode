# Lintcode 1334//Easy
# Description
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Example
# Example 1:

# Input: [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Challenge
# 1.Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# 2.Could you do it in-place with O(1) extra space?

from typing import (
    List,
)

# SOLUTION 1
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        length = len(nums)
        res = [0] * length
        for (i, v) in enumerate(nums):
            res[(i+k)%length] = v
        return res

# SOLUTION 2
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        length = len(nums)
        cut_off = k % length
        if cut_off > 0:
            return nums[(-cut_off):] + nums[:(-cut_off)]
        # else no need to rotate
        return nums

# Solution 3:
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums: List[int], k: int) -> List[int]:
        # Write your code here
        n_nums = len(nums)
        k = k % n_nums
        if k == 0:
            return nums
        self.reverse(nums, 0, n_nums)
        self.reverse(nums, 0, k)
        self.reverse(nums, k, n_nums)
        return nums
    
    def reverse(self, arr: List[int], st: int, ed: int) -> List[int]: 
        # Double pointer for reversing (part of) an array in place
        # ed is exclusive
        ed -= 1
        while st < ed:
            arr[st], arr[ed] = arr[ed], arr[st]
            st += 1
            ed -= 1
  
