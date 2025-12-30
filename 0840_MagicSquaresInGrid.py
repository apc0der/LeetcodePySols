class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        out = 0 # manual check, nothing fancy
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.check(grid, i, j, i+3, j+3):
                    out += 1
        return out
    
    def check(self, grid, sr, sc, er, ec):
        uniq = set()
        for r in range(sr, er):
            for c in range(sc, ec):
                if (grid[r][c] < 1 or grid[r][c] > 9):
                    return False
                uniq.add(grid[r][c])
        if (len(uniq) != 9):
            return False
        for r in range(sr, er):
            sum = 0
            for c in range(sc, ec):
                sum += grid[r][c]
            if sum != 15:
                return False
        for c in range(sc, ec):
            sum = 0
            for r in range(sr, er):
                sum += grid[r][c]
            #print(sum)
            if sum != 15:
                return False
        if grid[sr+1][sc+1] != 5:
            return False
        return True
