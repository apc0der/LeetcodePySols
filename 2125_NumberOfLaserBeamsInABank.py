class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devs = [b.count('1') for b in bank if b != '0'*len(b)] # get only rows w/ devices and their counts
        return sum([devs[i]*devs[i-1] for i in range(1, len(devs))]) # return pairwise products
