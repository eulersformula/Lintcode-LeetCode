#Given a string, find the length of the longest substring without repeating characters.

#Example:
#For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
#For "bbbbb" the longest substring is "b", with the length of 1.

#Challenge: O(n) time.

#Use array to record earliest char appearing time. Refresh starting point when a repeating character is found.
#Time complexity: O(n). Space complexity: O(1)
class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        if s == None or s == '':
            return 0
        letters = [-1] * 256
        st = 0
        maxLen = 0
        for (i, c) in enumerate(s):
            pos = ord(c)
            if letters[pos] >= st: #Mistake 1: repeating condition
                ed = letters[pos]
                maxLen = max(maxLen, i - st)
                st = ed + 1
            letters[pos] = i
        maxLen = max(maxLen, len(s) - st) #Mistake 2: don't forget to check this final stage
        return maxLen
