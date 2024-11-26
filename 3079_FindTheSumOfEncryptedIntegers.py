class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        # replace every digit with its max digit and return the sum
        return sum([int(max(str(i))*len(str(i))) for i in nums])
