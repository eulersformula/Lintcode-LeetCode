#Given a binary tree, return the preorder traversal of its nodes' values.

#Example:
#Given:
#    1
#   / \
#  2   3
# / \
#4   5
#return [1,2,4,5,3]

#Challenge: Can you do it without recursion?

#Method 1: Recursion
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if root == None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

#Method 2: Non-recursion: stack. Master this well!
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root == None:
            return []
        stack = [root]
        res = []
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return res
