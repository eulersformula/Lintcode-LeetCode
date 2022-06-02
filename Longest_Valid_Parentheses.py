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

# DP解法： T: O(n); S: O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        max_len = 0
        # the longest valid substring ending in index i
        tmp = [0] * len(s)
        for i in range(1, len(s)):
            # print(i)
            # nothing to do for i == 0
            # nothing to do if ss == '(' since it is not valid to end here
            if s[i] == ')':
                if s[i-1] == '(':
                    tmp[i] = 2 + tmp[i-2] if i >= 2 else 2
                else:
                    # s[i-1] == ')', valid from (i-tmp[i-1]) to (i-1)
                    # look at (i-tmp[i-1]-1)
                    idx_to_look = i - tmp[i-1] - 1
                    if idx_to_look >= 0 and s[idx_to_look] == '(':
                        tmp[i] = tmp[i-1] + 2
                        if idx_to_look - 1 >= 0:
                            tmp[i] += tmp[idx_to_look-1]
                max_len = max(max_len, tmp[i])
        return max_len
