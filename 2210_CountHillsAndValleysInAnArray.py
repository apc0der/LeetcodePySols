class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        smun = [nums[0]] # remove dupes
        ct = 0 # result
        for i in range(1, len(nums)):
            if nums[i] != smun[-1]: # if its a new number
                smun.append(nums[i]) # add
                if len(smun) > 2: # check if the number before the add its a hill or valley
                    if (smun[-3] < smun[-2] > smun[-1]) or (smun[-3] > smun[-2] < smun[-1]):
                        ct += 1
        return ct
