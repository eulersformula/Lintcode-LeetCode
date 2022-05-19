# Leetcode 15//Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 
# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

# SOLUTION 1: T: O(n^2); S: O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Questions to ask:
        # 1. Is it possible for nums to contain duplicated numbers?
        # 一开始审题不清，要求返回的不是indices，而是值的triplet
        if len(nums) <= 2:
            return []
        nums_dict = dict()
        for (i, n) in enumerate(nums):
            if n not in nums_dict:
                nums_dict[n] = set()
            nums_dict[n].add(i)
        res = []
        for (v1, idx1) in nums_dict.items():
            for (v2, idx2) in nums_dict.items():
                if v1 > v2:
                    continue
                if v1 == v2 and len(idx1) < 2:
                    continue
                r = -v1 - v2
                if r < v2:
                    continue
                if r in nums_dict:
                    if v1 == v2 and v1 == r and len(idx1) < 3:
                        continue
                    if v2 == r and len(idx2) < 2:
                        continue
                    res.append([v1, v2, r])
        return res
