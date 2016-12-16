#Count how many 1 in binary representation of a 32-bit integer.

#Example
#Given 32, return 1
#Given 5, return 2
#Given 1023, return 9

#Challenge: If the integer is n bits with m 1 bits. Can you do it in O(m) time?

#Solution 1: Normal method, O(n) time, n is the number of bits
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        cnt = 0
        for i in xrange(32):
            cnt += num & 1
            num = num >> 1
        return cnt

#Solution 2: [x & (x - 1)] will make the last bit 1 to be 0. O(m) time, m is the number of bits of 1. This doesn't quite seem to work for python.
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        cnt = 0
        while num:
            num = num & (num - 1)
            cnt += 1
        return cnt
