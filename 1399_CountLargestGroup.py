class Solution:
    def countLargestGroup(self, n: int) -> int:
        # track sum frequencies
        sf = [0]*36
        for i in range(1, n+1):
            sf[sum([int(x) for x in str(i)])-1] += 1
        
        return sf.count(max(sf))
