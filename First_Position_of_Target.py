#For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

#If the target number does not exist in the array, return -1.

#Example
#If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        if nums == []:
            return False
        lenNums = len(nums)
        if lenNums == 1:
            if nums[0] == target:
                return 0
            return -1
        st, ed = 0, lenNums - 1
        while st != ed - 1:
            pos = (st + ed) / 2
            if nums[pos] >= target:
                ed = pos
            else:
                st = pos
        if nums[st] == target:
            return st
        if nums[ed] == target:
            return ed
        return -1

