class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champ = set([i for i in range(n)]) # possible champions
        for e in edges:
            if e[1] in champ:
                champ.remove(e[1]) # remove if it is weaker
        if len(champ) > 1: # if multiple champions
            return -1
        return list(champ)[0]
