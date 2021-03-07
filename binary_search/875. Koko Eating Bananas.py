from math import ceil
class Solution:
    def is_valid(self, piles, h, K):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / K)
        return hours <= h
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            mid = l + (r - l) //2
            if self.is_valid(piles, h, mid):
                r = mid
            else:
                l = mid + 1
            
        return l