#Two times

#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#Note
#You can only move either down or right at any point in time.

#This is a classical dynamic programming problem. I did the calculation in place which will change grid matrix. Need to ask if this is allowed. Otherwise can require a new matrix to store the results.

#Key points are:
#First, initialize the first row and first column.
#Second, calculate the shortest path for each point from top to bottom, from left to right. 

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        for i in xrange(1, m):
            grid[i][0] += grid[i - 1][0]
        for j in xrange(1, n):
            grid[0][j] += grid[0][j - 1]
        for j in xrange(1, n):
            for i in xrange(1, m):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[m - 1][n - 1]
