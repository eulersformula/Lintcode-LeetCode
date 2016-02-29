#Given a binary tree, return all root-to-leaf paths.

#Example:
#Given the following binary tree:
#   1
# /   \
#2     3
# \
#  5
#All root-to-leaf paths are:
#[
#  "1->2->5",
#  "1->3"
#]

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        if root == None: #Don't forget this case!!
            return []
        if root.left == None and root.right == None:
            return [`root.val`]
        leftPaths = [`root.val` + '->' + x for x in self.binaryTreePaths(root.left)] if root.left != None else []
        rightPaths = [`root.val` + '->' + x for x in self.binaryTreePaths(root.right)] if root.right != None else []
        return leftPaths + rightPaths
