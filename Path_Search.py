# Lintcode 1647//Medium

# Description
# Given the undirected graph of n points and m edges, the point are numbered 0, 1, 2...(n-1). Output all the simple routes starting from point S to point T, and the output simple routes are in dictionary order sorting. When a route does not pass a node more than once, it is called a simple route.
# Example: If there are three routes from point 0 to point 2: [0,1,2], [0,2] and [0,1,3,2]
# Then the output is:
# [[0,1,2],[0,1,3,2],[0,2]]

# n ≤ 10
# m ≤ 50
# Example
# Example 1:

# Input: n=4, G=[[0,1],[0,2],[1,2],[1,3],[3,2]], S=0, T=2,
# Output: [[0,1,2],[0,1,3,2],[0,2]]
# Explanation: There are three routes from 0 to 2:
# [0,1,2],[0,1,3,2],[0,2]
# Example 2:

# Input: n=4, G=[[0,1],[2,3]], S=0, T=2,
# Output: []
# Explanation: There isn't any route from 0 to 2.

from typing import (
    List,
)
from collections import deque

# SOLUTION 1: BFS。复杂度需要分析。

class Solution:
    """
    @param n: The number of points
    @param g: The description of graph
    @param s: The point S
    @param t: The point T
    @return: output all the paths from S to T
    """
    def get_path(self, n: int, g: List[List[int]], s: int, t: int) -> List[List[int]]:
        # Write your code here
        neighbors = {i: set([]) for i in range(n)}
        # 易错点：
        # 1. undirected graph，neighbor要相互加
        # 2. 加edge以后并不一定所有的node都在dict里，可以先根据总node的数目初始化一个空的dict。
        for (i, j) in g: 
            if i not in neighbors:
                neighbors[i] = set([])
            neighbors[i].add(j)
            if j not in neighbors:
                neighbors[j] = set([])
            neighbors[j].add(i)
        # print(neighbors)
        paths = deque([([s], set([s]))])
        res = []
        while len(paths) > 0:
            n_path = len(paths)
            for _ in range(n_path):
                path, visited_nodes = paths.popleft()
                if path[-1] == t:
                    res.append(path)
                    continue
                for n in neighbors[path[-1]]:
                    if n not in visited_nodes:
                        paths.append([path+[n], visited_nodes|set([n])])
        return sorted(res) #此处不sort过不了testing，但是题目并没有要求sort

# SOLUTION 2: DFS。复杂度需要分析。

