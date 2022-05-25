# Lincode 596//Easy//Microsoft//Yelp

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

# SOLUTION 1: RECURSION

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def sum_tree(self, root:TreeNode):
        if root is None:
            return None
        res = root.val
        if root.left is not None:
            res += self.sum_tree(root.left)
        if root.right is not None:
            res += self.sum_tree(root.right)
        return res
        
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        right_min_subtree = self.find_subtree(root.right)
        right_min_sum = self.sum_tree(right_min_subtree)
        left_min_subtree = self.find_subtree(root.left)
        left_min_sum = self.sum_tree(left_min_subtree)
        cur_sum = root.val
        if root.left is not None:
            cur_sum += self.sum_tree(root.left)
        if root.right is not None:
            cur_sum += self.sum_tree(root.right)
        if left_min_sum is not None and left_min_sum < cur_sum:
            root = left_min_subtree
            cur_sum = left_min_sum
        if right_min_sum is not None and right_min_sum < cur_sum:
            root = right_min_subtree
            cur_sum = right_min_sum
        return root

# SOLUTION 2: ITERATIVE
