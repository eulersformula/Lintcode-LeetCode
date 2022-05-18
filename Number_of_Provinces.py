# Leetcode 547//Medium


# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

# Example 1:

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:

# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 
# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

# T: O(n); S: O(n)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0:
            return 0
        n = len(isConnected)
        remaining_nodes = set(range(n))
        n_provinces = 0
        while len(remaining_nodes) > 0:
            node = remaining_nodes.pop()
            node_set = set([node])
            while len(node_set) > 0:
                new_node_set = set([])
                for i in node_set:
                    cur_visited_nodes = set([])
                    for j in remaining_nodes:
                        if isConnected[i][j] == 1:
                            cur_visited_nodes.add(j)
                    remaining_nodes -= cur_visited_nodes
                    new_node_set |= cur_visited_nodes
                node_set = new_node_set
            n_provinces += 1
        return n_provinces
  
  # TODO: Disjoint Sets
