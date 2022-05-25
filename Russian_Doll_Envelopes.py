# Leetcode 354//Hard

# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# Constraints:

# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5

# Initial submission
class Solution:
    def helper(self, envelopes: List[Tuple[int]], w: int, h: int) -> int:
        if len(envelopes) == 0:
            return 0
        if len(envelopes) == 1:
            if envelopes[0][0] > w and envelopes[0][1] > h:
                return 1
            return 0
        # find the next suitable envelope
        idx = 0
        while idx < len(envelopes) and (envelopes[idx][0] <= w or envelopes[idx][1] <= h):
            idx += 1
        if idx == len(envelopes): # no more suitable envelope
            return 0
        w_1, h_1 = envelopes[idx]
        return max(1 + self.helper(envelopes[(idx+1):], w_1, h_1), self.helper(envelopes[:idx] + envelopes[:(idx+1)], w, h))
        
        
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = set([(w, h) for (w, h) in envelopes]) # remove redundancy
        envelopes = list(envelopes)
        envelopes.sort(key=lambda x: x[0])
        return self.helper(envelopes, 0, 0)

