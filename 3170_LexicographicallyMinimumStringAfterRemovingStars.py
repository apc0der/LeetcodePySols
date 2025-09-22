class Solution:
    def clearStars(self, s: str) -> str:
        minheap = [] # sort by smallest lex, then by rightmost index
        starred = set() # ignore stars at the end

        for idx in range(len(s)):
            if s[idx] == '*':
                starred.add(idx) # no stars
                tup = heappop(minheap)
                starred.add(-1*tup[1]) # no deleted chars
            else:
                heappush(minheap, (s[idx], -1*idx)) # ascending lex, descending index

        return "".join([s[x] for x in range(len(s)) if x not in starred])
