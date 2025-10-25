class Solution:
    def totalMoney(self, n: int) -> int:
        # just math
        fullWeeks = n//7 
        tot = 21*fullWeeks + 7*(fullWeeks*(fullWeeks+1)//2) # math for full weeks
        for i in range(0, n-fullWeeks*7):
            tot += i+fullWeeks+1 # manually add the remainder days
        return tot
