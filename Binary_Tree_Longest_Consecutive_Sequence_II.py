# Lintcode 614//Google//Medium

# Description
# Given a binary tree, find the length(number of nodes) of the longest consecutive sequence(Monotonic and adjacent node values differ by 1) path.
# The path could be start and end at any node in the tree

# Example
# Example 1:

# Input:
# {1,2,0,3}
# Output:
# 4
# Explanation:
#     1
#    / \
#   2   0
#  /
# 3
# 0-1-2-3
# Example 2:

# Input:
# {3,2,2}
# Output:
# 2
# Explanation:
#     3
#    / \
#   2   2
# 2-3

# 一开始Solution：最后一个case TLE
from lintcode import (
    TreeNode,
)
from collections import deque
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
    def find_longest_from_root(self, root: TreeNode, dv: int) -> int:
        if root is None:
            return 0
        max_res = 1
        stack = deque([[root, 1]])
        while len(stack) > 0:
            node, n_consec = stack.pop()
            if node.right is not None and node.right.val - node.val == dv:
                stack.append([node.right, n_consec+1])
            else:
                max_res = max(n_consec, max_res)
            if node.left is not None and node.left.val - node.val == dv:
                stack.append([node.left, n_consec+1])
            else:
                max_res = max(n_consec, max_res)
        return max_res

    def longest_consecutive2(self, root: TreeNode) -> int:
        # write your code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        res, dv_left, dv_right = 1, None, None
        if (root.left is not None) and \
            (root.left.val - root.val) in [1, -1]:
            dv_left = root.left.val - root.val
            best_left_res = self.find_longest_from_root(root.left, dv_left)
            res = max(res, 1+best_left_res)
            # print(best_left_res)
        if (root.right is not None) and \
            (root.right.val - root.val) in [1, -1]:
            dv_right = root.right.val - root.val
            best_right_res = self.find_longest_from_root(root.right, dv_right)
            res = max(res, 1+best_right_res)
            # print(best_right_res)
        if dv_left is not None and dv_right is not None and \
            dv_left * dv_right == -1:
            res = max(res, best_left_res+best_right_res+1)
        return max(res, self.longest_consecutive2(root.left), 
            self.longest_consecutive2(root.right))
