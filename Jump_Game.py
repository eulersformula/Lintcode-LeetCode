#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.

#Example
#A = [2,3,1,1,4], return true.
#A = [3,2,1,0,4], return false.

#Note
#This problem have two method which is Greedy and Dynamic Programming.
#The time complexity of Greedy method is O(n).
#The time complexity of Dynamic Programming method is O(n^2).

#Method 1: Dynamic Programming. Time Complexity: O(n^2), Space Complexity: O(n).

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        lA = len(A)
        dp = [False] * lA
        dp[0] = True
        for i in xrange(0, lA):
            if dp[i]:
                for j in xrange(1, A[i] + 1):
                    if i + j < lA:
                        dp[i + j] = True
        return dp[-1]
