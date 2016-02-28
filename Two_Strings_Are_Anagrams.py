#Write a method anagram(s,t) to decide if two strings are anagrams or not.

#Example:
#Given s="abcd", t="dcab", return true.

#Challenge: O(n) time, O(1) extra space

#Method 1: Sort and compare. Time complexity: O(nlog(n)). Space complexity: O(1).

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if s == None or t == None: #if both are NULL, are they anagrams?
            return False
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False
        sortedS = sorted(s) #str.sort() does not work! string objects cannot be directly sorted.
        sortedT = sorted(t)
        return sortedS == sortedT

#Method 2: Use an array of length 256 to record appearances of each char. Doesn't need to use dict: ord(c) is in range(256)!
#Time complexity: O(n). Space compelxity: O(1).
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if s == None or t == None: #if both are NULL, are they anagrams?
            return False
        lenS = len(s)
        lenT = len(t)
        if lenS != lenT:
            return False
        charCounts = [0] * 256
        for i in xrange(lenS):
            charCounts[ord(s[i])] += 1
            charCounts[ord(t[i])] -= 1
        for ct in charCounts:
            if ct != 0:
                return False
        return True
            


