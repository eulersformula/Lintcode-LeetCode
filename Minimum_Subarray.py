#Given an array of integers, find the subarray with smallest sum.
#Return the sum of the subarray.

#Example:
#For [1, -1, -2, 1], return -3

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        if nums == None or len(nums) == 0:
            return None
        allMin = nums[0]
        curMin = nums[0]
        for n in nums[1:]:
            curMin = n if curMin > 0 else (curMin + n)
            allMin = min(curMin, allMin)
        return allMin
