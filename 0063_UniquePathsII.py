class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        og = obstacleGrid
        r, c = len(og), len(og[0])
        # tells us how many paths to get from (0, 0) to any (i, j)
        paths = [[0 for _ in range(c)] for _ in range(r)]
        # check how many we can reach by going straight across
        # as soon as obstacle, anything further right also becomes unreachable
        for i in range(c):
            if og[0][i] == 1:
                break
            paths[0][i] = 1
        # same for straight down
        for i in range(r):
            if og[i][0] == 1:
                break
            paths[i][0] = 1
        # note that the number of ways to reach a space is equal to the sum of ways
        # to come from above or the left
        # but is 0 if it is an obstacle
        for i in range(1, r):
            for j in range(1, c):
                if og[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        # number of paths to reach last cell
        return paths[r-1][c-1]
