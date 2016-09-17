#Merge two given sorted integer array A and B into a new sorted integer array.

#Example
#A=[1,2,3,4]
#B=[2,4,5,6]
#return [1,2,2,3,4,4,5,6]

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        if A == []:
            return B
        if B == []:
            return A
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        if i == len(A):
            res += B[j:]
        else:
            res += A[i:]
        return res
