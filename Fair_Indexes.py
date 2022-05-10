# Lintcode 1882//Medium//Microsoft

# Description
# You are given two arrays A and B consisting of N integers each.

# Index K is named fair if the four sums(A[0]+...A[K-1]),(A[K]+...+A[N-1]),(B[0]+...+B[K-1]) and (B[K]+...+B[N-1]) are all equal, In other words, K is the index where the two arrays, A and B, can be split (into two non-empty arrays each) in such a way that the sums of the resulting arrays’ elements are equal.

# For example, given arrays A = [4,-1, 0, 3] and B = [-2, 5, 0, 3], index K = 2 is fair. The sums of the subarrays are all equal: 4+(-1) = 3; 0+3 = 3; -2 + 5 = 3 and 0 + 3 = 3.

# Now you have to figure out the number of fair indexes.

# 2<=N<=100000
# -1000000000<=a[i],b[i]<=1000000000 (0<=i<N)
# Example
# Example 1:

# Input: 
# [4,-1,0,3] [-2,5,0,3]
# Output: 
# 2
# Example 2:

# Input: 
# [2,-2,-3,3] [0,0,4,-4]
# Output: 
# 1
# Example 3:

# Input: 
# [4,-1,0,3] [-2,6,0,4]
# Output: 
# 0
# Example 4:

# Input: 
# [1,4,2,-2,5] [7,-2,-2,2,5]
# Output: 
# 2

from typing import (
    List,
)

class Solution:
    """
    @param a: an array of integers
    @param b: an array of integers
    @return: return a integer indicating the number of fair indexes.
    """
    def count_indexes(self, a: List[int], b: List[int]) -> int:
        # Write your code here.
        # Questions to ask:
        # 1. Is it guaranteed to have such an index?
        # 题目要求是要把a和b分成non-empty arrays
        if len(a) == 0 or len(b) == 0 or len(a) != len(b):
            return 0
        cur_sum_a_r, cur_sum_b_r = sum(a), sum(b)
        cur_sum_a_l, cur_sum_b_l = 0, 0
        n_indices = 0
        for (a_v, b_v) in zip(a[:-1], b[:-1]): # Last element excluded; otherwise right array is empty
            cur_sum_a_l += a_v
            cur_sum_b_l += b_v
            cur_sum_a_r -= a_v
            cur_sum_b_r -= b_v
            if cur_sum_a_l == cur_sum_a_r and cur_sum_a_l == cur_sum_b_l and cur_sum_b_l == cur_sum_b_r:
                n_indices += 1
        return n_indices
