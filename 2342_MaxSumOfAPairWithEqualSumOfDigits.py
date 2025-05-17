class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {} # unique sum tracker
        for n in nums:
            k = sum([int(x) for x in list(str(n))])
            if k not in d:
                d[k] = []
            d[k].append(n)
            if len(d[k]) == 3: # keep the best two
                d[k].remove(min(d[k]))
        out = -1
        for k in d.keys():
            if len(d[k]) == 2: # if a pair
                out = max(out, sum(d[k]))
        return out
