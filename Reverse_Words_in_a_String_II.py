# Lintcode 927//Medium//Amazon//Uber//Microsoft
# Description
# Given an input string array, reverse the array word by word. A word is defined as a sequence of non-space strings.

# The input character array does not contain leading or trailing spaces and the words are always separated by a single space.

# Example
# Example1

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example2

# Input: "a b c"
# Output: "c b a"
# Challenge
# Could you do it in-place without allocating extra space?

# SOLUTION 1:
class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverse_words(self, str: str) -> str:
        return ' '.join(reversed(str.split()))

# SOLUTION 2: In place. T: O(n); S: O(1)

class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverse_words(self, str: str) -> str:
        # write your code here
        # 两次遍历。第一次从头到尾交换，第二次只交换每个词内部顺序。
        # python 无法实现str的in place改变因为是immutable。
        if len(str) <= 1:
            return str
        res = list(str)
        st, ed = 0, len(res) - 1
        while st < ed:
            res[st], res[ed] = res[ed], res[st]
            st += 1
            ed -= 1
        head_idx = 0
        n_chars = len(res)
        for idx in range(n_chars):
            if res[idx] == ' ':
                st, ed = head_idx, idx - 1
                while st < ed:
                    res[st], res[ed] = res[ed], res[st]
                    st += 1
                    ed -= 1
                head_idx = idx + 1
        ed = n_chars - 1
        while head_idx < ed:
            res[head_idx], res[ed] = res[ed], res[head_idx]
            head_idx += 1
            ed -= 1
        return ''.join(res)
