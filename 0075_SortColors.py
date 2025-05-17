class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Push all 0s leftward
        for i in range(1, len(nums)):
            if nums[i] == 0:
                j = i
                while j > 0 and nums[j-1] != 0:
                    nums[j], nums[j-1] = nums[j-1], 0
                    j -= 1
        # Push all 2s rightward
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 2:
                j = i
                while j < len(nums)-1 and nums[j+1] != 2:
                    nums[j], nums[j+1] = nums[j+1], 2
                    j += 1
        # Leaves all 1s in the middle
