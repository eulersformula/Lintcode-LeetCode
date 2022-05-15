# Lintcode 595//Easy//Google//NetEase

# Description
# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

# Example
# Example 1:

# Input:
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Output:3
# Explanation:
# Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:

# Input:
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1
# Output:2
# Explanation:
# Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.

# SOLUTION 1: RECURSION (TIME LIMIT EXCEEDED)

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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive_with_root(self, root:TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None: # leaf node
            return 1
        left_res, right_res = 1, 1 # 此处一开始误写成0, 0。至少consecutive为1。
        if root.left is not None and root.left.val == root.val+1: # ==误写成=
            left_res += self.longest_consecutive_with_root(root.left)
        if root.right is not None and root.right.val == root.val+1:
            right_res += self.longest_consecutive_with_root(root.right) # 笔误：root.right写成root.left
        return max(left_res, right_res)
            
    def longest_consecutive(self, root: TreeNode) -> int:
        # write your code here
        if root is None:
            return 0
        return max(self.longest_consecutive_with_root(root), \
                    self.longest_consecutive(root.left), \
                    self.longest_consecutive(root.right))
