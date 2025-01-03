class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() # remove whitespace
        neg = False # negative Flag
        if not s: # if nothing, just 0
            return 0
        if not s[:1].isdigit(): # if a nondigit
            if s[0] != '+' and s[0] != '-': # if its not a sign
                return 0
            if s[0] == '-': # if it is a neg. sign
                neg = True
            s = s[1:] # otherwise its a pos. sign
        l, r = 0, 0 # two pointers
        if not s: # if nothing, just 0
            return 0
        while s[l] == '0': # while leading zeroes
            l += 1 # start of parse moves forward
            r += 1 # end of parse = start of parse, for now
            if l == len(s): # if we reach end, just 0
                return 0
        while s[r:r+1].isdigit(): # while we still have digits  
            r += 1 # move the end of parse forward
            if r == len(s): # if we reach end, no more looping
                break
        if l == r: # nothing to read, just 0
            return 0
        ret = int(s[l:r]) # simple conversion
        if neg and ret >= 2147483648: # bounding on neg. side
            return -2147483648
        if not neg and ret >= 2147483647: # bounding on pos. side
            return 2147483647
        return -1*int(s[l:r]) if neg else int(s[l:r]) # regular return
