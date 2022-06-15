# Lintcode 257//Leetcode 1048//Medium

# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

# For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.

# Example 1:

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
# Example 2:

# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
# Example 3:

# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 
# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.

# 从前往后
class Solution:
    def isPredecessor(self, w1: str, w2: str) -> bool:
        for idx in range(len(w2)):
            if w2[:idx]+w2[(idx+1):] == w1:
                return True
        return False
    
    def longestStrChain(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1
        words = sorted([(len(word), word) for word in words])
        words = [x[1] for x in words]
        st = 0
        len_pos = dict()
        for idx in range(1, len(words)):
            if len(words[idx]) != len(words[st]):
                len_pos[len(words[st])] = [st, idx-1]
                st = idx
        len_pos[len(words[st])] = [st, len(words)-1]
        tmp = [1] * len(words)
        # print(words, len_pos)
        for idx in range(len(words)):
            cur_len = len(words[idx]) - 1
            if cur_len in len_pos:
                for j in range(len_pos[cur_len][0], len_pos[cur_len][1]+1):
                    if self.isPredecessor(words[j], words[idx]):
                        tmp[idx] = max(tmp[idx], 1+tmp[j])
            # print(tmp)
        return max(tmp)

# 从后往前：最优。T: O(nm); S: O(n)
class Solution:
    """
    @param words: the list of word.
    @return: the length of the longest string chain.
    """
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted([(word, len(word)) for word in words], key=lambda x: -x[1])
        words = [x[0] for x in words]
        word_to_idx = {word:idx for (idx, word) in enumerate(words)}
        dp = [1] * len(words)
        for (idx, word) in enumerate(words):
            for j in range(len(word)):
                tmp = word[:j] + word[(j+1):]
                if tmp in word_to_idx and dp[word_to_idx[tmp]] <= dp[idx]:
                    dp[word_to_idx[tmp]] = dp[idx] + 1
        return max(dp)
