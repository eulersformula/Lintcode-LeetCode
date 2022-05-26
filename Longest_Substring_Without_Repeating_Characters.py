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
        # 错误：忘了把前面的字符从dict中抹去
        if len(s) <= 1:
            return len(s)
        st = None
        char_pos = dict()
        max_len = 0
        for (idx, c) in enumerate(s):
            if st is None:
                st = idx
            elif c in char_pos:
                cur_len = idx - st
                if cur_len > max_len:
                    max_len = cur_len
                for cc in s[st:char_pos[c]]: #错误：tmp variable用重复
                    char_pos.pop(cc)
                st = char_pos[c] + 1
            char_pos[c] = idx
        cur_len = len(s) - st
        if cur_len > max_len:
            max_len = cur_len
        return max_len
        
