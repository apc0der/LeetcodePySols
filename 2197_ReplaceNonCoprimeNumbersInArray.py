class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stk = [nums[0]] # stack guarantees everything behind the top 2 are permanent

        for i in range(1, len(nums)):
            stk.append(nums[i])
            while len(stk) > 1 and math.gcd(stk[-1], stk[-2]) > 1: # we can cascade collapsing into the LCM
                x = stk[-1]*stk[-2] // math.gcd(stk[-1], stk[-2])
                stk.pop()
                stk.pop()
                stk.append(x)

        return stk
