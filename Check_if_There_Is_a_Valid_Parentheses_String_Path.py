# Leetcode 2267//Hard

# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

# The path starts from the upper left cell (0, 0).
# The path ends at the bottom-right cell (m - 1, n - 1).
# The path only ever moves down or right.
# The resulting parentheses string formed by the path is valid.
# Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

# Example 1:

# Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# Output: true
# Explanation: The above diagram shows two possible paths that form valid parentheses strings.
# The first path shown results in the valid parentheses string "()(())".
# The second path shown results in the valid parentheses string "((()))".
# Note that there may be other valid parentheses string paths.
# Example 2:

# Input: grid = [[")",")"],["(","("]]
# Output: false
# Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is either '(' or ')'.

# 尝试DFS：TLE

class Solution:
    def dfs(self, x: int, y: int, grid: List[List[str]], n_left_p: int, remaining: int) -> bool:
        if remaining == 1:
            # print(n_left_p)
            if n_left_p == 1 and grid[x][y] == ')':
                # print('here')
                return True
            return False
        if grid[x][y] == ')':
            if n_left_p == 0:
                return False
            n_left_p -= 1
        else:
            n_left_p += 1
        remaining -= 1
        # print('xy', x, y, n_left_p, remaining)
        if remaining < n_left_p:
            return False
        down_res, right_res = False, False
        if x < len(grid) - 1:
            down_res = self.dfs(x+1, y, grid, n_left_p, remaining)
            if down_res:
                return True # 达到直接退出，不需要进入下个if
        if y < len(grid[0]) - 1:
            right_res = self.dfs(x, y+1, grid, n_left_p, remaining)
            if right_res:
                return True
        return False
            
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        return self.dfs(0, 0, grid, 0, m+n-1)
        
