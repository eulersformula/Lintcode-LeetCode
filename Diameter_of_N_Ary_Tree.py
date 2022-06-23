# Leetcode 1522//Medium

# Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.
# The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.
# (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)
 
# Example 1:

# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# Explanation: Diameter is shown in red color.
# Example 2:

# Input: root = [1,null,2,null,3,4,null,5,null,6]
# Output: 4

# Example 3:

# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 7

 
# Constraints:
# The depth of the n-ary tree is less than or equal to 1000.
# The total number of nodes is between [0, 10^4].

"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

# T: O(n); S: O(h), worst case O(n)

class Solution:
    def helper(self, root: Optional[DirectedGraphNode]) -> Tuple[int, int]:
        # return maximum depth and max diameter in this tree
        max_depth_ls, max_diameter = [0, 0], 0
        for node in root.neighbors:
            cur_max_depth, cur_max_diameter = self.helper(node)
            if cur_max_depth >= max_depth_ls[1]:
                max_depth_ls = [max_depth_ls[1], cur_max_depth]
            elif cur_max_depth_ls > max_depth_ls[0]:
                max_depth_ls = [cur_max_depth, max_depth_ls[1]]
            max_diameter = max(max_diameter, cur_max_diameter)
        max_diameter = max(max_diameter, sum(max_depth_ls))
        max_depth = 1 + max(max_depth)
        return (max_depth, max_diameter)
        
    def diameterOfNaryTree(self, root: Optional[DirectedGraphNode]) -> int:
        return self.helper(root)[1]
