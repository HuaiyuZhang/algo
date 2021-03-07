class Solution:
    def is_valid(self, weights, D, W):
        cum_sum = 0
        days = 0
        for weight in weights:
            # if weight > W:
            #     return False
            if cum_sum + weight > W:
                days += 1
                cum_sum = weight
            else:
                cum_sum += weight
        return days + 1 <= D
        
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = l + (r - l) // 2
            if self.is_valid(weights, D, mid):
                r = mid
            else:
                l = mid + 1
        return l