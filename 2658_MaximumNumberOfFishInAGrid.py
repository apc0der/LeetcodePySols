class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if grid == [[0 for _ in range(C)] for _ in range(R)]:
            return 0
        ret = 0
        vis = set()
        def flood(r, c):
            s = 0
            if 0 <= r < R and 0 <= c < C:
                if (r, c) not in vis and grid[r][c] > 0:
                    vis.add((r, c))
                    s += grid[r][c]
                    s += flood(r-1, c)
                    s += flood(r+1, c)
                    s += flood(r, c-1)
                    s += flood(r, c+1)
                    return s
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ret = max(ret, flood(i, j))
        return ret
