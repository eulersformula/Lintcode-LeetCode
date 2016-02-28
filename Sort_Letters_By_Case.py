#Given a string which contains only letters. Sort it by lower case first and upper case second.

#Example: For "abAcD", a reasonable answer is "acbAD"

#Challenge: Do it in one-pass and in-place.

class Solution:
    """
    @param chars: The letters array you should sort.
    """
    def sortLetters(self, chars):
        # write your code here
        if chars != None:
            st, ed = 0, len(chars) - 1
            while st < ed:
                while st < ed and 'a' <= chars[st] <= 'z':
                    st += 1
                while st < ed and 'A' <= chars[ed] <= 'Z':
                    ed -= 1
                chars[st], chars[ed] = chars[ed], chars[st]
