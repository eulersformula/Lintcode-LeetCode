# Lintcode 1702//Hard//Google

# Description
# Given a string S, count the number of distinct, non-empty subsequences of S .

# Since the result may be large, return the answer modulo 10^9 + 7.

# S contains only lowercase letters.
# 1 <= S.length <= 2000
# Example
# Example 1:

# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
# Example 2:

# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
# Example 3:

# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

# SOLUTION 1: MLE. T: O(2^n); S: O(2^n)

class Solution:
    """
    @param s: The string s
    @return: The number of distinct, non-empty subsequences of S.
    """
    def distinct_subseq_i_i(self, s: str) -> int:
        # Write your code here
        n_s = len(s)
        if n_s == 1:
            return 1
        combs = set([''])
        for ss in s:
            cur = combs.copy()
            for comb in combs:
                cur.add(comb + ss)
            combs = cur
        # print(combs)
        return (len(combs) - 1) % int(1e9+7) # remove the empty
