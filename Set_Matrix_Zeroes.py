# Leetcode 73//Medium

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1

# T: O(nm); S: O(n) + O(m)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_rows, len_cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()
        for i in range(len_rows):
            for j in range(len_cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            for j in range(len_cols):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(len_rows):
                matrix[i][j] = 0
                

# 用其他值代替被变成的0以防止混淆。S: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_rows, len_cols = len(matrix), len(matrix[0])
        for i in range(len_rows):
            row_zero = False
            for j in range(len_cols):
                if matrix[i][j] == 0:
                    if not row_zero:
                        row_zero = True
                    for ii in range(len_rows):
                        if matrix[ii][j] not in [0, None]:
                            matrix[ii][j] = None
            if row_zero:
                for j in range(len_cols):
                    if matrix[i][j] not in [0, None]:
                        matrix[i][j] = None
        for i in range(len_rows):
            for j in range(len_cols):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

# 用一行一列当做tmp storage。T: O(nm); S: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_rows, len_cols = len(matrix), len(matrix[0])
        # 选定需要消去的row, col作为tmp storage
        row, col = None, None
        for i in range(len_rows):
            for j in range(len_cols):
                if matrix[i][j] == 0:
                    row, col = i, j
                    break
        # 需要考虑没有遇到0的情况
        if row is not None:
            for i in range(len_rows):
                if i == row:
                    continue
                for j in range(len_cols):
                    if j == col:
                        continue
                    if matrix[i][j] == 0:
                        if matrix[i][col] != 0:
                            matrix[i][col] = 0
                        if matrix[row][j] != 0:
                            matrix[row][j] = 0
            for i in range(len_rows):
                if i == row:
                    continue
                if matrix[i][col] == 0:
                    for j in range(len_cols):
                        if j == col:
                            continue
                        if matrix[i][j] != 0:
                            matrix[i][j] = 0
            for j in range(len_cols):
                if matrix[row][j] == 0:
                    for i in range(len_rows):
                        if matrix[i][j] != 0:
                            matrix[i][j] = 0
            for j in range(len_cols):
                if matrix[row][j] != 0:
                    matrix[row][j] = 0
