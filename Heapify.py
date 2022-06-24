# Lintcode 130//Medium

# Description
# Given an integer array, heapify it into a min-heap array.

# For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

# What is heap? What is heapify? What if there is a lot of solutions?

# Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
# Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
# Return any of them.
# Example
# Example 1

# Input : [3,2,1,4,5]
# Output : [1,2,3,4,5]
# Explanation : return any one of the legitimate heap arrays
# Challenge
# O(n) time complexity

# Sift Up: T: O(n logn)
class Solution:
    """
    @param a: Given an integer array
    @return: nothing
    """
    # For index i, maximum time complexity is O(h_i) = O(log i)
    # Total time complexity is O(log n!) ~ O(n)
    def heapify(self, a: List[int]):
        # write your code here
        for idx in range(len(a)): # if a is empty nothing executed
            # parent of i is (i-1)//2
            p = (idx-1) // 2
            while idx > 0 and a[idx] < a[p]:
                a[idx], a[p] = a[p], a[idx]
                idx = p
                p = (idx-1) // 2
   
