# Lintcode 1101//Medium//Amazon

# Description
# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of a layer of a binary tree is defined as the distance between the nodes at both ends of the layer. Note that the empty node between the nodes at both ends is also counted as the length.

# The answer will be in the range of 32-bit signed integer.

# Example
# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,#,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
		
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,#,#,#,#,#,#,7).

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

# T: O(n); S: O(n); n is number of nodes

class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """
    def width_of_binary_tree(self, root: TreeNode) -> int:
        # Write your code here
        if root is None:
            return 0
        queue = [(root, 0)]
        max_width = 1
        while len(queue) > 0:
            cur_queue = []
            cur_width = queue[-1][1] - queue[0][1] + 1
            print(queue)
            if cur_width > max_width:
                max_width = cur_width
            for (node, idx) in queue:
                if node.left is not None:
                    cur_queue.append((node.left, idx<<1))
                if node.right is not None:
                    cur_queue.append((node.right, (idx<<1)+1)) # python里位运算优先级低于arithmetic
            queue = cur_queue
        return max_width
