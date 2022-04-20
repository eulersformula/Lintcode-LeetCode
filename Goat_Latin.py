# Lintcode 1394//Easy//Facebook

# Description
# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

# The rules of Goat Latin are as follows:

# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.

# For example, the word 'apple' becomes 'applema'.

# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".

# For example, the word "goat" becomes "oatgma".

# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin.

# S contains only uppercase, lowercase and spaces. Exactly one space between each word.
# 1 <= S.length <= 150.
# Example
# Example1

# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# Example2

# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

class Solution:
    """
    @param s: 
    @return: 
    """
    def toGoatLatin(self, s: str) -> str:
        # Questions to ask:
        # 1. More than one spaces to separate the words?
        # 2. Is it possible for a word to not start with a letter? e.g. a number?
        words = s.split()
        vowels = ['a', 'e', 'i', 'o', 'u']
        for (i, word) in enumerate(words):
            if word[0].lower() in vowels: # Attention to both lower case and upper case
                words[i] = word + 'ma'
            else:
                words[i] = word[1:] + word[0] + 'ma'
            words[i] += 'a' * (i + 1)
        return ' '.join(words)
      
# ONE-LINE SOLUTION
