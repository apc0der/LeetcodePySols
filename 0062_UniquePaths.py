class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # note that this is just stars and bars
        # we always make m+n-2 moves always
        # we need to choose how many ways we can do n-1 move downs
        # out of these moves
        # aka, (m+n-2)C(n-1)
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)
