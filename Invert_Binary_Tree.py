# Leetcode 226//Easy

#######################################################################################################################################
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off. #
#######################################################################################################################################

#Invert a binary tree.
#Example
#  1         1
# / \       / \
#2   3  => 3   2
#   /       \
#  4         4

# Lintcode无返回值版本

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

#Method 1: Recursion
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root != None:
            root.left, root.right = root.right, root.left
            self.invertBinaryTree(root.left)
            self.invertBinaryTree(root.right)

#Method 2: Iterative (How to assess evrery node in a tree without recursion? Store all nodes in a list using BFS!)
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        allNodes = []
        if root != None:
          allNodes.append(root)
        while allNodes != []:
          node = allNodes.pop(0)
          if node.left != None:
            allNodes.append(node.left)
          if node.right != None:
            allNodes.append(node.right)
          node.left, node.right = node.right, node.left
        return root

# Leetcode有返回值版本
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        # 注意如果分两行执行需要设置tmp variable，因为会导致left/right branch发生改变
        root.left, root.right =\
        self.invertTree(root.right), self.invertTree(root.left) 
        return root
