# Lintcode 41//Easy
# Leetcode 53//Medium

#Given an array of integers, find a contiguous subarray which has the largest sum.

#Example: Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

#Challenge: Can you do it in time complexity O(n)?

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if nums == None or len(nums) == 0:
            return None
        maxSum = [nums[0], nums[0]]
        for i in nums[1:]:
            maxSum[1] = i if maxSum[1] < 0 else (maxSum[1] + i)
            maxSum[0] = max(maxSum[1], maxSum[0])
        return max(maxSum)

# 二刷
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        s = nums[0]
        min_s = min(nums[0], 0)
        for n in nums[1:]:
            s += n
            res = max(s - min_s, res)
            if s < min_s:
                min_s = s 
        return res
