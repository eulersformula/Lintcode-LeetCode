# Leetcode 96//Medium
# Lintcode 163//Medium

# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Example 1:
# Input: n = 3
# Output: 5

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
# 1 <= n <= 19

# SOLUTION 1: RECURSION (TIME LIMIT EXCEEDED)
# SOLTION 2: DP

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        n_trees = [1, 1, 2] + [0] * (n - 2) # 不使用append会加速
        for r in range(3, n+1):
            # suppose root node is val 1 <= v <= n
            res = 0
            for v in range(1, r+1):
                num_trees_left = n_trees[v-1] 
                num_trees_right = n_trees[r-v] # from (v + 1) to r
                res += num_trees_left * num_trees_right
            n_trees[r] = res
        return res
