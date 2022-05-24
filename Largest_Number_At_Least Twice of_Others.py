# Lintcode 1053//Easy//Google

# Description
# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].
# Example
# Example 1:

# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
# Example 2:

# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

from typing import (
    List,
)

# T: O(n); S: O(1)

class Solution:
    """
    @param nums: a integer array
    @return: the index of the largest element
    """
    def dominant_index(self, nums: List[int]) -> int:
        # Write your code here
        # 1. What to return if length of nums is 1?
        if len(nums) <= 1:
            return 0
        max_num, max_num_idx, second_max_num = nums[0], 0, None
        for i in range(1, len(nums)):
            if max_num < nums[i]: # there is only one largest element
                second_max_num = max_num
                max_num, max_num_idx = nums[i], i
            if second_max_num is None: # nums[1] <= nums[0]
                second_max_num = nums[i]
        if max_num >= 2 * second_max_num:
            return max_num_idx
        return -1
