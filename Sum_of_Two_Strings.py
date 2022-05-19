# Lintcode 1343//Easy//Quora

# Description
# Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.

# A and B are strings which are composed of numbers
# Example
# Example1:
# Input:
# A = "99"
# B = "111"
# Output: "11010"
# Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"
# Example2:
# Input:
# A = "2"
# B = "321"
# Output: "323"
# Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"

# T: O(max(m, n)); S: O(1) if not consideing the space needed for result

class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return the sum of two strings
    """
    def sumof_two_strings(self, a: str, b: str) -> str:
        # write your code here
        if a == '' and b == '':
            return ''
        if a == '':
            return int(b)
        if b == '':
            return int(a)
        res = ''
        common_len = min(len(a), len(b))
        for idx in range(common_len):
            idx_a = len(a) - idx - 1
            idx_b = len(b) - idx - 1
            s = int(a[idx_a]) + int(b[idx_b])
            res = str(s) + res
        if len(a) > len(b):
            res = a[:(len(a) - common_len)] + res
        elif len(b) > len(a):
            res = b[:(len(b) - common_len)] + res
        return res
