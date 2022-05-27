# Leetcode 95//Medium

# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# Example 2:
# Input: n = 1
# Output: [[1]]
 

# Constraints:
# 1 <= n <= 8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def copyTree(self, root: Optional[TreeNode], v: int=0) -> Optional[TreeNode]: # 学习variable type declaration & default value
        # v: how much to increase/decrease for all the nodes
        if root is None:
            return None
        new_root = TreeNode(root.val+v)
        new_root.left = self.copyTree(root.left, v)
        new_root.right = self.copyTree(root.right, v)
        return new_root # 错误：new_root写成root
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Questions to ask:
        # 1. What to return? A list of root nodes?
        # 错误：return type应是list of nodes, 不是list of lists
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(1)]
        # trees[i] corresponds to all of the configurations of i
        trees = [[None], [TreeNode(1)]] + [None] * (n-1)
        for r in range(2, n+1):
            res = []
            for v in range(1, r+1):
                # [1,...,v-1] [v] [v+1,...,r]
                for lr in trees[v-1]:
                    for rr in trees[r-v]:
                        root = TreeNode(v)
                        root.left = self.copyTree(lr)
                        root.right = self.copyTree(rr, v)
                        res.append(root)
            trees[r] = res
        return res
