# Leetcode 43//Medium

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
 
# Constraints:

# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def string_to_integer(self, s: str) -> str:
        # 记住：ord(c): ordinal of a character; chr(n): a character (string) from an integer n
        res = 0
        for l in s:
            res *= 10
            res += ord(l) - ord('0')
        return res
    
    def integer_to_str(self, n: int) -> str:
        if n == 0:
            return '0'
        digits = []
        while n > 0:
            d = n % 10
            digits.append(chr(ord('0')+d))
            n = n // 10
        return ''.join(digits[::-1])
             
    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.string_to_integer(num1)
        num2 = self.string_to_integer(num2)
        return self.integer_to_str(num1*num2)
