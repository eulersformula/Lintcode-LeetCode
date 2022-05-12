# Lintcode 1237//Easy//Google

# Description
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

# Example
# Input:
# [[0,0],[1,0],[2,0]]

# Output:
# 2

# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

from typing import (
    List,
)

class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """
    def number_of_boomerangs(self, points: List[List[int]]) -> int:
        # Write your code here
        if len(points) <= 2:
            return 0
        dist = [[0 for _ in range(len(points))] for _ in range(len(points))]
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(len(points)):
                xj, yj = points[j]
                dist[i][j] = (xj - xi) ** 2 + (yj - yi) ** 2 # does not matter if to take square root
        res = 0
        for i in range(len(points)):
            vals = dict()
            for j in range(len(points)):
                if dist[i][j] not in vals:
                    vals[dist[i][j]] = 0
                vals[dist[i][j]] += 1
            for v, c in vals.items():
                res += c * (c - 1)
        return int(res)
