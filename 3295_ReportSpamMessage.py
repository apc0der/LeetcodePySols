class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        b = set(bannedWords) & set(message) # get the banned words in the msg
        ct = 0 # number of banned words
        for w in b:
            ct += message.count(w)
            if ct > 1: # if at least 2
                return True
        return False
