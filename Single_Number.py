#Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

#Example: Given [1,2,2,1,3,4,3], return 4

#Challenge: One-pass, constant extra space.

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        if len(A) == 0: #I don't think this special case makes sense. However, need to include this case to pass Lintcode testcases.
            return 0
        res = A[0]
        for n in A[1:]:
            res ^= n  
        return res
        
#The key point is to use using XOR. 
#Property: a XOR b == 1 if and only if a + b == 1. (a XOR b = (a + b) % 2)
#Thus for any number a, a XOR a = 0.
#XOR has exchangeability.
