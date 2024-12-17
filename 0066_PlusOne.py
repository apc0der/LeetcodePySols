class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # simple propagate the 1 and any additions across
        d = digits[::-1] # start with least value digit
        c = 1 # carry and also our starting +1
        i = 0 # index
        while i < len(d): # while still some carrying
            sum = c + d[i] # check the sum w cur index
            if sum == 10: # can only be 10
                d[i] = 0 # this digit is 0
                c = 1 # carry the 1
                i += 1 # check the next index
            else: # or single digit
                d[i] = sum # nothing more
                c = 0 # no carry
                break # so we can stop
        if c == 1: # if carry left over (ex. 99 --> 00)
            d += [1] # we need to add the extra digit
        return d[::-1] # reverse to get original order
