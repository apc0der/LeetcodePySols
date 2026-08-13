class WordDictionary:
    def __init__(self):
        self.dictionary = set()

    def addWord(self, word: str) -> None:
        self.dictionary.add(word)

    def search(self, word: str) -> bool:
        if word.count('.') == 0:
            return word in self.dictionary
        elif word.count('.') == 1:
            word = word.split('.')
            for i in range(ord('a'), ord('z') + 1):
                if word[0]+str(chr(i))+word[1] in self.dictionary:
                    return True
            return False
        else:
            word = word.split('.')
            for i in range(ord('a'), ord('z') + 1):
                for j in range(ord('a'), ord('z') + 1):
                    if word[0]+str(chr(i))+word[1]+str(chr(j))+word[2] in self.dictionary:
                        return True
            return False
