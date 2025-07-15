class Solution:
    def isValid(self, word: str) -> bool:
        digs = set([chr(x) for x in range(48, 58)]) # digits
        lets = set([chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]) # letters
        allow = digs | lets # allowed chars
        vows = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} # vowels
        cons = lets - vows # consonants
        w = set(list(word)) # convert to a set for comparison
        return len(word) >= 3 and w <= allow and len(w & vows) > 0 and len(w & cons) > 0
