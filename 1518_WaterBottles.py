class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full, empty, tot = numBottles, 0, 0
        while full != 0:
            tot, empty, full = tot+full, empty+full, 0
            full, empty = empty//numExchange, int(empty%numExchange)
        return tot
