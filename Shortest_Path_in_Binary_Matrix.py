# Leetcode 1091//Medium

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

# SOLUTION 1: BFS LEVEL. T: O(n); S: O(n); n is the number of elements in the matrix

class Solution:
    def valid_coord(self, coord, visited_coord, n):
        if coord in visited_coord:
            return False
        if coord[0] < 0 or coord[0] >= n or coord[1] < 0 or coord[1] >= n:
            return False
        return True
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        if grid[0][0] == 1:
            return -1
        n = len(grid) # 一开始忘了定义n导致错误
        coord_set = {(0, 0)} # set initialization一开始写错了，写成了((0, 0))
        len_path = 1
        visited_coord = set()
        while len(coord_set) > 0:
            for (x, y) in coord_set:
                if x == n - 1 and y == n - 1:
                    return len_path
            next_level_coord_set = set()
            for x, y in coord_set:
                for step_x in [-1, 0, 1]:
                    for step_y in [-1, 0, 1]:
                        if step_x == 0 and step_y == 0:
                            continue
                        cur_x, cur_y = x + step_x, y + step_y
                        if self.valid_coord((cur_x, cur_y), visited_coord, n) and grid[cur_x][cur_y] == 0:
                            next_level_coord_set.add((cur_x, cur_y))
                            visited_coord.add((cur_x, cur_y))
            coord_set = next_level_coord_set
            len_path += 1
        return -1
