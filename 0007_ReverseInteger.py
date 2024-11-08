class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0 # keeps track if negative
        x = abs(x) # value
        xs = str(x)[::-1] # reverse
        xs = (10-len(xs))*"0"+xs # pad for comparison
        if (neg and xs > "2147483648") or (not neg and xs > "2147483647"):
            return 0 # if out of range
        if neg: # if negative
            return -1*int(xs)
        return int(xs)
