# Lintcode 1908//Hard//Meituan
# Description
# Given a string represents a Boolean expression only including "true","false","or","and".
# Your task is to calculate the result of the expression by returning "true" or "false".
# If the expression is not valid, you need to return a string "error".

# We promise that there are no more than 1000010000 elements in the expression.
# There are only 4 kinds of elements in the expression : "true", "false", "and", "or".

# Example
# Example 1

# Input：
# "true and false"
# Output：
# "false"
# Example 2

# Input：
# "true or"
# Output：
# "error"

# SOLUTION 1: RECURSION
from typing import List
class Solution:
    """
    @param expression: a string that representing an expression
    @return: the result of the expression
    """
    def evaluate_and_seq(self, expression_ls: List[str]) -> str:
        if len(expression_ls) % 2 == 0:
            return 'error'
        st, ed = 0, len(expression_ls) - 1
        while (st <= ed):
            st_val, ed_val = expression_ls[st], expression_ls[ed]
            if st % 2 == 0:
                if st_val not in ['true', 'false'] or \
                   ed_val not in ['true', 'false']:
                    return 'error'
                if st_val == 'false' or ed_val == 'false':
                    return 'false'
            elif st_val != 'and' or ed_val != 'and':
                return 'error'
            st += 1
            ed -= 1
        return 'true'

    def evaluate_expression_ls(self, expression_ls: List[str]) -> None:
        if len(expression_ls) == 0:
            return 'error'
        if len(expression_ls) == 1:
            if expression_ls[0] == 'true':
                return 'true'
            if expression_ls[0] == 'false':
                return 'false'
            return 'error'
        # find first or
        idx = 0
        len_ls = len(expression_ls)
        while idx < len_ls and expression_ls[idx] != 'or':
            idx += 1
        if idx == len_ls:
            return self.evaluate_and_seq(expression_ls)
        left_res = self.evaluate_expression_ls(expression_ls[:idx])
        right_res = self.evaluate_expression_ls(expression_ls[(idx+1):])
        if left_res == 'error' or right_res == 'error':
            return 'error'
        if left_res == 'true' or right_res == 'true':
            return 'true'
        return 'false'

    def evaluation(self, expression: str) -> str:
        # write your code here
        expression_ls = expression.split()
        return self.evaluate_expression_ls(expression_ls)
 
# SOLUTION 2: MONOTONIC STACK
