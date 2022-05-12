# Lintcode 1181//Easy//Facebook//Google

# Description
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree.

# The length of path between two nodes is represented by the number of edges between them.

# Example
# Example 1:

# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Example 2:

# Input:[2,3,#,1]
# Output:2

# Explanation:
#       2
#     /
#    3
#   /
# 1

from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def depth_of_binary_tree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is None:
            return 1 + self.depth_of_binary_tree(root.right)
        if root.right is None:
            return 1 + self.depth_of_binary_tree(root.left)
        return 1 + max(self.depth_of_binary_tree(root.left), self.depth_of_binary_tree(root.right))

    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        # write your code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is None:
            return 1 + self.depth_of_binary_tree(root.right)
        if root.right is None:
            return 1 + self.depth_of_binary_tree(root.left)
        return 2 + self.depth_of_binary_tree(root.left) + self.depth_of_binary_tree(root.right)

      
 # TODO: BFS solution
