class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums) # max element
        n = len(nums) # length
        idxs = [i for i in range(n) if nums[i] == m] # grab the indices of the maximum
        nonleft = [idxs[0] if i == 0 else idxs[i] - idxs[i-1] - 1 for i in range(len(idxs))]
        # how much we can "extend" the array leftwards without including another instance of m
        tot = 0
        for i in range(len(idxs)-k+1): # for each leftmost instance of m
            # include ALL subarrays that have at least k instances of m
            tot += (nonleft[i]+1)*(n - idxs[i+k-1])
        return tot
