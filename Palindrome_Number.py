# Lintcode 491//Easy
# Leetcode 9//Easy

# Description
# Check a positive number is a palindrome or not.

# A palindrome number is that if you reverse the whole number you will get exactly the same number.

# It's guaranteed the input number is a 32-bit integer, but after reversion, the number may exceed the 32-bit integer.

# Example
# Example 1:

# Input:11
# Output:true
# Example 2:

# Input:1232
# Output:false
# Explanation:
# 1232!=2321

# SOLUTION 1 T: O(n); S: O(n)
class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def is_palindrome(self, num: int) -> bool:
        # write your code here
        return str(num) == str(num)[::-1]
