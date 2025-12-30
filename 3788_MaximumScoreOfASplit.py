class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        pfix = [nums[0]] # pfix sum
        sfix = [nums[-1]] # sfix min
        n = len(nums)

        for i in range(1, n-1): # standard pfix generator
            pfix.append(nums[i] + pfix[-1])

        for i in range(n-2, 0, -1): # this is p normal as well
            sfix.append(min(nums[i], sfix[-1]))
        sfix = sfix[::-1]

        best = pfix[0]-sfix[0] # not much going on here, I can't lie
        for i in range(1, len(pfix)):
            best = max(best, pfix[i]-sfix[i])
        return best
