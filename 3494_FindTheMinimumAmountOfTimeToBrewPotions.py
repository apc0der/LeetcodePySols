class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        pfix = [0] # base time
        for s in skill:
            pfix.append(pfix[-1]+s)
        curr = [mana[0]*p for p in pfix] # potion zero

        
        for i in range(1, len(mana)): # remaining potions
            base = [mana[i]*x for x in pfix] # calculate base brewing time
            offset = max([curr[i+1]-base[i] for i in range(len(skill))]) # find minimal offset 
            curr = [offset + b for b in base] # this is the next potion
        return curr[-1] # last potion, last time = finish
