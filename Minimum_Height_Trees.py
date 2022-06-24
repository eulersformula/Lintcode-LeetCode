# Leetcode 310//Medium

# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# Example 1:

# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
# Example 2:

# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]

# Constraints:

# 1 <= n <= 2 * 10^4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.

# Trial 1: TLE

class Solution:
    def dfs(self, node_1, node_2, neighbors):
        if neighbors[node_1][node_2] == -1:
            if len(neighbors[node_2]) == 1: # leaf node, only one neighbor
                neighbors[node_1][node_2] = 1
                return 1
            res = 0
            for neighbor in neighbors[node_2]:
                if neighbor != node_1:
                    res = max(res, self.dfs(node_2, neighbor, neighbors))
            res += 1
            neighbors[node_1][node_2] = res
        return neighbors[node_1][node_2]
        
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 未考虑边角情况 n = 1
        if n == 1:
            return [0]
        neighbors = dict()
        for (a, b) in edges:
            if a not in neighbors:
                neighbors[a] = dict()
            if b not in neighbors:
                neighbors[b] = dict()
            neighbors[a][b] = -1
            neighbors[b][a] = -1
        # print(neighbors)
        min_height = -1
        nodes = neighbors.keys()
        res = []
        for node in nodes:
            height = max([self.dfs(node, neighbor, neighbors) \
                            for neighbor in neighbors[node].keys()])
            if min_height == -1 or height < min_height:
                min_height = height
                res = [node]
            elif height == min_height:
                res.append(node)
        # print(neighbors)
        return res
