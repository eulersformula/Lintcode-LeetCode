# Lintcode 1892//Medium

# Description
# It's an easy mine-sweeping game.You are given a n*m matrix as the map of game.
# Each position has a value (0 or 1, 1 means there is no thunder, 0 means there is thunder).
# You are given a start position (x, y). X is the number of rows and Y is the number of columns(x, y are both counting from 0).
# If there is no mine at current position then you can reach in four directions, otherwise, can't reach the new position.
# Returns all accessible coordinates.

# 0<n,m<=200.
# You should return an array in any order. The array includes all reachable position coordinates.

# Example
# Example 1

# input: 
# [[1,0,0,0],[1,0,0,0],[0,1,1,1],[0,1,0,0]]
# [0,1]
# output: 
# [[0,1]]
# explain: 
# There is 0 at [0,1], so you can't move,then the answer is [[0,1]].
# Example 2

# input: 
# [[1,0,0,0],[1,0,0,0],[0,1,1,1],[0,1,0,0]]
# [1,0]
# output: 
# [[0,0],[1,0],[1,1],[2,0],[0,1]]
# explain: 
# You can arrive [[0,0],[1,1],[2,0]] from [1,0], then arrive [[0,1]] from [0,0]. 

# Questions to ask:
# 1. Is it possible to have a zero size matrix? If so, what to return?
# 2. Is it possible for the start position to be out side of the mine_map? If so, what to return?
# 3. How should I organize the returned coordinates? For example should I sort them?


from typing import (
    List,
)

# SOLUTION 1: RECURSION
class Solution:
    """
    @param mine_map: an matrix represents the map.
    @param start: the start position.
    @return: return an array including all reachable positions.
    """
    def mine_sweeping(self, mine_map: List[List[int]], start: List[int]) -> List[List[int]]:
        # write your code here
        x, y = start[0], start[1]
        n_rows, n_cols = len(mine_map), len(mine_map[0])
        if x < 0 or x >= n_rows or y < 0 or y >= n_cols:
            return []
        if mine_map[x][y] == 0:
            mine_map[x][y] = 2
            return [[x, y]]
        res = [[x, y]] # current location is a 1
        mine_map[x][y] = 2
        res += self.mine_sweeping(mine_map, [x-1, y])
        res += self.mine_sweeping(mine_map, [x+1, y])
        res += self.mine_sweeping(mine_map, [x, y-1])
        res += self.mine_sweeping(mine_map, [x, y+1])
        return res

#SOLUTION 2: BFS
class Solution:
    """
    @param mine_map: an matrix represents the map.
    @param start: the start position.
    @return: return an array including all reachable positions.
    """
    def mine_sweeping(self, mine_map: List[List[int]], start: List[int]) -> List[List[int]]:
        n_rows, n_cols = len(mine_map), len(mine_map[0])
        coords = [start]
        while len(coords) > 0:
            cur_x, cur_y = coords.pop(0)
            if mine_map[cur_x][cur_y] == 0:
                mine_map[cur_x][cur_y] = 2
            elif mine_map[cur_x][cur_y] == 1:
                mine_map[cur_x][cur_y] = 2
                if cur_x > 0 and mine_map[cur_x-1][cur_y] != 2:
                    coords.append([cur_x-1, cur_y])
                if cur_x < n_rows - 1 and mine_map[cur_x+1][cur_y] != 2:
                    coords.append([cur_x+1, cur_y])
                if cur_y > 0 and mine_map[cur_x][cur_y-1] != 2:
                    coords.append([cur_x, cur_y-1])
                if cur_y < n_cols - 1 and mine_map[cur_x][cur_y+1] != 2:
                    coords.append([cur_x, cur_y+1])
        res = []
        for x in range(n_rows):
            for y in range(n_cols):
                if mine_map[x][y] == 2:
                    res.append([x, y])
        return res
