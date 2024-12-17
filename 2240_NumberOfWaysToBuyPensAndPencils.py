class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        c1, c2 = max(cost1, cost2), min(cost1, cost2) # want to go thru less iterations
        ret = 0 # accumulator
        for x in range(total//c1+1): # for every num. of high cost
            ret += (total-x*c1)//c2 + 1 # see how many low cost combos
        return ret
