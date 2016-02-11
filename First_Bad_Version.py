#The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

#You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

#Example
#Given n = 5:

#isBadVersion(3) -> false
#isBadVersion(5) -> true
#isBadVersion(4) -> true

#This problem is nearly identical to "First Position of Target", which clearly should use binary search.
#I just can't understand why LintCode ranked the difficulty of this problem as 'Median' but the other as 'Easy'!

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
    def findFirstBadVersion(self, n):
        #I am not checking if n < 1 or there is no bad version. Should ask the interviewer if asked in an interview.
        st, ed = 1, n
        while st < ed - 1:
            mid = (st + ed) / 2
            if SVNRepo.isBadVersion(mid):
                ed = mid
            else:
                st = mid
        if SVNRepo.isBadVersion(st):
            return st
        return ed
