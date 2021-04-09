import bisect
def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)   
        diff=[]
        sum_diff = 0
        for i in range(n):
            curr = abs(nums1[i] - nums2[i])
            sum_diff += curr
            diff.append(curr)
        
        nums1.sort()
        
        res = sum_diff
        for i in range(n):
            # find the closest item in nums2
            closest_idx = bisect.bisect_left(nums1, nums2[i])
            # given this idx, we need to compare its left and right
            if closest_idx > 0:
                # compare left
                res = min(res, sum_diff - diff[i] + abs(nums2[i] - nums1[closest_idx-1]))
            if closest_idx < n:
                # compare right
                res = min(res, sum_diff - diff[i] + abs(nums2[i] - nums1[closest_idx]))
        mod = 10**9+7
        return res%mod