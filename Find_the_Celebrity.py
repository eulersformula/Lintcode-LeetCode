# Lintcode 645//Medium//Facebook//LinkedIn
# Leetcode 277//Medium//Premium

# Description
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

# There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

# Example
# Example1

# Input:
# 2 // next n * (n - 1) lines 
# 0 knows 1
# 1 does not know 0
# Output: 1
# Explanation:
# Everyone knows 1,and 1 knows no one.
# Example2

# Input:
# 3 // next n * (n - 1) lines 
# 0 does not know 1
# 0 does not know 2
# 1 knows 0
# 1 does not know 2
# 2 knows 0
# 2 knows 1
# Output: 0
# Explanation:
# Everyone knows 0,and 0 knows no one.
# 0 does not know 1,and 1 knows 0.
# 2 knows everyone,but 1 does not know 2.

"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        # Questions to ask:
        # 1. Is it possible for a person to know himself? Namely is it legit to call Celebrity.knows(a, a)? If so, does it count?
        # According to the test cases, Celebrity.knows(i, i) is always True. No need to check.
        if n == 0:
            return -1
        know_i = [set() for _ in range(n)]
        rule_out = set()
        possible = list(range(n))
        while len(possible) > 0:
            i = possible.pop(0)
            if i in rule_out:
                continue
            for j in range(n): # check if i knows anyone
                if i == j: # 一开始没判定i、j是否相等导致错误
                    continue
                call = Celebrity.knows(i, j)
                if call: # i knows j and cannot be the celebrity
                    rule_out.add(i)
                    know_i[j].add(i)
                    break
                # i doesn't know j; j cannot be the celebrity
                rule_out.add(j)
            # print(i, rule_out, know_i)
            if i in rule_out:
                continue
            cur_know_i = set()
            for j in set(range(n)) - know_i[i] - set([j]):
                call = Celebrity.knows(j, i)
                if not call: # j doesn't know i; i cannot be the celebrity
                    break
                cur_know_i.add(j)
                rule_out.add(j) # j knows i; j cannot be the celebrity
            know_i[i] |= cur_know_i # 一开始set相加写错了，应该是a | b，写成了a + b
            if len(know_i[i]) == n - 1:
                return i
            rule_out.add(i)
        return -1
