# Lintcode 860//Medium//Amazon

# Description
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if and only if one island has the same shape as another island (and not rotated or reflected).

# Notice that:

# 11
# 1
# and

#  1
# 11
# are considered different island, because we do not consider reflection / rotation.

# The length of each dimension in the given grid does not exceed 50.

# Example
# Example 1:

# Input: 
#   [
#     [1,1,0,0,1],
#     [1,0,0,0,0],
#     [1,1,0,0,1],
#     [0,1,0,1,1]
#   ]
# Output: 3
# Explanation:
#   11   1    1
#   1        11   
#   11
#    1
# Example 2:

# Input:
#   [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,0,1,1],
#     [0,0,0,1,1]
#   ]
# Output: 1

from typing import (
    List,
)

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        # write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        island_configs = set()
        while True:
            island_coord = None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        island_coord = i, j
                        break
            if island_coord is None:
                break
            cur_island_coords = set()
            min_x, min_y = None, None
            island_coords = [island_coord]
            while len(island_coords) > 0:
                i, j = island_coords.pop()
                if grid[i][j] == 1:
                    grid[i][j] = 0 # FORGOT TO DO ZERO!
                    cur_island_coords.add((i, j))
                    min_x = min(min_x, i) if min_x is not None else i
                    min_y = min(min_y, j) if min_y is not None else j
                    if i > 0:
                        island_coords.append((i-1, j))
                    if i < len(grid) - 1:
                        island_coords.append((i+1, j))
                    if j > 0:
                        island_coords.append((i, j-1))
                    if j < len(grid[0]) - 1:
                        island_coords.append((i, j+1))
            normalized_island_coords = set()
            for (i,j) in cur_island_coords:
                normalized_island_coords.add((i-min_x, j-min_y))
            island_configs.add(frozenset(normalized_island_coords)) # ONLY IMMUTABLE OBJECTS IN PYTHON IS HASHABLE
        return len(island_configs)
