"""
Description
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

You can not divide any item into small pieces.

Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
"""

def backPack(self, m, A):
    if A == None or len(A) == 0:
        return 0
    record = [0] * (m + 1)
    for i in xrange(A[0], m + 1):
        record[i] = A[0]
    for n in xrange(1, len(A)):
        tmpRecord = [0] * (m + 1)
        for i in xrange(min(m + 1, A[n])):
            tmpRecord[i] = record[i]
        for i in xrange(A[n], m + 1):
            tmpRecord[i] = max(A[n] + record[i - A[n]], record[i])
        record = tmpRecord
    return max(record)
