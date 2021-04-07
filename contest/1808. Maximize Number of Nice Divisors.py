# Solution 1: DP using array, memory exceed limit
def maxNiceDivisors(self, primeFactors: int) -> int:
        n = primeFactors
        dp = [1] * (n+1)
        # then dp[0] = dp[1] = 1
        for i in range(2, n+1):
            curMax = 0
            for j in range(1, i + 1):
                curMax = max(curMax, j * dp[i-j])
            dp[i] = curMax
        return dp[n] % (10**9+7)

# Solution 2: DP with cache, max recursion  depth exceeded.
def maxNiceDivisors(self, primeFactors: int) -> int:
	
        @functools.lru_cache(None)
        def helper(p):   
            if p == 0:
                return 1
            best = 0
            for i in range(1, p+1):
                best = max(best, i*helper(p-i))
            return best
        
        MOD = 10**9 + 7
        return helper(primeFactors) % MOD

# Solution 3: Math
# This is close to 343.integer split
# make split to get most 3's
import math
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        n = primeFactors
        if n<=4:
            return n
        a, b = n//3, n%3
        mod = 10**9+7
        if b==0:
            return pow(3,a, mod) 
        elif b == 1:
            return (pow(3,a-1, mod) * 4) % mod
        else:
            return (pow(3,a, mod) * 2) % mod