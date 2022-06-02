# Lintcode 1501//Easy
# Leetcode 867//Easy

# Given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# xample 2:

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 1000
# 1 <= m * n <= 10^5
# -10^9 <= matrix[i][j] <= 10^9

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        if n == 0:
            return matrix
        m = len(matrix[0])
        if m == 0:
            return matrix
        # transpose means a[i][j] -> a[j][i]
        if n == m:
            for i in range(n-1):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        res = [[None for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i] = matrix[i][j]    
        return res

# 一行code写法
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
      return [list(x) for x in zip(*matrix)]
