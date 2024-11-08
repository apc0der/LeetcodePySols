class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n2i = {} # K: target - nums[i], V: i
        for i in range(len(nums)): # iterate across indices
            # if number is not seen previously as a complement
            if nums[i] not in n2i: 
                # map complement to the current index for future
                n2i[target-nums[i]] = i 
            else: # if it was seen as complement
                # then simply return [complement index, current index]
                return [n2i[nums[i]], i]
