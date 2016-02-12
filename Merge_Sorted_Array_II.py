#Merge two given sorted integer array A and B into a new sorted integer array.

#Example
#A=[1,2,3,4]
#B=[2,4,5,6]

#return [1,2,2,3,4,4,5,6]

#Method 1: Time complexity O(n), Space complexity O(n)

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        res = []
        i, j, lenA, lenB = 0, 0, len(A), len(B)
        while i < lenA and j < lenB:
            if A[i] <= B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        if i == lenA:
            return res + B[j:]
        if j == lenB:
            return res + A[i:]

#Challenge
#How can you optimize your algorithm if one array is very large and the other is very small?
#In this case, might use binary search to insert the small array. Time complexity will be O(m log(n)).
