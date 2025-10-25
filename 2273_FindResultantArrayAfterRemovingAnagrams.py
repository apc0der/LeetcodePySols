class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ret = [words[0]] # will always have the first word

        for i in range(1, len(words)): # every other consecutive word
            if sorted(list(ret[-1])) != sorted(list(words[i])): # if not anagrams
                ret.append(words[i]) # add it to result
        return ret
