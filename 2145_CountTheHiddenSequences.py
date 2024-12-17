class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        pfix = [0] # build up prefix array
        for d in differences:
            pfix.append(d+pfix[-1])
        pfix.sort() # get the range
        return max(0, (upper-lower) - (pfix[-1]-pfix[0]) + 1) # find how much you can slide the range
