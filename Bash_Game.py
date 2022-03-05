# Lintcode 1300//Easy

# Description
# You are playing the following game with your friend: There is a pile of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove stones.
# Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones.
# For example, if there are 4 stones, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.


# Example
# Example 1：

# Input：n = 4 
# Output：False
# Explanation：Take 1, 2 or 3 first, the other party will take the last one
# Example 2：

# Input：n = 5 
# Output：True
# Explanation：Take 1 first，Than，we can win the game

# Questions to ask:
# 1. Can n be 0?
# Analysis: The number of stones determines winning or losing. Losing is only when the opponent wins no matter the current player takes 1, 2, or 3.

# SOLUTION 1. RECURSION
class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        # Write your code here
        if n in [1, 2, 3]:
            return True
        if n == 4:
            return False
        return not (self.can_win_bash(n - 1) and self.can_win_bash(n - 2) and self.can_win_bash(n - 3))


# SOLUTION 2. DP
class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        # Write your code here
        if n <= 3:
            return True
        if n == 4:
            return False
        win_lose_arr = [True, True, False]
        for _ in range(n - 4):
            tmp = not (win_lose_arr[0] and win_lose_arr[1] and win_lose_arr[2])
            win_lose_arr[0], win_lose_arr[1], win_lose_arr[2] = win_lose_arr[1], win_lose_arr[2], tmp
        return win_lose_arr[-1]
 
# SOLUTION 3
class Solution:
    """
    @param n: an integer
    @return: whether you can win the game given the number of stones in the heap
    """
    def can_win_bash(self, n: int) -> bool:
        # Write your code here
        if n % 4 == 0:
            return False
        return True

# TAGS: RECURSION, DYNAMIC PROGRAMMING
