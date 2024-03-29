# Lintcode 1314//Easy//Google

# Description
# Given an integer, write a function to determine if it is a power of two.

# Example
# Example

# Input: n = 3
# Output: false

# SOLUTION 1: RECURSION. T: O(log n); S: O(log n)
class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def is_power_of_two(self, n: int) -> bool:
        # Write your code here
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return self.is_power_of_two(n//2)

# SOLUTION 2: BIT OPERATION. T: O(1); S: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 二进制仅有一位为1。减1后1位变0，右侧所有0变1
        # 对于其他数，第一位1后仍有1，减1后首位1仍为1
        return n and not (n & (n-1)) # 注意0和负数的情况

