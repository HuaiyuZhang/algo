class Solution:
    # The function `is_valid` cannot guarantee the total meets the upper bound `mid`.
    def is_valid(self, nums, m, mid):
        cuts, curr_sum  = 0, 0
        for x in nums:
            if x > mid:
                return False
            curr_sum += x
            if curr_sum > mid:
                cuts, curr_sum = cuts+1, x
        subs = cuts + 1
        return (subs <= m)
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        r = sum(nums)
        ans =  -1
        while l <= r:
            mid = l + int((r-l)/2)
            if self.is_valid(nums, m, mid):
                ans, r = mid, mid -1
            else:
                l = mid + 1
        return ans