class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ret = 0
        m24 = {} # store mods
        for h in hours:
            k = int(h%24) # mod 24
            if k not in m24: # frequency tracker
                m24[k] = 0
            m24[k] += 1
        
        ret = 0
        if 0 in m24: # pairs of 0s
            ret += m24[0]*(m24[0]-1)//2
        if 12 in m24: # pairs of 12s
            ret += m24[12]*(m24[12]-1)//2
        for i in range(1, 12): # any other complement
            if i in m24 and 24-i in m24:
                ret += m24[i]*m24[24-i]
        return ret
