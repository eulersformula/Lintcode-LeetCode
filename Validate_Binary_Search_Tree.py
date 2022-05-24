# Leetcode 98//Medium
# Lintcode 95//Medium

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 
# Example 1:

# Input: root = [2,1,3]
# Output: true
# Example 2:

# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

#Constraints:

# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# SOLUTION 1: RECURSION. T: O(n)

class Solution:
    def get_inorder_traversal_val_list(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.get_inorder_traversal_val_list(root.left) + [root.val] +  self.get_inorder_traversal_val_list(root.right)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        node_ls = self.get_inorder_traversal_val_list(root)
        for i in range(len(node_ls)-1):
            if node_ls[i] >= node_ls[i+1]:
                return False
        return True
 
