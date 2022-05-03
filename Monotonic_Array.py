# Lintcode 1745//Easy//Facebook

# Description
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return true if and only if the given array A is monotonic.Otherwise, return false.

# 1 \leq A.length \leq 500001≤A.length≤50000
# -100000 \leq A[i] \leq 100000−100000≤A[i]≤100000

# Example
# Example 1:
# Input: [1,2,2,3]
# Output: true

Example 2:
# Input: [1,3,2]
# Output: false

from typing import (
    List,
)

class Solution:
    """
    @param a: a array
    @return: is it monotonous
    """
    def is_monotonic(self, a: List[int]) -> bool:
        # Write your code here.
        # Questions to ask:
        # 1. Can a be empty? If so, is it monotonic?
        if len(a) <= 1:
            return True
        increasing, decreasing = False, False
        for i in range(1, len(a)):
            if a[i] == a[i-1]:
                continue
            if a[i] > a[i-1]:
                if decreasing:
                    return False
                if not increasing:
                    increasing = True
            elif a[i] < a[i-1]:
                if increasing:
                    return False
                if not decreasing:
                    decreasing = True
        return True

# Other solutions: sorted array, 单调栈
