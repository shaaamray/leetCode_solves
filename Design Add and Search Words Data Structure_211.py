class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        pointer = self.root

        for i in word:
            if i not in pointer.children:
                pointer.children[i] = TrieNode()
            pointer = pointer.children[i]
        pointer.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            pointer = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in pointer.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in pointer.children:
                        return False
                    pointer = pointer.children[c]
            return pointer.word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)