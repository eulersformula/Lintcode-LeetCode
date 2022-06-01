# Leetcode 32//Hard

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.

# DP解法：TLE
from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        valid = deque([('', 0)]) # keep a one dimensional array of valid configs so far
        max_len = 0
        for ss in s:
            len_valid = len(valid)
            for _ in range(len(valid)):
                tmp, l = valid.popleft()
                if len(tmp) == 0 and l > 0:
                    max_len = max(max_len, l)
                if ss == '(':
                    valid.append((tmp+ss, l+1))
                else:
                    if len(tmp) == 0 or tmp[-1] != '(':
                        continue
                    valid.append((tmp[:-1], l+1))
            valid.appendleft(('', 0))
            # print(valid)
        for (v, l) in valid:
            if len(v) == 0:
                max_len = max(max_len, l)
        return max_len
