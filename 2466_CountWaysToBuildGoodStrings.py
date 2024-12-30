class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0]*(high+1) # all the way up till high
        dp[0] = 1 # null string
        dp[zero] += 1 # also handles if zero == one
        dp[one] += 1
        for i in range(min(one, zero)+1, len(dp)):
            dp[i] = dp[i-zero] + dp[i-one] # simple dp
            dp[i] %= 1000000007 # saves time from complex additions
        return sum(dp[low:])%1000000007
