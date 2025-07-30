class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def check(n): # fast prime checker function
            if n == 1:
                return False
            if n < 4:
                return True
            if n%2 == 0 or n%3 == 0:
                return False
            
            i = 5
            while i**2 <= n:
                if n%i == 0 or n%(i+2) == 0:
                    return False
                i += 6
            return True

        primes = [] # list of primes
        minDiff = 10000000 # running min
        for i in range(left, right+1):
            if check(i): # if prime
                primes.append(i)
                if len(primes) > 1: # if there exists an available difference
                    minDiff = min(minDiff, primes[-1]-primes[-2])
        
        if len(primes) < 2: # if no pairs
            return [-1, -1]
        # return the smallest pair whose difference is the minDiff
        return min([[primes[i], primes[i+1]] for i in range(len(primes)-1) if primes[i+1]-primes[i] == minDiff])
