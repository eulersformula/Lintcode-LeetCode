# Lintcode 118//Medium

# Description
# Given two strings S and T. Count the number of distinct subsequences of S which equals T.

# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not)

# len(S) <= 200len(S)<=200
# len(T) <= 30len(T)<=30

# Example
# Example 1:

# Input:

# S = "rabbbit"
# T = "rabbit"
# Output:

# 3
# Explanation:

# You could remove any 'b' in S, so there are 3 ways to get T.

# Example 2:

# Input:

# S = "abcd"
# T = ""
# Output:

# 1
# Explanation:

# There is only 1 way to get T - remove all chars in S.

# Challenge
# Do it in O(n^2) time and O(n) memory.

# O(n^2) memory is also acceptable if you do not know how to optimize memory.

# 初次：

class Solution:
    """
    @param s: A string
    @param t: A string
    @return: Count the number of distinct subsequences
    """
    def num_distinct(self, s: str, t: str) -> int:
        # write your code here
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            if s == t:
                return 1
            return False
        if len(t) == 0:
            return 1
        tmp = set()
        res = 0
        for (idx, ss) in enumerate(s):
            print(idx, tmp)
            cur = set()
            if ss == t[0]:
                cur.add((1, (idx,)))
            for c in tmp:
                if c[0] == len(t):
                    res += 1
                    continue
                cur.add(c)
                if ss == t[c[0]]:
                    cur.add((c[0]+1, c[1]+(idx,)))
            tmp = cur
        for c in tmp:
            if c[0] == len(t):
                res += 1
        return res

# 不需要记录具体是哪些位置；只需要记录方法数。T: O(n); S: O(m); n is the number of chars in S; m is the number of chars in T.
class Solution:
    """
    @param s: A string
    @param t: A string
    @return: Count the number of distinct subsequences
    """
    def num_distinct(self, s: str, t: str) -> int:
        # write your code here
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            if s == t:
                return 1
            return 0
        if len(t) == 0:
            return 1
        n_ways = [0] * (len(t))
        char_to_idx = dict()
        for (idx, c) in enumerate(t):
            if c not in char_to_idx:
                char_to_idx[c] = [idx]
            else:
                char_to_idx[c].append(idx)
        for ss in s:
            cur = [x for x in n_ways]
            if ss in char_to_idx:
                for idx in char_to_idx[ss]:
                    if idx == 0:
                        cur[0] += 1
                    else:
                        cur[idx] += n_ways[idx-1]
            n_ways = cur
        return n_ways[-1]
