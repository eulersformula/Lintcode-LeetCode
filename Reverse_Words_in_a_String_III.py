# Lintcode 1173//Zappos

# Description
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# In the string, each word is separated by single space and there will not be any extra space in the string.

# Example
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# T:O(n); S:O(n)
class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverse_words(self, str: str) -> str:
        # reversed函数只能作用于List。把字符串按每个字符转化成list用list(s)
        return ' '.join([''.join(reversed(list(x))) for x in s.split()])
