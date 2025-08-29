class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = [] # ret array

        def eval(nums, ops): # evaluate an expression
            stk = [nums[0]]
            for i in range(1, len(nums)):
                if ops[i-1] == '*':
                    stk[-1] *= nums[i]
                elif ops[i-1] == '-':
                    stk.append(-1*nums[i])
                else:
                    stk.append(nums[i])
            return sum(stk)

        def fill(remain, nums, ops, s):
            if remain == "": # at end
                if eval(nums, ops) == target: # if exp evals properly
                    res.append(s) # good exp
            else:
                if len(nums) > 0 and nums[-1] != 0: # if a number to append to, with no leading zero
                    # then concat
                    fill(remain[1:], nums[:-1]+[nums[-1]*10+int(remain[0])], ops[:], s+remain[0])
                fill(remain[1:], nums+[int(remain[0])], ops+["+"], s+"+"+remain[0]) # add
                fill(remain[1:], nums+[int(remain[0])], ops+["-"], s+"-"+remain[0]) # sub
                fill(remain[1:], nums+[int(remain[0])], ops+["*"], s+"*"+remain[0]) # mult
                
        fill(num[1:], [int(num[0])], [], num[0]) # init
        return res
