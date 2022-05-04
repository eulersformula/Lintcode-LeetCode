# Lintcode 1618//Medium//Goldman Sachs

# Description
# Given a csv file a, using vector to represent, each string contains m words, indicating a certain line of the csv file. Now it is required to right-align the words in each column of the file and output the new csv file (return vector)

# Example
# Example 1:

# a = ["ac,abc,a","a,bb,ccc"]
# return ["ac,abc,  a"," a, bb,ccc"]

# Input:
# ac,abc,a
# a,bb,ccc
# Output:
# ac,abc,  a
#  a, bb,ccc

# Example 2:

# a = ["acde,adbc,a","a,b,cc"]
# return ["acde,adbc,  a","    a,  bb,ccc"]

# Input:
# acde,adbc,a
# a,bb,ccc
# Output:
# acde,adbc,  a
#    a,  bb,ccc

from typing import (
    List,
)

class Solution:
    """
    @param a: the csv file a
    @return: return the processed file
    """
    def processing_file(self, a: List[str]) -> List[str]:
        # Write your code here
        # Questions to ask:
        # 1. Can a be empty?
        # 2. Is it guaranteed that each string in the list contains the same number of commas?
        if len(a) == 0 or len(a[0]) == 0:
            return a
        line = a[0].split(',')
        max_chars = [len(x) for x in line]
        for line in a[1:]:
            line = line.split(',')
            cur_max_chars = [len(x) for x in line]
            max_chars = [max(x, y) for (x, y) in zip(max_chars, cur_max_chars)]
        res = []
        for line in a:
            line = line.split(',')
            cur_res = []
            for (i, entry) in enumerate(line):
                entry = ' ' * (max_chars[i] - len(entry)) + entry
                cur_res.append(entry)
            res.append(','.join(cur_res))
        return res
