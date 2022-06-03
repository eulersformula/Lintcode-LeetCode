# Lintcode 1042//Easy//Google
# Leetcode 766//Easy//Google
# Description
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].
# Example
# Example 1:

# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: True
# Explanation:
# 1234
# 5123
# 9512

# In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.

# Example 2:

# Input: matrix = [[1,2],[2,2]]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.

# Follow up:

# What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into the memory at once?

from typing import (
    List,
)

class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def is_toeplitz_matrix(self, matrix: List[List[int]]) -> bool:
        # Write your code here
        n = len(matrix)
        if n == 1:
            return True
        m = len(matrix[0])
        if m == 1:
            return True
        for j in range(m):
            base = matrix[0][j]
            ii, jj = 1, j+1
            while ii < n and jj < m:
                if matrix[ii][jj] != base:
                    return False
                ii += 1
                jj += 1
        for i in range(n):
            base = matrix[i][0]
            ii, jj = i+1, 1
            while ii < n and jj < m:
                if matrix[ii][jj] != base:
                    return False
                ii += 1
                jj += 1
        return True

