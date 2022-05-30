# Leetcode 508//Medium

# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

# Example 1:

# Input: root = [5,2,-3]
# Output: [2,-3,4]
# Example 2:

# Input: root = [5,2,-5]
# Output: [2]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTreeSum(self, root:Optional[TreeNode]): 
        # return a tuple. The first is the sum of the root subtree
        # the second is the sum of subtrees and their freqs
        if root is None:
            return None, {}
        if root.left is None and root.right is None: # leaf node
            return root.val, {root.val:1}
        left_sum, left_sum_freqs = self.findTreeSum(root.left)
        right_sum, right_sum_freqs = self.findTreeSum(root.right)
        root_sum = root.val
        if left_sum is not None:
            root_sum += left_sum
        if right_sum is not None:
            root_sum += right_sum
        if len(left_sum_freqs) == 0:
            res = right_sum_freqs
        else:
            res = left_sum_freqs
            for (k, v) in right_sum_freqs.items():
                if k not in res:
                    res[k] = 0
                res[k] += v
        if root_sum not in res:
            res[root_sum] = 0
        res[root_sum] += 1
        return root_sum, res
        
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        _, res = self.findTreeSum(root)
        if len(res) == 0:
            return []
        res = [(k, v) for (k, v) in res.items()]
        res.sort(key=lambda x: -x[1])
        ans = [res[0][0]]
        for (k, v) in res[1:]:
            if v == res[0][1]:
                ans.append(k)
        return ans
