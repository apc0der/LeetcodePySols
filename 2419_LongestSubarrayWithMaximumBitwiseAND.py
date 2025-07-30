class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        largest = max(nums) # this is the only number that matters, every other number decreases the AND
        best, curr = 0, 0
        
        for num in nums:
            if num == largest: # chain of largest number
                curr += 1
            else:
                best = max(best, curr) # log the chain
                curr = 0 # reset
        best = max(best, curr) # in case of trailing chain
        return best
