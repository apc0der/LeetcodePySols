class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ret = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                # check if same from front and from back (front of reverse!)
                if words[i] == words[j][:len(words[i])] and words[i][::-1] == words[j][::-1][:len(words[i])]:
                    ret += 1
        return ret
