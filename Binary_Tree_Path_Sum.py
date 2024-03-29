# Lintcode 376//Easy

# Description
# Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

# A valid path is from root node to any of the leaf nodes.

# Example
# Example 1:

# Input:
# {1,2,4,2,3}
# 5
# Output: [[1, 2, 2],[1, 4]]
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
# Example 2:

# Input:
# {1,2,4,2,3}
# 3
# Output: []
# Explanation:
# The tree is look like this:
# 	     1
# 	    / \
# 	   2   4
# 	  / \
# 	 2   3
# Notice we need to find all paths from root node to leaf nodes.
# 1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5 
# There is no one satisfying it.

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

# Solution 1: Recursion
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        # 注意审题：必须包含root node
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == target:
                return [[target]]
            return []
        res = []
        left_path = self.binary_tree_path_sum(root.left, target-root.val)
        if len(left_path) > 0:
            res += [[root.val] + p for p in left_path]
        right_path = self.binary_tree_path_sum(root.right, target-root.val)
        if len(right_path) > 0:
            res += [[root.val] + p for p in right_path]
        return res

# Solution 2: DFS
class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        # 注意审题：必须是从root到leaf node的path
        # Questions to ask:
        # 1. What is the range of values in the binary tree
        # 通过Testing case得知node.val可以小于0
        if root is None:
            return []
        from collections import deque
        stack = deque([root])
        path = deque([[root.val]])
        path_sum = deque([root.val])
        res = []
        while len(stack) > 0:
            node = stack.popleft()
            p = path.popleft()
            s = path_sum.popleft()
            print(p, s, node.val)
            if node.left is None and node.right is None: # leaf node 
                if s == target:
                    res.append(p)
            else: # not leaf node
                if node.right is not None:
                    stack.append(node.right)
                    path.append(p+[node.right.val]) # list.append() 返回值为None
                    path_sum.append(s+node.right.val)
                if node.left is not None:
                    print('left not none')
                    stack.append(node.left)
                    path.append(p+[node.left.val])
                    path_sum.append(s+node.left.val)
        return res
