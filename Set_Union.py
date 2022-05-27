# Lintcode 1396//Medium//Facebook
# Description
# There is a list composed by sets. If two sets have the same elements, merge them. Returns the last remaining collection.

# The number of sets n <=1000.
# The number of elements for each set m <= 100.
# The element must be a non negative integer and not greater than 100000.
# Example
# Example 1:

# Input :list = [[1,2,3],[3,9,7],[4,5,10]]
# Output:2 .
# Explanation:There are 2 sets of [1,2,3,9,7] and [4,5,10] left.
# Example 2:

# Input:list = [[1],[1,2,3],[4],[8,7,4,5]]
# Output :2
# Explanation:There are 2 sets of [1,2,3] 


from typing import (
    List,
)

# 初刷答案
class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def set_union(self, sets: List[List[int]]) -> int:
        # Write your code here
        if len(sets) <= 1:
            return len(sets)
        from collections import deque
        sets = deque([set(s) for s in sets])
        cnt = 0
        while cnt < len(sets):
            s0 = sets.popleft()
            found_merge = False
            for i in range(len(sets)):
                if sets[i] & s0:
                    sets[i] |= s0
                    cnt = 0
                    found_merge = True
                    break
            if found_merge:
                cnt = 0
            else:
                sets.append(s0)
                cnt += 1
        return len(sets)
