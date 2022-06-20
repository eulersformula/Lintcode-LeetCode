# Lintcode 367//Hard
# Leetcode 1597 Build Binary Expression Tree From Infix Expression//Hard
# 下面给的是Leetcode上的描述，相比Lintcode更加明确


# A binary expression tree is a kind of binary tree used to represent arithmetic expressions.
# Each node of a binary expression tree has either zero or two children.

# Leaf nodes (nodes with 0 children) correspond to operands (numbers),
# and internal nodes (nodes with 2 children) correspond to the operators
# '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

# For each internal node with operator o, the infix expression that it represents is (A o B),
# where A is the expression the left subtree represents and B is the expression the right subtree represents.

# You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

# Return the binary expression tree, which its in-order traversal reproduce s.

# Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first,
# and multiplication and division happen before addition and subtraction.


# Example 1:

# Input: s = "2-3/(5*2)+1"
# Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]


# Example 2:

# Input: s = "3*4-2*5"
# Output: [-,*,*,3,4,2,5]


# Example 3:

# Input: s = "1+2+3+4+5"
# Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]


# Constraints:
#     1 <= s.length <= 105
#     s consists of digits and the characters '+', '-', '*', '/', '(', and ')'.
#     Operands in s are exactly 1 digit.
#     It is guaranteed that s is a valid expression.

# 第一次答案
from typing import (
    List,
)
from lintcode import (
    ExpressionTreeNode,
)

"""
Definition of ExpressionTreeNode:
class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None
"""

class Solution:
    """
    @param expression: A string array
    @return: The root of expression tree
    """
    def getNextValidPos(self, ex: List[str]) -> int:
        valid_pos, idx = -1, 0
        # 错误：乘除取第一次出现作为valid。除法不满足结合律：a/b/c != a/(b/c)
        # 乘除取最后一次出现作为valid，防止连续比的情况
        pm_flag = False
        while idx < len(ex):
            if ex[idx] == '+' or (ex[idx] == '-' and idx > 0 \
                and ex[idx-1] not in ['+', '-', '*', '/']): # 考虑优先级
                valid_pos = idx
                if not pm_flag:
                    pm_flag = True
                idx += 1
            if ex[idx] in ['*', '/'] and not pm_flag: # and valid_pos == -1: 
                valid_pos = idx
                idx += 1
            elif ex[idx] == '(':
                n_left = 1
                idx += 1
                # print(ex)
                while n_left > 0:
                    if ex[idx] == '(':
                        n_left += 1
                    elif ex[idx] == ')':
                        n_left -= 1
                    idx += 1
                    # print(idx, n_left)
            else:
                idx += 1
        return valid_pos

    def build(self, expression: List[str]) -> ExpressionTreeNode:
        # write your code here
        if len(expression) == 0: # Empty
            return None
        if len(expression) == 1: # expression: n
            return ExpressionTreeNode(expression[0])
        if len(expression) == 2 and expression[0] != '(': # expression must be -n
            root = ExpressionTreeNode('-')
            root.left = ExpressionTreeNode(expression[1])
            return root
        # expression = (...)
        # if expression[0] == '(' and expression[-1] == ')':
        # 不能直接这样判断是否是括号里一整个expression，因为比如(3+5)/(-2)就是错的
        next_valid_pos = self.getNextValidPos(expression)
        # print(expression)
        # print('next_valid_pos', next_valid_pos)
        if next_valid_pos == -1: # must be (...)
            return self.build(expression[1:-1])
        root = ExpressionTreeNode(expression[next_valid_pos])
        root.left = self.build(expression[:next_valid_pos])
        root.right = self.build(expression[(next_valid_pos+1):])
        return root
 
# TODO: 标准答案
