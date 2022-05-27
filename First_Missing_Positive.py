# Leetcode 41//Hard

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1

# SOLUTION 1: SORTING. T: O(nlog(n)); S: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        nums.sort()
        idx = 0
        while idx < len(nums):
            if nums[idx] == 1:
                break
            idx += 1
        if idx > len(nums) - 1:
            return 1
        if idx == len(nums) - 1:
            return 2
        idx += 1
        while idx < len(nums) and nums[idx] - nums[idx-1] < 2:
            idx += 1
        return nums[idx-1] + 1

# SOLUTION 2:
