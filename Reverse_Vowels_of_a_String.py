#Write a function that takes a string as input and reverse only the vowels of a string.

#Example 1:
#Given s = "hello", return "holle".

#Example 2:
#Given s = "leetcode", return "leotcede".

#Note:
#The vowels does not include the letter "y".

#Time Complexity: O(n); Space Complexity: O(n)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        s_vowels = [l for l in s if l.lower() in vowels]
        res = []
        for l in s:
            if l.lower() in vowels:
                res.append(s_vowels.pop(-1))
            else:
                res.append(l)
        return ''.join(res)
