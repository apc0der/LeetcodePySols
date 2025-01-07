class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def k(v):
            return (-1*len(v), v)
        w = sorted(words, key=k) # guarantees later strs can fit inside prev strs
        ct = []
        for i in range(1, len(w)): # longest str cannot be part of anything
            for x in w[:i]:  # for each prev string
                if w[i] in x: # if current string in prev string
                    ct.append(w[i])
                    break
        return ct
