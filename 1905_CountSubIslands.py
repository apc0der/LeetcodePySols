class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        g1, g2 = grid1, grid2 # short forms
        r, c = len(g1), len(g1[0]) # dimensions
        v = set() # visited set for cells
        flag = False

        def flood(a, b):
            nonlocal flag
            if -1 < a < r and -1 < b < c and g2[a][b] == 1 and (a, b) not in v:
                v.add((a, b)) # no looping
                if g1[a][b] == 0:
                    flag = False # not a subisland
                flood(a-1, b) # explore
                flood(a, b+1) # in 
                flood(a, b-1) # all 4 
                flood(a+1, b) # directions

        ret = 0
        for i in range(r): # for every row
            for j in range(c): # for every cell
                if g2[i][j] == 1 and (i, j) not in v: # if undiscovered island in g2
                    flag = True
                    flood(i, j)
                    if flag:
                        ret += 1

        return ret
