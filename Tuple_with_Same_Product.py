# Leetcode 1726//Medium
# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

# Constraints:

# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^4
# All elements in nums are distinct.

# 一开始解法
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Questions to ask:
        # 1. Range of nums
        # 审题：positive integers
        if len(nums) < 4:
            return 0
        nums_set = set(nums)
        from collections import deque
        ordered_nums = deque(sorted(nums))
        # find 4-element tuple pairs: a < b < c < d and ad == bc
        res = 0
        while len(ordered_nums) >= 4:
            a = ordered_nums.popleft()
            nums_set.remove(a) # set remove
            for d_idx in range(len(ordered_nums)-1, 1, -1):
                prod = a * ordered_nums[d_idx]
                for c_idx in range(d_idx-1, 0, -1):
                    target = prod / ordered_nums[c_idx]
                    if target in nums_set and target < ordered_nums[c_idx]:
                        res += 8
        return res

# 第二次答案：T: O(n^2); S: O(n^2) worst case scenarios all pairs have different products
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Questions to ask:
        # 1. Range of nums
        # 审题：positive integers
        if len(nums) < 4:
            return 0
        prod_dict = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in prod_dict:
                    prod_dict[prod] = [0]
                if nums[i] not in prod_dict[prod][0] and \
                   nums[j] not in prod_dict[prod][0]:
                    prod_dict[prod][0].add(nums[i])
                    prod_dict[prod][0].add(nums[j])
                    prod_dict[prod][1] += 1
        res = 0
        for (k, v) in prod_dict.items():
            cnt = v[1]
            res += cnt * (cnt - 1) * 4 # if cnt == 1, no pairs
        return res
    
# 继续优化：对于unique positive pairs（nested for loop），如果两对乘积相等，必不可能有相同元素
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Questions to ask:
        # 1. Range of nums
        # 审题：positive integers
        if len(nums) < 4:
            return 0
        prod_dict = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = nums[i] * nums[j]
                if prod not in prod_dict:
                    prod_dict[prod] = 0
                prod_dict[prod] += 1
        res = 0
        for (k, v) in prod_dict.items():
            if v > 1:
                res += v * (v - 1) * 4 # if cnt == 1, no pairs
        return res
