# Lintcode 310//Easy//Tesla

# Description
# Now the question gives a string number A.
# The string number B is a deformation of A, formed by alternating the digits of the string number A.
# In order, it is the first digit of the right digit of A, the first digit of the left digit, the second digit of the right digit ..... and so on to obtain the string number B.A.

# 0<=A<=1e200

# Example
# input: "12345678"
# output:"81726354"

class Solution:
    """
    @param a: the integer discrible in problem
    @return: the integer after distortion
    """
    def distortion(self, a: str) -> str:
        # Questions to ask:
        # 1. Can a be empty? If so should I directly return the empty string?
        if len(a) <= 1:
            return a
        res = ''
        st, ed = 0, len(a) - 1
        while st < ed:
            res += a[ed]
            ed -= 1
            res += a[st]
            st += 1
        if st == ed:
            res += a[st]
        return res

# 注意奇偶性
