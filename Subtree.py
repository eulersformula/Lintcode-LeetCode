#You have two every large binary trees: T1, with millions of nodes, and T2, with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of T1.

#Notice
#A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

#Example
#T2 is a subtree of T1 in the following case:
#       1                3
#      / \              / 
#T1 = 2   3      T2 =  4
#        /
#       4
#T2 isn't a subtree of T1 in the following case:
#       1               3
#      / \               \
#T1 = 2   3       T2 =    4
#        /
#       4

#Method 1: Compare root value.
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isIdentical(self, T1, T2):
        if T1 == None and T2 == None:
            return True
        if T1 == None or T2 == None:
            return False
        if T1.val == T2.val:
            return self.isIdentical(T1.left, T2.left) and self.isIdentical(T1.right, T2.right)
        return False
        
    def isSubtree(self, T1, T2):
        # write your code here
        if T2 == None:
            return True
        if T1 == None:
            return False
        flag = False
        if T1.val == T2.val:
            flag = self.isIdentical(T1, T2)
        return flag or self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

#Method 2: Compare tree length.
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isIdentical(self, T1, T2):
        if T1 == None and T2 == None:
            return True
        if T1 == None or T2 == None:
            return False
        if T1.val == T2.val:
            return self.isIdentical(T1.left, T2.left) and self.isIdentical(T1.right, T2.right)
        return False
    
    def nodeCount(self, T):
        if T == None:
            return 0
        return 1 + self.nodeCount(T.left) + self.nodeCount(T.right)
        
    def isSubtree(self, T1, T2):
        if T2 == None:
            return True
        if T1 == None:
            return False
        if self.nodeCount(T1) < self.nodeCount(T2):
            return False
        if self.nodeCount(T1) == self.nodeCount(T2):
            return self.isIdentical(T1, T2)
        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)
