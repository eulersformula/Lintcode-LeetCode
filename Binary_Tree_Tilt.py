# Lintcode 1172//Easy//Indeed

# Description
# Given a binary tree, return the tilt of the whole tree.

# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

# The tilt of the whole tree is defined as the sum of all nodes' tilt.

# 1.The sum of node values in any subtree won't exceed the range of 32-bit integer.
# 2.All the tilt values won't exceed the range of 32-bit integer.

# Example
# Example 1:

# Input: 
# {1,2,3}
# Output: 1

# Explanation: 
#          1
#        /   \
#       2     3
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# **Example 2: **

# Input：
# {1,1,#,2,3}
# Output：
# 7

# Explanation：
#         1
#       /
#     1
#    /  \
# 2     3

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
    @param root: the root
    @return: the tilt of the whole tree
    """
    def find_sum(self, root:TreeNode) -> int:
        if root is None:
            return 0
        if not hasattr(root, 'sum'):
            res = root.val
            res += root.left.sum if hasattr(root.left, 'sum') else self.find_sum(root.left)
            res += root.right.sum if hasattr(root.right, 'sum') else self.find_sum(root.right)
            root.sum = res
        return root.sum

    def find_tilt(self, root: TreeNode) -> int:
        # Write your code here
        if root is None:
            return 0
        return abs(self.find_sum(root.left) - self.find_sum(root.right)) + \
                    self.find_tilt(root.left) + self.find_tilt(root.right)


# 需补充解: 使用其他函数返回多值
