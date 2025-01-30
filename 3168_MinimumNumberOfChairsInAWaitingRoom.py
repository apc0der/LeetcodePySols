class Solution:
    def minimumChairs(self, s: str) -> int:
        ct = 0
        ret = 0 # track the max # at any point
        for x in s:
            if x == 'E':
                ct += 1
                ret = max(ret, ct)
            else:
                ct -= 1
        return ret
