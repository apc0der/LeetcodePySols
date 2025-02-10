class Solution:
    def distinctSequences(self, n: int) -> int:
        self.prev = {1: {1, 2, 3, 4, 5, 6}, # allowable next rolls
                     2: {1, 3, 5},          # given key = prev roll
                     3: {1, 2, 4, 5},
                     4: {1, 3, 5},
                     5: {1, 2, 3, 4, 6},
                     6: {1, 5}}
        return self.helper(n, None, None)
    
    @cache
    def helper(self, rolls, p, p2): # rolls left, prev roll, prev prev roll
        sum = 0 # initial sum
        if rolls == 0: # if no rolls left
            return 1 # valid configuration
        if p is None: # if no prev roll aka first roll
            for i in range(1, 7): # all rolls valid
                sum += self.helper(rolls-1, i, None)
                sum %= 1000000007
            return sum
        nxt = set(self.prev[p]) # pull from available next moves (copy set to avoid mutation issues)
        if p in nxt: # remove prev roll
            nxt.remove(p)
        if p2 is not None and p2 in nxt: # remove 2nd prev roll
            nxt.remove(p2)
        for n in nxt: # out of available moves
            sum += self.helper(rolls-1, n, p) # add up total subrolls
            sum %= 1000000007
        return sum
