#Find the Nth number in Fibonacci sequence.
#A Fibonacci sequence is defined as follows:
#The first two numbers are 0 and 1.
#The i th number is the sum of i-1 th number and i-2 th number.
#The first ten numbers in Fibonacci sequence is:
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

#Example: 
#Given 1, return 0
#Given 2, return 1
#Given 10, return 34

#Method 1: Recursion. Very bad implementation!
#Time Complexity: T(n) = T(n-1) + T(n-2), which is exponential. 
#Space Complexity: O(n) if we consider the function call stack size, otherwise O(1).

#Method 2: DP. 
#Time Complexity: O(n). Space Complexity: O(1).

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n <= 0:
            return None
        if n == 1:
            return 0
        seq = [0, 1]
        for i in xrange(2, n):
            seq[0], seq[1] = seq[1], seq[0] + seq[1]
        return seq[1]
