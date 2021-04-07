class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.lru_cache(None)
        def helper(p):   
            if p == 0 or p==1:
                return 1
            best = 1
            for i in range(1, p):
                best = max(best, max(i*(p-i), i*helper(p-i)))
            return best
        
        return helper(n)