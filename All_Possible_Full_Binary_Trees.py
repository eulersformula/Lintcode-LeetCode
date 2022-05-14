# Lintcode 1588//Medium//Google

# Description
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Return a list of all possible full binary trees with N nodes. Each element of the answer is the root node of one possible tree.

# Each node of each tree in the answer must have node.val = 0.

# You may return the final list of trees in any order.

# 1 <= N <= 20

# Example
# Example 1:

# [0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0
# Explanation:

# Example 2:

# Input：8
# Output：[]
# Explanation：No full binary tree satisfies conditions.

# 不知道为什么Lintcode过不了，Leetcode可以过

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Solution 1: Recursion (Time limit exceeded when n = 17)

class Solution:
    """
    @param n: An integer
    @return: A list of root
    """
    def allPossibleFBT(self, n):
        # write your code here.
        if n == 0:
            return []
        if n == 1:
            root = TreeNode(0)
            return [root] # 一开始写return root，没有写成List导致错误
        res = []
        for i in range(1, n-1):
            n_left, n_right = i, n-i-1
            left_root_ls = self.allPossibleFBT(n_left)
            right_root_ls = self.allPossibleFBT(n_right)
            for left_root in left_root_ls:
                for right_root in right_root_ls:
                    root = TreeNode(0)
                    root.left = left_root
                    root.right = right_root
                    res.append(root)
        return res

# Solution 2: Recursion + DP
class Solution(object):
    def allPossibleFBT(self, n):
        # write your code here.
        cached_res = []
        if n == 0:
            return []
        root = TreeNode(0)
        if n == 1:
            return [root]
        cached_res.append([])
        cached_res.append([root])
        for idx in range(2, n+1):
            res = []
            for i in range(1, idx-1):
                n_left, n_right = i, idx-i-1
                left_root_ls, right_root_ls = cached_res[n_left], cached_res[n_right]
                for left_root in left_root_ls:
                    for right_root in right_root_ls:
                        root = TreeNode(0)
                        root.left = left_root
                        root.right = right_root
                        res.append(root)
            cached_res.append(res)
        return cached_res[n]

