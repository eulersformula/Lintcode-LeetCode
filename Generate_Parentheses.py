#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Example
#Given n = 3, a solution set is:
#"((()))", "(()())", "(())()", "()(())", "()()()"

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
