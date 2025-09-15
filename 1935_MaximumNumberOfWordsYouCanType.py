class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ") # grab each word
        broke = set(list(brokenLetters)) # for set comparison
        res = len(text) # assume all words good
        
        for t in text:
            if len(set(list(t)) & broke) > 0: # if any broken letters
                res -= 1 # one less good word
        return res
