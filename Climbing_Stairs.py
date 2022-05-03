# Lintcode 111//Easy

# Description
# You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example
# Example 1:
# Input:
# n = 3
# Output:
# 3
# Explanation:
# 1, 1, 1
# 1, 2
# 2, 1
# total 3.

# Example 2:
# Input:
# n = 1
# Output:
# 1
# Explanation:
# only 1 way.

# SOLUTION 1: RECURSION
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n: int) -> int:
        # write your code here
        # Questions to ask:
        # 1. Can n be 0? If so, what is the number of steps?
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climb_stairs(n-1) + self.climb_stairs(n-2)

# SOLUTION 2: DP
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n: int) -> int:
        # write your code here
        # Questions to ask:
        # 1. Can n be 0? If so, what is the number of steps?
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        n_ways = [1, 2]
        for i in range(3, n+1):
            n_ways[0], n_ways[1] = n_ways[1], n_ways[0] + n_ways[1]
        return n_ways[1]
