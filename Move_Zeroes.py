#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

#Notice
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.

#Example
#Given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        n = len(nums)
        if n > 1:
            i = 0
            while i < n and nums[i]: #check i<n first!
                i += 1
            j = i + 1 
            while j < n:
                if nums[j]:
                    nums[i] = nums[j]
                    i += 1
                j += 1
            while i < n:
                nums[i] = 0
                i += 1
