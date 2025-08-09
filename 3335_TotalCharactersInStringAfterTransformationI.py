class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freq = [0]*26 # get the frequencies
        for x in s:
            freq[ord(x)-ord('a')] += 1
        
        for i in range(t):
            zs = freq[-1]
            freq = [zs] + freq[:-1] # transformation is just a shift
            freq[1] += zs # plus the prev zs to a and b
        
        return sum(freq)%1000000007
