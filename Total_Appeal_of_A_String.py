# Leetcode 2262//Hard

# The appeal of a string is the number of distinct characters found in the string.

# For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
# Given a string s, return the total appeal of all of its substrings.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "abbca"
# Output: 28
# Explanation: The following are the substrings of "abbca":
# - Substrings of length 1: "a", "b", "b", "c", "a" have an appeal of 1, 1, 1, 1, and 1 respectively. The sum is 5.
# - Substrings of length 2: "ab", "bb", "bc", "ca" have an appeal of 2, 1, 2, and 2 respectively. The sum is 7.
# - Substrings of length 3: "abb", "bbc", "bca" have an appeal of 2, 2, and 3 respectively. The sum is 7.
# - Substrings of length 4: "abbc", "bbca" have an appeal of 3 and 3 respectively. The sum is 6.
# - Substrings of length 5: "abbca" has an appeal of 3. The sum is 3.
# The total sum is 5 + 7 + 7 + 6 + 3 = 28.
# Example 2:

# Input: s = "code"
# Output: 20
# Explanation: The following are the substrings of "code":
# - Substrings of length 1: "c", "o", "d", "e" have an appeal of 1, 1, 1, and 1 respectively. The sum is 4.
# - Substrings of length 2: "co", "od", "de" have an appeal of 2, 2, and 2 respectively. The sum is 6.
# - Substrings of length 3: "cod", "ode" have an appeal of 3 and 3 respectively. The sum is 6.
# - Substrings of length 4: "code" has an appeal of 4. The sum is 4.
# The total sum is 4 + 6 + 6 + 4 = 20.
 
# Constraints:

# 1 <= s.length <= 10^5
# s consists of lowercase English letters.

# Solution 1: T: O(n^2); S: O(n^2)
class Solution:
    def appealSum(self, s: str) -> int:
        if len(s) == 0:
            return 0
        chars = []
        res = 0
        for c in s:
            for idx in range(len(chars)):
                chars[idx].add(c)
                res += len(chars[idx])
            chars.append(set([c]))
            res += 1
        return res

# Solution 2: T: O(n); S: O(n)
class Solution:
    def appealSum(self, s: str) -> int:
        char_to_pos = {}
        to_remove = 0
        for (idx, l) in enumerate(s):
            if l not in char_to_pos:
                to_remove += idx * (idx + 1) // 2
            elif char_to_pos[l] < idx - 1:
                    tmp = (idx - char_to_pos[l] - 1) * \
                          (idx - char_to_pos[l])
                    to_remove += tmp // 2
            char_to_pos[l] = idx
        n_s = len(s)
        for v in char_to_pos.values():
            to_remove += ((n_s - v) * (n_s - v - 1)) // 2
        return len(char_to_pos) * n_s * (n_s + 1) // 2 - to_remove
