class Solution:
    def numSub(self, s: str) -> int:
        s += '0' # helps with termination
        print(s)
        ct = 0 # counts consec 1s
        ret = 0
        for i in range(len(s)):
            if s[i] == '0' and ct > 0: # add this to the total
                ret += ct*(ct+1)//2
                ret %= 1000000007
                ct = 0
            if s[i] == '1': # just increment 1-streak
                ct += 1
        return ret
