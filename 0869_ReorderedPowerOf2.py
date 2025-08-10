class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # reordering means only frequency matters
        n = str(n)
        nfreq = [n.count(str(i)) for i in range(0, 10)]
        
        # so check freqency of n and check frequency of every power of 2
        for i in range(0, 31):
            x = str(2**i)
            # if they match, all good
            if [x.count(str(i)) for i in range(0, 10)] == nfreq:
                return True
        # else return False
        return False
