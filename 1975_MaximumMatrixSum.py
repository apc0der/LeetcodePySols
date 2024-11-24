class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # note that the best case is either 1 negative or none
        # in former case, note that transformations just 
        # involve moving the negative sign around
        # if 1 negative, simply put the neg on the smallest number
        smol = 200000 # minimum
        negCt = 0 # flips to keep track of number of negatives
        potential = 0 # possible sum
        for mat in matrix:
            for m in mat:
                if m < 0: # if negative
                    negCt = 1 - negCt
                smol = min(smol, abs(m)) # want smallest abs min
                potential += abs(m) # potential includes all
        if negCt: # if negative
            # potential is rest + min, we want rest - min
            return potential - 2*smol
        # if no negative, potential is best case
        return potential
