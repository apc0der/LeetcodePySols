class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        mat = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))] # will transpose after
        for i in range(len(colSum)): # populate first "row"
            mat[0][i] = colSum[i]
        for r in range(len(mat)): # for each row
            # note: colSum always conserved
            c = len(mat[0])-1
            while sum(mat[r]) != rowSum[r]: # while still diff
                d = sum(mat[r]) - rowSum[r] # find the remaining diff
                if d < mat[r][c]: # if no need to put all the way to 0
                    if r+1 != len(mat):
                        mat[r+1][c] += d # drop only remaining
                    mat[r][c] -= d
                else:
                    if r+1 != len(mat):
                        mat[r+1][c] += mat[r][c] # drop the entire value to 0
                    d -= mat[r][c] # accounted for
                    mat[r][c] = 0 # also accounted for
                    c -= 1 # need to check next column
        return mat
