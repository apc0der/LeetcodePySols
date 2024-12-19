class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # get indices of character with caps on the end
        d = [-1]+[i for i in range(len(s)) if s[i] == c]+[len(s)]
        gaps = [d[i]-d[i-1]-1 for i in range(1, len(d))]
        ret = [] # distances
        for g in range(len(gaps)):
            if g == 0: # for first gap
                ret += [i+1 for i in range(gaps[g])][::-1]
                ret += [0] # for the character
            elif g == len(gaps)-1: # for last gap
                ret += [i+1 for i in range(gaps[g])]
            else: # for every other gap
                l, r = 0, gaps[g]-1
                t = [0]*gaps[g]
                c = 1 # kinda like building up a pyramid
                while l <= r: # set to cur value, move the l, r
                    t[l], t[r] = c, c
                    l, r, c = l+1, r-1, c+1
                ret += t
                ret += [0] # for the character
        return ret
