class TrieNode:
    def __init__(self, val, isWord):
        self.val = val
        self.isWord = isWord
        self.children = {}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("", False)
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                newNode = TrieNode(char, False)
                node.children[char] = newNode
            node = node.children[char]
        node.isWord = True
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            # node should end in the last char
        if node.isWord:
            return True
        else:
            return False

     def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True