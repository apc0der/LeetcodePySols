class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # must be positive, and must have all 1s if decremented
        return n > 0 and n&(n-1) == 0
