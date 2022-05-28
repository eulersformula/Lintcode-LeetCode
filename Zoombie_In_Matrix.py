# Lintcode 598//Medium
# Description
# Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

# Example
# Example 1:

# Input:
# [[0,1,2,0,0],
#  [1,0,0,2,1],
#  [0,1,0,0,0]]
# Output:
# 2
# Example 2:

# Input:
# [[0,0,0],
#  [0,0,0],
#  [0,0,1]]
# Output:
# 4

from typing import (
    List,
)

class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def helper(self, grid: List[List[int]], i: int, j: int) -> bool:
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) \
               and grid[i][j] == 0:
            grid[i][j] = 1
            return True
        return False

    def zombie(self, grid: List[List[int]]) -> int:
        # write your code here
        # Questions to ask:
        # 1. Does the zombie turn only one people into zombie every day, or
        # all possible ones?
        # 2. Can grid be empty or a row of grid be empty?
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1
        from collections import deque
        zombie_locs = set()
        n_human = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    zombie_locs.add((i, j))
                elif grid[i][j] == 0:
                    n_human += 1
        # print(zombie_locs)
        n_days = 0
        dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while n_human > 0 and len(zombie_locs) > 0:
            cur_locs = set()
            for (i, j) in zombie_locs:
                for (dx, dy) in dxdy:
                    if self.helper(grid, i+dx, j+dy):
                        cur_locs.add((i+dx, j+dy))
                        n_human -= 1
            print(grid)
            print(cur_locs)
            zombie_locs = cur_locs
            n_days += 1
        if n_human > 0:
            return -1
        return n_days

# Lintcode 官方
class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        if m == 0:
            return 0

        q = []
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    q.append((i, j))

        d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        days = 0
        while q:
            days += 1
            new_q = []
            for node in q:
                for k in xrange(4):
                    x = node[0] + d[k][0]
                    y = node[1] + d[k][1]
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 0:
                        grid[x][y] = 1
                        new_q.append((x, y))
            q = new_q

        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 0:
                    return -1

        return days - 1
