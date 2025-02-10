class Solution:
    def clearDigits(self, s: str) -> str:
        ret = "" # build up result
        for x in s:
            if x < '0' or x > '9': # if non digit, add
                ret += x
            else: # if digit
                if ret: # and not the first
                    ret = ret[:-1] # delete the nondigit
        return ret
