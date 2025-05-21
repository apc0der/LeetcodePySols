class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rz, cz = set(), set() # keep a set, modify all at once after
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    rz.add(i)
                    cz.add(j)
        for r in rz:
            for j in range(len(matrix[0])):
                matrix[r][j] = 0
        for c in cz:
            for i in range(len(matrix)):
                matrix[i][c] = 0
