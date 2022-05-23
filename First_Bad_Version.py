# Leetcode 278//Easy
# Lintcode 74//Medium

#The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

#You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

#Example
#Given n = 5:

#isBadVersion(3) -> false
#isBadVersion(5) -> true
#isBadVersion(4) -> true

# SOLUTION: 二分法查找，保证左指针指向0，右指针指向1且二者相邻，则右指针必指向第一个1
# T: O(log n); S: O(1)

#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n: int) -> int:
        if SVNRepo.isBadVersion(1):
            return 1
        st, ed = 1, n
        while st < ed - 1:
            mid = (st + ed) // 2
            if SVNRepo.isBadVersion(mid):
                ed = mid
            else:
                st = mid
        return ed
