class Solution:
    def clearStars(self, s: str) -> str:
        minheap = [] # sort by smallest lex, then by rightmost index

        for idx in range(len(s)):
            if s[idx] == '*':
                tup = heappop(minheap)
            else:
                heappush(minheap, (s[idx], -1*idx)) # ascending lex, descending index
        
        minheap.sort(key=lambda c: (-c[1]))
        return "".join([c[0] for c in minheap])
