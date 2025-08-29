class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice only wins if n+m is odd
        nE = n // 2 # number of even choices for x
        nO = n - nE # number of odd choices for x
        mE = m // 2 # number of even choices for y
        mO = m - mE # number of odd choices for y

        # return sum of even x, odd y or odd x, even y
        return nE*mO + nO*mE
