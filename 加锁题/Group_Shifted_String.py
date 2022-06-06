# Leetcode 249//Medium//Google//Uber

# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# Return:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# Note: For the return value, each inner list's elements must follow the lexicographic order.
# Hide Company Tags Google Uber
# Hide Tags Hash Table String
# Hide Similar Problems (M) Group Anagrams

# T: O(C); S: O(C)
def group_shifted_strings(strs: List[str]) -> List[List[str]]:
    n_strs = len(strs)
    if n_strs == 0:
        return []
    grouped_strings = dict()
    base = ord('a')
    for s in strs:
        delta = ord(s[0]) - ord('a')
        tmp = ''
        for l in s:
            if ord(l) - delta < base:
                tmp += (chr(ord(l)-delta+26)) # string没有append method
            else:
                tmp += (chr(ord(l)-delta))
        if tmp not in grouped_strings:
            grouped_strings[tmp] = []
        grouped_strings[tmp].append(s)
    print(grouped_strings)
    res = []
    for ls in grouped_strings.values():
        ls.sort()
        res.append(ls)
    return res

