class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ret = 0 # return val
        uniq = set(s) # unique end points
        for x in uniq: # for each 
            l, r = s.index(x), s.rindex(x) # find the extreme points
            # we want to capture as many characters in between as possible
            ret += len(set(s[l+1:r])) # return the number of unique m between a pair of x
        return ret
