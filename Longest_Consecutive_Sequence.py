#Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

#Clarification
#Your algorithm should run in O(n) complexity.

#Example
#Given [100, 4, 200, 1, 3, 2],
#The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

#First solution: more obvious but O(nlogn) time.
#Sort the original list. Note that there are 3 cases when comparing with previous number: prev + 1, prev, others. It's easy to leave out prev.
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        num = sorted(num)
        glob, local, prev = 0, 0, None
        for n in num:
            if prev == None:
                local = 1
            elif n == prev + 1:
                local += 1
            elif n == prev:
                continue
            else:
                glob = max(glob, local)
                local = 1
            prev = n
        glob = max(glob, local)
        return glob

#Second solution: O(n) time.
#Use hashtable. This will first eliminate duplicated numbers and leave only distinct numbers.

