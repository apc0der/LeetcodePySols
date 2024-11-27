class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dist = [] # least num of hops
        hop = {} # tracks next hop
        ret = [] # output array
        d = deque() # used for propagating changes
        for i in range(n): # initially
            dist.append(i) # all distances are indices
            hop[i] = set()
            if i < n-1: # everything except last
                hop[i].add(i+1) # hops 1 forward
        for q in queries:
            hop[q[0]].add(q[1]) # add new hop
            d.clear() # get ready
            d.append((q[0], dist[q[0]])) # propagate change starting at new hop
            while len(d) != 0: # while changes left to commit
                top = d[0] # get the top tuple out
                d.popleft()
                for h in hop[top[0]]: # propagate change to all next hops
                    if top[1]+1 < dist[h]: # only if change is required
                        dist[h] = top[1]+1 # do we update
                        d.append((h, dist[h])) # and propagate
            ret += [dist[-1]] # update answer array when done
        return ret       
