class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        r, c = len(g), len(g[0])
        p = [[0 for _ in range(c)] for _ in range(r)]
        p[0][0] = g[0][0]
        # straight across
        for i in range(1, c):
            p[0][i] = p[0][i-1]+g[0][i]
        # straight down
        for i in range(1, r):
            p[i][0] = p[i-1][0]+g[i][0]
        # for each other cell, it is the minimum of the one from above and to the left
        for i in range(1, r):
            for j in range(1, c):
                p[i][j] = g[i][j]+min(p[i-1][j], p[i][j-1])
        return p[-1][-1] # final cell
