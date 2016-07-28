#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

#Example
#For example,
#If n = 4 and k = 2, a solution is:
#[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

#Method 1: Backtracking problem! Use recursion
#1. It's easy to forget corner cases.
#2. Each element in the returned list should be a list.

class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):
        
        if k == 0 or n < k:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        return  self.combine(n - 1, k) + [l + [n] for l in self.combine(n - 1, k - 1)]
