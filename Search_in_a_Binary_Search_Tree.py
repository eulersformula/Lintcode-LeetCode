# Lintcode 1524//Easy

# Description
# Given the root of a binary search tree (BST) and a value.

# Return the node whose value equals the given value. If such node doesn't exist, return null.

# Example
# Example 1:

# Input: value = 2
#         4
#        / \
#       2   7
#      / \
#     1   3
# Output: node 2
# Example 2:

# Input: value = 5
#         4
#        / \
#       2   7
#      / \
#     1   3
# Output: null

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

# Solution 1: Recursion
class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def search_b_s_t(self, root: TreeNode, val: int) -> TreeNode:
        # Write your code here.
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.search_b_s_t(root.left, val)
        return self.search_b_s_t(root.right, val)

# Solution 2: Traversal. T: O(n); S: O(1). n is the number of nodes
class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def search_b_s_t(self, root: TreeNode, val: int) -> TreeNode:
        # Write your code here.
        if root is None:
            return None
        while root is not None:
            if root.val == val:
                return root
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return None
