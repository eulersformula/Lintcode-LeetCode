#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Example
#Given n = 3, a solution set is:
#"((()))", "(()())", "(())()", "()(())", "()()()"

#Method 1: Recursion. Consider the first pair of parenthesis. The problem can be broken up into:
#( i pairs of parentheses inside first pair ) (n - i - 1) pairs of parentheses on the right
#i = 0, 1, ..., n - 1
#Perhaps dynamic programming can be better.

class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        res = []
        for i in xrange(0, n):
            validInside = self.generateParenthesis(i)
            validRight = self.generateParenthesis(n - i - 1)
            for inside in validInside:
                for right in validRight:
                    res.append('(' + inside + ')' + right)
        return res
