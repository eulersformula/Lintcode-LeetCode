# Lintcode 384//Medium//Adobe//Amazon//Yelp//Bloomberg//Yelp
# Leetcode 3//Medium

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

# 第二次方案：T：O(n); S: O(L); L is the length of vocab
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s # 易错点1：返回值不符合要求（一开始写成return s）
        max_len, chars = 1, {s[0]:0}
        for idx in range(1, len_s):
            if s[idx] in chars:
                if len(chars) > max_len:
                    max_len = len(chars)
                cur_chars = list(chars.keys())
                for c in cur_chars:
                    if chars[c] < chars[s[idx]]:
                        del chars[c]
            chars[s[idx]] = idx
        return max(max_len, len(chars)) # 易错点2：没有最后check
        
