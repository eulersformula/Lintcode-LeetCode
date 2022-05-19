# Lintcode 1421//Easy//Goldman Sachs

# Description
# Two people choose numbers in a matrix. Everyone chooses the best number.
# The selected column can‘t selected anymore. you should return the difference between two people at last.

# Example
# Example:
# Input:
# grids:[[1,4,7],[2,5,8],[3,6,9]]
# Output:6
# Explanation: each column maxium is [3, 6, 9], at first, A choose 9 so B can't choose 3rd column. then B choose 6, finally, A choose 3, you should return (3 + 9) - 6 = 6

from typing import (
    List,
)

# 审题不清：selected column cannot be selected, 不是row
# T: O(mn); S: O(m)

class Solution:
    """
    @param grids: a integer matrix
    @return: return the difference between two people at last.
    """
    def matrix_game(self, grids: List[List[int]]) -> int:
        # write your code here
        if len(grids) == 0 or len(grids[0]) == 0:
            return 0
        max_col_nums = []
        for j in range(len(grids[0])):
            cur_max = None
            for i in range(len(grids)):
                if cur_max is None or grids[i][j] > cur_max:
                    cur_max = grids[i][j]
            max_col_nums.append(cur_max)
        max_col_nums.sort(reverse=True)
        p1_sum, p2_sum = 0, 0
        for (i, v) in enumerate(max_col_nums):
            if i % 2 == 0:
                p1_sum += v
            else:
                p2_sum += v
        return p1_sum - p2_sum
