class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        x = min(len(s1), len(s2), len(s3)) # at max, this many characters can be in common
        # if we havent hit the bad case and 3 strings are not equal
        while x != 0 and not (s1[:x] == s2[:x] and s3[:x] == s2[:x]):
            x -= 1 # shift down
        if x == 0: # if bad case
            return -1
        return len(s1)+len(s2)+len(s3)-x*3 # total number of deletions
