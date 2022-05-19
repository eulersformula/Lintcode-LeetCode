# Leetcode 17//Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 
# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Solution 1. Recursion

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_to_letters = dict()
        digit_to_letters['2'] = ['a', 'b', 'c']
        digit_to_letters['3'] = ['d', 'e', 'f']
        digit_to_letters['4'] = ['g', 'h', 'i']
        digit_to_letters['5'] = ['j', 'k', 'l']
        digit_to_letters['6'] = ['m', 'n', 'o']
        digit_to_letters['7'] = ['p', 'q', 'r', 's']
        digit_to_letters['8'] = ['t', 'u', 'v']
        digit_to_letters['9'] = ['w', 'x', 'y', 'z']
        if len(digits) == 1:
            return digit_to_letters[digits]
        combs = self.letterCombinations(digits[1:])
        res = []
        for l in digit_to_letters[digits[0]]:
            res += [l + c for c in combs]
        return res

# Solution 2: DP
# T: O(m^2); S: O(m^2); m is the number of all possible combinations.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_to_letters = dict()
        digit_to_letters['2'] = ['a', 'b', 'c']
        digit_to_letters['3'] = ['d', 'e', 'f']
        digit_to_letters['4'] = ['g', 'h', 'i']
        digit_to_letters['5'] = ['j', 'k', 'l']
        digit_to_letters['6'] = ['m', 'n', 'o']
        digit_to_letters['7'] = ['p', 'q', 'r', 's']
        digit_to_letters['8'] = ['t', 'u', 'v']
        digit_to_letters['9'] = ['w', 'x', 'y', 'z']
        res = ['']
        for d in digits:
            res = [r + l for r in res for l in digit_to_letters[d]]
        return res
      
