# Lintcode 31//Medium

# Description
# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.

# If all elements in nums are smaller than k, then return nums.length
# 0 <= nums.length <= 20000<=nums.length<=2000

# Example
# Example 1:

# Input:

# nums = []
# k = 9
# Output:

# 0
# Explanation:

# Empty array, print 0.

# Example 2:

# Input:

# nums = [3,2,2,1]
# k = 2
# Output:

# 1
# Explanation:

# the real array is[1,2,2,3].So return 1.

# Challenge
# Can you partition the array in-place and in O(n)?

from typing import (
    List,
)

# T: O(n); S: O(1)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    # 第一遍的时候完全写反了， 变成了值不小于k的在前面，值小于k的在后面
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        # Questions to ask:
        # 1. What to return if there is no such idx? Namely no element >= k?
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] >= k:
                return 0
            return 1
        geq_idx, lt_idx = 0, None
        while lt_idx is None or lt_idx < len(nums):
            while geq_idx < len(nums) and nums[geq_idx] < k:
                geq_idx += 1
            if geq_idx == len(nums):
                break
            if lt_idx is None: # 若不加此判断，第一次赋值时，lt_idx就变成了geq_idx的左边
                lt_idx = geq_idx + 1
            while lt_idx < len(nums) and nums[lt_idx] >= k:
                lt_idx += 1
            if lt_idx == len(nums):
                break
            nums[geq_idx], nums[lt_idx] = nums[lt_idx], nums[geq_idx] # actually no need for this step since we don't need to return this partitioned array
            geq_idx += 1
            lt_idx += 1
        return geq_idx # 从test case里得知，如果所有值都小于k那么return len(nums)

# TODO: 精简双指针模板

