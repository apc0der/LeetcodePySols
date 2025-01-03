class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) # two pointers approach
        l, r = 0, len(x)-1
        while l < r: # ignores when l == r
            if x[l] != x[r]: # if not matching
                return False # no palindrome
            l, r = l+1, r-1 # check inside
        return True # loop finishes, palindrome
