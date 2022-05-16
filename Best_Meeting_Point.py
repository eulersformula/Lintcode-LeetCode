# Lintcode 912//Hard//Twitter

# Description
# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# Example
# Example 1:

# [1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]

# Output:
# 6

# Explanation:
# The point `(0,2)` is an ideal meeting point, as the total travel distance of `2 + 2 + 2 = 6` is minimal. So return `6`.
# Example 2:

# [1,1,0,0,1],[1,0,1,0,0],[0,0,1,0,1]

# Output:
# 14

# T: O((n + m)c); S: O(c)

from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def get_distance_sum(self, target, coord_dict):
        dist_sum = 0
        for coord in coord_dict:
            dist_sum += coord_dict[coord] * abs(coord - target)
        return dist_sum

    def min_total_distance(self, grid: List[List[int]]) -> int:
        # Write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        x_coord_dict, y_coord_dict = dict(), dict()
        min_x, min_y, max_x, max_y = [None] * 4
        for (i, l) in enumerate(grid):
            for (j, v) in enumerate(l):
                if v == 1:
                    if i not in x_coord_dict:
                        x_coord_dict[i] = 0
                    x_coord_dict[i] += 1
                    if j not in y_coord_dict:
                        y_coord_dict[j] = 0
                    y_coord_dict[j] += 1
                    if min_x is None or i < min_x:
                        min_x = i
                    if min_y is None or j < min_y:
                        min_y = j
                    if max_x is None or i > max_x:
                        max_x = i
                    if max_y is None or j > max_y:
                        max_y = j 
        min_distance_x = None
        for coord in range(min_x, max_x+1):
            cur_distance_x = self.get_distance_sum(coord, x_coord_dict)
            if min_distance_x is None or cur_distance_x < min_distance_x:
                min_distance_x = cur_distance_x
        min_distance_y = None
        for coord in range(min_y, max_y+1):
            cur_distance_y = self.get_distance_sum(coord, y_coord_dict)
            if min_distance_y is None or cur_distance_y < min_distance_y:
                min_distance_y = cur_distance_y
        return min_distance_x + min_distance_y
