class Solution:
    @cache # memo
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2: # if both are empty
            return not s3 # works only if combined is empty
        if not s1: # if s1 is empty
            return s2 == s3 # check if remainder of s2 is s3
        if not s2: # same for s2
            return s1 == s3
        if not s3: # if both are non empty and s3 is empty
            return False
        if s1[0] == s2[0] and s2[0] == s3[0]: # if both match
            # try both ways
            return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
        if s1[0] == s3[0]: # if s1 matches s3
            # cut it down and recurse
            return self.isInterleave(s1[1:], s2, s3[1:])
        if s2[0] == s3[0]: # same for s2 matching s3
            return self.isInterleave(s1, s2[1:], s3[1:])
        # if neither s1 nor s2 match s3, roadblock
        return False
