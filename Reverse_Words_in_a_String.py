#Given an input string, reverse the string word by word.

#For example,
#Given s = "the sky is blue",
#return "blue is sky the".

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
      if s == None:
        return s
      return ' '.join(s.split()[::-1]) #if s.split() will delete all the leading and trailing spaces. Even for an empty list s, s[::-1] still works  
