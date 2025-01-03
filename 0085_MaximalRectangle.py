class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        pfix = [[0 for _ in range(c+1)] for _ in range(r+1)] # 2D Prefix

        all1s = True
        for i in range(1, r+1): # build up the 2D prefix array
            for j in range(1, c+1):
                if matrix[i-1][j-1] == '0':
                    all1s = False
                pfix[i][j] = int(matrix[i-1][j-1]) + pfix[i-1][j] + pfix[i][j-1] - pfix[i-1][j-1]
        
        if all1s: # trivial case
            return r*c

        ret = 0 
        for a in range(0, r): # upper left row
            for b in range(0, c): # upper left column
                lim = c # redundant limit (no column past lim is worth it)
                for x in range (a, r): # bottom right row
                    for y in range(b, lim): # bottom right column
                        s = pfix[a][b] + pfix[x+1][y+1] - pfix[a][y+1] - pfix[x+1][b]
                        if s == (x-a+1)*(y-b+1):
                            ret = max(ret, s)
                        else: # no point in expanding rightward, everything else fails automatically
                            lim = y # this column contains a zero, so its the limit
                            break
        return ret
