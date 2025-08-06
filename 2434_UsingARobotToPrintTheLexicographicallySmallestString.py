class Solution:
    def robotWithString(self, s: str) -> str:
        # t is a stack
        s = list(s)[::-1]
        t = []
        ret = ""
        suffix = [s[0]]
        for x in range(1, len(s)): # running suffix check
            suffix.append(min(suffix[-1], s[x]))

        while len(s) > 0:
            t.append(s.pop())
            # while the top is less than any remaining elements in s, write to the paper...
            while len(t) > 0:
                if len(s) == 0:
                    ret += t.pop()
                # write as many as possible without going over
                else: 
                    if suffix[len(s)-1] >= t[-1]: # no possible smaller character
                        ret += t.pop() # might as well write this one
                    else: # but once no more
                        break # break to get back to adding to t
        return ret
