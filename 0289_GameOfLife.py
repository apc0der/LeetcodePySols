class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        prev = [b[:] for b in board]
        m = len(board)
        n = len(board[0])
        dirx = [-1, 0, 1]
        diry = [-1, 0, 1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0
                for x in range(3):
                    for y in range(3):
                        if 0 <= i+dirx[x] < m and 0 <= j+diry[y] < n and not (x==1 and y==1):
                            live += prev[i+dirx[x]][j+diry[y]]
                if not prev[i][j] and live==3:
                    board[i][j] = 1
                elif prev[i][j] and (live < 2 or live > 3):
                    board[i][j] = 0
