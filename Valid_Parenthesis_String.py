# Lintcode 1089//Medium

# Description
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# The string size will be in the range [1, 100].
# Example
# Example 1:
# 	Input:  "()"
# 	Output:  true

	
# Example 2:
#  Input: "(*)"
# 	Output:  true
	
# Explanation:
# 	'*' is empty.
	
# Example 3:
# 	Input: "(*))"
# 	Output: true
	
# 	Explanation:
# 	use '*' as '('.

# Hard aspect: The use of the position of the stars for canceling out the parentheses.

class Solution:
    """
    @param s: the given string
    @return: whether this string is valid
    """
    def check_valid_string(self, s):
        # Write your code here
        left_pos, right_pos, star_pos = [], [], []
        for (i, c) in enumerate(s):
            if c == '(':
                left_pos.append(i)
            elif c == ')':
                if len(left_pos) > 0:
                    left_pos.pop(-1)
                else:
                    right_pos.append(i)
            elif c == '*':
                star_pos.append(i)
        while len(left_pos) > 0:
            p = left_pos[-1]
            if len(star_pos) > 0 and star_pos[-1] > p:
                star_pos.pop(-1)
                left_pos.pop(-1)
            else:
                return False 
        while len(right_pos) > 0:
            p = right_pos[0]
            if len(star_pos) > 0 and star_pos[0] < p:
                star_pos.pop(0)
                right_pos.pop(0)
            else:
                return False
        return True
