class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0: # if only negatives, need the biggest
            return sorted(nums)[-1]
        nums = [k for k in nums if k > -1] # remove negatives
        return sum(set(nums)) # removes all dupes
