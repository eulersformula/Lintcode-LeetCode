# Lintcode 442//Medium
# Leetcode 208//Medium

#Implement a trie with insert, search, and startsWith methods.
#Notice: You may assume that all inputs are consist of lowercase letters a-z.
#Example:
#insert("lintcode")
#search("code") // return false
#startsWith("lint") // return true
#startsWith("linterror") // return false
#insert("linterror")
#search("lintcode) // return true
#startsWith("linterror") // return true

#It's very important to have isLeaf attribute in TrieNode. Otherwise, you can't know if 'aaa' is in the trie if 'aaaa' is inserted after 'aaa'.
#Not running any corner test on the input string, since the problem says all inputs are consist of lowercase letters a-z.

"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""
class TrieNode:
  def __init__(self):
    # Initialize your data structure here.
    self.children = dict()
    self.isLeaf = False

class Trie:
  def __init__(self):
    self.root = TrieNode()

  # @param {string} word
  # @return {void}
  # Inserts a word into the trie.
  def insert(self, word):
    node = self.root
    for w in word:
        if w not in node.children:
            node.children[w] = TrieNode()
        node = node.children[w]
    node.isLeaf = True
        
  # @param {string} word
  # @return {boolean}
  # Returns if the word is in the trie.
  def search(self, word):
    node = self.root
    for w in word:
        if w not in node.children:
            return False
        node = node.children[w]
    return node.isLeaf

  # @param {string} prefix
  # @return {boolean}
  # Returns if there is any word in the trie
  # that starts with the given prefix.
  def startsWith(self, prefix):
    node = self.root
    for p in prefix:
        if p not in node.children:
            return False
        node = node.children[p]
    return True
 
# 二刷code（Leetcode）
class TreeNode:
    def __init__(self, val=''):
        self.val = val
        self.is_word = False
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = TreeNode() # initialize with empty string as root
        
    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.root.is_word = True
        else:
            idx, node = 0, self.root
            while idx < len(word):
                letter = word[idx]
                if letter not in node.children:
                    node.children[letter] = TreeNode(letter)
                node = node.children[letter]
                if idx == len(word) - 1:
                    node.is_word = True
                idx += 1   

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.root.is_word
        idx, node = 0, self.root
        while idx < len(word):
            letter = word[idx]
            if letter not in node.children:
                return False
            node = node.children[letter]
            if idx == len(word) - 1 and node.is_word:
                return True
            idx += 1
        return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            if len(self.root.children) > 0:
                return True
            return self.root.is_word
        idx, node = 0, self.root
        while idx < len(prefix):
            letter = prefix[idx]
            if letter not in node.children:
                return False
            node = node.children[letter]
            idx += 1
        return True
