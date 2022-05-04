# Lintcode 1080//Easy//Intuit

# Description
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

# The length of each dimension in the given grid does not exceed 50.

# Example
# Example 1:

# input:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# output : 6.
# Explanation : Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# input: [[0,0,0,0,0,0,0,0]]
# output : 0

from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        # Write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        max_area = 0
        while True:
            # find an island
            coord = None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        coord = i, j
                        break
            if coord is None:
                break
            coord_list = [coord]
            cur_area = 0
            while len(coord_list) > 0:
                i, j = coord_list.pop()
                if grid[i][j] == 1:
                    grid[i][j] = 0 #第一次赋值写成了==导致死循环
                    cur_area += 1
                    if i > 0:
                        coord_list.append((i-1, j))
                    if i < len(grid) - 1:
                        coord_list.append((i+1, j))
                    if j > 0:
                        coord_list.append((i, j-1))
                    if j < len(grid[0]) - 1:
                        coord_list.append((i, j+1))
            if cur_area > max_area:
                max_area = cur_area
        return max_area
