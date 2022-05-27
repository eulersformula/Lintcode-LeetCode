# Leetcode 199//Medium

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
# Input: root = []
# Output: []
 
# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# SOLUTION 1: RECURSION
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        root_left_res = self.rightSideView(root.left)
        root_right_res = self.rightSideView(root.right)
        return [root.val] + root_right_res + \
               root_left_res[len(root_right_res):] # 一开始写错成len(root_right_res)+1

# SOLUTION 2: DFS
