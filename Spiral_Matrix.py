# Lintcode 374 // Medium // Microsoft // Uber // Google
# Description
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example
# Example 1:

# Input:	[[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2

# Input:	[[ 6,4,1 ], [ 7,8,9 ]]
# Output: [6,4,1,9,8,7]

from typing import (
    List,
)

# SOLUTION: RECURSION
class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0: # Notice: [] cannot directly do n_rows, n_cols = len(matrix), len(matrix[0])!
            return []
        n_rows, n_cols = len(matrix), len(matrix[0])
        if n_rows == 1:
            return matrix[0]
        if n_cols == 1:
            res = []
            for i in range(n_rows):
                res.append(matrix[i][0])
            return res
        res = matrix[0]
        for i in range(1, n_rows):
            res.append(matrix[i][-1])
        res += matrix[-1][::-1][1:n_cols] # Pay attention to this use
        for i in range(n_rows-2, 0, -1):
            res.append(matrix[i][0])
        """
        # First time code 
        remaining = []
        for i in range(1, n_rows-1):
            remaining.append(matrix[i][1:(n_cols-1)])
        return res + self.spiral_order(remaining)
        """
        """ To avoid additional space """
        matrix.pop(0)
        matrix.pop(-1)
        for i in range(len(matrix)):
            matrix[i].pop(0)
            matrix[i].pop(-1)
        return res + self.spiral_order(matrix)

# TODO: BFS

# TODO: While loop, no recursion
