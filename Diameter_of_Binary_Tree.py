# Lintcode 1181//Easy//Facebook//Google
# Leetcode 543//Easy

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

# 二刷：T: O(n); S: O(h), worst case O(n)
class Solution:
    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return (0, 0)
        left_max_depth, left_max_diameter = self.helper(root.left)
        right_max_depth, right_max_diameter = self.helper(root.right)
        max_depth = 1 + max(left_max_depth, right_max_depth)
        max_diameter = left_max_depth + right_max_depth
        max_diameter = max(max_diameter, left_max_diameter, right_max_diameter)
        # print('node val', root.val, max_depth, max_diameter)
        return (max_depth, max_diameter)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1]
 
