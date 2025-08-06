class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # this is just a variation of LCS
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        dp[0][0] = 0
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        lcs = dp[-1][-1] # the number of deletions is each length minus LCS
        return len(word1)+len(word2) - 2*lcs
