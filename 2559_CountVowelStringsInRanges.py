class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pfix = [0] # range queries mean use prefix sum
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                pfix.append(pfix[-1]+1) # if starts, ends with vowel
            else:
                pfix.append(pfix[-1])
        ret = []
        for q in queries:
            ret.append(pfix[q[1]+1] - pfix[q[0]])
        return ret
