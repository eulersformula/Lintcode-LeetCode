# Lintcode 88//Medium

# Description
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

# Assume two nodes are exist in tree.

# Example

# Example 1:
# Input:
# tree = {1}
# A = 1
# B = 1
# Output:
# 1
# Explanation:
# For the following binary tree（only one node）:
#         1
# LCA(1,1) = 1

# Example 2:
# Input:
# tree = {4,3,7,#,#,5,6}
# A = 3
# B = 5
# Output:
# 4
# Explanation:
# For the following binary tree:
#      4
#     / \
#    3   7
#       / \
#      5   6
# LCA(3, 5) = 4

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# SOLUTION 1
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        # Questions to ask:
        # 1. Is it possible that A or/and B is not in the tree?
        # 2. Can A and B be the same node? If so, should this node just be returned?
        # 3. If one node is a parent of the other, should this parent node be returned?
        if root == None:
            return None
        if A == B:
            return A
        if A == root or B == root:
            return root
        parent_map = {root:None} # Missing this line originally
        nodes = [root]
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.left is not None:
                parent_map[node.left] = node
                nodes.append(node.left)
            if node.right is not None:
                parent_map[node.right] = node
                nodes.append(node.right)
        parent_list_A = []
        parent = A
        while parent in parent_map:
            parent_list_A.append(parent)
            parent = parent_map[parent]
        parent_list_B = []
        parent = B
        while parent in parent_map:
            parent_list_B.append(parent)
            parent = parent_map[parent]
        max_idx = min(len(parent_list_A), len(parent_list_B)) + 1
        res = parent_list_A[-1]
        for idx in range(2, max_idx):
            idx = -idx
            if parent_list_A[idx] == parent_list_B[idx]:
                res = parent_list_A[idx]
            else:
                break
        return res

# SOLUTION 2: RECURSION
