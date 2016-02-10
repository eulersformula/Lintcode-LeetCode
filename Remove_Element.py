#Given an array and a value, remove all occurrences of that value in place and return the new length.
#The order of elements can be changed, and the elements after the new length don't matter.

#Example
#Given an array [0,4,4,0,0,2,4,4], value=4
#return 4 and front four elements of the array is [0,0,0,2]

#Method 1: Direct operation. Be careful that array length changes after each deletion!
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        st, lenA = 0, len(A)
        while st < lenA:
            if A[st] == elem:
                del A[st]
                lenA -= 1
            else:
                st += 1
        return len(A)
