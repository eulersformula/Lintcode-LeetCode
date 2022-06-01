# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

# 第一次解法：
from collections import deque
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n_nums = len(nums)
        if n_nums <= 1:
            return n_nums
        stack = set([tuple()])
        res = 0
        for n in nums:
            best_to_append = tuple()
            for s in stack:
                if len(s) > len(best_to_append) and n > s[-1]:
                    best_to_append = s
            stack.add(best_to_append + (n,))
            if len(best_to_append) + 1 > res:
                res = len(best_to_append) + 1
        return res
  
 # 第二次解法：不需要记录实际的数组，只需要记录长度和最大元素即可. T: O(n^2); S: O(n^2)
from collections import deque
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n_nums = len(nums)
        if n_nums <= 1:
            return n_nums
        stack = set([(None, 0)])
        res = 0
        for n in nums:
            max_prev_nums = 0
            # print('num', n)
            for s in stack:
                # print(s, s[1] > best_to_append[1], best_to_append)
                if s[1] > max_prev_nums and n > s[0]:
                    max_prev_nums = s[1]
            stack.add((n, max_prev_nums+1))
            if max_prev_nums + 1 > res:
                res = max_prev_nums + 1
            # print(stack, res)
        return res
            
