# LeetCode 997//Easy

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
 
# Constraints:

# 1 <= n <= 1000
# 0 <= trust.length <= 104
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n

# T: O(n); S: O(n)
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Questions to ask:
        # 1. Is it possible for trust to have duplicated elements?
        # 2. What is the range of n?
        # 3. For n = 1, is person 1 the judge if trust == []?
        trust_count = [[0, 0] for _ in range(n)] # first element stands for how many people this one trusted, second element stands for how many people trust this one
        for (a, b) in trust:
            trust_count[a-1][0] += 1
            trust_count[b-1][1] += 1
        for i in range(n):
            if trust_count[i][0] == 0 and trust_count[i][1] == n - 1:
                return i + 1
        return -1
