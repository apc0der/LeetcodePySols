class Solution:
    def numDecodings(self, s: str) -> int:
        return self.helper(s) # helper method
    @cache # memo
    def helper(self, s):
        if not s: # if reached end, valid decoding
            return 1
        if int(s[0]) == 0: # no encoding starts with 0, so impossible
            return 0
        if len(s) == 1: # any 1 digit works, no need to go to the other base case
            return 1
        # atp, length is at least 2
        if int(s[0]) == 1: # if first is 1
            if int(s[1]) == 0: # and second is 0
                return self.helper(s[2:]) # only possibility is 10
            # otherwise, you could do 1 or 1X, where X is any digit but 0
            return self.helper(s[1:]) + self.helper(s[2:])
        if int(s[0]) == 2: # if first is 2
            if int(s[1]) == 0: # and second is 0
                return self.helper(s[2:]) # only possibility is 20
            elif int(s[1]) > 6: # if its 2X, where X in [7, 9]
                return self.helper(s[1:]) # only possibility is 2
            # otherwise you could do 2 or 2X, where X in [1, 6]
            return self.helper(s[1:]) + self.helper(s[2:])
        # if it starts with any digit in [3, 9]
        return self.helper(s[1:]) # single digit is only possibility
