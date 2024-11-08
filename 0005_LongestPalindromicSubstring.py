class Solution:
    def longestPalindrome(self, s: str) -> str:
        # note that if you cannot pal with n-2 length
        # then you cannot pal with n length
        even = True # keep track of possibility of pal 
        odd = True # for each parity
        x = 2 # start at 2
        ret = s[0] # our worst case result is single letter
        while x < len(s)+1: # for increasing size
            if x % 2 == 0: # if even, set both false (as we check every 2)
                even = False
                odd = False
            else: # if odd, don't clear even
                odd = False
            for i in range(0, len(s)-x+1): # start indices
                if s[i:i+x] == s[i:i+x][::-1]: # check pal
                    ret = s[i:i+x] # store result
                    if x % 2 == 0: # if x is even
                        even = True
                    else: # if x is odd
                        odd = True
                    break
            if x % 2 == 1: # if on odd, and neither even nor odd
                if not even and not odd:
                    break
            x += 1 # increment size
        return ret
