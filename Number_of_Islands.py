# Lintcode 433//Easy//Facebook//Amazon//Zenefits//Microsoft//Uber//Google

# Description
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

# Find the number of islands.

# Example
# Example 1:

# Input:
# [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,1],
#   [0,0,0,0,0],
#   [0,0,0,0,1]
# ]
# Output:
# 3

# Example 2:

# Input:
# [
#   [1,1]
# ]
# Output:
# 1

from typing import (
    List,
)

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        # write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n_islands = 0
        while True:
            island_coord = -1, -1
            # Variables declared in for loop is tmp, cannot be called outside loops
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        island_coord = i, j
                        break # 此处break只跳出当前循环，不能跳出外循环
                if island_coord != (-1, -1):
                    break
            if island_coord == (-1, -1):
                break
            # grid[i][j] is 1
            # print(i,j)
            l = [island_coord]
            while len(l) > 0:
                i, j = l.pop(0) # pop函数默认argument -1
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if i > 0:
                        l.append((i-1, j))
                    if i < len(grid)-1:
                        l.append((i+1, j))
                    if j > 0:
                        l.append((i, j-1))
                    if j < len(grid[0]) - 1:
                        l.append((i, j+1))
            n_islands += 1
        return n_islands
