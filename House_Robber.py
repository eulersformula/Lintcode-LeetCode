# Lintcode 392//Medium//LinkedIn//Airbnb

# Description
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example
# Example 1:

# Input: [3, 8, 4]
# Output: 8
# Explanation: Just rob the second house.
# Example 2:

# Input: [5, 2, 1, 3]
# Output: 8
# Explanation: Rob the first and the last house.

# Challenge
# O(n) time and O(1) memory.

from typing import (
    List,
)

class Solution:
    """
    @param a: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def house_robber(self, a: List[int]) -> int:
        # write your code here
        # Questions to ask:
        # 1. Can a be empty? If so, should I return 0?
        if len(a) == 0:
            return 0
        if len(a) == 1:
            return a[0]
        if len(a) == 2:
            return max(a[0], a[1])
        max_money = [a[0], max(a[0], a[1])]
        for i in range(2, len(a)):
            max_money[0], max_money[1] = max_money[1], max(max_money[0]+a[i], max_money[1])
        return max_money[1] 
