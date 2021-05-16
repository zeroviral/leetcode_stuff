class WordDictionary:

    def __init__(self):
        self.words = defaultdict(set)


    def addWord(self, word: str) -> None:
        self.words[len(word)].add(word)

    def search(self, word: str) -> bool:
        size = len(word)
        for choiceWord in self.words[size]:
            i = 0
            while i < size and (choiceWord[i] == word[i] or word[i] == '.'):
                i += 1
            if i == size:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)