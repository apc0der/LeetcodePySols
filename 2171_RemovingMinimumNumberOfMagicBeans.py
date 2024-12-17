class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        ret = sum(beans) - beans[0]*len(beans) # running min
        cur = ret # current sum, no bag removal
        for i in range(1, len(beans)):
            cur += beans[i-1]*(len(beans)-i+1) # remove the old reduction
            cur -= beans[i]*(len(beans)-i) # add the new reduction
            ret = min(ret, cur)
        return ret
