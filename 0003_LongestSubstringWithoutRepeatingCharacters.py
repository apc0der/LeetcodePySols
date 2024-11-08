class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0 # return value
        if len(s) != 0: # if characters to process
            m = {} # K: character, V: last time seen
            i = 0 # index
            while i != len(s): # iterate through
                if s[i] not in m: # if not seen
                    m[s[i]] = i # mark as seen
                    i += 1 # continue
                else: # if seen
                    # m has only unique, so len(m)
                    # is the maximal substring
                    ret = max(ret, len(m)) 
                    i = m[s[i]]+1 # move i to 1 past last seen
                    m.clear() # clean slate
            # else clause doesn't trigger automatically
            ret = max(ret, len(m)) # one last check
        return ret
