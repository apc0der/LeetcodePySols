class Solution:
    def minSwaps(self, s: str) -> int:
        stk = deque()
        stk.appendleft(s[0]) # start with first 
        for i in range(1, len(s)): # linear scan
            if len(stk) == 0: # no collapsing possible
                stk.appendleft(s[i])
            elif stk[0] == '[' and s[i] == ']': # we can collapse
                stk.popleft()
            else: # not much else to do
                stk.appendleft(s[i])    
        # atp, guaranteed all ] is left of all [, ct is number of pairs
        return (len(stk)//2+1)//2 # ceiling of number of pairs over 2
