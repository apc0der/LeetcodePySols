class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code) # length of array for ease of use
        if k == 0: # no replacement sum, so just 0
            return [0]*n

        l, r = None, None # initialize
        if k < 0: # if summing k leftmost
            l, r = n-abs(k), n-1
        else: # if summing k rightmost
            l, r = 1, k

        s = sum(code[l:r+1]) # first sliding window sum
        out = [s]

        for i in range(1, n): # for each element 
            s -= code[l] # take out left
            l = (l+1)%n # update as needed
            r = (r+1)%n # update as needed
            s += code[r] # add in right
            out.append(s) # new sum for this element

        return out
