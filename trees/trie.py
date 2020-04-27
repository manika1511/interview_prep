class TrieNode():
    def __init__(self, char=None):
        self.char = char
        self.children = []
        self.finish = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            found = False
            for child in curr.children:
                if child.char == c:
                    found = True
                    curr = child
                    break
            if not found:
                new_node = TrieNode(c)
                curr.children.append(new_node)
                curr = new_node

        curr.finish = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root

        for i, c in enumerate(word):
            not_found = True
            for child in curr.children:
                if child.char == c:
                    not_found = False
                    curr = child
                    break
            if not_found:
                return False
        if curr.finish == True:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if self.root.children == []:
            return False
        curr = self.root
        for c in prefix:
            not_found = True
            for child in curr.children:
                if child.char == c:
                    not_found = False
                    curr = child
                    break

            if not_found:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)