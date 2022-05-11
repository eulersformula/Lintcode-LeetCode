# Lintcode 209//Easy//Google//Amazon//Bloomberg//Google

# Description
# Given a string and find the first unique character in a given string. You can assume that there is at least one unique character in the string.

# Example
# Example 1:
# 	Input: "abaccdeff"
# 	Output:  'b'
	
# 	Explanation:
# 	There is only one 'b' and it is the first one.


# Example 2:
# 	Input: "aabccd"
# 	Output:  'b'
	
# 	Explanation:
# 	'b' is the first one.

# 二次遍历 T: O(n); S: O(|L|)
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def first_uniq_char(self, str: str) -> str:
        # Write your code here
        if len(str) == 0:
            return ''
        freq = dict()
        for (i, c) in enumerate(str):
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        for c in str:
            if freq[c] == 1:
                return c
        return ''
