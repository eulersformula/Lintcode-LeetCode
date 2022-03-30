# Lintcode 47//Medium

# Description
# Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array.
# Find it.
# There is only one majority number in the array.

# Example
# Example 1:
# Input:
# nums = [99,2,99,2,99,3,3]
# Output:
# 99
# Explanation:
# 99 appeared three times.

# Example 2:
# Input:
# nums = [1, 2, 1, 2, 1, 3, 3]
# Output:
# 1
# Explanation:
# 1 appeared three times.

# Challenge
# O(n) time and O(1) extra space.

from typing import (
    List,
)

# SOLUTION 1: O(n) time and O(n) extra space.
class Solution:
    """
    @param nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    # Questions to ask:
    # 1. Can nums be empty?
    # 2. Is the existence of such a number guaranteed and unique?
    def majority_number(self, nums: List[int]) -> int:
        # write your code here
        num_counts = {}
        for n in nums:
            if n not in num_counts:
                num_counts[n] = 0
            num_counts[n] += 1
        for num in num_counts:
            if num_counts[num] > len(nums) / 3:
                return num

# SOLUTION 2: O(n) time and O(1) extra space. 
##Boyer–Moore majority vote algorithm: https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm##


