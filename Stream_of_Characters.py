# Lintcode 1032//Hard

# Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.

# For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.

# Implement the StreamChecker class:

# StreamChecker(String[] words) Initializes the object with the strings array words.
# boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.
 

# Example 1:

# Input
# ["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
# [[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
# Output
# [null, false, false, false, true, false, true, false, false, false, false, false, true]

# Explanation
# StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
# streamChecker.query("a"); // return False
# streamChecker.query("b"); // return False
# streamChecker.query("c"); // return False
# streamChecker.query("d"); // return True, because 'cd' is in the wordlist
# streamChecker.query("e"); // return False
# streamChecker.query("f"); // return True, because 'f' is in the wordlist
# streamChecker.query("g"); // return False
# streamChecker.query("h"); // return False
# streamChecker.query("i"); // return False
# streamChecker.query("j"); // return False
# streamChecker.query("k"); // return False
# streamChecker.query("l"); // return True, because 'kl' is in the wordlist

# Constraints:

# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# words[i] consists of lowercase English letters.
# letter is a lowercase English letter.
# At most 4 * 10^4 calls will be made to query.

# 一开始答案：TLE

from collections import deque

class Node:
    
    def __init__(self, val: str):
        self.is_word = False
        self.val = val
        self.children = dict()


class Trie:
    
    def __init__(self):
        self.root = Node('')
        
    def insert(self, word: str) -> None:
        if word == '' and not self.root.is_word:
            self.root.is_word = True
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.is_word = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.queue = deque([self.trie.root])
        
    def query(self, letter: str) -> bool:
        res = False
        len_queue = len(self.queue)
        for _ in range(len_queue):
            node = self.queue.popleft()
            if letter in node.children:
                node = node.children[letter]
                if node.is_word:
                    res = True
                self.queue.append(node)
        self.queue.append(self.trie.root)
        return res


