class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        m = {} # DP map
        for c in candidates:
            m[c] = [] # each candidate init has just themselves
            m[c].append([c])
        for i in range(1, target+1):
            if i not in m: # all possible targets should have an entry
                m[i] = []
            for c in [k for k in candidates if k < i]: # for all candidates strictly < i
                for q in m[i-c]: # for any existing entries in i-c (basically 1 candidate step BACK)
                    j = sorted(q+[c]) # tack on that c value
                    if j not in m[i]: # and if its a unique combination
                        m[i] += [j] # append it
        return m[target]
