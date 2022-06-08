# Lintcode 293//Medium//Google

# Description
# We say that a binary matrix has a tunnel if it has 0's everywhere except for a path of 1's from the top-left cell to the top-right cell, going through adfacent cells. Every "1" in the path is adjacent to exactly two other 1's, except for the first and last 1's, which are only adjacent to one other "1".
# Now give you a matrix with a tunnel, find how deep the tunnel reaches (the index of the last row traversed by the tunnel, count from 0).

# The number of cells in the matrix not exceed 1e7.

# Example

# input: [[1,0,0,0,1],[1,1,0,0,1],[0,1,0,1,1],[0,1,1,1,0],[0,0,0,0,0]]
# output:3

from typing import (
    List,
)
# Solution 1: DFS. T: O(n) = O(2m-2) = O(m); S: O(1); n为矩阵里1的个数，m为矩阵列数，每列两个1除了首尾【易错，多练】
from collections import deque
class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """
    # Matrix print:
    # '\n'.join([' '.join([str(y) for y in x]) for x in matrix])
    def find_depth(self, matrix: List[List[int]]) -> int:
        # 1 0 0 0 1
        # 1 1 0 0 1
        # 0 1 0 1 1
        # 0 1 1 1 0
        # 0 0 0 0 0
        n_rows = len(matrix)
        if n_rows == 1:
            return 0
        n_cols = len(matrix[0]) # 一开始写成len(matrix[0])
        stack = deque([((0, 0), 0)])
        dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(stack) > 0:
            (x, y), d = stack.pop()
            if x == 0 and y == n_cols - 1:
                return d
            matrix[x][y] = 0
            for (dx, dy) in dxdy:
                new_x, new_y = x + dx, y + dy
                if new_x >= 0 and new_x < n_rows and new_y >= 0 \
                    and new_y < n_cols and matrix[new_x][new_y] == 1: 
                    # 一开始max(new_x, d)写成max(new_x, x)
                    stack.append(((new_x, new_y), max(new_x, d))) 
            # print('\n'.join([' '.join([str(y) for y in x]) for x in matrix]))
            
 # 改进写法
class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """
    def find_depth(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        if n_rows == 1:
            return 0
        n_cols = len(matrix[0])
        if n_cols == 1:
            return 0
        max_d = 0
        x, y = 0, 0
        dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while x != 0 or y != n_cols - 1:
            matrix[x][y] = 0
            for (dx, dy) in dxdy:
                new_x, new_y = x + dx, y + dy
                if new_x >= 0 and new_x < n_rows and new_y >= 0 and \
                    new_y < n_cols and matrix[new_x][new_y] == 1:
                    x, y = new_x, new_y
                    max_d = max(max_d, x)
                    break
        return max_d

# Solution 2: Binary Search. T: O(mlog n); S: O(1); n为行数，m为列数。 
class Solution:
    """
    @param matrix: the matrix in problem
    @return: the depth of the tunnel.
    """
    def find_depth(self, matrix: List[List[int]]) -> int:
        n_rows = len(matrix)
        if n_rows == 1:
            return 0
        n_cols = len(matrix[0])
        if n_cols == 1:
            return 0
        st, ed = 0, n_rows - 1
        while st < ed - 1:
            mid = (st + ed) // 2
            if sum(matrix[mid]) <= 0:
                ed = mid
            else:
                st = mid
        if sum(matrix[ed]) > 0:
            return ed
        return st
