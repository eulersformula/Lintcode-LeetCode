# Leetcode 976//Easy
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
# Example 1:

# Input: nums = [2,1,2]
# Output: 5
# Example 2:

# Input: nums = [1,2,1]
# Output: 0
 

# Constraints:

# 3 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^6

# 初次解: T: O(n^2); S: O(1). TLE
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 3:
            return 0
        nums.sort(reverse=True)
        res = 0
        for i in range(len_nums-2):
            for j in range(i+1, len_nums-1):
                if nums[j+1] > nums[i] - nums[j]:
                    res = max(res, nums[i]+nums[j]+nums[j+1])
        return res

# 二次解：T: O(nlog n); S: O(1)
# 考虑reverse sort过后的index i和j > i，需要满足的要求是nums[j+1] > nums[i] - nums[j] (index越大值越小，若j+1不能满足则之后元素均
# 不能满足，并且j+1已最大故周长最大），那么当j=i时满足要求，因为nums[i] - nums[i+1] <= nums[i] - nums[j]，nums[i+2] > nums[j+1]，
# 若(nums[i], nums[i+1], nums[i+2])不能满足要求，则(nums[i], nums[j], nums[j+1])也不能满足要求。且前者之和大于后者。
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 3:
            return 0
        nums.sort(reverse=True)
        for i in range(len_nums-2):
            if nums[i+2] > nums[i] - nums[i+1]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
