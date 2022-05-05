# Lintcode 1911//Medium

# Description
# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
# The distance used in this problem is the Manhattan distance : the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# If there is only land or ocean on the grid, return to -1.

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

# Example
# Example 1:

# Input: 
# grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 
# 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.
# Example 2:

# Input: 
# grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 
# 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.

from typing import (
    List,
)

class Solution:
    """
    @param grid: An array.
    @return: An integer.
    """
    def get_nearest_land_cell_dist(self, land_boundary_coords, water_coords):
        if len(land_boundary_coords) == 0 or len(water_coords) == 0:
            return 0
        max_dist = None
        for (ii, jj) in water_coords:
            # 第一遍实现时没有注意是要到land的最短距离
            min_dist = None
            for (i, j) in land_boundary_coords:
                dist = abs(i-ii) + abs(j-jj)
                if min_dist is None or min_dist > dist:
                    min_dist = dist
            if max_dist is None or max_dist < min_dist:
                max_dist = min_dist
        return max_dist

    def max_distance(self, grid: List[List[int]]) -> int:
        # Write your code here.
        # Questions to ask:
        # 1. Is it possible for values in grid to be all 0's or all 1's?
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        values = set()
        for x in grid:
            for v in x:
                values.add(v)
        if len(values) == 1:
            return -1
        max_dist = None
        while True:
            # Find a 0
            coord = None
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        coord = (i, j)
                        break # break只能跳过当前循环，不能跳过外部循环
                if coord is not None:
                    break
            if coord is None:
                break
            island_boundary_coords, water_coords = set(), set() #可以用set来减少冗余坐标
            coords = [coord]
            while len(coords) > 0:
                i, j = coords.pop(0) # pop()默认是最后一个element，此处需要用pop(0)
                if grid[i][j] == 0:
                    grid[i][j] = 2 # 又把赋值写成了==，从上一行复制粘贴导致错误
                    if (i, j) not in water_coords:
                        water_coords.add((i, j))
                    if i > 0:
                        coords.append((i-1, j))
                    if i < len(grid) - 1:
                        coords.append((i+1, j))
                    if j > 0:
                        coords.append((i, j-1))
                    if j < len(grid[0]) - 1:
                        coords.append((i, j+1))
                elif grid[i][j] == 1 and (i, j) not in land_boundary_coords:
                    land_boundary_coords.add((i, j))
            cur_max_dist = self.get_nearest_land_cell_dist(land_boundary_coords, water_coords)
            if max_dist is None or max_dist < cur_max_dist:
                max_dist = cur_max_dist
        return max_dist
