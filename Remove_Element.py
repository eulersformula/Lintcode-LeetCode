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

#Method 2: Head-tail swap, like partition in Quicksort (probably this is intended to be used).
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        lenA = len(A)
        if elem not in A:
            return lenA
        st, ed = 0, lenA - 1
        while st <= ed:
            if A[st] == elem:
                A[st], A[ed] = A[ed], A[st]
                ed -= 1
                lenA -= 1
            else:
                st += 1
        st = A.index(elem) #list/string.index() returns the FIRST appearance of element. It will raise an error if not found.
        del A[st:]
        return lenA
