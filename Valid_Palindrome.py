#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#Example
#"A man, a plan, a canal: Panama" is a palindrome.
#"race a car" is not a palindrome.

#Note
#Have you consider that the string might be empty? This is a good question to ask during an interview.
#For the purpose of this problem, we define empty string as valid palindrome.

#Challenge
#O(n) time without extra memory.

#Method 1: Extra memory is allowed
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        validOrds = range(ord('a'), ord('z') + 1) + range(ord('0'), ord('9') + 1)
        sLower = s.lower()
        sValid = ''.join([lt for lt in sLower if ord(lt) in validOrds])
        return sValid == sValid[::-1] #notice that for a string s, s[::-1] returns the reversed string


#Method 2: Extra memory is not allowed
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        sLower = s.lower()
        st, ed = 0, len(s) - 1
        while st < ed:
          if not ('0' <= sLower[st] <= '9' or 'a' <= sLower[st] <= 'z'):
            st += 1
          elif not ('0' <= sLower[ed] <= '9' or 'a' <= sLower[ed] <= 'z'):
            ed -= 1
          elif sLower[st] == sLower[ed]:
            st += 1
            ed -= 1
          else:
              return False
        return True
            
