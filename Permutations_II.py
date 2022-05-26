# Lintcode 16//Medium
# Description
# Given a list of numbers with duplicate numbers in it. Find all unique permutations of it.

# Example
# Example 1:

# Input:

# nums = [1,1] 
# Output:

# [ 
#   [1,1] 
# ] 
# Explanation:

# The different arrangement of [1,1] is only [1,1].

# Example 2:

# Input:

# nums = [1,2,2] 
# Output:

# [ 
#   [1,2,2], 
#   [2,1,2], 
#   [2,2,1] 
# ] 
# Explanation:

# The different arrangements of [1,2,2] are [1,2,2],[2,1,2]and [2,2,1].

# Challenge
# Using recursion to do it is acceptable. If you can do it without recursion, that would be great!

from typing import (
    List,
)

# T: O(N); S: O(N); N is the number of permutations

class Solution:
    """
    @param nums: A list of integers
    @return: A list of unique permutations
             we will sort your return value in output
    """
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if len(nums) == 0:
            return [[]] # 注意该边角情况
        res = set()
        res.add((nums[0],))
        for n in nums[1:]:
            cur_res = set()
            for t in res:
                for idx in range(len(t)+1):
                    tmp = t[:idx] + (n,) + t[idx:]
                    cur_res.add(tmp)
            res = cur_res
        return [list(x) for x in res]
