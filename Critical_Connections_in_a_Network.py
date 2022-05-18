# Leetcode 1192//Hard

# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

# Example 1:
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# Example 2:
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
 
# Constraints:

# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.

# SOLUTION 1: TIME LIMIT EXCEEDED
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # convert connections to set
        new_connections = set()
        for (i, j) in connections:
            if (j, i) in new_connections:
                continue
            new_connections.add((i, j))
        connections = new_connections
        neighbors = dict()
        for (i, j) in connections:
            if i not in neighbors:
                neighbors[i] = set()
            neighbors[i].add(j)
            if j not in neighbors:
                neighbors[j] = set()
            neighbors[j].add(i)
        res = []
        for (i, j) in connections:
            # if there is only one connection attached to i or j, it must be critical
            if len(neighbors[i]) == 1 or len(neighbors[j]) == 1:
                res.append([i, j])
                continue
            # find another path from i to j
            reachable = set([i])
            bfs_nodes = set([i])
            reached = False
            while len(bfs_nodes) > 0:
                # bfs level
                cur_bfs_nodes = set()
                for q in bfs_nodes:
                    if q == j:
                        reached = True
                    for k in neighbors[q]:
                        if (q, k) == (i, j) or (k, q) == (i, j):
                            continue
                        if k in reachable:
                            continue
                        cur_bfs_nodes.add(k) # 该行一开始写错，cur_bfs_nodes写成了bfs_nodes
                        reachable.add(k)
                bfs_nodes = cur_bfs_nodes
            if not reached:
                res.append([i, j])
        return res  
