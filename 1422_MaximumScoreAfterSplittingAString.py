class Solution:
    def maxScore(self, s: str) -> int:
        l, r = s[:1], s[1:]
        score = l.count('0') + r.count('1') # as defined
        ret = score
        for i in range(1, len(s)-1): # linear scan
            if s[i] == '0': # how score changes in 0 case
                score += 1
            else: # same for 1 case
                score -= 1
            ret = max(ret, score) # running max
        return ret
