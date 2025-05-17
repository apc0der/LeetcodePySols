class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Double Kadane's algo - one for global min and one for global max
        cmin, cmax, gmin, gmax = nums[0], nums[0], nums[0], nums[0]

        # iterate across remaining elems.
        for i in range(1, len(nums)):
            cmin = min(nums[i], cmin+nums[i])
            cmax = max(nums[i], cmax+nums[i])
            gmin = min(cmin, gmin)
            gmax = max(cmax, gmax)
        
        return max(abs(gmin), gmax)
