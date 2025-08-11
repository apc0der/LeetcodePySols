class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # we sort and find the sum of the top k numbers
        x = sorted(nums)[::-1][:k][::-1]
        ret = []

        for i in range(len(nums)):
            if len(x) > 0:
                if nums[i] in x:
                    ret.append(nums[i])
                    x.remove(nums[i])
        
        return ret
