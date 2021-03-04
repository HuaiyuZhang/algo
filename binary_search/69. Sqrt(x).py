class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            mid = l + int((r-l+1)/2)
            sqr = mid * mid
            if  sqr > x:
                r = mid - 1
            else:
                l = mid 
        return l
                