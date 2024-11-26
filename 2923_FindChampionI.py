class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        # find the one that beats all others
        # in other words, all 1s except itself
        return [sum(g) for g in grid].index(len(grid)-1)
