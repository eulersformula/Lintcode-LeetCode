# Lintcode 1835//Easy//Apple

# Description
# You have a pointer at index 00 in an array of size arrLenarrLen.

# At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place (The pointer should not be placed outside the array at any time).

# Given two integers stepssteps and arrLenarrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps.

# Since the answer may be too large, return it modulo 10^9 + 7

# 1 \leq steps \leq 15
# 1 \leq arrLen \leq 10^6
 
# Example
# Example 1:

# Input: 
# 3
# 2
# Output: 
# 4
# Explanation: 
# There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay
# Example 2:

# Input: 
# 2
# 4
# Output: 
# 2
# Explanation: 
# There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay
# Example 3:

# Input: 
# 4
# 2
# Output: 
# 8

# SOLUTION 1: O(mn) time complexity, O(n) space complexity。初次写的答案，TIME LIMIT EXCEEDED.
class Solution:
    """
    @param steps: steps you can move
    @param arr_len: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def num_ways(self, steps: int, arr_len: int) -> int:
        # write your code here
        if arr_len == 0:
            return 0
        if steps == 0:
            return 1
        n_ways = [1] + [0] * (arr_len-1)
        for i in range(steps):
            cur_n_ways = n_ways.copy()
            for j in range(arr_len):
                n_ways[j] = cur_n_ways[j]
                if j > 0:
                    n_ways[j] += cur_n_ways[j-1]
                if j < arr_len - 1:
                    n_ways[j] += cur_n_ways[j+1]
        return n_ways[0] % int(1e9 + 7)

# SOLUTION 2: 关键点：最远到达的index为steps，不需初始化arr_len长度的状态变量以减少加和次数
class Solution:
    """
    @param steps: steps you can move
    @param arr_len: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    def num_ways(self, steps: int, arr_len: int) -> int:
        # write your code here
        if arr_len == 0:
            return 0
        if steps == 0:
            return 1
        n_ways = [1] # at time 0, only 1 way at pos 0
        for i in range(steps):
            cur_n_ways = []
            for j in range(len(n_ways)):
                res = n_ways[j]
                if j > 0:
                    res += n_ways[j-1]
                if j < len(n_ways) - 1:
                    res += n_ways[j+1]
                cur_n_ways.append(res)
            last_term = n_ways[-1]
            n_ways = cur_n_ways
            if len(cur_n_ways) < arr_len:
                n_ways.append(last_term)
        return n_ways[0] % int(1e9 + 7)
 

