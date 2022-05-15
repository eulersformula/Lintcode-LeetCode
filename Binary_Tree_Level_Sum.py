# Lintcode 482//Easy//Google

# Description
# Given a binary tree and an integer which is the depth of the target level.

# Calculate the sum of the nodes in the target level.

# Example
# Example 1:

# Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},2
# Output：5 
# Explanation：
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#    /       \
#   8         9
# 2+3=5
# Example 2:

# Input：{1,2,3,4,5,6,7,#,#,8,#,#,#,#,9},3
# Output：22
# Explanation：
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#    /       \
#   8         9
# 4+5+6+7=22


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

# SOLUTION 1: BFS. TIME LIMIT EXCEEDED

class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def max_depth_tree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth_tree(root.left), self.max_depth_tree(root.right))

    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        # Questions to ask:
        # 1. Is it guaranteed that all values are valid (namely no None) in that level?
        # 2. Is it possible that level is greater than the depth of the tree?
        # 3. What is the range of level? Can it be 0 or negative?
        if root is None or level <= 0:
            return 0
        if level > self.max_depth_tree(root):
            return 0
        node_ls = [root]
        node_cnt = 0
        node_cnt_st, node_cnt_ed = 2 **(level-1), 2 ** level - 1
        res = 0
        no_valid_node = False
        while len(node_ls) > 0 and node_cnt < node_cnt_ed:
            node = node_ls.pop(0)
            node_cnt += 1
            if node is None:
                node_ls.append(None)
                node_ls.append(None)
                continue
            if node.left is not None:
                node_ls.append(node.left)
            else:
                node_ls.append(None)
            if node.right is not None:
                node_ls.append(node.right)
            else:
                node_ls.append(None)
            if node_cnt >= node_cnt_st and node_cnt <= node_cnt_ed:
                res += node.val
        return res
 
# SOLUTION 2: RECURSION
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """

    def level_sum(self, root: TreeNode, level: int) -> int:
        if root is None or level <= 0:
            return 0
        if level == 1:
            return root.val
        return self.level_sum(root.left, level-1) + self.level_sum(root.right, level-1)

# SOLUTION 3: BFS
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """

    def level_sum(self, root: TreeNode, level: int) -> int:
        # write your code here
        # Questions to ask:
        # 1. Is it guaranteed that all values are valid (namely no None) in that level?
        # 2. Is it possible that level is greater than the depth of the tree?
        if root is None or level <= 0:
            return 0
        cur_level = 0
        node_ls = [root]
        while len(node_ls) > 0:
            cur_level += 1
            if cur_level < level:
                tmp_node_ls = []
                while len(node_ls) > 0:
                    node = node_ls.pop(0)
                    if node.left is not None:
                        tmp_node_ls.append(node.left)
                    if node.right is not None:
                        tmp_node_ls.append(node.right)
                node_ls = tmp_node_ls
            elif cur_level == level:
                res = 0
                for node in node_ls:
                    res += node.val
                return res   
        return 0
# 需补充解法：DFS
        
