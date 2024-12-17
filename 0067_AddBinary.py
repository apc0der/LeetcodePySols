class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a # a is the shorter of the two
        a, b = a[::-1], b[::-1]
        a += "0"*(len(b)-len(a)) # pad with extra 0s
        c = 0 # carry
        res = ""
        for i in range(len(b)):
            s = int(a[i]) + int(b[i]) + c
            res += str(int(s%2)) # add the digit
            c = s//2 # take the carry
        if c == 1:
            res += "1" # add extra carry digit
        return res[::-1]
