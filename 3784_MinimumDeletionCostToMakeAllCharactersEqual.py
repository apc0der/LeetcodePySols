class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        totC = sum(cost) # think of inverting the target -> find the max cost of any one letter to AVOID deletion
        letC = [0]*26 # tracks total cost of each letter
        for x in range(len(s)):
            letC[ord(s[x])-97] += cost[x]
        return totC - max(letC) # the minimum total deletion is just the total minus the maximum that remains
