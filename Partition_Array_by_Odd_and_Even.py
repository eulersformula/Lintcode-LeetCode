#Partition an integers array into odd number first and even number second.

#Example
#Given [1, 2, 3, 4], return [1, 3, 2, 4]

#Analysis: Very similar to the partition function in quicksort algorithm (two pointers) 
#Time complexity: O(n); Space complexity: O(1).

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        n = len(nums)
        if n > 1:
            st, ed = 0, n - 1
            while st < ed:
                if not (nums[st] & 1):
                    nums[st], nums[ed] = nums[ed], nums[st]
                    ed -= 1
                elif nums[ed] & 1:
                    nums[st], nums[ed] = nums[ed], nums[st]
                    st += 1
                else:
                    st += 1
                    ed -= 1
