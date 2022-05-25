# Lintcode 878//Medium//Google//Amazon

# Description
# Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

# Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

# The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

# The right-most node is also defined by the same way with left and right exchanged.

# Example
# Example 1:

# Input: {1,#,2,3,4}
# Output: [1,3,4,2]
# Explanation: 
#   1
#    \
#     2
#    / \
#   3   4
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].
# Example 2:

# Input: {1,2,3,4,5,6,#,#,#,7,8,9,10}
# Output: [1,2,4,7,8,9,10,6,3]
# Explanation: 
#           1
#      /          \
#     2            3
#    / \          / 
#   4   5        6   
#      / \      / \
#     7   8    9  10  
#   The left boundary are node 1,2,4. (4 is the left-most node according to definition)
#   The leaves are node 4,7,8,9,10.
#   The right boundary are node 1,3,6,10. (10 is the right-most node).
#   So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

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

# TODO: 清理code

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundary_of_binary_tree(self, root: TreeNode) -> List[int]:
        # write your code here
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        # left boundary
        left_boundary = [root]
        if root.left is not None:
            node = root.left
            left_boundary.append(root.left)
            while node is not None:
                if node.left is not None:
                    left_boundary.append(node.left)
                    node = node.left
                elif node.right is not None:
                    left_boundary.append(node.right)
                    node = node.right
                else:
                    break
        # right boundary
        right_boundary = [root]
        if root.right is not None:
            node = root.right
            right_boundary.append(root.right)
            while node is not None:
                if node.right is not None:
                    right_boundary.append(node.right)
                    node = node.right
                elif node.left is not None:
                    right_boundary.append(node.left)
                    node = node.left
                else:
                    break
        right_boundary = right_boundary[::-1] # [::-1] applicable to empty list
        # get leaf nodes
        from collections import deque
        leaves = []
        node_ls = deque()
        node_ls.append(root)
        while len(node_ls) > 0:
            node = node_ls.pop()
            if node.left is None and node.right is None:
                leaves.append(node)
            if node.right is not None:
                node_ls.append(node.right)
            if node.left is not None:
                node_ls.append(node.left)   
        if len(left_boundary) > 0 and len(leaves) > 0:
            trunc_idx = None
            for (i, node) in enumerate(left_boundary):
                if node == leaves[0]:
                    trunc_idx = i
                    break
            if trunc_idx is not None:
                left_boundary = left_boundary[:trunc_idx]
        if len(right_boundary) > 0 and len(leaves) > 0:
            trunc_idx = None
            for (i, node) in enumerate(leaves):
                if node == right_boundary[0]:
                    trunc_idx = i
                    break
            if trunc_idx is not None:
                leaves = leaves[:trunc_idx]
        if len(left_boundary) > 0 and len(right_boundary) > 0:
            trunc_idx = None
            for (i, node) in enumerate(right_boundary):
                if node == left_boundary[0]:
                    trunc_idx = i
                    break
            if trunc_idx is not None:
                right_boundary = right_boundary[:trunc_idx]
        return [x.val for x in left_boundary] + [x.val for x in leaves] + [x.val for x in right_boundary]
