#Given a dictionary, find all of the longest words in the dictionary.

#Given
#{
#  "dog",
#  "google",
#  "facebook",
#  "internationalization",
#  "blabla"
#}
#the longest words are(is) ["internationalization"].
#Given
#{
#  "like",
#  "love",
#  "hate",
#  "yes"
#}
#the longest words are ["like", "love", "hate"].

#Challenge: It's easy to solve it in two passes, can you do it in one pass?

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        if dictionary == None:
            return None
        if len(dictionary) == 0:
            return []
        longest = 0
        words = []
        for word in dictionary:
            lWord = len(word)
            if lWord == longest:
                words.append(word)
            elif lWord > longest:
                words = [word]
                longest = lWord
        return words
