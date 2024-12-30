class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        es = [0]*len(edges) # edge scores
        for e in range(len(edges)): # for each edge
            es[edges[e]] += e # append source node value to destination node's score
        return es.index(max(es)) # get first index of the maximum       
