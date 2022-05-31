# Leetcode 22//Medium
# Lintcode 427//Medium//Zenefits//Uber//Google

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

# 二刷
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[], ['()']] # for convenience add a 0 pair res
        for idx in range(2, n+1):
            cur_res = set()
            for config in res[idx-1]:
                cur_res.add('(' + config + ')')
            for j in range(1, idx):
                k = idx - j
                for left_config in res[j]:
                    for right_config in res[k]:
                        cur_res.add(left_config + right_config)
            res.append(list(cur_res))
        return res[n]
# 稍改进（和一刷code一样）
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[''], ['()']] # for convenience add a 0 pair res
        for idx in range(2, n+1):
            cur_res = []
            # how many pairs inside the left first pair
            for j in range(idx):
                for left_config in res[j]:
                    for right_config in res[idx-j-1]:
                        cur_res.append('(' + left_config + ')' + right_config)
            res.append(list(cur_res))
        return res[n]
# DFS
