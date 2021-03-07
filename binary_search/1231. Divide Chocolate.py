class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = 1, int(sum(sweetness) / (K+1))
        
        while l < r:
            mid =  l + (r-l+1)//2
            current_sum = 0 
            cuts = 0
            for sweet in sweetness:
                current_sum += sweet
                
                if current_sum >= mid:
                    cuts += 1
                    current_sum = 0
            # large candidate `mid` will make the cuts small, so search the candidate on the left (not include the current candidate)   
            if cuts > K:
                l = mid
            else:
                r = mid - 1
        return r
                    