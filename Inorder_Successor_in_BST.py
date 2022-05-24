# Lintcode 448//Medium//Microsoft//Facebook//Pocket
# Description
# Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

# If the given node has no in-order successor in the tree, return null.

# It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

# Example
# Example 1:

# Input: {1,#,2}, node with value 1
# Output: 2
# Explanation:
#   1
#    \
#     2
# Example 2:

# Input: {2,1,3}, node with value 1
# Output: 2
# Explanation: 
#     2
#    / \
#   1   3
# Binary Tree Representation

# Challenge
# O(h), where h is the height of the BST.

# 性质：root本身和right subtree的node的successor一定在right subtree。left subtree的node的successor可以在left subtree或者root。

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

# 初次答案：T: O(h); S: O(h). TODO: 精简
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def find_left_most_node(self, node):
        if node is None:
            return None
        prev, node = node, node.left
        while node is not None:
            prev, node = node, node.left
        return prev
        
    def inorderSuccessor(self, root, p):
        # write your code here
        if root is None or p is None:
            return None
        if root.val < p.val: # p is on right of root
            if p == root.right: # p is right of root
                return self.find_left_most_node(p.right)
            return self.inorderSuccessor(root.right, p)
        if root == p: # p is the root
            return self.find_left_most_node(root.right) 
        if p.val < root.val: # p is on left of root
            if p.val < root.left.val:
                return self.inorderSuccessor(root.left, p)
            if p == root.left:
                if p.right is None:
                    return root
                return self.find_left_most_node(p.right)
            # consider the scenario that root may be the in order successor of p
            # need to find a root that has a value higher that p
            node = root.left
            while node is not None and node.val < p.val:
                node = node.right
            if node == p:
                if p.right is None:
                    return root
                return self.inorderSuccessor(node, p)
            return self.inorderSuccessor(node, p)
        return None
        
