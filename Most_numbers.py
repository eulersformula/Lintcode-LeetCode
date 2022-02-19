# Lintcode 1910//Easy
# Description
# Find the number with the most occurrences in the given array.
# When the number of occurrences is the same, return the smallest one.

# Example
# Example 1:

# Input: 
# [1,1,2,3,3,3,4,5]
# Output: 
# 3
# Example 2:

# Input: 
# [1]
# Output: 
# 1

class Solution:
    """
    @param array: An array.
    @return: An interger.
    """
    def find_number(self, array):
        # Write your code here.
        cnts = {}
        for a in array:
            if a not in cnts:
                cnts[a] = 0
            cnts[a] += 1
        max_occ, res = 0, -1
        for (k, v) in cnts.items():
            if v > max_occ:
                res = k
                max_occ = v
            elif v == max_occ:
                res = min(res, k)
        return res
