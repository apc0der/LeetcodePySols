class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = nums[0]-sum(nums[1:]) # first difference
        ret = 0 if s < 0 else 1
        for i in range(1, len(nums)-1): # sliding window
            s += 2*nums[i] # simple difference in the sums
            ret += 0 if s < 0 else 1
        return ret
