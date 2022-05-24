# Lintcode 1360//Medium//Bloomberg//Microsoft//LinkedIn

# Description
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Example
# Example1

# Input: {1,2,2,3,4,4,3}
# Output: true
# Explanation:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# This binary tree {1,2,2,3,4,4,3} is symmetric
# Example2

# Input: {1,2,2,#,3,#,3}
# Output: false
# Explanation:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# This is not a symmetric tree
# Challenge
# Could you solve it both recursively and iteratively?

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

# SOLUTION 1: BFS. T: O(n); S: O(max(n_i)); n_i is the number of nodes in level i

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def get_inorder_traversal(self, root: TreeNode):
        if root is None:
            return [None]
        return self.get_inorder_traversal(root.left) + [root.val] + self.get_inorder_traversal(root.right)
    
    def is_symmetric(self, root: TreeNode) -> bool:
        # Write your code here
        # Questions to ask:
        # 1. What if root is None
        if root is None:
            return True
        from collections import deque
        node_ls = deque()
        node_ls.append(root)
        while len(node_ls) > 0:
            l = len(node_ls)
            cur_vals = []
            for _ in range(l):
                node = node_ls.popleft() # 此处注意是popleft，pop会返回最后一个元素
                if node is None:
                    cur_vals.append(None)
                else:
                    cur_vals.append(node.val)
                    node_ls.append(node.left)
                    node_ls.append(node.right)
            if len(cur_vals) > 1:
                st, ed = 0, len(cur_vals) - 1
                while st < ed:
                    if cur_vals[st] != cur_vals[ed]:
                        return False
                    st += 1
                    ed -= 1
        return True
 
# TODO: RECURSIVE
