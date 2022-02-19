# Lintcode 2506//Easy

# Description
# You will get a string s which consisting of lowercase letters a-z, left parentheses '(' and right parentheses ')'.

# Your task is to remove as few parentheses as you can so that the parentheses in s is valid.

# You need to return a valid string.

# Because of the answer may be more than one, so you can return any of them.

# "()", "(())", "()()", "(())()" are valid parentheses strings, and ")(", "(()", "()()(", "()())" are not valid parentheses strings.

# A string without parentheses(such as：abcd) or a empty string "" is also a valid string.
# You can only remove parentheses, other operations will not be allowed.

# Example
# Example 1:

# Input:

# s = "a(b(c(de)fgh)"
# Output:

# "a(b(cde)fgh)"
# Explanation:

# There are 3 corrcect answers: "ab(c(de)fgh)"，"a(bc(de)fgh)"，"a(b(cde)fgh)"。
# You can return any of them.

# Example 2:

# Input:

# s = "((("
# Output:

""
# Explanation:

# A empty string "" is also a valid string.

class Solution:
    """
    @param s: A string with lowercase letters and parentheses
    @return: A string which has been removed invalid parentheses
    """
    def removeParentheses(self, s):
        # write your code here.
        invalid_left_parentheses_pos, invalid_right_parentheses_pos = [], []
        for (i, c) in enumerate(s):
            if c == '(':
                invalid_left_parentheses_pos.append(i)
            elif c == ')':
                if len(invalid_left_parentheses_pos) > 0:
                    invalid_left_parentheses_pos.pop(-1)
                else:
                    invalid_right_parentheses_pos.append(i)
        res = ''
        for (i, c) in enumerate(s):
            if i in invalid_left_parentheses_pos or i in invalid_right_parentheses_pos:
                continue
            res += c
        return res

