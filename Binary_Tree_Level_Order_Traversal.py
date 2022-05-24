# Description
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).)

# The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
# The number of nodes does not exceed 20.
# Example
# Example 1:

# Input:

# tree = {1,2,3}
# Output:

# [[1],[2,3]]
# Explanation:

#    1 
#   / \ 
#  2   3 
# it will be serialized {1,2,3}
# Example 2:

# Input:

# tree = {1,#,2,3} 
# Output:

# [[1],[2],[3]] 
# Explanation:

# 1 
#  \ 
#   2 
#  / 
# 3 
# it will be serialized {1,#,2,3}

# Challenge
# Challenge 1: Using only 1 queue to implement it.
# Challenge 2: Use BFS algorithm to do it.

from typing import (
    List,
)
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

# SOLUTION 1: BFS. T: O(n); S: O(2^n); n is number of nodes. TODO: 使用deque减少S至O(1).
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def level_order(self, root: TreeNode) -> List[List[int]]:
        # write your code here
        node_ls = [root]
        res = []
        while len(node_ls) > 0:
            cur_node_ls = []
            cur_res = []
            for node in node_ls:
                if node is not None:
                    cur_res.append(node.val)
                    cur_node_ls.append(node.left)
                    cur_node_ls.append(node.right)
            if len(cur_res) > 0:
                res.append(cur_res)
            else:
                break
            node_ls = cur_node_ls
        return res
