class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        f = {} # track frequencies
        for c in s: # populate frequency table
            if c not in f:
                f[c] = 0
            f[c] += 1
        def k(val): # we want them in the order of their last index
            return s.rindex(val)
        # get largest frequency chars, they are last to go
        last2go = sorted([x for x in f if f[x] == max(f.values())], key=k)
        return "".join(last2go)
