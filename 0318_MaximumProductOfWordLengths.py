class Solution:
    def maxProduct(self, words: List[str]) -> int:
        w2s = {} # store the set to compare uniqueness
        for w in words:
            # store length for final result
            w2s[w] = (set(list(w)), len(w))
        ret = 0
        for k1 in w2s.keys():
            for k2 in w2s.keys():
                if k1 != k2:
                    # if no common elements
                    if not (w2s[k1][0] & w2s[k2][0]):
                        ret = max(ret, w2s[k1][1]*w2s[k2][1])
        return ret        
