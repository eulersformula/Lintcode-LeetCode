# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

# Example 1:


# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:


# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:


# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
 

# Constraints:

# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.

# BFS: T: O(n); S: O(n)

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        if x == root.val or y == root.val:
            return False
        nodes = deque([root])
        parent = {}
        while len(nodes) > 0:
            cur_len = len(nodes)
            for _ in range(cur_len):
                node = nodes.popleft() # BFS pop left!
                if node.left is not None:
                    if node.left.val in [x, y]:
                        parent[node.left.val] = node
                    nodes.append(node.left)
                if node.right is not None:
                    if node.right.val in [x, y]:
                        parent[node.right.val] = node
                    nodes.append(node.right)
            if len(parent) == 1:
                return False
            if len(parent) == 2 and parent[x] != parent[y]:
                return True
        return False
 
