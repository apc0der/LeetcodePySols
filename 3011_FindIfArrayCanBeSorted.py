class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        sbm = {} # map of numbers to set bits
        for n in nums:
            if n not in sbm: # if a new number
                sbm[n] = n.bit_count() # ease of use method
        
        for i in range(len(nums)): # for every element
            for j in range(i+1, len(nums)): # and for every element after this one
                # if the left is greater than right, it must eventually swap at some pt
                # but cannot happen if set bits do not match
                if nums[i] > nums[j] and sbm[nums[i]] != sbm[nums[j]]:
                    return False
        
        return True
