#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#Example
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#Method 1: Keypoint: (1) the first appearace of some right parenthese must have its corresponding left parenthese on its left; (2) use stack to delete last input element

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        if len(s) == 0:
            return True
        leftParentheses = ['(', '[', '{']
        rightParentheses = [')', ']', '}']
        stack = []
        for p in s:
          if p in leftParentheses:
            stack.append(p)
          else:
            if len(stack) == 0:
              return False
            left = stack.pop() #list.pop() returns the last element and delete it in place
            if not (p == ')' and left == '(' or p == ']' and left == '[' or p == '}' and left == '{'):
              return False
        if len(stack) != 0:
          return False
        return True
