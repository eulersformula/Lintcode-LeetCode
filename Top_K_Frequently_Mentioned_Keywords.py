# Lintcode 1883//Medium

# Description
# Given a list of reviews, a list of keywords and an integer k .
# Find out the top k keywords that appear most frequently in different comments, and the K keywords are sorted according to the number of times.
# The comparison of strings is case-insensitive. If the mentioned times of keywords are the same in different reviews, list the keywords in alphabetical order.

# If K is greater than the length of the list keywords, then output keywords directly
# the length of keywords within range: [1, 100]
# the length of reviews within range: [1, 1000]
# keywords [i] consists of lowercase letters
# reviews [i] consists of uppercase and lowercase letters and punctuation: [ "[", "\", "!", "?", ",", ";" , ".", "]", " "]
# Example
# Example 1:
# Input:
# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#   "Anacell provides the best services in the city",
#   "betacellular has awesome services",
#   "Best services provided by anacell, everyone should use anacell",
# ]
# Output:
# ["anacell", "betacellular"]
# Explanation:
# "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
# Example 2:
# Input:
# k = 2
# keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
# reviews = [
#   "I love anacell Best services; Best services provided by anacell",
#   "betacellular has great services",
#   "deltacellular provides much better services than betacellular",
#   "cetracular is worse than anacell",
#   "Betacellular is better than deltacellular.",
# ]
# Output:
# ["betacellular", "anacell"]
# Explanation:
# "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.

from typing import (
    List,
)

class Solution:
    """
    @param k: an integer
    @param keywords: a list of string
    @param reviews: a list of string
    @return: return the top k keywords list
    """
    def topk_keywords(self, k: int, keywords: List[str], reviews: List[str]) -> List[str]:
        # write your code here
        # Questions to ask:
        # 1. How to exactly define a word in the review? For example, are words separted by spaces? Is there any punctuation? Does a punctuation count towards a keyword?
        # 2. Can k be negative? 0? Larger than the number of different keywords? (In the instruction it is mentioned that If K is greater than the length of the list keywords, then output keywords directly)
        # 3. Are keywords all lower-case letters? (In the instruction it is mentioned that keywords [i] consists of lowercase letters)
        # Pay attention to details: the problem asks how many reviews each keyword appears in, not how many times.
        if k == 0:
            return []
        # I did not pay attention to the requirement: If K is greater than the length of the list keywords, then output keywords directly. In the first version I wrote 
        # return sorted(keywords) 
        # The requirement did not ask to sort the keywords in this case. 
        # But the testing data sorted the keywords according to the number of appearance times even when k > len(keywords). 
        # Should the k > len(keywords) case be:
        # if k > len(keywords):
            # return keywords
        keyword_counts = {keyword:0 for keyword in keywords}
        for review in reviews:
            review = review.split()
            cur_keywords = set()
            for word in review:
                word = word.lower()
                if word in keyword_counts:
                    cur_keywords.add(word)
            for word in cur_keywords:
                keyword_counts[word] += 1
        count_to_keywords = dict()
        for (key, val) in keyword_counts.items():
            if val not in count_to_keywords:
                count_to_keywords[val] = []
            count_to_keywords[val].append(key)
        res, n_output = [], 0
        for key in sorted(count_to_keywords.keys())[::-1]:
            for word in sorted(count_to_keywords[key]):
                if n_output >= k:
                    break
                res.append(word)
                n_output += 1
        return res
