#There is a fence with n posts, each post can be painted with one of the k colors.
#You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#Return the total number of ways you can paint the fence.

#Notice
#n and k are non-negative integers.

#Example
#Given n=3, k=2 return 6
#      post 1,   post 2, post 3
#way1    0         0       1 
#way2    0         1       0
#way3    0         1       1
#way4    1         0       0
#way5    1         0       1
#way6    1         1       0

#Idea: How many ways ---in most scenarios---> DP. This is a classic DP problem actually!
#There are two ways to paint n fences from all the ways to paint (n - 1) fences:
#Case 1. If the last two of the (n - 1) fences are already of the same color, we have (k - 1) colors to paint fence n. These will all make the last two of n fences to be of different color (namely still this case).
#Case 2. If the last two of the (n - 1) fences are of different colors, we can either paint fence n using the same color of fence (n - 1) (now becomes Case 1), or we can paint fence n using a different color with (k - 1) ways (stays at Case 2). 
#We need to record the number of ways of these two scenarios seperately.

#Base cases to consider:
#1. If n == 0 or k == 0, return 0
#2. If n == 1, k != 0, case 1 is k, case 2 is 0.

class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        if n == 0 or k == 0:
            return 0
        f, g = k, 0
        for _ in xrange(n - 1):
            f, g = (f + g) * (k - 1), f
        return f + g
